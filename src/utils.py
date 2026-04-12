import os
import shutil
import re


from mdtohtml import *

def copy_dir(src, tgt, plog=False):
    # Note: this is reading from cwd.  So it sees if it can find these dirs in the one you run the script (main.py) in
    log = ""
    try:
        if os.path.exists(src):
            if not os.path.exists(tgt):
                os.makedirs(tgt)
            if os.listdir(tgt):
                log += f"removing all objects in {tgt}...\n"
                if plog: print(f"removing all objects in {tgt}...")
                shutil.rmtree(tgt)
                os.mkdir(tgt)
            dirs = []
            log += f"adding objects to {tgt}...\n"
            if plog: print(f"adding objects to {tgt}...")
            for obj in os.listdir(src):
                src_path = os.path.join(src, obj)
                tgt_path = os.path.join(tgt, obj)
                if os.path.isdir(src_path):
                    dirs.append(obj)
                    log += f"creating a directory at {tgt_path}\n"
                    if plog: print(f"creating a directory at {tgt_path}")
                    os.mkdir(tgt_path)
                else:
                    log += f"copying file {obj} to {src}\n"
                    if plog: print(f"copying file {obj} to {src}")
                    shutil.copy(src_path, tgt)
            for d in dirs:
                new_src = os.path.join(src, d)
                new_tgt = os.path.join(tgt, d)
                log += f"beginning to copy {new_src} to {new_tgt}...\n"
                if plog: print(f"moving to copy {new_src} to {new_tgt}...\n")
                copy_dir(new_src, new_tgt, plog)
            
        else:
            log += f"{src} or {tgt} could not be found in CWD\n"
        return
    except Exception as e:
        print(f"There was an error while copying the files:\n{type(e).__name__}: {e}.\nPrinting log now...")
        print("-"*65)
        print(log)

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, 'r') as file:
        md = file.read()
    with open(template_path, 'r') as file:
        temp = file.read()
        
    node = markdown_to_html_node(md)
    html = node.to_html()
    title = extract_title(md)
    
    temp = temp.replace("{{ Title }}", title)
    temp = temp.replace("{{ Content }}", html)
    temp = temp.replace('href="/', f'href="{basepath}')
    temp = temp.replace('src="/', f'src="{basepath}')
    
    dir_name = os.path.dirname(dest_path)
    os.makedirs(dir_name,exist_ok=True)
    with open(dest_path, "w") as file:
        file.write(temp)
        
def generate_page_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for obj in os.listdir(dir_path_content):
        obj_path = os.path.join(dir_path_content, obj)
        if os.path.isfile(obj_path):
            regex = r"\w+"
            matches = re.findall(regex, obj)[0]
            dest_file_path = os.path.join(dest_dir_path, f"{matches}.html")
            generate_page(obj_path, template_path, dest_file_path, basepath)
        else:
            new_dest_dir_path = os.path.join(dest_dir_path, obj)
            generate_page_recursive(obj_path, template_path, new_dest_dir_path, basepath)
            

    