from app.api.models import user


def already_exit_username(username, db):
    check = db.query(user.User).filter(user.User.username == username).first()
    if check:
        return True
    return False


def already_exit_email(email, db):
    check = db.query(user.User).filter(user.User.email == email).first()
    if check:
        return True
    return False


def valid_email(email):
    return email.__contains__("@") and email.__contains__(".")
