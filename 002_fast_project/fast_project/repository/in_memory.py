from ..models.models import User, SignupRequestBody

users: list[User] = []


class InMemoryRepo:

    @staticmethod
    def add_user(param: SignupRequestBody):
        user = User(**param)
        users.append(user)

    @staticmethod
    def get_all():
        return users
