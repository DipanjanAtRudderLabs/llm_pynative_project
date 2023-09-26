from profiles_rudderstack.model import BaseModelType
from profiles_rudderstack.contract import build_contract
from profiles_rudderstack.recipe import PyNativeRecipe
from profiles_rudderstack.material import WhtMaterial
from profiles_rudderstack.logger import Logger
from typing import List

class CommonColumnUnionModel(BaseModelType):
    TypeName = "common_column_union"
    BuildSpecSchema = {
        "type": "object",
        "properties": {
            "inputs": { "type": "array", "items": { "type": "string" } },            
        },
        "required": ["inputs"],
        "additionalProperties": False
    }

    def __init__(self, build_spec: dict, schema_version: int, pb_version: str) -> None:
        super().__init__(build_spec, schema_version, pb_version)

    def get_material_recipe(self)-> PyNativeRecipe:
        return CommonColumnUnionRecipe(self.build_spec["inputs"])

    def validate(self):
        # Model Validate
        if self.build_spec.get("inputs") is None or len(self.build_spec["inputs"]) == 0:
            return False, "inputs are required"
        
        return super().validate()


class CommonColumnUnionRecipe(PyNativeRecipe):
    def __init__(self, inputs: List[str]) -> None:
        self.inputs = inputs
        self.logger = Logger("CommonColumnUnionRecipe")

    def describe(self, this: WhtMaterial):
        material_name = this.name()
        return f"""Material - {material_name}\nInputs: {self.inputs}""", ".txt"

    def prepare(self, this: WhtMaterial):
        for in_model in self.inputs:
            contract = build_contract('{ "is_event_stream": true, "with_columns":[{"name":"num"}] }')
            this.de_ref(in_model, contract)

    def execute(self, this: WhtMaterial):
        self.logger.info("Executing CommonColumnUnionRecipe")
        tables = []
        common_columns_count = {}
        for in_model in self.inputs:
            input_material = this.de_ref(in_model)
            tables.append(input_material.name())
            query = "show columns in table " + input_material.name()
            self.logger.info(f"Executing query: {query}")
            columns = input_material.get_table_data().columns
            columns = columns.map(lambda x: {"name": x, "type": "string"})
            # columns = input_material.get_columns()
            for col in columns:
                key = (col["name"], col["type"])
                if key in common_columns_count:
                    common_columns_count[key] += 1
                else:
                    common_columns_count[key] = 1
        
        common_columns = [name for (name, _), count in common_columns_count.items() if count == len(self.inputs)]

        if len(common_columns) > 0:
            select_columns = ', '.join([f'{column}' for column in common_columns])
            union_queries = []
            for table in tables:
                union_queries.append(f"SELECT {select_columns} FROM {table}")
            
            union_sql = " UNION ALL ".join(union_queries)

            this.wht_ctx.client.query_template_without_result(
                "{% macro selector_sql() %}" + 
                union_sql + 
                "{% endmacro %}" + 
                """{% exec %}{{ warehouse.CreateReplaceTableAs(this.Name(), selector_sql()) }}{% endexec %}"""
            )
        
