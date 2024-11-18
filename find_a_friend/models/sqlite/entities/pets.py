from sqlalchemy import INTEGER, Column, String

from find_a_friend.models.sqlite.settings.base import Base


class PetsTable(Base):
    __tablename__ = 'pets'
    __table_args__ = {'extend_existing': True}
    id = Column(INTEGER, primary_key=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)

    def __repr__(self):
        return f'Pets [name={self.name}, type={self.type}]'
