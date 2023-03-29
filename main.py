from os import system, path, name
import json
import re

# Menambahkan validasi input URL
def is_url(string):
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// atau https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain
        r'localhost|' # localhost
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ip
        r'(?::\d+)?' # opsional: port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, string) is not None

def main():
    system("title Mini-project: TEST-API @syaauqqii" if name=='nt' else "")
    system("cls" if name=='nt' else "clear")

    # Design: https://patorjk.com/software/taag/#p=display&f=Big%20Money-nw&t=
    print("\n $$$$$$$$\\ $$$$$$$$\\  $$$$$$\\ $$$$$$$$\\       $$$$$$\\  $$$$$$$\\ $$$$$$\\ ")
    print(" \\__$$  __|$$  _____|$$  __$$\\\\__$$  __|     $$  __$$\ $$  __$$\\\\_$$  _|")
    print("    $$ |   $$ |      $$ /  \__|  $$ |        $$ /  $$ |$$ |  $$ | $$ |  ")
    print("    $$ |   $$$$$\    \\$$$$$$\\    $$ |$$$$$$\\ $$$$$$$$ |$$$$$$$  | $$ |  ")
    print("    $$ |   $$  __|    \\____$$\   $$ |\______|$$  __$$ |$$  ____/  $$ |  ")
    print("    $$ |   $$ |      $$\\   $$ |  $$ |        $$ |  $$ |$$ |       $$ |  ")
    print("    $$ |   $$$$$$$$\\ \\$$$$$$  |  $$ |        $$ |  $$ |$$ |     $$$$$$\ ")
    print("    \\__|   \\________| \\______/   \\__|        \\__|  \\__|\\__|     \\______|")
    print("\n                    [ IG: @syaauqqii | GP2D-API CLI ]                           ")

    print("\n     [#] FORMAT INPUT url:\n         > ex: https://reqres.in/api/users")
    url  = str(input("\n [>] INPUT url : "))
    if is_url(url):
        pass
    else:
        print("\n  {")
        print("    \"status\" : \"error\",")
        print("    \"message\": \"yang anda inputkan bukanlah URL yang valid!\"")
        print("  }")
        print("\n [!] tekan ENTER untuk keluar! [ENTER]", end='')
        input("")
        exit(0)
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
        data_json = json.dumps(dict([tuple(d.split('=')) for d in data.split('&')]))
        data_query = '&'.join([f"{k}={v}" for k, v in json.loads(data_json).items()])
        print()
        cmd = f'curl -s -X {req} -d "{data_query}" {url} | jq > result.json'
        system(cmd)
    else:
        system(f"curl -s -X {req} \"{url}\" | jq > result.json")

    print(" [#] RESULT:\n")

    if path.isfile("result.json"):
        with open("result.json", "r") as f:
            txt = ' ' + f.read().replace('\n', '\n ')

        try:
            data = json.loads(txt)
        except json.JSONDecodeError as e:
            print(f"Invalid JSON format in result.json: {e}")
            return

        with open("result.json", "w") as f:
            json_string = json.dumps(data, indent=2)
            spaced_json_string = json_string.replace('\n', '\n     ')
            f.write(spaced_json_string)

        system("cat result.json || type result.json")

    else:
        print("Result file is missing")

    print("\n\n [!] ENTER untuk keluar!", end='')
    input("")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # system("cls" if name=='nt' else "clear")
        print("\n\n  {")
        print("    \"status\" : \"success\",")
        print("    \"message\": \"berhasil exit dengan CTRL + C\"")
        print("  }")
        print("\n [!] tekan ENTER untuk keluar! [ENTER]", end='')
        input("")
        exit(0)
