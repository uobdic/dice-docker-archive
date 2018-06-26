#!/bin/bash
HOST=`hostname -f`
USER_INFO=`id`
USER=`whoami`
OS_INFO=`/bin/cat /etc/redhat-release`
echo "Running on ${HOST} (${OS_INFO})"
echo "User info: ${USER_INFO}"


echo "Checking access to HDFS"
hdfs dfs -ls /
echo "Copying file from local to hadoop"
hdfs dfs -copyFromLocal /hdfs/user/$USER/iml_challenge/train.csv /user/$USER/test/train.csv
echo "Removing test file"
hdfs dfs -rm -skipTrash /user/$USER/test/train.csv

echo "Testing mounts"
ls -l /srv* /hdfs /tmp /etc
sleep 120
