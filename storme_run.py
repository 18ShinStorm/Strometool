import os
import sys
from storme_colors import Colors as C

def show_menu():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(f"""{C.RED}
  _____ ___________ _____ _____ 
 / ____|  ___| ___ \_   _|  _  |
| (___ | |__ | |_/ / | | | | | |
 \___ \|  __||  __/  | | | | | |
 ____) | |___| |    _| |_\ \_/ /
|_____/\_____/\_|    \___/ \___/ 
{C.RESET}""")
    print(f"{C.YELLOW}🔥 STORME-DEFACE | @18shinstorme | KEY: stormeshin18{C.RESET}\n")
    print("1. STORME-DEFACE V1 (Basic)")
    print("2. STORME-DEFACE V2 (Pro)")
    print("3. Exit\n")

def main():
    while True:
        show_menu()
        choice = input(f"{C.CYAN}>>> {C.RESET}").strip()
        
        if choice == "1":
            os.system('python3 stormeV1.py')
        elif choice == "2":
            os.system('python3 stormeV2.py')
        elif choice == "3":
            print(f"{C.RED}[!] Exiting...{C.RESET}")
            sys.exit(0)
        else:
            print(f"{C.RED}[!] Invalid option!{C.RESET}")
            time.sleep(1)

if __name__ == "__main__":
    main()