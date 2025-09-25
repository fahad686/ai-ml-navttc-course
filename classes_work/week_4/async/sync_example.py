'''A synchronous program executes tasks sequentially, one after another.
This means each task must complete before the next one can begin, even if the program
is just waiting for an I/O-bound operation, like a network request or a database query.'''

import  time


def prepare_agent():
    print('gather knowledge..')
    time.sleep(3)
    print('gathered in 3 sec....')

def proceed_knowledge():
    print('proceeding info.....')
    time.sleep(4)
    print('agent made in 4 sec... ')

def agent_making():
    start_time=time.time()
    print('start making agent....')
    prepare_agent()
    proceed_knowledge()
    end_time=time.time()
    print(f'successfully agent created in {end_time-start_time:.2f} sec..')


agent_making()