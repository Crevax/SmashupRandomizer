CREATE TABLE IF NOT EXISTS deck_sets (
  set_id SERIAL PRIMARY KEY,
  set_name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS decks (
  deck_id SERIAL PRIMARY KEY,
  set_id INT REFERENCES deck_sets(set_id),
  deck_name TEXT NOT NULL
);