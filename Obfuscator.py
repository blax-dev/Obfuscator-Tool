import os
import random
import zlib
import lzma
from marshal import dumps

os.system('cls' if os.name == 'nt' else 'clear')

def redblue(text):
    os.system("")
    faded = ""
    red = 255
    blue = 0
    for line in text.splitlines():
        faded += (f"\033[38;2;{red};0;{blue}m{line}\033[0m\n")
        if blue < 255:
            blue += 15
            if blue > 255:
                blue = 255
        if red > 0:
            red -= 15
            if red < 0:
                red = 0
    return faded

print(redblue('''
 ▒█████   ▄▄▄▄     █████▒█    ██   ██████  ▄████▄   ▄▄▄     ▄▄▄█████▓ ▒█████   ██▀███  
▒██▒  ██▒▓█████▄ ▓██   ▒ ██  ▓██▒▒██    ▒ ▒██▀ ▀█  ▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
▒██░  ██▒▒██▒ ▄██▒████ ░▓██  ▒██░░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
▒██   ██░▒██░█▀  ░▓█▒  ░▓▓█  ░██░  ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  
░ ████▓▒░░▓█  ▀█▓░▒█░   ▒▒█████▓ ▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
░ ▒░▒░▒░ ░▒▓███▀▒ ▒ ░   ░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
  ░ ▒ ▒░ ▒░▒   ░  ░     ░░▒░ ░ ░ ░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░   ░      ░ ▒ ▒░   ░▒ ░ ▒░
░ ░ ░ ▒   ░    ░  ░ ░    ░░░ ░ ░ ░  ░  ░  ░          ░   ▒    ░      ░ ░ ░ ▒    ░░   ░ 
    ░ ░   ░                ░           ░  ░ ░            ░  ░            ░ ░     ░
               ░                          ░
                  By https://github.com/blax_dev     
                                   
'''))

junk = "__byblaxt__" * 15

file = input('Metez le nom de votre fichier dans le dossiers : ')

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def genvar():
    var = ''
    for i in range(10):
        var += random.choice(chars)
    return var

def compress(text):
    ok = zlib.compress(text.encode())
    ok = lzma.compress(ok)
    return ok

def encrypt1(text):
    src = compile(text, 'coduter', 'exec')
    ma = dumps(src)
    s = f'{junk}="{junk}";{junk}="{junk}";{junk}="{junk}";exec(loads({ma}));{junk}="{junk}";{junk}="{junk}"'
    compresse = compress(s)
    oke = f"import zlib,lzma\nexec(zlib.decompress(lzma.decompress({compresse})))"
    return oke

def encrypt2(text):
    sta = genvar()
    code = text
    s = compile(code, 'coduter', 'exec')
    maa = dumps(s)
    stub2 = f'from marshal import loads;exec(loads({maa}));'
    fin = f'{junk}="{junk}";{junk}="{junk}";{stub2}{junk}="{junk}";{junk}="{junk}";'
    return fin

if not os.path.isfile(file):
    print('File not found')
    exit()
print('\n')
print('[+] encrypting ...')

# Modifier cette ligne pour utiliser l'encodage utf-8
with open(file, 'r', encoding='utf-8') as f:
    code = f.read()

code = encrypt1(code)
code = encrypt2(code)
print('[+] done')
print('\n')
name = file.split('/')[-1]
name = name.split('.')[0]
with open(f'{name}-obf.py', 'w', encoding='utf-8') as f:
    f.write(code)

os.system('cls' if os.name == 'nt' else 'clear')
print(f'Votre fichier est obfusquer et enregistré sous le nom de {name}-obf.py')
print('\n')
print('Merci d’utiliser ce tools')
import time
time.sleep(5)
exit()
