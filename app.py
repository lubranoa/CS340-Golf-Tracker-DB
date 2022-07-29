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
def read_clubs():
    """Route to clubs table"""
    db_connection = db.connect_to_database()
    query = "SELECT * FROM clubs;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("read_clubs.j2", gt_clubs=results)

@app.route('/holes')
def read_holes():
    """Route to holes table"""
    db_connection = db.connect_to_database()
    query = "SELECT * FROM holes;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("read_holes.j2", gt_holes=results)

@app.route('/courses')
def read_courses():
    """Route to courses table"""
    db_connection = db.connect_to_database()
    query = "SELECT * FROM courses;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("read_courses.j2", gt_courses=results)

@app.route('/player-clubs')
def read_player_clubs():
    """Route to player_clubs intersection table"""
    db_connection = db.connect_to_database()    
    query = "SELECT * FROM player_clubs;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("read_player_clubs.j2", gt_player_clubs=results)


@app.route('/players')
def read_players():
    """Route to players table"""
    db_connection = db.connect_to_database()
    query = "SELECT * FROM players;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("read_players.j2", gt_players=results)

@app.route('/rounds')
def read_rounds():
    """Route to rounds table"""
    db_connection = db.connect_to_database()
    query = "SELECT * FROM rounds;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("read_rounds.j2", gt_rounds=results)

@app.route('/swings')
def read_swings():
    """Route to swings table"""
    db_connection = db.connect_to_database()
    query = "SELECT * FROM swings;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("read_swings.j2", gt_player_round_swings=results)

# ----------------------------------------------------------------------------
# INSERT ROUTES: Update Entity Handlers
#
#
# ----------------------------------------------------------------------------

@app.route("/insert-club", methods=["POST", "GET"])
def insert_club():
    """Route that handles inserting a club into the database"""
    
    #TODO: implement route

    if request.method == "GET":
        return render_template("insert_club.j2")
    
    elif request.method == "POST":
    
        return redirect("/clubs")

@app.route("/insert-course", methods=["POST", "GET"])
def insert_course():
    """Route that handles inserting a course into the database"""
    
    #TODO: implement route

    if request.method == "GET":
        return render_template("insert_course.j2")
    
    elif request.method == "POST":
    
        return redirect("/courses")

@app.route("/insert-hole", methods=["POST", "GET"])
def insert_hole():
    """Route that handles inserting a hole into the database"""
    
    #TODO: implement route
    
    if request.method == "GET":
        return render_template("insert_hole.j2")
    
    elif request.method == "POST":
    
        return redirect("/holes")

@app.route("/insert-player-club", methods=["POST", "GET"])
def insert_player_club():
    """
    Route that handles inserting a player_club intersection table entry into
    the database.
    """
    
    if request.method == "GET":
        db_connection = db.connect_to_database()
        
        p_query = "SELECT player_name FROM players;"
        cursor = db.execute_query(
            db_connection=db_connection, 
            query=p_query
        )
        p_res = cursor.fetchall()

        c_query = "SELECT brand, club_name, club_type FROM clubs;"
        cursor = db.execute_query(
            db_connection=db_connection,
            query=c_query
        )
        c_res = cursor.fetchall()
        
        return render_template("insert_player_club.j2", gt_players=p_res, gt_clubs=c_res)
            
    elif request.method == "POST":
    
        return redirect("/player-clubs")


@app.route("/insert-player", methods=["POST", "GET"])
def insert_player():
    """Route that handles inserting a player into the database"""
    
    if request.method == "GET":
        return render_template("insert_player.j2")
    
    elif request.method == "POST":
        
        player_name = request.form["player_name"]
        player_city = request.form["player_city"]
        player_state = request.form["player_state"]

        insert_query = "INSERT INTO players (player_name, player_city, player_state) VALUES (%s, %s, %s);"
        db.execute_query(db_connection=db_connection, query=insert_query, query_params=(player_name, player_city, player_state))

        return redirect("/players")

@app.route("/insert-round", methods=["POST", "GET"])
def insert_round():
    """Route that handles inserting a round into the database"""
    
    #TODO: implement route
    
    if request.method == "GET":
        return render_template("insert_round.j2")
    
    elif request.method == "POST":
    
        return redirect("/rounds")

@app.route("/insert-swing", methods=["POST", "GET"])
def insert_swing():
    """Route that handles inserting a swing into the database"""
    
    #TODO: implement route
    
    if request.method == "GET":
        return render_template("insert_swing.j2")
    
    elif request.method == "POST":
    
        return redirect("/swings")

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
        
        player_id = id
        player_name = request.form["player_name"]
        player_city = request.form["player_city"]
        player_state = request.form["player_state"]

        #TODO: Validate user input to not be NULL

        update_query = "UPDATE players SET players.player_name = %s, players.player_city =%s, players.player_state = %s WHERE players.player_id = %s;"
        db.execute_query(db_connection=db_connection, query=update_query, query_params=(player_name, player_city, player_state, player_id))
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

    if request.method == "GET":
        read_query = "SELECT * FROM players WHERE player_id = '%s';" % (id)
        cursor = db.execute_query(db_connection=db_connection, query=read_query)
        results = cursor.fetchall()
        return render_template("delete_player.j2", gt_player=results)
    
    elif request.method == "POST":
        
        player_id = id
        delete = request.form["delete"]

        if delete == "yes":
            delete_query = "DELETE FROM players WHERE player_id = '%s';"
            db.execute_query(db_connection=db_connection, query=delete_query, query_params=(player_id,))

        return redirect("/players")


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
    port = int(os.environ.get('PORT', 15434))
    app.run(port=port, debug=True)
