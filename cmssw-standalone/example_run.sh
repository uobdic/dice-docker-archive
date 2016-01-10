#!/bin/sh -ex

source ${VO_CMS_SW_DIR}/cmsset_default.sh
cd /home/cms/cmssw/src
eval `scram run -sh`
cmsRun myPythonConfig.py
