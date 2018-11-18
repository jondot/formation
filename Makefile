watch:
	poetry run ptw -- --testmon
test:
	tox
release:
	python ci/release.py
