from os import system, path, name
from re import compile, match, IGNORECASE
from json import dumps, loads

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
    print("\n  {")
    print("    \"status\" : \"error\",")
    print("    \"message\": \"yang anda inputkan bukanlah URL yang valid!\"")
    print("  }")
    print("\n\n [!] tekan apa saja untuk keluar!", end='')
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
    print("""\n     $$$$$$$$\\ $$$$$$$$\\  $$$$$$\\ $$$$$$$$\\       $$$$$$\\  $$$$$$$\\ $$$$$$\\
     \\__$$  __|$$  _____|$$  __$$\\\\__$$  __|     $$  __$$\ $$  __$$\\\\_$$  _|
        $$ |   $$ |      $$ /  \__|  $$ |        $$ /  $$ |$$ |  $$ | $$ |
        $$ |   $$$$$\    \\$$$$$$\\    $$ |$$$$$$\\ $$$$$$$$ |$$$$$$$  | $$ |
        $$ |   $$  __|    \\____$$\   $$ |\______|$$  __$$ |$$  ____/  $$ |
        $$ |   $$ |      $$\\   $$ |  $$ |        $$ |  $$ |$$ |       $$ |
        $$ |   $$$$$$$$\\ \\$$$$$$  |  $$ |        $$ |  $$ |$$ |     $$$$$$\\
        \\__|   \\________| \\______/   \\__|        \\__|  \\__|\\__|     \\______|
    \n                    [ IG: @syaauqqii | GP2D-API CLI ]""")

def main():
    filename = "result.json"
    clearScreen()
    banner()
    print("\n     [#] FORMAT INPUT url:\n         > ex: https://reqres.in/api/users")
    url  = str(input("\n [>] INPUT url : "))
    if isURL(url): pass
    else: falseURL()
    print("\n     [#] HTTP:\n         [1] GET    [3] PUT\n         [2] POST   [4] DELETE\n")
    http = int(input(" [>] INPUT http: (1..4) "))
    print()

    if http == 1:
        req = "GET"
    elif http == 2:
        req = "POST"
    elif http == 3:
        req = "PUT"
    elif http == 4:
        req = "DELETE"

    if http in [2, 3]:
        print("     [#] FORMAT INPUT data:\n         > ex: name=dimas&job=tidur\n")
        data = input(" [>] INPUT data: ")
        data_json = dumps(dict([tuple(d.split('=')) for d in data.split('&')]))
        data_query = '&'.join([f"{k}={v}" for k, v in loads(data_json).items()])
        print()
        cmd = f'curl -s -X {req} -d "{data_query}" {url} | jq > result.json'
        system(cmd)
    else:
        system(f"curl -s -X {req} \"{url}\" | jq > result.json")

    print(" [#] RESULT:\n")

    if path.isfile(filename):
        with open(filename, "r") as f:
            lines = f.readlines()

        with open(filename, "w") as f:
            for line in lines:
                f.write('  ' + line)

        readFileName(filename)

    else:
        print("Result file is missing")

if __name__ == "__main__":
    try:
        system("title Mini-project: TEST-API @syaauqqii" if name=='nt' else "")
        while True:
             main()
             print("\n\n [!] tekan [ENTER] / [ESC] untuk keluar!", end='')
             if getch() in [b'\r', b'\x1b']: print(); break 
    except KeyboardInterrupt:
        print("\n\n  {")
        print("    \"status\" : \"success\",")
        print("    \"message\": \"berhasil exit dengan CTRL + C\"")
        print("  }")
        print("\n\n [!] tekan apa saja untuk keluar!", end='')
        try:
            input("")
        except KeyboardInterrupt:
            print()
            exit(0)
        exit(0)
