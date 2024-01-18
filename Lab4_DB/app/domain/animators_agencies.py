from typing import Dict, Any
from app import db

class AnimatorsAgencies(db.Model):
    __tablename__ = 'animators_agencies'
    idAnimators_Agencies=db.Column(db.Integer, primary_key=True, autoincrement=True)


    def __repr__(self) -> str:
        return f"AnimatorsAgencies(idAnimators_Agencies={self.idAnimators_Agencies})"

    def to_dict(self) -> Dict[str, Any]:
        return {
            'idAnimators_Agencies': self.idAnimators_Agencies
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'AnimatorsAgencies':
        return AnimatorsAgencies()
