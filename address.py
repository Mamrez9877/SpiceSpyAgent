from uagents import Agent, Context
SSP = Agent(name="SSP", seed="SSP recovery phrase")

@SSP.on_event("startup")
async def say_hello(ctx: Context):
    ctx.logger.info(f'hello, my name is {ctx.agent.name} and my address is {SSP.address}, and my wallet address is {SSP.wallet.address()}')

 
if __name__ == "__main__":
    SSP.run()