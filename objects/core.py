from objects.player import player
from database.database import database
from objects.permission import permission

from mysql.connector.errors import IntegrityError


class core:
    def __init__(self):
        self.white_list = permission()
        self.database = database()

        self.squads = []
        self.orders = []

        self.handlers = []

        players = self.database.query(
            "select uid,permission as rank,username from players")
        for p in players:
            pl = player(p[0], p[1], p[2])
            self.white_list.add_user(pl)
            print(pl)

        chats = self.database.query("select * from chats")
        for chat in chats:
            print(chat)

# GETTERS
    def get_white_list(self):
        return self.white_list

    def get_squads(self):
        return self.squads

    def get_orders(self):
        return self.orders

    def get_handlers(self):
        return self.handlers

# PROCEDURES
    def add_player(self, pl):
        p = (pl.get_name(), pl.get_uid(), pl.get_rank())
        try:
            self.db_insert(
                "INSERT INTO players (username,uid,permission)", [p])
            self.white_list.add_user(pl)
        except IntegrityError:
            print("logging insert error")

    def rm_player(self, pl):
        query = f"DELETE FROM `players` WHERE uid = {pl.get_uid()};"
        self.db_query(query)
        self.white_list.rm_user(pl.get_uid())

    def add_squad(self, squad):
        self.squads.append(squad)
        s = (squad.get_chat_id(), squad.get_name(), squad.get_type())
        self.db_insert("INSERT INTO chats (cid,squad_name,squad_type)", [s])

    def rm_squad(self, cid):
        for (i, squad) in self.squads:
            if squad.get_cid() == cid:
                del self.squads[i]
                return

    def add_order(self, order):
        self.orders.append(order)

    def rm_order(self, oid):
        for (i, order) in self.orders:
            if order.get_id() == oid:
                del self.orders[i]
                return

    def add_handler(self, handler):
        self.handlers.append(handler)

    def db_query(self, query):
        return self.database.query(query)

    def db_insert(self, query, values):
        self.database.insert(query, values)
