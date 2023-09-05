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
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(),
                           onupdate=db.func.current_timestamp())
    published_at = db.Column(db.DateTime, nullable=True)
    last_assignment_at = \
        db.Column(db.DateTime, default=db.func.current_timestamp())

    # Relationship
    assets_translated = db.relationship('AssetTranslated', backref='asset')
    subtitles = db.relationship('Subtitle', backref='asset')

    # FK
    composer_id = \
        db.Column(db.Integer, db.ForeignKey('composer.id'), nullable=True)
    current_assigned_user_id = \
        db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    created_by_id = \
        db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    updated_by_id = \
        db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    speaker_id = \
        db.Column(db.Integer, db.ForeignKey('speaker.id'), nullable=True)
    status_by_domain_id = db.Column(
        db.Integer, db.ForeignKey('status_by_domain.id'), default=1
    )
    step_lifecycle_id = db.Column(
        db.Integer, db.ForeignKey('step_lifecycle.id'), default=1
    )
    booking_id = \
        db.Column(db.Integer, db.ForeignKey('booking.id'), nullable=True)
    captation_id = \
        db.Column(db.Integer, db.ForeignKey('captation.id'), nullable=True)
    post_prod_id = \
        db.Column(db.Integer, db.ForeignKey('post_prod.id'), nullable=True)
    transformation_id = db.Column(
        db.Integer, db.ForeignKey('transformation.id'), nullable=True
    )

    # Relationships FK
    composer = db.relationship('Composer', backref='assets')
    current_assigned_user = db.relationship('User', foreign_keys=[
        current_assigned_user_id], backref='assigned_assets')
    created_by = db.relationship('User', foreign_keys=[created_by_id],
                                 backref='created_assets')
    updated_by = db.relationship('User', foreign_keys=[updated_by_id],
                                 backref='updated_assets')
    speaker = db.relationship('Speaker', backref='assets')
    status_by_domain = db.relationship('StatusByDomain', backref='assets')
    step_lifecycle = db.relationship('StepLifecycle', backref='assets')
    booking = db.relationship('Booking', backref='assets')
    captation = db.relationship('Captation', backref='assets')
    post_prod = db.relationship('PostProd', backref='assets')
    transformation = db.relationship('Transformation', backref='assets')

    def __init__(self, title, music_title, created_by_id,
                 step_lifecycle_id, updated_by_id, status_by_domain_id,
                 current_assigned_user_id=None, booking_id=None,
                 composer_id=None, speaker_id=None, captation_id=None,
                 post_prod_id=None, transformation_id=None,
                 has_high_priority=False, published=False, created_at=None,
                 updated_at=None, published_at=None, last_assignment_at=None,
                 student_fullname=None, art_description=None, thumbnail=None,
                 asset_description=None, link_partitions=None, resumed=None):
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
