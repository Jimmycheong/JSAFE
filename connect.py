from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from jdb import Base, Epasswords, Hasht
from lockandkey import getKey, jencrypt, dencrypt

engine = create_engine('sqlite:///storage.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

#gkeyp = getKey('hello'.encode('utf'))
gkeyp = b'}k\x16\x8b\xae\xf3\xa3|f\x82\xba/\xbd\xf1\xf8F\xcf\xac\x88\x92(\xed\x9f\xab\xbc\x06G\xcc mB('
print ('G: ', gkeyp)

#====##====##====##====##====##====#
#Delete current password entries
#====##====##====##====##====##====#
deleteit = session.query(Epasswords).all()
for d in deleteit:
    session.delete(d)
    session.commit()

new1 = Epasswords(company= 'Google', username = 'Mark', password=jencrypt(gkeyp,'cooldogs'))
new2 = Epasswords(company= 'Facebook', username = 'Sergey', password=jencrypt(gkeyp,'peterrabbit'))
new3 = Epasswords(company= 'Yahoo', username = 'Elizabeth', password=jencrypt(gkeyp,'dogsarethebest'))
new4 = Epasswords(company= 'HSBC', username = 'Thomas', password=jencrypt(gkeyp,'password12345'))
new5 = Epasswords(company= 'Deliveroo', username = 'Jeffery', password=jencrypt(gkeyp,'8badboys8'))
new6 = Epasswords(company= 'Snapchat', username = 'Calvin', password=jencrypt(gkeyp,'lengjai'))
new7 = Epasswords(company= 'Instagram', username = 'Steve', password=jencrypt(gkeyp,'snappy'))
new8 = Epasswords(company= 'Apple', username = 'Terrence', password=jencrypt(gkeyp,'techboy45'))

entries = [new1,new2,new3,new4,new5,new6,new7,new8]

for i in entries: 
	session.add(i)
	session.commit()

#====##====##====##====##====##====#
#Reset current password
#====##====##====##====##====##====#

resetit = session.query(Hasht).all()
for r in resetit:
    session.delete(r)
    session.commit()

reset = Hasht(hash = gkeyp)
session.add(reset)
session.commit()
