import pandas as pd

def df_creator():
        # Listas fornecidas
        pan = ['fulano', 'ciclano', 'beltrano']
        age = [42, 25, 32]

        # Criando um DataFrame a partir das listas usando zip
        df = pd.DataFrame(list(zip(pan, age)), columns=['Nome', 'Idade'])

        # Exibindo o DataFrame
        return df

print(df_creator())
