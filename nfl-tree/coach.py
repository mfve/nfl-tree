class Coach:
    def __init__(self, link):
        self.link = link
        self.coaching_history = []

    def add_history(self, h):
        self.coaching_history << h