# TÀI LIỆU THIẾT KẾ CƠ SỞ DỮ LIỆU
## Hệ thống Giám sát Tài xế sử dụng Computer Vision & AI

---

**Tên dự án:** Hệ thống Giám sát Tài xế (DMS)  
**Loại tài liệu:** Thiết kế Cơ sở dữ liệu  
**Phiên bản:** 1.0  
**Tác giả:** Hùng Thanh  
**Ngày:** 04 tháng 3, 2026  
**Trạng thái:** Bản thảo cuối cùng

---

## MỤC LỤC

1. [Giới thiệu](#1-giới-thiệu)
2. [Tổng quan Cơ sở dữ liệu](#2-tổng-quan-cơ-sở-dữ-liệu)
3. [Sơ đồ Quan hệ Thực thể (ERD)](#3-sơ-đồ-quan-hệ-thực-thể)
4. [Sơ đồ Cơ sở dữ liệu (Schema)](#4-sơ-đồ-cơ-sở-dữ-liệu)
5. [Đặc tả các Bảng](#5-đặc-tả-các-bảng)
6. [Chỉ mục & Tối ưu hóa](#6-chỉ-mục--tối-ưu-hóa)
7. [Chính sách Lưu trữ Dữ liệu](#7-chính-sách-lưu-trữ-dữ-liệu)
8. [Bảo mật Cơ sở dữ liệu](#8-bảo-mật-cơ-sở-dữ-liệu)

---

## 1. GIỚI THIỆU

### 1.1 Mục đích
Tài liệu này mô tả thiết kế cơ sở dữ liệu hoàn chỉnh cho Hệ thống Giám sát Tài xế (DMS). Nó cung cấp các đặc tả chi tiết về lưu trữ dữ liệu, bao gồm định nghĩa schema, mối quan hệ, chỉ mục và các chính sách quản lý dữ liệu để hỗ trợ triển khai đồ án tốt nghiệp.

### 1.2 Phạm vi
Thiết kế này bao gồm:
- Schema cho tất cả các thực thể hệ thống.
- Cấu trúc bảng với các cột, kiểu dữ liệu và ràng buộc.
- Mối quan hệ giữa các thực thể (khóa ngoại).
- Các truy vấn SQL mẫu cho các hoạt động phổ biến.
- Quy trình sao lưu và phục hồi.

---

## 2. TỔNG QUAN CƠ SỞ DỮ LIỆU

### 2.1 Lựa chọn Công nghệ
**Hệ quản trị CSDL: SQLite 3.x**

**Lý do chọn:**
- **Nhúng (Embedded)**: Không cần tiến trình server riêng biệt.
- **Dựa trên tệp tin**: Toàn bộ database nằm trong một file duy nhất, dễ dàng sao lưu và di chuyển.
- **Cấu hình bằng không**: Không cần cài đặt hay quản trị phức tạp.
- **Hiệu năng đủ dùng**: Xử lý tốt hàng ngàn sự kiện mỗi ngày.
- **Tích hợp Python**: Hỗ trợ sẵn qua module `sqlite3`.

---

## 3. CÁC THỰC THỂ CỐT LÕI

Cơ sở dữ liệu bao gồm **8 thực thể chính**:

1. **drivers**: Hồ sơ tài xế và dữ liệu xác thực khuôn mặt.
2. **trips**: Các chuyến đi với thời gian bắt đầu/kết thúc.
3. **events**: Các sự kiện rủi ro được phát hiện (buồn ngủ, xao nhãng, hành vi).
4. **drowsiness_details**: Chi tiết các chỉ số buồn ngủ theo từng sự kiện.
5. **distraction_details**: Chi tiết các chỉ số xao nhãng theo từng sự kiện.
6. **activity_details**: Dữ liệu nhận diện hành vi nguy hiểm.
7. **system_health**: Các chỉ số hiệu năng và sức khỏe hệ thống.
8. **configuration**: Các thiết lập cấu hình và ngưỡng (thresholds).

---

## 4. SCHEMA CHI TIẾT (TRÍCH DẪN)

Hệ thống sử dụng các ràng buộc khóa ngoại (Foreign Keys) để đảm bảo tính toàn vẹn dữ liệu:
- Một **Tài xế (Driver)** có nhiều **Chuyến đi (Trip)**.
- Một **Chuyến đi (Trip)** có nhiều **Sự kiện (Event)**.
- Mỗi **Sự kiện (Event)** có thông tin chi tiết tương ứng (1:1) trong các bảng details tùy theo loại sự kiện.

---

## 5. CHÍNH SÁCH LƯU TRỮ

- **Chuyến đi và Sự kiện**: Lưu trữ trong 30 ngày, sau đó lưu trữ (archived) vào file dự phòng và xóa khỏi DB chính.
- **Ảnh chụp sự kiện (Snapshots)**: Lưu trữ trong 7 ngày để tiết kiệm dung lượng đĩa.
- **Log hệ thống**: Lưu trữ trong 7 ngày.

---

## 6. BẢO MẬT

- **Quyền truy cập tệp**: File database chỉ có quyền đọc/ghi bởi người dùng chạy tiến trình DMS.
- **Phòng chống SQL Injection**: Sử dụng các truy vấn có tham số (parameterized queries).
- **Sao lưu**: Tự động sao lưu hàng ngày vào lúc 2:00 AM.

---
*Ghi chú: Đây là bản tóm tắt thiết kế cơ sở dữ liệu bằng tiếng Việt. Chi tiết về code SQL và các hàm tiện ích cụ thể có thể tham khảo trong bản tiếng Anh.*
