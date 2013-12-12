manualy merged lines starting with INSERT INTO `api_data` VALUES
sed -i "s/'),(1/'\n1/g" api
sed "s/\\\'/ESCAPEDDD/g" lapi > apiESCAPEDDD
python tofile.py

Some transformation steps were done "manually" using Sublime Text multiple-cursors (by laziness to write regular expressions) and might be non trivial to reproduce depending on your text editor or choice.
