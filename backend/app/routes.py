from flask import Blueprint, render_template, request, jsonify
from .models import db, Book
from datetime import datetime

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template("base.html")

@bp.route('/add-book')
def add_book_page():
    return render_template("add_book.html")

@bp.route('/books', methods=['GET'])
def list_books():
    books = Book.query.all()
    return render_template('books_list.html', books=books)

@bp.route('/books/add', methods=['POST'])
def add_book():
    data = request.get_json() or {}
    title = data.get("title")
    author = data.get("author")
    published_date = data.get("published_date")
    if not title or not author:
        return jsonify({"error": "Missing title or author"}), 400
    try:
        date = None
        if published_date:
            if isinstance(published_date, str):
                date = datetime.strptime(published_date, '%Y-%m-%d').date()
            else:
                date = published_date
        new_book = Book(title=title, author=author, published_date=date)
        db.session.add(new_book)
        db.session.commit()
        return jsonify({"message": "Book added", "id": new_book.id}), 201
    except ValueError:
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400
