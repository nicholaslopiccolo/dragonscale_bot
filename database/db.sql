CREATE TABLE chats
(
    cid BIGINT PRIMARY KEY NOT NULL,
    squad_name char(64),
    squad_type tinyint
);
#drop table players;
CREATE TABLE players
(
    uid BIGINT PRIMARY KEY NOT NULL,
    username char(30),
    permission tinyint default(0),
    cid BIGINT,
    FOREIGN KEY (cid) REFERENCES chats(cid)
);