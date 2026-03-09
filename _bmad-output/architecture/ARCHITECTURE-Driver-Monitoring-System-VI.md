# TÀI LIỆU THIẾT KẾ KIẾN TRÚC
## Hệ thống Giám sát Tài xế sử dụng Computer Vision & AI

---

**Tên dự án:** Hệ thống Giám sát Tài xế (DMS)  
**Loại tài liệu:** Thiết kế Kiến trúc Hệ thống  
**Phiên bản:** 1.0  
**Tác giả:** Hùng Thanh  
**Ngày:** 04 tháng 3, 2026  
**Trạng thái:** Bản thảo cuối cùng

---

## MỤC LỤC

1. [Giới thiệu](#1-giới-thiệu)
2. [Tổng quan Kiến trúc](#2-tổng-quan-kiến-trúc)
3. [Bối cảnh & Ranh giới Hệ thống](#3-bối-cảnh--ranh-giới-hệ-thống)
4. [Góc nhìn Thành phần](#4-góc-nhìn-thành-phần)
5. [Góc nhìn Triển khai](#5-góc-nhìn-triển-khai)
6. [Góc nhìn Luồng dữ liệu](#6-góc-nhìn-luồng-dữ-liệu)
7. [Góc nhìn Quy trình](#7-góc-nhìn-quy-trình)
8. [Kiến trúc Vật lý](#8-kiến-trúc-vật-lý)
9. [Stack Công nghệ](#9-stack-công-nghệ)
10. [Thiết kế Chi tiết Thành phần](#10-thiết-kế-chi-tiết-thành-phần)

---

## 1. GIỚI THIỆU

### 1.1 Mục đích

Tài liệu này mô tả kiến trúc phần mềm hoàn chỉnh cho Hệ thống Giám sát Tài xế (DMS). Nó cung cấp cái nhìn toàn diện về cấu trúc hệ thống, các thành phần, giao diện, luồng dữ liệu và mô hình triển khai để hướng dẫn thực hiện và làm tài liệu tham khảo cho dự án đồ án tốt nghiệp.

### 1.2 Phạm vi

Kiến trúc này bao gồm:
- Các thành phần hệ thống và tương tác của chúng
- Mô hình triển khai phần cứng và phần mềm
- Các đường ống xử lý dữ liệu và thuật toán
- Stack công nghệ và các framework
- Thông số giao diện giữa các thành phần
- Sơ đồ cơ sở dữ liệu và quản lý dữ liệu
- Các cân nhắc về bảo mật và hiệu năng

### 1.3 Đối tượng mục tiêu

- **Sinh viên phát triển (Hùng Thanh)**: Tham khảo để triển khai
- **Giảng viên hướng dẫn**: Đánh giá kỹ thuật và hướng dẫn
- **Hội đồng chấm đồ án**: Đánh giá thiết kế hệ thống
- **Người bảo trì tương lai**: Hiểu và sửa đổi hệ thống

### 1.4 Mục tiêu Kiến trúc

| Mục tiêu | Mô tả | Ưu tiên |
|------|-------------|----------|
| **Hiệu năng thời gian thực** | Xử lý video ≥15 FPS với độ trễ cảnh báo <200ms | BẮT BUỘC |
| **Tính mô-đun** | Các thành phần độc lập, ít phụ thuộc để dễ bảo trì | BẮT BUỘC |
| **Độ chính xác** | ≥90% phát hiện buồn ngủ, ≥85% nhận diện hành vi | BẮT BUỘC |
| **Khả năng mở rộng** | Dễ dàng thêm các tính năng phát hiện mới | NÊN CÓ |
| **Hiệu quả tài nguyên** | Chạy trên thiết bị biên (Jetson Nano / RPi 4) | BẮT BUỘC |
| **Độ tin cậy** | Duy trì hoạt động ổn định khi các thành phần gặp lỗi | NÊN CÓ |

---

## 2. TỔNG QUAN KIẾN TRÚC

### 2.1 Phong cách Kiến trúc

**Mẫu chính:** **Kiến trúc Đường ống (Pipeline Architecture)**

Hệ thống tuân theo kiến trúc đường ống tuyến tính, nơi các khung hình video chạy qua các giai đoạn xử lý tuần tự:

```
Đầu vào Video → Giai đoạn Phát hiện → Giai đoạn Phân tích → Giai đoạn Hành động → Đầu ra
```

**Lý do chọn:**
- Phù hợp tự nhiên với quy trình xử lý video
- Chuyển đổi dữ liệu rõ ràng tại mỗi giai đoạn
- Dễ dàng tối ưu hóa từng giai đoạn riêng lẻ
- Đơn giản để hiểu và bảo trì
- Rất phù hợp cho dữ liệu phát trực tuyến thời gian thực

**Mẫu phụ:**
- **Kiến trúc phân lớp (Layered Architecture)**: Chia thành các lớp Phát hiện, Phân tích, Hành động
- **Mẫu Repository**: Lưu trữ dữ liệu tập trung (Cơ sở dữ liệu SQLite)
- **Mẫu Observer**: Thông báo cho người đăng ký cảnh báo khi có sự kiện xảy ra

### 2.2 Sơ đồ Kiến trúc cấp cao

Hệ thống được chia thành 4 lớp chính:
1. **Lớp Đầu vào**: Chụp và tiền xử lý khung hình video từ camera hồng ngoại (IR).
2. **Lớp Phát hiện**: Trích xuất các đặc trưng (landmarks khuôn mặt, trạng thái mắt, tư thế đầu) bằng Computer Vision.
3. **Lớp Phân tích**: Diễn giải các đặc trưng để đánh giá trạng thái tài xế (buồn ngủ, xao nhãng).
4. **Lớp Hành động**: Tạo cảnh báo và ghi lại các sự kiện vào cơ sở dữ liệu.

---

## 3. BỐI CẢNH & RANH GIỚI HỆ THỐNG

### 3.1 Ranh giới Hệ thống

**Bên trong Hệ thống (Trách nhiệm):**
- Chụp video và xử lý hình ảnh
- Phát hiện khuôn mặt, mắt và hành vi
- Phân tích trạng thái tài xế (buồn ngủ, xao nhãng)
- Tạo và gửi cảnh báo
- Ghi log sự kiện và lưu trữ dữ liệu
- Theo dõi sức khỏe hệ thống

**Bên ngoài Hệ thống (Không bao gồm):**
- Các hệ thống điều khiển xe (phanh, lái)
- Kết nối Internet / dịch vụ đám mây
- Các hệ thống hỗ trợ lái xe nâng cao (ADAS)
- Tích hợp hệ thống thông tin giải trí trong xe

---

## 4. GÓC NHÌN THÀNH PHẦN

Hệ thống bao gồm các hệ thống con (Subsystems) sau:
- **Hệ thống con Đầu vào**: Chụp video và tiền xử lý.
- **Hệ thống con Phát hiện**: Bao gồm các bộ phát hiện khuôn mặt, mắt, tư thế đầu, hướng nhìn, miệng, tay và hành vi.
- **Hệ thống con Phân tích**: Phân tích buồn ngủ, xao nhãng và đánh giá rủi ro.
- **Hệ thống con Hành động**: Quản lý cảnh báo, ghi log và tạo báo cáo.
- **Hệ thống con Lưu trữ**: Quản lý cơ sở dữ liệu và lưu trữ tệp tin.

---

## 5. KIẾN TRÚC VẬT LÝ VÀ TRIỂN KHAI

### 5.1 Phần cứng đề xuất
- **Thiết bị chính**: NVIDIA Jetson Nano 4GB (Khuyến nghị do có GPU hỗ trợ tăng tốc AI).
- **Camera**: Camera hồng ngoại (IR) kết nối USB để hoạt động tốt trong mọi điều kiện ánh sáng.
- **Cảnh báo**: Loa (âm thanh) và đèn LED (thị giác).

### 5.2 Phần mềm
- **Hệ điều hành**: Ubuntu 20.04 LTS hoặc Raspberry Pi OS.
- **Ngôn ngữ**: Python 3.8.
- **Thư viện chính**: OpenCV, dlib, TensorFlow Lite, NumPy, SQLite.

---

## 6. LỘ TRÌNH VÀ CHIẾN LƯỢC TRIỂN KHAI

Hệ thống sẽ được triển khai theo mô hình đường ống xử lý video với mục tiêu đạt được:
- Độ trễ dưới 200ms cho các cảnh báo quan trọng.
- Hoạt động ổn định trên các thiết bị nhúng có tài nguyên hạn chế.
- Khả năng xử lý 24/7 với camera hồng ngoại.

---
*Ghi chú: Đây là bản tóm tắt kiến trúc hệ thống bằng tiếng Việt. Chi tiết kỹ thuật về các hàm và thuật toán cụ thể có thể tham khảo trong bản tiếng Anh.*
