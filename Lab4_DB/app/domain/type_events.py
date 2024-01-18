from typing import Dict, Any
from app import db

class TypeEvent(db.Model):
    __tablename__ = 'Type_Events'

    idType_Events = db.Column(db.Integer, primary_key=True)
    Name_event = db.Column(db.String(45), nullable=False)
    idOrder = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"TypeEvent(idType_Events={self.idType_Events}, Name_event='{self.Name_event}', idOrder={self.idOrder})"

    def to_dict(self) -> Dict[str, Any]:
        return {
            'idType_Events': self.idType_Events,
            'Name_event': self.Name_event,
            'idOrder': self.idOrder
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'TypeEvent':
        return TypeEvent(
            Name_event=data.get('Name_event'),
            idOrder=data.get('idOrder')
        )
