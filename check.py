import subprocess
import pickle
import os
import time

try:
    exe = 'credentials.pickle'
    final_path = ""

    for root, dirs, files in os.walk(r'C:'):
        for name in files:
            if name == exe:
                final_path = os.path.abspath(root)

    final_path = os.path.join(final_path, "credentials.pickle")

    file = open(final_path , "rb")
    credentials = pickle.load(file)
    username = credentials[0]
    password = credentials[1]

    username_length = len(username)
    password_length = len(password)

    if username_length > 4 and password_length > 0:
        subprocess.call([r'C:\Users\jzhao\OneDrive\Desktop\Web\Attendence\run_web.bat'])

except:
        subprocess.call([r'C:\Users\jzhao\OneDrive\Desktop\Web\Attendence\run_UI.bat'])
