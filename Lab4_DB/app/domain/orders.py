from typing import Dict, Any
from app import db

class Order(db.Model):
    __tablename__ = 'order'
    idOrder = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(45), nullable=False)

    def __repr__(self) -> str:
        return f"Order(idOrder={self.idOrder}, Name='{self.Name}')"

    def to_dict(self) -> Dict[str, Any]:
        return {
            'idOrder': self.idOrder,
            'Name': self.Name
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'Order':
        return Order(
            Name=data.get('Name')
        )
