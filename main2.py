from threading import *
from time import time, sleep


def function1(*, number: float):
    sleep(number)
    print("Отработала функция 1")


def function2(*, number: float):
    sleep(number)
    print("Отработала функция 2")


thread1 = Thread(target=function1, kwargs={'number': 1})
thread2 = Thread(target=function2, kwargs={'number': 2})


def main():
    currentTime = time()
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    lastTime = time()

    pastTense = round(lastTime - currentTime)
    print(f"Прошедшее время: {pastTense}s")


if __name__ == "__main__":
    main()
