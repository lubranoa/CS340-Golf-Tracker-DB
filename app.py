from flask import Flask, render_template, json
import os
import database.db_connector as db

# Configuration

app = Flask(__name__)
db_connection = db.connect_to_database()

# Routes

@app.route('/')
def root():
    return render_template("main.j2")

@app.route('/players')
def players():
    query = "SELECT * FROM players;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("players.j2", gt_players=results)

@app.route('/player_clubs')
def player_clubs():
    query = "SELECT * FROM clubs;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("player_clubs.j2", gt_player_clubs=results)

@app.route('/clubs')
def clubs():
    query = "SELECT * FROM clubs ORDER BY brand DESC;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("clubs.j2", gt_clubs=results)

@app.route('/player_rounds')
def player_rounds():
    query = "SELECT * FROM rounds;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("player_rounds.j2", gt_rounds=results)

@app.route('/player_club_swings')
def player_club_swings():
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
    return render_template("courses.j2", gt_holes=results)

# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 15432))
    app.run(port=port, debug=True)
