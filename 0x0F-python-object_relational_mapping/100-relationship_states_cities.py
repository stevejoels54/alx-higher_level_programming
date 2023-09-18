#!/usr/bin/python3
"""Print all City objects from the hbtn_0e_14_usa database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City
from model_state import State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    new = State(name="California", cities=[City(name="San Francisco")])

    session.add(new)
    session.commit()

    session.close()
