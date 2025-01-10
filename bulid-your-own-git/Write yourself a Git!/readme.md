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
因为现在还没有命令，所以Commands是空的：{ }

如果要求运行脚本时必须提供一个子命令，则可以使用以下代码
~~~python
argsubparsers.required=True
~~~

## 创建主入口函数main
代码如下：
~~~python
def main(argv=sys.argv[1:]):
    args = argparser.parse_args(argv)
    match args.command:
        case "add"          : cmd_add(args)
        case "cat-file"     : cmd_cat_file(args)
        case "check-ignore" : cmd_check_ignore(args)
        case "checkout"     : cmd_checkout(args)
        case "commit"       : cmd_commit(args)
        case "hash-object"  : cmd_hash_object(args)
        case "init"         : cmd_init(args)
        case "log"          : cmd_log(args)
        case "ls-files"     : cmd_ls_files(args)
        case "ls-tree"      : cmd_ls_tree(args)
        case "rev-parse"    : cmd_rev_parse(args)
        case "rm"           : cmd_rm(args)
        case "show-ref"     : cmd_show_ref(args)
        case "status"       : cmd_status(args)
        case "tag"          : cmd_tag(args)
        case _              : print("Bad command.")
~~~
### 接收参数
`def main(argv=sys.argv[1:]):`定义一个入口函数，它接受一个参数 `argv`，默认值为 `sys.argv[1:]`

其中`sys` 是 Python 的一个标准库模块，提供对解释器使用或维护的一些变量和函数的访问。
`sys.argv` 是一个列表，包含了命令行参数。具体来说：
* `sys.argv[0]`: 是脚本名称。
* `sys.argv[1:]`: 是传递给脚本的所有额外命令行参数

### 将参数解析，并存入Namespace
`args = argparser.parse_args(argv)`:解析传递给 main 函数的参数列表 `argv`，并将解析结果存储在 `args` 中。
`parse_args` 方法将 `argv` 列表中的参数解析为一个 `Namespace` 对象，其中包含了根据定义的命令行参数设置的属性
>`Namespace` 是 `argparse` 模块中的一个简单类，用于存储解析后的命令行参数。它的主要功能是将命令行参数转换为易于访问的属性，使得开发者可以通过点（.）操作符方便地访问参数值。
### 测试
假如我们写了以下代码:
~~~python
argparser = argparse.ArgumentParser(description="这是一个简单的git实现")
argsubparsers = argparser.add_subparsers(title='Commands',dest = 'command')
argsubparsers.required = True

argsp = argsubparsers.add_parser("init", help="Initialize a new, empty repository.")
argsp.add_argument("path",
                   metavar="directory",
                   nargs="?",
                   default=".",
                   help="Where to create the repository.")
# 定义入口函数
def main(argv=sys.argv[1:]):
    print(f'这是sys.argv的输出：{sys.argv}')
    print(f'这是argv的输出：{argv}')
    args = argparser.parse_args(argv) # 把参数转换成Namespace命名空间，更加方便处理
    print(f'这是args的输出：{args}')
~~~

运行脚本：
~~~bash
./wyag init path='dsadadadasd'
~~~

得到结果如下：
~~~bash
这是sys.argv的输出：['./wyag', 'init', 'path=dsadadadasd']
这是argv的输出：['init', 'path=dsadadadasd']
这是args的输出：Namespace(command='init', path='path=dsadadadasd')
~~~
可以看出他们分别是列表和Namespace对象

