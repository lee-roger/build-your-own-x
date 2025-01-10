# 使用python实现一个简单的git
## 介绍
实现一个自己的git项目

学习项目的网址：https://wyag.thb.lt/

## 设置命令解析器
使用Python的`argparse`模块，用于解析命令行参数和选项

**导入**
~~~python
import argparse
~~~

### **创建解析器对象（ArgumentParser）**
`argparse.ArgumentParser` 是 `argparse` 模块中的核心类，用于创建一个解析器对象，该对象将处理从命令行传递给脚本的参数和选项。

**参数解析：**
* description： 为整个命令行工具提供一个描述，这个描述会在用户使用 -h 或 --help 选项查看帮助信息时显示。

~~~python
import argparse

argparser = argparse.ArgumentParser(description="这是一个简单的git实现")
~~~

输出为下：
~~~bashr
usage: wyag [-h]

这是一个简单的git实现

options:
  -h, --help  show this help message and exit

~~~

### 添加子解析器（Subparasers）
`add_subparsers` 方法用于为主解析器添加子命令。这使得你的命令行工具能够支持多个子命令，每个子命令可以有自己独立的参数和选项。

参数解析：
* title： 为子命令部分提供一个标题，这个标题会在帮助信息中显示，帮助用户理解有哪些可用的子命令。

* dest： 指定存储子命令名称的属性名。在解析命令行参数后，子命令的名称将被存储在 args.command 中（假设解析结果存储在 args 变量中,切dest属性为command）。
~~~python
argsubparsers = argparser.add_subparsers(title='Commands',dest = 'command')

~~~
输出结果如下:
~~~bashr
usage: wyag [-h] {} ...

这是一个简单的git实现

options:
  -h, --help  show this help message and exit

Commands:
  {}

~~~
因为现在还没有命令，所以Commands是空的：{}

如果要求运行脚本时必须提供一个子命令，则可以使用以下代码
~~~python
argsubparsers.required=True

~~~