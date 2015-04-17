DO
$do$
BEGIN
  IF NOT EXISTS (SELECT * FROM deck_sets) THEN
    INSERT INTO deck_sets (set_name)
    VALUES ('Core'), ('Awesome Level 9000'), ('The Obligatory Cthulhu Set'), ('Science Fiction Double Feature'), ('The Big Geeky Box'), ('Monster Smash'), ('Pretty Pretty Smash Up');
  END IF;
END
$do$