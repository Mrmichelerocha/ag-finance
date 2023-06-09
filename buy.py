from uagents import Agent, Context, Model
from aumanaque import Create_agent
from action import Action

class Message(Model):
    message: str
    
buy = Create_agent.buy()
action = Action()

@buy.on_message(model=Message)
async def message_handler(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"Received message from: {msg.message}")
    if msg.message == 'compra':
        await ctx.send(sender, Message(message="Hello there alice."))    
    
if __name__ == "__main__":
    buy.run()