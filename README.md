# notion to github pages with python
Easy python implementation of automatically chaninging notion markdown zip file to github pages.

## Requirements and Installation

### :star: Requirements

- Python
- libraries: zipfile, glob, time, shutil, os

### :star: How to Use

1. [Notion page] Press the 'ㆍㆍㆍ' button (at the top right corner) on your notion page.
2. [Notion page] Press the 'Export' button and set the 'Export format' as Markdown & CVS and 'Include content' as everything.
3. [Github repo] Move zip files (Two or more are possible) to the base folder of your github io repo (without changing file names).
4. [Github repo] Copy notion2githubpages.py to the same base folder and command 'python notion2githubpages.py'.
5. [Github repo] Enter the Title, Excerpt, Category and Tags(separated by '/') as inputs.
6. It will automatically convert to github pages style markdown with posts_folder_path='_posts/' and images_folder_path='assets/images/'.

#### FOR KOREAN
1. [노션 페이지] 노션 페이지에 들어가 'ㆍㆍㆍ' 버튼(우상단)을 클릭합니다.
2. [노션 페이지] 'Export' 버튼을 누르고 'Export format'으로 Markdown & CVS 을 선택하고 'Include content' 을 everything로 설정합니다.
3. github io repo의 base 폴더에 다운받은 zip파일들(여러 개 가능)을 옮깁니다. (파일 이름 변경 금지) 
4. notion2githubpages.py를 같은 base folder에 복사 후 'python notion2githubpages.py'를 입력합니다.
5. Title(제목), Excerpt(발췌-제목 아래에 표시되는 내용), Category(카테고리)와 Tags(태그, '/'로 구분해서 여러 개 입력 가능)을 입력합니다.
6. 자동적으로 md 파일은  posts_folder_path='_posts/'에 저장되고 이미지는 images_folder_path='assets/images/'에 저장됩니다. 

### :star: Notes
1. I use the jekyll with [minimal mistake](https://mademistakes.com/work/minimal-mistakes-jekyll-theme/), so I cannot guarantee for other environments.
2. I couldn't find a python implementation for notion2githubpages, but if there is, please let me know.
3. Refer [shell implementation](https://github.com/uoneway/notion-to-github-pages) for the shell implementation and [guideline](https://swieeft.github.io/2020/03/02/NotionToGithubioPorting.html) for checking the github markdown differences.
4. Refer [notion2tistory](https://www.notion.so/Notion2Tistory-f46185df1db14f8eb571d366b66c5e9c) for the emplementation of notion to tistory.
