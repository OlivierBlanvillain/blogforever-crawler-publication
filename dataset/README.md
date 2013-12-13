Our extraction evaluation is based on the [the ICWSM 2009 Spinn3r Dataset](http://www.icwsm.org/data/). This dataset is only available for research purposes, which mean that we can not include it in this repository.

Starting from `dump.sql`:

    "manually" merge lines starting with (INSERT INTO `api_data` VALUES) into api
    sed -i "s/'),(1/'\n1/g" api
    sed "s/\\\'/ESCAPEDDD/g" lapi > apiESCAPEDDD
    python tofile.py
    python toFilesTitles.py

`dataset/titles/` and `dataset/contents/` contain an example of the expected output.
