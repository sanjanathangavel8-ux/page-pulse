import asyncio

# Allow only 5 URL audits at the same time
semaphore = asyncio.Semaphore(5)