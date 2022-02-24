import numpy as np
import pandas as pd

# import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
import datetime as dt

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station



#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

# Homepage
@app.route("/")
def welcome():
    """The following is a list of all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api.v1.0/<start>/<end><br/>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all dates and precipitation"""
    # Query all dates and precipitation and order by date.
    results = session.query(Measurement.date, Measurement.prcp).\
        order_by(Measurement.date).all()

    session.close()

    # Create a dictionary from the row data and append to a list of precip_info
    precip_info = []
    
    for date, pcrp in results:
        precip_dict = {date:pcrp}
        precip_info.append(precip_dict)

    return jsonify(precip_info)


@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of station data including the name and station ID."""
    # Query all station names and station IDs
    results = session.query(Station.name, Station.station).all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_stations
    all_stations = []
    for name, station in results:
        station_dict = {}
        station_dict["name"] = name
        station_dict["station"] = station
        all_stations.append(station_dict)

    return jsonify(all_stations)


@app.route("/api/v1.0/tobs")
def temps():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return data for the station with the most """
    # Query all stations, dates, tobs and filter to the last year for the most active station.
    results = session.query(Measurement.station, Measurement.date, Measurement.tobs).\
        filter(func.date(Measurement.date) >= "2016-08-24").\
        filter(Measurement.station == "USC00519281").\
        order_by(Measurement.date).all()
    
    session.close()

    # Create a dictionary from the row data and append to a list of all_temps
    all_temps = []
    for station, date, tobs in results:
        temp_dict = {}
        temp_dict["station"] = station
        temp_dict["date"] = date
        temp_dict["tobs"] = tobs
        all_temps.append(temp_dict)

    return jsonify(all_temps)

@app.route("/api/v1.0/<start>")
def start(start):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    stats = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
        filter(Measurement.date >= start).all()
 
    session.close()
    
    # create JSONified list of dictionaries
    list = []
    for min, max, avg in stats:
        starts = {}
        starts ["start"] = start
        starts["Min Temp"] = min
        starts["Max Temp"] = max
        starts["Avg Temp"] = avg
        list.append(starts)
        
    return jsonify(list)

@app.route("/api.v1.0/<start>/<end>")
def end(start, end):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    stats = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
        filter(Measurement.date >= start).\
        filter(Measurement.date < end).all()
 
    session.close()
    
    # create JSONified list of dictionaries
    list = []
    for min, max, avg in stats:
        ends = {}
        ends ["start"] = start
        ends["end"] = end
        ends["Min Temp"] = min
        ends["Max Temp"] = max
        ends["Avg Temp"] = avg
        list.append(ends)
        
    return jsonify(list)


if __name__ == '__main__':
    app.run(debug=True)
