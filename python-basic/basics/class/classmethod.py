
import uuid

'''
generate_id 是一个类方法，它不需要实例就可以调用，用于为每本书生成一个唯一的ID。这里通过cls访问了类变量_book_count并使用了uuid库生成唯一标识。
is_valid_isbn 是一个静态方法，用于检查ISBN号码的有效性，它不依赖于类或实例的具体状态，只是提供一个与类逻辑相关的工具方法。
formatted_title 使用了@property装饰器，使得调用它就像访问一个普通的属性一样，但实际上它执行了一个将书名首字母大写的逻辑。
这提供了一种更优雅的数据访问方式，同时也便于在未来添加额外的逻辑而不影响外部调用代码。
'''
class Book:
    _book_count = 0  # 类变量，用于记录创建的书籍总数

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.id = self.generate_id()  # 使用类方法生成唯一ID
        Book._book_count += 1

    @classmethod
    def generate_id(cls):
        """类方法，用于生成书籍的唯一ID"""
        return f"BK-{uuid.uuid4()}"

    @staticmethod
    def is_valid_isbn(isbn):
        """静态方法，检查给定的ISBN是否有效（简化示例，实际验证更复杂）"""
        return len(isbn) == 13 and isbn.isdigit()

    @property
    def formatted_title(self):
        """属性装饰器，格式化书名，使其首字母大写"""
        return self.title.capitalize()

# 使用示例
book1 = Book("Python Cookbook", "David Beazley", "9780596007973")
print(book1.id)  # 调用类方法生成的唯一ID
print(Book.is_valid_isbn(book1.isbn))  # 静态方法验证ISBN
print(book1.formatted_title)  # 使用属性访问方式获取格式化后的书名

# 类方法直接调用
new_id = Book.generate_id()
print(new_id)