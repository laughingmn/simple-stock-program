# Simple Stock Program

This is a simple stock program that models stock services, including dividend yield, P/E ratio, and trade records, using Python.

## Table of Contents
1. [Installation](#installation)
2. [Setting Up the Environment](#setting-up-the-environment)
3. [Running the Program](#running-the-program)
4. [Testing the Application](#testing-the-application)

## Installation

To get started with this project, first, ensure that you have [Poetry](https://python-poetry.org/) installed on your system. Poetry is used to manage dependencies, run scripts, and test the application.

### Install Poetry

If you don’t have Poetry installed, you can install it by running:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

## Setting Up the Environment
Once you have Poetry installed, follow these steps to set up your environment:

1.Clone the Repository:

Clone the project repository to your local machine:

```bash
git clone https://github.com/your-username/simple-stock-program.git
cd simple-stock-program
```
2. Install the Dependencies:

```bash
poetry install
```

## Running the Program

Once the dependencies are installed, you can run the main application with the following command:

```bash
poetry run python -m src.main
```

## Testing the Application

1. Run All tests

To run all the tests, simply execute:
```bash
poetry run pytest
```

2. Run Specific Test

To run a specific test or test file, use the following command:
```bash
poetry run pytest <path/to/test_file.py>
```





