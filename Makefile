#запускать из корня
build:
	uv build

#запускать из корня
install:
	uv sync
	
#запускать из корня
package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml