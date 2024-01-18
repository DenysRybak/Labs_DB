from typing import Dict, Any
from app import db

class OrderDays(db.Model):
    __tablename__ = 'order_days'
    idAnimator_Work_Days = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Time_work = db.Column(db.String(45), nullable=False)


    def __repr__(self) -> str:
        return f"OrderDays(idAnimator_Work_Days={self.idAnimator_Work_Days}, Time_work='{self.Time_work}')"

    def to_dict(self) -> Dict[str, Any]:
        return {
            'idAnimator_Work_Days': self.idAnimator_Work_Days,
            'Time_work': self.Time_work
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'OrderDays':
        return OrderDays(
            Time_work=data.get('Time_work')
        )
