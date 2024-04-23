.PHONY: test lint format run all test_and_run audit

# Define o diretório do código fonte
SRC_DIR := df_creator

# Comando para executar o pyaudit
audit:
	-poetry run pip-audit

# Comando para rodar os testes com pytest
test:
	poetry run pytest -v

# Comando para formatar o código com blue
format:
	poetry run blue $(SRC_DIR)

# Comando para fazer lint do código com ruff
lint:
	poetry run ruff check $(SRC_DIR)

# Comando para executar o arquivo main.py como um script PySpark
run:
	poetry run python $(SRC_DIR)/df_creator.py

# Comando padrão que executa lint, formatação, testes e auditoria
#all: audit lint format test run

# Comando para executar testes e depois rodar o programa
audit_format_test_and_run: audit lint format test run
