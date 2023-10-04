-- This database is about fictional high-speed world trains that everyone desires
-- so we could travel and know more cultures easily and in a safe way!
-- Let's assume that these trains don't have any stops in between and we are making a one-week test to check the adhesion to these trains.

-- CREATE DATABASE Trains;
-- USE Trains

-- CREATE TABLE Routes ( -- Table with the routes available
-- departure_station VARCHAR(50) NOT NULL,
-- arrival_station VARCHAR(50) NOT NULL,
-- route_ID INTEGER PRIMARY KEY
-- );

-- CREATE TABLE Trips ( -- Table with the trips available
-- 	trip_ID INTEGER PRIMARY KEY,
--  status BOOLEAN DEFAULT(1), -- Either the trip is going to happen (1) or is cancelled (0)
--  departure_time DATETIME, 
--  arrival_time DATETIME,
--  route_ID INTEGER,
--  FOREIGN KEY (route_ID) REFERENCES Routes(route_ID)
-- );

-- CREATE TABLE Passengers ( -- Table with the customers/passengers of the trains
-- 	first_name VARCHAR(55) NOT NULL,
--  last_name VARCHAR(55) NOT NULL,
--  passenger_ID INTEGER PRIMARY KEY,
--  age INTEGER CHECK(age>=18), -- When inserting the age of a 17 years-old the check constraint gave the following message Error Code: 3819. Check constraint 'passengers_chk_1' is violated.
--  nationality VARCHAR(15) NOT NULL
-- );

-- CREATE TABLE Bookings ( -- Table with the bookings of the passengers
-- 	booking_ID INTEGER PRIMARY KEY,
--  passenger_ID INTEGER,
--  route_ID INTEGER,
--  trip_ID INTEGER,
--  FOREIGN KEY (passenger_ID) REFERENCES Passengers(passenger_ID),
--  FOREIGN KEY (route_ID) REFERENCES Routes(route_ID),
--  FOREIGN KEY (trip_ID) REFERENCES Trips(trip_ID)
-- );-- 

-- INSERT INTO Routes
-- (departure_station, arrival_station, route_ID)
-- VALUES
-- ("Bangkok", "Moscow", 1),
-- ("Kuala Lumpur", "Beijing", 2),
-- ("Lisbon", "Dubai", 3),
-- ("Madrid", "Maputo", 4),
-- ("Ottawa", "Brasilia", 5);

-- INSERT INTO Trips
-- (trip_ID, departure_time, arrival_time, route_ID) -- I did not add status since it has a default value and at least for now we do not want to change it
-- VALUES
-- (1, "2023-10-09 06:00:00", "2023-10-12 08:00:00", 1),
-- (2, "2023-10-08 06:00:00", "2023-10-10 08:00:00", 1),
-- (3, "2023-10-09 12:00:00", "2023-10-10 09:30:00", 2),
-- (4, "2023-10-10 09:00:00", "2023-10-11 01:30:00", 3),
-- (5, "2023-10-11 01:00:00", "2023-10-12 12:00:00", 3),
-- (6, "2023-10-11 08:00:00", "2023-10-14 01:00:00", 4),
-- (7, "2023-10-12 03:00:00", "2023-10-14 23:00:00", 5),
-- (8, "2023-10-13 02:00:00", "2023-10-15 22:00:00", 5);


