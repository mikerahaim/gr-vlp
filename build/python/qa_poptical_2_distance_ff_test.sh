#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/rich/Desktop/vlp_repos/gr-vlp/python
export PATH=/home/rich/Desktop/vlp_repos/gr-vlp/build/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH
export PYTHONPATH=/home/rich/Desktop/vlp_repos/gr-vlp/build/swig:$PYTHONPATH
/usr/bin/python2 /home/rich/Desktop/vlp_repos/gr-vlp/python/qa_poptical_2_distance_ff.py 
