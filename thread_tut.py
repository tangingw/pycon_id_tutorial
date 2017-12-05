import time
import threading


def wait_print():
    thread_name = threading.currentThread().getName()
    print("%s reporting!\n" % thread_name)
    time.sleep(5)
    print("%s is inside Ecto-1\n" % thread_name)


def main():

    ghostbuster = [
        "Peter Venkman",
        "Egon Spengler",
        "Raymond Stantz",
        "Winston Zeddemore"
    ]
    
    threads = [threading.Thread(name=gb, target=wait_print, args=()) for gb in ghostbuster]
    
    for thread in threads:
        thread.start()
        
    
if __name__ == "__main__":
    main()
