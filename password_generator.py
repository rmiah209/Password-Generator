# Mamba Password Manager - Password Generator

# Modules
import secrets
import pyperclip
import string

def generate_password():
        length=12,
        special_chars=True,
        digits=True,
        upper_case=True,
        lower_case=True,

        password = None

        """This function takes the user's input of their desired password length, and the password is then generated through the use of the 'secrets' module while staying true to the inputted length."""
        chars = ""
        if lower_case:
            chars += string.ascii_lowercase
        if upper_case:
            chars += string.ascii_uppercase
        if digits:
            chars += string.digits
        if special_chars:
            chars += string.punctuation

        while True:
            try:
                length = int(
                    input(
                        "Please enter the desired password length, Mamba will do the rest: "
                    )
                )
                if length < 1:
                    print(
                        "The password length should be greater than 0, please try again."
                    )
                else:
                    break
            except ValueError:
                print(
                    "Please only enter number values to generate the password. Please try again."
                )

        password = "".join(secrets.choice(chars) for _ in range(length))

        pyperclip.copy(password)
        print(
            f"The shiny, new generated password (and copied to clipboard) is: {password}"
        )

        return password

password_genartor = generate_password()


