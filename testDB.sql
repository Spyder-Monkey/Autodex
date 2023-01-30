-- \copy target_table (column-1, column-2, column-3, ...) from '/path/to/local/filename.csv' WITH DELIMITER ',' CSV HEADER;
-- wget https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeId/11081\?format\=csv -O - >> ModelsForMake.csv

CREATE TABLE IF NOT EXISTS users (
    id SERIAL,
    username VARCHAR(64) NOT NULL,
    password VARCHAR(64) NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS make (
    id INTEGER NOT NULL,
    make_name TEXT NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS model (
    id INTEGER NOT NULL,
    model_name TEXT NOT NULL,
    make_id INTEGER NOT NULL,
    make_name TEXT NOT NULL,
    PRIMARY KEY(id),
    CONSTRAINT fk_make FOREIGN KEY(make_id) REFERENCES make(id)
);

CREATE TABLE IF NOT EXISTS engine (
    id SERIAL,
    model VARCHAR NOT NULL,
    horsepower INTEGER NOT NULL DEFAULT 0,
    displacement INTEGER NOT NULL DEFAULT 0,
    cylinders INTEGER NOT NULL DEFAULT 0,
    configuration TEXT NOT NULL DEFAULT '',
    drive_type TEXT NOT NULL DEFAULT '',
    fuel_type TEXT NOT NULL DEFAULT '',
    PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS body (
    id SERIAL,
    type TEXT NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS vehicle (
    vin VARCHAR(17) NOT NULL,
    year INTEGER NOT NULL DEFAULT 1900,
    color TEXT NOT NULL DEFAULT '',
    make_id INTEGER NOT NULL,
    model_id INTEGER NOT NULL,
    body_id INTEGER NOT NULL,
    engine_id INTEGER NOT NULL,
    PRIMARY KEY(vin),
    CONSTRAINT fk_make FOREIGN KEY(make_id) REFERENCES make(id),
    CONSTRAINT fk_model FOREIGN KEY(model_id) REFERENCES model(id),
    CONSTRAINT fk_body FOREIGN KEY(body_id) REFERENCES body(id),
    CONSTRAINT fk_engine FOREIGN KEY(engine_id) REFERENCES engine(id)
);

CREATE TABLE IF NOT EXISTS tracked_vehicles (
    user_id INTEGER NOT NULL,
    vehicle_vin VARCHAR(17) NOT NULL,
    PRIMARY KEY(user_id, vehicle_vin)
);