-- INSERT INTO Passengers
-- (first_name, last_name, passenger_ID, age, nationality)
-- VALUES
-- ('Dante' ,'Allott', 1, 94, 'Chinese'),
-- ('Hyacintha' ,'Ibbitt', 2, 19, 'Spanish'),
-- ('Valenka' ,'Fawdrie', 3, 19, 'Mexian'),
-- ('Grayce' ,'Beynon', 4, 85, 'Puerto Rican'),
-- ('Graig' ,'Cornwell', 5, 92, 'Irish'),
-- ('Bil' ,'Josifovic', 6, 33, 'Filipino'),
-- ('Nicolea' ,'Brumfitt', 7, 25, 'Albanian'),
-- ('Ara' ,'Kippin', 8, 21, 'Bangladeshi'),
-- ('Ignacius' ,'Alvar', 9, 72, 'Honduran'),
-- ('Bradly' ,'Tidy', 10, 45, 'Cameroonian'),
-- ('Noland' ,'Hursey', 11, 52, 'British'),
-- ('Deloria' ,'Zavattari', 12, 93, 'Greek'),
-- ('Ines' ,'Branco Veiga', 13, 27, 'Portuguese'),
-- ('Maxine' ,'Lorrain', 14, 49, 'Indonesian'),
-- ('Sherill' ,'Attewell', 15, 71, 'Uruguayan'),
-- ('Eugenius' ,'Dennant', 16, 76, 'Cambodian'),
-- ('Aubree' ,'Costa', 17, 67, 'Croatian'),
-- ('Vitia' ,'Milkin', 18, 49, 'Ecuadorian'),
-- ('Virgina' ,'Benard', 19, 31, 'Estonian'),
-- ('Sibyl' ,'Nisen', 20, 98, 'Finish'),
-- ('Filberte' ,'Pescod', 21, 56, 'French'),
-- ('Harriette' ,'Thompstone', 22, 84, 'American'),
-- ('Agatha' ,'Digman', 23, 59, 'Thai'),
-- ('Gwendolyn' ,'Cordeux', 24, 24, 'German'),
-- ('Elsworth' ,'Chewter', 25, 36, 'Hungarian'),
-- ('Isac' ,'Spring', 26, 20, 'Icelandic'),
-- ('Holden' ,'Janeway', 27, 67, 'Jamaican'),
-- ('Osborn' ,'Eckersall', 28, 73, 'Italian'),
-- ('Pooh' ,'Antoniewicz', 29, 31, 'Tongan'),
-- ('Marlo' ,'Denk', 30, 50, 'Salvadoran'),
-- ('Lurette' ,'Schwieso', 31, 27, 'Italian'),
-- ('Tabor' ,'Pillman', 32, 92, 'Liberian'),
-- ('Conan' ,'Godlee', 33, 71, 'Nepalese'),
-- ('Aggy' ,'Grossier', 34, 26, 'Macanese'),
-- ('Gladys' ,'Southwood', 35, 97, 'Lao'),
-- ('Jaymee' ,'Richley', 36, 38, 'Nigerien'),
-- ('Michel' ,'Bore', 37, 18, 'Mozambican'),
-- ('Sigfried' ,'Travers', 38, 53, 'Omani'),
-- ('Ariela' ,'Loftie', 39, 84, 'Bolivian'),
-- ('Abba' ,'Cleaton', 40, 42, 'Guatemalan'),
-- ('Annice' ,'Guerola', 41, 92, 'Taiwanese'),
-- ('Lynnett' ,'MacCaughey', 42, 20, 'Micronesian'),
-- ('Queenie' ,'Ector', 43, 87, 'Palestinian'),
-- ('Chris' ,'Cobson', 44, 27, 'Pakistani'),
-- ('Jobey' ,'Dodworth', 45, 88, 'Argentinian'),
-- ('Si' ,'Mertgen', 46, 26, 'Serbian'),
-- ('Georas' ,'Pembridge', 47, 23, 'Paraguayan'),
-- ('Sheena' ,'Beeres', 48, 44, 'Scotish'),
-- ('Jacklin' ,'Braunroth', 49, 63, 'Vietnamese'),
-- ('Dosi' ,'Bridgens', 50, 32, 'Korean'),
-- ('Standford' ,'Wolstenholme', 51, 88, 'Guamanian'),
-- ('Keven' ,'Mac Giany', 52, 19, 'Slovak'),
-- ('Bettye' ,'Berkery', 53, 48, 'Slovenian'),
-- ('Thebault' ,'Macon', 54, 95, 'Bangladeshi'),
-- ('Orelie' ,'Tomaschke', 55, 40, 'Russian'),
-- ('Robert' ,'McGerraghty', 56, 76, 'Turkish'),
-- ('Loren' ,'Gulliver', 57, 52, 'Ukrainian'),
-- ('Charin' ,'Snelson', 58, 20, 'Uzbek'),
-- ('Etan' ,'Rawdall', 59, 25, 'Swedish'),
-- ('Ajay' ,'Haggis', 60, 68, 'Swiss'),
-- ('Kori' ,'Cordle', 61, 92, 'Welsh'),
-- ('Bell' ,'Towersey', 62, 74, 'Sri Lankan'),
-- ('Davidson' ,'Chilvers', 63, 56, 'Puerto Rican'),
-- ('Sharia' ,'Girke', 64, 44, 'Zambian'),
-- ('Sarette' ,'Ashborne', 65, 39, 'Costa Rican'),
-- ('Sacha' ,'Cranefield', 66, 92, 'Uruguayan'),
-- ('Vikki' ,'Warrell', 67, 30, 'Dominican'),
-- ('Rudolf' ,'Gradon', 68, 71, 'Korean'),
-- ('Aubree' ,'Manach', 69, 57, 'Vietnamese'),
-- ('Elmer' ,'Le Page', 70, 37, 'Chinese'),
-- ('Helena' ,'Szymanski', 71, 60, 'Portuguese'),
-- ('Celestina' ,'Doram', 72, 68, 'Spanish'),
-- ('Daron' ,'Eacle', 73, 48, 'Guamanian'),
-- ('Barry' ,'Itschakov', 74, 25, 'Irish'),
-- ('Teddie' ,'Gadson', 75, 66, 'Chinese'),
-- ('Hattie' ,'Camolli', 76, 50, 'Costa Rican'),
-- ('Reeva' ,'Sweedland', 77, 77, 'Swiss'),
-- ('Clementina' ,'Hearfield', 78, 18, 'Canadian'),
-- ('Neilla' ,'Heinig', 79, 50, 'Taiwanese'),
-- ('Phillida' ,'Hame', 80, 31, 'Venezuelan'),
-- ('Meridith' ,'Mill', 81, 47, 'Bolivean'),
-- ('Donetta' ,'Hedau', 82, 25, 'Mexican'),
-- ('Guglielmo' ,'Doorey', 83, 54, 'Costa Rican'),
-- ('Valry' ,'Stubbley', 84, 43, 'Guamanian'),
-- ('Lynne' ,'Greated', 85, 29, 'Peruvian'),
-- ('Sam', 'Melinda', 86, 26, 'American');

