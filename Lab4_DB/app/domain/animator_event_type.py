from typing import Dict, Any
from app import db

class AnimatorEventType(db.Model):
    __tablename__ = 'animator_event_types'
    idAnimator_Event_Types = db.Column(db.Integer, primary_key=True)


    def __repr__(self) -> str:
        return f"AnimatorEventType(idAnimator_Event_Types={self.idAnimator_Event_Types})"

    def to_dict(self) -> Dict[str, Any]:
        return {
            'idAnimator_Event_Types': self.idAnimator_Event_Types
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'AnimatorEventType':
        return AnimatorEventType(
            idAnimator_Event_Types=data.get('idAnimator_Event_Types')
        )
