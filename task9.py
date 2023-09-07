from abc import ABC, abstractmethod


class post_in_social_chanels_machine(ABC):
    @abstractmethod
    def post_a_message(self):
        pass


class Youtube_post_machine(post_in_social_chanels_machine):
    def __init__(self, message: dict):
        self.message = message

    def post_a_message(self):
        print("___Post in YouTube___")
        process_schedule(self)


class Facebook_post_machine(post_in_social_chanels_machine):
    def __init__(self, massage: dict):
        self.massage = massage

    def post_a_message(self):
        print("___Post in Facebook___")
        process_schedule(self)


class Twitter_post_machine(post_in_social_chanels_machine):
    def __init__(self, message: dict):
        self.message = message

    def post_a_message(self):
        print("___Post in Twitter___")
        process_schedule(self)


def process_schedule(post: post_in_social_chanels_machine) -> None:
    if isinstance(post, post_in_social_chanels_machine):
        if 14.30 >= float(list(post.message.keys())[0]):
            print(str(list(post.message.values())[0]))
    else:
        print("Invalid post object")
        exit(2)


b = 13.30
a = Twitter_post_machine({b: "Meowww"})
a.post_a_message()
