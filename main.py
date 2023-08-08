from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

driver.get('https://coursera.org?authMode=login')

time.sleep(2.7)

Flag = True

while Flag:

    driver.find_element(By.ID, "email").send_keys(input('email cousera: '))

    print("[+] email added")

    driver.find_element(By.ID, "password").send_keys(
        input('password coursera: '))

    print("[+] password added")

    confirm = input('Are you ready to submit ? | Y/N : ')

    match confirm:
        case 'Y' | 'YES' | 'yes' | 'y':
            Flag = False
            driver.find_element(By.CLASS_NAME, "_6dgzsvq").click()
            print("[+] Login awaiting successful status")

        case 'N' | 'NO' | 'no' | 'n':
            x = input(
                "[!] Action Relod \n [?] you want to continue or exit ? | C/E : ")
            match x:
                case 'C' | 'c' | 'CONTINUE' | 'Continue' | 'continue':
                    driver.find_element(By.ID, "email").clear()
                    driver.find_element(By.ID, "password").clear()
                    Flag = True

                case 'E' | 'e' | 'EXIT' | 'Exit' | 'exit':
                    driver.close()
                    print('Program Close')
                    break
