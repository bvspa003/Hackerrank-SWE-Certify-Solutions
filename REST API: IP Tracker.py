#!/bin/python3

import math
import os
import random
import re
import sys
import requests

def ipTracker(ip):
    # URL for the API request
    url = f"https://jsonmock.hackerrank.com/api/ip?ip={ip}"

    # Send GET request to the API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Check if any record is returned
        if data['total'] == 0:
            return 'No Result Found'

        # Extract the country code from the record
        country = data['data'][0]['country']
        return country
    else:
        # Request failed, return an error message
        return 'API request failed'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ip = input()

    result = ipTracker(ip)

    fptr.write(str(result) + '\n')

    fptr.close()
