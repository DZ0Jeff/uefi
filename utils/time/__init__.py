from random import randint
from time import sleep


def generate_random_time():
    time = randint(10, 30)
    print(f'[LPC] > Esperando {time} segundos')
    sleep(time)