CREATE TABLE users(
   id SERIAL PRIMARY KEY,
   username VARCHAR(100) NOT NULL,
   email VARCHAR(100) NOT NULL,
   password VARCHAR(100) NOT NULL,
   contact VARCHAR(100) NOT NULL
);

CREATE TABLE rides(
   id SERIAL PRIMARY KEY,
   route VARCHAR(100) NOT NULL,
   driver INT references users(id),
   fare VARCHAR(100) NOT NULL,
   created_at TIMESTAMP default CURRENT_TIMESTAMP
);

CREATE TABLE requests(
   id SERIAL PRIMARY KEY,
   passenger INT references users(id),
   ride INT references rides(id),
   status BOOLEAN NOT NULL DEFAULT FALSE,
   created_at TIMESTAMP default CURRENT_TIMESTAMP
);