class Player:
    def __init__(self, nickname: str, weight: int = None):
        self.nickname = nickname
        self.xp = 0
        self.category = ""
        self.weight = weight

    def upgrade_xp(self, add_xp: int):
        self.xp += add_xp

    def update_category(self, category: str):
        self.category = category

    def get_info(self):
        return self.nickname + ", weight: " + str(self.weight) + ", category: " + self.category + "."
