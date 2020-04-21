import os
import random
from collections import namedtuple

Grass = namedtuple('Grass', 'cow, goat')
Terminal = namedtuple('Terminal', 'rows, columns')

def animal_feast(meals, kg_lower, kg_upper=None):
    if kg_upper is None:
        kg_upper = kg_lower + 1

    measurements = []
    for _ in Grass._fields:
        kilos = random.randrange(kg_lower, kg_upper)
        eaten = random.sample(range(meals, 40), kilos)
        measurements.append(eaten)

    return Grass(*measurements)

v1 = animal_feast(0, 12)
v2 = animal_feast(0, 1, 15)
v3 = animal_feast(-10, 1, 15)

terminal = Terminal(*map(int, os.popen('stty size').read().split()))
