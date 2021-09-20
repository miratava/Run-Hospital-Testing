#!/bin/bash

cd /home/buildagent/
python3 /home/buildagent/socketserver.py &
/run-services.sh
