import sqlalchemy as sa

engine = sa.create_engine("sqlite:///:memory:",echo=True)
connection = engine.connect()

metadata = sa.MetaData()

user_table = sa.Table(
    "user", 
    metadata,
    sa.Column('id',sa.Integer,primary_key=True),
    sa.Column("username",sa.String),
    sa.Column("email",sa.String),
)

def insert_user(username:str,email:str)->None:
    query = user_table.insert().values(username=username,email=email)
    connection.execute(query)

def select_user(username:str)->sa.engine.Result:
    query = user_table.select().where(user_table.c.username==username)
    result = connection.execute(query)
    return result.fetchall()

def main()->None:
    metadata.create_all(engine)
    insert_user("Mahesh","mahesh@gmail.com")
    insert_user("Ram","ram@gmail.com")
    insert_user("Mahesh","mj@gmail.com")
    print(select_user("Mahesh"))
    connection.close()

if __name__ == '__main__':
    main()

