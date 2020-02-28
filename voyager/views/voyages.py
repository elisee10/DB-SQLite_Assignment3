from collections import namedtuple

from flask import render_template
from flask import request

from voyager.db import get_db, execute


def voyages(conn):
    # return execute(conn, "SELECT b.name || '   ' || s.name, v.date_of_voyage from boats b, Voyages v, Sailors s WHERE b.bid = v.bid  and s.sid = v.sid")
    return execute(conn, "SELECT Voyages.sid, Voyages.bid, Voyages.date_of_voyage FROM Voyages")

def views(bp):
    @bp.route("/voyages")
    def _voyages():
        with get_db() as conn:
            rows = voyages(conn)
        return render_template("table.html", name = "voyages",rows = rows)



