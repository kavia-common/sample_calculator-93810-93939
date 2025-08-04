from .db import db

# PUBLIC_INTERFACE
class CalculationResult(db.Model):
    """Model representing a calculation result (expandable for more fields)."""
    __tablename__ = 'calculation_results'
    id = db.Column(db.Integer, primary_key=True)
    input_data = db.Column(db.Text, nullable=False)
    result = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)

# """Extend with more models for users, logs, admin as needed."""
