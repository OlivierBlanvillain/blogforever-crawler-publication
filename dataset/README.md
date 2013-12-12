TODO...

http://www.icwsm.org/data/

Some transformation steps were done "manually" using Sublime Text multiple-cursors (by laziness to write regular expressions) and might be non trivial to reproduce depending on your text editor or choice.

    manualy merged lines starting with INSERT INTO `api_data` VALUES into `api`
    sed -i "s/'),(1/'\n1/g" api
    sed "s/\\\'/ESCAPEDDD/g" lapi > apiESCAPEDDD
    mkdir titles
    mkdir contents
    python tofile.py
    python toFilesTitles.py
