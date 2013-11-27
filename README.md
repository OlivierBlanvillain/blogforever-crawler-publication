blogforever-crawler-publication
===============================

Install:

    sudo apt-get install latexmk gnuplot texlive-latex-base texlive-latex-extra texlive-fonts-recommended texlive-fonts-extra texlive-science

Compile:

    latexmk -pdflatex='pdflatex -interaction=nonstopmode -halt-on-error -file-line-error --shell-escape' -bibtex -pdf -pvc main.tex

Note that tex/main.bib is generated with zotero and the [modified bibtex export translator](http://www.rtwilson.com/academic/autozotbib) from [this shared library](https://www.zotero.org/groups/blogforever-crawler).
