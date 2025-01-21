from flask import Flask, render_template, request

app = Flask(__name__)

searchbook =[]

books = [
{"id": 1, "title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling", "year": 1997},
{"id": 2, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
{"id": 3, "title": "1984", "author": "George Orwell", "year": 1949},
{"id": 4, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
{"id": 5, "title": "A Promised Land", "author": "Barack Obama", "year": 2020}]


@app.route('/', methods=["GET","POST"])
def index():
    return render_template("index.html")


@app.route('/addbook', methods=['POST'])
def add():
    id = len(books)+1
    title = request.form.get('title')
    author = request.form.get('author')
    year = request.form.get('year')
    books.append({"id": id, "title": title, "author": author, "year": year})

    return books


@app.route('/api/v2/search', methods=["GET"])
def search():
    author = request.args.get('author')
    for livre in books:
        if livre["author"] == author:
            searchbook.append(livre)
    return searchbook

if __name__ == '__main__':
    app.run(port=5050)