-- Description: This query will insert the layer 1 data into the database.


-- User
INSERT INTO "user"
    (email, fullname, password, profile_picture, created_at,
    count_assigning_asset, role_id, domain_id)
VALUES
    ('nass@saline.com', 'Nass La Menass',
    'HASH', NULL, CURRENT_TIMESTAMP, 0, 4, 4);


-- Meta Value
INSERT INTO "meta_value" (value, meta_key_id)
VALUES
    -- Style
    ('baroque', 1), ('classical', 1), ('romantic', 1), ('contemporary', 1),
    -- Period
    ('renaissance', 2), ('baroque', 2), ('classical', 2), ('romantic', 2), ('modern', 2),
    -- Difficulty Level
    ('beginner', 3), ('intermediate', 3), ('advanced', 3),
    -- Instruments
    ('piano', 4), ('guitar', 4), ('violin', 4), ('drums', 4), ('saxophone', 4), ('trumpet', 4), ('flute', 4),
    -- Skill
    ('sight-reading', 5), ('ear-training', 5), ('improvisation', 5), ('composition', 5);


-- Composer
        self.fullname = fullname
        self.biography = biography
        self.publishable = publishable
        self.last_update = last_update
        self.composer_parent = composer_parent
        self.language_id = language_id
INSERT INTO "composer"
    (fullname, biography, publishable, last_update, composer_parent_id, language_id)
VALUES
    ('Johann Sebastian Bach', 'Johann Sebastian Bach was a German composer and musician of the Baroque period. He is known for instrumental compositions such as the Brandenburg Concertos and the Goldberg Variations, and for vocal music such as the St Matthew Passion and the Mass in B minor.', true, CURRENT_TIMESTAMP, NULL, 1),
    ('Ludwig van Beethoven', 'Ludwig van Beethoven was a German composer and pianist. A crucial figure in the transition between the classical and romantic eras in classical music, he remains one of the most recognized and influential musicians of this period, and is considered to be one of the greatest composers of all time.', true, CURRENT_TIMESTAMP, NULL, 1),
    ('Wolfgang Amadeus Mozart', 'Wolfgang Amadeus Mozart, baptised as Johannes Chrysostomus Wolfgangus Theophilus Mozart, was a prolific and influential composer of the Classical period.', true, CURRENT_TIMESTAMP, NULL, 1),
    ('Frédéric Chopin', 'Frédéric François Chopin was a Polish composer and virtuoso pianist of the Romantic era who wrote primarily for solo piano. He has maintained worldwide renown as a leading musician of his era, one whose "poetic genius was based on a professional technique that was without equal in his generation."', true, CURRENT_TIMESTAMP, NULL, 1),
    ('Franz Liszt', 'Franz Liszt was a Hungarian composer, virtuoso pianist, conductor, music teacher, arranger, and organist of the Romantic era. He was also a writer, a philanthropist, a Hungarian nationalist and a Franciscan tertiary.', true, CURRENT_TIMESTAMP, NULL, 1),
    ('Robert Schumann', 'Robert Schumann was a German composer, pianist, and influential music critic. He is widely regarded as one of the greatest composers of the Romantic era. Schumann left the study of law, intending to pursue a career as a virtuoso pianist.', true, CURRENT_TIMESTAMP, NULL, 1);


-- Speaker
INSERT INTO "speaker"
    (fullname, biography, last_update, publishable, speaker_parent_id, language_id)
VALUES
    ('John Doe', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.', CURRENT_TIMESTAMP, true, NULL, 1),
    ('Jane Smith', 'Sed ut perspiciatis unde omnis iste natus error sit voluptatem.', CURRENT_TIMESTAMP, true, NULL, 2),
    ('Nass La Menass', 'At vero eos et accusamus et iusto odio dignissimos.', CURRENT_TIMESTAMP, true, NULL, 1);


-- Booking
INSERT INTO "booking" (date, timeslot, room_id)
VALUES
    ('2023-10-08', 'am', 1),
    ('2023-10-08', 'pm', 1),
    ('2023-10-09', 'pm', 1),
    ('2023-10-09', 'am', 2);


-- Captation
INSERT INTO "captation" (duration, filmed_at, deposit_path, report, type_id)
VALUES
    (3600, '2023-10-08', '/saline/captation/file20230602_AA.mp4', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.', 1),
    (3750, '2023-10-08', '/saline/captation/file20230602_AA.mp4', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.', 1),
    (2500, '2023-10-08', '/saline/captation/file20230602_AA.mp4', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.', 1),
    (1200, '2023-10-08', '/saline/captation/file20230602_AA.mp4', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.', 1);
