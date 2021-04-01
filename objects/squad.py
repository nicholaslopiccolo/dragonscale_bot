
class squad:
    def __init__(self, cid: int, tp: int, name: str):
        self.name = name
        self.chat_id = cid
        self.type = tp

        self.attack = 9990
        self.defense = 9990

# GETTERS
    def get_name(self) -> str:
        return self.name

    def get_chat_id(self) -> int:
        return self.chat_id

    def get_type(self) -> int:
        return self.type

    def get_attack(self) -> int:
        return self.attack

    def get_defense(self) -> int:
        return self.defense

# SETTERS
    def set_name(self, name: str):
        self.name = name

    def set_chat_id(self, chat_id: int):
        self.chat_id = chat_id

    def set_type(self, tp: int):
        self.type = tp

    def set_attack(self, attack: int):
        self.attack = attack

    def set_defense(self, defense: int):
        self.defense = defense

# UTILS
    def to_msg_string(self) -> str:
        return f"{self.name}\n {self.attack}⚔\n {self.defense}🛡"
