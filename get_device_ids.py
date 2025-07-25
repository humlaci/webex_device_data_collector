#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module docstring."""

# Imports
import api_calls

# Module Constants


# Module "Global" Variables
device_ids = {"items":[]}

# Module Functions and Classes
def main(*args):
    """Program execution starts here."""
    devices = api_calls.list_devices()
    for device in devices["items"]:
        device_ids["items"].append(device["id"])
        

    with open("result.json", "w", encoding='utf-8') as output:
        output.write("[\n")
    output.close()
    
    with open("result.json", "a", encoding='utf-8') as final_output:
        for id in device_ids["items"]:
            final_output.write('{"device_id": ')
            final_output.write(f'"{id}"')
            final_output.write('},\n')
        
    with open("result.json", "a", encoding='utf-8') as output:
        output.write("]\n")
    output.close()        
    
# Check to see if this file is the "__main__" script being executed
if __name__ == '__main__':
    main()