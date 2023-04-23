import ctypes
import os
import sys


def make_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


print('----------------------------------------------------------')
print("SFC SCAN NOW WITH PYTHON [ADMIN]")
print('----------------------------------------------------------')

print("Execute sfc / scannow ? ( y| n )")
choice = ['y', 'n']
user_choice = "n"
try:
    user_choice = input("Enter your validation : ").lower()
    if user_choice not in choice:
        raise TypeError
except ValueError:
    print("Enter (y or n) ")
except TypeError:
    print("Don't enter anything else ")

if user_choice == "y":
    if make_admin():
        os.system("sfc /scannow")
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, "".join(sys.argv), None, 1)
else:
    print("Good bye ... ")
