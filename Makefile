watch:
	poetry run ptw -- --testmon

cover:
	pytest --cov=formation tests -sq

test:
	pytest -vv --cov-report xml:cov.xml --cov=formation tests -sq

tox:
	tox

release:
	python ci/release.py
