
class order:
    def __init__(self, squads):
        print("Creating a order...")
        self.id = 1                     # id of the order
        self.squads = [1, 3, 7, 11]        # map of the squads (only indexs)

    def get_id(self):
        return self.id
