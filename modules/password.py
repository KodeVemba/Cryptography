from zxcvbn import zxcvbn
from getpass import getpass
import bcrypt


def check_stregth(password):
    result = zxcvbn(password)
    score = result["score"]
    if score < 3:
        feedback = result.get("feedback")
        warning = feedback.get("warning")
        suggestion = feedback.get("suggestions")
        response = "Weak password"
        response += f" Warning {warning}"
        response += f" Suggestion "
        for i in suggestion:
            response += " " + i

    elif score == 3:
        response = "strong enough password"
    elif score > 3:
        response = " strong password"

    return response


def hash_pw(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode, salt)
    return hashed


def verify_pw(password, hashed):
    if bcrypt.checkpw(password.encode(), hashed):
        return "Correct password. Access granted"
    else:
        return "Password is wrong"


if __name__ == "__main__":
    while True:
        password1 = getpass("Password: ")
        if check_stregth(password1).startswith("Weak"):
            print("Choose a stronger password")
        else:
            break
    hashed_password = hash_pw(password1)
