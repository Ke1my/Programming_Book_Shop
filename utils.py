import re

EMAIL_REGEX = re.compile(
    r"^((?!\.)[a-z0-9.]{1,64}(?<!\.))@((?!-)[a-z0-9-]{1,63}(?<!-)\.)+[a-z]{2,6}$")


def check_email(email: str) -> bool:
    return EMAIL_REGEX.match(email) is not None


def review_is_valid(mark, content):
    if mark is None or\
            mark == '' or\
            content is None or\
            content == '':
        return False
    else:
        return True
