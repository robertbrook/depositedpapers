from google.appengine.ext import db

class Deposit(db.Model):
	deposit_number = db.StringProperty()
	deposit_legislature = db.StringProperty()
	deposit_date = db.StringProperty()
	deposit_source = db.StringProperty()
	deposit_link = db.StringProperty()
	deposit_file = db.StringProperty()
	text = db.StringProperty()
	associated_legislation = db.StringProperty()
