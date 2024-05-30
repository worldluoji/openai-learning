# Civitai and Hugging Face
除了我们经常听到的 Stable Diffusion 1.4、1.5、2.0 这样的模型，我们在开源社区中还能找到成千上万的有趣模型，为我们所用。

Civitai 和 Hugging Face 是 AI 绘画领域两个非常重要的开源社区。它们吸引了来自全球各地的网友们参与其中。
这些社区成为了一个宝藏般的资源库，提供了大量且多样的风格模型。
通过这些社区，人们可以相互交流、分享和发现新的 AI 绘画技巧，不断推动 AI 绘画领域的发展。

<br>

## Hugging Face
对于 Hugging Face，你需要先注册官方账号并安装 diffusers 库，这样你就可以使用社区中提供的各种模型。
以 SD1.5 模型为例，你调用相关的 API 即可用它完成图像生成任务，脚本如下。
```
from diffusers import StableDiffusionPipeline
import torch

model_id = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

prompt = "a photo of an astronaut riding a horse on mars"
image = pipe(prompt).images[0]  
    
image.save("astronaut_rides_horse.png")
```
大多数情况下，模型的更换就是更换 “model_id”。
但如果我们希望有良好的界面管理，而且希望联合使用多种能力的话，WebUI 配合 Civitai 或许是你最佳的选择。
通过界面上的选项，就能选择不同的模型和参数设置，实现定制化的 AI 绘图。

几个推荐模型：
- ToonYou，可以生成很好看的美漫风格。
- CounterFeit，可以生成比较精美的漫画形象。
- 人造人模型，可以生成类似证件照风格的照片效果。

<br>

## Civitai
在使用 Civitai 网站时，很重要的一步是找到并且选择适合自己的模型。
你需要仔细查看模型的类型和使用方式，以确保正确地安装和配置模型，这样 WebUI 才能顺利调用它。


## Midjourney：风头无两的画师
Midjourney 也是 AI 绘画的一大杀器。不同于 WebUI，我们可以在聊天应用程序 Discord 中使用 Midjourney，
不需要本地 GPU 资源，也不需要安装任务 WebUI 类的工具。

相比前面的两个开源社区，Midjourney 模型 AI 绘画的效果在精致度、图像文本关联性上都有更显著的优势,但是Midjourney收费。

Midjourney 描述词 1，创作一幅温馨真挚微笑的年轻亚洲女孩的写实肖像画。
```
Create a realistic portrait of a young asian girl with a warm, genuine smile --ar 2:3Midjourney 
```
描述词 2，我们要求图像里避免出现眼镜和卷发，而且对写实、年轻和微笑都设置了不同的文本权重。
```
Create a realistic::-1.0 portrait of a young::1.5 asian girl with a warm, genuine smile::1.4 --no glasses curly hair --ar 2:3
```