-- Golf Tracker Data Manipulation Query
-- :colons indicate variable that would be adjusted by other programming language

-- See courses
SELECT course_name, course_state from courses;

-- See all holes for a particular course
SELECT holes.course_id, hole_id, par_swing_count, distance
FROM holes
INNER JOIN courses
ON holes.course_id = courses.course_id
WHERE courses.course_id = :course_id;

-- See rounds played by a particular player
SELECT players.player_name, courses.course_name, rounds.round_id, rounds.round_date, rounds.round_score
FROM rounds
INNER JOIN players ON rounds.player_id = players.player_id
INNER JOIN courses ON rounds.course_id = courses.course_id
WHERE players.player_id = :player_id; 

-- See clubs owned by a particular player
SELECT brand, club_name, club_type
FROM players
INNER JOIN player_clubs on players.player_id = player_clubs.player_id
INNER JOIN clubs on player_clubs.club_id = clubs.club_id
WHERE players.player_id = :player_id;

-- See all clubs in app
SELECT brand, club_name, club_type
FROM clubs;

-- See all swings by a particular player
SELECT swing_id, dist_traveled_yd, brand, club_name, club_type
FROM swings
INNER JOIN players on swings.player_id = players.player_id
INNER JOIN clubs on swings.club_id = clubs.club_id
where swings.player_id = :player_id;

-- See all swings by a particular player on a particular round
SELECT swing_id, dist_traveled_yd, brand, club_name, club_type, round_date, swings.round_id
FROM swings
INNER JOIN players on swings.player_id = players.player_id
INNER JOIN clubs on swings.club_id = clubs.club_id
INNER JOIN rounds on swings.round_id = rounds.round_id
where swings.player_id = :player_id AND swings.round_id = :round_id;

-- See all swings by a particular player with a particular club
SELECT swing_id, dist_traveled_yd, brand, club_name, club_type, round_date, swings.round_id
FROM swings
INNER JOIN players on swings.player_id = players.player_id
INNER JOIN clubs on swings.club_id = clubs.club_id
INNER JOIN rounds on swings.round_id = rounds.round_id
where swings.player_id = :player_id AND swings.club_id = :club_id;

-- Insert new round for a player on a course (each value would be drop downs)
INSERT INTO rounds (course_id, player_id, round_date, round_score)
VALUES (:course_id, :player_id, :round_date, :round_score);

--  Insert a new swing for a player on a hole, during a around with a club
INSERT INTO swings (swing_id, hole_id, round_id, player_id, club_id, dist_traveled_yd)
VALUES (:hole_id, :round_id, :player_id, :club_id, :dist_traveled_yd);

-- Insert a new club to the database  (debatable on if user can do this)
INSERT INTO clubs (brands, club_name, club_type)
VALUES (:brand, :club_name, :club_type);

-- Insert a new player
INSERT INTO players (player_name, player_city, player_state)
VALUES (:player_name, :player_city, :player_state)

-- DELETES a swing
DELETE FROM swings
WHERE swing_id = :swing_id;

-- Deletes a club (debatable on if user can do this)
DELETE FROM clubs
WHERE club_id = :club_id;

-- Deletes a club (REVIEW - deleting round will delete associated swings)
DELETE rounds, swings
FROM rounds
INNER JOIN swings on rounds.round_id = swings.round_id
WHERE rounds.round_id = :round_id;

-- Updates a swing
UPDATE swings
SET hole_id = :hole_id, round_id = :round_id, player_id = :player_id, club_id=:club_id;

-- Updates a round
UPDATE rounds
SET course_id = :course_id, player_id = :player_id, round_date = :round_date, round_score = :round_score;

-- Update Player
UPDATE players
SET player_name = :player_name, player_city = :player_city, player_state = :player_state;
