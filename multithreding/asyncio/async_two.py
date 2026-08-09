import asyncio
import time

async def brew(name):
    print(f"brew chai {name}...")
    await asyncio.sleep(2)
    # time.sleep(2)
    print(f"{name} chai is ready")

# async def brew_chai(name):
#     print(f"brew chai {name}...")
#     await asyncio.sleep(2)
#     print(f"{name} chai is ready...")

# asyncio.run(brew_chai("latto"))

async def main():
    await asyncio.gather(
        brew("Maslala"),
        brew("green"),
        brew("ginger"),
    ) 

asyncio.run(main())