import argparse     #解析命令行参数的包
import configparser #读取文件的包
from datetime import datetime # 日期时间操作
import grp,pwd
from fnmatch import fnmatch
import hashlib
from math import ceil
import os
import re
import sys
import zlib
# 创建一个解析器对象
argparser = argparse.ArgumentParser(description="这是一个简单的git实现")
argsubparsers = argparser.add_subparsers(title='Commands',dest = 'command')
argsubparsers.required = True

#argsp = argsubparsers.add_parser("init", help="Initialize a new, empty repository.")


def main(argv=sys.argv[1:]):
    args = argparser.parse_args(argv)
    match args.command:

        case "init"         : cmd_init(args)

        case _              : print("Bad command.")


def cmd_init(args):
    print(args)

