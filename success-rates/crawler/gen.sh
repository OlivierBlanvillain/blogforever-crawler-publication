#!/bin/sh

for d in $(cat ../blogforever-crawler-publication/dataset/bloglist.txt); do sudo python -m bibcrawl/run $d; done
