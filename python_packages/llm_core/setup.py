from setuptools import setup

setup(
    name='rudderstack_predictions_llm_core',
    version='0.0.1',
    author='Dipanjan Biswas',
    author_email='dipanjan@rudderstack.com',
    description='A py_native model package for generic LLM invocations',
    packages=['rudderstack_predictions_llm_core'],
    install_requires=[
        'langchain',
        'pandas',
        'openai',
        'langchain-google-genai',
        'boto3',
        'awscli',
        'botocore'
    ],
)
