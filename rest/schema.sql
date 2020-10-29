DROP TABLE IF EXISTS requests;

CREATE TABLE requests (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  request_duration timestamp NOT NULL,
  request_timestamp timestamp DEFAULT CURRENT_TIMESTAMP NOT NULL,
  request_termination timestamp NOT NULL
);

