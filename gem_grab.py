class Gems:
    def __init__(self,count, type):
        self.count = count
        self.type = type
    def get_gems(self, count: int)->int:
        return self.count