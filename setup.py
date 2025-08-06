from setuptools import find_packages, setup

setup(
    name="e-commerce-bot",
    version="0.1",
    author="Soumadeep Das",
    author_email="soumadeep154@gmail.com",
    description="A customer support system bot, for e-commerce using RAG pipeline with AstraDB",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "langchain_core",
        "langchain_astradb",
        "python-dotenv",
        "langchain" 
    ],
)