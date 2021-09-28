#!/bin/bash
find / -type f -iname "buildAgent.properties" -exec sed -i 's/'^name=.\*'/name='"$AGENT_NAME"'/1' {} + 2>/dev/null 
cd /home/buildagent/
python3 /home/buildagent/socketserver.py &
/run-services.sh



