#
# Helper code for Lab 7 (dictionaries)
#

import random
from collections import namedtuple

def genkey():
    key = ''
    a = ord('a')
    pivot = a + round((ord('z') - a) / 2)

    for i in range(3):
        rand = random.randrange(a, pivot)
        key += chr(rand)
        
    return key

def ishundred(usrdict):
    if len(usrdict) != 100:
        raise ValueError('Incorrect dictionary length!')
    print("You're okay!")

Dragons = namedtuple('Dragons', 'colors, breeds')
dragons = Dragons(
    [ 'black',
      'white',
      'red',
      'blue', ],
    [ 'Antipodean Opaleye',
      'Chinese Fireball',
      'Common Welsh Green',
      'Hebridean Black',
      'Hungarian Horntail',
      'Norwegian Ridgeback',
      'Peruvian Vipertooth',
      'Romanian Longhorn',
      'Swedish Short-Snout',
      'Ukrainian Ironbelly', ]
)
