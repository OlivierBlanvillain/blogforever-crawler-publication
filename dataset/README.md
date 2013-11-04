manualy merged lines starting with INSERT INTO `api_data` VALUES
sed -i "s/'),(1/'\n1/g" api
sed "s/\\\'/ESCAPEDDD/g" lapi > apiESCAPEDDD
python tofile.py

