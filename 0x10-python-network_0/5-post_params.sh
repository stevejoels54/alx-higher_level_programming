#!/bin/bash
# Send the POST request with the specified data and display the response body
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
