# Random-Cyrillic-Inclusive-Password-Generator
This is a python module that creates randomised password. A lot of password generators don't use non ASCII characters out of fear that they might not be compatible with websites, however OWASP states that the websites should not limit the password input to specific character set. So my goal with this project was to partially diversify the password generation with cyrillic characters.

This project also includes unit tests to ensure its reliablity even after being updated. rcipg.py is the main script, test_rcipg.py is the script with the unit tests and example.py is a script that shows usage of the module being implemented. Besides cyrillic characters the password also contains ASCII characters, upper-case characters, numbers and special characters.

## Features
- Password generation with ASCII, numeric, uppercase, special and cyrillic characters.
- Provides ability to select the character set.
- Tested for python version 3.10.

## Installation
Download the rcipg.py script and place it into your project.
Import the module using `import rcipg`.

## Usage
The `generate()` function takes 4 arguments:
- The length of the password (int).
- Usage of uppercase characters in the password generation (bool)
- Usage of special characters in the password generation (bool)
- Usage of cyrillic characters in the password generation (bool)

The function returns password on output so you can save it to a variable.
```py
import rcipg

#generate a password with upper, special and cyrillic characters
password=rcipg.generate(8,True,True,True)
```

## License
The project is licensed under the MIT license.