-- INSERT INTO Bookings
-- (booking_ID, passenger_ID, route_ID, trip_ID) 
-- VALUES
-- (1, 1, 1, 1),
-- (2, 2, 1, 2),
-- (3, 3, 2, 3),
-- (4, 4, 1, 2),
-- (5, 5, 3, 5),
-- (6, 6, 4, 6),
-- (7, 7, 5, 7),
-- (8, 8, 5, 8),
-- (9, 9, 1, 1),
-- (10, 10, 1, 1),
-- (11, 11, 2, 3),
-- (12, 12, 3, 4),
-- (13, 13, 3, 5),
-- (14, 14, 4, 6),
-- (15, 15, 1, 2),
-- (16, 16, 1, 1),
-- (17, 17, 1, 1),
-- (18, 18, 1, 1),
-- (19, 19, 2, 3),
-- (20, 20, 1, 4),
-- (21, 21, 3, 5),
-- (22, 22, 4, 6),
-- (23, 23, 1, 1),
-- (24, 24, 1, 1),
-- (25, 25, 1, 1),
-- (26, 26, 1, 1),
-- (27, 27, 2, 3),
-- (28, 28, 3, 4),
-- (29, 29, 3, 5),
-- (30, 30, 4, 6),
-- (31, 31, 5, 7),
-- (32, 32, 1, 2),
-- (33, 33, 1, 1),
-- (34, 34, 5, 8),
-- (35, 35, 2, 3),
-- (36, 36, 3, 4),
-- (37, 37, 3, 5),
-- (38, 38, 4, 6),
-- (39, 39, 5, 7),
-- (40, 40, 1, 1),
-- (41, 41, 4, 6),
-- (42, 42, 2, 3),
-- (43, 43, 3, 4),
-- (44, 44, 3, 5),
-- (45, 45, 4, 6),
-- (46, 46, 5, 7),
-- (47, 47, 5, 8),
-- (48, 48, 1, 1),
-- (49, 49, 1, 2),
-- (50, 50, 2, 3),
-- (51, 51, 3, 4),
-- (52, 52, 3, 5),
-- (53, 53, 4, 6),
-- (54, 54, 5, 7),
-- (55, 55, 5, 8),
-- (56, 56, 1, 1),
-- (57, 57, 2, 3),
-- (58, 58, 2, 3),
-- (59, 59, 3, 4),
-- (60, 60, 3, 5),
-- (61, 61, 4, 6),
-- (62, 62, 5, 7),
-- (63, 63, 5, 8),
-- (64, 64, 1, 1),
-- (65, 65, 2, 3),
-- (66, 66, 2, 3),
-- (67, 67, 3, 4),
-- (68, 68, 3, 5),
-- (69, 69, 4, 6),
-- (70, 70, 5, 7),
-- (71, 71, 5, 8),
-- (72, 72, 1, 1),
-- (73, 73, 5, 7),
-- (74, 74, 2, 3),
-- (75, 75, 3, 4),
-- (76, 75, 1, 1),
-- (77, 76, 3, 5),
-- (78, 77, 4, 6),
-- (79, 78, 5, 7),
-- (80, 79, 5, 8),
-- (81, 80, 1, 1),
-- (82, 81, 5, 8),
-- (83, 82, 1, 1),
-- (84, 82, 2, 3),
-- (85, 83, 3, 4),
-- (86, 84, 3, 5),
-- (87, 85, 4, 6),
-- (88, 86, 1, 1);

