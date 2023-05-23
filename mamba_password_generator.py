# Mamba Password Manager - Password Generator

# Modules
import secrets
import pyperclip
import string


# Mamba Password Generator Class
class MambaPasswordGenerator:
    def __init__(
        self,
        length=12,
        special_chars=True,
        digits=True,
        upper_case=True,
        lower_case=True,
    ):
        """This function initalises the 'MambaPasswordGenerator' class and attributes which are: the password length, special_chars, digits, upper_case and lower_case all included within the generated password's properties."""
        self.length = length
        self.special_chars = special_chars
        self.digits = digits
        self.upper_case = upper_case
        self.lower_case = lower_case
        self.mamba_password = None

    def mamba_generate_password(self):
        """This function takes the user's input of their desired password length, and the password is then generated through the use of the 'secrets' module while staying true to the inputted length."""
        chars = ""
        if self.lower_case:
            chars += string.ascii_lowercase
        if self.upper_case:
            chars += string.ascii_uppercase
        if self.digits:
            chars += string.digits
        if self.special_chars:
            chars += string.punctuation

        while True:
            try:
                self.length = int(
                    input(
                        "Please enter the desired password length, Mamba will do the rest: "
                    )
                )
                if self.length < 1:
                    print(
                        "The password length should be greater than 0, please try again."
                    )
                else:
                    break
            except ValueError:
                print(
                    "Mamba wants a number to generate the password. Please try again."
                )

        self.mamba_password = "".join(secrets.choice(chars) for _ in range(self.length))

        pyperclip.copy(self.mamba_password)
        print(
            f"Mamba has done it's magic! The shiny, new password generated is (already copied to clipboard): {self.mamba_password}"
        )

        return self.mamba_password


pg = MambaPasswordGenerator()
pg.mamba_generate_password()
