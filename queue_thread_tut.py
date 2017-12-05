import random
import time
import threading as th
from queue import Queue


def capture(ghost_pool, trap):

    while True:

        ghost = ghost_pool.get()

        if not ghost is None:

            gb = th.currentThread().getName()
            trap.put(ghost)

            print("%s captures %s" %(gb, ghost))

            time.sleep(1)

            ghost_pool.task_done()


def gen_ghost(num_of_ghosts, ghost_pool):

    for i in range(num_of_ghosts):

        rand_id = random.randint(1, 100)
        ghost_pool.put("ghost_%d" % rand_id)
	#time.sleep(0.005)


def main():

    random.seed()
    trap = Queue()
    ghost_pool = Queue()

    ghostbuster = ["Peter Venkman", "Egon Spengler", "Raymond Stantz", "Winston Zeddemore"]

    threads = [th.Thread(
        name=gb,
        target=capture,
        args=(ghost_pool, trap)
        ) for gb in ghostbuster
              ]


    for thread in threads:

        thread.setDaemon(True)
        thread.start()


    gen_ghost(20, ghost_pool)

    ghost_pool.join()

    print("\n")
    print("Ghostbusters had completed their missions!\n")    

    while not trap.empty():

        print("Storing %s to Containment Unit!" % trap.get())


if __name__ == "__main__":

    main()
