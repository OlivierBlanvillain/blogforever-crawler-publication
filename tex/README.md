Install:

    sudo apt-get install latexmk gnuplot texlive-latex-base texlive-latex-extra texlive-fonts-recommended texlive-fonts-extra texlive-science diffpdf pandoc

Compile:

    latexmk

To enable visual PDF diffs:

    git config --global diff.diffpdf.command diffpdf

(If you are forced to use a proprietary operating system... Sorry.)
