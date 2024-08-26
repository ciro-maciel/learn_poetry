# Learn: Poetry for Python

Welcome to the repository for learning how using Poetry in Python projects. This repository serves as a resource for developers looking to adopt Poetry into their workflows.

## Course Overview

The **Learn: Poetry for Python** course is designed to help developers seamlessly integrate Poetry into their Python projects. Whether you are new to Poetry or looking to refine your project management skills, this course provides a comprehensive guide to mastering Poetry, a tool that simplifies dependency management, virtual environments, and package publishing.

**Key Highlights of the Course:**

- **Introduction to Poetry**: Understand what Poetry is and why it's a valuable tool for Python developers.
- **Step-by-Step Installation**: Learn how to install Poetry on your system and verify its version.
- **Configuration Best Practices**: Discover how to configure Poetry to fit your development needs, including setting up virtual environments within your project.
- **Project Initialization**: Follow detailed instructions to create new projects using Poetry and manage your project's configuration with ease.
- **Efficient Dependency Management**: Add, remove, and update dependencies in your projects with simple commands, keeping your environment clean and organized.
- **Environment Handling**: Manage virtual environments effectively, including creating, listing, and removing them as needed.
- **Version Control**: Learn how to manage and update your project’s versioning using Poetry, ensuring your packages are always up-to-date.

This course is packed with practical examples, clear explanations, and useful commands that will enable you to leverage Poetry’s full potential in your Python projects. Whether you're building new projects or managing existing ones, **Learn: Poetry for Python** offers the tools and knowledge you need to optimize your development workflow.

### What is Poetry?

Poetry is a dependency and package management tool for Python that makes it easy to create and manage isolated environments and simplify package publishing.

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

This repository was created and is maintained by **Ciro Cesar Maciel**. I am a Software Engineer passionate about creating efficient and well-documented solutions. I am always looking for new tools and practices that can simplify and improve the development workflow.

In addition to this project, I have been working on other interesting projects related to automation, Artificial Intelligence (AI), browser extensions, and more. I am also beginning to teach what is necessary to learn Artificial Intelligence (AI), helping others to get started on their AI journey.

If you are interested in Software Development, Data Science, AI, or other tech topics, feel free to explore my GitHub profile and connect with me.

### How to Find Me:

- GitHub: [ciro-maciel](https://github.com/ciro-maciel)
- LinkedIn: [Ciro Cesar Maciel](https://www.linkedin.com/in/ciro-maciel/)
- Website: [ciro-maciel](https://www.ciro-maciel.click)

I am always open to new collaborations and projects. If you have an interesting idea or just want to exchange thoughts about development, don't hesitate to reach out!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
