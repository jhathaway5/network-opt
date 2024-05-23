
# Network Optimization Environment Setup

This README provides instructions for setting up a Python environment named `networkopt-env` for network optimization tasks, including generating and using a `requirements.txt` file.

## Prerequisites

- Python 3.x installed on your system
- `pip` (Python package installer)

## Setting Up the Python Environment

### 1. Create a Virtual Environment

First, create a virtual environment named `networkopt-env`:

```sh
python -m venv networkopt-env
```

### 2. Activate the Virtual Environment

Activate the virtual environment using the appropriate command for your operating system:

- On Unix/Linux/Mac:
  ```sh
  source networkopt-env/bin/activate
  ```

- On Windows:
  ```sh
  networkopt-env\Scripts\activate
  ```

## Generating `requirements.txt`

### 1. Install Necessary Packages

Install the necessary packages for your project. For example:

```sh
pip install networkx matplotlib heapq
```

### 2. Generate `requirements.txt`

Generate the `requirements.txt` file to list all installed packages:

```sh
pip freeze > requirements.txt
```

## Installing Modules from `requirements.txt`

If a `requirements.txt` file already exists, you can install all listed modules as follows:

### 1. Ensure the Virtual Environment is Activated

Ensure that the virtual environment `networkopt-env` is activated (see the activation instructions above).

### 2. Install the Requirements

Install all the required packages listed in the `requirements.txt` file:

```sh
pip install -r requirements.txt
```

## Deactivating the Virtual Environment

When you are done working in the virtual environment, you can deactivate it:

```sh
deactivate
```

## Running Your Python Script

Once the environment is set up and the required packages are installed, you can run your Python script. For example:

```sh
python your_script.py
```

## Additional Resources

- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)
- [pip Documentation](https://pip.pypa.io/en/stable/)
