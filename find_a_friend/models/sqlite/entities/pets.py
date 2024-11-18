from sqlalchemy import INTEGER, Column, String

from find_a_friend.models.sqlite.settings.base import Base


class PetsTable(Base):
    __tablename__ = 'pets'
    id = Column(INTEGER, primary_key=True)
    nome = Column(String, nullable=False)
    type = Column(String, nullable=False)

    def __repr__(self):
        return f'Pets [name={self.name}, type={self.type}]'
