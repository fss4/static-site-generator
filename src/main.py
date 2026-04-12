from utils import *

import sys
import os

def main():
    if len(sys.argv) == 3:
        basepath = sys.argv[1]
        generator_path = sys.argv[2]
        copy_dir(os.path.join(generator_path, "static"),"docs")
        generate_page_recursive(os.path.join(generator_path, "content"), os.path.join(generator_path, "template.html"), "docs", basepath)
    else:
        basepath = "/"
        copy_dir("static","draft")
        generate_page_recursive("content", "template.html", "draft", basepath)
main()