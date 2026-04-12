from utils import *

import sys

def main():
    if len(sys.argv) == 2:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    copy_dir("static","docs")
    generate_page_recursive("content", "template.html", "docs", basepath)
main()