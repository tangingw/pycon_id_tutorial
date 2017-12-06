# Source code for brief Tutorial on concurrency at [PyCon Indonesia](https://pycon.id) Talk

This is toy demo of concurrency, multithreading and queue for PyCon Indonesia. All the scripts in this repo         uses [_Ghostbusters_](https://en.wikipedia.org/wiki/Ghostbusters) as the storyline to illustrate various action of Ghostbusters. 

## Tutorial 1: thread_tut.py

Tutorial 1 uses [**threading**](https://docs.python.org/3/library/threading.html) package to show how Ghostbusters can be ready for action and sit inside [_Ecto-1_](http://ghostbusters.wikia.com/wiki/Ecto-1) at different time sequence. Note that due to GIL, the threading module is not going to exhibit the parallelism but rather we can use it as concurrency with time-slicing effect.


## Tutorial 2: multiprocessing_tut.py

Tutorial 2 uses [**multiprocessing**](https://docs.python.org/3/library/multiprocessing.html) to show the same effect as in tutorial one.

## Tutorial 3: queue_thread.py

This tutorial allows the user to see how python allows communication between threads using the [**queue**](https://docs.python.org/3/library/queue.html). Threads puts the processed/computed outputs into the queue and later the main thread retrieves the overall output from the queue. The model used in this tutorial is a worker-producer model where the producer produces the ghost pool with numbers of ghost as parameters, while Ghostbusters will be the worker. The queue acts as a [trap](http://ghostbusters.wikia.com/wiki/Trap). Note that the queue over here is non-blocking queue, which means once the ghost is inside into theh ghost pool, Ghostbusters will be able to see it and capture it. There is no wait in producing the ghost and the threads are running as daemon

## Tutorial 4: queue_mp.py

This tutorial has the similar structure but the queue used in this example is the [**queue**](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Queue) from multprocessing package. There is no involvement of threading package in this tutorial. Note that all the processes are running as background. Based on personal experience, the output of queue_mp.py depicts a closer picture of what the author actually wants.

### To Do

* Act the tutorial that deals with Lock
* Play around with asyncio and see if I can reproduce this

### [Contact me](mailto:tangingw.pas@gmail.com) 
