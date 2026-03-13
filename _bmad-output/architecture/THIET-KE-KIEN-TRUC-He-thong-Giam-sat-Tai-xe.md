# TÀI LIỆU THIẾT KẾ KIẾN TRÚC
## Hệ thống Giám sát Tài xế sử dụng Thị giác máy tính & AI

---

**Tên dự án:** Hệ thống Giám sát Tài xế (Driver Monitoring System - DMS)  
**Loại tài liệu:** Thiết kế kiến trúc hệ thống  
**Phiên bản:** 1.0  
**Tác giả:** Hùng Thành  
**Ngày:** 04/03/2026  
**Trạng thái:** Bản thảo cuối cùng

---

## MỤC LỤC

1. [Giới thiệu](#1-giới-thiệu)
2. [Tổng quan kiến trúc](#2-tổng-quan-kiến-trúc)
3. [Ngữ cảnh & Phạm vi hệ thống](#3-ngữ-cảnh--phạm-vi-hệ-thống)
4. [Các thành phần hệ thống](#4-các-thành-phần-hệ-thống)
5. [Triển khai hệ thống](#5-triển-khai-hệ-thống)
6. [Luồng dữ liệu](#6-luồng-dữ-liệu)
7. [Quy trình xử lý](#7-quy- trình-xử-lý)
8. [Kiến trúc vật lý](#8-kiến-trúc-vật-lý)
9. [Danh mục công nghệ](#9-danh-mục-công-nghệ)
10. [Thiết kế chi tiết thành phần](#10-thiết-kế-chi-tiết-thành-phần)
11. [Đặc tả giao diện](#11-đặc-tả-giao-diện)
12. [Kiến trúc dữ liệu](#12-kiến-trúc-dữ-liệu)
13. [Kiến trúc bảo mật](#13-kiến-trúc-bảo-mật)
14. [Kiến trúc hiệu năng](#14-kiến-trúc-hiệu-năng)
15. [Triển khai & Cấu hình](#15-triển-khai--cấu-hình)

---

## 1. GIỚI THIỆU

### 1.1 Mục đích

Tài liệu này mô tả kiến trúc phần mềm hoàn chỉnh cho Hệ thống Giám sát Tài xế (DMS). Nó cung cấp cái nhìn toàn diện về cấu trúc hệ thống, các thành phần, giao diện, luồng dữ liệu và mô hình triển khai để hướng dẫn việc thực hiện và đóng vai trò là tài liệu tham khảo cho đồ án tốt nghiệp đại học.

### 1.2 Phạm vi

Kiến trúc này bao gồm:
- Các thành phần hệ thống và sự tương tác giữa chúng
- Cấu trúc triển khai phần cứng và phần mềm
- Các đường dẫn xử lý dữ liệu (pipelines) và thuật toán
- Danh mục công nghệ và các frameworks sử dụng
- Đặc tả giao diện giữa các thành phần
- Lược đồ cơ sở dữ liệu và quản lý dữ liệu
- Các cân nhắc về bảo mật và hiệu năng

### 1.3 Đối tượng hướng tới

- **Sinh viên phát triển (Hùng Thành)**: Tài liệu tham khảo triển khai
- **Giảng viên hướng dẫn**: Xem xét kỹ thuật và hướng dẫn
- **Hội đồng chấm đồ án**: Đánh giá thiết kế hệ thống
- **Người bảo trì trong tương lai**: Hiểu và sửa đổi hệ thống

### 1.4 Mục tiêu kiến trúc

| Mục tiêu | Mô tả | Độ ưu tiên |
|------|-------------|----------|
| **Hiệu năng thời gian thực** | Xử lý video ở mức ≥15 FPS với độ trễ cảnh báo <200ms | BẮT BUỘC |
| **Tính mô-đun** | Các thành phần độc lập, ít phụ thuộc để dễ bảo trì | BẮT BUỘC |
| **Độ chính xác** | Phát hiện buồn ngủ ≥90%, nhận diện hoạt động ≥85% | BẮT BUỘC |
| **Khả năng mở rộng** | Dễ dàng thêm các tính năng phát hiện mới | NÊN CÓ |
| **Hiệu quả tài nguyên** | Chạy trên thiết bị nhúng (Jetson Nano / RPi 4) | BẮT BUỘC |
| **Độ tin cậy** | Duy trì hoạt động ổn định khi các thành phần phụ gặp lỗi | NÊN CÓ |

### 1.5 Nguyên tắc kiến trúc

1. **Tách biệt các mối quan tâm (Separation of Concerns)**: Các lớp Phát hiện (Detection), Phân tích (Analysis) và Hành động (Action) hoạt động độc lập.
2. **Trách nhiệm đơn nhất (Single Responsibility)**: Mỗi thành phần có một chức năng chính duy nhất.
3. **Mô hình đường dẫn (Pipeline Pattern)**: Các giai đoạn xử lý tuần tự với các ràng buộc dữ liệu rõ ràng.
4. **Cảnh báo dựa trên sự kiện (Event-Driven Alerts)**: Tạo cảnh báo không đồng bộ dựa trên kết quả phân tích.
5. **Cấu hình thay vì mã hóa (Configuration over Code)**: Các ngưỡng và tham số được lưu trong tệp cấu hình.
6. **Thiết kế an toàn (Fail-Safe Design)**: Hệ thống tiếp tục hoạt động ngay cả khi các thành phần không trọng yếu gặp lỗi.

---

## 2. TỔNG QUAN KIẾN TRÚC

### 2.1 Phong cách kiến trúc

**Mô hình chính:** **Kiến trúc đường dẫn (Pipeline Architecture)** (Pipes and Filters)

Hệ thống tuân theo một **kiến trúc đường dẫn tuyến tính**, nơi các khung hình video chạy qua các giai đoạn xử lý tuần tự:

```
Đầu vào video → Giai đoạn phát hiện → Giai đoạn phân tích → Giai đoạn hành động → Đầu ra
```

**Lý do lựa chọn:**
- Phù hợp tự nhiên với quy trình xử lý video.
- Chuyển đổi dữ liệu rõ ràng ở mỗi giai đoạn.
- Dễ dàng tối ưu hóa từng giai đoạn riêng lẻ.
- Đơn giản để hiểu và bảo trì.
- Rất phù hợp cho dữ liệu truyền tải theo thời gian thực.

**Các mô hình phụ trợ:**
- **Kiến trúc phân lớp (Layered Architecture)**: Chia thành các lớp Phát hiện, Phân tích, Hành động.
- **Mô hình Repository**: Lưu trữ dữ liệu tập trung (Cơ sở dữ liệu SQLite).
- **Mô hình Observer**: Các thành phần đăng ký nhận thông báo cảnh báo khi sự kiện xảy ra.

### 2.2 Sơ đồ kiến trúc mức cao

```
┌─────────────────────────────────────────────────────────────────────┐
│                        HỆ THỐNG GIÁM SÁT TÀI XẾ                      │
├─────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  ┌────────────┐         ┌─────────────────────────────────────┐    │
│  │ Camera Hồng  │────────▶│       LỚP ĐẦU VÀO                    │    │
│  │ ngoại (Video)│         │  - Thu nhận khung hình (OpenCV)      │    │
│  └────────────┘         │  - Tiền xử lý hình ảnh IR            │    │
│                         └──────────────┬──────────────────────┘    │
│                                        │                             │
│                                        ▼                             │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │              LỚP PHÁT HIỆN (Thị giác máy tính)               │   │
│  ├─────────────────────────────────────────────────────────────┤   │
│  │ ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │   │
│  │ │   Phát hiện  │  │   Theo dõi   │  │   Ước tính   │      │   │
│  │ │    khuôn mặt │  │    mắt       │  │   tư thế đầu │      │   │
│  └──────────────┘  └──────────────┘  └──────────────┘      │   │
│  │                                                               │   │
│  │ ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │   │
│  │ │   Theo dõi   │  │   Phát hiện  │  │   Phát hiện  │      │   │
│  │ │    ánh mắt   │  │    miệng     │  │    tay       │      │   │
│  └──────────────┘  └──────────────┘  └──────────────┘      │   │
│  │                                                               │   │
│  │ ┌──────────────┐  ┌──────────────┐                          │   │
│  │ │   Nhận diện  │  │   Đếm hành   │                          │   │
│  │ │   hành động  │  │   khách      │                          │   │
│  └──────────────┘  └──────────────┘                          │   │
│  └──────────────────────────┬──────────────────────────────────┘   │
│                             │                                        │
│                             ▼                                        │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │              LỚP PHÂN TÍCH (Ra quyết định bằng AI)           │   │
│  ├─────────────────────────────────────────────────────────────┤   │
│  │ ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │   │
│  │ │ Phân tích    │  │ Phân tích    │  │  Phân tích   │      │   │
│  │ │ buồn ngủ     │  │ xao nhãng    │  │  hành động   │      │   │
│  └──────────────┘  └──────────────┘  └──────────────┘      │   │
│  │                                                               │   │
│  │ ┌─────────────────────────────────────────┐                 │   │
│  │ │      Bộ máy đánh giá rủi ro             │                 │   │
│  │ │  (Tổng hợp tất cả kết quả phân tích)    │                 │   │
│  └─────────────────────────────────────────┘                 │   │
│  └──────────────────────────┬──────────────────────────────────┘   │
│                             │                                        │
│                             ▼                                        │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │              LỚP HÀNH ĐỘNG (Phản hồi & Lưu trữ)               │   │
│  ├─────────────────────────────────────────────────────────────┤   │
│  │ ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │   │
│  │ │   Quản lý    │  │   Ghi nhật   │  │   Tạo báo    │      │   │
│  │ │   cảnh báo   │  │   ký sự kiện │  │   cáo        │      │   │
│  └──────────────┘  └──────────────┘  └──────────────┘      │   │
│  └──────────────────────────┬──────────────────────────────────┘   │
│                             │                                        │
│                             ▼                                        │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                   LỚP ĐẦU RA                                 │   │
│  ├─────────────────────────────────────────────────────────────┤   │
│  │  - Cảnh báo Âm thanh/Hình ảnh (Loa, LED)                    │   │
│  │  - Giao diện Dashboard (Màn hình theo dõi tùy chọn)         │   │
│  │  - Lưu trữ Cơ sở dữ liệu (SQLite)                           │   │
│  │  - Tệp nhật ký (Hệ thống, sự kiện)                          │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                       │
└───────────────────────────────────────────────────────────────────┘
```

### 2.3 Mô tả các lớp

| Lớp | Trách nhiệm | Đầu vào | Đầu ra |
|-------|---------------|-------|--------|
| **Đầu vào** | Thu nhận và tiền xử lý khung hình video | Luồng camera hồng ngoại | Khung hình đã xử lý (640x480, grayscale) |
| **Phát hiện** | Trích xuất đặc trưng bằng CV | Khung hình đã xử lý | Vector đặc trưng (điểm mốc khuôn mặt, trạng thái mắt, tư thế) |
| **Phân tích** | Diễn giải đặc trưng để đánh giá trạng thái tài xế | Vector đặc trưng | Kết quả phân tích (mức độ buồn ngủ, điểm xao nhãng) |
| **Hành động** | Tạo cảnh báo và ghi nhật ký sự kiện | Kết quả phân tích | Cảnh báo, bản ghi database, nhật ký |
| **Đầu ra** | Trình bày thông tin cho tài xế/hệ thống | Cảnh báo, nhật ký | Cảnh báo âm thanh/hình ảnh, giao diện, dữ liệu lưu trữ |

---

## 3. NGỮ CẢNH & PHẠM VI HỆ THỐNG

### 3.1 Sơ đồ ngữ cảnh hệ thống

```
                    ┌─────────────────────────────────────┐
                    │   MÔI TRƯỜNG BÊN NGOÀI              │
                    │                                     │
                    │  ┌──────────┐      ┌──────────┐   │
                    │  │  Tài xế  │      │ Nội thất │   │
                    │  │ (Con người)│     │ Xe       │   │
                    │  └─────┬────┘      └────┬─────┘   │
                    │        │                │         │
                    │        │ được quan sát  │ lắp đặt │
                    │        │ bởi            │ trong   │
                    └────────┼────────────────┼─────────┘
                             │                │
                             ▼                ▼
┌────────────────────────────────────────────────────────────────┐
│                 HỆ THỐNG GIÁM SÁT TÀI XẾ                        │
│                 (Phạm vi hệ thống)                               │
│                                                                  │
│  ┌──────────────┐        ┌─────────────────┐                  │
│  │  Camera hồng │───────▶│  Bộ xử lý chính │                  │
│  │   ngoại      │        │                 │                  │
│  └──────────────┘        └────────┬────────┘                  │
│                                   │                             │
│                          ┌────────▼────────┐                   │
│                          │   Lưu trữ dữ liệu│                   │
│                          │    (SQLite)     │                   │
│                          └─────────────────┘                   │
│                                   │                             │
│  ┌──────────────┐        ┌────────▼────────┐                  │
│  │ Cảnh báo Âm  │◀───────│  Đầu ra cảnh    │                  │
│  │ thanh/Hình ảnh│        │  báo            │                  │
│  └──────────────┘        └─────────────────┘                  │
│                                                                  │
└──────────────────────────────────────────────────────────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Người dùng ngoài│
                    │ (Quản lý đội xe)│
                    │ (Xem lại nhật ký)│
                    └─────────────────┘
```

### 3.2 Phạm vi hệ thống

**Bên trong phạm vi hệ thống (Trách nhiệm):**
- Thu nhận video và xử lý hình ảnh.
- Phát hiện khuôn mặt, mắt và hoạt động.
- Phân tích trạng thái tài xế (buồn ngủ, xao nhãng).
- Tạo và chuyển giao cảnh báo.
- Ghi nhật ký sự kiện và lưu trữ dữ liệu.
- Theo dõi sức khỏe hệ thống.

**Bên ngoài phạm vi hệ thống (Không bao gồm):**
- Hệ thống điều khiển xe (phanh, lái).
- Kết nối Internet / dịch vụ đám mây.
- Các hệ thống hỗ trợ lái xe nâng cao (ADAS).
- Tích hợp hệ thống thông tin giải trí trên xe.
- Thiết lập nhiều camera (chỉ sử dụng một camera hồng ngoại).
- Hệ thống xác thực tài xế (dành cho nghiên cứu tương lai).

### 3.3 Giao diện bên ngoài

| Giao diện | Loại | Hướng | Mô tả |
|-----------|------|-----------|-------------|
| **Camera hồng ngoại** | Phần cứng | Đầu vào | Camera hồng ngoại kết nối USB cung cấp luồng video 30fps |
| **Loa** | Phần cứng | Đầu ra | Đầu ra âm thanh USB/3.5mm cho tiếng chuông cảnh báo |
| **Đèn LED chỉ báo** | Phần cứng | Đầu ra | Đèn LED điều khiển qua GPIO để cảnh báo hình ảnh |
| **Nguồn điện** | Phần cứng | Đầu vào | Nguồn 5V USB-C (cho Jetson Nano/RPi 4) |
| **Hệ thống tệp** | Phần mềm | Hai chiều | Lưu trữ cục bộ cho database, nhật ký, tệp cấu hình |
| **Hệ điều hành** | Phần mềm | Hai chiều | Linux (Ubuntu 20.04 / Raspberry Pi OS) |

---

## 4. CÁC THÀNH PHẦN HỆ THỐNG

### 4.1 Sơ đồ thành phần

```
┌────────────────────────────────────────────────────────────────────┐
│                    HỆ THỐNG GIÁM SÁT TÀI XẾ                         │
│                                                                      │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │  PHÂN HỆ ĐẦU VÀO                                              │ │
│  │  ┌────────────────┐      ┌────────────────┐                 │ │
│  │  │ Thành phần     │─────▶│ Thành phần     │                 │ │
│  │  │ Thu nhận video │      │ Tiền xử lý     │                 │ │
│  │  └────────────────┘      └────────────────┘                 │ │
│  └──────────────────────────────┬───────────────────────────────┘ │
│                                 │ khung hình                       │
│  ┌──────────────────────────────▼───────────────────────────────┐ │
│  │  PHÂN HỆ PHÁT HIỆN                                           │ │
│  │  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐│ │
│  │  │ Phát hiện mặt  │  │ Theo dõi mắt   │  │ Ước tính tư thế││ │
│  │  └────────────────┘  └────────────────┘  └────────────────┘│ │
│  │  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐│ │
│  │  │ Theo dõi ánh   │  │ Phát hiện      │  │ Phát hiện tay  ││ │
│  │  │ mắt            │  │ miệng          │  │                ││ │
│  │  └────────────────┘  └────────────────┘  └────────────────┘│ │
│  │  ┌────────────────┐  ┌────────────────┐                    │ │
│  │  │ Nhận diện hành │  │ Đếm hành khách │                    │ │
│  │  │ động           │  │                │                    │ │
│  │  └────────────────┘  └────────────────┘                    │ │
│  └──────────────────────────────┬───────────────────────────────┘ │
│                                 │ đặc trưng                        │
│  ┌──────────────────────────────▼───────────────────────────────┐ │
│  │  PHÂN HỆ PHÂN TÍCH                                            │ │
│  │  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐│ │
│  │  │ Phân tích      │  │ Phân tích      │  │ Phân tích      ││ │
│  │  │ buồn ngủ       │  │ xao nhãng      │  │ hành động      ││ │
│  │  └────────┬───────┘  └────────┬───────┘  └────────┬───────┘│ │
│  │           │                   │                   │         │ │
│  │           └───────────────────┼───────────────────┘         │ │
│  │                               ▼                              │ │
│  │                    ┌────────────────────┐                    │ │
│  │                    │ Bộ máy đánh giá    │                    │ │
│  │                    │ rủi ro             │                    │ │
│  │                    └────────────────────┘                    │ │
│  └──────────────────────────────┬───────────────────────────────┘ │
│                                 │ sự kiện rủi ro                   │
│  ┌──────────────────────────────▼───────────────────────────────┐ │
│  │  PHÂN HỆ HÀNH ĐỘNG                                            │ │
│  │  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐│ │
│  │  │ Quản lý cảnh   │  │ Ghi nhật ký    │  │ Tạo báo cáo    ││ │
│  │  │ báo            │  │ sự kiện        │  │                ││ │
│  │  └────────────────┘  └────────────────┘  └────────────────┘│ │
│  └──────────────────────────────┬───────────────────────────────┘ │
│                                 │                                  │
│  ┌──────────────────────────────▼───────────────────────────────┐ │
│  │  PHÂN HỆ LƯU TRỮ                                              │ │
│  │  ┌────────────────┐  ┌────────────────┐                     │ │
│  │  │ Quản lý Cơ sở  │  │ Quản lý lưu    │                     │ │
│  │  │ dữ liệu        │  │ trữ tệp        │                     │ │
│  │  └────────────────┘  └────────────────┘                     │ │
│  └──────────────────────────────────────────────────────────────┘ │
│                                                                      │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │  PHÂN HỆ BỔ TRỢ                                               │ │
│  │  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐│ │
│  │  │ Quản lý cấu    │  │ Theo dõi hệ    │  │ Ghi log kỹ     ││ │
│  │  │ hình           │  │ thống          │  │ thuật          ││ │
│  │  └────────────────┘  └────────────────┘  └────────────────┘│ │
│  └──────────────────────────────────────────────────────────────┘ │
│                                                                      │
└────────────────────────────────────────────────────────────────────┘
```

### 4.2 Trách nhiệm của các thành phần

#### **PHÂN HỆ ĐẦU VÀO**

| Thành phần | Trách nhiệm | Các chức năng chính |
|-----------|---------------|---------------|
| **Thu nhận video** | Giao tiếp với camera IR, chụp khung hình | `init_camera()`, `get_frame()`, `release()` |
| **Tiền xử lý** | Chuẩn bị khung hình (thay đổi kích thước, chuẩn hóa, tăng cường) | `preprocess()`, `enhance_ir_image()`, `normalize()` |

#### **PHÂN HỆ PHÁT HIỆN**

| Thành phần | Trách nhiệm | Các chức năng chính |
|-----------|---------------|---------------|
| **Phát hiện khuôn mặt** | Phát hiện mặt và trích xuất 68 điểm mốc | `detect_face()`, `get_landmarks()` |
| **Theo dõi mắt** | Theo dõi mắt, tính toán tỷ lệ EAR (Eye Aspect Ratio) | `track_eyes()`, `compute_ear()`, `detect_blink()` |
| **Ước tính tư thế đầu** | Ước tính tư thế đầu 3D (pitch, yaw, roll) | `estimate_pose()`, `get_rotation_angles()` |
| **Theo dõi ánh mắt** | Theo dõi hướng nhìn và tiêu điểm của mắt | `track_gaze()`, `compute_gaze_vector()` |
| **Phát hiện miệng** | Phát hiện trạng thái miệng (mở/đóng, ngáp) | `detect_mouth()`, `compute_mar()` (Mouth Aspect Ratio) |
| **Phát hiện tay** | Phát hiện vị trí tay (trên vô lăng, rời vô lăng, cầm điện thoại) | `detect_hands()`, `classify_hand_activity()` |
| **Nhận diện hành động** | Nhận diện hành động nguy hiểm (gọi điện, uống nước, hút thuốc, v.v.) | `recognize_activity()`, `classify_object()` |
| **Đếm hành khách** | Đếm số lượng người trong xe | `count_passengers()`, `detect_multiple_faces()` |

#### **PHÂN HỆ PHÂN TÍCH**

| Thành phần | Trách nhiệm | Các chức năng chính |
|-----------|---------------|---------------|
| **Phân tích buồn ngủ** | Phân tích mức độ buồn ngủ dựa trên dữ liệu mắt, miệng, đầu | `analyze_drowsiness()`, `compute_perclos()`, `detect_microsleep()` |
| **Phân tích xao nhãng** | Phân tích sự xao nhãng dựa trên ánh mắt và tư thế đầu | `analyze_distraction()`, `compute_attention_score()` |
| **Phân tích hành động** | Phân tích các hành động nguy hiểm và đánh giá rủi ro | `analyze_activity()`, `assess_activity_risk()` |
| **Bộ máy đánh giá rủi ro** | Tổng hợp tất cả kết quả phân tích, tính toán điểm rủi ro tổng thể | `assess_overall_risk()`, `generate_event()` |

#### **PHÂN HỆ HÀNH ĐỘNG**

| Thành phần | Trách nhiệm | Các chức năng chính |
|-----------|---------------|---------------|
| **Quản lý cảnh báo** | Tạo và chuyển giao cảnh báo âm thanh/hình ảnh | `trigger_alert()`, `play_audio()`, `blink_led()` |
| **Ghi nhật ký sự kiện** | Ghi lại các sự kiện vào database và tệp | `log_event()`, `store_to_db()`, `write_to_file()` |
| **Tạo báo cáo** | Tạo báo cáo tóm tắt và số liệu phân tích | `generate_trip_report()`, `create_statistics()` |

#### **PHÂN HỆ LƯU TRỮ**

| Thành phần | Trách nhiệm | Các chức năng chính |
|-----------|---------------|---------------|
| **Quản lý Cơ sở dữ liệu** | Quản lý kết nối và truy vấn SQLite | `connect()`, `execute_query()`, `insert_event()` |
| **Quản lý lưu trữ tệp** | Quản lý tệp nhật ký và tệp cấu hình | `write_log()`, `read_config()`, `save_snapshot()` |

#### **PHÂN HỆ BỔ TRỢ**

| Thành phần | Trách nhiệm | Các chức năng chính |
|-----------|---------------|---------------|
| **Quản lý cấu hình** | Tải và quản lý cấu hình hệ thống | `load_config()`, `get_threshold()`, `update_setting()` |
| **Theo dõi hệ thống** | Theo dõi sức khỏe hệ thống (CPU, bộ nhớ, FPS) | `monitor_resources()`, `check_health()`, `log_performance()` |
| **Ghi log kỹ thuật** | Ghi nhật ký tập trung để phục vụ gỡ lỗi | `log_info()`, `log_error()`, `log_debug()` |

---

## 5. TRIỂN KHAI HỆ THỐNG

### 5.1 Kiến trúc triển khai

```
┌─────────────────────────────────────────────────────────────────┐
│                        PHƯƠNG TIỆN VẬT LÝ                        │
│                                                                   │
│  ┌────────────────────────────────────────────────────────────┐│
│  │  LẮP ĐẶT TRÊN BẢNG ĐIỀU KHIỂN (DASHBOARD)                   ││
│  │                                                              ││
│  │  ┌──────────────────────────────────────────────────────┐ ││
│  │  │  Thiết bị tính toán tại biên (Edge Device)           │ ││
│  │  │  (Jetson Nano 4GB / Raspberry Pi 4 8GB)              │ ││
│  │  │                                                        │ ││
│  │  │  ┌──────────────────────────────────────────────┐   │ ││
│  │  │  │  Hệ điều hành: Ubuntu 20.04 / RPi OS        │   │ ││
│  │  │  └──────────────────────────────────────────────┘   │ ││
│  │  │  ┌──────────────────────────────────────────────┐   │ ││
│  │  │  │  Môi trường chạy Python 3.8                  │   │ ││
│  │  │  └──────────────────────────────────────────────┘   │ ││
│  │  │  ┌──────────────────────────────────────────────┐   │ ││
│  │  │  │  Ứng dụng DMS                                 │   │ ││
│  │  │  │  - Tiến trình chính (dms_main.py)            │   │ ││
│  │  │  │  - Các mô-đun phát hiện                      │   │ ││
│  │  │  │  - Các mô-đun phân tích                      │   │ ││
│  │  │  │  - Các mô-đun hành động                      │   │ ││
│  │  │  └──────────────────────────────────────────────┘   │ ││
│  │  │  ┌──────────────────────────────────────────────┐   │ ││
│  │  │  │  Thư viện & Phụ thuộc                         │   │ ││
│  │  │  │  - OpenCV 4.5                                 │   │ ││
│  │  │  │  - dlib 19.22                                 │   │ ││
│  │  │  │  - TensorFlow Lite 2.8                        │   │ ││
│  │  │  │  - NumPy, SciPy                               │   │ ││
│  │  │  └──────────────────────────────────────────────┘   │ ││
│  │  │  ┌──────────────────────────────────────────────┐   │ ││
│  │  │  │  Lưu trữ cục bộ                               │   │ ││
│  │  │  │  - CSDL SQLite (events.db)                   │   │ ││
│  │  │  │  - Tệp cấu hình (config.yaml)                │   │ ││
│  │  │  │  - Tệp nhật ký (logs/*.log)                  │   │ ││
│  │  │  │  - Tệp mô hình (models/*.tflite)             │   │ ││
│  │  │  └──────────────────────────────────────────────┘   │ ││
│  │  │                                                        │ ││
│  │  └─────┬───────────┬────────────┬──────────────────────┘ ││
│  │        │           │            │                          ││
│  └────────┼───────────┼────────────┼──────────────────────────┘│
│           │           │            │                            │
│  ┌────────▼──────┐ ┌─▼───────┐ ┌─▼──────────┐ ┌──────────────┐│
│  │ Camera IR     │ │ Loa     │ │ Dải đèn LED│ │ Nguồn điện   ││
│  │ (USB)         │ │ (Âm      │ │ (GPIO)     │ │ (USB-C 5V)   ││
│  │ 640x480 30fps │ │ thanh)   │ │ Cảnh báo   │ │ 15W          ││
│  └───────────────┘ └─────────┘ └────────────┘ └──────────────┘│
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

### 5.2 Thông số triển khai phần cứng

#### **Lựa chọn 1: NVIDIA Jetson Nano 4GB (Khuyến nghị)**

| Thành phần | Thông số | Mục đích |
|-----------|---------------|---------|
| **CPU** | Quad-core ARM Cortex-A57 @ 1.43 GHz | Xử lý chính |
| **GPU** | 128-core NVIDIA Maxwell | Tăng tốc suy luận mô hình |
| **RAM** | 4GB LPDDR4 | Bộ nhớ ứng dụng |
| **Lưu trữ** | Thẻ nhớ microSD 64GB | Hệ điều hành, ứng dụng, CSDL, nhật ký |
| **Giao diện Camera** | USB 2.0 | Kết nối camera IR |
| **Đầu ra âm thanh** | Jack 3.5mm / HDMI | Âm thanh cảnh báo |
| **GPIO** | Header 40 chân | Đèn LED chỉ báo |
| **Nguồn** | 5V 4A (USB-C / DC) | Nguồn hệ thống |
| **Chi phí** | ~$100-120 | |

**Ưu điểm:**
- Tăng tốc GPU cho các mô hình TensorFlow.
- Hiệu năng thời gian thực tốt hơn (dự kiến 20-25 FPS).
- Còn nhiều dư địa cho các tính năng trong tương lai.

#### **Lựa chọn 2: Raspberry Pi 4 Model B 8GB (Thay thế)**

| Thành phần | Thông số | Mục đích |
|-----------|---------------|---------|
| **CPU** | Quad-core ARM Cortex-A72 @ 1.5 GHz | Xử lý chính |
| **RAM** | 8GB LPDDR4 | Bộ nhớ ứng dụng (đệm lớn hơn) |
| **Lưu trữ** | Thẻ nhớ microSD 64GB | Hệ điều hành, ứng dụng, CSDL, nhật ký |
| **Giao diện Camera** | USB 3.0 | Kết nối camera IR |
| **Đầu ra âm thanh** | Jack 3.5mm / HDMI | Âm thanh cảnh báo |
| **GPIO** | Header 40 chân | Đèn LED chỉ báo |
| **Nguồn** | 5V 3A (USB-C) | Nguồn hệ thống |
| **Chi phí** | ~$75-90 | |

**Ưu điểm:**
- Chi phí thấp hơn.
- RAM lớn hơn (8GB so với 4GB).
- Dễ mua hơn.

**Nhược điểm:**
- Không có tăng tốc GPU (suy luận chỉ bằng CPU).
- FPS thấp hơn (dự kiến 15-18 FPS).

---

## 6. LUỒNG DỮ LIỆU

### 6.1 Đường dẫn xử lý chính

```
┌──────────┐
│ Camera IR│
│ (30 FPS) │
└─────┬────┘
      │ khung hình thô (640x480 RGB)
      ▼
┌───────────────────┐
│ Thành phần        │
│ Thu nhận video    │
│ - Chụp khung hình │
│ - Kiểm tra hợp lệ │
└─────┬─────────────┘
      │ frame: np.ndarray(480,640,3)
      ▼
┌───────────────────┐
│ Tiền xử lý        │
│ - Đổi kích thước  │
│ - Chuyển xám      │
│ - Chuẩn hóa       │
│ - Tăng cường      │
└─────┬─────────────┘
      │ preprocessed_frame: np.ndarray(480,640)
      ▼
┌─────────────────────────────────────────────┐
│         GIAI ĐOẠN PHÁT HIỆN (SONG SONG)     │
├─────────────────────────────────────────────┤
│                                             │
│  ┌──────────────┐    ┌──────────────┐     │
│  │ Phát hiện    │───▶│ Điểm mốc     │     │
│  │ khuôn mặt    │    │ (68 điểm)    │     │
│  └──────────────┘    └──────┬───────┘     │
│                             │               │
│  ┌──────────────────────────▼───────────┐ │
│  │     PHÁT HIỆN PHỤ THUỘC              │ │
│  │  (Yêu cầu điểm mốc mặt làm đầu vào)  │ │
│  │                                       │ │
│  │  ┌────────────┐  ┌────────────┐     │ │
│  │  │ Theo dõi   │  │ Phát hiện  │     │ │
│  │  │ mắt        │  │ miệng      │     │ │
│  │  └─────┬──────┘  └─────┬──────┘     │ │
│  │        │               │             │ │
│  │        │  ┌────────────▼──┐          │ │
│  │        │  │ Ước tính      │          │ │
│  │        │  │ tư thế đầu    │          │ │
│  │        │  └─────┬─────────┘          │ │
│  │        │        │                    │ │
│  │        │  ┌─────▼─────┐              │ │
│  │        │  │ Theo dõi   │              │ │
│  │        │  │ ánh mắt    │              │ │
│  │        │  └───────────┘              │ │
│  └────────┼────────┬────────────────────┘ │
│           │        │                       │
│  ┌────────▼────┐  ┌▼───────────┐          │
│  │ Phát hiện   │  │ Nhận diện  │          │
│  │ tay         │  │ hành động  │          │
│  └─────────────┘  └────────────┘          │
│                                             │
└─────────────────┬───────────────────────────┘
                  │
                  │ detection_results: DetectionData
                  │ {
                  │   face_landmarks: array(68,2),
                  │   left_eye_ear: float,
                  │   right_eye_ear: float,
                  │   mar: float,
                  │   head_pose: (pitch, yaw, roll),
                  │   gaze_direction: (x, y),
                  │   hands_on_wheel: bool,
                  │   detected_activity: string,
                  │   timestamp: datetime
                  │ }
                  ▼
┌─────────────────────────────────────────────┐
│         GIAI ĐOẠN PHÂN TÍCH (SONG SONG)     │
├─────────────────────────────────────────────┤
│                                             │
│  ┌──────────────────┐                      │
│  │ Phân tích        │                      │
│  │ buồn ngủ         │                      │
│  │ Đầu vào:         │                      │
│  │  - EAR trái/phải │                      │
│  │  - MAR           │                      │
│  │  - pitch đầu     │                      │
│  │ Đầu ra:          │                      │
│  │  - mức buồn ngủ  │                      │
│  │    (0-100)       │                      │
│  │  - có buồn ngủ   │                      │
│  └──────────┬───────┘                      │
│             │                               │
│  ┌──────────▼───────┐                      │
│  │ Phân tích        │                      │
│  │ xao nhãng        │                      │
│  │ Đầu vào:         │                      │
│  │  - yaw/pitch đầu │                      │
│  │  - hướng nhìn    │                      │
│  │ Đầu ra:          │                      │
│  │  - điểm tập trung│                      │
│  │    (0-100)       │                      │
│  │  - có xao nhãng  │                      │
│  └──────────┬───────┘                      │
│             │                               │
│  ┌──────────▼───────┐                      │
│  │ Phân tích        │                      │
│  │ hành động        │                      │
│  │ Đầu vào:         │                      │
│  │  - loại hành động│                      │
│  │  - trạng thái tay│                      │
│  │ Đầu ra:          │                      │
│  │  - mức rủi ro    │                      │
│  │  - có nguy hiểm  │                      │
│  └──────────┬───────┘                      │
│             │                               │
│             └───────┬───────────────────────┤
│                     │                       │
│             ┌───────▼────────┐              │
│             │ Đánh giá rủi ro│              │
│             │ - Tổng hợp     │              │
│             │ - Tính điểm    │              │
│             │ - Tạo sự kiện  │              │
│             └────────────────┘              │
│                                             │
└─────────────────┬───────────────────────────┘
                  │
                  │ risk_event: RiskEvent
                  │ {
                  │   event_type: string,
                  │   severity: string (LOW/MEDIUM/HIGH),
                  │   risk_score: float,
                  │   drowsiness_level: float,
                  │   attention_score: float,
                  │   detected_activity: string,
                  │   requires_alert: bool,
                  │   timestamp: datetime
                  │ }
                  ▼
┌─────────────────────────────────────────────┐
│         GIAI ĐOẠN HÀNH ĐỘNG (TUẦN TỰ)       │
├─────────────────────────────────────────────┤
│                                             │
│  ┌──────────────────┐                      │
│  │ 1. Quản lý cảnh   │                      │
│  │    báo           │                      │
│  │ - Kiểm tra độ ngh.│                      │
│  │ - Phát âm thanh  │                      │
│  │ - Nháy đèn LED   │                      │
│  └──────────┬───────┘                      │
│             │                               │
│  ┌──────────▼───────┐                      │
│  │ 2. Ghi nhật ký   │                      │
│  │ - Lưu vào DB     │                      │
│  │ - Ghi vào tệp    │                      │
│  └──────────┬───────┘                      │
│             │                               │
│  ┌──────────▼───────┐                      │
│  │ 3. Tạo báo cáo   │                      │
│  │ (khi kết thúc)   │                      │
│  │ - Tổng hợp dữ li.│                      │
│  │ - Tạo báo cáo    │                      │
│  └──────────────────┘                      │
│                                             │
└─────────────────────────────────────────────┘
                  │
                  ▼
        ┌──────────────────┐
        │ ĐẦU RA:          │
        │ - Âm thanh báo   │
        │ - Đèn LED nháy   │
        │ - Bản ghi DB     │
        │ - Nhật ký tệp    │
        └──────────────────┘
```

### 6.2 Thời gian luồng dữ liệu

**Tiến trình xử lý khung hình (Mục tiêu: <67ms cho 15 FPS):**

| Giai đoạn | Thành phần | Thời gian dự tính | Cộng dồn |
|-------|-----------|-------------|------------|
| 1 | Thu nhận video | 5ms | 5ms |
| 2 | Tiền xử lý | 3ms | 8ms |
| 3 | Phát hiện khuôn mặt | 15ms | 23ms |
| 4 | Theo dõi mắt + miệng | 8ms | 31ms |
| 5 | Tư thế đầu + Ánh mắt | 10ms | 41ms |
| 6 | Nhận diện tay + hành động | 12ms | 53ms |
| 7 | Phân tích (Buồn ngủ + Xao nhãng + Hành động) | 8ms | 61ms |
| 8 | Đánh giá rủi ro | 2ms | 63ms |
| 9 | Cảnh báo + Ghi nhật ký | 3ms | 66ms |
| **TỔNG CỘNG** | | **66ms** | **~15 FPS** |

**Lưu ý về hiệu năng:**
- Giai đoạn phát hiện (bước 3-6) có thể được song song hóa một phần trên GPU của Jetson Nano.
- Cảnh báo và ghi nhật ký (bước 9) có thể chạy không đồng bộ để tránh chặn khung hình tiếp theo.
- Nếu thời gian xử lý vượt quá 67ms, khung hình sẽ bị bỏ qua (graceful degradation).

---

## 7. QUY TRÌNH XỬ LÝ

### 7.1 Luồng tiến trình chính

```
┌────────────────────────────────────────────────────────────────┐
│                      KHỞI ĐỘNG HỆ THỐNG                         │
└────────────┬───────────────────────────────────────────────────┘
             │
             ▼
      ┌─────────────┐
      │ Tải cấu hình│
      └──────┬──────┘
             │
             ▼
     ┌────────────────┐
     │ Khởi tạo CSDL  │
     │ (tạo bảng nếu  │
     │  chưa có)      │
     └──────┬─────────┘
             │
             ▼
     ┌────────────────┐
     │ Tải mô hình ML │
     │ - điểm mốc     │
     │ - phân loại h.đ│
     └──────┬─────────┘
             │
             ▼
     ┌────────────────┐
     │ Khởi tạo Camera│
     │ (kiểm tra k.nối)│
     └──────┬─────────┘
             │
             ▼
     ┌────────────────┐
     │ Khởi tạo p.cứng│
     │ - loa          │
     │ - GPIO cho LED │
     └──────┬─────────┘
             │
             ▼
┌────────────────────────────────────────────────────────────────┐
│                    VÒNG LẶP XỬ LÝ CHÍNH                         │
│  while running:                                                 │
│    ┌─────────────────────────────────────────────────────┐    │
│    │ 1. Chụp khung hình                                   │    │
│    │    - Lấy khung hình từ camera                        │    │
│    │    - Kiểm tra tính hợp lệ                            │    │
│    │    - Nếu lỗi: ghi log, bỏ qua vòng lặp               │    │
│    └────────┬────────────────────────────────────────────┘    │
│             │                                                   │
│             ▼                                                   │
│    ┌─────────────────────────────────────────────────────┐    │
│    │ 2. Tiền xử lý khung hình                             │    │
│    │    - Thay đổi kích thước                             │    │
│    │    - Chuyển sang ảnh xám                             │    │
│    │    - Tăng cường với CLAHE                            │    │
│    └────────┬────────────────────────────────────────────┘    │
│             │                                                   │
│             ▼                                                   │
│    ┌─────────────────────────────────────────────────────┐    │
│    │ 3. Giai đoạn phát hiện                               │    │
│    │    a) Phát hiện khuôn mặt và điểm mốc                │    │
│    │       - Nếu không mặt: tăng no_face_counter          │    │
│    │       - Nếu vượt ngưỡng: cảnh báo "không mặt",       │    │
│    │         nhảy tới bước 9                              │    │
│    │    b) Theo dõi mắt (tính EAR)                        │    │
│    │    c) Phát hiện miệng (tính MAR)                     │    │
│    │    d) Ước tính tư thế đầu                            │    │
│    │    e) Theo dõi hướng nhìn                            │    │
│    │    f) Phát hiện tay                                  │    │
│    │    g) Nhận diện hành động                            │    │
│    └────────┬────────────────────────────────────────────┘    │
│             │                                                   │
│             ▼                                                   │
│    ┌─────────────────────────────────────────────────────┐    │
│    │ 4. Giai đoạn phân tích                               │    │
│    │    a) Phân tích buồn ngủ                             │    │
│    │       - Tính PERCLOS                                 │    │
│    │       - Kiểm tra ngủ gật (microsleep)                │    │
│    │       - Đánh giá tần suất ngáp                       │    │
│    │    b) Phân tích xao nhãng                            │    │
│    │       - Kiểm tra thời gian nhìn ra ngoài             │    │
│    │       - Kiểm tra góc quay đầu                        │    │
│    │    c) Phân tích hành động                            │    │
│    │       - Đánh giá mức rủi ro hành động                │    │
│    └────────┬────────────────────────────────────────────┘    │
│             │                                                   │
│             ▼                                                   │
│    ┌─────────────────────────────────────────────────────┐    │
│    │ 5. Đánh giá rủi ro                                   │    │
│    │    - Tổng hợp kết quả phân tích                      │    │
│    │    - Tính toán điểm rủi ro tổng thể                  │    │
│    │    - Xác định loại sự kiện và mức độ                 │    │
│    │    - Quyết định có cần cảnh báo không                │    │
│    └────────┬────────────────────────────────────────────┘    │
│             │                                                   │
│             ▼                                                   │
│    ┌─────────────────────────────────────────────────────┐    │
│    │ 6. Cảnh báo (nếu cần)                                │    │
│    │    - Kích hoạt âm thanh (không đồng bộ)              │    │
│    │    - Nháy đèn LED (không đồng bộ)                    │    │
│    └────────┬────────────────────────────────────────────┘    │
│             │                                                   │
│             ▼                                                   │
│    ┌─────────────────────────────────────────────────────┐    │
│    │ 7. Ghi nhật ký                                       │    │
│    │    - Lưu vào CSDL (không đồng bộ)                    │    │
│    │    - Ghi vào tệp (không đồng bộ)                     │    │
│    │    - Lưu ảnh chụp (nếu có cấu hình)                  │    │
│    └────────┬────────────────────────────────────────────┘    │
│             │                                                   │
│             ▼                                                   │
│    ┌─────────────────────────────────────────────────────┐    │
│    │ 8. Theo dõi hệ thống                                 │    │
│    │    - Theo dõi FPS                                    │    │
│    │    - Theo dõi CPU/bộ nhớ                             │    │
│    │    - Ghi log hiệu năng (mỗi 100 khung hình)          │    │
│    └────────┬────────────────────────────────────────────┘    │
│             │                                                   │
│             ▼                                                   │
│    ┌─────────────────────────────────────────────────────┐    │
│    │ 9. Điều khiển vòng lặp                               │    │
│    │    - Kiểm tra tín hiệu tắt máy                       │    │
│    │    - Trả lời hệ điều hành (tránh chiếm dụng CPU)     │    │
│    └─────────────────────────────────────────────────────┘    │
│             │                                                   │
│             └──────────────────▶ (quay lại bước 1)             │
└────────────────────────────────────────────────────────────────┘
             │
             ▼ (khi có tín hiệu tắt máy)
┌────────────────────────────────────────────────────────────────┐
│                      TẮT MÁY HỆ THỐNG                           │
│  ┌────────────────┐                                            │
│  │ Giải phóng Cam │                                            │
│  └────────┬───────┘                                            │
│           ▼                                                     │
│  ┌────────────────┐                                            │
│  │ Đóng CSDL      │                                            │
│  └────────┬───────┘                                            │
│           ▼                                                     │
│  ┌────────────────┐                                            │
│  │ Tạo báo cáo    │                                            │
│  │ (tóm tắt chuyến)│                                            │
│  └────────┬───────┘                                            │
│           ▼                                                     │
│  ┌────────────────┐                                            │
│  │ Dọn dẹp GPIO   │                                            │
│  └────────┬───────┘                                            │
│           ▼                                                     │
│       Exit(0)                                                   │
└────────────────────────────────────────────────────────────────┘
```

### 7.2 Sơ đồ trạng thái: Phát hiện trạng thái tài xế

```
                      ┌──────────────┐
                      │   BẮT ĐẦU    │
                      └──────┬───────┘
                             │
                             ▼
                   ┌─────────────────┐
              ┌───▶│   KHÔNG MẶT     │◀────┐
              │    │ (không thấy mặt)│     │
              │    └────────┬────────┘     │
              │             │               │
              │   thấy mặt  │               │ mất mặt >3s
              │             │               │
              │             ▼               │
     mất      │    ┌─────────────────┐     │
     mặt      │    │    BÌNH THƯỜNG  │─────┘
              │    │ (tỉnh táo, tập tr)│
              │    └────────┬────────┘
              │             │
              │             │ dấu hiệu buồn ngủ
              │             ▼
              │    ┌─────────────────┐
              │    │ BUỒN NGỦ NHẸ    │
              │    │ (EAR thấp, MAR↑)│
              │    └────────┬────────┘
              │             │
              │             │ buồn ngủ kéo dài >5s
              │             ▼
              │    ┌─────────────────┐
              └────┤ BUỒN NGỦ NẶNG   │
                   │ (PERCLOS>80%,   │
                   │  ngủ gật)       │
                   └─────────────────┘
                             │
                             │ mở mắt, tỉnh táo
                             ▼
                       (về BÌNH THƯỜNG)

                    ┌─────────────────┐
           ┌───────▶│   XAO NHÃNG     │◀──────┐
           │        │ (nhìn ra ngoài) │       │
           │        └─────────────────┘       │
           │                │                  │
           │                │ nhìn thẳng lại   │ nhìn ra >2s
           │                │                  │
           │                ▼                  │
    nhìn   │        ┌─────────────────┐       │
    ra     └────────│    BÌNH THƯỜNG  │───────┘
                    │                 │
                    └────────┬────────┘
                             │
                             │ phát hiện hành động nguy hiểm
                             ▼
                    ┌─────────────────┐
                    │ H.ĐỘNG NGUY HIỂM│
                    │ (gọi điện, uống,│
                    │  hút thuốc, v.v)│
                    └─────────────────┘
                             │
                             │ dừng hành động
                             ▼
                       (về BÌNH THƯỜNG)
```

---

## 8. KIẾN TRÚC VẬT LÝ

### 8.1 Các thành phần phần cứng

```
┌──────────────────────────────────────────────────────────────┐
│                    BỐ TRÍ HỆ THỐNG VẬT LÝ                     │
│                                                                │
│  ┌─────────────────────┐                                     │
│  │    CAMERA HỒNG NGOẠI│                                     │
│  │  - Độ phân giải: 640x480                                  │
│  │  - Tốc độ khung hình: 30fps                               │
│  │  - LED IR: 850nm     │                                    │
│  │  - Giao diện: USB 2.0│                                    │
│  │  - Lắp đặt: Dashboard, hướng về tài xế                    │
│  └──────────┬──────────┘                                     │
│             │ cáp USB (1.5m)                                  │
│             │                                                  │
│  ┌──────────▼──────────────────────────────────────────────┐│
│  │  THIẾT BỊ TÍNH TOÁN BIÊN                                 ││
│  │  (Jetson Nano 4GB / Raspberry Pi 4 8GB)                 ││
│  │                                                           ││
│  │  Cổng kết nối:                                            ││
│  │  - USB 2.0/3.0 x4 (camera, loa, ngoại vi)               ││
│  │  - Header GPIO 40 chân (đèn LED)                         ││
│  │  - Khe cắm microSD (lưu trữ)                             ││
│  │  - Đầu vào nguồn (USB-C hoặc DC)                         ││
│  └───────────┬──────────────────────────────────────────────┘│
│              │                                                 │
│      ┌───────┼──────────┬──────────────┐                     │
│      │       │          │              │                     │
│  ┌───▼──┐ ┌─▼──────┐ ┌─▼──────┐ ┌────▼──────┐              │
│  │ Dải  │ │ Loa    │ │ Thẻ    │ │ Nguồn     │              │
│  │ LED  │ │ (USB/  │ │ microSD│ │ điện      │              │
│  │(GPIO)│  3.5mm)  │ │ 64GB   │ │ 5V 4A     │              │
│  └──────┘ └────────┘ └────────┘ └───────────┘              │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

### 8.2 Kết nối các thành phần

| Nguồn | Đích | Giao diện | Cáp/Kết nối | Luồng dữ liệu |
|--------|-------------|-----------|------------------|-----------|
| Camera IR | Thiết bị biên | USB 2.0 | USB-A sang USB-A (1.5m) | Khung hình video → Thiết bị |
| Thiết bị biên | Loa | Âm thanh (3.5mm/USB) | Cáp 3.5mm hoặc USB | Âm thanh cảnh báo → Loa |
| Thiết bị biên | Dải đèn LED | GPIO (chân 11,13,15) | Dây nhảy (Jumper) | Tín hiệu điều khiển → LED |
| Bộ nguồn | Thiết bị biên | USB-C hoặc DC | Cáp nguồn | Nguồn 5V → Thiết bị |
| Bộ nguồn | Camera IR | USB (cấp qua bus) | Qua cáp dữ liệu USB | Nguồn 5V → Camera |

### 8.3 Lắp đặt trong xe

```
                        CÁI NHÌN BÊN TRONG XE
                        (Góc nhìn của tài xế)

         ┌─────────────────────────────────────────────┐
         │              Kính chắn gió                  │
         └─────────────────────────────────────────────┘
                             │
                             │
        ┌────────────────────▼────────────────────────┐
        │           Mặt trên Dashboard                 │
        │  ┌──────────────┐    ┌──────────────┐      │
        │  │ Camera IR    │    │ Dải đèn LED  │      │
        │  │ (trung tâm,  │    │ chỉ báo      │      │
        │  │  hướng về    │    │ (trong tầm   │      │
        │  │  tài xế)     │    │  mắt tài xế) │      │
        │  └──────┬───────┘    └──────────────┘      │
        │         │ cáp USB (đi luồn xuống)           │
        └─────────┼───────────────────────────────────┘
                  │
        ┌─────────▼───────────────────────────────────┐
        │         Mặt dưới Dashboard / Hộc để đồ       │
        │  ┌──────────────────────────────────────┐   │
        │  │ Thiết bị tính toán biên              │   │
        │  │ (Jetson Nano / Raspberry Pi)         │   │
        │  │ - Cố định bằng velcro hoặc giá đỡ    │   │
        │  └──────────────────────────────────────┘   │
        │  ┌──────────────┐                           │
        │  │ Loa          │                           │
        │  │ (vị trí cho  │                           │
        │  │  âm thanh rõ)│                           │
        │  └──────────────┘                           │
        └─────────────────────────────────────────────┘
                  │
                  │ Cáp nguồn
                  ▼
        ┌─────────────────────────────────────────────┐
        │      Tẩu thuốc 12V của xe với bộ            │
        │      chuyển đổi 12V→5V                      │
        └─────────────────────────────────────────────┘
```

**Yêu cầu lắp đặt:**
1. **Vị trí Camera**: Trung tâm dashboard, cách mặt tài xế 20-40cm, nghiêng 10-15° xuống dưới.
2. **Vị trí LED**: Trong tầm nhìn ngoại vi của tài xế, không cản trở tầm nhìn đường.
3. **Cố định thiết bị**: Phải được gắn chặt để tránh di chuyển/rung lắc.
4. **Quản lý cáp**: Cáp phải được cố định và không gây vướng víu các bộ phận điều khiển lái.
5. **Kết nối nguồn**: Nguồn 5V ổn định từ xe (sử dụng bộ chuyển đổi 12V→5V chất lượng).

---

## 9. DANH MỤC CÔNG NGHỆ

### 9.1 Tổng quan danh mục công nghệ

```
┌─────────────────────────────────────────────────────────────┐
│                    LỚP ỨNG DỤNG                              │
│  ┌───────────────────────────────────────────────────────┐ │
│  │ Hệ thống Giám sát Tài xế (Python 3.8)                 │ │
│  │ - Các mô-đun phát hiện, phân tích, hành động tùy chỉnh│ │
│  └───────────────────────────────────────────────────────┘ │
└────────────────────────┬────────────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────────────┐
│                 FRAMEWORKS & THƯ VIỆN                        │
├──────────────────────────────────────────────────────────────┤
│  Thị giác máy tính:                                         │
│  - OpenCV 4.5.5 (cv2)                                       │
│  - dlib 19.22 (phát hiện mặt, điểm mốc)                     │
│                                                              │
│  Học máy (Machine Learning):                                │
│  - TensorFlow Lite 2.8 (nhận diện hành động)                │
│  - NumPy 1.21 (toán học ma trận)                            │
│  - SciPy 1.7 (xử lý tín hiệu)                               │
│                                                              │
│  Dữ liệu & Lưu trữ:                                          │
│  - SQLite3 (có sẵn, cơ sở dữ liệu)                          │
│  - PyYAML 6.0 (tệp cấu hình)                                 │
│                                                              │
│  Giao tiếp phần cứng:                                        │
│  - RPi.GPIO / Jetson.GPIO (điều khiển LED)                  │
│  - pygame 2.1 (phát âm thanh)                               │
└────────────────────────┬────────────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────────────┐
│                  HỆ ĐIỀU HÀNH                                │
│  - Ubuntu 20.04 LTS (cho Jetson Nano)                      │
│  - Raspberry Pi OS (cho Raspberry Pi 4)                     │
│  - Môi trường chạy Python 3.8                                │
└────────────────────────┬────────────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────────────┐
│                    LỚP PHẦN CỨNG                             │
│  - NVIDIA Jetson Nano 4GB / Raspberry Pi 4 8GB             │
│  - Camera IR (USB)                                           │
│  - Loa, LED, Lưu trữ (microSD)                              │
└──────────────────────────────────────────────────────────────┘
```

### 9.2 Lựa chọn công nghệ chi tiết

#### **Ngôn ngữ lập trình**

| Công nghệ | Phiên bản | Mục đích | Lý do lựa chọn |
|------------|---------|---------|---------------|
| **Python** | 3.8 | Ngôn ngữ chính | - Hỗ trợ thư viện CV và ML tuyệt vời<br>- Dễ phát triển và gỡ lỗi<br>- Hiệu năng tốt cho mẫu thử<br>- Được hỗ trợ trên cả Jetson và RPi |

#### **Thư viện Thị giác máy tính**

| Công nghệ | Phiên bản | Mục đích | Lý do lựa chọn |
|------------|---------|---------|---------------|
| **OpenCV** | 4.5.5 | Thu nhận video, xử lý ảnh, vẽ đồ họa | - Tiêu chuẩn ngành cho CV<br>- Hỗ trợ tăng tốc phần cứng<br>- Tài liệu phong phú<br>- Tối ưu cho xử lý thời gian thực |
| **dlib** | 19.22 | Phát hiện mặt, điểm mốc mặt (68 điểm) | - Độ chính xác cao cho phát hiện mặt<br>- Có sẵn mô hình đã huấn luyện<br>- Hoạt động tốt với ảnh IR<br>- Backend C++ hiệu quả |

#### **Thư viện Học máy**

| Công nghệ | Phiên bản | Mục đích | Lý do lựa chọn |
|------------|---------|---------|---------------|
| **TensorFlow Lite** | 2.8 | Suy luận nhận diện hành động | - Tối ưu cho thiết bị biên<br>- Tăng tốc GPU trên Jetson Nano<br>- Kích thước mô hình nhỏ<br>- Hiệu năng tốt trên ARM |
| **NumPy** | 1.21 | Thao tác mảng, tính toán số học | - Tiêu chuẩn cho tính toán số học trong Python<br>- Thao tác mảng nhanh<br>- Được OpenCV và TensorFlow sử dụng |
| **SciPy** | 1.7 | Xử lý tín hiệu, lọc dữ liệu | - Lọc theo thời gian (trung bình trượt)<br>- Các hàm thống kê<br>- Làm mượt tín hiệu |

#### **Lưu trữ dữ liệu**

| Công nghệ | Phiên bản | Mục đích | Lý do lựa chọn |
|------------|---------|---------|---------------|
| **SQLite3** | 3.x (sẵn có) | CSDL cho sự kiện, nhật ký | - Không cần máy chủ (nhúng trực tiếp)<br>- Dạng tệp (dễ di chuyển)<br>- Tuân thủ ACID<br>- Đủ dùng cho hệ thống đơn người dùng |
| **PyYAML** | 6.0 | Đọc tệp cấu hình | - Định dạng dễ đọc với con người<br>- Dễ dàng chỉnh sửa các ngưỡng<br>- Tiêu chuẩn cho cấu hình Python |

#### **Giao tiếp phần cứng**

| Công nghệ | Phiên bản | Mục đích | Lý do lựa chọn |
|------------|---------|---------|---------------|
| **RPi.GPIO / Jetson.GPIO** | Mới nhất | Điều khiển GPIO cho LED | - Thư viện chính thức để truy cập GPIO<br>- API đơn giản<br>- Độ tin cậy cao |
| **pygame** | 2.1 | Phát âm thanh cảnh báo | - API âm thanh đơn giản<br>- Đa nền tảng<br>- Không phụ thuộc vào máy chủ âm thanh hệ thống |

#### **Công cụ phát triển & triển khai**

| Công nghệ | Phiên bản | Mục đích | Lý do lựa chọn |
|------------|---------|---------|---------------|
| **Git** | 2.x | Quản lý phiên bản | - Tiêu chuẩn quản lý mã nguồn<br>- Sao lưu và cộng tác |
| **pytest** | 7.x | Kiểm thử đơn vị (Unit testing) | - Khung kiểm thử đơn giản, kiểu Python<br>- Hệ sinh thái plugin tốt |
| **black** | 22.x | Định dạng mã nguồn | - Phong cách mã thống nhất<br>- Định dạng tự động |

### 9.3 Các mô hình đã huấn luyện sẵn

| Mô hình | Nguồn | Mục đích | Kích thước | Định dạng |
|-------|--------|---------|------|--------|
| **Phát hiện 68 điểm mốc mặt** | dlib | Phát hiện điểm mốc khuôn mặt | 99.7 MB | tệp `.dat` |
| **MobileNetV2 SSD** | TF Model Zoo | Phát hiện tay | 18 MB | `.tflite` |
| **Phân loại hành động tùy chỉnh** | Tự huấn luyện | Nhận diện hành động (7 lớp) | 12 MB | `.tflite` |

**Huấn luyện mô hình (cho bộ phân loại hành động tùy chỉnh):**
- Bộ dữ liệu: Tự thu thập + ảnh tăng cường (200 ảnh mỗi lớp × 7 lớp).
- Kiến trúc: MobileNetV2 (transfer learning).
- Huấn luyện: TensorFlow/Keras trên máy tính bàn có GPU.
- Chuyển đổi: TensorFlow → TensorFlow Lite (lượng tử hóa cho thiết bị biên).

---

## 10. THIẾT KẾ CHI TIẾT THÀNH PHẦN

### 10.1 Các thành phần phát hiện

#### **10.1.1 Thành phần Phát hiện khuôn mặt (Face Detector)**

**Trách nhiệm:** Phát hiện khuôn mặt tài xế và trích xuất 68 điểm mốc mặt.

**Thuật toán:** Bộ phát hiện mặt dựa trên HOG của dlib + Shape Predictor.

**Thiết kế lớp:**

```python
class FaceDetector:
    """
    Phát hiện khuôn mặt và trích xuất 68 điểm mốc bằng dlib.
    """
    
    def __init__(self, model_path: str):
        """
        Khởi tạo bộ phát hiện mặt.
        
        Args:
            model_path: Đường dẫn tới shape_predictor_68_face_landmarks.dat
        """
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor(model_path)
        self.no_face_counter = 0
        self.no_face_threshold = 30  # khung hình (1 giây ở 30fps)
    
    def detect_face(self, frame: np.ndarray) -> Tuple[Optional[dlib.rectangle], 
                                                       Optional[np.ndarray]]:
        """
        Phát hiện mặt và trả về khung bao và các điểm mốc.
        
        Args:
            frame: Khung hình đầu vào (ảnh xám, np.ndarray)
        
        Returns:
            face_rect: dlib.rectangle hoặc None nếu không có mặt
            landmarks: mảng np.ndarray kích thước (68, 2) hoặc None
        """
        faces = self.detector(frame, 0)  # 0 = không nâng mẫu (upsampling)
        
        if len(faces) == 0:
            self.no_face_counter += 1
            return None, None
        
        # Reset biến đếm khi thấy mặt
        self.no_face_counter = 0
        
        # Lấy khuôn mặt đầu tiên (giả định chỉ có một tài xế)
        face = faces[0]
        
        # Lấy các điểm mốc
        shape = self.predictor(frame, face)
        landmarks = np.array([[p.x, p.y] for p in shape.parts()])
        
        return face, landmarks
    
    def is_no_face_alert_required(self) -> bool:
        """Kiểm tra xem có cần kích hoạt cảnh báo không thấy mặt không."""
        return self.no_face_counter >= self.no_face_threshold
```

**Các tham số chính:**
- `upsampling_factor = 0`: Đánh đổi giữa tốc độ và khả năng phát hiện (0 = nhanh nhất).
- `no_face_threshold = 30`: số khung hình (có thể cấu hình).

**Đầu ra:**
- Khung bao mặt: `dlib.rectangle` với (trái, trên, phải, dưới).
- Các điểm mốc: Mảng NumPy kích thước (68, 2) với tọa độ (x, y).

**Chỉ số các điểm mốc (mô hình 68 điểm của dlib):**
- Hàm: 0-16
- Lông mày phải: 17-21
- Lông mày trái: 22-26
- Mũi: 27-35
- Mắt phải: 36-41
- Mắt trái: 42-47
- Môi ngoài: 48-59
- Môi trong: 60-67

---

#### **10.1.2 Thành phần Theo dõi mắt (Eye Tracker)**

**Trách nhiệm:** Theo dõi mắt và tính toán Tỷ lệ khung hình mắt (Eye Aspect Ratio - EAR) để phát hiện nháy mắt và nhắm mắt.

**Thuật toán:** Tính toán EAR dựa trên hình học sử dụng các điểm mốc vùng mắt.

**Thiết kế lớp:**

```python
class EyeTracker:
    """
    Theo dõi mắt và tính EAR phục vụ phát hiện buồn ngủ.
    """
    
    # Chỉ số các điểm mốc cho mắt
    LEFT_EYE_INDICES = list(range(42, 48))   # 42-47
    RIGHT_EYE_INDICES = list(range(36, 42))  # 36-41
    
    def __init__(self, ear_threshold: float = 0.25, 
                 blink_threshold: int = 3):
        """
        Khởi tạo bộ theo dõi mắt.
        
        Args:
            ear_threshold: EAR dưới giá trị này nghĩa là mắt nhắm
            blink_threshold: Số khung hình liên tiếp EAR thấp = một lần nháy
        """
        self.ear_threshold = ear_threshold
        self.blink_threshold = blink_threshold
        self.blink_counter = 0
        self.total_blinks = 0
    
    def track_eyes(self, landmarks: np.ndarray) -> Tuple[float, float]:
        """
        Theo dõi mắt và tính EAR cho cả hai mắt.
        
        Args:
            landmarks: Mảng các điểm mốc khuôn mặt (68, 2)
        
        Returns:
            left_ear: EAR của mắt trái
            right_ear: EAR của mắt phải
        """
        left_eye = landmarks[self.LEFT_EYE_INDICES]
        right_eye = landmarks[self.RIGHT_EYE_INDICES]
        
        left_ear = self._compute_ear(left_eye)
        right_ear = self._compute_ear(right_eye)
        
        # EAR trung bình
        avg_ear = (left_ear + right_ear) / 2.0
        
        # Phát hiện nháy mắt
        if avg_ear < self.ear_threshold:
            self.blink_counter += 1
        else:
            if self.blink_counter >= self.blink_threshold:
                self.total_blinks += 1
            self.blink_counter = 0
        
        return left_ear, right_ear
    
    def _compute_ear(self, eye: np.ndarray) -> float:
        """
        Tính toán Tỷ lệ khung hình mắt (EAR).
        
        Công thức:
            EAR = (||p2 - p6|| + ||p3 - p5||) / (2 * ||p1 - p4||)
        
        Trong đó p1-p6 là các điểm mốc vùng mắt (6 điểm mỗi mắt).
        
        Args:
            eye: Các điểm mốc vùng mắt (6, 2)
        
        Returns:
            ear: Tỷ lệ khung hình mắt (float)
        """
        # Khoảng cách dọc
        v1 = np.linalg.norm(eye[1] - eye[5])  # p2 - p6
        v2 = np.linalg.norm(eye[2] - eye[4])  # p3 - p5
        
        # Khoảng cách ngang
        h = np.linalg.norm(eye[0] - eye[3])   # p1 - p4
        
        # EAR
        ear = (v1 + v2) / (2.0 * h)
        
        return ear
    
    def get_blink_count(self) -> int:
        """Lấy tổng số lần nháy mắt đã phát hiện."""
        return self.total_blinks
    
    def reset_blink_count(self):
        """Reset bộ đếm nháy mắt (gọi khi bắt đầu mỗi chuyến đi)."""
        self.total_blinks = 0
```

**Giải thích công thức EAR:**

```
      p2
    p1  p3
    p6  p4
      p5

EAR = (khoảng_cách_dọc_1 + khoảng_cách_dọc_2) / (2 * khoảng_cách_ngang)
```

- **Mắt mở bình thường**: EAR ≈ 0.3 - 0.4.
- **Mắt nhắm một phần**: EAR ≈ 0.15 - 0.25.
- **Mắt nhắm hoàn toàn**: EAR ≈ 0.05 - 0.15.

**Các ngưỡng chính:**
- `ear_threshold = 0.25`: Dưới mức này = mắt nhắm.
- `blink_threshold = 3`: Số khung hình liên tiếp EAR < ngưỡng = tính là một lần nháy.

---

#### **10.1.3 Thành phần Ước tính tư thế đầu (Head Pose Estimator)**

**Trách nhiệm:** Ước tính tư thế đầu 3D (pitch, yaw, roll) để phát hiện chuyển động đầu.

**Thuật toán:** solvePnP (Perspective-n-Point) sử dụng các điểm mốc mặt và mô hình đầu 3D.

**Thiết kế lớp:**

```python
class HeadPoseEstimator:
    """
    Ước tính tư thế đầu 3D (pitch, yaw, roll) bằng solvePnP.
    """
    
    def __init__(self, frame_width: int = 640, frame_height: int = 480):
        """
        Khởi tạo bộ ước tính tư thế đầu.
        
        Args:
            frame_width: Chiều rộng khung hình camera
            frame_height: Chiều cao khung hình camera
        """
        # Các điểm mô hình 3D (mô hình mặt phổ thông đơn vị cm)
        self.model_points = np.array([
            (0.0, 0.0, 0.0),             # Đỉnh mũi (30)
            (0.0, -330.0, -65.0),        # Cằm (8)
            (-225.0, 170.0, -135.0),     # Khóe mắt trái (45)
            (225.0, 170.0, -135.0),      # Khóe mắt phải (36)
            (-150.0, -150.0, -125.0),    # Khóe miệng trái (54)
            (150.0, -150.0, -125.0)      # Khóe miệng phải (48)
        ], dtype=np.float64)
        
        # Ma trận camera (giả định không có méo ống kính)
        focal_length = frame_width
        center = (frame_width / 2, frame_height / 2)
        self.camera_matrix = np.array([
            [focal_length, 0, center[0]],
            [0, focal_length, center[1]],
            [0, 0, 1]
        ], dtype=np.float64)
        
        # Giả định không có méo ống kính
        self.dist_coeffs = np.zeros((4, 1))
    
    def estimate_pose(self, landmarks: np.ndarray) -> Tuple[float, float, float]:
        """
        Ước tính các góc tư thế đầu.
        
        Args:
            landmarks: Các điểm mốc mặt (68, 2)
        
        Returns:
            pitch: Góc quay lên/xuống (độ)
            yaw: Góc quay trái/phải (độ)
            roll: Góc nghiêng (độ)
        """
        # Các điểm ảnh 2D từ điểm mốc
        image_points = np.array([
            landmarks[30],  # Đỉnh mũi
            landmarks[8],   # Cằm
            landmarks[45],  # Khóe mắt trái
            landmarks[36],  # Khóe mắt phải
            landmarks[54],  # Khóe miệng trái
            landmarks[48]   # Khóe miệng phải
        ], dtype=np.float64)
        
        # Giải bài toán PnP
        success, rotation_vec, translation_vec = cv2.solvePnP(
            self.model_points,
            image_points,
            self.camera_matrix,
            self.dist_coeffs,
            flags=cv2.SOLVEPNP_ITERATIVE
        )
        
        # Chuyển đổi vector quay sang ma trận quay
        rotation_mat, _ = cv2.Rodrigues(rotation_vec)
        
        # Phân rã ma trận quay sang các góc Euler
        pose_mat = cv2.hconcat((rotation_mat, translation_vec))
        _, _, _, _, _, _, euler_angles = cv2.decomposeProjectionMatrix(pose_mat)
        
        pitch = euler_angles[0][0]
        yaw = euler_angles[1][0]
        roll = euler_angles[2][0]
        
        return pitch, yaw, roll
    
    def is_head_turned(self, yaw: float, threshold: float = 30.0) -> bool:
        """Kiểm tra xem đầu có quay sang trái/phải quá mức không."""
        return abs(yaw) > threshold
    
    def is_head_down(self, pitch: float, threshold: float = 20.0) -> bool:
        """Kiểm tra xem đầu có gục xuống không (dấu hiệu buồn ngủ)."""
        return pitch > threshold
```

**Các góc tư thế đầu:**
- **Pitch (Quay quanh trục X)**: 
  - Dương = đầu gục xuống.
  - Âm = đầu ngẩng lên.
  - Phạm vi bình thường: -10° đến +10°.
  - Chỉ số buồn ngủ: > +20°.
  
- **Yaw (Quay quanh trục Y)**: 
  - Dương = đầu quay sang phải.
  - Âm = đầu quay sang trái.
  - Phạm vi bình thường: -15° đến +15°.
  - Chỉ số xao nhãng: > ±30°.
  
- **Roll (Quay quanh trục Z)**: 
  - Dương = đầu nghiêng sang phải.
  - Âm = đầu nghiêng sang trái.
  - Phạm vi bình thường: -10° đến +10°.

---

#### **10.1.4 Thành phần Theo dõi ánh mắt (Gaze Tracker)**

**Trách nhiệm:** Theo dõi hướng nhìn để phát hiện xem tài xế đang nhìn đi đâu.

**Thuật toán:** Vị trí con ngươi tương đối so với khóe mắt (cách tiếp cận hình học).

**Thiết kế lớp:**

```python
class GazeTracker:
    """
    Theo dõi hướng nhìn dựa trên vị trí con ngươi trong vùng mắt.
    """
    
    LEFT_EYE_INDICES = list(range(42, 48))
    RIGHT_EYE_INDICES = list(range(36, 42))
    
    def __init__(self):
        """Khởi tạo bộ theo dõi ánh mắt."""
        self.gaze_history = []  # Lưu các vị trí nhìn gần đây để làm mượt
        self.history_size = 5
    
    def track_gaze(self, frame: np.ndarray, 
                   landmarks: np.ndarray) -> Tuple[float, float]:
        """
        Theo dõi hướng nhìn.
        
        Args:
            frame: Khung hình ảnh xám
            landmarks: Các điểm mốc khuôn mặt (68, 2)
        
        Returns:
            gaze_x: Tỷ lệ nhìn ngang (-1=trái, 0=giữa, +1=phải)
            gaze_y: Tỷ lệ nhìn dọc (-1=trên, 0=giữa, +1=dưới)
        """
        left_eye = landmarks[self.LEFT_EYE_INDICES]
        right_eye = landmarks[self.RIGHT_EYE_INDICES]
        
        # Trích xuất vùng mắt (ROI)
        left_roi = self._extract_eye_roi(frame, left_eye)
        right_roi = self._extract_eye_roi(frame, right_eye)
        
        # Tìm tâm con ngươi trong mỗi mắt
        left_gaze = self._find_iris_center(left_roi, left_eye)
        right_gaze = self._find_iris_center(right_roi, right_eye)
        
        # Trung bình hướng nhìn trái và phải
        gaze_x = (left_gaze[0] + right_gaze[0]) / 2.0
        gaze_y = (left_gaze[1] + right_gaze[1]) / 2.0
        
        # Làm mượt bằng lịch sử
        self.gaze_history.append((gaze_x, gaze_y))
        if len(self.gaze_history) > self.history_size:
            self.gaze_history.pop(0)
        
        smoothed_gaze = np.mean(self.gaze_history, axis=0)
        
        return smoothed_gaze[0], smoothed_gaze[1]
    
    def _extract_eye_roi(self, frame: np.ndarray, 
                         eye_landmarks: np.ndarray) -> np.ndarray:
        """Trích xuất vùng mắt quan tâm (ROI)."""
        # Lấy khung bao
        x_min = int(np.min(eye_landmarks[:, 0]))
        x_max = int(np.max(eye_landmarks[:, 0]))
        y_min = int(np.min(eye_landmarks[:, 1]))
        y_max = int(np.max(eye_landmarks[:, 1]))
        
        # Thêm lề (padding)
        padding = 5
        x_min = max(0, x_min - padding)
        y_min = max(0, y_min - padding)
        x_max = min(frame.shape[1], x_max + padding)
        y_max = min(frame.shape[0], y_max + padding)
        
        roi = frame[y_min:y_max, x_min:x_max]
        return roi
    
    def _find_iris_center(self, eye_roi: np.ndarray, 
                          eye_landmarks: np.ndarray) -> Tuple[float, float]:
        """
        Tìm tâm con ngươi bằng phân ngưỡng và tìm đường bao.
        
        Returns:
            gaze_ratio_x, gaze_ratio_y (-1 đến +1)
        """
        # Phân ngưỡng để tách con ngươi (vùng tối nhất)
        _, threshold = cv2.threshold(eye_roi, 50, 255, cv2.THRESH_BINARY_INV)
        
        # Tìm các đường bao
        contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, 
                                       cv2.CHAIN_APPROX_SIMPLE)
        
        if not contours:
            return (0.0, 0.0)  # Mặc định nhìn thẳng nếu không tìm thấy
        
        # Lấy đường bao lớn nhất (con ngươi)
        iris_contour = max(contours, key=cv2.contourArea)
        
        # Tính tâm con ngươi (Moments)
        M = cv2.moments(iris_contour)
        if M["m00"] != 0:
            iris_x = M["m10"] / M["m00"]
            iris_y = M["m01"] / M["m00"]
        else:
            return (0.0, 0.0)
        
        # Tính chiều rộng/cao vùng mắt
        eye_width = np.max(eye_landmarks[:, 0]) - np.min(eye_landmarks[:, 0])
        eye_height = np.max(eye_landmarks[:, 1]) - np.min(eye_landmarks[:, 1])
        
        # Tính tỷ lệ hướng nhìn (-1 đến +1)
        gaze_ratio_x = (iris_x - eye_roi.shape[1] / 2) / (eye_width / 2)
        gaze_ratio_y = (iris_y - eye_roi.shape[0] / 2) / (eye_height / 2)
        
        # Giới hạn trong khoảng [-1, 1]
        gaze_ratio_x = np.clip(gaze_ratio_x, -1.0, 1.0)
        gaze_ratio_y = np.clip(gaze_ratio_y, -1.0, 1.0)
        
        return (gaze_ratio_x, gaze_ratio_y)
    
    def is_looking_away(self, gaze_x: float, gaze_y: float, 
                       threshold: float = 0.4) -> bool:
        """Kiểm tra xem hướng nhìn có lệch xa trung tâm không."""
        return abs(gaze_x) > threshold or abs(gaze_y) > threshold
```

**Diễn giải hướng nhìn:**
- `gaze_x`:
  - `-1.0`: Nhìn xa sang trái.
  - `0.0`: Nhìn thẳng về phía trước.
  - `+1.0`: Nhìn xa sang phải.
- `gaze_y`:
  - `-1.0`: Nhìn lên trên.
  - `0.0`: Nhìn thẳng.
  - `+1.0`: Nhìn xuống dưới.

**Ngưỡng cho "nhìn đi chỗ khác"**: `|gaze_x| > 0.4` hoặc `|gaze_y| > 0.4`.

---

### 10.2 Các thành phần phân tích

#### **10.2.1 Thành phần Phân tích buồn ngủ (Drowsiness Analyzer)**

**Trách nhiệm:** Phân tích mức độ buồn ngủ dựa trên dữ liệu mắt, miệng và đầu.

**Thuật toán:** Tính điểm buồn ngủ đa yếu tố sử dụng PERCLOS, MAR, tần suất nháy mắt và tư thế đầu.

**Thiết kế lớp:**

```python
class DrowsinessAnalyzer:
    """
    Phân tích sự buồn ngủ của tài xế qua nhiều chỉ số.
    """
    
    def __init__(self):
        """Khởi tạo bộ phân tích buồn ngủ."""
        self.ear_history = []
        self.mar_history = []
        self.history_duration = 60  # khung hình (2 giây ở 30fps)
        
        # Các ngưỡng (có thể cấu hình qua tệp config)
        self.perclos_threshold = 0.8  # 80% thời gian nhắm mắt
        self.mar_yawn_threshold = 0.6
        self.drowsy_ear_threshold = 0.25
        self.drowsy_duration_threshold = 30  # khung hình
    
    def analyze_drowsiness(self, left_ear: float, right_ear: float,
                          mar: float, pitch: float) -> Dict[str, Any]:
        """
        Phân tích mức độ buồn ngủ.
        
        Args:
            left_ear: EAR mắt trái
            right_ear: EAR mắt phải
            mar: Tỷ lệ khung hình miệng (MAR)
            pitch: Góc gục đầu (độ)
        
        Returns:
            analysis_result: Dict chứa:
                - drowsiness_level: 0-100 (int)
                - is_drowsy: bool
                - perclos: float (0-1)
                - yawn_detected: bool (ngáp)
                - microsleep_detected: bool (ngủ gật)
        """
        avg_ear = (left_ear + right_ear) / 2.0
        
        # Cập nhật lịch sử
        self.ear_history.append(avg_ear)
        self.mar_history.append(mar)
        
        if len(self.ear_history) > self.history_duration:
            self.ear_history.pop(0)
            self.mar_history.pop(0)
        
        # Tính PERCLOS (Phần trăm thời gian nhắm mắt)
        perclos = self._compute_perclos()
        
        # Phát hiện ngáp
        yawn_detected = mar > self.mar_yawn_threshold
        
        # Phát hiện ngủ gật (nhắm mắt liên tục thời gian dài)
        microsleep_detected = self._detect_microsleep()
        
        # Phát hiện gục đầu
        head_down = pitch > 20.0
        
        # Tính toán mức độ buồn ngủ (0-100)
        drowsiness_level = 0
        
        if perclos > 0.8:
            drowsiness_level += 40
        elif perclos > 0.5:
            drowsiness_level += 20
        
        if yawn_detected:
            drowsiness_level += 20
        
        if microsleep_detected:
            drowsiness_level += 30
        
        if head_down:
            drowsiness_level += 10
        
        drowsiness_level = min(100, drowsiness_level)
        
        # Xác định xem có bị coi là buồn ngủ không
        is_drowsy = drowsiness_level >= 60 or microsleep_detected
        
        return {
            'drowsiness_level': drowsiness_level,
            'is_drowsy': is_drowsy,
            'perclos': perclos,
            'yawn_detected': yawn_detected,
            'microsleep_detected': microsleep_detected,
            'head_down': head_down
        }
    
    def _compute_perclos(self) -> float:
        """Tính toán chỉ số PERCLOS."""
        if len(self.ear_history) == 0:
            return 0.0
        
        closed_count = sum(1 for ear in self.ear_history 
                          if ear < self.drowsy_ear_threshold)
        perclos = closed_count / len(self.ear_history)
        
        return perclos
    
    def _detect_microsleep(self) -> bool:
        """Phát hiện ngủ gật (nhắm mắt >1 giây liên tục)."""
        if len(self.ear_history) < self.drowsy_duration_threshold:
            return False
        
        # Kiểm tra N khung hình gần nhất có nhắm mắt không
        recent_ear = self.ear_history[-self.drowsy_duration_threshold:]
        closed_frames = sum(1 for ear in recent_ear 
                           if ear < self.drowsy_ear_threshold)
        
        # Coi là ngủ gật nếu nhắm mắt >90% số khung hình gần đây
        return closed_frames >= (0.9 * self.drowsy_duration_threshold)
```

**Các chỉ số buồn ngủ:**

| Chỉ số | Ngưỡng | Trọng số | Ghi chú |
|-----------|-----------|--------|-------|
| **PERCLOS > 80%** | 80% thời gian nhắm mắt | +40 điểm | Chỉ số rất mạnh |
| **PERCLOS > 50%** | 50% thời gian nhắm mắt | +20 điểm | Chỉ số trung bình |
| **Ngáp** | MAR > 0.6 | +20 điểm | Dấu hiệu mệt mỏi |
| **Ngủ gật** | Nhắm mắt >1 giây | +30 điểm | Chỉ số nguy kịch |
| **Gục đầu** | Pitch > 20° | +10 điểm | Mất tư thế tỉnh táo |

**Thang mức độ buồn ngủ:**
- **0-30**: Tỉnh táo (Xanh)
- **31-59**: Buồn ngủ nhẹ (Vàng)
- **60-100**: Buồn ngủ - Cần cảnh báo ngay (Đỏ)

---

Tài liệu tiếp tục với các phần còn lại từ 10.2.2 đến 15...

