# Import library berdasarkan OS yang dipakai
import os
import sys
import re
import json

# COLORAMA: untuk mewarnai console
try:
    from colorama import Fore, Style
except ModuleNotFoundError:
    os.system("pip install colorama")
    try:
        from colorama import Fore, Style
    except ImportError:
        sys.exit(0)

# Import library berdasarkan OS yang dipakai
if os.name == "posix":
    # GETCH: untuk merekam input user [ESC]
    try:
        from getch import getch
    except ModuleNotFoundError:
        os.system("pip install getch")
        try:
            from getch import getch
        except ImportError:
            sys.exit(0)
elif os.name == "nt":
    # GETCH: untuk merekam input user [ESC]
    try:
        from msvcrt import getch
    except ModuleNotFoundError:
        os.system("pip install msvcrt")
        try:
            from msvcrt import getch
        except ImportError:
            sys.exit(0)

# Variable Global
RED = Fore.RED
GREEN = Fore.GREEN
CYAN = Fore.CYAN
YELLOW = Fore.YELLOW
BRIGHT = Style.BRIGHT
RESET = Style.RESET_ALL

FILENAME = "result.json"

# Fungsi: untuk membersihkan console berdasarkan OS yang dipakai
def clear_screen():
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
    else:
        return

# Fungsi: Untuk validasi input apakah yang diinputkan berupa URL?
def is_url(string):
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// atau https:// atau ftp:// atau ftps://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain
        r'localhost|'  # localhost
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ip (x.x.x.x) 3 dot
        r'(?::\d+)?'  # opsional: port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return bool(re.match(regex, string))

# Fungsi: Untuk handle jika yang diinputkan bukan URL
def false_url():
    print(f"\n {CYAN}{BRIGHT}[{YELLOW}#{CYAN}] {GREEN}RESULT{RESET}:\n  |")
    print("  |  {")
    print(f"  |    \"status\" : \"{RED}{BRIGHT}error{RESET}\",")
    print(f"  |    \"message\": \"{CYAN}{BRIGHT}yang anda inputkan bukanlah URL yang valid!{RESET}\"")
    print("  |  }")
    print(f"  |", end='')
    return True

# Fungsi: Untuk dump / menampilkan data dalam file berdasarkan OS yang dipakai
def read_file_name(filename):
    if os.name == "nt":
        os.system(f"type {filename}")
    elif os.name == "posix":
        os.system(f"cat {filename}")
    else:
        return

# Fungsi: Untuk menampilkan banner di main program
def banner():
    # Design: https://patorjk.com/software/taag/#p=display&f=Big%20Money-nw&t=
    print(f"""{CYAN}\n     $$$$$$$$\\ $$$$$$$$\\  $$$$$$\\ $$$$$$$$\\       $$$$$$\\  $$$$$$$\\ $$$$$$\\
     \\__$$  __|$$  _____|$$  __$$\\\\__$$  __|     $$  __$$\\ $$  __$$\\\\_$$  _|
        $$ |   $$ |      $$ /  \\__|  $$ |        $$ /  $$ |$$ |  $$ | $$ |
        $$ |   $$$$$\\    \\$$$$$$\\    $$ |$$$$$$\\ $$$$$$$$ |$$$$$$$  | $$ |
        $$ |   $$  __|    \\____$$\\   $$ |\\______|$$  __$$ |$$  ____/  $$ |
        $$ |   $$ |      $$\\   $$ |  $$ |        $$ |  $$ |$$ |       $$ |
        $$ |   $$$$$$$$\\ \\$$$$$$  |  $$ |        $$ |  $$ |$$ |     $$$$$$\\
        \\__|   \\________| \\______/   \\__|        \\__|  \\__|\\__|     \\______|
    \n                        {RED}{BRIGHT}[ {YELLOW}CONTACT ME{Fore.WHITE}: {GREEN}0xd1m5@gmail.com{RESET}{BRIGHT}{RED} ]{RESET}""")

