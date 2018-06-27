#!/usr/bin/timeout -s9 10s

if [ -z ${USER+x} ]
then
	USER=`whoami`
fi

if [ "$USER" != root ]
then
	source /cvmfs/grid.cern.ch/umd-c7wn-latest/etc/profile.d/setup-c7-wn-example.sh
else
	echo "User root detected - not loading grid setup"
fi
