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

key = input(RED + "Please enter your encryption key: " + GREEN)
message = input(RED + "Please enter the string you want to decrypt: " + GREEN)

f = Fernet(key.encode())

decrypted = f.decrypt(message.encode())

print(RED + "\nDecrypted String\n >> " + GREEN + decrypted.decode() + END)
