from sqlalchemy import create_engine, Column, Integer, String, ForeignKey,Boolean
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship,Session
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///myDatabase.db')

class Base(DeclarativeBase):
    pass
class User(Base):
    __tablename__ = "users"
    player_id = Column(Integer, primary_key=True, index=True)
    player_name = Column(String)
    player_money=Column(Integer,default=100)
    server_id = Column(Integer, ForeignKey("servers.server_id"))
    player_is_online=Column(Boolean,default=False)
    server = relationship("Server", back_populates="server_list_players")
 
class Server(Base):
    __tablename__ = "servers"
    server_id = Column(Integer, primary_key=True, index=True)
    server_name = Column(String)
    server_start=Column(String)
    server_is_alive=Column(Boolean,default=True)
    server_list_players = relationship("User", back_populates="server")

def print_info_users():
    Session = sessionmaker(bind=engine)
    session = Session()
    users=session.query(User).all()
    return users

def print_info_servers():
    Session = sessionmaker(bind=engine)
    session = Session()
    servers=session.query(Server).all()
    return servers

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    with Session(autoflush=False, bind=engine) as db:
        server1 = Server(server_name="Minecraft",server_start="22.07.2024")
        server2 = Server(server_name="Fortnite",server_start="10.10.2020")
        server3 = Server(server_name="CSGO",server_start="24.04.2018",server_is_alive=False)

        player1 = User(player_name="Peta",player_money=200,server=server1)
        player2 = User(player_name="Cola",player_money=300,player_is_online=True,server=server3)
        player3 = User(player_name="VOva",player_money=900,player_is_online=True,server=server3)
        player4 = User(player_name="Mita",player_is_online=True,server=server1)
        player5 = User(player_name="Anna",player_money=0,server=server2)
        player6 = User(player_name="Dima",player_money=50,server=server1)

        server1.server_list_players=[player1,player4,player6]
        server2.server_list_players=[player5]
        server3.server_list_players=[player2,player3]

        db.add_all([server1,server2,server3])
        db.commit()

        db.add_all([player1,player2,player3,player4,player5,player6])
        db.commit()

        print(print_info_users()[0].player_name)
        print(print_info_users()[3].player_money)
        print(print_info_users()[5].player_is_online)
        
        print(print_info_servers()[0].server_name)
        print(print_info_servers()[2].server_start)
        print(print_info_servers()[1].server_is_alive)
