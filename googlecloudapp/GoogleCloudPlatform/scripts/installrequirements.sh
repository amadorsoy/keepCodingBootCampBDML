#!/bin/bash

apt-get install -y libsasl2-dev libsasl2-modules python-pip

pip install pyhs2 pyhive

gsutil cp "gs://ismalp-bda5-keepcoding/scripts/createtablesandloaddata.py" /home/amadorsoy/createtablesandloaddata.py

python /home/amadorsoy/createtablesandloaddata.py