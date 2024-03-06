from dotenv import load_dotenv
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAI

load_dotenv("../.env")

llm = OpenAI()


def map_reduce_summarization(article):
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n"], chunk_size=10000, chunk_overlap=500
    )
    docs = text_splitter.create_documents([article])
    summarization_chain = load_summarize_chain(
        llm=llm, chain_type="map_reduce", verbose=True
    )
    output = summarization_chain.run(docs)
    return output
