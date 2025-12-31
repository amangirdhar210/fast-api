import bcrypt


def generate_pwd_hash(pwd: str) -> str:
    return bcrypt.hashpw(bytes(pwd), bcrypt.gensalt(10))

bcrypt.hashpw()


def check_password_and_hash(pwd: str, hash_pw: str) -> bool:
    return bcrypt.checkpw(bytes(pwd), )
