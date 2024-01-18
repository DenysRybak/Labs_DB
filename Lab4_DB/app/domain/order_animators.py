from typing import Dict, Any
from app import db

class OrderAnimators(db.Model):
    __tablename__ = 'order_animators'
    id_Order = db.Column(db.Integer, db.ForeignKey('orders.idOrder'), primary_key=True)

    def __repr__(self) -> str:
        return f"OrderAnimators(id_Order={self.id_Order})"

    def to_dict(self) -> Dict[str, Any]:
        return {
            'id_Order': self.id_Order
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'OrderAnimators':
        return OrderAnimators(
            id_Order=data.get('id_Order')
        )
