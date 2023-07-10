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
