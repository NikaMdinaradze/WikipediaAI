from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAI

llm = OpenAI()


def map_reduce_summarization(article: str) -> str:
    """
    Generate a summary of the given article using map-reduce summarization.
    """

    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n"], chunk_size=10000, chunk_overlap=500
    )
    docs = text_splitter.create_documents([article])
    summarization_chain = load_summarize_chain(
        llm=llm, chain_type="map_reduce", verbose=True
    )
    output = summarization_chain.run(docs)
    return output
