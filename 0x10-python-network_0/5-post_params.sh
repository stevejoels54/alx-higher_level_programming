#!/bin/bash
# Define the URL
URL="$1"

# Define the POST data
POST_DATA="email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD"

# Send the POST request with the specified data and display the response body
curl -s -X POST -d "$POST_DATA" "$URL"
