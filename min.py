from uagents import Context, Model
from aumanaque import Create_agent
from action import Action

class Message(Model):
    message: str
    
min = Create_agent.min()
action = Action()

@min.on_interval(period=30.5)
async def plan_interval(ctx: Context):
    await ctx.send(Create_agent.MAX_ADDRESS, Message(message="compra")) if action.checked_data_min(ctx) else False
    
if __name__ == "__main__":
    min.run()