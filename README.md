# LAB - Class 03
# madlib-cli


## Bayan Banat


**How to initialize/run application**

    python madlib_cli/madlib.py



**Tests**
using pytest to write and run tests for code
using **TDD** process:

- **import pytest**
- create a file  "__init__.py"
- creating test_prompt function for the prompt function using unit test function with patch fixture :
    
    ```
   def test_prompt():
    with patch('builtins.input', side_effect=["majestic", "purple", "Scott", "colored", "JB", "laughing", "tickled", "arrows", "gorilla", "butterfly", "Betty", "silly", "tests", "striped", "jackets", "44", "Wilson", "3", "leaves", "4", "swords"]):
        actual = prompt(("majestic", "purple", "Scott", "colored", "JB", "laughing", "tickled", "arrows", "gorilla", "butterfly", "Betty", "silly", "tests", "striped", "jackets", "44", "Wilson", "3", "leaves", "4", "swords"))
    expected = (("majestic", "purple", "Scott", "colored", "JB", "laughing", "tickled", "arrows", "gorilla", "butterfly", "Betty", "silly", "tests", "striped", "jackets", "44", "Wilson", "3", "leaves", "4", "swords"))
    assert actual == expected
    ```
testing by run **pytest**


 