-- There was an error when processing the payment of the last passenger so he won't be travelling. Let's first delete his data.
-- SELECT MAX(passenger_ID) FROM bookings; -- the last passenger_ID is 86

-- DELETE FROM Bookings
-- WHERE passenger_ID = 86;

-- DELETE FROM Passengers
-- WHERE passenger_ID = 86;

-- Let's make sure that records of this passenger do not exist both in tables Bookings and Passengers
-- SELECT passenger_ID 
-- FROM Bookings
-- ORDER BY passenger_ID DESC; -- We can see that the first passenger_id is 85, so the 86 was indeed deleted

-- SELECT passenger_ID
-- FROM Passengers
-- ORDER BY passenger_ID DESC; -- We can see that the first passenger_id is 85, so the 86 was indeed deleted

-- Let's check which trip has the most passengers and what is the route they take
SELECT t.trip_ID, r.departure_station, r.arrival_station, subquery.trip_count_passengers
FROM Trips AS t
LEFT JOIN Routes AS r 
ON t.route_ID = r.route_ID
INNER JOIN (
	SELECT b.trip_ID, COUNT(b.trip_ID) AS trip_count_passengers -- To check which trip_ID has the most bookings
	FROM Bookings AS b
	GROUP BY b.trip_ID
	ORDER BY 2 DESC -- Order the second column by descending order 
	LIMIT 1) AS subquery -- We only want the trip with the most passengers so we limit to the 1st row
ON t.trip_ID = subquery.trip_ID;
-- When running this query we can see that the trip 1 has the most passengers: 19 to be precise. The route is from Bangkok to Moscow.


