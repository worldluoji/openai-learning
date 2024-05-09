
# 字符享元类（Character Flyweight）
class CharacterFlyweight:
    def __init__(self, character):
        self.character = character

    def display(self, screen_position):
        print(f"Rendering '{self.character}' at position {screen_position}")


# 享元工厂（Flyweight Factory）确保相同字符只创建一次。
class CharacterFactory:
    _flyweights = {}

    @classmethod
    def get_character(cls, character):
        if character not in cls._flyweights:
            cls._flyweights[character] = CharacterFlyweight(character)
        return cls._flyweights[character]


'''
CharacterFlyweight类代表了字符的享元，它存储字符的内在状态（字符本身）。
CharacterFactory则作为享元工厂，确保对同一字符的请求总是返回相同的享元实例，从而减少了内存中的对象数量。

通过这种方式，即使文本很长，包含大量重复字符，程序也能够高效地处理和显示文本，避免了不必要的资源消耗。
'''
def main():
    factory = CharacterFactory()

    # 假设要渲染的文本
    text = "Hello, World! This is an example of the Flyweight pattern."

    # 遍历文本并使用享元模式渲染字符
    for position, char in enumerate(text):
        flyweight = factory.get_character(char)
        flyweight.display((position, 0))  # 屏幕位置简化为行号（本例中只有一行）

if __name__ == "__main__":
    main()