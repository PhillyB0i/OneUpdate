################################################################
#############Created by Philip Boubenchikov        #############
#############For RapidOne&SAP Software             #############
#############Build 1.0.6                           #############
################################################################
import os
import requests # pip install requests
import zipfile
import sys
import subprocess
from requests.sessions import dispatch_hook
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from colorama import Fore, Back, Style
from time import sleep

#Chromedriver URL, choices, change to cwd path
Durl = 'https://chromedriver.storage.googleapis.com/99.0.4844.51/chromedriver_win32.zip'
chromedriver = requests.get(Durl)
yesChoice = ['y', 'Y', 'ye', 'Ye', 'Yes', 'yes', 'YES', 'YE']
noChoice = ['n', 'N', 'no', 'No', 'Nah', 'nah', 'NAH', 'NO']
FileName = chromedriver.url[Durl.rfind('/')+1:]
path = os.getcwd()


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


#Download Yes or No and extract from ZIP (Not required if file presant on PC)
print('Made by Philip Boubenchikov / RapidImage')
print('Build 1.0.6')

while True:
        DownloadFile = input("Download required files? (Y/N): ").lower()
        if DownloadFile not in yesChoice or noChoice:
            print("Please Enter Valid Input!!")
    
        if DownloadFile in yesChoice:
            with open(FileName, 'wb') as f:
                for chunk in chromedriver.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        print('Downloading...')            

        if DownloadFile in yesChoice:
            with zipfile.ZipFile('chromedriver_win32.zip', 'r') as zip_ref:
                zip_ref.extract('chromedriver.exe')
            print('Extracting...')
            clearConsole()
            break

        elif DownloadFile in noChoice:
            print('Ok..Skipping.')
            clearConsole()
            break

#SAP Kill
while True:

        Customer = input("Type Customer Name (For M4U type name R#_NAME):")
        print('Working..')
        driver = webdriver.Chrome('chromedriver.exe')
        driver.get("http://localhost:5001/")
        sleep(2)
        search = driver.find_element_by_xpath('/html/body/div/main/div/div/div[1]/form/p/input[1]')
        search.send_keys(Customer)
        search.send_keys(Keys.RETURN)
        sleep(2)
        elem = driver.find_element_by_xpath('/html/body/div/main/div/table/thead/tr/th[1]/input')
        kill = driver.find_element_by_xpath('/html/body/div/main/div/div/div[4]/form/p/input[1]')
        actions = ActionChains(driver)
        actions.click(elem)
        actions.click(kill)
        actions.perform()
        driver.close()
        clearConsole()
        break

 
while True:
        WannaUp = input('Would you like to update?(Y/N):')

        if WannaUp in noChoice:
                print('Ok.. Skipping.')
                exit(0)


        if WannaUp in yesChoice:
                ChooseServer = input("Choose Server: [ROTS1==1, ROTS2==2, ROTS3==3, M4U-IIS==4]:")
                ROTS1 = '1'
                ROTS2 = '2'
                ROTS3 = '3'
                M4U = '4'

        if ChooseServer in ROTS1:
                Version = input('Which Version (type RapidOne_Version#.#.# or DEVELOP): ')
                os.system(R"powershell.exe cd C:\users\sap1.RAPIDCLOUD\desktop")
                os.system(R"powershell.exe Import-Module C:\tmp\sqlserver.21.1.18135\SqlServer.psm1")
                os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition " + Version + " -forceConfig -deployEnvironments " + Customer)
                exit(0)

        if ChooseServer in ROTS2:
                Version = input('Which Version (type RapidOne_Version#.#.# or DEVELOP): ')
                os.system(R"powershell.exe cd c:\users\sap1\desktop")
                os.system(R"powershell.exe C:\Users\sap1\Desktop\PublishLocal.ps1 -configPath C:\Users\sap1\Desktop\RoTs2Config.ps1 -buildDefinition " + Version + " -forceConfig -deployEnvironments " + Customer)
                exit(0)

        if ChooseServer in ROTS3:
                Version = input('Which Version (type RapidOne_Version#.#.# or DEVELOP): ')
                os.system(R"powershell.exe cd C:\users\vlad\desktop")
                os.system(R"powershell.exe C:\Users\vlad\Desktop\PublishLocal.ps1 -configPath C:\Users\vlad\Desktop\RoTs3Config.ps1 -buildDefinition " + Version + " -forceConfig -deployEnvironments " + Customer)
                exit(0)

        if ChooseServer in M4U:
                Version = input('Which Version (type RapidOne_Version#.#.# or DEVELOP): ')
                os.system(R"powershell.exe cd c:\scripts")
                os.system(R"powershell.exe C:\Scripts\PublishLocal.ps1 -configPath C:\Scripts\RoTs3Config.ps1 -buildDefinition " + Version + " -forceConfig -deployEnvironments " + Customer)
                exit(0)