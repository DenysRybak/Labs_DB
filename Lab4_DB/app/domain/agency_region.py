from typing import Dict, Any
from app import db

class AgencyRegion(db.Model):
    __tablename__ = 'agency_regions'
    idAgency_Regions = db.Column(db.Integer, primary_key=True)
    Region = db.Column(db.String(45), nullable=False)


    def __repr__(self) -> str:
        return f"AgencyRegion(idAgency_Regions={self.idAgency_Regions}, Region='{self.Region}')"

    def to_dict(self) -> Dict[str, Any]:
        return {
            'idAgency_Regions': self.idAgency_Regions,
            'Region': self.Region
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'AgencyRegion':
        return AgencyRegion(
            idAgency_Regions=data.get('idAgency_Regions'),
            Region=data.get('Region')
        )
