from string import digits, ascii_uppercase, ascii_lowercase
import re


USER_REGEX = re.compile(
    r"^[a-zA-Zа-яА-Я]{1,20}$")

EMAIL_REGEX = re.compile(
    r"^((?!\.)[a-z0-9.]{1,64}(?<!\.))@((?!-)[a-z0-9-]{1,63}(?<!-)\.)+[a-z]{2,6}$")

PHONE_REGEX = re.compile(
    r'^((\+?7|8)[ \-] ?)?((\(\d{3}\))|(\d{3}))?([ \-])?(\d{3}[\- ]?\d{2}[\- ]?\d{2})$')

def check_email(email: str) -> bool:
    return EMAIL_REGEX.match(email) is not None

def check_password_weakness(password: str) -> bool:
    if check_password_length(password):
        if any(num in password for num in digits):
            if any(upper in password for upper in ascii_uppercase):
                if any(lower in password for lower in ascii_lowercase):
                    return True
    return False

def check_mark(mark: int) -> bool:
    if not mark.isnumeric():
        return False
    elif not 0 <= int(mark) <= 10:
        return False
    else:
        return True

def check_phone(phone: str) -> bool:
    return PHONE_REGEX.match(phone) is not None

def check_username(name: str) -> bool:
    return USER_REGEX.match(name) is not None

def check_password_length(password: str) -> bool:
    if len(password) >= 8:
        return True
    else:
        return False

def cart_is_valid(phone, adress):
    if phone is None or phone == '' or adress is None or adress == '':
        return False
    else:
        return True