-- Description: This query contains the main data need to be inserted into the database.


-- Step Life Cycle


-- Meta Key
INSERT INTO "meta_key" (key)
VALUES ('style'), ('period'), ('level'), ('instruments'), ('skill');


-- Language
INSERT INTO "language" (name, code)
VALUES ('english', 'en'), ('french', 'fr');

-- Room
INSERT INTO "room" (name)
VALUES ('amphi mozart'), ('room violin'), ('room piano'), ('room guitar');

-- Transformation
INSERT INTO "transformation" (deposit_path)
VALUES ('/saline/transformation/file20230602_AA.mp4');

-- Type
INSERT INTO "type" (name)
VALUES ('lesson'), ('interview'), ('presentation'), ('concert'), ('other');

-- Domain
INSERT INTO "domain" (name)
VALUES ('redaction'), ('translation'), ('management'), ('development');

-- Role
INSERT INTO "role" (name)
VALUES ('worker'), ('lead'), ('superadmin'), ('dev');