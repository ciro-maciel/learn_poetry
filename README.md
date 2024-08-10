# Learn: Poetry for Python

Welcome to the repository for learning how using Poetry in Python projects. This repository serves as a resource for developers looking to adopt Poetry into their workflows.

## What is Poetry?

Poetry is a dependency and package management tool for Python that makes it easy to create and manage isolated environments and simplify package publishing.

## About the Project

This project aims to provide a solid foundation on how to use Poetry for managing packages and virtual environments in Python. Includes practical examples, step-by-step tutorials, and detailed explanations.

### Poetry Installation

With Python installed on your computer, you can install Poetry, run the following command:

```bash
$ pip install poetry
```

To check the version of Poetry, run the following command:

```bash
$ poetry --version
```

### Poetry Configuration

To configure Poetry, run the following command:

```bash
$ poetry config virtualenvs.in-project true
```

To see the current configuration, run the following command:

```bash
$ poetry config --list
```

### Project Creation

How to start a new project with Poetry.

```bash
$ poetry init
```

In the folder, you will see a `pyproject.toml` file with the Poetry configuration.

### Dependency Management

Add, remove and update packages with ease.

```bash
$ poetry add [package name]
```

Remove packages with ease.

```bash
$ poetry remove [package name]
```

To show the current dependencies, run the following command:

```bash
$ poetry show
```

### Run Commands

To install the dependencies, run the following command:

```bash
$ poetry install
```

The shell command spawns a shell within the project’s virtual environment.

```bash
$ poetry shell
```

As such, `exit` should be used to properly exit the shell.

Run Poetry commands with ease.

```bash
$ python src/github.py
```

```bash
$ python src/birthdate.py
```

```bash
$ python src/frequency.py
```

### Managing Environments

If you want to get basic information about the currently activated virtual environment

```bash
$ poetry env info
```

You can also list all the virtual environments associated with the current project

```bash
$ poetry env list
```

Delete existing virtual environments

```bash
$ poetry env remove [virtual environment name]
```

Use the `--all` option to delete all virtual environments at once.

### Version Control

To check the current version of Poetry, run the following command:

```bash
$ poetry version
```

To update the version of Poetry, run the following table:

| RULE  | BEFORE | AFTER |
| ----- | ------ | ----- |
| major | 1.3.0  | 2.0.0 |
| minor | 2.1.4  | 2.2.0 |
| patch | 4.1.1  | 4.1.2 |

```bash
$ poetry version [major|minor|patch]
```

## References

- [Poetry](https://python-poetry.org/)
- [Poetry Documentation](https://python-poetry.org/docs)

## About the Author

This repository was created and is maintained by Ciro Cesar Maciel. I am a Software Engineer passionate about creating efficient and well-documented solutions. I am always looking for new tools and practices that can simplify and improve the development workflow.

In addition to this project, I have been working on other interesting projects related to automation, Artificial Intelligence (AI), browser extensions, and more. I am also beginning to teach what is necessary to learn Artificial Intelligence (AI), helping others to get started on their AI journey.

If you are interested in Software Development, Data Science, AI, or other tech topics, feel free to explore my GitHub profile and connect with me.

### How to Find Me:

- GitHub: [ciro-maciel](https://github.com/ciro-maciel)
- LinkedIn: [Ciro Cesar Maciel](https://www.linkedin.com/in/ciro-maciel/)
- Website: [ciro-maciel](https://www.ciro-maciel.click)

I am always open to new collaborations and projects. If you have an interesting idea or just want to exchange thoughts about development, don't hesitate to reach out!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
