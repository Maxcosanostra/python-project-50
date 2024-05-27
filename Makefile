install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 .

pytest:
	poetry run pytest

gendiff-h:
	poetry run gendiff -h

yaml-comparison:
	poetry run gendiff file1.yml file2.yml

recursive-comparison:
	poetry run gendiff file1.json file2.json

format-plain-comparison:
        poetry run gendiff --format plain file1.json file2.json

format-json-comparison:
        poetry run gendiff --format json file1.json file2.json
