-- Description: This query contains the main data need to be inserted into the database.


-- Step Life Cycle
INSERT INTO "step_lifecycle" (step)
VALUES
    ('initialization'), ('captation'), ('regisseur_review'), ('post_production'), ('admin_review'),
    ('transformation'), ('edition'), ('translation'), ('ready'), ('deleted'), ('refused');

superadmin :
    valdation montage : http://localhost:8004/api/v1/assets/?step_lifecycle_id=5
    validation finale : http://localhost:8004/api/v1/assets/?step_lifecycle_id=9
    en cours : http://localhost:8004/api/v1/assets/
admin post prod :
    à attribuer : http://localhost:8004/api/v1/assets/?step_lifecycle_id=4/?status_by_domain_id=1
                  http://localhost:8004/api/v1/assets/?step_lifecycle_id=6/?status_by_domain_id=1
    en cours : http://localhost:8004/api/v1/assets/?step_lifecycle_id=4/?status_by_domain_id=2
               http://localhost:8004/api/v1/assets/?step_lifecycle_id=6/?status_by_domain_id=2
               http://localhost:8004/api/v1/assets/?step_lifecycle_id=4/?status_by_domain_id=3
               http://localhost:8004/api/v1/assets/?step_lifecycle_id=6/?status_by_domain_id=3
    à venir : http://localhost:8004/api/v1/assets/?step_lifecycle_id=5
admin édito :
    à attribuer : http://localhost:8004/api/v1/assets/?step_lifecycle_id=7/?status_by_domain_id=1
                  http://localhost:8004/api/v1/assets/?step_lifecycle_id=8/?status_by_domain_id=1
    en cours : http://localhost:8004/api/v1/assets/
    à venir : http://localhost:8004/api/v1/assets/
admin régisseur (pas besoin à venir):
    à attribuer : http://localhost:8004/api/v1/assets/
    en cours : http://localhost:8004/api/v1/assets/
    à venir : http://localhost:8004/api/v1/assets/
admin captation :
    à attribuer : http://localhost:8004/api/v1/assets/
    en cours : http://localhost:8004/api/v1/assets/
    à venir : http://localhost:8004/api/v1/assets/
régisseur (pas besoin à venir):
    à commencer : http://localhost:8004/api/v1/assets/
    en cours : http://localhost:8004/api/v1/assets/
captation :
    à commencer : http://localhost:8004/api/v1/assets/
    en cours : http://localhost:8004/api/v1/assets/
post-prod :
    à commencer : http://localhost:8004/api/v1/assets/
    en cours : http://localhost:8004/api/v1/assets/
edition :
    à commencer : http://localhost:8004/api/v1/assets/
    en cours : http://localhost:8004/api/v1/assets/
traduction :
    à commencer : http://localhost:8004/api/v1/assets/
    en cours : http://localhost:8004/api/v1/assets/


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
VALUES ('lesson'), ('interview'), ('presentation'), ('concert'), ('masterclass'), ('other');


-- Domain
INSERT INTO "domain" (name)
VALUES ('Regie'), ('Captation'), ('Post-prod'), ('Edition'), ('Traduction');


-- Status By Domain
INSERT INTO "status_by_domain" (status)
VALUES ('to_assign'), ('to_begin'), ('in_progress');


-- Role
INSERT INTO "role" (name)
VALUES ('worker'), ('lead'), ('superadmin');


-- Post Prod
INSERT INTO "post_prod" (
    rush_received, started_at, ended_at, validated_at, deposit_path, version
)
VALUES (
    true, null, null, null, '/saline/post_prod/file20230602_AA.mp4', 1
);

