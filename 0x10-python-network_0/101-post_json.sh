#!/bin/bash
# Define the URL and JSON file
URL="$1"
JSON_FILE="$2"

# Send the JSON POST request and display the response body
curl -s -X POST -H "Content-Type: application/json" -d @"$JSON_FILE" "$URL"
