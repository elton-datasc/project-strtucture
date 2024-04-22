import pandas as pd

names = ['fulano', 'ciclano', 'beltrano']

age = [42, 25, 32]


def creator(*args):

        # Criando um DataFrame a partir das listas usando zip
        df = pd.DataFrame(list(zip(names, age)), columns=['Nome', 'Idade'])

        # Exibindo o DataFrame
        return df

print(creator())
