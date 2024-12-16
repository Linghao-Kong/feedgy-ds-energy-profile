**Table of content**
- [1. Introduction of repo](#1-introduction-of-repo)
- [2. Plugins](#2-plugins)
  - [2.1. Miniconda](#21-miniconda)
  - [2.2. Poetry](#22-poetry)
  - [2.3. Pre-commit](#23-pre-commit)
  - [2.4. Ruff](#24-ruff)
  - [2.5. Dockerfile](#25-dockerfile)
  - [2.6. VSCode](#26-vscode)
  - [2.7. Links](#27-links)
  - [2.8. TODO](#28-todo)
  - [2.9. Notes](#29-notes)

# 1. Introduction of repo

`feedgy-ds-repo-template` is a demo repo for Feedgy data science team project.

# 2. Plugins
## 2.1. Miniconda
[Offical website]([https://](https://docs.anaconda.com/free/miniconda/))

Download miniconda at [here]([https://](https://docs.anaconda.com/free/miniconda/))

Or you can directly run the following commandes to install:
```bash
mkdir -p ~/miniconda3
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh -o ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
```

## 2.2. Poetry
```bash
poetry self update
poetry shell
poetry install
poetry build
```

## 2.3. Pre-commit
[Offical website](https://pre-commit.com/)
```bash
pre-commit install
pre-commit run --all-files # for the first time
pre-cmmit autoupdate # if any new hook is added
```
There is a list of supported hooks, please check them [here]([https://](https://pre-commit.com/hooks.html))


## 2.4. Ruff
[Official website](https://docs.astral.sh/ruff/)
Ruff can be used to replace Flake8 (plus dozens of plugins), Black, isort,
pydocstyle, pyupgrade, autoflake, and more, all while executing tens or
hundreds of times faster than any individual tool.

```bash
ruff check .
ruff check --fix
ruff format .
```
## 2.5. Dockerfile
Make sure that you have docker installed on your system.

```bash
# Test your docker image locally
export DOCKER_NAME=ds-repo-template
docker build -t $DOCKER_NAME:latest .
docker images | grep $DOCKER_NAME
docker run -d $DOCKER_NAME
docker run -it $DOCKER_NAME

# Build & Run directly the final image, without tagging
docker run -it $(docker build -q -f docker/Dockerfile .)
# Build & Run & Delete the container
docker run --rm -it $(docker build -q .)

# List all images
docker images -a
# Prune unused docker images
docker image prune
docker image prune -a -f
# List dangling images - those not tagged and not referenced by any container
docker images --filter dangling=true
```

## 2.6. VSCode

Management of user profile:
https://code.visualstudio.com/docs/editor/profiles


## 2.7. Links
[The major updates of python versions]([https://](https://www.nicholashairs.com/posts/major-changes-between-python-versions/))
[The difference between functional programming and OOP]([https://](https://www.datacamp.com/tutorial/functional-programming-vs-object-oriented-programming))
[Docker best practices]([https://](https://testdriven.io/blog/docker-best-practices/))

## 2.8. TODO

Finished :
- [x] Poetry
- [x] Dockerfile
- [x] Bandit
- [x] Pre-commit
- [x] Github Actions
- [x] VSCode profile
- [x] VSCode settings
- [x] Project structure
- [x] env file
- [x] gitignore
- [x] dockerignore

TODO :
- [ ] Launch.json
- [ ] Docstrings
- [ ] Pytest python example
- [ ] Pytest mocked S3 client
- [ ] Program argument with Click
- [ ] Logging
- [ ] README.md template
- [ ] Notebook analysis template
- [ ] Dump version with Poetry
- [ ] Install conda / Pyenv with Poetry
- [ ] Sagemaker docker environment
- [ ] VSCode usage


## 2.9. Notes

Some key point to explain during the workshops:
- explain docker : image, container, layer
- explain base image, RUN, ENTRYPOINT, CMD
- explain linux system : /opt, group, id, bash vs sh
- explain poetry
- explain the difference between 0.0.0.0, 127.0.0.1, localhost for docker
- explain CI/CD actions with simple examples
