# OS: untuk menjalankan beberapa command dan handling beberapa proses
from os import system, path, name
# REGULAR EXPRESSION (REGEX): untuk "operasi" string
from re import compile, match, IGNORECASE
# JSON: untuk manipulasi data
from json import dumps, loads

# COLORAMA: untuk mewarnai console
try:
    from colorama import Fore, Back, Style
except ModuleNotFoundError:
    system("pip install colorama")
    try:
        from colorama import Fore, Back, init
    except ImportError:
        exit(0)

# Import library berdasarkan OS yang dipakai
if name == "posix":
    # GETCH: untuk merekam input user [ESC]
    try:
        from getch import getch
    except ModuleNotFoundError:
        system("pip install getch")
        try:
            from getch import getch
        except ImportError:
            exit(0)
elif name == "nt":
    # GETCH: untuk merekam input user [ESC]
    try:
        from msvcrt import getch
    except ModuleNotFoundError:
        system("pip install msvcrt")
        try:
            from msvcrt import getch
        except ImportError:
            exit(0)

# Variable Global
RED    = Fore.RED
GREEN  = Fore.GREEN
CYAN   = Fore.CYAN
YELLOW = Fore.YELLOW
BRIGHT = Style.BRIGHT
RESET  = Style.RESET_ALL

FILENAME = "result.json"

# Fungsi: untuk membersihkan console berdasarkan OS yang dipakai
def clearScreen():
    if name == "nt":
        system("cls")
    elif name == "posix":
        system("clear")
    else:
        return

# Fungsi: Untuk validasi input apakah yang diinputkan berupa URL?
def isURL(string):
    regex = compile(
        r'^(?:http|ftp)s?://' # http:// atau https:// atau ftp:// atau ftps://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain
        r'localhost|' # localhost
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ip (x.x.x.x) 3 dot
        r'(?::\d+)?' # opsional: port
        r'(?:/?|[/?]\S+)$', IGNORECASE)
    return match(regex, string) is not None

# Fungsi: Untuk handle jika yang diinputkan bukan URL
def falseURL():
    print(f"\n {CYAN}{BRIGHT}[{YELLOW}#{CYAN}] {GREEN}RESULT{RESET}:\n  |")
    print("  |  {")
    print(f"  |    \"status\" : \"{RED}{BRIGHT}error{RESET}\",")
    print(f"  |    \"message\": \"{CYAN}{BRIGHT}yang anda inputkan bukanlah URL yang valid!{RESET}\"")
    print("  |  }")
    print(f"  |", end='')
    return True

# Fungsi: Untuk dump / menampilkan data dalam file berdasarkan OS yang dipakai
def readFileName(filename):
    if name == "nt":
        system(f"type {filename}")
    elif name == "posix":
        system(f"cat {filename}")
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
    clearScreen()
    banner()\
    # INPUT URL ======================================
    print(f"\n {CYAN}{BRIGHT}[{YELLOW}#{CYAN}]{GREEN} FORMAT INPUT url{RESET}:\n  |  {CYAN}> ex{RESET}: https://reqres.in/api/users/2\n  |")
    url  = str(input(f"  +--{CYAN}{BRIGHT}[{YELLOW}?{CYAN}]{RESET} INPUT url : {YELLOW}{BRIGHT}"))
    if isURL(url): pass
    else:
        if falseURL(): return
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
    elif http == 3:
        req = "PUT"
    elif http == 4:
        req = "DELETE"

    if http not in [1,2,3,4]:
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
            data_json = dumps(dict([tuple(d.split('=')) for d in data.split('&')]))
            data_query = '&'.join([f"{k}={v}" for k, v in loads(data_json).items()])
        except ValueError as e:
            print(f"\n {CYAN}{BRIGHT}[{YELLOW}#{CYAN}] {GREEN}RESULT{RESET}:\n  |")
            print("  |  {")
            print(f"  |    \"status\" : \"{RED}{BRIGHT}error{RESET}\",")
            print(f"  |    \"message\": \"{CYAN}{BRIGHT}{e}{RESET}\"")
            print("  |  }")
            print(f"  |", end='')
            return

        print()
        system(f'curl -s -X {req} -d "{data_query}" {url} | jq > {FILENAME}')
    else:
        system(f"curl -s -X {req} \"{url}\" | jq > {FILENAME}")

    print(f" {CYAN}{BRIGHT}[{YELLOW}#{CYAN}] {GREEN}RESULT{RESET}:\n")

    if path.isfile(FILENAME):
        with open(FILENAME, "r") as f:
            lines = f.readlines()

        with open(FILENAME, "w") as f:
            for line in lines:
                # f.write('  |  ' + line)
                f.write('     ' + line)

        readFileName(FILENAME)

    else:
        print(f"\n {CYAN}{BRIGHT}[{YELLOW}#{CYAN}] {GREEN}RESULT{RESET}:\n  |")
        print("  |  {")
        print(f"  |    \"status\" : \"{RED}{BRIGHT}error{RESET}\",")
        print(f"  |    \"message\": \"{CYAN}{BRIGHT}file {FILENAME} tidak ditemukan!{RESET}\"")
        print("  |  }")
        print(f"  |\n {CYAN}{BRIGHT}[{YELLOW}#{CYAN}] {RESET}tekan apa saja untuk {BRIGHT}{YELLOW}keluar{RESET}!", end='')
        exit(0)

if __name__ == "__main__":
    try:
        system("title Mini-project: TEST-API @syaauqqii" if name=='nt' else "")
        while True:
            # main program
            main()
            print(f"\n {CYAN}{BRIGHT}[{YELLOW}!{CYAN}] {RESET}tekan {RED}{BRIGHT}[ESC] {RESET}untuk {YELLOW}{BRIGHT}keluar{RESET}!", end='')
            if getch() == b'\x1b': print(); break # [ESC] -> Keluar
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
            exit(0)
        exit(0)
