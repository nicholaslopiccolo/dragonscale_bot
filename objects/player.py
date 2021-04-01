class player:
    def __init__(self, uid, rank, name):
        self.name = name
        self.uid = uid
        self.rank = rank

# GETTERS
    def get_name(self) -> int:
        return self.name

    def get_uid(self) -> int:
        return self.uid

    def get_rank(self) -> int:
        return self.rank

# SETTERS
    def set_name(self, name: str):
        self.name = name

    def set_uid(self, uid: int):
        self.uid = uid

    def set_rank(self, rank: int):
        self.rank = rank
