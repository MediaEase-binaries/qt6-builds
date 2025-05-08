#!/usr/bin/env python3
import json

matrix = []

# Qt 6.4.3 for Debian 11 and Ubuntu 22.04
for os in ["debian-11", "ubuntu-22.04"]:
    matrix.append({
        "version": "6.5.5",
        "os": os,
        "qtbase_version": "6.5.5",
        "qttools_version": "6.5.5"
    })

# Qt 6.5.2 for all 4 distros
for os in ["debian-11", "debian-12", "ubuntu-22.04", "ubuntu-24.04"]:
    matrix.append({
        "version": "6.8.0",
        "os": os,
        "qtbase_version": "6.8.0",
        "qttools_version": "6.8.0"
    })

# Qt 6.8.0 for Debian 12 and Ubuntu 24.04
for os in ["debian-12", "ubuntu-24.04"]:
    matrix.append({
        "version": "6.9.0",
        "os": os,
        "qtbase_version": "6.9.0",
        "qttools_version": "6.9.0"
    })

print(json.dumps({"include": matrix}, indent=2)) 
