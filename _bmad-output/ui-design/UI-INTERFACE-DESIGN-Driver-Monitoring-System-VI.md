# TÀI LIỆU THIẾT KẾ GIAO DIỆN NGƯỜI DÙNG (UI/UX)
## Hệ thống Giám sát Tài xế sử dụng Computer Vision & AI

---

**Tên dự án:** Hệ thống Giám sát Tài xế (DMS)  
**Loại tài liệu:** Thiết kế Giao diện / UI Design  
**Phiên bản:** 1.0  
**Tác giả:** Hùng Thanh  
**Ngày:** 05 tháng 3, 2026  
**Trạng thái:** Bản thảo cuối cùng

---

## MỤC LỤC

1. [Giới thiệu](#1-giới-thiệu)
2. [Tổng quan Thiết kế](#2-tổng-quan-thiết-kế)
3. [Các Chế độ Giao diện](#3-các-chế-độ-giao diện)
4. [Các Thành phần Giao diện chính](#4-các-thành-phần-giao-diện-chính)
5. [Thiết kế các Màn hình](#5-thiết-kế-các-màn-hình)
6. [Hệ thống Cảnh báo (Alert System)](#6-hệ-thống-cảnh-báo)
7. [Hệ thống Thiết kế Hình ảnh (Visual Design)](#7-hệ-thống-thiết-kế-hình-ảnh)

---

## 1. GIỚI THIỆU

### 1.1 Mục đích
Tài liệu này mô tả thiết kế Giao diện người dùng (UI) hoàn chỉnh cho Hệ thống Giám sát Tài xế (DMS). Nó cung cấp các đặc tả chi tiết cho tất cả các màn hình, thành phần, thiết kế hình ảnh, tương tác người dùng và hướng dẫn triển khai để đảm bảo giao diện nhất quán, dễ sử dụng cho đồ án tốt nghiệp.

### 1.2 Mục tiêu Thiết kế
- **Sự rõ ràng**: Thông tin được trình bày rõ ràng, không gây rối mắt.
- **Phản hồi thời gian thực**: Phản hồi hình ảnh tức thì về trạng thái tài xế.
- **Giảm thiểu xao nhãng**: Giao diện không được gây mất tập trung cho tài xế khi đang lái xe.
- **Tính trực quan**: Dễ dàng tìm thấy các cài đặt và xem báo cáo.

---

## 2. TỔNG QUAN THIẾT KẾ

### 2.1 Các Loại Giao diện
Hệ thống DMS có **3 chế độ giao diện chính**:

1.  **Màn hình trong xe (Giao diện chính)**: Giám sát thời gian thực khi đang lái xe (Màn hình 7-10 inch gắn trên táp-lô).
2.  **Giao diện Cấu hình (Giao diện phụ)**: Thiết lập hệ thống, đăng ký tài xế (Chỉ hoạt động khi xe đang đỗ).
3.  **Dashboard Web (Mở rộng tương lai)**: Phân tích dữ liệu lịch sử và báo cáo trên trình duyệt.

### 2.2 Stack Công nghệ UI
- **Framework**: PyQt5 (Ưu tiên do hiệu năng tốt trên Jetson Nano/Raspberry Pi).
- **Đồ họa**: OpenCV để hiển thị luồng video thời gian thực.
- **Âm thanh**: Thư viện `pygame` để phát âm thanh cảnh báo.
- **Phần cứng**: Đèn LED điều khiển qua GPIO.

---

## 3. THIẾT KẾ CÁC MÀN HÌNH CHÍNH

### 3.1 Màn hình Giám sát Thời gian thực (Live Monitoring)
- **Bên trái (70%)**: Hiển thị video trực tiếp từ camera IR với các lớp phủ (overlays) nhận diện khuôn mặt, mắt.
- **Bên phải (30%)**: Bảng trạng thái hiển thị các chỉ số EAR (độ mở mắt), Drowsiness (mức buồn ngủ) và Attention (mức tập trung).
- **Phía trên (Header)**: Tên tài xế, thời gian và menu.
- **Phía dưới (Footer)**: Thời gian chuyến đi, số sự kiện vi phạm và nút kết thúc hành trình.

### 3.2 Hệ thống Cảnh báo (Alert Overlay)
Khi phát hiện rủi ro, một banner thông báo sẽ đè lên màn hình chính:
- **Cảnh báo Nghiêm trọng (Đỏ)**: Buồn ngủ (Microsleep), hành vi cực kỳ nguy hiểm. Kèm âm thanh bíp liên tục và đèn LED đỏ nháy nhanh.
- **Cảnh báo Trung bình (Vàng)**: Xao nhãng, ngáp kéo dài. Kèm âm thanh bíp đơn và đèn LED vàng nháy.

---

## 4. QUY TRÌNH NGƯỜI DÙNG (USER FLOW)

1.  **Khởi hành**: Tài xế lên xe -> Hệ thống nhận diện khuôn mặt -> Hiển thị lời chào -> Bắt đầu giám sát.
2.  **Xử lý cảnh báo**: Hệ thống phát hiện rủi ro -> Hiển thị thông báo đè -> Phát âm thanh/đèn LED -> Ghi log vào DB -> Tự đóng khi tài xế tỉnh táo trở lại.
3.  **Kết thúc**: Tài xế bấm "Kết thúc" -> Hiển thị màn hình Tóm tắt chuyến đi (Trip Summary) với các chỉ số đánh giá sao (1-5 sao).

---

## 5. HỆ THỐNG THIẾT KẾ (VISUAL DESIGN)

- **Màu sắc**:
  - Nền tối (#2C3E50) để giảm chói mắt ban đêm.
  - Màu nhấn xanh Teal (#1ABC9C) cho các nút bấm.
  - Màu cảnh báo: Đỏ (#E74C3C), Vàng (#F39C12), Xanh lá (#27AE60).
- **Phông chữ**: Roboto hoặc Arial (không chân), kích thước tối thiểu 14px để dễ đọc ở khoảng cách một cánh tay.

---
*Ghi chú: Đây là bản tóm tắt thiết kế giao diện bằng tiếng Việt. Chi tiết về các lớp PyQt5 và mã nguồn cụ thể có thể tham khảo trong bản tiếng Anh.*
