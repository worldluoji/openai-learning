# Google Python命名规范
## 1. 常用
```
模块名写法: module_name ;
包名写法: package_name ;
类名: ClassName ;
方法名: method_name ;
异常名: ExceptionName ;
函数名: function_name ;
全局常量名: GLOBAL_CONSTANT_NAME ;
全局变量名: global_var_name ;
实例名: instance_var_name ;
函数参数名: function_parameter_name ;
局部变量名: local_var_name .函数名,变量名和文件名应该是描述性的,尽量避免缩写,特别要避免使用非项目人员不清楚难以理解的缩写,不要通过删除单词中的字母来进行缩写. 始终使用 .py 作为文件后缀名,不要用破折号.
```

<br>

## 2. 命名约定
- 所谓”内部(Internal)”表示仅模块内可用, 或者, 在类内是保护或私有的.
- 用单下划线(_)开头表示模块变量或函数是protected的(使用from module import *时不会包含).
- 用双下划线(__)开头的实例变量或方法表示类内私有.
- 将相关的类和顶级函数放在同一个模块里. 不像Java, 没必要限制一个类一个模块.
- 对类名使用大写字母开头的单词(如CapWords, 即Pascal风格), 但是模块名应该用小写加下划线的方式(如lower_with_under.py). 尽管已经有很多现存的模块使用类似于CapWords.py这样的命名, 但现在已经不鼓励这样做, 因为如果模块名碰巧和类名一致, 这会让人困扰.

<br>

## 3. 函数长度
!! 推荐函数功能尽量集中,简单,小巧

不对函数长度做硬性限制.但是若一个函数超过来40行,推荐考虑一下是否可以在不损害程序结构的情况下对其进行分解. 
因为即使现在长函数运行良好,但几个月后可能会有人修改它并添加一些新的行为,这容易产生难以发现的bug.
保持函数的简练,使其更加容易阅读和修改. 当遇到一些很长的函数时,若发现调试比较困难或是想在其他地方使用函数的一部分功能,不妨考虑将这个场函数进行拆分.

<br>

## 4. main
!! 即使是一个打算被用作脚本的文件, 也应该是可导入的. 并且简单的导入不应该导致这个脚本的主功能(main functionality)被执行, 这是一种副作用. 主功能应该放在一个main()函数中.

在Python中, pydoc以及单元测试要求模块必须是可导入的. 你的代码应该在执行主程序前总是检查 if __name__ == '__main__' , 这样当模块被导入时主程序就不会被执行.

若使用 absl, 请使用 app.run :
```
from absl import app ... def main(argv): # process non-flag arguments ... if __name__ == '__main__': app.run(main)
```
否则,使用:
```
def main(): ... if __name__ == '__main__': main()
```
所有的顶级代码在模块导入时都会被执行. 要小心不要去调用函数, 创建对象, 或者执行那些不应该在使用pydoc时执行的操作.

<br>

## 5. 类型注释
- 通用规则请先熟悉下PEP-484对于方法，仅在必要时才对 self 或 cls 注释 若对类型没有任何显示，请使用 Any 无需注释模块中的所有函数。
- 公共的API需要注释 在代码的安全性，清晰性和灵活性上进行权衡是否注释 对于容易出现类型相关的错误的代码进行注释 
- 难以理解的代码请进行注释 若代码中的类型已经稳定，可以进行注释. 对于一份成熟的代码，多数情况下，即使注释了所有的函数，也不会丧失太多的灵活性.