from sqlalchemy import Column, String, delete
from sqlalchemy.orm.exc import NoResultFound
from . import BASE, SESSION

class bankc(BASE):
    __tablename__ = "autogrouptable"
    agroup = Column(String, primary_key=True)

    def __init__(self, agroup):
        self.agroup = str(agroup)


bankc.__table__.create(checkfirst=True)


def auto_g(
    agroup,
):
    try:
        if SESSION.query(bankc).one():
            del_auto_g()
    except NoResultFound:
        pass
    user = bankc(agroup)
    SESSION.add(user)
    SESSION.commit()
    SESSION.close()
    return True

def del_auto_g():   
    to_check = get_auto_g()
    if not to_check:
        return False
    stmt = delete(bankc)
    SESSION.execute(stmt)
    SESSION.commit()
    #SESSION.close()
    return stmt

def get_auto_g():
    try:
        if _result := SESSION.query(bankc).one().agroup:
            return _result
    except NoResultFound:
        return None
    finally:
        SESSION.close()
