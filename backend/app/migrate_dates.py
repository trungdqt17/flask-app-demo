from app import create_app
from app.models import db, Book
from datetime import datetime

def migrate_dates():
    app = create_app()
    with app.app_context():
        books = Book.query.all()
        for book in books:
            if book.published_date and isinstance(book.published_date, str):
                try:
                    book.published_date = datetime.strptime(book.published_date, '%Y-%m-%d').date()
                except ValueError:
                    # If date can't be parsed, set it to None
                    book.published_date = None
        db.session.commit()

if __name__ == '__main__':
    migrate_dates()
    print("Date migration completed successfully")
