from typing import Dict, Any
from app import db

class Agency(db.Model):
    __tablename__ = 'Agencies'

    idAgencies = db.Column(db.Integer, primary_key=True)
    Name_agency = db.Column(db.String(45), nullable=False)
    Number = db.Column(db.String(45), nullable=False)

    def __repr__(self):
        return f"Agency(idAgencies={self.idAgencies}, Name_agency='{self.Name_agency}', Number='{self.Number}')"

    def to_dict(self) -> Dict[str, Any]:
        return {
            'idAgencies': self.idAgencies,
            'Name_agency': self.Name_agency,
            'Number': self.Number
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'Agency':
        return Agency(
            Name_agency=data.get('Name_agency'),
            Number=data.get('Number')
        )

