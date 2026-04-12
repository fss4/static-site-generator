from textnode import *
from htmlnode import *
from mdinlinereader import *
from mdblockreader import *
from mdtohtml import *
from utils import *

import sys
import os
import shutil

def main():
    copy_dir("static","public")
    generate_page_recursive("content", "template.html", "public")
main()