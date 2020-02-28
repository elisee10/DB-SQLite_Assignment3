from collections import namedtuple
from flask import render_template
from flask import request
from flask import escape
from voyager.db import get_db, execute

def addBoat(conn):
    print("-----------------------------------")
    boat_name = request.args.get('boat-name')
    boat_color = request.args.get('boat-color')
    if boat_name == None or boat_color == None:
        print("herere")
        return 
    return execute(conn, "INSERT INTO Boats(name,color) VALUES ((?), (?));", (boat_name, boat_color, ))

def views(bp):
    @bp.route("/boats/add", methods = ['GET'])
    def _addBoat():
        with get_db() as conn:
            rows = addBoat(conn)
        print("herer again")
        return render_template("InsertBoat.html", name="Add a boat")