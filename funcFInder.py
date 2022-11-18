# coding=utf-8

import os
import sys
import subprocess
import re
import argparse

 
def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", type=str, default="", help="libc path")
    parser.add_argument("-s", type=str, default="", help="symbol you want to find")
    hp = parser.parse_args()
    return hp

def read_from_user():
    hp = get_parser()
    global PATH 
    PATH = hp.__dict__['l']
    global FUNC_NAME 
    FUNC_NAME = hp.__dict__['s']

def grep_file():
    filename_list = []
    result = subprocess.run(['grep', '-r', FUNC_NAME, PATH], stdout=subprocess.PIPE)
    result_list = result.stdout.decode('utf-8').split("\n")
    for i in range(len(result_list)):
        if "Binary file" not in result_list[i]:
            continue
        r = result_list[i].replace('Binary file ','').replace(' matches','')
        filename_list.append(r)
    return filename_list
        
def nm_symbols(filename):
    print('[...] Checking %s'%filename)
    result = subprocess.run(['nm', '-D', filename],stdout=subprocess.PIPE)
    symbol_list = result.stdout.decode('utf-8').split('\n')
    for i in range(len(symbol_list)):
        if FUNC_NAME in symbol_list[i] and symbol_list[i].split(' ')[1] == 'T':
            print('[ * ] Find funciton in : \033[0;32;40m%s\033[0m'%filename)
            break


def main():
    read_from_user()
    filename_list = grep_file()

    for i in range(len(filename_list)):
        nm_symbols(filename_list[i])

if __name__ == "__main__":
    main()
