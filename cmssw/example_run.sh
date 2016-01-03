#!/bin/sh -ex

source /opt/cms/cmsset_default.sh
scram project CMSSW_7_4_12
cd CMSSW_7_4_12
eval `scram run -sh`
mkdir -p /data
cd /data
cmsRun myPythonConfig.py
