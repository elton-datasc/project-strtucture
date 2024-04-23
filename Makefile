.PHONY: test lint format run all test_and_run

# Define o diretório do código fonte
SRC_DIR := df_creator

# Define o ambiente virtual do Poetry como prefixo para os comandos
POETRY_RUN=poetry run

# Comando para executar testes com pytest
test:
	$(POETRY_RUN) pytest -v

# Comando para executar análise estática com ruff
lint:
	$(POETRY_RUN) ruff check $(SRC_DIR)

# Comando para formatar o código com blue
format:
	$(POETRY_RUN) blue $(SRC_DIR)

run:
	$(POETRY_RUN) python $(SRC_DIR)/df_creator.py
# Comando para executar todos os comandos acima
all: test lint format

# Comando para executar testes e depois rodar o programa
test_and_run: test run
