#!/bin/sh

python score.py contents/ ../../blogforever-crawler/out
python score.py contents/ goose/
python score.py contents/ readability/
python score.py contents/ boilerpipe/
