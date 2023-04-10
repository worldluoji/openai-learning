# OpenAI API learning
OpenAI 就只提供了 Completion 和 Embedding 两个接口，
其中，Completion 可以让模型根据你的输入进行自动续写，Embedding 可以将你输入的文本转化成向量。

## preparation
1. 更新pip
```
python3 -m pip install --upgrade pip
```
2. 设置pip镜像(optional)
```
pip3 config set global.index-url https://mirrors.aliyun.com/pypi/simple
```
3. 安装依赖
```
pip3 install -r requirements.txt
```
The requirements.txt was created by command "pip3 freeze > requirements.txt"

<br>

## Completion
Completion 这个接口里面的参数:
1. 第一个参数是 engine，也就是我们使用的是 Open AI 的哪一个引擎，这里我们使用的是 text-davinci-003，也就是现在可以使用到的最擅长根据你的指令输出内容的模型。当然，也是调用成本最高的模型。
2. 第二个参数是 prompt，是我们输入的提示语。
3. 第三个参数是 max_tokens，也就是调用生成的内容允许的最大 token 数量。你可以简单地把 token 理解成一个单词。有时候，一个单词会被分解成两个 token。比如，icecream 是一个单词，但是实际在大语言模型里，会被拆分成 ice 和 cream 两个 token。这里用的 text-davinci-003 模型，允许最多有 4096 个 token。
4. 第四个参数 n，代表你希望 AI 给你生成几条内容供你选择。在这样自动生成客服内容的场景里，我们当然设置成 1。但是如果在一些辅助写作的场景里，你可以设置成 3 或者更多，供用户在多个结果里面自己选择自己想要的。
5. 第五个参数 stop，代表你希望模型输出的内容在遇到什么内容的时候就停下来。这个参数我们常常会选用 "\n\n"这样的连续换行，因为这通常意味着文章已经要另起一个新的段落了，既会消耗大量的 token 数量，又可能没有必要
### example1: "1. hello/hello_openai.py"

上面例子调用了 OpenAI 的 Completion 接口，然后向它提了一个需求，也就是为一个我在 1688 上找到的中文商品名称做三件事情。
- 为这个商品写一个适合在亚马逊上使用的英文标题。
- 给这个商品写 5 个卖点。
- 估计一下，这个商品在美国卖多少钱比较合适。

同时，我们告诉 OpenAI，我们希望返回的结果是 JSON 格式的，并且上面的三个事情用 title、selling_points 和 price_range 三个字段返回。

### example2: "3. chat robot/prompt.py"
相同的提示语，连续调用两次之后，给到了含义相同、遣词造句不同的结果。

每次回复的内容不一样，则归功于我们使用的一个参数 temperature。这个参数的输入范围是 0-2 之间的浮点数，代表输出结果的随机性或者说多样性。在这里，我们选择了 1.0，也就是还是让每次生成的内容都有些不一样。你也可以把这个参数设置为 0，这样，每次输出的结果的随机性就会比较小。

这个参数该怎么设置，取决于实际使用的场景。如果对应的场景比较严肃，不希望出现差错，那么设得低一点比较合适，比如银行客服的场景。如果场景没那么严肃，有趣更加重要，比如讲笑话的机器人，那么就可以设置得高一些。

### example3: "3. chat robot/food_chatbot.py"
GPT 的模型，要完成支持多轮的问答也并不复杂。

我们只需要在提示语里，在问题之前加上 “Q :” 表示这是一个问题，然后另起一行，加上 “A :” 表示我想要一个回答，那么 Completion 的接口就会回答你在 “Q : ” 里面跟的问题。

要完成多轮对话其实也不麻烦，只要把之前对话的内容也都放到提示语里面，把整个上下文都提供给 AI。AI 就能够自动根据上下文，回答第二个问题。比如：
```
question =  """
Q : 鱼香肉丝怎么做？
A : 
1.准备好食材：500克猪里脊肉，2个青椒，2个红椒，1个洋葱，2勺蒜蓉，3勺白糖，适量料酒，半勺盐，2勺生抽，2勺酱油，2勺醋，少许花椒粉，半勺老抽，适量水淀粉。
2.将猪里脊肉洗净，沥干水分，放入料酒、盐，抓捏抓匀，腌制20分钟。
3.将青红椒洗净，切成丝，洋葱洗净，切成葱花，蒜末拌入小苏打水中腌制。
4.将猪里脊肉切成丝，放入锅中，加入洋葱，炒制至断生，加入青红椒，炒匀，加入腌制好的蒜末，炒制至断生。
5.将白糖、生抽、酱油、醋、花椒粉、老抽、水淀粉倒入锅中，翻炒匀，用小火收汁，调味即可。

Q : 那蚝油牛肉呢？
A : 
"""
print(get_response(question))
```
想要退出的时候，就在需要提问的时候，输入 “bye” 就好了。

