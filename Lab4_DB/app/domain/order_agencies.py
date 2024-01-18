from typing import Dict, Any
from app import db

class OrderAgencies(db.Model):
    __tablename__ = 'order_agencies'
    idOrder_Agencies = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Order_Agenciescol = db.Column(db.String(45), nullable=False)

    def __repr__(self) -> str:
        return f"OrderAgencies(idOrder_Agencies={self.idOrder_Agencies}, Order_Agenciescol='{self.Order_Agenciescol}')"

    def to_dict(self) -> Dict[str, Any]:
        return {
            'idOrder_Agencies': self.idOrder_Agencies,
            'Order_Agenciescol': self.Order_Agenciescol
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'OrderAgencies':
        return OrderAgencies(
            Order_Agenciescol=data.get('Order_Agenciescol')
        )
