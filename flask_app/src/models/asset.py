from db import db
from models.base import Base


class Asset(Base):
    """This class represents the asset table"""
    __tablename__ = 'asset'

    id = db.Column(db.Integer, primary_key=True)

    # Nullable False
    title = db.Column(db.String(250), unique=True, nullable=False)
    music_title = db.Column(db.String(250), nullable=False)

    # Nullable True
    art_description = db.Column(db.String(5000), nullable=True)
    student_fullname = db.Column(db.String(250), nullable=True)
    asset_description = db.Column(db.String(5000), nullable=True)
    link_partitions = db.Column(db.String(1000), nullable=True)
    thumbnail = db.Column(db.String(1000), nullable=True)
    resumed = db.Column(db.String(5000), nullable=True)

    # Boolean
    has_high_priority = db.Column(db.Boolean, default=False)
    published = db.Column(db.Boolean, default=False)

    # Date
    created_at = db.Column(db.Date, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    published_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    last_assignment_at = \
        db.Column(db.DateTime, default=db.func.current_timestamp())

    # FK
    composer_id = \
        db.Column(db.Integer, db.ForeignKey('composer.id'), nullable=False)
    current_assigned_user_id = \
        db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_by_id = \
        db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    updated_by_id = \
        db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    speaker_id = \
        db.Column(db.Integer, db.ForeignKey('speaker.id'), nullable=False)
    status_by_domain_id = db.Column(
        db.Integer, db.ForeignKey('status_by_domain.id'), nullable=False
    )
    step_lifecycle_id = db.Column(
        db.Integer, db.ForeignKey('step_lifecycle.id'), nullable=False
    )
    booking_id = \
        db.Column(db.Integer, db.ForeignKey('booking.id'), nullable=False)
    captation_id = \
        db.Column(db.Integer, db.ForeignKey('captation.id'), nullable=False)
    post_prod_id = \
        db.Column(db.Integer, db.ForeignKey('post_prod.id'), nullable=False)
    transformation_id = db.Column(
        db.Integer, db.ForeignKey('transformation.id'), nullable=False
    )
    asset_translated_id = db.Column(
        db.Integer, db.ForeignKey('asset_translated.id'), nullable=False
    )
    subtitle_id = \
        db.Column(db.Integer, db.ForeignKey('subtitle.id'), nullable=False)

    def __init__(self, title, music_title, art_description, student_fullname,
                 asset_description, link_partitions, thumbnail, resumed,
                 has_high_priority, published, created_at, updated_at,
                 published_at, last_assignment_at, composer_id,
                 current_assigned_user_id, created_by_id, updated_by_id,
                 speaker_id, status_by_domain_id, step_lifecycle_id,
                 booking_id, captation_id, post_prod_id, transformation_id,
                 asset_translated_id, subtitle_id):
        self.title = title
        self.music_title = music_title
        self.art_description = art_description
        self.student_fullname = student_fullname
        self.asset_description = asset_description
        self.link_partitions = link_partitions
        self.thumbnail = thumbnail
        self.resumed = resumed
        self.has_high_priority = has_high_priority
        self.published = published
        self.created_at = created_at
        self.updated_at = updated_at
        self.published_at = published_at
        self.last_assignment_at = last_assignment_at
        self.composer_id = composer_id
        self.current_assigned_user_id = current_assigned_user_id
        self.created_by_id = created_by_id
        self.updated_by_id = updated_by_id
        self.speaker_id = speaker_id
        self.status_by_domain_id = status_by_domain_id
        self.step_lifecycle_id = step_lifecycle_id
        self.booking_id = booking_id
        self.captation_id = captation_id
        self.post_prod_id = post_prod_id
        self.transformation_id = transformation_id
        self.asset_translated_id = asset_translated_id
        self.subtitle_id = subtitle_id
