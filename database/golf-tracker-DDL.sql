SET FOREIGN_KEY_CHECKS=0;
SET AUTOCOMMIT = 0;

CREATE OR REPLACE TABLE courses 
(
    course_id int NOT NULL AUTO_INCREMENT,
    course_name varchar(50) NOT NULL,
    course_state varchar(50) NOT NULL,
    PRIMARY KEY (course_id)
);

CREATE OR REPLACE TABLE players
(
    player_id int NOT NULL AUTO_INCREMENT,
    player_name varchar(50) NOT NULL,
    player_city varchar(50) NOT NULL,
    player_state varchar(50) NOT NULL,
    PRIMARY KEY (player_id)
);

CREATE OR REPLACE TABLE holes
(
    hole_id int NOT NULL AUTO_INCREMENT,
    course_id int NOT NULL,
    par_swing_count int NOT NULL,
    distance int NOT NULL,
    PRIMARY KEY (hole_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

CREATE OR REPLACE TABLE rounds
(
    round_id int NOT NULL AUTO_INCREMENT,
    course_id int NOT NULL,
    player_id int NOT NULL,
    round_date datetime NOT NULL,
    round_score int NOT NULL,
    PRIMARY KEY (round_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id),
    FOREIGN KEY (player_id) REFERENCES players(player_id)
);

CREATE OR REPLACE TABLE clubs
(
    club_id int NOT NULL AUTO_INCREMENT,
    brand varchar(50) NOT NULL,
    club_name varchar(50) NOT NULL,
    club_type varchar(50) NOT NULL,
    PRIMARY KEY (club_id)
);

CREATE OR REPLACE TABLE player_clubs
(
    player_id int NOT NULL,
    club_id int NOT NULL,
    FOREIGN KEY (player_id) REFERENCES players(player_id),
    FOREIGN KEY (club_id) REFERENCES clubs(club_id)
);

CREATE OR REPLACE TABLE swings
(
    swing_id int NOT NULL AUTO_INCREMENT,
    hole_id int NOT NULL,
    round_id int NOT NULL,
    player_id int NOT NULL, 
    club_id int NOT NULL,
    dist_traveled_yd int NOT NULL,
    PRIMARY KEY (swing_id),
    FOREIGN KEY (hole_id) REFERENCES holes(hole_id),
    FOREIGN KEY (round_id) REFERENCES rounds(round_id),
    FOREIGN KEY (player_id) REFERENCES players(player_id),
    FOREIGN KEY (club_id) REFERENCES clubs(club_id)
);

INSERT INTO courses (course_id, course_name, course_state) 
VALUES
(1, 'Augusta National Golf Club', 'Georgia'),
(2, 'Pebble Beach', 'California'),
(3, 'Nanea Golf Club', 'Hawaii'),
(4, 'Bluejack National Golf Club', 'Texas')
;

INSERT INTO players (player_id, player_name, player_city, player_state) 
VALUES
(1, 'John Doe', 'Houston', 'Texas'),
(2, 'Jane Deer', 'New York', 'New York'),
(3, 'Happy Gilmore', 'Hartford', 'Connecticut'),
(4, 'Shooter McGavin', 'Dallas', 'Texas')
;

INSERT INTO holes (hole_id, course_id, par_swing_count, distance) 
VALUES      
(1, 1, 4, 445),
(2, 1, 5, 575),
(3, 1, 4, 350),
(4, 1, 3, 240),
(5, 1, 4, 495),
(6, 1, 3, 180),
(7, 1, 4, 450),
(8, 1, 5, 570),
(9, 1, 4, 460),
(10, 1, 4, 495),
(11, 1, 4, 520),
(12, 1, 3, 155),
(13, 1, 5, 510),
(14, 1, 4, 440),
(15, 1, 5, 550),
(16, 1, 3, 170),
(17, 1, 4, 440),
(18, 1, 4, 465)
;

INSERT INTO rounds (round_id, course_id, player_id, round_date, round_score) 
VALUES
(1, 1, 1, '2022-03-02 08:15:22', 98),
(2, 2, 1, '2022-03-10 09:30:14', 91),
(3, 3, 3, '2022-03-23 08:00:39', 70),
(4, 3, 4, '2022-03-23 08:00:39', 102)
;

INSERT INTO clubs (club_id, brand, club_name, club_type) 
VALUES
(1, 'Taylormade', 'Stealth', 'Driver/1 Wood'),
(2, 'Taylormade', 'Stealth', '3 Wood'),
(3, 'Ping', 'G425', '7 Wood'),
(4, 'Mizuno', 'JPX Hot Metal', '4 Iron'),
(5, 'Mizuno', 'JPX Hot Metal', '5 Iron'),
(6, 'Mizuno', 'JPX Hot Metal', '6 Iron'),
(7, 'Mizuno', 'JPX Hot Metal', '7 Iron'),
(8, 'Mizuno', 'JPX Hot Metal', '8 Iron'),
(9, 'Mizuno', 'JPX Hot Metal', '9 Iron'),
(10, 'Mizuno', 'JPX Hot Metal', 'Pitching Wdge'),
(11, 'Callaway', 'Jaws', 'Gap Wedge'),
(12, 'Mizuno', 'JPX Hot Metal', 'Sand Wedge'),
(13, 'Titleist', 'Bob Vokey', 'Lob Wedge'),
(14, 'Ping', 'PLD', 'Putter'),
(15, 'Custom', 'Hockey', 'Putter')
;

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

INSERT INTO swings (swing_id, hole_id, round_id, player_id, club_id, dist_traveled_yd) 
VALUES
(1, 1, 1, 1, 1, 230),
(2, 1, 1, 1, 4, 170),
(3, 1, 1, 1, 11, 50),
(4, 1, 1, 1, 14, 6),
(5, 1, 1, 1, 14, 1),
(6, 2, 1, 1, 1, 235),
(7, 2, 1, 1, 2, 215),
(8, 2, 1, 1, 9, 120),
(9, 2, 1, 1, 12, 1),
(10, 2, 1, 1, 12, 10),
(11, 2, 1, 1, 14, 3),
(12, 3, 1, 1, 1, 233)
;

SET FOREIGN_KEY_CHECKS=1;
COMMIT;