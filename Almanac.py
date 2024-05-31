
from uagents.setup import fund_agent_if_low
from uagents import Agent, Context, Protocol
SSP = Agent(
    name="SSP",
    port=8000,
    seed="SSP secret phrase",
    endpoint=["http://127.0.0.1:8000/submit"])

@SSP.on_event("startup")
async def say_hello(ctx: Context):
    ctx.logger.info(f'hello, my name is {ctx.agent.name} and my address is {SSP.address}, and my wallet address is {SSP.wallet.address()}')

fund_agent_if_low(SSP.wallet.address())
 
if __name__ == "__main__":
    SSP.run()