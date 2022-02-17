from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from time import sleep
from os import listdir


path = "D:\\Sowesign-shotcut\\"


def typePinCode(driver, pin):
    keySet = driver.find_elements(By.CLASS_NAME, "key")
    for e in pin:
        for keyElement in keySet:
            if keyElement.text == e:
                keyElement.click()
        sleep(0.1)


def typeClassCode(driver, code):
    keyArray = [Keys.NUMPAD0,
                Keys.NUMPAD1,
                Keys.NUMPAD2,
                Keys.NUMPAD3,
                Keys.NUMPAD4,
                Keys.NUMPAD5,
                Keys.NUMPAD6,
                Keys.NUMPAD7,
                Keys.NUMPAD8,
                Keys.NUMPAD9]
    for num in code:
        ActionChains(driver).send_keys(keyArray[int(num)]).perform()
        sleep(0.1)


def drawSig(sigFile):
    pass


def getCreds():
    print("Who Are You ?")
    credsAvailable = listdir(path + "\\creds")
    for i in range(len(credsAvailable)):
        print(str(i + 1) + ") " + ".".join(credsAvailable[i].split(".")[:-1]))
    answer = int(input("> "))
    finalCreds = []
    with open(path + "creds\\" + credsAvailable[answer-1], "r") as f:
        for i in range(4):
            finalCreds.append(f.readline().strip())
    return finalCreds


def main():
    SCHOOLCODE, PERSONALCODE, PINCODE, SIGNATUREFILE = getCreds()
    UNIQUECODE = input("Entre le code de la séance :\n> ")
    s = Service("chromedriver.exe")
    print("Launching driver")
    driver = webdriver.Chrome(service=s)
    sleep(1)
    print("Going to app.sowesign.com")
    driver.get("https://app.sowesign.com/")
    sleep(1)
    print("Typing School Code : ")
    driver.find_element(By.ID, "codeCustomer").send_keys(SCHOOLCODE)
    print("Typing Personal Code : ")
    driver.find_element(By.ID, "codeId").send_keys(PERSONALCODE)
    typePinCode(driver, PINCODE)
    driver.find_element(By.CLASS_NAME, "button").click()
    sleep(7)
    typeClassCode(driver, UNIQUECODE)
    sleep(5)
    drawSig(SIGNATUREFILE)
    # click on da button


if __name__ == '__main__':
    main()
