from os import system, path, name
from re import compile, match, IGNORECASE
from json import dumps, loads
try:
    from colorama import Fore, Back, Style
except ModuleNotFoundError:
    system("pip install colorama")
    try:
        from colorama import Fore, Back, init
    except ImportError:
        exit(0)

if name == "posix":
    try:
        from getch import getch
    except ModuleNotFoundError:
        system("pip install getch")
        try:
            from getch import getch
        except ImportError:
            exit(0)
elif name == "nt":
    try:
        from msvcrt import getch
    except ModuleNotFoundError:
        system("pip install msvcrt")
        try:
            from msvcrt import getch
        except ImportError:
            exit(0)

def clearScreen():
    if name == "nt":
        system("cls")
    elif name == "posix":
        system("clear")
    else:
        return

# Menambahkan validasi input URL
def isURL(string):
    regex = compile(
        r'^(?:http|ftp)s?://' # http:// atau https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain
        r'localhost|' # localhost
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ip
        r'(?::\d+)?' # opsional: port
        r'(?:/?|[/?]\S+)$', IGNORECASE)
    return match(regex, string) is not None

def falseURL():
    print("\n " + Fore.CYAN + "[" + Fore.YELLOW + Style.BRIGHT + "#" + Style.RESET_ALL + Fore.CYAN + "]" + Fore.GREEN + Style.BRIGHT + " RESULT" + Style.RESET_ALL + ":\n  |")
    print("  |  {")
    print("  |    \"status\" : \"" + Fore.RED + Style.BRIGHT + "error" + Style.RESET_ALL + "\",")
    print("  |    \"message\": \"" + Fore.CYAN + Style.BRIGHT + "yang anda inputkan bukanlah URL yang valid!" + Style.RESET_ALL + "\"")
    print("  |  }")
    print("  |\n " + Fore.CYAN + "[" + Fore.YELLOW + Style.BRIGHT + "#" + Style.RESET_ALL + Fore.CYAN + "]" + Style.RESET_ALL  + " tekan apa saja untuk " + Fore.YELLOW + "keluar" + Style.RESET_ALL + "!", end='')
    input("")
    exit(0)

def readFileName(filename):
    if name == "nt":
        system(f"type {filename}")
    elif name == "posix":
        system(f"cat {filename}")
    else:
        return

def banner():
   # Design: https://patorjk.com/software/taag/#p=display&f=Big%20Money-nw&t=
    print(Fore.CYAN + """\n     $$$$$$$$\\ $$$$$$$$\\  $$$$$$\\ $$$$$$$$\\       $$$$$$\\  $$$$$$$\\ $$$$$$\\
     \\__$$  __|$$  _____|$$  __$$\\\\__$$  __|     $$  __$$\ $$  __$$\\\\_$$  _|
        $$ |   $$ |      $$ /  \__|  $$ |        $$ /  $$ |$$ |  $$ | $$ |
        $$ |   $$$$$\    \\$$$$$$\\    $$ |$$$$$$\\ $$$$$$$$ |$$$$$$$  | $$ |
        $$ |   $$  __|    \\____$$\   $$ |\______|$$  __$$ |$$  ____/  $$ |
        $$ |   $$ |      $$\\   $$ |  $$ |        $$ |  $$ |$$ |       $$ |
        $$ |   $$$$$$$$\\ \\$$$$$$  |  $$ |        $$ |  $$ |$$ |     $$$$$$\\
        \\__|   \\________| \\______/   \\__|        \\__|  \\__|\\__|     \\______|
    \n                     [ """ + Fore.RED + Style.BRIGHT + "IG" + Style.RESET_ALL + ": @syaauqqii | GP2D-API CLI " + Fore.CYAN + "]" + Style.RESET_ALL)

