#!/bin/sh -ex

cd /home/cms/cmssw/src
source ${VO_CMS_SW_DIR}/cmsset_default.sh
eval `scram run -sh`
scram b -j4
# BristolAnalysis/NTupleTools is supplied via the '-v' parameter (see README.md)
python BristolAnalysis/NTupleTools/Configuration/create_heppy_ntuple.py
