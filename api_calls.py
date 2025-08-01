#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module docstring."""

# Imports
from dotenv import dotenv_values
import requests
import json
from time import sleep
from loguru import logger

# Module Constants


# Module "Global" Variables
config = dotenv_values()
try:
    my_headers = {
        "Authorization": f"Bearer {config["ACCESS_TOKEN"]}",
        "Accept": "application/json"
    }    
except KeyError as e:
    print(f"No ACCESS_TOKEN or .env missing")
    exit(-1)

# Module Functions and Classes
def list_people():
    """Return all users"""
    api_url = "https://webexapis.com/v1/people"
    

def send_request(url,type="GET", payload=None) -> requests.Response:
    """Handling http 429 and whatever comes up later"""
    # response = requests.get("https://webexapis.com/v1/devices?max=200", headers=my_headers)
    
    while True:
        match type:
            case "GET":
                logger.debug(url)
                response = requests.get(url, headers=my_headers)
            case "PUT":
                pass
            case "POST":
                pass
            case "PATCH":
                pass
            case _:
                pass
        if response.status_code == 429:
            logger.warning(f"Too many requests, wait for: {response.headers["Retry-After"]}s")
            sleep(int(response.headers["Retry-After"]))
        elif response.status_code == 200:
            return response
        else:
            logger.error(response.status_code)
            return None
        
    return None
    
def list_devices() -> dict | None:
    """Return all devices"""
    api_url = "https://webexapis.com/v1/devices?max=200"
    
    response = send_request(api_url)
    if response:
        try:
            if response.headers["link"]:
                next_link = str(response.headers["link"]).split(";")
                next_link = str(next_link[0])
                next_link = next_link.replace("<","")
                _ = input(f"There is more result on this link: {next_link}, press any key to continue")
                logger.info(f"There is more result on this link: {next_link}")
        except KeyError as e:
            pass
        
        devices = json.loads(response.text)
        return devices
    return None

def list_number_associated_with_workspace(workspace_id: str) -> list:
    """List numbers associated with a specific workspace"""
    api_url = f"https://webexapis.com/v1/workspaces/{workspace_id}/features/numbers"
    
    response = send_request(api_url)
    try:
        if response.headers["link"]:
            next_link = str(response.headers["link"]).split(";")
            next_link = str(next_link[0])
            next_link = next_link.replace("<","")
            _ = input(f"There is more result on this link: {next_link}, press any key to continue")
            logger.info(f"There is more result on this link: {next_link}")
    except KeyError as e:
        pass
    
    workspace = json.loads(response.text)
    return workspace

def get_person_details(person_id: str) -> list:
    """Get Person Details"""
    api_url = f"https://webexapis.com/v1/people/{person_id}"
    
    response = send_request(api_url)
    try:
        if response.headers["link"]:
            next_link = str(response.headers["link"]).split(";")
            next_link = str(next_link[0])
            next_link = next_link.replace("<","")
            _ = input(f"There is more result on this link: {next_link}, press any key to continue")
            logger.info(f"There is more result on this link: {next_link}")
    except KeyError as e:
        pass
    
    user = json.loads(response.text)
    return user
    

def main(*args):
    """Program execution starts here."""
    """Nothing to do here -> this module is imported by main.py"""
    
# Check to see if this file is the "__main__" script being executed
if __name__ == '__main__':
    main()