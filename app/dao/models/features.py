from app.setup_db import db


class Features(db.Model):
    __tablename__ = 'features'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    feature = db.Column(db.String)

    def to_dict(self):
        return {
            column.name: getattr(self, column.name)
            for column in self.__table__.columns
        }

    def __repr__(self):
        return f'Feature: {self.feature}'
