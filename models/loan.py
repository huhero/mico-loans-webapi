# SqlAlchemy
import sqlalchemy


# DB
from db import metadata


# Models
from models.enums import State

loan = sqlalchemy.Table(
    "loans",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("contract_id", sqlalchemy.String(100), unique=True),
    sqlalchemy.Column("contract_document_url", sqlalchemy.String(250)),
    sqlalchemy.Column("amount", sqlalchemy.Integer),
    sqlalchemy.Column("term", sqlalchemy.Integer),
    sqlalchemy.Column("interest_rate", sqlalchemy.Float),
    sqlalchemy.Column(
        "state",
        sqlalchemy.Enum(State),
        nullable=False,
        server_default=State.pending.name,
    ),
    sqlalchemy.Column("user_id", sqlalchemy.ForeignKey("users.id"), nullable=False),
    sqlalchemy.Column(
        "created_at", sqlalchemy.DateTime, server_default=sqlalchemy.func.now()
    ),
    sqlalchemy.Column(
        "last_updated",
        sqlalchemy.DateTime,
        server_default=sqlalchemy.func.now(),
        onupdate=sqlalchemy.func.now(),
    ),
)
