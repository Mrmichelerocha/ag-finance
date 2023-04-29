from uagents.setup import fund_agent_if_low
from uagents import Agent, Context, Model
from uagents.resolver import RulesBasedResolver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import urllib.request
import requests
import time

PURCHASE_ADDRESS = "agent1qv5dcwn5gnpqflvwzu2dw38ftvaz2ltjrhs82g3yljgl9qd66v6mv5k5j2h"

purchase = Agent(
    name="purchase",
    port=8020,
    seed="purchase secret phrase",
    resolve=RulesBasedResolver(
        {
            PURCHASE_ADDRESS: "http://127.0.0.1:8020/submit",

        }
    ),
)

fund_agent_if_low(purchase.wallet.address())

class Message(Model):
    message: str
    data: int
    
class House_env():        
    def update_perception(ctx: Context):
        # Sobe 'crença' | atualiza dado
        if(House_data_purchase.checked_purchase):
            data = {"purchase_status": House_data_purchase.status,}  
            ctx.storage.set('desire_purchase', data)
    
class House_data_purchase():
    aux = 0    
    status = None
    checked_purchase = None
    
    def pesquisar_no_yahoo(query):
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
        
        driver.find_element(By.XPATH, '//*[@id="app"]')

        # Aguarde um pouco para o navegador carregar os resultados da pesquisa
        time.sleep(60)

        # Feche o navegador
        driver.quit()
        
    def checked_data(ctx: Context):
        # Entra 'banco' pega status da purchase 
        url = "http://192.168.0.111/purchase"
        response = requests.get(url)
        
        if response.status_code == 200:
            highest_id = 0
            House_data_purchase.status = 0.0
            
            data = response.json()
            for item in data["purchase_dict"]:
                if item["id"] >= highest_id:
                    highest_id = item["id"]
                    House_data_purchase.status = item["purchase_status"]
                    House_data_purchase.brain_post()

            print("Highest ID:", highest_id)
            print(House_data_purchase.status)
            House_data_purchase.checked_purchase = True
            House_env.update_perception(ctx)
            print(House_data_purchase.checked_purchase)
        else:
            print("Falha ao fazer a solicitação.") 
            
    def brain_post():
        print("adiciono status ao meu cerebro")
        url = "http://127.0.0.1:8000/datapurchase/"
        
        if House_data_purchase.status != House_data_purchase.aux:
            data = {
                "status": House_data_purchase.status,
            }
            response = requests.post(url, data)
            House_data_purchase.aux = House_data_purchase.status

            if response.status_code == 201:
                print("Post bem-sucedido!")
            else:
                print("Post falhou.")
        else:
            pass

@purchase.on_interval(period=30.5)
async def waiting_status(ctx: Context):
    House_data_purchase.pesquisar_no_yahoo("teste michele")
    if(House_data_purchase.checked_purchase):
        pass         

if __name__ == "__main__":
    purchase.run()
