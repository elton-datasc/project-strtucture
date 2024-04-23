import pandera as pa

from df_creator.df_creator import (
    creator,
)

# Define the expected schema using Pandera
schema = pa.DataFrameSchema(
    {
        'Nome': pa.Column(
            str
        ),  # Validate that all values in 'Nome' are strings
        'Idade': pa.Column(
            int
        ),  # Validate that all values in 'Idade' are integers
    }
)


def test_df_creator():
    # Call the function to create the DataFrame
    df = creator()

    # Validate the DataFrame against the schema
    # This will raise an error if the validation fails
    schema.validate(df)

    # If no exceptions are raised, the test passes
    assert True  # This line is optional, as the test will fail on exception


# Optionally, you can add more specific tests,such as checking for non-empty Df
def test_df_non_empty():
    df = creator()
    assert not df.empty
