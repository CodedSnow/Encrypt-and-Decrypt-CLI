from cryptography.fernet import Fernet
import os
import sys

BLUE = '\33[94m'
LightBlue = '\033[94m'
RED = '\033[91m'
GREEN = '\033[32m'
END = '\033[0m'

os.system("clear || cls")
sys.stdout.write(LightBlue + """\n ██████╗ ██████╗ ██████╗ ███████╗██████╗ ███████╗███╗   ██╗ ██████╗ ██╗    ██╗
██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗██╔════╝████╗  ██║██╔═══██╗██║    ██║
██║     ██║   ██║██║  ██║█████╗  ██║  ██║███████╗██╔██╗ ██║██║   ██║██║ █╗ ██║
██║     ██║   ██║██║  ██║██╔══╝  ██║  ██║╚════██║██║╚██╗██║██║   ██║██║███╗██║
╚██████╗╚██████╔╝██████╔╝███████╗██████╔╝███████║██║ ╚████║╚██████╔╝╚███╔███╔╝
 ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═════╝ ╚══════╝╚═╝  ╚═══╝ ╚═════╝  ╚══╝╚══╝ 
                                                                              """ + END + BLUE + "\n==============================================================================\n\n" + END)

message = input(RED + "Please enter the string you want to encrypt: " + GREEN)

key = Fernet.generate_key()
f = Fernet(key)

encrypted = f.encrypt(message.encode())
decrypted = f.decrypt(encrypted)

print(RED + "\nEncryption Key\n >> " + GREEN + key.decode())
print(RED + "Encrypted String\n >> " + GREEN + encrypted.decode() + END)
