from threading import *
from time import time, sleep
from concurrent.futures import ThreadPoolExecutor

# Задача сделать программу которая заваривает доширак:
# 1. Открыть упаковку
# 2. Засыпать приправу
# 3. Засыпать залень
# 4. Набрать и поставить чайник
# 5. Дождаться пока чайник закипит
# 6. Залить и ждать полного приготовления


def open_pack():
    sleep(1)
    print("Открыли упаковку")


def add_spice():
    sleep(1)
    print("Засыпали приправу")


def add_sauce():
    sleep(1)
    print("Засыпали залень")


def boil_water():
    sleep(3)
    print("Набрали воду и ставим чайник")
    sleep(2)
    print("Дожидаемся, пока чайник закипит")


def pour_water():
    sleep(1)
    print("Залили воду в доширак")
    sleep(4)
    print("Ждем, пока доширак будет готов")
    sleep(3)
    print("Доширак готов")


def CreateRamen():
    # Создаем и запускаем потоки
    # t1 = Thread(target=open_pack).start()
    # t2 = Thread(target=add_spice).start()
    # t3 = Thread(target=add_sauce).start()
    # t4 = Thread(target=boil_water).start()
    # t5 = Thread(target=pour_water).start()

    # # Ожидаем завершения всех потоков
    # t1.join()
    # t2.join()
    # t3.join()
    # t4.join()
    # t5.join()

    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.submit(open_pack)
        executor.submit(add_spice)
        executor.submit(add_sauce)
        executor.submit(boil_water)
        executor.submit(pour_water)


def main():
    currentTime = time()
    CreateRamen()
    lastTime = time()

    pastTense = round(lastTime - currentTime)
    print(f"Прошедшее время: {pastTense}s")


if __name__ == "__main__":
    main()
