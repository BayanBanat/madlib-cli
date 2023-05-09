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
    with patch('builtins.input', side_effect=["bbbb", "aaaa", "yyyy", "aaaa", "nnnnn"]):
        actual = prompt(5)
    expected = ("bbbb", "aaaa", "yyyy", "aaaa", "nnnnn")
    assert actual == expected

    ```
testing by run **pytest**


 

