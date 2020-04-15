import asyncio


async def divide(x, y):
	asyncio.sleep(2)
	return x / y


async def main():
	task = asyncio.create_task(divide(6,5))
	await task

asyncio.run(main())
