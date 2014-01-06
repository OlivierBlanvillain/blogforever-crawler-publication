#!/bin/sh

python score.py ../dataset/articles/ ../../crawler/articles
python score.py ../dataset/articles/ articles/goose/
python score.py ../dataset/articles/ articles/readability/
python score.py ../dataset/articles/ articles/boilerpipe/
