#!/bin/bash
# vim: tw=0
source /cvmfs/sft.cern.ch/lcg/views/LCG_94/x86_64-slc6-gcc7-opt/setup.sh

python calculate_trigger_efficiencies.py -w medium tight vtight -o tauTriggerEfficiencies_updated.root -i /ceph/mburkart/Artus/artusjobs_Data_and_MC_Fall17v2MC_ReReco31Mar2018_TauTagAndProbe_03_09_2019/merged/ -f DATA MC
