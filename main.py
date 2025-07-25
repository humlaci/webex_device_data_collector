#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module docstring."""


from loguru import logger
import sys
from functions import func2
from dotenv import dotenv_values
from my_logger import logger_init
import json
import api_calls

# Module constants
OUTPUT_FILE = "result.csv"

# .env
config = dotenv_values()

# Module "Global" Variables
locations = {
    "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzM5NTE1NDAzLWJlZTctNGQ0MS1iMDg0LWE2ZDQ0MTIyYzJhMw" : "Fót",
    "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzQ4NGNlYTExLTk2ZDUtNGQ4Ny05NjFhLWI3NGE4M2E2NzQ3Ng" :"Győr",
    "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OL2NkNzUyNTk5LTE3YTItNDZhNi1iZmIwLWI4YjA3MmQ0ZjM4NQ" :"Kecskemét",
    "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzg4NTY0MTE3LWI2MGQtNDg5ZS1iZWQwLWM0MTVlZGRhZjYyNA" : "Polgár",
    "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzg5YTMxMmNkLTg3NmQtNDc1Mi04MDdjLTIwNzU0ZmYwZGQ5Zg" : "Szeged",
    "Y2lzY29zcGFyazovL3VzL0xPQ0FUSU9OLzYwMWNmMmVlLWJlOGItNDgwZS04ZjU1LTIzMTE4MmZhMTQ5Mw" : "Zalaegerszeg"
}

# Funtcions and Classes
def init_output() -> None:
    """empty out output file"""
    
    with open(OUTPUT_FILE, "w", encoding='utf-8') as outputbf:
        outputbf.write("")
    return None

def write_output(content:str) -> None:
    """Generate result file"""
    
    with open(OUTPUT_FILE, "a", encoding='utf-8') as outputbf:
        outputbf.write(f"{content}")
    return None
    
def main(*args, **kwargs) -> None:
    """Program execution starts here"""
    logger_init()
    init_output()
    
    all_devices = api_calls.list_devices()
    
    sum = 0;
    workspace_num = 0;
    user_num = 0
    
    for device in all_devices["items"]:
        try:
            if device["placeId"]:
                # logger.info(f"This is a workspace device")
                workspace_num = workspace_num + 1
                sum = sum +1
                
                workspace = api_calls.list_number_associated_with_workspace(device["placeId"])
                try:
                    write_output(f"{device["displayName"]}|")
                except KeyError as e:
                    write_output("<no display name>|")
                
                try:
                    write_output(f"{device["product"]}|")
                except KeyError as e:
                    write_output("<no product>w")
                    
                try:
                    write_output(f"{device["mac"]}|")
                except KeyError as e:
                    write_output("<no mac>w")
                    
                try:
                    write_output(f"{device["serial"]}|")
                except KeyError as e:
                    write_output("<no serial>|")    

                try:
                    write_output(f"{workspace["phoneNumbers"][0]["external"]}|")
                    write_output(f"{workspace["phoneNumbers"][0]["extension"]}|")
                except KeyError as e:
                    write_output("<no phone numbers>|")    
                write_output("\n")
        except KeyError as e:
            pass
        try:
            if device["personId"]:
                logger.info(f"This is a user device")
                user_num = user_num +1
                sum = sum +1 
                
                user = api_calls.get_person_details(device["personId"])
                
                try:
                    write_output(f"{device["displayName"]}|")
                except KeyError as e:
                    write_output("<no display name>|")
                
                try:
                    write_output(f"{device["product"]}|")
                except KeyError as e:
                    write_output("<no product>w")
                    
                try:
                    write_output(f"{device["mac"]}|")
                except KeyError as e:
                    write_output("<no mac>w")
                    
                try:
                    write_output(f"{device["serial"]}|")
                except KeyError as e:
                    write_output("<no serial>|")    

                try:
                    write_output(f"{user["phoneNumbers"][0]["value"]}|")
                    write_output(f"{user["phoneNumbers"][1]["value"]}|")
                except KeyError as e:
                    write_output("<no phone numbers>|")    
                write_output("\n")

        except KeyError as e:
            pass
    print(f"Sum {sum}, Workspace {workspace_num}, User {user_num}")
    
    return None


if __name__ == "__main__":
    main(1,2,3,45,6, s=10, c=20)
    