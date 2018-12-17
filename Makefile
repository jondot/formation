watch:
	poetry run ptw -- --testmon

test:
	pytest --cov-report xml:cov.xml --cov=formation tests -sq
tox:
	tox
release:
	python ci/release.py
