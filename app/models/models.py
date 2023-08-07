from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, UUID
import uuid

metadata = MetaData()

roles = Table(
    "users",
    metadata,
    Column("id", UUID(as_uuid=True), default=uuid.uuid4(), primary_key=True),
    Column("first_name", String(30), nullable=False),
    Column("last_name", String(30), nullable=False),
    Column("email", String(30), nullable=False),
    Column("password", String(150), nullable=False),
    Column("role", String(30), nullable=False)

)