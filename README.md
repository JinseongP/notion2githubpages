# notion to github pages with python
Easy python implementation of automatically chaninging notion markdown zip file to github pages.

## Requirements and Installation

### :star: Requirements

- Python
- libraries: zipfile, glob, time, shutil, os

### :star: How to Use

1. [Notion page] Press the 'ㆍㆍㆍ' button (at the top right corner) on your notion page.
2. [Notion page] Press the 'Export' button and set the 'Export format' as Markdown & CVS and 'Include content' as everything.
3. Move zip files (Two or more are possible) to the base folder of your github io repo.
4. Copy notion2githubpages.py to the same base folder and command notion2githubpages.py.
5. Enter the Title, Excerpt, Category and Tags(separated by '/') as inputs.
6. It will automatically convert to github pages style markdown with 

### :star: Notes
1. I use the jekyll with [minimal mistake](https://mademistakes.com/work/minimal-mistakes-jekyll-theme/), so I cannot guarantee for other environments.
2. I couldn't find a python implementation for notion2githubpages, but if there is, please let me know.
3. Refer [shell implementation](https://github.com/uoneway/notion-to-github-pages) and [guideline](https://swieeft.github.io/2020/03/02/NotionToGithubioPorting.html).
4. Refer [notion2tistory](https://www.notion.so/Notion2Tistory-f46185df1db14f8eb571d366b66c5e9c).
