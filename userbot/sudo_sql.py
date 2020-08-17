
from userbot.database import SESSION, BASE
from sqlalchemy import Column, String, UnicodeText


class Sudo(BASE):
    __tablename__ = "sudo"
    sender = Column(String(14), primary_key=True)

    def __init__(self, sender):
        self.sender = str(sender)


Sudo.__table__.create(checkfirst=True)


def is_sudod(sender_id):
    try:
        return SESSION.query(Sudo).all()
    except BaseException:
        return None
    finally:
        SESSION.close()


def sudo(sender):
    adder = Sudo(str(sender))
    SESSION.add(adder)
    SESSION.commit()


def unsudo(sender):
    rem = SESSION.query(Sudo).get((str(sender)))
    if rem:
        SESSION.delete(rem)
        SESSION.commit()


def get_all_sudo():
    rem = SESSION.query(Sudo).all()
    SESSION.close()
    return rem




