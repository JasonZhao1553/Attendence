import webbrowser
from selenium import webdriver
import time
from keyboard import press
import getpass
import pickle
import os


def execute():
    exe = 'credentials.pickle'
    final_path = ""

    for root, dirs, files in os.walk(r'C:'):
        for name in files:
            if name == exe:
                final_path = os.path.abspath(root)

    final_path = os.path.join(final_path, "credentials.pickle")

    raw_data = open(final_path , "rb")
    credentials_array = pickle.load(raw_data)

    username = credentials_array[0]
    email = username + "@student.methacton.org"
    password = credentials_array[1]

    PATH = "C:\Program Files (x86)\chromedriver.exe"
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches" , ["enable-logging"])
    driver = webdriver.Chrome(options=options, executable_path=r'C:\Program Files (x86)\chromedriver.exe')
    driver.get("https://classroom.google.com/u/1/c/NzMyMTY1NDYzNzBa")

    driver.find_element_by_id("identifierId").send_keys(email)

    driver.find_element_by_id("identifierNext").click()

    time.sleep(10)

    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("signin").click()

    time.sleep(10)

    driver.find_element_by_class_name("VfPpkd-RLmnJb").click()

    time.sleep(10)

    driver.find_element_by_class_name("GQW44b").click()

    time.sleep(10)

    driver.find_element_by_class_name("J5AvUe").click()

    time.sleep(10)

    driver.find_element_by_class_name("appsMaterialWizToggleRadiogroupRadioButtonContainer").click()

    driver.find_element_by_class_name("appsMaterialWizButtonPaperbuttonContent.exportButtonContent").click()

    driver.quit()

execute()
