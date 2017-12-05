import random
import time
import multiprocessing as mp
from queue import Queue


def capture(gb, ghost_pool, trap):

    while True:

        ghost = ghost_pool.get()

        if not ghost is None:

            trap.put_nowait(ghost)

            print("%s captures %s" %(gb, ghost))

            time.sleep(1)

            ghost_pool.task_done()


def gen_ghost(num_of_ghosts, ghost_pool):

    for i in range(num_of_ghosts):

        rand_id = random.randint(1, 100)
        ghost_pool.put_nowait("ghost_%d" % rand_id)
	#time.sleep(0.005)


def main():

    random.seed()
    trap = mp.Queue()
    ghost_pool = mp.JoinableQueue()

    ghostbuster = ["Peter Venkman", "Egon Spengler", "Raymond Stantz", "Winston Zeddemore"]

    processes = [mp.Process(
        target=capture,
        args=(gb, ghost_pool, trap)
        ) for gb in ghostbuster
                ]


    for process in processes:

        process.daemon = True
        process.start()


    gen_ghost(20, ghost_pool)

    ghost_pool.join()

    print("\n")
    print("Ghostbusters had completed their missions!\n")    

    while not trap.empty():

        print("Storing %s to Containment Unit!" % trap.get())


if __name__ == "__main__":

    main()
