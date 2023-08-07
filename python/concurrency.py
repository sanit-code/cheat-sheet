import time
import threading


# ############################## LOCKING ##############################
class TestBooleanLock:
    def __init__(self):
        self.lock = threading.Lock()                    # Lock
        self.val = True

    def get_and_toggle(self):
        self.lock.acquire()                             # Wait and get lock
        tmp = self.val                                  # Store value
        self.val = not self.val                         # Toggle value
        self.lock.release()                             # Release lock
        return tmp


# ############################## THREADS ##############################
def threads():
    # In python, threads run one at a time in same CPU
    # Total time is slower than sequential execution because of the cost of context switch
    data = TestBooleanLock()
    results = []

    def fn(st: float, ns: int):                         # Function to run in thread
        time.sleep(st)
        if data.get_and_toggle():                       # Check thread safe boolean
            results.append([                            # Append is thread safe
                threading.get_ident(),                  # Store thread id
                sum([x for x in range(ns)])             # Store computation
            ])
        else:
            results.append([threading.get_ident(), ns])

    n = 10000000
    ths = [
        threading.Thread(target=fn, args=(0.1, n,)),    # Create thread for fn
        threading.Thread(target=fn, args=(0.5, n,)),
        threading.Thread(target=fn, args=(1.0, n,))
    ]

    for th in ths:
        th.start()                                      # Start running the thread

    ths[0].join()                                       # Wait for first thread to end
    ths[1].join(0.1)                                    # Wait for second at most 0.1 seconds

    alive = [th.is_alive() for th in ths]               # Check each if it's alive  -> [False, ?, True]

    for th in ths:                                      # Wait for all threads
        th.join()

    # ##### THREAD POOL ####
    from multiprocessing.pool import ThreadPool
    pool = ThreadPool(3)                                # Initialize a pool of 3 threads
    results = pool.map(                                 # Run and wait for threads   ->   [0,1,4,9,16]
        lambda x: x ** 2,                               # Function to run for each thread
        range(5)                                        # Argument for each call
    )

    return


# ############################## PROCESSES ##############################
import multiprocessing as mp
import os


def test_function(n: int, queue: mp.Queue = None):      # Functions for processes must be global
    data = [
        os.getppid(),                                   # Store parent process id
        os.getpid(),                                    # Store process id
        sum([x for x in range(n)])                      # Store computation result
    ]
    if not queue:
        return data
    queue.put(data)


def processes():
    # Processes do not necessarily run on the same CPU
    from multiprocessing import Process, Queue
    import os
    n = 10000000

    q = Queue()                                         # Process-safe queue
    pcs = [
        Process(target=test_function, args=(n, q,)),    # Create process
        Process(target=test_function, args=(n, q,)),    # Can synchronize by passing locks/etc as args
        Process(target=test_function, args=(n, q,)),    # Best to avoid shared data between processes
    ]
    for pc in pcs:
        pc.start()                                      # Start process
    for pc in pcs:
        pc.join()                                       # Wait for process to end

    data = [
        q.get(block=True)                               # Wait and get from queue
        for _ in pcs
    ]

    # ### ENDING PROCESS ###
    p = mp.Process(target=test_function, args=(n,))
    p.start()                                           # Start process
    p.terminate()                                       # Terminate process
    p.join()                                            # Wait for it
    p.close()                                           # Free resources

    # ### PROCESS POOL ###
    with mp.Pool(os.cpu_count()) as pool:               # Pool as many as number of CPUs
        result = pool.map(                              # Run and wait for all processes
            test_function,
            [n for _ in range(10)]                      # Run 10 times with argument (n,)
        )
        result2 = pool.imap_unordered(                  # Make iterator of results in arbitrary order
            test_function,
            [(n//(i+1)) for i in range(10)]             # Run with smaller amounts
        )
        debug_var = True

    return


if __name__ == '__main__':
    threads()
    processes()

