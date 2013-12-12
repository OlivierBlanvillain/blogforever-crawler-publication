blogforever-crawler-publication
===============================

This repository contains all the scripts and files related the blogforever-crawler-publication. It is organized as follows:

- `/tex` contains the latex and gnuplot files together with instructions on how to compile [the paper](https://github.com/OlivierBlanvillain/blogforever-crawler-publication/blob/master/tex/main.tex) from source,
- `/dataset` explains how to extract our test-set from of the [Spinn3r Dataset](http://www.icwsm.org/data/),
- `/extraction-success-rates` has the scripts we used to obtain the
"extraction success rates" data,
- `/content-extraction-running-times` contains the code we used for running time measurements.

Please keep in mind that all scripts you will find here were written as "single use code" and are anything but beautiful. Because the Spinn3r Dataset is only available for research purposes we could include it in this repository, which means that you will have to download it and follow the instruction in `/dataset` to be able to reproduce the `/extraction-success-rates` experiment.
