from collections import namedtuple

from flask import g
from flask import escape
from flask import render_template
from flask import request

from voyager.db import get_db, execute
from voyager.validate import validate_field, render_errors
from voyager.validate import NAME_RE, INT_RE, DATE_RE


def sailors(conn):
    return execute(conn, "SELECT s.name, s.age, s.experience FROM Sailors AS s")


#Sailor 
def sail_boat(conn,x):
    return execute(conn, "SELECT Sailors.name, Voyages.date_of_voyage from ((sailors JOIN  voyages ON sailors.sid = Voyages.sid) JOIN boats ON sailors.sid = boats.bid) WHERE boats.name = :x", {"x":x })
                       
def sail_date(conn,x):
    return execute(conn, "SELECT Sailors.name, Voyages.date_of_voyage from ((sailors JOIN  voyages ON sailors.sid = Voyages.sid) JOIN boats ON sailors.sid = boats.bid) WHERE Voyages.date_of_voyage = :x", {"x":x })
                       
def boat_color(conn,x):
    return execute(conn, "SELECT Sailors.name, Voyages.date_of_voyage from ((sailors JOIN  voyages ON sailors.sid = Voyages.sid) JOIN boats ON sailors.sid = boats.bid) WHERE Boats.color = :x", {"x":x })
                        

def boat_popular(conn,x):
    return execute(conn, "SELECT b.name, Count() from boats b, voyages v where b.bid = v.bid group by b.name order by 2 desc")









    
def views(bp):

    @bp.route("/sailors")
    def _get_all_sailors():
        with get_db() as conn:
            rows = sailors (conn)
        return render_template("table.html", name="sailors", rows=rows)




    @bp.route("/sailors/who-sailed", methods = ['GET', 'POST'])
    def sail_boat():
        with get_db() as conn:
            x =  request.args.get("boat-name")
            print(x)
            rows = sail_boat(conn,x)
        return render_template("table.html", name= "Sailor Who Sailed ", rows=rows) 


#Date


    @bp.route("/sailors/who-sailed-on-date", methods = ['GET', 'POST'])
    def sail_date_page():
        with get_db() as conn:
            x =  request.args.get("date")
            print(x)
            rows = sail_date(conn,x)
        return render_template("table.html", name= "Sailor Who Sailed on Date ", rows=rows) 


#Color 

    @bp.route("/sailors/who-sailed-on-boat-of-color", methods = ['GET', 'POST'])
    def sail_date_Color_page():
        with get_db() as conn:
            x =  request.args.get("color")
            print(x)
            rows = boat_color(conn,x)
        return render_template("table.html", name= "Sailor Who sailed on a boat of color ", rows=rows) 



#Popularity 
    @bp.route("/boats/by-popularity", methods = ['GET', 'POST'])
    def popularity():
        with get_db() as conn:
            x =  request.args.get(" ")
            print(x)
            rows = boat_popular(conn,x)
        return render_template("table.html", name= " Boat Popularity ", rows=rows) 

