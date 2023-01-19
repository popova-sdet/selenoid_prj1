from selenium import webdriver
from time import sleep

capabilities = {
    "browserName": "chrome",
    "browserVersion": "108.0",
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": False,
        "name": "MyTestName",
        "screenResolution": "1920x1080x24",
    }
}

driver = webdriver.Remote(
    command_executor="http://172.17.0.1:4444/wd/hub",
    desired_capabilities=capabilities)

driver.get('https://www.fortinet.com')
driver.maximize_window()
print("Open")
sleep(10)
driver.quit()
print("Close")
