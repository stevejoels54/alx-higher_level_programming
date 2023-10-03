#!/bin/bash
# Define the URL
URL="$1"

# Send the request and display only the status code
curl -s -o /dev/null -w "%{http_code}\n" "$URL"
