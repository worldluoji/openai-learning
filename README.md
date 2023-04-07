# OpenAI API learning
OpenAI 就只提供了 Completion 和 Embedding 两个接口，
其中，Completion 可以让模型根据你的输入进行自动续写，Embedding 可以将你输入的文本转化成向量。

## Completion
exapmle1: "1. hello/hello_openai.ipynb"

上面例子调用了 OpenAI 的 Completion 接口，然后向它提了一个需求，也就是为一个我在 1688 上找到的中文商品名称做三件事情。
- 为这个商品写一个适合在亚马逊上使用的英文标题。
- 给这个商品写 5 个卖点。
- 估计一下，这个商品在美国卖多少钱比较合适。

同时，我们告诉 OpenAI，我们希望返回的结果是 JSON 格式的，并且上面的三个事情用 title、selling_points 和 price_range 三个字段返回。

## Embedding
通过大语言模型来进行情感分析，最简单的方式就是利用它提供的 Embedding 这个 API。
这个 API 可以把任何你指定的一段文本，变成一个大语言模型下的向量，也就是用一组固定长度的参数来代表任何一段文本。

example1: -> "2. sentiment analysis/comment_analysis.ipynb"

这个例子中，对于任何一段文本评论，我们都可以通过 API 拿到它的 Embedding。
那么，把这段文本的 Embedding 和“好评”以及“差评”通过余弦距离（Cosine Similarity）计算出它的相似度。
然后拿这个 Embedding 和“好评”之间的相似度，去减去和“差评”之间的相似度，就会得到一个分数。

如果这个分数大于 0，那么说明我们的评论和“好评”的距离更近，我们就可以判断它为好评。
如果这个分数小于 0，那么就是离差评更近，我们就可以判断它为差评。