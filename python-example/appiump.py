from appium import webdriver 
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.options.android import UiAutomator2Options

# Definindo as opções
options = UiAutomator2Options()
options.device_name = "emulator-5554"
options.avd = "samsung_galaxy_s10_14.0"
options.automation_name = "UiAutomator2"
options.app = "/app/calculadora.apk"
options.full_reset = True

# Inicializando o driver com as opções
driver = webdriver.Remote('http://127.0.0.1:4723', options=options)

import time ; time.sleep(10)

#Numeros da calculardora
num1 = driver.find_element(by=AppiumBy.ID, value="com.google.android.calculator:id/digit_1")
num2 = driver.find_element(by=AppiumBy.ID, value="com.google.android.calculator:id/digit_2")
num3 = driver.find_element(by=AppiumBy.ID, value="com.google.android.calculator:id/digit_3")
num4 = driver.find_element(by=AppiumBy.ID, value="com.google.android.calculator:id/digit_4")
num5 = driver.find_element(by=AppiumBy.ID, value="com.google.android.calculator:id/digit_5")
num6 = driver.find_element(by=AppiumBy.ID, value="com.google.android.calculator:id/digit_6")
num7 = driver.find_element(by=AppiumBy.ID, value="com.google.android.calculator:id/digit_7")
num8 = driver.find_element(by=AppiumBy.ID, value="com.google.android.calculator:id/digit_8")
num9 = driver.find_element(by=AppiumBy.ID, value="com.google.android.calculator:id/digit_9")


#Operadores
somar = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="plus")
multi = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="multiply")
divis = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="divide")
subtr = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="minus")

#Realiza operação
realiza_operacao = WebDriverWait(driver,15).until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID,"equals")))


num1.click()
somar.click()
num7.click()
realiza_operacao.click()

soma = int(num1.text)+int(num7.text)

time.sleep(5)
resultado = driver.find_element(by=AppiumBy.ID, value="com.google.android.calculator:id/result_final")


assert int(resultado.text) == soma
print(f'Resultado da soma foi: {soma}')

numero_atual = int(resultado.text)

multi.click()
num5.click()
realiza_operacao.click()

assert numero_atual*int(num5.text) == int(resultado.text)

numero_atual = int(resultado.text)

# import ipdb; ipdb.sset_trace()

print(f'Multiplicação feita, novo valor é {numero_atual}')

