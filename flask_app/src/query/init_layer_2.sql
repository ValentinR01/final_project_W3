-- Description: This query will insert the layer 2 data into the database.


-- Subtitle
INSERT INTO "subtitle" (file_path, published, translated_by, language_id, asset_id)
VALUES ('/saline/subtitle/file20230602_AA.sub', true, 1, 1, 1);


-- Asset Translated
INSERT INTO "asset_translated" (
    title, description, music_title, created_at, updated_at,
    last_assignment_at, resumed, current_assigned_user_id, composer_id,
    speaker_id, language_id, step_lifecycle_id, status_by_domain_id, asset_id
)
VALUES (
    'Title translated',
    'Description: taque earum rerum us maiores  repellat translated',
    'Music title translated', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP,
    'Resumed: Sed ut perspiciatis unde omnis iste natus error sit translated',
    1, 1, 1, 1, 1, 1, 1
);


-- Metadata
INSERT INTO "metadata" (meta_value_id, asset_id)
VALUES (1, 1), (7, 1), (11, 1), (12, 1);
