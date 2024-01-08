from profiles_rudderstack.project import WhtProject
from .llm_prompt_response import LLMPromptResponseModel

def register_extensions(project: WhtProject):
    project.register_model_type(LLMPromptResponseModel)
