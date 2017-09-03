'''
The following script is used to reset the master password.

Open the terminal and type python reset_password.py to run this script.

Ensure all dependancies at installed beforehand.

'''

import sys
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from jdb import Base, Epasswords, Hasht
from lockandkey import get_hashed_key, jencrypt

def create_session():
    '''
    Creates a SQLAclhemy cursor object to interact with sqlite3 database
    '''
    engine = create_engine('sqlite:///storage.db')
    Base.metadata.bind = engine
    db_session = sessionmaker(bind=engine)
    session = db_session()
    return session

def wipe_db(session):
    '''
    Remove all existing encrypted password hashes

    Args:
        session (object): Connection object to sqlite3 database

    '''
    passwords = session.query(Epasswords).all()
    for password in passwords:
        session.delete(password)
        session.commit()

def repopulate_db(session, gkeyp):
    '''
    Repopulates the db with dummy data as examples

    Args:
        session (object): Connection object to sqlite3 database
        gkeyp (byte): Byte string Hash

    '''
    new1 = Epasswords(
        company='Google',
        username='Mark',
        password=jencrypt(gkeyp, 'cooldogs')
        )
    new2 = Epasswords(
        company='Facebook',
        username='Sergey',
        password=jencrypt(gkeyp, 'peterrabbit')
        )
    new3 = Epasswords(
        company='Yahoo',
        username='Elizabeth',
        password=jencrypt(gkeyp, 'dogsarethebest')
        )
    new4 = Epasswords(
        company='HSBC',
        username='Thomas',
        password=jencrypt(gkeyp, 'password12345')
        )
    new5 = Epasswords(
        company='Deliveroo',
        username='Jeffery',
        password=jencrypt(gkeyp, '8badboys8')
        )
    new6 = Epasswords(
        company='Snapchat',
        username='Calvin',
        password=jencrypt(gkeyp, 'lengjai')
        )
    new7 = Epasswords(
        company='Instagram',
        username='Steve',
        password=jencrypt(gkeyp, 'snappy')
        )
    new8 = Epasswords(
        company='Apple',
        username='Terrence',
        password=jencrypt(gkeyp, 'techboy45')
        )

    entries = [new1, new2, new3, new4, new5, new6, new7, new8]

    for i in entries:
        session.add(i)
        session.commit()

def reset_password(session, gkeyp):
    '''
    Resets the master password hash with new entry.

    Args:
        session (object): Connection object to sqlite3 database
        gkeyp (byte): Byte string Hash

    '''
    passwords = session.query(Hasht).all()
    for password in passwords:
        session.delete(password)
        session.commit()

    reset = Hasht(hash=gkeyp)
    session.add(reset)
    session.commit()


if __name__ == '__main__':

    FILLER = '\n#====##====##====##====##====##====#\n'

    print(
        FILLER,
        "JSAFE PASSWORD RESET",
        FILLER,
        "\nDanger! This program deletes all existing passwords stored."
        )

    try:
        OPTION = input("Please type 'reset' to continue: ")
        if isinstance(OPTION, str) and OPTION != 'reset':
            print("\nExiting program")
            sys.exit()
    except (KeyboardInterrupt, SystemExit):
        print("\n")
        sys.exit()

    passwords_match = False

    try:
        while passwords_match != True:
            NEW_MASTER_PASSWORD = input("Enter new master password: ")
            CONFIRM_MASTER_PASSWORD = input("Retype new master password:")
            if NEW_MASTER_PASSWORD != CONFIRM_MASTER_PASSWORD:
                print("Passwords did not match. Please try again")
            else:
                passwords_match = True

    except (KeyboardInterrupt, SystemExit):
        print("\nClosing Program..")

    BYTE_HASH = get_hashed_key(NEW_MASTER_PASSWORD.encode('utf'))

    print("Encrypted hash generated")
    time.sleep(1)
    CONNECTION = create_session()

    print("Wiping Db...")
    time.sleep(1)
    wipe_db(CONNECTION)

    print("Repopulating Db...")
    time.sleep(1)
    repopulate_db(CONNECTION, BYTE_HASH)

    print("Resetting with new password...")
    time.sleep(1)
    reset_password(CONNECTION, BYTE_HASH)

    print("Your password has now successfully been reset.")
