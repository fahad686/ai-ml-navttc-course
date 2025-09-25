# async programming
# use asyncio library
import asyncio
import time





#take starting time
start_time=time.time()

#first function
async  def boil_water():
    print('start boiling water')
    await asyncio.sleep(2)
    print('boild water done')

async  def bread_toasted():
    print('bread dop in toster....')
    await asyncio.sleep(3)
    print('tosted successfuly..')

async def breakfast_preparing():
    print('Start making breakfast....!')
    await asyncio.gather(
        boil_water(),
        bread_toasted()
    )
    end_time=time.time()
    print(f'end time{end_time-start_time:.2f}')


asyncio.run(breakfast_preparing())