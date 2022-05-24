"""
This is a flask app to display the data from a SQLlite database

John Moen
"""
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


"""
Set up the Database
"""
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save references to database table objects
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session link
session = Session(engine)


"""
Set up Flask
"""
app = Flask(__name__)

@app.route('/')
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!<br/>
    Available Routes:<br/>
    /api/v1.0/precipitation<br/>
    /api/v1.0/stations<br/>
    /api/v1.0/tobs<br/>
    /api/v1.0/temp/start/end
    ''')

