from pydantic import Field
from typing import Optional
from datetime import datetime
from uuid import UUID, uuid4
from beanie import Document, Indexed, Link, before_event, Replace, Insert


class User(Document):
    class Settings:
        collection = 'Users'
    user_id: UUID = Field(default_factory=uuid4, unique=True)
    phone_number: str = Indexed(unique=True)
    first_name: str
    last_name: str
    email: str = Indexed(unique=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    def __hash__(self) -> int:
        return hash(self.user_id)

    def __eq__(self, other: object)->bool:
        if isinstance(other, User):
            return self.user_id == other.user_id
        return False
    
    @before_event([Replace, Insert])
    def update_update_at(self):
        self.updated_at = datetime.utcnow()



