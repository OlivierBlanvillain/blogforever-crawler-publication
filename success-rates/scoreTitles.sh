#!/bin/sh

python score.py ../dataset/titles/ ../../crawler/titles
python score.py ../dataset/titles/ titles/goose/
python score.py ../dataset/titles/ titles/readability/
