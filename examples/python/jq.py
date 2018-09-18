#!/usr/bin/env python3
import json
import sys

print(json.dumps(json.loads(sys.stdin.read()), sort_keys=True, indent=4))
