from index.models import Book


class Books:
    def __init__(self, id, count):
        cur = Book.objects.filter(id=id)[0]
        self.id = id
        self.count = count
        self.name = cur.name
        self.price = cur.current_price
        self.pic = cur.pics
        self.publisher = cur.publisher

    @property
    def getTolPrice(self):
        return float(self.price) * float(self.count)


class Cart:
    def __init__(self):
        self.book_list = []

    def add(self, id, count=1):
        book = self.getBook(id)
        if book:
            book.count += count
            return 1
        else:
            nbook = Books(id, count)
            self.book_list.append(nbook)
            return 2

    def removeBook(self, id):
        book = self.getBook(id)
        if book: self.book_list.remove(book)

    def getBook(self, id):
        for book in self.book_list:
            if book.id == id:
                return book
        return None

    def __len__(self):
        return len(self.book_list)