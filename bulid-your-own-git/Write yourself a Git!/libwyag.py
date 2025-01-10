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

argsp = argsubparsers.add_parser("init", help="Initialize a new, empty repository.")
argsp.add_argument("path",
                   metavar="directory",
                   nargs="?",
                   default=".",
                   help="Where to create the repository.")

def cmd_add(args):
    pass


def cmd_init(args):
    print(args)

# 定义入口函数
def cmd_cat_file(args):
    pass


def cmd_check_ignore(args):
    pass


def cmd_commit(args):
    pass


def cmd_hash_objecy(args):
    pass


def cmd_log(args):
    pass


def cmd_ls_files(args):
    pass


def cmd_ls_tree(args):
    pass


def cmd_status(args):
    pass


def cmd_rev_parse(args):
    pass


def cmd_rm(args):
    pass


def cmd_show_ref(args):
    pass


def cmd_tag(args):
    pass


def main(argv=sys.argv[1:]):
    args = argparser.parse_args(argv)
    match args.command:
        case 'add'          : cmd_add(args)
        case 'cat-file'     : cmd_cat_file(args)
        case 'check-ignore' : cmd_check_ignore(args)
        case 'commit'       : cmd_commit(args)
        case 'hash-object'  : cmd_hash_objecy(args)
        case 'init'         : cmd_init(args)
        case 'log'          : cmd_log(args)
        case 'ls-files'     : cmd_ls_files(args)
        case 'ls-tree'      : cmd_ls_tree(args)
        case "rev-parse"    : cmd_rev_parse(args)
        case "rm"           : cmd_rm(args)
        case "show-ref"     : cmd_show_ref(args)
        case "status"       : cmd_status(args)
        case "tag"          : cmd_tag(args)
        case _              :print("Bad command.")




