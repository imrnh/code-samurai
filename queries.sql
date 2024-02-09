create table users(
	user_id SERIAL primary key,
	user_name varchar(255),
	balance int
);

create table stations(
	station_id SERIAL primary key,
	station_name varchar(255),
	longitude double,
	latitude double,
);


create table trains(
	train_id SERIAL primary key,
	train_name varchar(255),
	capacity int,
);


create table train_stops(
    id SERIAL primary key,
    train_id int REFERENCES trains(train_id),
    station_id int REFERENCES stations(station_id)
);