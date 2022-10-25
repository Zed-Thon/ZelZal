from sqlalchemy import Column, String, UnicodeText

from . import SESSION, BASE


class Nsfwatch(BASE):
    __tablename__ = "nsfwatch"
    chat_id = Column(String(14), primary_key=True)
    action = Column(UnicodeText)

    def __init__(self, chat_id, action):
        self.chat_id = chat_id
        self.action = action

Nsfwatch.__table__.create(checkfirst=True)

def add_nsfwatch(chat_id, action):
    nsfws = Nsfwatch(
        chat_id,
        action
    )
    SESSION.add(nsfws)
    SESSION.commit()


def rmnsfwatch(chat_id, action):
    nsfwm = SESSION.query(Nsfwatch).get(str(chat_id), action)
    if nsfwm:
        SESSION.delete(nsfwm)
        SESSION.commit()


def get_all_nsfw_enabled_chat():
    zedthon = SESSION.query(Nsfwatch).all()
    SESSION.close()
    return zedthon


def is_nsfwatch_indb(chat_id, action):
    try:
        return SESSION.query(Nsfwatch).get(str(chat_id), action)
    except BaseException:
        return None
    finally:
        SESSION.close()
