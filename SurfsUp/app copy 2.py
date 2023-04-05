# Import the dependencies.

import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, distinct

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
base = automap_base()
# reflect the tables
base.prepare(engine, reflect=True)

# Save references to each table
measurement = base.classes.measurement
station = base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

# List all the available routes

@app.route("/")
def welcome():
    return (
        f"Available Routes for Hawaii Weather Data:<br/><br>"
        f"-- Daily Precipitation Totals for Last Year: <a href=\"/api/v1.0/precipitation\">/api/v1.0/precipitation<a><br/>"
        f"-- Active Weather Stations: <a href=\"/api/v1.0/stations\">/api/v1.0/stations<a><br/>"
        f"-- Daily Temperature Observations for Station USC00519281 for Last Year: <a href=\"/api/v1.0/tobs\">/api/v1.0/tobs<a><br/>"
        f"-- Min, Average & Max Temperatures for Date Range: /api/v1.0/trip/yyyy-mm-dd/yyyy-mm-dd<br>"
        f"NOTE: If no end-date is provided, the trip api calculates stats through 08/23/17<br>" 
    )

# Convert the query results from your precepitation analysis,
# retireive only the last 12 months of data to a dictionary,
# using date as the key and prcp as the value
# use the following ... /api/v1.0/precipitation

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    start_date = '2016-08-23'
    select = [measurement.date, 
        func.sum(measurement.prcp)]
    precipitation = session.query(*select).\
            filter(measurement.date >= start_date).\
            group_by(measurement.date).\
            order_by(measurement.date).all()
   
    session.close()

prec_dates = []
prec_totals = []

for date, dailytotal in precipitation:
        prec_dates.append(date)
        prec_totals.append(dailytotal)
        prec_dict = dict(zip(prec_dates, prec_totals))

return jsonify(prec_dict)

# Return a JSON list of stations from the dataset
# use the following /api/v1.0/stations

@app.route("/api/v1.0/stations")
def stations():

# Query the dates and temperature observations of the most-active station for the previous year
# return a JSON list of temperature observations for the previous year
# use /api/v1.0/tobs

@app.route("/api/v1.0/tobs")
def tobs():

# Return a JSON list of the min temp, max temp, avg temp for a specified start/ end range
# For a specified start calculate TMIN, TAVG, and TMAX for all dates greater than or equal to the start date
# For a specified start date calculate TMIN, TAVG, and TMAX for the dates from the start to the end date, inclusive

@app.route("/api/v1.0/trip/<start_date>")
def trip1
@app.route("/api/v1.0/trip/<start_date>/<end_date>")
def trip2
    

 #Note this code is incomplete as I continue to fail to understand this module.

