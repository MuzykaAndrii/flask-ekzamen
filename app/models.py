from . import db

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    year_posted = db.Column(db.String(10), nullable=False)
    count_of_pages = db.Column(db.Integer, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    note = db.Column(db.String(300), nullable=False)
    type_of_art = db.Column(db.String(50), nullable=False)

    def __init__(self, name, year_posted, count_of_pages, author, note, type_of_art):
        self.name = name
        self.year_posted = year_posted
        self.count_of_pages = count_of_pages
        self.author = author
        self.note = note
        self.type_of_art = type_of_art
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def __repr__(self):
        return f"Post('{self.name}', '{self.author}', '{self.year_posted}', '{self.type_of_art}')"


