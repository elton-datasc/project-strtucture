"""Testes das funções do arquivo df_creator.py."""
import pandera as pa

from df_creator.df_creator import creator

# Define the expected schema using Pandera
"""
'Nome' são strings

'Idade' são inteiros
"""
schema = pa.DataFrameSchema(
    {
        'Nome': pa.Column(str),
        'Idade': pa.Column(int),
    }
)


def test_df_creator() -> None:
    """
    Testa a creator pra garantir que o df criado atenda ao esquema definido.

    Returns:
        None

    Raises:
        SchemaError: Se o DataFrame não atender ao esquema definido.
    """
    # Call the function to create the DataFrame
    df = creator()

    # Validate the DataFrame against the schema
    # This will raise an error if the validation fails
    schema.validate(df)

    # If no exceptions are raised, the test passes
    assert True  # This line is optional, as the test will fail on exception


def test_df_non_empty() -> None:
    """
    Testa se o DataFrame criado pela função creator não está vazio.

    Returns:
        None

    Raises:
        AssertionError: Se o DataFrame estiver vazio.
    """
    df = creator()
    assert not df.empty, "O DataFrame não deve estar vazio."
