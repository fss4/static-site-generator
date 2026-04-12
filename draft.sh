#!/bin/bash

# This script builds the site in such a way that is appropriate for local testing and lauches a local HTTP server in order to view the produces HTML
python3 src/main.py 
# connects the webserver to localhost:8888
cd draft && python3 -m http.server 8888