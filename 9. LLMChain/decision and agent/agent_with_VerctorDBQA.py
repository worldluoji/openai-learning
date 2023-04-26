
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import SpacyTextSplitter,CharacterTextSplitter
from langchain import OpenAI, VectorDBQA
from langchain.document_loaders import TextLoader,CSVLoader
from langchain.agents import initialize_agent, Tool

llm = OpenAI(temperature=0)
loader = TextLoader('../data/ecommerce_faq.txt')
documents = loader.load()
text_splitter = SpacyTextSplitter(chunk_size=256, pipeline="zh_core_web_sm")
texts = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()
docsearch = FAISS.from_documents(texts, embeddings)

faq_chain = VectorDBQA.from_chain_type(llm=llm, vectorstore=docsearch, verbose=True)

from langchain.agents import tool

# 我们通过 @tool 这个 Python 的 decorator 功能，将 FAQ 这个函数直接变成了 Tool 对象，这可以减少我们每次创建 Tools 的时候都要指定 name 和 description 的工作。
@tool("FAQ")
def faq(intput: str) -> str:
    """"useful for when you need to answer questions about shopping policies, like return policy, shipping policy, etc."""
    return faq_chain.run(intput)

# 对于商品推荐，我们可以如法炮制，也把对应的信息，存到 VectorStore 里，然后通过先搜索后问答的方式来解决
product_loader = CSVLoader('../data/ecommerce_products.csv')
product_documents = product_loader.load()
product_text_splitter = CharacterTextSplitter(chunk_size=1024, separator="\n")
product_texts = product_text_splitter.split_documents(product_documents)
product_search = FAISS.from_documents(product_texts, OpenAIEmbeddings())
product_chain = VectorDBQA.from_chain_type(llm=llm, vectorstore=product_search, verbose=True)

def recommend_product(input: str) -> str:
    """"useful for when you need to search and recommend products and recommend it to the user"""
    return product_chain.run(input)

def search_order(input: str) -> str:
    return "订单状态：已发货；发货日期：2023-01-01；预计送达时间：2023-01-10"

tools = [
    Tool(
        name = "Search Order",func=search_order, 
        description="useful for when you need to answer questions about customers orders"
    ),
    Tool(name="Recommend Product", func=recommend_product, 
         description="useful for when you need to answer questions about product recommendations"
    ),
    faq
]

agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)


question = "请问你们的货，能送到三亚吗？大概需要几天？"
result = agent.run(question)
print(result)

question = "我想买一件衣服，想要在春天去公园穿，但是不知道哪个款式好看，你能帮我推荐一下吗？"
answer = agent.run(question)
print(answer)