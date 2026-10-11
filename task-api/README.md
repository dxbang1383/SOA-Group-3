# Task API - Book Management

## 1. Giới thiệu

Bài tập xây dựng API quản lý sách, tác giả và phiếu mượn bằng **OpenAPI YAML** và Flask. Backend hiện là bản mẫu, dữ liệu lưu trong bộ nhớ.

## 2. Mục tiêu

- Thiết kế API theo các nguyên tắc REST.
- Mô tả endpoint, HTTP method, request và response.
- Tái sử dụng schema thông qua `$ref`.
- Kiểm tra tính hợp lệ của đặc tả OpenAPI.
- Triển khai và kiểm thử API sau khi hoàn thiện đặc tả.

## 3. Cấu trúc thư mục

| File/thư mục | Ý nghĩa |
|---|---|
| `openapi.yaml` | Entry point và nguồn OpenAPI modular; sửa file này để thêm metadata hoặc khai báo tham chiếu. |
| `paths/` | Định nghĩa endpoint theo tài nguyên: books, authors và borrows. |
| `components/` | Schemas, parameters, request bodies và responses dùng chung. |
| `bundled-openapi.yaml` | Bản tự chứa được sinh từ `openapi.yaml`; không sửa trực tiếp. |
| `app/__init__.py` | Tạo Flask application và đăng ký routes. |
| `app/routes.py` | Khai báo endpoint và xử lý HTTP request/response. |
| `app/schemas.py` | Các hàm kiểm tra dữ liệu đầu vào ở phía Python; không tự sinh từ OpenAPI. |
| `app/services.py` | Xử lý nghiệp vụ quản lý sách, tách khỏi phần HTTP. |
| `tests/test_books.py` | Kiểm thử các endpoint bằng Flask test client. |
| `requirements.txt` | Danh sách thư viện Python cần cài. |

## 4. Các API

| Method | Endpoint | Chức năng |
|---|---|---|
| `GET` | `/books`, `/authors`, `/borrows` | Lấy danh sách theo tài nguyên. |
| `POST` | `/books`, `/authors`, `/borrows` | Tạo sách, tác giả hoặc phiếu mượn. |
| `GET` | `/books/{id}`, `/authors/{author_id}`, `/borrows/{borrow_id}` | Lấy một bản ghi theo ID. |
| `PUT` | Các endpoint theo ID ở trên | Thay thế thông tin bản ghi. |
| `DELETE` | Các endpoint theo ID ở trên | Xóa bản ghi. |

## 5. Schema dùng chung

Các schema được định nghĩa trong `components/schemas.yaml` và được tham chiếu từ `openapi.yaml`:

- `Book`: sách đầy đủ, bao gồm `id`.
- `BookCreate`: dữ liệu tạo sách, không cần `id` do server cấp.
- `BookUpdate`: dữ liệu cập nhật; trong mẫu này yêu cầu đủ các trường có thể sửa theo ngữ nghĩa PUT.
- `Author` / `AuthorWrite`: thông tin tác giả.
- `Borrow` / `BorrowWrite`: thông tin phiếu mượn.
- `Error`: cấu trúc phản hồi lỗi.

Các file trong `paths/` tham chiếu đến schema và response dùng chung bằng `$ref` tương đối. Redocly sẽ gom các tham chiếu này thành một tài liệu duy nhất.

> `$ref` tái sử dụng định nghĩa trong tài liệu OpenAPI; nó không tự động sinh hay tái sử dụng mã Python. Nếu cần sinh code, phải dùng công cụ code generation riêng.

## 6. Tạo bản bundle

Từ thư mục `task-api/`, tạo hoặc cập nhật bản bundle bằng:

```bash
npx --yes @redocly/cli bundle openapi.yaml --output bundled-openapi.yaml
```

Sửa các file nguồn (`openapi.yaml`, `paths/`, `components/`), sau đó chạy lại lệnh trên. Dùng `bundled-openapi.yaml` khi cần đưa một file duy nhất vào Swagger UI hoặc code generator.

## 7. Công nghệ

- OpenAPI 3.0.3 / YAML: mô tả API.
- Flask: triển khai backend.
- pytest: kiểm thử tự động.
- Swagger UI hoặc trình soạn thảo OpenAPI tương thích: xem và thử đặc tả.

## 8. Chạy dự án

Từ thư mục `task-api/`:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\\Scripts\\Activate.ps1
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Cài thư viện và chạy:

```bash
pip install -r requirements.txt
python -m flask --app app run --debug
```

Mặc định API chạy tại `http://127.0.0.1:5000`.

## 9. Kiểm thử

Khi môi trường ảo đã được kích hoạt:

```bash
pytest
```

Dữ liệu sách hiện được lưu trong bộ nhớ; khởi động lại server sẽ đặt dữ liệu về ban đầu. Đây là bản mẫu học tập, chưa dùng cơ sở dữ liệu.
