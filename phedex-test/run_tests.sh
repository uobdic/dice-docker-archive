#!/bin/bash
source $sw/PHEDEX/etc/profile.d/init.sh
# this file is introduced with the docker run command (see README)
storage_xml=/opt/SITECONF/local/PhEDEx/storage.xml
protocols="file direct gsiftp srmv2 xrootd xrootdfallback"

LFN=/store/PhEDEx_LoadTest07/LoadTest07_Debug_US_Purdue/UK_SGrid_Bristol/138/LoadTest07_Purdue_F8_NRYVSGIAvf5NCQ1s_138
for p in $protocols; do
TestCatalogue -c $storage_xml -p $p -L $LFN
done

# Hammercloud
LFN=/store/test/xrootd/T2_UK_SGrid_Bristol/store/mc/HC/GenericTTbar/GEN-SIM-RECO/CMSSW_7_0_4_START70_V7-v1/00000
echo "PFN should be /dpm/phy.bris.ac.uk/home/cms/store/mc/HC/GenericTTbar/GEN-SIM-RECO/CMSSW_7_0_4_START70_V7-v1/00000"
echo "Re-LFN will not work (that's OK)"
for p in $protocols; do
TestCatalogue -c $storage_xml -p $p -L $LFN
done

# local stageout
p=gsiftp
LFN=/store/user/kreczko
TestCatalogue -c $storage_xml -p $p -L $LFN

# remote stageout
p=gsiftp
LFN=/store/temp/user/kreczko
TestCatalogue -c $storage_xml -p $p -L $LFN
