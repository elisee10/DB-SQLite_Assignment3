from collections import namedtuple
from flask import render_template
from flask import request
from voyager.db import get_db, execute
from flask import redirect
from flask import url_for

def insertVoyage(conn):
    sailorid = request.args.get('sailor-id')
    boatid = request.args.get('boat-id')
    date = request.args.get('date-of-voyage')
    if boatid == None or sailorid == None:
        return 
    return execute(conn, "INSERT INTO Voyages(sid,bid,date_of_voyage) VALUES ((?), (?), (?));", (sailorid, boatid, date, ))
 
def views(bp):
    @bp.route("/voyages/add", methods = ['GET'])
    def _addVoyage():
        return render_template("InsertVoyage.html", name="Add a Voyage")

    @bp.route("/voyages/add/submit", methods = ['GET', 'POST'])
    def _insertVoyage():
        with get_db() as conn:
            rows = insertVoyage(conn)
        return  redirect(url_for('index'))
        
        



