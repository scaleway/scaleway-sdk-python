WORKDIR = $(shell pwd)
LIBRARIES = scaleway-core scaleway-async scaleway

build:
	for lib in $(LIBRARIES); do \
		cd ${WORKDIR}/$$lib && \
		poetry build; \
	done

install-dependencies:	
	for lib in $(LIBRARIES); do \
		cd ${WORKDIR}/$$lib && \
		poetry install --no-root; \
	done

install-only-root:
	for lib in $(LIBRARIES); do \
		cd ${WORKDIR}/$$lib && \
		poetry install --only-root; \
	done

format:
	for lib in $(LIBRARIES); do \
		cd ${WORKDIR}/$$lib && \
		poetry run ruff --version && \
		poetry run ruff format ./; \
	done

format-check:
	for lib in $(LIBRARIES); do \
		cd ${WORKDIR}/$$lib && \
		poetry run ruff --version && \
		poetry run ruff format --check ./; \
	done

typing:
	for lib in $(LIBRARIES); do \
		cd ${WORKDIR}/$$lib && \
		poetry run mypy --version && \
		poetry run mypy --install-types --non-interactive --strict $$(echo $$lib | tr "-" "_"); \
	done

lint:
	for lib in $(LIBRARIES); do \
		cd ${WORKDIR}/$$lib && \
		poetry run ruff --version && \
		poetry run ruff check . --ignore E721 --ignore F541; \
	done

test:
	for lib in $(LIBRARIES); do \
		cd ${WORKDIR}/$$lib && \
		poetry run python -m unittest discover -s tests -v; \
	done

publish: install-dependencies
	for lib in $(LIBRARIES); do \
		cd ${WORKDIR}/$$lib && \
		poetry version "${PACKAGE_VERSION}" && \
		poetry build && \
		poetry publish --repository "${PYPI_REPOSITORY}" --no-interaction; \
	done
