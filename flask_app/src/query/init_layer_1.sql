-- Description: This query will insert the layer 1 data into the database.


-- User
INSERT INTO "user"
    (email, fullname, password, profile_picture, created_at,
    count_assigning_asset, role_id, domain_id)
VALUES
    ('nass@saline.com', 'Nass La Menass',
    '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8',
    NULL, CURRENT_TIMESTAMP, 0, 4, 4);
