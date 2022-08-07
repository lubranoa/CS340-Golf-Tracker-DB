------------------------------------------------------------------------------
-- Authors: Conner Marchell and Alexander Lubrano
-- Course: CS 340 - Introduction to Databases
-- File Name: golf-tracker-DDQ.sql
-- Last Modified: 08/04/2022
-- Description: This SQL file contains the Data Definition Queries used to 
--     create the tables necessary for our Golf Tracker application and 
--     contains INSERT queries that enter sample data into the newly created
--     tables.
------------------------------------------------------------------------------

-- Turn off foreign key checking and autocommit to minimize import errors
SET FOREIGN_KEY_CHECKS=0;
SET AUTOCOMMIT = 0;

-- Drop all project tables from MySQL database if they already exist
DROP TABLE IF EXISTS player_clubs, swings, rounds, holes, clubs, players, courses;

-- Create courses table with id, name, and state attributes
--     PK = course_id (courses are unique and their own ID)
CREATE TABLE courses 
(
    course_id int NOT NULL AUTO_INCREMENT,
    course_name varchar(50) NOT NULL,
    course_state varchar(50) NOT NULL,
    PRIMARY KEY (course_id)
);

-- Create players table with id, name, city, and state attributes
--     PK = player_id (players are unique and need their own ID)
CREATE TABLE players
(
    player_id int NOT NULL AUTO_INCREMENT,
    player_name varchar(50) NOT NULL,
    player_city varchar(50) NOT NULL,
    player_state varchar(50) NOT NULL,
    PRIMARY KEY (player_id)
);

