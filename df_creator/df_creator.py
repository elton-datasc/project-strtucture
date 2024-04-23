import pandas as pd

names = ['fulano', 'ciclano', 'beltrano']

age = [42, 25, 32]


def creator(*args):

    df = pd.DataFrame(list(zip(names, age)), columns=['Nome', 'Idade'])

    return df


print(creator())
