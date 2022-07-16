#!/bin/sh

echo "installing guiltyspark!"

if [ ! -d "/usr/local/guiltyspark" ]
then
    mkdir /usr/local/guiltyspark
fi

cp -r * /usr/local/guiltyspark/

cp guiltyspark /usr/local/bin/

chmod a+rw /usr/local/guiltyspark/
chmod a+rwx /usr/local/guiltyspark/*

echo "installed guiltyspark to /usr/local/guiltyspark/"
