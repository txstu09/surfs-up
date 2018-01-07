import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.db")

Base = automap_base()
Base.prepare(engine, reflect=True)

Station = Base.classes.stations
Measurement = Base.classes.measurements

app = Flask(__name__)

@app.route("/")
def welcome():
    return (
        "Available Routes:<br/>"
        "/api/v1.0/precipitation<br/>"
        "/api/v1.0/stations<br/>"
        "/api/v1.0/tobs<br/>"
        "/api/v1.0/<start><br/>"
        "/api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    return()

@app.route("/api/v1.0/stations")
def stations():
    return()

@app.route("/api/v1.0/tobs")
def tobs():
    return()

@app.route("/api/v1.0/<start>")
def start():
    return()

@app.route("/api/v1.0/<start>/<end>")
def start_end():
    return()

if __name__ == '__main__':
    app.run(debug=True)