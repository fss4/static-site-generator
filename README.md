# Operation
__________
This is a very simple static site generator which I have continued to modify after completing the corresponding [course](https://www.boot.dev/courses/build-static-site-generator-python) on [boot.dev](https://www.boot.dev).

The basic operation is as follows:

1. Put all desired images, PDFs etc. under `static/assets`
2. If you would like to use a favicon name it `favicon.png` and put it in `static`
3. Any `CSS` formatting should be done in `index.css`
4. Design your webserver file structure in `content`.  Your main page should be a `.md` file inside of this directory, any further pages should be stored in subdirectories of `content` also as `.md` files.

At this moment the supported markdown block syntax includes:

- headings (line begins with 1-6 copies of "#" followed by a space)
- ordered lists (each line begins with an increasing number followed by a period and a space i.e. "1. ")
- unordered lists (each line begins with "- ")
- quotes (each line begins with ">")
- codeblocks (the block begins with three backticks "```" and a new line and ends with a newline followed by three backticks)
- normal paragraphs 

All blocks are seperated by double newlines.

Inline markdown syntax that is supported is
- `code`
- **bold**
-  _italic_
- links (formatted as \[link text\](uri))
- images (formatted as \!\[alt text\](uri))

**Inline formatting treats the strings as seperate entities and should not be nested**.  Code, bold, and italic are given by surrounding the desired text with `, **,  and _ respectively.

Once the site structure is set up and the `.md` files are populated as indicated above you can test build the site by running `bash draft.sh` in terminal while the pwd is the root of this project.  This will create the equivalent tree and `HTML` formatted files in a directory called `draft` and start up a local HTTP server which can be reched through a browser at `localhost:8888`.

Once the site is ready to be published to the internet this can be done easily via GitHub pages by following these steps.

1. Make a [GitHub](https://github.com) repo and name it whatever you like.
2. from the directory where you would like the public repo to be stored on your machine run `bash [PATH_TO_SITE_GENERATOR]/build.sh` where the term in brackets should be replaced by the appropriate path.  For example if you want to build the public site tree in a directory `site` on the same level as the root directory of the generator which is named `gen` you should make `site` your working directory and run `bash ../gen/build.sh`.
3. You will be prompted for the name of the repo you made in GitHub and the path to the site generator.  Using the previous example the repo is `site` and the path is `../gen`.
4. The generator will create a directory in the pwd called `docs` and populate it.
5. [push the local repository to GitHub](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github)
6. Go to settings in the repository and then under Code and Automation go to the Pages tab.
7. Set the branch to whatever the branch of the GitHub repo you've created is (there should only be one if you are using a brand new repo) it is likely either `main` or `master`.
8. Set the folder to the `docs` folder that was generated and save.

You should now be able to access your site at `https://{Your GitHub username}.github.io/{repository name}`!

In the future if you make any changes and regenerate the site you just need to commit and push the changes to the repo, the site should update automatically within a few minutes.

# TO DO:
- Implement translation of nested markdown. i.e. currently the code can turn "this is **bold text**" into the appropriate HTML format, but it cannot parse something like _this is **bold text** inside italic text_