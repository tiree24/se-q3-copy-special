#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "tiree Daniel help me figure out solving the problem."

import re
import os
import sys
import shutil
import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    # your code here
    list = []
    paths = os.listdir(dirname)
    for filename in paths:
        match = re.search(r'__(\w+)__', filename)
        if match:
            list.append(os.path.abspath(os.path.join(dirname, filename)))
    return list


def copy_to(path_list, dest_dir):
    """copy the special files to a directory"""
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    for path in path_list:
        filename = os.path.basename(path)
        shutil.copy(path, os.path.join(dest_dir, filename))


def zip_to(path_list, dest_zip):
    """zips special files"""
    cmd = ['zip', '-j', dest_zip]
    cmd += path_list
    subprocess.run(cmd)


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('from_dir', help='dir to search')
    # TODO: add one more argument definition to parse the 'from_dir' argument
    ns = parser.parse_args(args)
    # print(ns.from_dir)
    # print(ns.todir)
    # print(ns.tozip)

    special_paths = get_special_paths(ns.from_dir)

    if ns.todir:
        copy_to(special_paths, ns.todir)
    elif ns.tozip:
        zip_to(special_paths, ns.tozip)
    else:
        print('\n'.join(special_paths))

    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.
    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).
    # Your code here: Invoke (call) your functions


if __name__ == "__main__":
    main(sys.argv[1:])
