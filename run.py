#!/usr/bin/env python3
import json
import sys

# Get inputs from action.yml
files = sys.argv[1].split()
severity = sys.argv[2]

result = {}

for file in files:
    result[file] = {
        "severity": severity,
        "status": "PASS"
    }

print(json.dumps(result, indent=2))
