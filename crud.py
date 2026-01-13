from app.models import Bill
def save(db,units,amount):
    b=Bill(units=units,amount=amount)
    db.add(b);db.commit();db.refresh(b);return b
