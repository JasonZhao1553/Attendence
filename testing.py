import os
import time
exe = 'UI.py'

for root, dirs, files in os.walk(r'C:'):
    for name in files:
        if name == exe:
            print (os.path.abspath(os.path.join(root, name)))
print("Hello")

# output
# D:\python\note\something.exe
