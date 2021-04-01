from telegram.ext import Filters
from objects.player import player
from database.database import database

"""
Returns and object that let create white lists depending on user rank
Ranks start to 0-Player until 9-King/Queen
"""


class permission:
    def __init__(self):
        self.ranks = []
        self.rank_map = ["Player", "1 - unnamed", "2 - unnamed", "Guild Leader", "4 - unnamed",
                         "Teacher", "Squad Leader", "7 - unnamed", "Council Member", "King/Queen"]

        self.init_ranks()
        self.db = database()

        #self.add_user(player(1007152999, 9, "TonRotob"))
        #self.add_user(player(1033556742, 9, "Starcatcher"))

    def init_ranks(self):
        for i in range(10):
            d = {"players": [], "f_users": Filters.user(), "f_chats": Filters.chat()}
            self.ranks.append(d)

    def get_rank_name(self, rank):
        return self.rank_map[rank]

    def get_users_filter(self, rank):
        return self.ranks[rank]["f_users"]

    def get_chats_filter(self, rank):
        return self.ranks[rank]["f_chats"]

    def get_player(self, uid):
        for (i, rank) in enumerate(self.ranks):
            for (j, p) in enumerate(rank["players"]):
                if p.get_uid() == uid:
                    return p
        return -1

    def add_user(self, p):
        rank = p.get_rank()
        self.ranks[rank]["players"].append(p)

        for (j, value) in enumerate(self.ranks):
            if j <= rank:
                #print(f"adding {uid} in {j}")
                self.ranks[j]["f_users"].add_user_ids(p.get_uid())

    def rm_user(self, uid):
        p = self.get_player(uid)
        rank = p.get_rank()
        self.ranks[rank]["players"].remove(p)
        for (j, value) in enumerate(self.ranks):
            if j <= rank:
                #print(f"removing {uid} in {j}")
                self.ranks[j]["f_users"].remove_user_ids(uid)
