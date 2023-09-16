-- Description: This query will insert the layer 1 data into the database.


-- User
INSERT INTO "user" (
    email, fullname, password, profile_picture, created_at,
    count_assigning_asset, role_id, domain_id
)
VALUES
    ('nass@saline.com', 'Nass La Menass', 'pbkdf2:sha256:600000$MFIgXR9G8QmB3Yqw$cc22c03b43785f647894db48313da07f71a6204029985e671bf611e0c07493b7',
    NULL, CURRENT_TIMESTAMP, 0, 3, 4),
    ('translator@saline.com', 'Translator', 'pbkdf2:sha256:600000$MFIgXR9G8QmB3Yqw$cc22c03b43785f647894db48313da07f71a6204029985e671bf611e0c07493b7',
    NULL, CURRENT_TIMESTAMP, 0, 1, 2),
    ('regisseur@saline.com', 'Regisseur', 'pbkdf2:sha256:600000$MFIgXR9G8QmB3Yqw$cc22c03b43785f647894db48313da07f71a6204029985e671bf611e0c07493b7',
    NULL, CURRENT_TIMESTAMP, 0, 1, 5);


-- Specialty
INSERT INTO "specialty" (name, domain_id, language_id)
VALUES
    ('logistic', 5, NULL), ('light', 5, NULL), (NULL, 2, 2), (NULL, 2, 1), (NULL, 2, 3), (NULL, 2, 4), (NULL, 2, 5);


-- specialties_users
INSERT INTO "specialties_users" (user_id, specialty_id)
VALUES (2, 3), (3, 1), (3, 2);


-- Meta Value
INSERT INTO "meta_value" (value, meta_key_id)
VALUES
    -- Style
    ('jazz', 1), ('classical', 1), ('blues', 1), ('country', 1), ('rock', 1), ('pop', 1), ('electronic', 1),
    -- Period
    ('renaissance', 2), ('baroque', 2), ('romantic', 2), ('modern', 2), ('medieval', 2),
    -- Difficulty Level
    ('beginner', 3), ('intermediate', 3), ('advanced', 3),
    -- Instruments
    ('piano', 4), ('guitar', 4), ('violin', 4), ('drums', 4), ('saxophone', 4), ('trumpet', 4), ('flute', 4), ('harmonica', 4), ('bass', 4), ('harp', 4),
    -- Skill
    ('sight-reading', 5), ('ear-training', 5), ('improvisation', 5), ('composition', 5);


-- Composer
INSERT INTO "composer"
    (fullname, biography, publishable, last_update, composer_parent, language_id)
VALUES
    ('Johann Sebastian Bach', 'Johann Sebastian Bach was a German composer and musician of the Baroque period. He is known for instrumental compositions such as the Brandenburg Concertos and the Goldberg Variations, and for vocal music such as the St Matthew Passion and the Mass in B minor.', true, CURRENT_TIMESTAMP, NULL, 1),
    ('Ludwig van Beethoven', 'Ludwig van Beethoven was a German composer and pianist. A crucial figure in the transition between the classical and romantic eras in classical music, he remains one of the most recognized and influential musicians of this period, and is considered to be one of the greatest composers of all time.', true, CURRENT_TIMESTAMP, NULL, 1),
    ('Wolfgang Amadeus Mozart', 'Wolfgang Amadeus Mozart, baptised as Johannes Chrysostomus Wolfgangus Theophilus Mozart, was a prolific and influential composer of the Classical period.', true, CURRENT_TIMESTAMP, NULL, 1),
    ('Frédéric Chopin', 'Frédéric François Chopin was a Polish composer and virtuoso pianist of the Romantic era who wrote primarily for solo piano. He has maintained worldwide renown as a leading musician of his era, one whose "poetic genius was based on a professional technique that was without equal in his generation."', true, CURRENT_TIMESTAMP, NULL, 1),
    ('Franz Liszt', 'Franz Liszt was a Hungarian composer, virtuoso pianist, conductor, music teacher, arranger, and organist of the Romantic era. He was also a writer, a philanthropist, a Hungarian nationalist and a Franciscan tertiary.', true, CURRENT_TIMESTAMP, NULL, 1),
    ('Robert Schumann', 'Robert Schumann was a German composer, pianist, and influential music critic. He is widely regarded as one of the greatest composers of the Romantic era. Schumann left the study of law, intending to pursue a career as a virtuoso pianist.', true, CURRENT_TIMESTAMP, NULL, 1);


-- Speaker
INSERT INTO "speaker"
    (fullname, biography, last_update, publishable, speaker_parent, language_id)
VALUES
    ('John Doe', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.', CURRENT_TIMESTAMP, true, NULL, 1),
    ('Jane Smith', 'Sed ut perspiciatis unde omnis iste natus error sit voluptatem.', CURRENT_TIMESTAMP, true, NULL, 2),
    ('Nass La Menass', 'At vero eos et accusamus et iusto odio dignissimos.', CURRENT_TIMESTAMP, true, NULL, 1);


-- Booking
INSERT INTO "booking" (date, is_am_timeslot, room_id)
VALUES
    ('2023-10-08', true, 1),
    ('2023-10-08', false, 1),
    ('2023-10-09', false, 1),
    ('2023-10-09', true, 2);


-- Captation
INSERT INTO "captation" (duration, filmed_at, deposit_path, report, type_id)
VALUES
    (3600, '2023-10-08', '/saline/captation/file20231008_AA.mp4', 'Report: Lorem ipsum adipiscing elit', 1),
    (3750, '2023-10-08', '/saline/captation/file20231008_AB.mp4', 'Report: Lorem ipsum adipiscing elit', 1),
    (2500, '2023-06-02', '/saline/captation/file20230602_AC.mp4', 'Report: Lorem ipsum adipiscing elit', 2),
    (1200, '2023-06-02', '/saline/captation/file20230602_AD.mp4', 'Report: Lorem ipsum adipiscing elit', 2);


-- Asset
INSERT INTO "asset"(
    title, music_title, art_description, student_fullname, asset_description,
    link_partitions, thumbnail, resumed, has_high_priority, published, created_at,
    updated_at, published_at, last_assignment_at, composer_id, current_assigned_user_id,
    created_by_id, updated_by_id, speaker_id, status_by_domain_id, step_lifecycle_id,
    booking_id, captation_id, post_prod_id, transformation_id
)
VALUES (
    'Title', 'Music Title', 'Art Description: Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
    'Jean VALJEAN','Asset Description: Lorem ipsum dolor sit amet',
    'https://www.saline.com/partition/toto?file', 'https://www.saline.com/thumbnail/toto?picture',
    'Resumed: At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium',
    true, false, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, null, '2023-07-11',
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
);