def main():
    filename = "result.json"
    clearScreen()
    banner()
    print("\n " + Fore.CYAN + "[" + Fore.YELLOW + Style.BRIGHT + "#" + Style.RESET_ALL + Fore.CYAN + "]" + Fore.GREEN + Style.BRIGHT + " FORMAT INPUT url" + Style.RESET_ALL + ":\n  |  " + Fore.CYAN + "> ex" + Style.RESET_ALL + ": https://reqres.in/api/users/2\n  |")
    url  = str(input("  +--" + Fore.CYAN + "[" + Fore.YELLOW + Style.BRIGHT + "!" + Style.RESET_ALL + Fore.CYAN + "]"  + Style.RESET_ALL  + " INPUT url : " + Fore.YELLOW + Style.BRIGHT))
    if isURL(url): pass
    else: falseURL()
    print("\n " + Fore.CYAN + "[" + Fore.YELLOW + Style.BRIGHT + "#" + Style.RESET_ALL + Fore.CYAN + "]" + Fore.GREEN + Style.BRIGHT + " HTTP request" + Style.RESET_ALL + ":\n  |  " + Fore.CYAN + "> options" + Style.RESET_ALL + ": 1. GET    3. PUT\n  |             2. POST   4. DELETE\n  |")
    http = int(input("  +--" + Fore.CYAN + "[" + Fore.YELLOW + Style.BRIGHT + "!" + Style.RESET_ALL + Fore.CYAN + "]"  + Style.RESET_ALL  + " INPUT http: (1..4) " + Fore.YELLOW + Style.BRIGHT))
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
        print(" " + Fore.CYAN + "[" + Fore.YELLOW + Style.BRIGHT + "#" + Style.RESET_ALL + Fore.CYAN + "]" + Fore.GREEN + Style.BRIGHT + " RESULT" + Style.RESET_ALL + ":\n  |")
        print("  |  {")
        print("  |    \"status\" : \"" + Fore.RED + Style.BRIGHT + "error" + Style.RESET_ALL + "\",")
        print("  |    \"message\": \"" + Fore.CYAN + Style.BRIGHT + "yang anda inputkan tidak ada di pilihan!" + Style.RESET_ALL + "\"")
        print("  |  }")
        print("  |\n " + Fore.CYAN + "[" + Fore.YELLOW + Style.BRIGHT + "#" + Style.RESET_ALL + Fore.CYAN + "]" + Style.RESET_ALL  + " tekan apa saja untuk " + Fore.YELLOW + "keluar" + Style.RESET_ALL + "!", end='')
        input("")
        exit(0)

    if http in [2, 3]:
        print(" " + Fore.CYAN + "[" + Fore.YELLOW + Style.BRIGHT + "#" + Style.RESET_ALL + Fore.CYAN + "]" + Fore.GREEN + Style.BRIGHT + " FORMAT INPUT data" + Style.RESET_ALL + ":\n  |  " + Fore.CYAN + "> ex" + Style.RESET_ALL + ": name=dimas&job=tidur\n  |"+ Style.RESET_ALL)
        data = input("  +--" + Fore.CYAN + "[" + Fore.YELLOW + Style.BRIGHT + "?" + Style.RESET_ALL + Fore.CYAN + "]"  + Style.RESET_ALL  + " INPUT data: " + Fore.YELLOW + Style.BRIGHT)
        data_json = dumps(dict([tuple(d.split('=')) for d in data.split('&')]))
        data_query = '&'.join([f"{k}={v}" for k, v in loads(data_json).items()])
        print()
        cmd = f'curl -s -X {req} -d "{data_query}" {url} | jq > result.json'
        system(cmd)
    else:
        system(f"curl -s -X {req} \"{url}\" | jq > result.json")

    print(" " + Fore.CYAN + "[" + Fore.YELLOW + Style.BRIGHT + "#" + Style.RESET_ALL + Fore.CYAN + "]" + Fore.GREEN + Style.BRIGHT + " RESULT" + Style.RESET_ALL + ":\n  |")

    if path.isfile(filename):
        with open(filename, "r") as f:
            lines = f.readlines()

        with open(filename, "w") as f:
            for line in lines:
                f.write('  |  ' + line)

        readFileName(filename)

    else:
        print("\n " + Fore.CYAN + "[" + Fore.YELLOW + Style.BRIGHT + "#" + Style.RESET_ALL + Fore.CYAN + "]" + Fore.GREEN + Style.BRIGHT + " RESULT" + Style.RESET_ALL + ":\n  |")
        print("  |  {")
        print("  |    \"status\" : \"" + Fore.RED + Style.BRIGHT + "error" + Style.RESET_ALL + "\",")
        print("  |    \"message\": \"" + Fore.CYAN + Style.BRIGHT + f"file {filename} tidak ditemukan!" + Style.RESET_ALL + "\"")
        print("  |  }")
        print("  |\n " + Fore.CYAN + "[" + Fore.YELLOW + Style.BRIGHT + "#" + Style.RESET_ALL + Fore.CYAN + "]" + Style.RESET_ALL  + " tekan apa saja untuk " + Fore.YELLOW + "keluar" + Style.RESET_ALL + "!", end='')
        exit(0)

if __name__ == "__main__":
    try:
        system("title Mini-project: TEST-API @syaauqqii" if name=='nt' else "")
        while True:
             main()
             print("  |\n  +--" + Fore.CYAN + "[" + Fore.YELLOW + Style.BRIGHT + "!" + Style.RESET_ALL + Fore.CYAN + "]" + Style.RESET_ALL + " tekan " + Fore.RED + Style.BRIGHT + "[ESC]" + Style.RESET_ALL + " untuk " + Fore.YELLOW + Style.BRIGHT + "keluar" + Style.RESET_ALL + "!", end='')
             if getch() == b'\x1b': print(); break 
    except KeyboardInterrupt:
        print("\n\n " + Fore.CYAN + "[" + Fore.YELLOW + Style.BRIGHT + "#" + Style.RESET_ALL + Fore.CYAN + "]" + Fore.GREEN + Style.BRIGHT + " RESULT" + Style.RESET_ALL + ":\n  |")
        print("  |  {")
        print("  |    \"status\" : \"" + Fore.GREEN + Style.BRIGHT + "success" + Style.RESET_ALL + "\",")
        print("  |    \"message\": \"" + Fore.CYAN + Style.BRIGHT + "berhasil exit dengan CTRL + C" + Style.RESET_ALL + "\"")
        print("  |  }")
        print("  |\n " + Fore.CYAN + "[" + Fore.YELLOW + Style.BRIGHT + "#" + Style.RESET_ALL + Fore.CYAN + "]" + Style.RESET_ALL  + " tekan apa saja untuk " + Fore.YELLOW + "keluar" + Style.RESET_ALL + "!", end='')
        try:
            input("")
        except KeyboardInterrupt:
            print()
            exit(0)
        exit(0)
