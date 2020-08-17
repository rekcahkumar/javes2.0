from sqlalchemy import Column, String
from userbot.database import SESSION, BASE


class SqlData(BASE):
    __tablename__ = "sqldatas"
    sqlvar = Column(String(14), primary_key=True)
    sqlvalue = Column(String(127))

    def __init__(self, sqlvar, sqlvalue):
        self.sqlvar = sqlvar
        self.sqlvalue = sqlvalue


SqlData.__table__.create(checkfirst=True)


def check_sql(sqlvar):
    try:
        return SESSION.query(SqlData).filter(SqlData.sqlvar == str(sqlvar)).one()
    except:
        return None
    finally:
        SESSION.close()


def addsql(sqlvar, sqlvalue):
    adder = SqlData(str(sqlvar), str(sqlvalue))
    SESSION.add(adder)
    SESSION.commit()


def resql(sqlvar):
    rem = SESSION.query(SqlData).get(str(sqlvar))
    if rem:
        SESSION.delete(rem)
        SESSION.commit()


def get_all_sql():
    rem = SESSION.query(SqlData).all()
    SESSION.close()
    return rem
