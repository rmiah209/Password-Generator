# Password-Generator
This program generates a strong, secret password with the length corresponding to the user's input.

# Modules
- secrets
- string
- pyperclip

# Functions
- generate_password()

# In-depth
The 'generate_password()' function takes the user's desired length as an input and stores it inside the length variable. If the user enters the correct input (consisting of the int datatype), the function then iterates through the empty 'chars' variable with the use of a for loop and appends the following to it depending on the length while keeping it randomised by use of the secrets module: 'string.ascii_lowercase', 'string.ascii_uppercase', 'string.digits', 'string.punctuation'. Once fully iterated and the password variable has its values appended to it by use of the in-built .join() method, the password is automatically copied to the user's clipboard by use of the .copy() method within the pyperclip module while simultanously being printed to the terminal with a completion message to let the user know that the prcoess has been completed and is also returned to end the function.
