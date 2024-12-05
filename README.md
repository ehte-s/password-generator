# password-generator
This is a Python-based password generator that creates strong, random passwords and securely saves them to a text file. The script is simple to use, lightweight, and suitable for personal password management or as a utility in larger projects.


**Features**

Random Password Generation: Generates strong passwords containing uppercase letters, lowercase letters, digits, and special characters.

Customizable Length: Default password length is 12 characters, but you can specify a different length as needed.

Automatic Saving: Generated passwords are automatically saved to a passwords.txt file for future reference.

Easy-to-Use Interface: A single function call generates, displays, and saves a password.

**How It Works**

The generate_password function creates a random password of the desired length using a mix of letters, numbers, and special characters.
The save_password function appends the generated password to a file named passwords.txt.
The generate_and_save_password function combines these functionalities to streamline the process.



**Requirements**

Python 3.x

No additional libraries are required.

By default, the script generates a 12-character password and saves it to passwords.txt.



**Example Output**

Generated password: w7X!pQz#2t1L

Password 'w7X!pQz#2t1L' has been saved to passwords.txt



**Customization**

To generate a password of a different length, modify the length parameter in the generate_and_save_password function:
python

generate_and_save_password(length=16)


**Notes**
The passwords.txt file is stored in the same directory as the script.
Ensure the passwords.txt file is secured and not shared publicly to protect stored passwords.

**Contribution**
Contributions are welcome! Feel free to fork this repository, submit pull requests, or report issues.


**License**
This project is licensed under the MIT License. See the LICENSE file for details.
