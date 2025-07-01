import time

def log_attack(target, status):
    """Registra ataques em arquivo de log."""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {target} -> {status}\n"
    with open("storme.log", "a", encoding="utf-8") as f:
        f.write(log_entry)