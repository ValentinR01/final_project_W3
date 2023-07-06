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

    # Relationship
    # metadatas = db.relationship('Metadata', backref='asset', lazy=True)
