import time
from multiprocessing import Process


def wait_print(process_name):
    print("%s reporting!\n" % process_name)
    time.sleep(5)
    print("%s is inside Ecto-1\n" % process_name)


def main():

    ghostbuster = ["Peter Venkman", "Egon Spengler", "Raymond Stantz", "Winston Zeddemore"]
    processes = [Process(target=wait_print, args=(gb,)) for gb in ghostbuster]

    for process in processes:
        process.start()


if __name__ == "__main__":
    main()
