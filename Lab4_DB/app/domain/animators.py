from typing import Dict, Any
from app import db


class Animator(db.Model):
    __tablename__ = 'Animators'

    idAnimators = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(45), nullable=False)
    Surname = db.Column(db.String(45), nullable=False)
    Years = db.Column(db.String(45), nullable=False)

    def __repr__(self):
        return f"Animator(idAnimators={self.idAnimators}, Name='{self.Name}', Surname='{self.Surname}', Years='{self.Years}')"

    def to_dict(self) -> Dict[str, Any]:
        return {
            'idAnimators': self.idAnimators,
            'Name': self.Name,
            'Surname': self.Surname,
            'Years': self.Years
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'Animator':
        return Animator(
            Name=data.get('Name'),
            Surname=data.get('Surname'),
            Years=data.get('Years')
        )
