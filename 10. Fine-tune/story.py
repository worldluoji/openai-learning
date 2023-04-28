
import os,openai,backoff
import pandas as pd

openai.api_key = os.getenv("OPENAI_API_KEY")
dynasties= ['唐', '宋', '元', '明', '清', '汉', '魏', '晋', '南北朝']
super_powers = ['隐形', '飞行', '读心术', '瞬间移动', '不死之身', '喷火']
story_types = ['轻松', '努力', '艰难']

@backoff.on_exception(backoff.expo, openai.error.RateLimitError)
def gpt35(prompt, max_tokens=2048, temperature=0.5, top_p=1, frequency_penalty=0, presence_penalty=0):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty)
    return response["choices"][0]["text"]


# 我们定义了一系列朝代、超能力和故事的类型。然后通过三重循环，让 AI 根据这三者的组合来生成一系列故事。这些生成出来的故事，也就构成了我们用来微调模型的训练数据。
# 因为数据量不大，我就直接用 CSV 把它存下来了。在这个过程中，数据是一条条生成的，比较慢，也比较消耗 Token
def prepare_stories(dynasties, super_powers, story_types, output_file="data/ultraman_stories.csv"):
    df = pd.DataFrame()
    repeat = 3
    for dynasty in dynasties:
        for super_power in super_powers:
            for story_type in story_types:
                   for i in range(repeat):
                        prompt = f"""请你用中文写一段300字的故事，情节跌宕起伏，讲述一位{dynasty}朝时期的英雄人物，穿越到现代，拥有了{super_power}这样的超能力，通过{story_type}的战斗，帮助奥特曼一起打败了怪兽的故事。"""
                        story = gpt35(prompt)
                        row = {"dynasty": dynasty, "super_power": super_power, "story_type": story_type, "story": story}
                        row = pd.DataFrame([row])
                        df = pd.concat([df, row], axis=0, ignore_index=True)

    df.to_csv("data/ultraman_stories.csv")

# prepare_stories(dynasties, super_powers, story_types)


# 把对应的 CSV 格式的数据转换成微调模型所需要的 JSONL 格式的文件

df = pd.read_csv("data/ultraman_stories.csv")
# 对于微调，我们使用的 Prompt 不再是一个完整的句子，而是只用了“朝代”+“超能力”+“故事类型”拼接在一起的字符串，中间用逗号隔开
df['sub_prompt'] = df['dynasty'] + "," + df['super_power'] + "," + df['story_type']
prepared_data = df.loc[:,['sub_prompt','story']]
prepared_data.rename(columns={'sub_prompt':'prompt', 'story':'completion'}, inplace=True)
prepared_data.to_csv('data/prepared_data.csv', index=False)

import subprocess

# 通过 subprocess 调用了命令行里的 OpenAI 工具，把上面的 CSV 文件，转化成了一个 JSONL 格式的文件
subprocess.run('openai tools fine_tunes.prepare_data --file data/prepared_data.csv --quiet'.split())

# 通过 subprocess 调用 OpenAI 的命令行工具，来提交微调的指令
# 在这个微调的指令里面，我们指定了三个参数，分别是用来训练的数据文件、一个基础模型，以及生成模型的后缀。
subprocess.run('openai api fine_tunes.create --training_file data/prepared_data_prepared.jsonl --model curie --suffix "ultraman"'.split())

# 通过下面的 fine_tunes.list 指令，找出所有我们微调的模型
subprocess.run('openai api fine_tunes.list'.split())


# 这个模型的使用方法，和我们使用 text-davinci-003 之类的模型是一样的，只要在 API 里面把对应的 model 字段换掉就好了
openai.api_key = os.getenv("OPENAI_API_KEY")

def write_a_story(prompt):
    response = openai.Completion.create(
        model="curie:ft-bothub-ai:ultraman-2023-04-04-03-03-26",
        prompt=prompt,
        temperature=0.7,
        max_tokens=2000,
        top_p=1,
        stop=["."])
    return response["choices"][0]["text"]

story = write_a_story("宋,发射激光,艰难 ->\n")
print(story)

# 对于模型微调的效果，我们也可以通过一个 OpenAI 提供的命令 fine_tunes.results 来看。对应的，我们需要提供给它一个微调任务的 id。这个 id，可以在 fine_tunes.list 列出的 fine_tunes 模型的 id 参数里找到
subprocess.run('openai api fine_tunes.results -i ft-3oxkr1zBVB4fJWogJDDjQbr0'.split())


# 如果有了新的数据，可以继续进行微调
'''
与上面原有的微调相比，修改了两个参数。
第一个是 model 参数，我们把 Curie 换成了我们刚才微调之后的模型 curie:ft-bothub-ai:ultraman-2023-04-04-03-03-26。
第二个是 learning_rate_multiplier，这个参数的默认值是根据你的样本数量在 0.05 到 0.2 不等。如果你继续微调的样本数要比之前微调的数据量小很多，你就可以调得大一点。
'''
subprocess.run('openai api fine_tunes.create --training_file data/prepared_data_more_prepared.jsonl --model curie:ft-bothub-ai:ultraman-2023-04-04-03-03-26 --suffix "ultraman" --learning_rate_multiplier 0.2'.split())
