
import openai, os
from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader

openai.api_key = os.environ.get("OPENAI_API_KEY")

TARGET_PATH = './index_tyxs.json'

if os.path.exists(TARGET_PATH) == False:
    documents = SimpleDirectoryReader('./articles').load_data()
    # 它会把文档分段转换成一个个向量，然后存储成一个索引。
    index = GPTSimpleVectorIndex.from_documents(documents)
    # 把对应的索引存下来，存储的结果就是一个 json 文件。后面，我们就可以用这个索引来进行相应的问答。
    index.save_to_disk(TARGET_PATH)

index = GPTSimpleVectorIndex.load_from_disk(TARGET_PATH)

# 调用 Query 函数，就能够获得问题的答案
response = index.query("鲁迅先生在日本学习医学的老师是谁？")
print(response)

response = index.query("鲁迅先生是去哪里学的医学？", verbose=True)
print(response)