#!/bin/bash
# Define the URL and custom header
URL="$1"
CUSTOM_HEADER="X-School-User-Id: 98"

# Send the GET request with the custom header and display the response body
curl -sH "$CUSTOM_HEADER" "$URL"
