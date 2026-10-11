
BOOKS = {}
_NEXT_BOOK_ID = 1


def _build_book(book_id, data):
    return {
        "id": book_id,
        "title": data["title"].strip(),
        "author": data["author"].strip(),
        "published_year": data["published_year"],
    }


def list_books():
    """Trả về danh sách sách được sắp xếp theo ID."""
    return [BOOKS[key].copy() for key in sorted(BOOKS)]


def get_book(book_id):
    """Trả về sách theo ID, hoặc None nếu không tìm thấy."""
    book = BOOKS.get(book_id)
    return book.copy() if book else None


def create_book(data):
    """Tạo sách mới và để máy chủ tự cấp ID."""
    global _NEXT_BOOK_ID

    book = _build_book(_NEXT_BOOK_ID, data)
    BOOKS[_NEXT_BOOK_ID] = book
    _NEXT_BOOK_ID += 1
    return book.copy()


def update_book(book_id, data):
    """Thay thế các trường có thể chỉnh sửa của sách."""
    if book_id not in BOOKS:
        return None

    BOOKS[book_id] = _build_book(book_id, data)
    return BOOKS[book_id].copy()


def delete_book(book_id):
    """Xóa sách và trả về True nếu sách tồn tại."""
    return BOOKS.pop(book_id, None) is not None


def reset_books():
    """Đặt lại dữ liệu sách trong bộ nhớ, chỉ dùng cho kiểm thử."""
    global _NEXT_BOOK_ID
    BOOKS.clear()
    _NEXT_BOOK_ID = 1


# DỊCH VỤ TÁC GIẢ
AUTHORS = {}
_NEXT_AUTHOR_ID = 1


def _build_author(author_id, data):
    return {
        "id": author_id,
        "name": data["name"].strip(),
        "bio": (data.get("bio") or "").strip(),
    }


def list_authors():
    """Trả về danh sách tác giả được sắp xếp theo ID."""
    return [AUTHORS[key].copy() for key in sorted(AUTHORS)]


def get_author(author_id):
    """Trả về tác giả theo ID, hoặc None nếu không tìm thấy."""
    author = AUTHORS.get(author_id)
    return author.copy() if author else None


def create_author(data):
    """Tạo tác giả mới và để máy chủ tự cấp ID."""
    global _NEXT_AUTHOR_ID

    author = _build_author(_NEXT_AUTHOR_ID, data)
    AUTHORS[_NEXT_AUTHOR_ID] = author
    _NEXT_AUTHOR_ID += 1
    return author.copy()


def update_author(author_id, data):
    """Thay thế các trường có thể chỉnh sửa của tác giả."""
    if author_id not in AUTHORS:
        return None

    AUTHORS[author_id] = _build_author(author_id, data)
    return AUTHORS[author_id].copy()


def delete_author(author_id):
    """Xóa tác giả và trả về True nếu tác giả tồn tại."""
    return AUTHORS.pop(author_id, None) is not None


def reset_authors():
    """Đặt lại dữ liệu tác giả trong bộ nhớ, chỉ dùng cho kiểm thử."""
    global _NEXT_AUTHOR_ID
    AUTHORS.clear()
    _NEXT_AUTHOR_ID = 1


# DỊCH VỤ PHIẾU MƯỢN
BORROWS = {}
_NEXT_BORROW_ID = 1


def _build_borrow(borrow_id, data):
    return {
        "id": borrow_id,
        "book_id": data["book_id"],
        "borrower": data["borrower"].strip(),
        "status": (data.get("status") or "borrowed").strip(),
        "borrow_date": data.get("borrow_date"),
    }


def list_borrows():
    """Trả về danh sách phiếu mượn được sắp xếp theo ID."""
    return [BORROWS[key].copy() for key in sorted(BORROWS)]


def get_borrow(borrow_id):
    """Trả về phiếu mượn theo ID, hoặc None nếu không tìm thấy."""
    borrow = BORROWS.get(borrow_id)
    return borrow.copy() if borrow else None


def create_borrow(data):
    """Tạo phiếu mượn mới và để máy chủ tự cấp ID."""
    global _NEXT_BORROW_ID

    borrow = _build_borrow(_NEXT_BORROW_ID, data)
    BORROWS[_NEXT_BORROW_ID] = borrow
    _NEXT_BORROW_ID += 1
    return borrow.copy()


def update_borrow(borrow_id, data):
    """Thay thế các trường có thể chỉnh sửa của phiếu mượn."""
    if borrow_id not in BORROWS:
        return None

    BORROWS[borrow_id] = _build_borrow(borrow_id, data)
    return BORROWS[borrow_id].copy()


def delete_borrow(borrow_id):
    """Xóa phiếu mượn và trả về True nếu phiếu tồn tại."""
    return BORROWS.pop(borrow_id, None) is not None


def reset_borrows():
    """Đặt lại dữ liệu phiếu mượn trong bộ nhớ, chỉ dùng cho kiểm thử."""
    global _NEXT_BORROW_ID
    BORROWS.clear()
    _NEXT_BORROW_ID = 1


# ĐẶT LẠI TOÀN BỘ DỮ LIỆU
def reset_all():
    """Đặt lại toàn bộ dữ liệu trong bộ nhớ của mọi loại đối tượng."""
    reset_books()
    reset_authors()
    reset_borrows()