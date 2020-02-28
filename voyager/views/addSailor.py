
from collections import namedtuple
from flask import render_template
from flask import request
from flask import escape
from voyager.db import get_db, execute

def addSailor(conn):
    name = request.args.get('sailor-name')
    age = request.args.get('sailor-age')
    experience = request.args.get('sailor-experience')
    if name == None or age == None or experience == None:
        return 
    return execute(conn, "INSERT INTO Sailors(name, age, experience) VALUES ((?), (?), (?));", (name, age,  experience ))

def views(bp):
    @bp.route("/sailors/add", methods = ['GET'])
    def _addSailor():
        with get_db() as conn:
            rows = addSailor(conn)
        return render_template("InsertSailor.html", name="Add a Sailor")




