"""Criação dos dataframes."""
import pandas as pd

names = ['fulano', 'ciclano', 'beltrano']
age = [42, 25, 32]


def creator() -> pd.DataFrame:
    """
    Cria um DataFrame a partir de listas predefinidas contendo nomes e idades.

    Returns:
        pd.DataFrame: Um DataFrame contendo duas colunas, 'Nome' e 'Idade',
                      com os dados das listas `names` e `age`.
    """
    df = pd.DataFrame(list(zip(names, age)), columns=['Nome', 'Idade'])
    return df


print(creator())
