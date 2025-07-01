import re

def validate_target(url):
    """Padroniza URLs para garantir requests válidos."""
    url = url.strip()
    if not re.match(r'^https?://', url, re.I):
        url = 'http://' + url
    return url.rstrip('/')

def generate_user_agent():
    """Gera User-Agent aleatório para evitar bloqueios."""
    agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36"
    ]
    return random.choice(agents)