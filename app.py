from flask import Flask, render_template, json
import os
import database.db_connector as db

# Configuration

app = Flask(__name__)
db_connection = db.connect_to_database()

# Routes

@app.route('/')
def root():
    '''Route to home page'''
    return render_template("main.j2")

@app.route('/players')
def players():
    '''Route to all players in the tracker'''
    query = "SELECT * FROM players;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("players.j2", gt_players=results)

@app.route('/player_clubs/')
def player_clubs():
    '''Route to a player's clubs'''

    # TODO: change query to only select clubs owned by one player using
    # the intersection tables

    query = "SELECT * FROM clubs \
            INNER JOIN player_clubs ON player_clubs.club_id = clubs.club_id \
            WHERE player_clubs.player_id = 3;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("player_clubs.j2", gt_player_clubs=results)

@app.route('/clubs')
def clubs():
    '''Route to all clubs in the tracker'''
    query = "SELECT * FROM clubs ORDER BY brand ASC;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("clubs.j2", gt_clubs=results)

@app.route('/player_rounds')
def player_rounds():
    '''Route to a player's rounds'''

    # TODO: change query to only select rounds played by one player 

    query = "SELECT * FROM rounds;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("player_rounds.j2", gt_player_rounds=results)

@app.route('/player_club_swings')
def player_club_swings():
    '''Route to a players swings by club'''

    # TODO: change query to select correct data

    query = "SELECT * FROM swings;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("player_round_swings.j2", gt_player_round_swings=results)\

@app.route('/player_round_swings')
def player_round_swings():
    query = "SELECT * FROM swings;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("player_club_swings.j2", gt_player_club_swings=results)

@app.route('/courses')
def courses():
    query = "SELECT * FROM courses;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("courses.j2", gt_courses=results)

@app.route('/course_holes')
def course_holes():
    query = "SELECT * FROM holes;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("course_holes.j2", gt_holes=results)

# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 15432))
    app.run(port=port, debug=True)
