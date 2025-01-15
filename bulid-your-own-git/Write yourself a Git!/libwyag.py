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



# 仓库类
class GitRespository(object):

    worktree = None
    gitdir = None
    conf = None

    # force参数：该参数禁用所有检查
    def __init__(self,path,force=False):
        self.worktree = path
        self.gitdir = os.path.join(path,'.git')

        # 如果检查失败
        if not(force or os.path.isdir(self.gitdir)):
            raise Exception(f"Not a Git respository {path}")

        #处理配置文件
        self.conf = configparser.ConfigParser() # 用于读取配置文件的对象
        cf = repo_file(self,"config") # 创建一个./git/config文件

        if cf and os.path.exists(cf):
            self.conf.read([cf]) # 表示一个列表传入，这样既可以传入一个参数又可以传入多个
        elif not force:
            raise Exception("Configuration file missing")

        # 版本检查：不禁用所有检查时生效，即force = False,
        if not force:
            vers = int(self.conf.get("core", "repositoryformatversion")) #从 [core] 部分获取 repositoryformatversion 的值。
            if vers != 0:
                raise Exception(f"Unsupported repositoryformatversion: {vers}")



def cmd_add(args):
    pass


# --------------------------- init -----------------------------------------------
# 方法：构建子路径
def repo_path(repo,*path):
    return os.path.join(repo.gitdir,*path)


# 方法：创建文件夹
def repo_dir(repo,*path,mkdir=False):
    """"与 repo_path 相同，但如果路径不存在且 `mkdir` 为真，则创建 *path 目录"""
    path = repo_path(repo,*path)

    # 如果文件夹存在了
    if os.path.exists(path):
        if(os.path.isdir(path)):
            return path
        else:
            raise Exception(f"Not a direction {path}")

    # 如果文件夹不存在，并且mkdir为真,则创建文件夹
    if mkdir:
        os.makedirs(path)
        return path
    else:
        return None


# 方法：创建文件
def repo_file(repo,*path,mkdir=False):
    """Same as repo_path, but create dirname(*path) if absent.  For
    example, repo_file(r, \"refs\", \"remotes\", \"origin\", \"HEAD\") will create
    .git/refs/remotes/origin. 只创建文件的文件夹，而不创建文件，返回文件的路径"""

    if repo_dir(repo,*path[:-1],mkdir=mkdir):
        return repo_path(repo,*path)

# 方法：设置默认的配置
def repo_default_config():
    ret = configparser.ConfigParser()

    ret.add_section("core")
    ret.set("core", "repositoryformatversion", "0")
    ret.set("core", "filemode", "false")
    ret.set("core", "bare", "false")

    return ret

# 方法：创建仓库
def repo_create(path):
    """在path目录下创建一个新的仓库"""
    #在创建时不强制检查
    repo = GitRespository(path,True)

    # 确保路径存在并且不为空文件夹,如果没有，则创建
    if os.path.exists(repo.worktree):
        if not os.path.isdir(repo.worktree):
            raise Exception(f"{path} is not a directory !!!")
        if os.path.exists(repo.gitdir) and os.listdir(repo.gitdir):
            raise Exception(f"{path} is not empty !!!" )
    else:
        # 与mkdir相比，makedirs可以创建多层路径
        os.makedirs(repo.worktree)

    # 断言创建.git目录下的文件夹
    assert repo_dir(repo,"branches",mkdir=True)
    assert repo_dir(repo,"objects",mkdir=True)
    assert repo_dir(repo,"refs","tags",mkdir=True)
    assert repo_dir(repo,"refs","heads",mkdir=True)

    # 创建文件 .git/description
    with open(repo_file(repo,"description"),"w") as f:
        f.write("Unnamed repository; edit this file 'description' to name the repository.\n")

    # 创建文件 ./git/HEAD
    with open(repo_file(repo,"HEAD"),"w") as f:
        f.write("ref: refs/heads/master\n")

    # 写入配置文件，在repo初始化中，配置文件已经创建好了，这里就要写入
    with open(repo_file(repo,"config"),"w") as f:
        config = repo_default_config()
        config.write(f)

    return repo


# 创建命令行
argsp = argsubparsers.add_parser("init", help="Initialize a new, empty repository.")

argsp.add_argument("path",   # 参数的名称：init path
                   metavar="directory",   # 代表该参数的别称
                   nargs="?",             #参数数量,表示该参数是可选的，即用户可以选择提供或不提供这个参数。不提供，那么就用default里的
                   default=".",           #.表示当前路径
                   help="Where to create the repository.")


def cmd_init(args):
    repo_create(args.path)

# --------------------------- init -----------------------------------------------



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




