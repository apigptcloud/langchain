# flake8: noqa
from langchain.prompts.prompt import PromptTemplate

_template = """给定下面的对话和一个后续问题，将后续问题改写成一个独立的问题。

聊天记录:
{chat_history}
后续问题: {question}
独立问题:"""
CONDENSE_QUESTION_PROMPT = PromptTemplate.from_template(_template)

prompt_template = """利用以下的上下文回答结尾的问题。如果你不知道答案，就说不知道，不要试图编造答案。

{context}

问题: {question}
有用的答案:"""
QA_PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
)
