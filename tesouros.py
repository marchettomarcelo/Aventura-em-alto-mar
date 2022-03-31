import random

def recompensa_do_tesouro(nivel):

    
    if nivel >=1 and nivel <= 8:
        return random.randint(0, 3)
    if nivel >=9 and nivel <= 16:
        return random.randint(4, 7)
    if nivel >=17 and nivel <=24:
        return random.randint(8, 11)
    if nivel >=25 and nivel <= 32:
        return random.randint(12, 15)