class Player:
    def __init__(self, nickname):
        self.nickname = nickname
        self.xp = 0

    def upgrade_xp(self, add_xp):
        self.xp += add_xp

    def get_info(self):
        return self.nickname + "(" + str(self.xp) + "xp)"