### example4: "2. sentiment analysis/good_or_bad.py""
这个“给一个任务描述、给少数几个例子、给需要解决的问题”这样三个步骤的组合，也是大语言模型里使用提示语的常见套路。一般我们称之为 Few-Shots Learning（少样本学习），也就是给一个或者少数几个例子，AI 就能够举一反三，回答我们的问题。

<br>

## Embedding
通过大语言模型来进行情感分析，最简单的方式就是利用它提供的 Embedding 这个 API。
这个 API 可以把任何你指定的一段文本，变成一个大语言模型下的向量，也就是用一组固定长度的参数来代表任何一段文本。

### example1: -> "2. sentiment analysis/comment_analysis.py"

这个例子中，对于任何一段文本评论，我们都可以通过 API 拿到它的 Embedding。
那么，把这段文本的 Embedding 和“好评”以及“差评”通过余弦距离（Cosine Similarity）计算出它的相似度。
然后拿这个 Embedding 和“好评”之间的相似度，去减去和“差评”之间的相似度，就会得到一个分数。

如果这个分数大于 0，那么说明我们的评论和“好评”的距离更近，我们就可以判断它为好评。
如果这个分数小于 0，那么就是离差评更近，我们就可以判断它为差评。

### 准确地预测出具体的分数
我们把 5 个不同的分数分成了正面、负面和中性，还去掉了相对难以判断的“中性”评价，这样我们判断的准确率高的确是比较好实现的。
但如果我们想要准确地预测出具体的分数呢？

最简单的办法就是利用我们拿到的文本 Embedding 的向量。
这一次，我们不直接用向量之间的距离，而是使用<strong>传统的机器学习的方法</strong>来进行分类。
毕竟，如果只是用向量之间的距离作为衡量标准，就没办法最大化地利用已经标注好的分数信息了。

数据集通过 datas/get_dataset_food.py获取，或者直接从 
```
https://raw.githubusercontent.com/xuwenhao/geektime-ai-course/main/data/fine_food_reviews_with_embeddings_1k.csv
```
下载

### example2: -> "2. sentiment analysis/classification_using_embeddings.py
通过embedding进行分类示例。
In this text classification task, we predict the score of a food review (1 to 5) based on the embedding of the review's text. 

reference: https://github.com/openai/openai-cookbook/blob/main/examples/Classification_using_embeddings.ipynb


## ChatCompletion
在 3 月 2 日，因为 ChatGPT 的火热，OpenAI 放出了一个直接可以进行对话聊天的接口。
这个接口叫做 ChatCompletion，对应的模型叫做 gpt-3.5-turbo，不但用起来更容易了，速度还快，
而且价格也是我们之前使用的 text-davinci-003 的十分之一，可谓是物美价廉了。
```
import openai
openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```
Prompt 变成了一个数组，数组的每个元素都有 role 和 content 两个字段。
- role 这个字段一共有三个角色可以选择，其中 system 代表系统，user 代表用户，而 assistant 则代表 AI 的回答。
- 当 role 是 system 的时候，content 里面的内容代表我们给 AI 的一个指令，也就是告诉 AI 应该怎么回答用户的问题。比如我们希望 AI 都通过中文回答，我们就可以在 content 里面写“你是一个只会用中文回答问题的助理”，这样即使用户问的问题都是英文的，AI 的回复也都会是中文的。
- 当 role 是 user 或者 assistant 的时候，content 里面的内容就代表用户和 AI 对话的内容。

example3: -> "3. chat robot/conversation.py"

值得注意的是，即使 ChatGPT 的接口是把对话分成了一个message数组，但是实际上，最终发送给模型的还是拼接到一起的字符串。
OpenAI 在它的 Python 库里面提供了一个叫做 ChatML 的格式，其实就是 ChatGPT 的 API 的底层实现。
OpenAI 实际做的，就是根据一个定义好特定分隔符的格式，将你提供的多轮对话的内容拼接在一起，提交给 gpt-3.5-turbo 这个模型。

OpenAI 是通过模型处理的 Token 数量来收费的，但是要注意，这个收费是“双向收费”。
它是按照你发送给它的上下文，加上它返回给你的内容的总 Token 数来计算花费的 Token 数量的。