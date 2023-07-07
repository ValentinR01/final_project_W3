-- Description: This query contains the main data need to be inserted into the database.

-- Transformation
INSERT INTO "transformation" (deposit_path)
VALUES ('/saline/transformation/file20230602_AA.mp4');

-- Type
INSERT INTO "type" (name)
VALUES ('lesson'), ('interview'), ('presentation'), ('concert');

-- Domain
INSERT INTO "domain" (name)
VALUES ('redaction'), ('translation'), ('management'), ('development');

-- Role
INSERT INTO "role" (name)
VALUES ('worker'), ('lead'), ('superadmin'), ('dev');