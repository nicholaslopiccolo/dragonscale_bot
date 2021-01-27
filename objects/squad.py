
class squad:
    def __init__(self):
        print("Creating squad...")
        self.name = "Test"
        self.chat_id = "11111111111"
        self.attack = 9990
        self.defense = 9990

# GETTERS
    def get_name(self):
        return self.name

    def get_chat_id(self):
        return self.chat_id

    def get_attack(self):
        return self.attack

    def get_defense(self):
        return self.defense

# SETTERS
    def get_name(self, name):
        self.name = name

    def get_chat_id(self, chat_id):
        self.chat_id = chat_id

    def get_attack(self, attack):
        self.attack = attack

    def get_defense(self, defense):
        self.defense = defense

# UTILS
    def to_msg_string(self):
        return f"{self.name}\n {self.attack}⚔\n {self.defense}🛡"
