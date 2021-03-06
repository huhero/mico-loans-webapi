# SqlAlchemy
from email.policy import default
import sqlalchemy


# enums
from models.enums import RoleType


# DB
from db import metadata


user = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("email", sqlalchemy.String(120), unique=True),
    sqlalchemy.Column("password", sqlalchemy.String(255)),
    sqlalchemy.Column("first_name", sqlalchemy.String(255)),
    sqlalchemy.Column("last_name", sqlalchemy.String(255)),
    sqlalchemy.Column("phone", sqlalchemy.String(20)),
    sqlalchemy.Column(
        "role",
        sqlalchemy.Enum(RoleType),
        nullable=False,
        server_default=RoleType.complainer.name,
    ),
    sqlalchemy.Column("active", sqlalchemy.Boolean(), default=False),
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
