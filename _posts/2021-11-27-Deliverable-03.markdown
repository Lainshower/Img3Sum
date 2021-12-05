---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: post
title:  "Deliverable 03"
date:   2021-11-24 24:00:00 +0900
categories: Development 03
tags:  ['development note']
excerpt_separator: <!--more-->
---

1.  Ceate documentation for project using the ReadTheDocs framework at our local machine using the Sphinx theme.

    ```bash
    pip install sphinx 
    pip install sphinx-rtd-theme
    ```

<!--more-->

2.  Create more comprehensive documentaton with following pages.

    * Index (=About page) : 
    * Installation
    * How to use
    * Contribution Guidelines
    * Licenses

3.  Pull our github repository and make  `docs` directory. Upload markdown files into the main branch of your repository under the `docs` folder

    ```bash
    git pull origin
    mkdir docs
    cd docs
    cp rtd folders docs/
    ```

4.  Connect the GitHub `docs`  documentation folder with the ReadTheDocs hosting.
    
    Hosting our official `readthedocs` documents by referring to the [readthedocs] and [readthedocshosting].

5. Following is our `readthedocs` link.

    Img3Sum Official Document : [Img3Sum Readthedocs] 

[readthedocs]: https://readthedocs.org/
[readthedocshosting]: https://www.youtube.com/watch?v=OdVKFkZQyTo&list=PLPDCBPbzk1AYghqYazE7Cxt3p7edml8I7&index=23
[Img3Sum Readthedocs]: https://img3sum.readthedocs.io/en/main/