from random import randint
import asyncio


async def sentemail(sec=3):
    await asyncio.sleep(sec)
    print(f'email gonderildi {sec} saniyeye')
    
    
async def more_sent(count=10):
    fns = [sentemail(randint(2,20)) for _ in range(count)]
    await asyncio.gather(*fns)
    print('All sent')    
    
    
asyncio.run(more_sent(50))    