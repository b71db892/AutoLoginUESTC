#!/bin/bash
cd /usr/local/share/SrunLoginScript
source /usr/local/miniconda3/bin/activate base
python always_online.py 2>&1
