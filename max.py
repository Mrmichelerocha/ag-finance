from uagents import Context, Model
from aumanaque import Create_agent
from action import Action

class Message(Model):
    message: str
    
max = Create_agent.max()
action = Action()

@max.on_message(model=Message)
async def message_handler(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"Received message from: {msg.message}")
    if msg.message == 'compra':
        action.checked_data_max(ctx)
        await ctx.send(sender, Message(message="venda")) 
    
if __name__ == "__main__":
    max.run()