
import torch
from PIL import Image
from IPython.display import display
from IPython.display import Image as IPyImage
from transformers import CLIPProcessor, CLIPModel

# 通过 Transformers 库的 CLIPModel 和 CLIPProcessor，加载了 clip-vit-base-patch32 这个模型，用来处理我们的图片和文本信息。
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# CLIPProcessor 对图片做预处理，变成一系列的数值特征表示的向量。这个预处理的过程，其实就是把原始的图片，变成一个个像素的 RGB 值；然后统一图片的尺寸，以及对于不规则的图片截取中间正方形的部分，最后做一下数值的归一化
# 再通过 CLIPModel，把上面的数值向量，推断成一个表达了图片含义的张量（Tensor）。把它当成是一个向量就好了。
def get_image_feature(filename: str):
    image = Image.open(filename).convert("RGB")
    processed = processor(images=image, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        image_features = model.get_image_features(pixel_values=processed["pixel_values"])
    return image_features

# 先把对应的文本通过 CLIPProcessor 转换成 Token，然后再通过模型推断出表示文本的张量。
def get_text_feature(text: str):
    processed = processor(text=text, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        text_features = model.get_text_features(processed['input_ids'])
    return text_features

def cosine_similarity(tensor1, tensor2):
    tensor1_normalized = tensor1 / tensor1.norm(dim=-1, keepdim=True)
    tensor2_normalized = tensor2 / tensor2.norm(dim=-1, keepdim=True)
    return (tensor1_normalized * tensor2_normalized).sum(dim=-1)

# 计算两个张量之间的余弦相似度
image_tensor = get_image_feature("./data/animal.jpeg")

cat_text = "This is a cat."
cat_text_tensor = get_text_feature(cat_text)

dog_text = "This is a dog."
dog_text_tensor = get_text_feature(dog_text)

display(IPyImage(filename='./data/animal.jpeg'))

print("Similarity with cat : ", cosine_similarity(image_tensor, cat_text_tensor))
print("Similarity with dog : ", cosine_similarity(image_tensor, dog_text_tensor))