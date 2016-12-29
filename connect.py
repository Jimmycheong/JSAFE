from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from jdb import Base, Epasswords

engine = create_engine('sqlite:///storage.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

deleteit = session.query(Epasswords).all()
for d in deleteit:
    session.delete(d)
    session.commit()

new1 = Epasswords(company= 'Google', username = 'Mark', password='cooldogs')
new2 = Epasswords(company= 'Facebook', username = 'Sergey', password='peterrabbit')
new3 = Epasswords(company= 'Yahoo', username = 'Elizabeth', password='dogsarethebest')
new4 = Epasswords(company= 'HSBC', username = 'Thomas', password='password12345')
new5 = Epasswords(company= 'Deliveroo', username = 'Jeffery', password='8badboys8')
new6 = Epasswords(company= 'Snapchat', username = 'Calvin', password='lengjai')
new7 = Epasswords(company= 'Instagram', username = 'Steve', password='snappy')
new8 = Epasswords(company= 'Apple', username = 'Terrence', password='techboy45')

entries = [new1,new2,new3,new4,new5,new6,new7,new8]

for i in entries: 
	session.add(i)
	session.commit()

#checkall = session.query(Epasswords).all()

#for a in checkall: 