-- It was decided that trips with less than ou equal to 5 passengers up to 24h before the trip will be cancelled.
-- Let's first check if we have a trip in this condition that might need cancelation in the future.
SELECT trip_ID, COUNT(trip_ID) AS trip_count_passengers2 -- to check which trip_ID has the least bookings
FROM Bookings AS b
GROUP BY b.trip_ID
HAVING COUNT(trip_ID) <= 5
ORDER BY 2 ASC; 
-- We can see that trip 2 has 5 passengers, so in the future the trip will be cancelled (considering that we won't add more passengers).

-- Let's create a View that has the number of passengers per trip, ordered by the trip with the most passengers
CREATE VIEW passengers_per_trip
AS
SELECT trip_ID, COUNT(trip_ID) AS trip_count_passengers3
FROM Bookings AS b
GROUP BY b.trip_ID
ORDER BY 2 DESC; 


-- Let's create a stored procedure to change the status of current and future trips to be cancelled when 
-- they have 5 passengers or less within 24h of the trip.
DELIMITER //
CREATE PROCEDURE Cancel_Trips(
IN tripID INT -- The input will be the tripID
)
BEGIN
	DECLARE passengers_count INT; -- The number of passengers of the trip
    DECLARE departure_time_trip DATETIME; -- The departure time of the trip
    -- Let's get the number of passengers per trip
    SELECT COUNT(trip_ID) INTO passengers_count -- Setting the variable we declared to be the number of passengers per trip
	FROM Bookings AS b
    GROUP BY trip_ID
    HAVING b.trip_ID = tripID;
    -- Let's set the departure_time_trip 
    SELECT departure_time INTO departure_time_trip
    FROM Trips as t
    WHERE t.trip_ID = tripID;
    -- Let's create the restrictions to check if trips have 5 passengers or less within 24h prior to the trip
    IF passengers_count <= 5 AND TIMEDIFF(departure_time_trip, NOW()) <= "24:00:00" THEN
		UPDATE Trips
		SET status = 0
        WHERE trip_ID = tripID;
	END IF;
END //
DELIMITER ;
-- Let's make sure that this SP is run every five hours to cancel trips with prior warning to the passengers
CREATE EVENT cancel_trips_event
	ON SCHEDULE EVERY 5 HOUR
	DO
	CALL Cancel_Trips(2);
-- In this case we already know that only trip 2 has 5 passengers of less.
-- For future reference, if we were to use this code with more trips it should be better to create a loop 
-- and a condition that we only call this SP for trips with 5 or less passengers and within 24h of the trip.
-- Nonetheless, for this particular assignment and due to the fact that loops are advanced material we will just be calling the SP
-- for trip 2 for the purpose of this assignment.


-- Let's check in which day of the week more passengers depart
SELECT DAYNAME(t.departure_time) AS day_week, COUNT(b.passenger_id) as passengers_count2
FROM Trips AS t
RIGHT JOIN Bookings AS b ON t.trip_ID = b.trip_ID
WHERE t.status = 1
GROUP BY day_week
ORDER BY -- When we order by day_week it orders alphabetically but we want the order to be by the day of week, starting on Monday.
	CASE 
        WHEN day_week = 'Monday' THEN 1
        WHEN day_week = 'Tuesday' THEN 2
        WHEN day_week = 'Wednesday' THEN 3
        WHEN day_week = 'Thursday' THEN 4
        WHEN day_week = 'Friday' THEN 5
        WHEN day_week = 'Saturday' THEN 6
        WHEN day_week = 'Sunday' THEN 7
    END;
-- We can see that the day with more passengers departing is on Monday and the day with least passengers departing
-- is on Sunday (considering that on 04/10 the trip 2 is still at status 1).


-- Let's check which trip has the biggest duration in hours
SELECT t.trip_ID, r.departure_station, r.arrival_station, HOUR(TIMEDIFF(arrival_time, departure_time)) AS trip_duration, t.departure_time, t.arrival_time
FROM Trips AS t
LEFT JOIN Routes AS r ON t.route_ID = r.route_ID
WHERE t.status = 1
ORDER BY trip_duration DESC;
-- Amazing! Trip 1 takes 74h and is still the one with more passengers!

-- Let's check which passengers have more than one booking
SELECT passenger_ID, COUNT(passenger_ID) AS passenger_count_booking
FROM Bookings
GROUP BY passenger_ID
HAVING passenger_count_booking > 1
ORDER BY passenger_count_booking;
-- We can see that passengers 75 and 85 have 2 bookings. Let's check their info and their bookings:
SELECT b.passenger_ID, p.first_name, p.last_name, p. age, p.nationality, b.route_ID, r.departure_station, r.arrival_station 
FROM Bookings AS b
LEFT JOIN Passengers AS p ON b.passenger_ID = p.passenger_ID
LEFT JOIN Routes AS r ON b.route_ID = r.route_ID
WHERE b.passenger_ID = 75 OR b.passenger_ID = 82
ORDER BY age; 
-- We can see that Donetta and Teddie have 2 bookings:
-- Donetta, aged 25 and Mexican booked the Bangkok-Mocow trip and Kuala Lumpur-Beijing trip as well
-- Teddie, aged 66 and Chinese booked the Lisbon-Dubai trip and Bangkok-Moscow trip as well

-- Let's check where and when Ines is travelling
SELECT CONCAT(p.first_name, ' ', p.last_name) AS full_name, p.age, p.nationality, r.departure_station, r.arrival_station, t.departure_time
FROM Passengers AS p
RIGHT JOIN Bookings AS b ON p.passenger_ID = b.passenger_ID
LEFT JOIN Routes AS r ON b.route_ID = r.route_ID
LEFT JOIN Trips AS t ON b.trip_ID = t.trip_ID
WHERE CONCAT(p.first_name, ' ', p.last_name) LIKE 'Ines%';
-- Great! Ines, aged 27 and Portuguese, will be travelling on the 11th of October from Lisbon to Dubai!

-- Imagine that this was actually real and not a fake scenario. People would be able to travel faster to different capitals of the World.
-- Considering all the assumptions, these world trips would be a complete success!