# Environment Variable Getter

This is a simple Python script to fetch and print the value of an environment variable.

## Description

The script defines a function `get_env_var` which takes the name of an environment variable as an argument and prints its value. If the environment variable is not set, it prints a default message "Variable not set". It then demonstrates the use of this function with a few common environment variables.

## Code

```python
import os

def get_env_var(variable):
  print(os.getenv(variable, 'Variable not set'))

get_env_var("HOME")
get_env_var("USER")
