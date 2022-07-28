from flask import Flask, render_template, json, request, redirect
import os
import database.db_connector as db

# Configuration

app = Flask(__name__)
db_connection = db.connect_to_database()

# ----------------------------------------------------------------------------
# READ ROUTES: Home Page and Display Entities Handlers
# 
# The following flask route functions handle getting the data for all entities
# in the Golf Tracker MySQL database. Each route connects and communicates 
# with the database and sends resultant data to the Jinja templates to be 
# rendered as a web page displaying that data, except for the home page.
# ----------------------------------------------------------------------------

@app.route('/')
def root():
    """Route to home page"""
    return render_template("main.j2")

@app.route('/clubs')
def clubs():
    """Route to clubs table"""
    db_connection = db.connect_to_database()
    query = "SELECT * FROM clubs;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("clubs.j2", gt_clubs=results)

@app.route('/holes')
def holes():
    """Route to holes table"""
    db_connection = db.connect_to_database()
    query = "SELECT * FROM holes;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("course_holes.j2", gt_holes=results)

@app.route('/courses')
def courses():
    """Route to courses table"""
    db_connection = db.connect_to_database()
    query = "SELECT * FROM courses;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("courses.j2", gt_courses=results)

@app.route('/player-clubs')
def player_clubs():
    """Route to player_clubs intersection table"""
    db_connection = db.connect_to_database()    
    query = "SELECT * FROM player_clubs;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("player_clubs.j2", gt_player_clubs=results)


@app.route('/players')
def players():
    """Route to players table"""
    db_connection = db.connect_to_database()
    query = "SELECT * FROM players;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("players.j2", gt_players=results)

@app.route('/rounds')
def rounds():
    """Route to rounds table"""
    db_connection = db.connect_to_database()
    query = "SELECT * FROM rounds;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("player_rounds.j2", gt_rounds=results)

@app.route('/swings')
def player_round_swings():
    """Route to swings table"""
    db_connection = db.connect_to_database()
    query = "SELECT * FROM swings;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("player_round_swings.j2", gt_player_round_swings=results)

# ----------------------------------------------------------------------------
# INSERT ROUTES: Update Entity Handlers
#
#
# ----------------------------------------------------------------------------

@app.route("/insert-club", methods=["POST", "GET"])
def insert_club():
    """Route that handles inserting a club into the database"""
    
    #TODO: implement route

    pass

@app.route("/insert-course", methods=["POST", "GET"])
def insert_course():
    """Route that handles inserting a course into the database"""
    
    #TODO: implement route
    
    pass

@app.route("/insert-hole", methods=["POST", "GET"])
def insert_hole():
    """Route that handles inserting a hole into the database"""
    
    #TODO: implement route
    
    pass

@app.route("/insert-player-club", methods=["POST", "GET"])
def insert_player_club():
    """
    Route that handles inserting a player_club intersection table entry into
    the database.
    """
    
    #TODO: implement route
    
    pass

@app.route("/insert-player", methods=["POST", "GET"])
def insert_player():
    """Route that handles inserting a player into the database"""
    
    if request.method == "GET":
        return render_template("insert_player.j2")
    
    elif request.method == "POST":
        
        #TODO: implement update operations

        return redirect("/players")
    
    pass

@app.route("/insert-round", methods=["POST", "GET"])
def insert_round():
    """Route that handles inserting a round into the database"""
    
    #TODO: implement route
    
    pass

@app.route("/insert-swing", methods=["POST", "GET"])
def insert_swing():
    """Route that handles inserting a swing into the database"""
    
    #TODO: implement route
    
    pass

# ----------------------------------------------------------------------------
# UPDATE ROUTES: Update Entity Handlers
#
#
# ----------------------------------------------------------------------------

@app.route("/update-player/<int:id>", methods=["POST", "GET"])
def update_player(id):
    """Route that handles updating a player's data"""
    
    db_connection = db.connect_to_database()
    
    if request.method == "GET":
        read_query = "SELECT * FROM players WHERE player_id = '%s';" % (id)
        cursor = db.execute_query(db_connection=db_connection, query=read_query)
        results = cursor.fetchall()
        return render_template("update_player.j2", gt_player=results)
    
    elif request.method == "POST":
        
        #TODO: implement update operations

        return redirect("/players")

# ----------------------------------------------------------------------------
# DELETE ROUTES: Delete Entity Handlers
#
#
# ----------------------------------------------------------------------------

@app.route("/delete-club/<int:id>", methods=["POST", "GET"])
def delete_club(id):
    """Route that handles deleting a club from the database"""
    
    #TODO: implement route

    pass

@app.route("/delete-player/<int:id>", methods=["POST", "GET"])
def delete_player(id):
    """Route that handles deleting a player from the database"""
    
    #TODO: implement route

    pass

@app.route("/delete-round/<int:id>", methods=["POST", "GET"])
def delete_round(id):
    """Route that handles deleting a round from the database"""
    
    #TODO: implement route

    pass

@app.route("/delete-swing/<int:id>", methods=["POST", "GET"])
def delete_swing(id):
    """Route that handles deleting a swing from the database"""
    
    #TODO: implement route

    pass

# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 15433))
    app.run(port=port, debug=True)
