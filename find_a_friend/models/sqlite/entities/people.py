from sqlalchemy import INTEGER, Column, ForeignKey, String

from find_a_friend.models.sqlite.settings.base import Base


class PeopleTable(Base):
    __tablename__ = 'people'
    __table_args__ = {'extend_existing': True}
    id = Column(INTEGER, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    age = Column(INTEGER, nullable=False)
    pet_id = Column(INTEGER, ForeignKey('pets_id'))
    type = Column(String, nullable=False)

    def __repr__(self):
        return f'People [first_name={self.first_name},last_name={self.last_name}, pet_id={self.pet_id}]'
