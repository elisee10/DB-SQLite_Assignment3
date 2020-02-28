
from collections import namedtuple

from flask import render_template
from flask import request
from flask import escape

from voyager.db import get_db, execute

def boats(conn):
    return execute(conn, "SELECT b.bid, b.name, b.color FROM Boats AS b")

def sail_by(conn,x):
    return execute(conn, "SELECT Boats.name, Voyages.date_of_voyage from ((sailors JOIN  voyages ON sailors.sid = Voyages.sid) JOIN boats ON Voyages.bid = boats.bid) WHERE Sailors.name = :x", {"x":x })

#Function to add a boat per user request 


#####
def views(bp):
    @bp.route("/boats")
    def _boats():
        with get_db() as conn:
            rows = boats(conn)
        return render_template("table.html", name="boats", rows=rows)

    @bp.route("/boats/sailed-by", methods = ['GET', 'POST'])
    def _sail_by():
        with get_db() as conn:
            x =  request.args.get("sailor-name")
            print(x)
            rows = sail_by(conn,x)
        return render_template("table.html", name= "Sailed by", rows=rows)

#Rendering the add baot