def main():
    clear_screen()
    banner()
    # INPUT URL ======================================
    print(f"\n {CYAN}{BRIGHT}[{YELLOW}#{CYAN}]{GREEN} FORMAT INPUT url{RESET}:\n  |  {CYAN}> ex{RESET}: https://reqres.in/api/users/2\n  |")
    url = str(input(f"  +--{CYAN}{BRIGHT}[{YELLOW}?{CYAN}]{RESET} INPUT url : {YELLOW}{BRIGHT}"))
    if is_url(url):
        pass
    else:
        if false_url():
            return
    print(f"\n {CYAN}{BRIGHT}[{YELLOW}#{CYAN}] {GREEN}HTTP request{RESET}:\n  |  {CYAN}> options{RESET}: 1. GET    3. PUT\n  |             2. POST   4. DELETE\n  |")
    # INPUT HTTP =====================================
    try:
        http = int(input(f"  +--{CYAN}{BRIGHT}[{YELLOW}?{CYAN}]{RESET} INPUT http: (1..4) {YELLOW}{BRIGHT}"))
    except ValueError as e:
        print(f"\n {CYAN}{BRIGHT}[{YELLOW}#{CYAN}] {GREEN}RESULT{RESET}:\n  |")
        print("  |  {")
        print(f"  |    \"status\" : \"{RED}{BRIGHT}error{RESET}\",")
        print(f"  |    \"message\": \"{CYAN}{BRIGHT}yang anda inputkan tidak ada di pilihan!{RESET}\"")
        print("  |  }")
        print(f"  |", end='')
        return
    print()

    if http == 1:
        req = "GET"
    elif http == 2:
        req = "POST"
    # Belum stabil: PUT & DELETE
    elif http == 3:
        req = "PUT"
    elif http == 4:
        req = "DELETE"

    if http not in [1, 2, 3, 4]:
        print(f" {CYAN}{BRIGHT}[{YELLOW}#{CYAN}] {GREEN}RESULT{RESET}:\n  |")
        print("  |  {")
        print(f"  |    \"status\" : \"{RED}{BRIGHT}error{RESET}\",")
        print(f"  |    \"message\": \"{CYAN}{BRIGHT}yang anda inputkan tidak ada di pilihan!{RESET}\"")
        print("  |  }")
        print(f"  |", end='')
        return

    if http in [2, 3]:
        print(f" {CYAN}{BRIGHT}[{YELLOW}#{CYAN}] {GREEN}FORMAT INPUT data{RESET}:\n  |  {CYAN}> ex{RESET}: name=dimas&job=tidur\n  |")
        # INPUT DATA =================================
        data = input(f"  +--{CYAN}{BRIGHT}[{YELLOW}?{CYAN}]{RESET} INPUT data: {YELLOW}{BRIGHT}")
        try:
            data_json = json.dumps(dict([tuple(d.split('=')) for d in data.split('&')]))
            data_query = '&'.join([f"{k}={v}" for k, v in json.loads(data_json).items()])
        except ValueError as e:
            print(f"\n {CYAN}{BRIGHT}[{YELLOW}#{CYAN}] {GREEN}RESULT{RESET}:\n  |")
            print("  |  {")
            print(f"  |    \"status\" : \"{RED}{BRIGHT}error{RESET}\",")
            print(f"  |    \"message\": \"{CYAN}{BRIGHT}{e}{RESET}\"")
            print("  |  }")
            print(f"  |", end='')
            return

        print()
        os.system(f'curl -s -X {req} -d "{data_query}" {url} | jq > {FILENAME} 2>&1')
    else:
        os.system(f"curl -s -X {req} \"{url}\" | jq > {FILENAME} 2>&1")

    print(f" {CYAN}{BRIGHT}[{YELLOW}#{CYAN}] {GREEN}RESULT{RESET}:\n")

    if os.path.isfile(FILENAME):
        with open(FILENAME, "r") as f:
            lines = f.readlines()

        with open(FILENAME, "w") as f:
            for line in lines:
                f.write('     ' + line)

        read_file_name(FILENAME)

    else:
        print(f"\n {CYAN}{BRIGHT}[{YELLOW}#{CYAN}] {GREEN}RESULT{RESET}:\n  |")
        print("  |  {")
        print(f"  |    \"status\" : \"{RED}{BRIGHT}error{RESET}\",")
        print(f"  |    \"message\": \"{CYAN}{BRIGHT}file {FILENAME} tidak ditemukan!{RESET}\"")
        print("  |  }")
        print(f"  |\n {CYAN}{BRIGHT}[{YELLOW}#{CYAN}] {RESET}tekan apa saja untuk {BRIGHT}{YELLOW}keluar{RESET}!", end='')
        sys.exit(0)

if __name__ == "__main__":
    try:
        os.system("title Mini-project: TEST-API @syaauqqii" if os.name == 'nt' else "")
        while True:
            # main program
            main()
            print(f"\n {CYAN}{BRIGHT}[{YELLOW}!{CYAN}] {RESET}tekan {RED}{BRIGHT}[ESC] {RESET}untuk {YELLOW}{BRIGHT}keluar{RESET}!", end='')
            if getch() == b'\x1b':
                print()
                break  # [ESC] -> Keluar
    except KeyboardInterrupt:
        print(f"\n\n {CYAN}{BRIGHT}[{YELLOW}#{CYAN}] {GREEN}RESULT{RESET}:\n  |")
        print("  |  {")
        print(f"  |    \"status\" : \"{GREEN}{BRIGHT}success{RESET}\",")
        print(f"  |    \"message\": \"{CYAN}{BRIGHT}berhasil exit dengan CTRL + C{RESET}\"")
        print("  |  }")
        print(f"  |\n {CYAN}{BRIGHT}[{YELLOW}#{CYAN}] {RESET}tekan apa saja untuk {BRIGHT}{YELLOW}keluar{RESET}!", end='')
        try:
            input("")
        except KeyboardInterrupt:
            print()
            sys.exit(0)
        sys.exit(0)
