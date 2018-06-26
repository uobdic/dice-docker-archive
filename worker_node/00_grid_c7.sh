#!/usr/bin/timeout -s9 10s
if [ $USER != root ]; then
	source /cvmfs/grid.cern.ch/umd-c7wn-latest/etc/profile.d/setup-c7-wn-example.sh
	# to fix java for the hadoop commands:
	unset JAVA_HOME
else
	echo "User root detected - not loading grid setup"
fi
