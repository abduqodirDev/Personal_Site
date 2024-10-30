def check_email(email):
    if "@" in email and not email.startswith("@"):
        just = email.split("@")[1]
        if just.startswith(".") or just.endswith("."):
            return False
        else:
            return True
    else:
        return False