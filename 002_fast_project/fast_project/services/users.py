from ..repository.in_memory import InMemoryRepo
import logging


class UserService:
    @staticmethod
    def signup(param):
        try:
            InMemoryRepo.add_user(param)
        except:
            logging.error("error occured while signing up")

    @staticmethod
    def get_all_users():
        try:
            return InMemoryRepo.get_all()
        except:
            logging.error("error occured")