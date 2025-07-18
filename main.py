#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module docstring."""


from loguru import logger
import sys
from functions import func2
from dotenv import dotenv_values
from my_logger import logger_init
import json

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
def get_phonenumbers(person_id:str, users) -> str | None:
    """Returns person extension and e164 phone number"""
    # print(users["items"][0]["id"])
    for user in users["items"]:
        if person_id == user["id"]:
            # print("found")
            # print(user["phoneNumbers"])
            # print(user["phoneNumbers"][0]["value"])
            # print(user["phoneNumbers"][1]["value"])
            return f'{user["phoneNumbers"][0]["value"]},{user["phoneNumbers"][1]["value"]}'
    return f"<no numbers>"
def main(*args, **kwargs) -> None:
    """Program execution starts here"""
    logger_init()
    
    msg = 'main'
    logger.debug(f'This is a debug message {msg}')
    logger.info(f'This is an info message {msg}')
    logger.warning(f'This is a warning message {msg}')
    logger.error(f'This is an error message {msg}')
    logger.critical(f'This is a critical message {msg}')

    func2()
    
    # TODO
    # Step1 remove all static files stuff move to API request
    # Step2 environment variables for access token
    # Step3 prepare API for 429 requests (retry-after header)
    # Step3 get all device api call
    # Step4 get the ddevice data (id, location, max, type, etc)
    # Step5 if the devive has personID -> Get the person details collect the numbers
    # Step6 if the device has placeID -> Get the workspace details collect the numbers
    with open("files/devices.json", "r", encoding='utf-8') as devicesbuff:
        devices = json.load(devicesbuff)
    
    with open("files/users.json", "r", encoding='utf-8') as usersbuff:
        users = json.load(usersbuff)
        
    with open("files/workspaces.json", "r", encoding='utf-8') as workspacesbuff:
        workspaces = json.load(workspacesbuff)
    
    for device in devices["items"]:
        try:
            print(device["product"], end='')
            print(", ", end='')
        except KeyError as e:
            print("<no product>", end='')
            print(", ", end='')

        try:
            print(device["mac"],  end='')
            print(", ", end='')
        except KeyError as e:
            print("<no mac>", end='')
            print(", ", end='')
            
        try:
            print(device["serial"],  end='')
            print(", ", end='')
        except KeyError as e:
            print("<no serial>", end='')
            print(", ", end='')
            
        try:
            print(device["displayName"],  end='')
            print(", ", end='')
        except KeyError as e:
            print("<no display>", end='')
            print(", ", end='')
        try:
            print(locations[device["locationId"]],  end='')
            print(",", end='')
        except KeyError as e:
            print("<no location>", end='')
            print("", end='')
        try:
            if device["placeId"]:
                print("<workspace device>", end='')
        except KeyError as e:
            pass
        try:
            if device["personId"]:
                print(get_phonenumbers(device["personId"], users), end='')
        except KeyError as e:
            pass
        print("\n", end='')
    
    
    return None


if __name__ == "__main__":
    main(1,2,3,45,6, s=10, c=20)