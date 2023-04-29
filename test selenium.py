from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Coloque o caminho do seu chromedriver aqui
chromedriver_path = "/path/to/chromedriver"

# Inicie o driver do Chrome
driver = webdriver.Chrome(chromedriver_path)

# Defina o tempo de espera implícita
driver.implicitly_wait(10)

# Abra o site do Yahoo
driver.get("https://www.nuinvest.com.br/autenticacao/")

# Encontrar os campos de email e senha e preenchê-los
email_field = driver.find_element(By.XPATH, '//*[@id="username"]')
email_field.send_keys('478.239.738-04')

senha_field = driver.find_element(By.XPATH, '//*[@id="password"]')
senha_field.send_keys('Mgg09@rock')

senha_field.send_keys(Keys.RETURN)

driver.find_element(By.XPATH, '//*[@id="customLink"]').click()

driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/section/div/div/greg-modal[1]/div/div[2]/greg-button').click()

driver.find_element(By.XPATH, '//*[@id="greg-input"]')
# senha_field.send_keys('Mgg09@rock')

# Aguarde um pouco para o navegador carregar os resultados da pesquisa
time.sleep(60)
# senha_field.send_keys('Mgg09@rock')


