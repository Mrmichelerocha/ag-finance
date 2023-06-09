# AÇÔES DISPONÍVEIS #
# Cada função/método corresponde a uma ação (por momento apenas simulada)
from datetime import datetime
from time import sleep


class Action:
    def list_symbol(self):
        list_symbol = ["ação1", "ação2"]
        return list_symbol
    
    def checked_data_min(self, ctx):
        list_symbol = self.list_symbol() 
        # Percorre cada ação na lista
        for symbol in list_symbol:
            data_base = False # aqui faz um HTTP GET no banco e recupera status da compra true|false
            if data_base == False:
                self.arbitration_min(ctx, symbol)
            else:
                return False
            
    def checked_data_max(self, ctx):
        list_symbol = self.list_symbol() 
        # Percorre cada ação na lista
        for symbol in list_symbol:
            data_base = True # aqui faz um HTTP GET no banco e recupera status da compra true|false
            if data_base == True:
                self.arbitration_max(ctx, symbol)
            else:
                return False
        
    def arbitration_min(self, ctx, symbol):
            # Faz a previsão do valor "low"
            low = self.preview_low(ctx, symbol)
            print(low)
            # Analisa o valor atual 
            now = self.price_now(ctx, symbol)
            print(now)
            # Verifica se o valor "low" é igual ao preço atual
            if low > now:
                self.buy(ctx, symbol, low)
            
    def arbitration_max(self, ctx, symbol):
        # Faz a previsão do valor "low"
        high = self.preview_high(ctx, symbol)
        print(high)
        # Analisa o valor atual 
        now = self.price_now(ctx, symbol)
        print(now)
        # Verifica se o valor "low" é igual ao preço atual
        if high > now:
            self.sell(ctx, symbol, high)
                
    def preview_low(self, ctx, symbol):
        #  << colocar logica
        return 2
    
    def preview_high(self, ctx, symbol):
        #  << colocar logica
        return 2
            
    def price_now(self, ctx, symbol):
        #  << colocar logica
        return 1
    
    def buy(self, ctx, symbol, price):
        corretora = True #  << aqui coloca a função da corretora de envio de compra
        print("manda processamento de compra para a corretora")
        if corretora == True:
            agora = datetime.now()
            data_formatada = agora.strftime("%Y-%m-%d %H:%M:%S")
            compra = {'ação': symbol,'price': price, 'compra': True}
            ctx.storage.set_belief(f'{data_formatada}', compra)
            
            # << guarda banco colocar logica
            
            print(f"B3 Min - Compra realizada: {compra}")
            
            sleep(5)
        else:
            self.arbitration_min(ctx)     

    def sell(self, ctx, symbol, price):
        corretora = True #  << aqui coloca a função da corretora de envio de compra
        print("manda processamento de compra para a corretora")
        if corretora == True:
            agora = datetime.now()
            data_formatada = agora.strftime("%Y-%m-%d %H:%M:%S")
            compra = {'ação': symbol,'price': price, 'Venda': True}
            ctx.storage.set_belief(f'{data_formatada}', compra)
            
            # << guarda banco colocar logica
            
            print(f"B3 Min - Compra realizada: {compra}")
            
            sleep(5)
        else:
            self.arbitration_min(ctx)   