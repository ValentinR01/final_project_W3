from models.base import Base


class Comment(Base):
    """This class represents the comment table."""
    __tablename__ = 'comment'

    id = None
    content = None
    created_at = None
    external_name = None
    posted_by = None
    asset = None

    def __init__(self, content, created_at, external_name, posted_by, asset):
        self.content = content
        self.created_at = created_at
        self.external_name = external_name
        self.posted_by = posted_by
        self.asset = asset











id - id
content - str
created_at - datetime
external_name - string
posted_by - uuid
asset - uuid