from time import time, sleep


def function1(*, number: float):
    sleep(number)
    print("Отработала функция 1")


def function2(*, number: float):
    sleep(number)
    print("Отработала функция 2")


def main():
    currentTime = time()
    function1(number=1)
    function2(number=1)
    lastTime = time()

    pastTense = round(lastTime - currentTime)
    print(f"Прошедшее время: {pastTense}s")


if __name__ == "__main__":
    main()