-- Create holes table with id, course_id, par, and distance attributes
--     PK = hole_id (holes are unique and need their own ID)
--     FK = course_id (holes are a part of a course)
CREATE TABLE holes
(
    hole_id int NOT NULL AUTO_INCREMENT,
    course_id int NOT NULL,
    hole_number int NOT NULL,
    par_swing_count int NOT NULL,
    distance int NOT NULL,
    PRIMARY KEY (hole_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- Create rounds table with an id, course_id, player_id, date and time, and score
--     PK = round_id (rounds are unique and need their own ID)
--     FK = course_id (rounds must be played on a course)
--     FK = player_id (rounds must be played by a player)
-- A round is deleted if a player or a course is deleted.
CREATE TABLE rounds
(
    round_id int NOT NULL AUTO_INCREMENT,
    course_id int NOT NULL,
    player_id int NOT NULL,
    round_date datetime NOT NULL,
    round_score int NOT NULL,
    PRIMARY KEY (round_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
    FOREIGN KEY (player_id) REFERENCES players(player_id) ON DELETE CASCADE
);

-- Create clubs table with an id, brand, name, and type
--     PK = club_id (clubs are unique and need their own ID)
-- Rows are unique based on brand, name, and type
CREATE TABLE clubs
(
    club_id int NOT NULL AUTO_INCREMENT,
    brand varchar(50) NOT NULL,
    club_name varchar(50) NOT NULL,
    club_type varchar(50) NOT NULL,
    PRIMARY KEY (club_id),
    CONSTRAINT UC_club UNIQUE (brand, club_name, club_type)
);

-- Create player_clubs intersection table to facilitate the many to many 
-- relationship of players to clubs, since one player can have one or more
-- clubs and one club can have many or more players.
--     NO PK necessary
--     FK = player_id (a player can own a club)
--     FK = club_id (a club can be owned by a player)
-- A player_club relationship is deleted if a player or a club is deleted.
-- Rows are unique based on player_id and club_id
CREATE TABLE player_clubs
(
    player_id int NOT NULL,
    club_id int NOT NULL,
    FOREIGN KEY (player_id) REFERENCES players(player_id) ON DELETE CASCADE,
    FOREIGN KEY (club_id) REFERENCES clubs(club_id) ON DELETE CASCADE,
    CONSTRAINT UC_pc UNIQUE (player_id, club_id)
);

-- Create swings table with an id, hole, round, player, club, and distance
--     PK = swing_id (swings are unique and need their own ID)
--     FK = player_id (swings must be done by a player)
--     FK = hole_id (swings must be done on a hole)
--     FK = round_id (swings must be part of a round)
--     FK = club_id (swings must be done by a club, which does not have to be logged)
-- A swing is deleted if its round is deleted. A swing's club_id is set to 
-- NULL if it's associated club is deleted. 
CREATE TABLE swings
(
    swing_id int NOT NULL AUTO_INCREMENT,
    hole_id int NOT NULL,
    round_id int NOT NULL,
    player_id int NOT NULL, 
    club_id int,
    dist_traveled_yd int NOT NULL,
    PRIMARY KEY (swing_id),
    FOREIGN KEY (hole_id) REFERENCES holes(hole_id),
    FOREIGN KEY (round_id) REFERENCES rounds(round_id) ON DELETE CASCADE,
    FOREIGN KEY (player_id) REFERENCES players(player_id),
    FOREIGN KEY (club_id) REFERENCES clubs(club_id) ON DELETE SET NULL
);

-- Insert sample data into courses table
INSERT INTO courses (course_id, course_name, course_state) 
VALUES
(1, 'Augusta National Golf Club', 'Georgia'),
(2, 'Pebble Beach', 'California'),
(3, 'Nanea Golf Club', 'Hawaii'),
(4, 'Bluejack National Golf Club', 'Texas')
;

-- Insert sample data into players table
INSERT INTO players (player_id, player_name, player_city, player_state) 
VALUES
(1, 'John Doe', 'Houston', 'Texas'),
(2, 'Jane Deer', 'New York', 'New York'),
(3, 'Happy Gilmore', 'Hartford', 'Connecticut'),
(4, 'Shooter McGavin', 'Dallas', 'Texas')
;

-- Insert sample data into holes table, associating each hole with existing 
-- courses
INSERT INTO holes (hole_id, course_id, hole_number, par_swing_count, distance) 
VALUES      
(1, 1, 1, 4, 445),
(2, 1, 2, 5, 575),
(3, 1, 3, 4, 350),
(4, 1, 4, 3, 240),
(5, 1, 5, 4, 495),
(6, 1, 6, 3, 180),
(7, 1, 7, 4, 450),
(8, 1, 8, 5, 570),
(9, 1, 9, 4, 460),
(10, 1, 10, 4, 495),
(11, 1, 11, 4, 520),
(12, 1, 12, 3, 155),
(13, 1, 13, 5, 510),
(14, 1, 14, 4, 440),
(15, 1, 15, 5, 550),
(16, 1, 16, 3, 170),
(17, 1, 17, 4, 440),
(18, 1, 18, 4, 465)
;

-- Insert sample data into rounds table, associating each round with existing
-- courses and players
INSERT INTO rounds (round_id, course_id, player_id, round_date, round_score) 
VALUES
(1, 1, 1, '2022-03-02 08:15:00', 98),
(2, 2, 1, '2022-03-10 09:30:00', 91),
(3, 3, 3, '2022-03-23 08:00:00', 70),
(4, 3, 4, '2022-03-23 08:00:00', 102)
;

-- Insert sample data into clubs table
INSERT INTO clubs (club_id, brand, club_name, club_type) 
VALUES
(1, 'Taylormade', 'Stealth', 'Driver'),
(2, 'Taylormade', 'Stealth', '3 Wood'),
(3, 'Ping', 'G425', '7 Wood'),
(4, 'Mizuno', 'JPX Hot Metal', '4 Iron'),
(5, 'Mizuno', 'JPX Hot Metal', '5 Iron'),
(6, 'Mizuno', 'JPX Hot Metal', '6 Iron'),
(7, 'Mizuno', 'JPX Hot Metal', '7 Iron'),
(8, 'Mizuno', 'JPX Hot Metal', '8 Iron'),
(9, 'Mizuno', 'JPX Hot Metal', '9 Iron'),
(10, 'Mizuno', 'JPX Hot Metal', 'Pitching Wedge'),
(11, 'Callaway', 'Jaws', 'Gap Wedge'),
(12, 'Mizuno', 'JPX Hot Metal', 'Sand Wedge'),
(13, 'Titleist', 'Bob Vokey', 'Lob Wedge'),
(14, 'Ping', 'PLD', 'Putter'),
(15, 'Custom', 'Hockey', 'Putter')
;

-- Insert sample data into player_clubs intersection table, creating 
-- relationships between existing players and clubs
INSERT INTO player_clubs (player_id, club_id) 
VALUES
(1, 1),
(1, 2),
(1, 3),
(1, 4),
(1, 5),
(1, 6),
(1, 7),
(1, 8),
(1, 9),
(1, 10),
(1, 11),
(1, 12),
(1, 13),
(1, 14),
(3, 1),
(3, 15)
;

-- Insert sample data into swings table, associating each swing with existing
-- players, rounds, holes, and clubs
INSERT INTO swings (swing_id, hole_id, round_id, player_id, club_id, dist_traveled_yd) 
VALUES
(1, 1, 1, 1, 1, 230),
(2, 1, 1, 1, 4, 170),
(3, 1, 1, 1, 11, 50),
(4, 1, 1, 1, 14, 6),
(5, 1, 1, 1, NULL, 1),
(6, 2, 1, 1, 1, 235),
(7, 2, 1, 1, 2, 215),
(8, 2, 1, 1, 9, 120),
(9, 2, 1, 1, 12, 1),
(10, 2, 1, 1, 12, 10),
(11, 2, 1, 1, 14, 3),
(12, 3, 1, 1, 1, 233),
(13, 3, 1, 1, NULL, 0)
;

-- Turn foreign key checking and autocommit back on
SET FOREIGN_KEY_CHECKS=1;
COMMIT;