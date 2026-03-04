# Tập Hợp Sản Phẩm - Hệ Thống Giám Sát Tài Xế

**Dự Án:** Hệ Thống Giám Sát Tài Xế (DMS) - Đồ Án Tốt Nghiệp  
**Tạo:** 2026-03-04  
**Nguồn:** Phiên Brainstorming 2026-03-03-004815  
**Tổng Mục:** 45 Mục Tập Hợp Sản Phẩm (PBIs)  

---

## Mục Lục

1. [Tổng Quan Tập Hợp Sản Phẩm](#tổng-quan-tập-hợp-sản-phẩm)
2. [Ma Trận Phân Tích Hình Thái](#ma-trận-phân-tích-hình-thái)
3. [Mục Tập Hợp Sản Phẩm Theo Danh Mục](#mục-tập-hợp-sản-phẩm-theo-danh-mục)
4. [Tóm Tắt Ưu Tiên MoSCoW](#tóm-tắt-ưu-tiên-moscow)
5. [Công Nghệ Sử Dụng](#công-nghệ-sử-dụng)

---

## Tổng Quan Tập Hợp Sản Phẩm

Tập hợp sản phẩm này được tạo bằng kỹ thuật **Phân Tích Hình Thái** để khám phá và phân loại một cách có hệ thống tất cả các tính năng của Hệ Thống Giám Sát Tài Xế.

### Thống Kê Tóm Tắt

- **Tổng PBIs:** 45 tính năng
- **Danh Mục Chức Năng:** 13 khu vực
- **Chia Theo MoSCoW:**
  - **PHẢI CÓ:** 24 mục (tính năng MVP cốt lõi)
  - **NÊN CÓ:** 17 mục (cải tiến quan trọng)
  - **CÓ THỂ CÓ:** 4 mục (tính năng tốt là có)
  - **KHÔNG CÓ:** Phát hiện dây an toàn (loại bỏ theo quyết định phạm vi)

---

## Ma Trận Phân Tích Hình Thái

Ma trận 4 chiều sau đây được sử dụng để khám phá một cách có hệ thống tất cả các tính năng có thể:

| Chiều | Tùy Chọn |
|-------|---------|
| **1. Loại Phát Hiện** | Phát Hiện Mặt, Giám Sát Mắt, Giám Sát Đầu, Theo Dõi Hướng Nhìn, Phát Hiện Ngủ Gật, Phát Hiện Bị Phân Tán, Nhận Dạng Hoạt Động, Đếm Hành Khách, Sức Khỏe Hệ Thống, Đăng Ký Tài Xế |
| **2. Thực Thể Được Giám Sát** | Chỉ Tài Xế, Tài Xế + Hành Khách, Camera/Hệ Thống |
| **3. Lớp Công Nghệ** | Thị Giác Máy Tính (CV), Hồng Ngoại (IR), Mô Hình AI/ML, Logic Dựa Trên Quy Tắc, Tích Hợp Phần Cứng |
| **4. Đầu Ra/Hành Động** | Cảnh Báo Theo Thời Gian Thực, Ghi Lại/Ghi Video, Hiển Thị Bảng Điều Khiển, Phân Tích/Báo Cáo |

---

## Mục Tập Hợp Sản Phẩm Theo Danh Mục

### Danh Mục 1: Phát Hiện Mặt & Mắt Cốt Lõi (Nền Tảng)

> **Mục Đích:** Lớp nền tảng cho tất cả các khả năng giám sát tài xế. Phải phát hiện và theo dõi các tính năng khuôn mặt một cách đáng tin cậy.

---

#### PBI-001: Phát Hiện & Theo Dõi Mặt

- **Ưu Tiên:** PHẢI CÓ
- **Mô Tả:** Phát hiện và theo dõi khuôn mặt tài xế theo thời gian thực bằng camera IR
- **Công Nghệ:** Thị Giác Máy Tính (dlib/MediaPipe) + Camera IR
- **Thực Thể Được Giám Sát:** Chỉ Tài Xế
- **Đầu Ra:** Hộp giới hạn mặt, điểm mốc khuôn mặt (68 điểm)
- **Phụ Thuộc:** Không (tính năng nền tảng)
- **Tiêu Chí Thành Công:**
  - Độ tin cậy phát hiện mặt >90%
  - Phát hiện hoạt động trong mọi điều kiện ánh sáng (ngày/đêm) với camera IR
  - Trích xuất 68 điểm mốc khuôn mặt thành công
  - Tốc độ khung hình: tối thiểu 15 FPS

---

#### PBI-002: Phát Hiện Vùng Mắt

- **Ưu Tiên:** PHẢI CÓ
- **Mô Tả:** Phát hiện vùng mắt trái và phải từ điểm mốc khuôn mặt
- **Công Nghệ:** Thị Giác Máy Tính (điểm mốc khuôn mặt dlib)
- **Thực Thể Được Giám Sát:** Chỉ Tài Xế
- **Đầu Ra:** Hộp giới hạn mắt, điểm mốc mắt
- **Phụ Thuộc:** PBI-001 (yêu cầu phát hiện mặt)
- **Tiêu Chí Thành Công:**
  - Cả hai mắt được phát hiện với độ chính xác >95% khi khuôn mặt có thể nhìn thấy
  - Trích xuất điểm mốc mắt (6 điểm mỗi mắt)
  - Xử lý che khuất một phần (một mắt có thể nhìn thấy)

---

#### PBI-003: Phát Hiện Mắt Mở

- **Ưu Tiên:** PHẢI CÓ
- **Mô Tả:** Tính toán Eye Aspect Ratio (EAR) để xác định mắt mở/đóng
- **Công Nghệ:** Logic Dựa Trên Quy Tắc (tính toán EAR từ điểm mốc mắt)
- **Thực Thể Được Giám Sát:** Chỉ Tài Xế
- **Đầu Ra:** Giá trị EAR (trái, phải, trung bình), trạng thái mở/đóng
- **Phụ Thuộc:** PBI-002 (yêu cầu điểm mốc mắt)
- **Tiêu Chí Thành Công:**
  - Tính toán EAR chính xác đến 2 số thập phân
  - Ngưỡng phân loại mở/đóng: EAR < 0,25 = đóng
  - Hoạt động với kính mắt (cải tiến PBI-032)

---

#### PBI-004: Giám Sát Tần Suất Chớp Mắt

- **Ưu Tiên:** PHẢI CÓ
- **Mô Tả:** Đếm chớp mắt mỗi phút để phát hiện các mô hình bất thường (chỉ báo ngủ gật)
- **Công Nghệ:** Logic Dựa Trên Quy Tắc (phát hiện ngưỡng EAR)
- **Thực Thể Được Giám Sát:** Chỉ Tài Xế
- **Đầu Ra:** Chớp mắt mỗi phút, trung bình thời lượng chớp mắt
- **Phụ Thuộc:** PBI-003 (yêu cầu tính toán EAR)
- **Tiêu Chí Thành Công:**
  - Phát hiện chớp mắt: EAR giảm dưới 0,25 trong 100-400ms
  - Đếm chớp mắt chính xác trong cửa sổ lăn 60 giây
  - Phạm vi bình thường: 15-20 chớp mắt/phút; Thấp: <10 (ngủ gật); Cao: >30 (căng thẳng)

---

#### PBI-005: Theo Dõi Vị Trí Mắt

- **Ưu Tiên:** PHẢI CÓ
- **Mô Tả:** Theo dõi vị trí mắt trong vùng khuôn mặt để ước tính hướng nhìn
- **Công Nghệ:** Thị Giác Máy Tính (phát hiện học sinh)
- **Thực Thể Được Giám Sát:** Chỉ Tài Xế
- **Đầu Ra:** Tọa độ tâm mắt (x, y)
- **Phụ Thuộc:** PBI-002 (yêu cầu vùng mắt)
- **Tiêu Chí Thành Công:**
  - Tâm học sinh được xác định với độ chính xác ±3 pixel
  - Cập nhật ở tốc độ khung hình (tối thiểu 15-20 Hz)
  - Nền tảng để ước tính hướng nhìn (PBI-009)

---

### Danh Mục 2: Posture & Hướng Đầu

> **Mục Đích:** Theo dõi chuyển động đầu để phát hiện bị phân tán chú ý, kết hợp với hướng nhìn để giám sát sự chú ý mạnh mẽ.

---

#### PBI-006: Ước Tính Posture Đầu

- **Ưu Tiên:** PHẢI CÓ
- **Mô Tả:** Ước tính hướng đầu (pitch, yaw, roll) từ điểm mốc khuôn mặt bằng ước tính posture 3D
- **Công Nghệ:** Thị Giác Máy Tính (thuật toán solvePnP)
- **Thực Thể Được Giám Sát:** Chỉ Tài Xế
- **Đầu Ra:** Góc Euler (pitch, yaw, roll theo độ)
- **Phụ Thuộc:** PBI-001 (yêu cầu điểm mốc khuôn mặt)
- **Tiêu Chí Thành Công:**
  - Các góc Pitch/Yaw/Roll được tính toán với độ chính xác ±5°
  - Phạm vi: Yaw ±90°, Pitch ±60°, Roll ±45°
  - Tốc độ cập nhật: 15+ Hz

---

#### PBI-007: Theo Dõi Vị Trí Đầu

- **Ưu Tiên:** PHẢI CÓ
- **Mô Tả:** Theo dõi vị trí đầu trong khung hình camera (trái, giữa, phải, trên, dưới)
- **Công Nghệ:** Thị Giác Máy Tính (theo dõi trọng tâm mặt)
- **Thực Thể Được Giám Sát:** Chỉ Tài Xế
- **Đầu Ra:** Vùng vị trí đầu (9 vùng: giữa, trái, phải, trên, dưới, kết hợp)
- **Phụ Thuộc:** PBI-001 (yêu cầu hộp giới hạn mặt)
- **Tiêu Chí Thành Công:**
  - Phân loại lưới 9 vùng (3x3: trái/giữa/phải × trên/giữa/dưới)
  - Cập nhật vị trí theo thời gian thực

---

#### PBI-008: Phân Loại Vùng Đầu

- **Ưu Tiên:** PHẢI CÓ
- **Mô Tả:** Phân loại posture đầu thành các vùng có ý nghĩa (nhìn về phía trước, quay trái/phải, nhìn xuống)
- **Công Nghệ:** Logic Dựa Trên Quy Tắc (ngưỡng góc posture đầu)
- **Thực Thể Được Giám Sát:** Chỉ Tài Xế
- **Đầu Ra:** Nhãn vùng (Phía Trước, Trái, Phải, Xuống, Góc Cực)
- **Phụ Thuộc:** PBI-006 (yêu cầu góc posture đầu)
- **Tiêu Chí Thành Công:**
  - Vùng phía trước: Yaw ±20°, Pitch ±15°
  - Trái/Phải: Yaw >±20°
  - Xuống: Pitch <-15° (nhìn vào điện thoại/bảng điều khiển)
  - Cực: Yaw >±60° hoặc Pitch >±45° (bị phân tán nghiêm trọng)

---

### Danh Mục 3: Theo Dõi Hướng Nhìn Mắt

> **Mục Đích:** Hướng nhìn chính xác để phát hiện tài xế đang nhìn vào đâu (đường, gương, điện thoại, hành khách).

---

#### PBI-009: Ước Tính Hướng Nhìn

- **Ưu Tiên:** PHẢI CÓ
- **Mô Tả:** Ước tính vectơ hướng nhìn từ điểm mốc mắt và vị trí học sinh
- **Công Nghệ:** Thị Giác Máy Tính (thuật toán ước tính hướng nhìn) + AI/ML
- **Thực Thể Được Giám Sát:** Chỉ Tài Xế
- **Đầu Ra:** Vectơ hướng nhìn (hướng 3D), góc hướng nhìn
- **Phụ Thuộc:** PBI-005 (yêu cầu vị trí học sinh), PBI-006 (yêu cầu posture đầu để hiệu chỉnh)
- **Tiêu Chí Thành Công:**
  - Độ chính xác góc hướng nhìn: ±5° (chấp nhận được cho phát hiện dựa trên vùng)
  - Hoạt động với hợp nhất posture đầu để ước tính mạnh mẽ
  - Xử lý giới hạn camera IR

---

#### PBI-010: Phân Loại Vùng Hướng Nhìn

- **Ưu Tiên:** PHẢI CÓ
- **Mô Tả:** Ánh xạ hướng nhìn thành các vùng cụ thể (đường phía trước, bảng điều khiển, gương bên, gương chiếu hậu, điện thoại/lòng, hành khách)
- **Công Nghệ:** Logic Dựa Trên Quy Tắc (ánh xạ góc hướng nhìn thành vùng)
- **Thực Thể Được Giám Sát:** Chỉ Tài Xế
- **Đầu Ra:** Nhãn vùng hướng nhìn, thời gian dừng lại mỗi vùng
- **Phụ Thuộc:** PBI-009 (yêu cầu hướng nhìn)
- **Tiêu Chí Thành Công:**
  - 6+ vùng được xác định: Đường, Bảng Điều Khiển, Gương Trái, Gương Phải, Gương Chiếu Hậu, Điện Thoại/Lòng, Hành Khách
  - Theo dõi thời gian dừng lại: thời gian tích lũy mỗi vùng trong cửa sổ 10 giây
  - Ngưỡng bị phân tán: >4 giây rời khỏi đường trong cửa sổ 10 giây

---

#### PBI-011: Phát Hiện & Theo Dõi Học Sinh

- **Ưu Tiên:** NÊN CÓ
- **Mô Tả:** Phát hiện và theo dõi vị trí học sinh để ước tính hướng nhìn chính xác (cải tiến PBI-005)
- **Công Nghệ:** Thị Giác Máy Tính (biến đổi Hough tròn hoặc học sâu - MediaPipe Iris)
- **Thực Thể Được Giám Sát:** Chỉ Tài Xế
- **Đầu Ra:** Tọa độ tâm học sinh, đường kính học sinh
- **Phụ Thuộc:** PBI-002 (yêu cầu vùng mắt)
- **Tiêu Chí Thành Công:**
  - Độ chính xác tâm học sinh: ±2 pixel
  - Đo được đường kính học sinh (hữu ích cho nghiên cứu căng thẳng/tải nhận thức - tương lai)
  - Cải thiện độ chính xác ước tính hướng nhìn từ ±5° thành ±3°

---

### Danh Mục 4: Phát Hiện Ngủ Gật

> **Mục Đích:** Phát hiện ngủ gật đa phương sử dụng đóng mắt, mô hình chớp mắt, ngáp, và số liệu thống kê.

---

#### PBI-012: Phát Hiện Ngủ Gật (dựa trên EAR)

- **Ưu Tiên:** PHẢI CÓ
- **Mô Tả:** Phát hiện ngủ gật bằng các giá trị EAR thấp kéo dài (mắt đóng lâu)
- **Công Nghệ:** Logic Dựa Trên Quy Tắc (ngưỡng EAR theo thời gian)
- **Thực Thể Được Giám Sát:** Chỉ Tài Xế
- **Đầu Ra:** Mức độ ngủ gật (bình thường, nhẹ, nặng), kích hoạt cảnh báo
- **Phụ Thuộc:** PBI-003 (yêu cầu giá trị EAR)
- **Tiêu Chí Thành Công:**
  - Ngủ gật nhẹ: EAR <0,25 trong 2-3 giây → cảnh báo
  - Ngủ gật nặng: EAR <0,25 trong >3 giây → cảnh báo quan trọng
  - Kết hợp với tỷ lệ chớp mắt (PBI-004) để mạnh mẽ
  - Mục tiêu: >90% độ chính xác phát hiện, <1 cảnh báo sai/giờ

---

#### PBI-013: Phát Hiện Ngáp

- **Ưu Tiên:** PHẢI CÓ
- **Mô Tả:** Phát hiện ngáp từ Mouth Aspect Ratio (MAR) và thời lượng
- **Công Nghệ:** Thị Giác Máy Tính (điểm mốc miệng từ dlib) + Logic Dựa Trên Quy Tắc
- **Thực Thể Được Giám Sát:** Chỉ Tài Xế
- **Đầu Ra:** Ngáp được phát hiện (có/không), số lượng ngáp mỗi kỳ
- **Phụ Thuộc:** PBI-001 (yêu cầu điểm mốc khuôn mặt bao gồm miệng)
- **Tiêu Chí Thành Công:**
  - Tính toán MAR: khoảng cách giữa môi trên/dưới so với chiều rộng miệng
  - Ngưỡng ngáp: MAR >0,6 trong >2 giây
  - Chỉ báo ngủ gật: 3+ ngáp trong 5 phút → cảnh báo
  - Phân biệt ngáp với nói chuyện/ăn (thời lượng + ngưỡng MAR)

---

#### PBI-014: Phát Hiện Vi Giấc Ngủ

- **Ưu Tiên:** PHẢI CÓ
- **Mô Tả:** Phát hiện mắt đóng rất ngắn (0,5-3 giây) chỉ báo các tập vi giấc
- **Công Nghệ:** Logic Dựa Trên Quy Tắc (phân tích thời lượng EAR)
- **Thực Thể Được Giám Sát:** Chỉ Tài Xế
- **Đầu Ra:** Số lượng sự kiện vi giấc, dấu thời gian
- **Phụ Thuộc:** PBI-003 (yêu cầu giá trị EAR)
- **Tiêu Chí Thành Công:**
  - Vi giấc: EAR <0,2 (hoàn toàn đóng) trong 0,5-3 giây
  - Phân biệt với chớp mắt bình thường (<0,4 giây) và đóng kéo dài (>3 giây)
  - Cảnh báo quan trọng tức thời khi phát hiện (cực kỳ nguy hiểm)
  - Ghi lại tất cả sự kiện vi giấc để phân tích

---

#### PBI-015: Tính Toán PERCLOS

- **Ưu Tiên:** NÊN CÓ
- **Mô Tả:** Tính Phần Trăm Đóng Mắt (PERCLOS) - số liệu ngủ gật tiêu chuẩn công nghiệp
- **Công Nghệ:** Logic Dựa Trên Quy Tắc (phân tích thống kê EAR theo cửa sổ thời gian)
- **Thực Thể Được Giám Sát:** Chỉ Tài Xế
- **Đầu Ra:** Giá trị PERCLOS (%), mức rủi ro ngủ gật
- **Phụ Thuộc:** PBI-003 (yêu cầu giá trị EAR)
- **Tiêu Chí Thành Công:**
  - PERCLOS = % thời gian mắt đóng trong cửa sổ 60 giây
  - Tính toán: đếm khung hình có EAR <0,25, chia cho tổng khung hình
  - Ngưỡng: <10% = cảnh báo, 10-20% = ngủ gật nhẹ, >20% = ngủ gật nặng
  - Cung cấp xác thực khoa học cho phát hiện ngủ gật

---

### Danh Mục 5: Phát Hiện Bị Phân Tán Chú Ý

> **Mục Đích:** Phát hiện khi sự chú ý của tài xế không ở trên đường bằng dữ liệu posture đầu và hướng nhìn.

---

#### PBI-016: Phân Tán Chú Ý Do Quay Đầu

- **Ưu Tiên:** PHẢI CÓ
- **Mô Tả:** Phát hiện quay đầu kéo dài rời khỏi đường (dựa trên góc yaw posture đầu)
- **Công Nghệ:** Logic Dựa Trên Quy Tắc (ngưỡng góc yaw + thời lượng)
- **Thực Thể Được Giám Sát:** Chỉ Tài Xế
- **Đầu Ra:** Cảnh báo bị phân tán, thời lượng đầu rời khỏi đường
- **Phụ Thuộc:** PBI-006 (yêu cầu góc posture đầu)
- **Tiêu Chí Thành Công:**
  - Ngưỡng bị phân tán: Yaw >±45° trong >2 giây → cảnh báo
  - Ngoại lệ: Yaw 20-45° trong <1,5 giây = kiểm tra gương (không cảnh báo)
  - Bị phân tán cực đoan: Yaw >±75° trong >1 giây → cảnh báo quan trọng
  - Ghi lại sự kiện bị phân tran với thời lượng và góc

---

#### PBI-017: Phát Hiện Nhìn Rời Khỏi Đường

- **Ưu Tiên:** PHẢI CÓ
- **Mô Tả:** Phát hiện khi hướng nhìn rời khỏi vùng đường phía trước trong thời gian kéo dài
- **Công Nghệ:** Logic Dựa Trên Quy Tắc (vùng hướng nhìn + thời lượng từ PBI-010)
- **Thực Thể Được Giám Sát:** Chỉ Tài Xế
- **Đầu Ra:** Thời lượng nhìn rời khỏi đường, kích hoạt cảnh báo
- **Phụ Thuộc:** PBI-010 (yêu cầu phân loại vùng hướng nhìn)
- **Tiêu Chí Thành Công:**
  - Ngưỡng nhìn rời khỏi đường: tích lũy 4 giây trong cửa sổ 10 giây
  - Kết hợp với posture đầu để phát hiện mạnh mẽ (đầu về phía trước nhưng hướng nhìn vào điện thoại)
  - Phân biệt kiểm tra gương (dịch chuyển hướng nhìn ngắn) với bị phân tán

---

#### PBI-018: Tính Toán Điểm Chú Ý

- **Ưu Tiên:** NÊN CÓ
- **Mô Tả:** Tính điểm chú ý tổng thể (0-100) kết hợp posture đầu, hướng nhìn, và mở mắt
- **Công Nghệ:** Logic Dựa Trên Quy Tắc hoặc ML (thuật toán tính điểm có trọng số)
- **Thực Thể Được Giám Sát:** Chỉ Tài Xế
- **Đầu Ra:** Điểm chú ý (0-100), mức độ chú ý (cao/trung bình/thấp)
- **Phụ Thuộc:** PBI-006, PBI-009, PBI-003 (yêu cầu dữ liệu đầu, hướng nhìn, mắt)
- **Tiêu Chí Thành Công:**
  - Tính toán điểm: trung bình có trọng số của đầu về phía trước (40%), hướng nhìn vào đường (40%), mắt mở (20%)
  - Chú ý cao: điểm >80 (xanh), Trung bình: 50-80 (vàng), Thấp: <50 (cảnh báo đỏ)
  - Hiển thị điểm thời gian thực trên bảng điều khiển (PBI-044)
  - Trung bình lăn trong cửa sổ 10 giây để ổn định

---

### Danh Mục 6: Nhận Dạng Hoạt Động Nguy Hiểm (7 Hoạt Động)

> **Mục Đích:** Phát hiện hành vi lái xe nguy hiểm bằng CNN phân loại hoạt động AI/ML.

---

#### PBI-019: Phát Hiện Gọi Điện Thoại

- **Ưu Tiên:** PHẢI CÓ
- **Mô Tả:** Phát hiện tài xế cầm điện thoại vào tai khi gọi
- **Công Nghệ:** AI/ML (CNN Hoạt Động - MobileNetV2 hoặc EfficientNet)
- **Thực Thể Được Giám Sát:** Chỉ Tài Xế
- **Đầu Ra:** Nhãn hoạt động "gọi điện", điểm tin cậy, cảnh báo
- **Phụ Thuộc:** PBI-026 (yêu cầu mô hình CNN Hoạt Động được huấn luyện)
- **Tiêu Chí Thành Công:**
  - Độ chính xác phát hiện: >85% trên tập dữ liệu kiểm tra
  - Ngưỡng tin cậy: >75% trong 3 khung hình liên tiếp (0,3s ở 10 FPS) → cảnh báo
  - Phân biệt với cạo mặt, điều chỉnh tóc (tính nhất quán thời gian)

---

#### PBI-020: Phát Hiện Uống Nước

- **Ưu Tiên:** PHẢI CÓ
- **Mô Tả:** Phát hiện tài xế uống từ chai/cốc trong khi lái
- **Công Nghệ:** AI/ML (CNN Hoạt Động)
- **Thực Thể Được Giám Sát:** Chỉ Tài Xế
- **Đầu Ra:** Nhãn hoạt động "uống", điểm tin cậy, cảnh báo
- **Phụ Thuộc:** PBI-026 (yêu cầu mô hình CNN Hoạt Động được huấn luyện)
- **Tiêu Chí Thành Công:**
  - Độ chính xác phát hiện: >85%
  - Ngưỡng tin cậy: >75% trong 2 khung hình liên tiếp → cảnh báo
  - Phát hiện các thùng chứa khác nhau (chai, cốc, lon)

---

#### PBI-021: Phát Hiện Hút Thuốc

- **Ưu Tiên:** PHẢI CÓ
- **Mô Tả:** Phát hiện tài xế hút thuốc lá trong khi lái
- **Công Nghệ:** AI/ML (CNN Hoạt Động)
- **Thực Thể Được Giám Sát:** Chỉ Tài Xế
- **Đầu Ra:** Nhãn hoạt động "hút thuốc", điểm tin cậy, cảnh báo
- **Phụ Thuộc:** PBI-026 (yêu cầu mô hình CNN Hoạt Động được huấn luyện)
- **Tiêu Chí Thành Công:**
  - Độ chính xác phát hiện: >85%
  - Ngưỡng tin cậy: >70% trong 5 khung hình liên tiếp (1 giây) → cảnh báo
  - Phát hiện cử động tay-vào-miệng với thuốc lá

---

#### PBI-022: Phát Hiện Hoạt Động Ngáp

- **Ưu Tiên:** PHẢI CÓ
- **Mô Tả:** Phát hiện ngáp như hoạt động nguy hiểm bằng CNN Hoạt Động (thay thế/bổ sung cho PBI-013)
- **Công Nghệ:** AI/ML (CNN Hoạt Động) hoặc CV (điểm mốc miệng)
- **Thực Thể Được Giám Sát:** Chỉ Tài Xế
- **Đầu Ra:** Nhãn hoạt động "ngáp", số lượng, cảnh báo
- **Phụ Thuộc:** PBI-026 (CNN Hoạt Động) HOẶC PBI-013 (dựa trên điểm mốc)
- **Tiêu Chí Thành Công:**
  - Hai cách tiếp cận: dựa trên CNN (PBI-022) và dựa trên điểm mốc (PBI-013)
  - Sử dụng cả hai để xác thực, hoặc chọn một dựa trên độ chính xác
  - Mục tiêu: >85% độ chính xác cho cách tiếp cận CNN

---

#### PBI-023: Phát Hiện Tay Không Ở Bánh Lái

- **Ưu Tiên:** PHẢI CÓ
- **Mô Tả:** Phát hiện khi tay tài xế không ở trên bánh lái
- **Công Nghệ:** AI/ML (Phát hiện tay + CNN Hoạt Động) hoặc mô đun theo dõi tay riêng biệt
- **Thực Thể Được Giám Sát:** Chỉ Tài Xế
- **Đầu Ra:** Nhãn hoạt động "tay_không_ở_bánh_lái", thời lượng, cảnh báo
- **Phụ Thuộc:** PBI-026 (CNN Hoạt Động) hoặc mô hình phát hiện tay riêng biệt
- **Tiêu Chí Thành Công:**
  - Độ chính xác phát hiện: >80% (thử thách do che khuất bánh lái)
  - Ngưỡng cảnh báo: hai tay không ở bánh lái >3 giây → cảnh báo, >5 giây → cảnh báo quan trọng
  - Một tay không ở bánh lái >10 giây → cảnh báo (chấp nhận được tạm thời)

---

#### PBI-024: Phát Hiện Tay Vươn Ra Ngoài Cửa Sổ

- **Ưu Tiên:** PHẢI CÓ
- **Mô Tả:** Phát hiện tay tài xế vươn ra ngoài cửa sổ
- **Công Nghệ:** AI/ML (CNN Hoạt Động + ước tính posture)
- **Thực Thể Được Giám Sát:** Chỉ Tài Xế
- **Đầu Ra:** Nhãn hoạt động "tay_ra_ngoài_cửa_sổ", thời lượng, cảnh báo
- **Phụ Thuộc:** PBI-026 (CNN Hoạt Động)
- **Tiêu Chí Thành Công:**
  - Độ chính xác phát hiện: >85%
  - Ngưỡng tin cậy: >75% trong 2 giây → cảnh báo
  - Phát hiện vị trí tay bên ngoài giới hạn khung hình bình thường

---

#### PBI-025: Phát Hiện Nhìn Vào Hướng Dẫn

- **Ưu Tiên:** PHẢI CÓ
- **Mô Tả:** Phát hiện tài xế nhìn vào điện thoại/GPS để định hướng (đầu xuống, hướng nhìn vào thiết bị trong lòng)
- **Công Nghệ:** AI/ML (CNN Hoạt Động) + Phân tích vùng hướng nhìn (PBI-010)
- **Thực Thể Được Giám Sát:** Chỉ Tài Xế
- **Đầu Ra:** Nhãn hoạt động "nhìn_vào_hướng_dẫn", thời lượng, cảnh báo
- **Phụ Thuộc:** PBI-026 (CNN Hoạt Động), PBI-010 (vùng hướng nhìn)
- **Tiêu Chí Thành Công:**
  - Phát hiện kết hợp: pitch đầu <-20° (nhìn xuống) + hướng nhìn vào vùng lòng
  - Ngưỡng cảnh báo: >2 giây nhìn vào hướng dẫn → cảnh báo
  - Phân biệt với nhìn bảng điều khiển (góc khác nhau, thời lượng ngắn hơn)

---

#### PBI-026: Huấn Luyện Mô Hình CNN Hoạt Động

- **Ưu Tiên:** PHẢI CÓ
- **Mô Tả:** Huấn luyện mô hình học sâu để nhận dạng hoạt động bao gồm tất cả 7 hoạt động nguy hiểm
- **Công Nghệ:** AI/ML (MobileNetV2, EfficientNet-B0, hoặc kiến trúc CNN tùy chỉnh)
- **Thực Thể Được Giám Sát:** Hệ Thống
- **Đầu Ra:** Tệp mô hình được huấn luyện (.h5 hoặc .pth), số liệu độ chính xác, ma trận nhầm lẫn
- **Phụ Thuộc:** Sưu tập tập dữ liệu (300+ mẫu mỗi hoạt động với tăng cường)
- **Tiêu Chí Thành Công:**
  - Độ chính xác tổng thể: >85% trên tập dữ liệu kiểm tra (70% dữ liệu được gắn nhãn)
  - Độ chính xác mỗi hoạt động: >85% cho mỗi 7 hoạt động
  - Ma trận nhầm lẫn: không có hai hoạt động nào có >15% nhầm lẫn chéo
  - Thời gian suy luận: <30ms mỗi khung hình (cho phép 30+ FPS)
  - Kích thước mô hình: <20MB để triển khai nhúng (MobileNetV2)
  - Tập dữ liệu huấn luyện: 300+ mẫu mỗi hoạt động, điều kiện đa dạng (ánh sáng, góc, nhân khẩu học)

---

### Danh Mục 7: Đăng Ký & Nhận Dạng Tài Xế

> **Mục Đích:** Xác định tài xế bằng nhận dạng khuôn mặt để giám sát được cá nhân hóa và chịu trách nhiệm.

---

#### PBI-027: Đăng Ký Khuôn Mặt Tài Xế

- **Ưu Tiên:** NÊN CÓ
- **Mô Tả:** Đăng ký tài xế mới bằng cách ghi lại hình ảnh khuôn mặt và lưu trữ các tính năng khuôn mặt (mã hóa)
- **Công Nghệ:** Thị Giác Máy Tính (mã hóa khuôn mặt - nhận dạng khuôn mặt dlib hoặc FaceNet)
- **Thực Thể Được Giám Sát:** Chỉ Tài Xế
- **Đầu Ra:** Vectơ mã hóa khuôn mặt 128D, ID Tài Xế, lưu trữ trong cơ sở dữ liệu
- **Phụ Thuộc:** PBI-001 (yêu cầu phát hiện mặt)
- **Tiêu Chí Thành Công:**
  - Ghi lại 10+ hình ảnh khuôn mặt trong quá trình đăng ký (góc: giữa, ±15° trái/phải, ±10° lên/xuống)
  - Độ tin cậy phát hiện mặt >90% cho tất cả hình ảnh ghi lại
  - Tạo vectơ mã hóa 128D bằng dlib/FaceNet
  - Lưu trữ trong cơ sở dữ liệu với siêu dữ liệu tài xế (tên, ID, ngày đăng ký)
  - Thời gian đăng ký: <30 giây
  - Phòng chặn trùng lặp: từ chối nếu độ tương tự >0,7 với tài xế hiện có

---

#### PBI-028: Nhận Dạng Tài Xế

- **Ưu Tiên:** NÊN CÓ
- **Mô Tả:** Xác định tài xế đã đăng ký khi họ vào xe bằng nhận dạng khuôn mặt
- **Công Nghệ:** Thị Giác Máy Tính (so sánh mã hóa khuôn mặt - độ tương tự cosin hoặc khoảng cách Euclidean)
- **Thực Thể Được Giám Sát:** Chỉ Tài Xế
- **Đầu Ra:** ID Tài Xế, điểm tin cậy, thông báo chào
- **Phụ Thuộc:** PBI-027 (yêu cầu tài xế được đăng ký), PBI-001 (yêu cầu phát hiện mặt)
- **Tiêu Chí Thành Công:**
  - Tốc độ nhận dạng: <100ms mỗi khung hình
  - Độ chính xác: >95% cho tài xế đã đăng ký
  - Ngưỡng độ tương tự: >0,6 = trùng khớp, <0,6 = tài xế không xác định
  - Xử lý tài xế không xác định: yêu cầu đăng ký hoặc tiếp tục dưới dạng "khách"
  - Liên kết tất cả sự kiện phiên với ID Tài Xế được xác định

---

#### PBI-029: Quản Lý Đa Tài Xế

- **Ưu Tiên:** NÊN CÓ
- **Mô Tả:** Hỗ trợ nhiều tài xế được đăng ký trên mỗi xe (ví dụ: xe gia đình, xe hạm đội chung)
- **Công Nghệ:** Cơ Sở Dữ Liệu + Nhận Dạng Khuôn Mặt
- **Thực Thể Được Giám Sát:** Chỉ Tài Xế
- **Đầu Ra:** Lựa chọn hồ sơ tài xế, liên kết phiên với ID Tài Xế
- **Phụ Thuộc:** PBI-027, PBI-028 (yêu cầu đăng ký và nhận dạng)
- **Tiêu Chí Thành Công:**
  - Hỗ trợ 5-10 tài xế được đăng ký trên mỗi xe
  - Tự động xác định tài xế ở đầu phiên (5 giây đầu tiên)
  - Cho phép chọn tài xế thủ công nếu tự động nhận dạng không thành công
  - Lưu trữ cài đặt mỗi tài xế (ngưỡng EAR, tùy chọn cảnh báo - cải tiến tương lai)
  - Theo dõi thống kê mỗi tài xế (điểm an toàn, lịch sử sự cố)

---

### Danh Mục 8: Giám Sát Hành Khách

> **Mục Đích:** Đếm hành khách để tuân thủ theo dõi (trường hợp sử dụng quản lý hạm đội).

---

#### PBI-030: Đếm Hành Khách

- **Ưu Tiên:** NÊN CÓ
- **Mô Tả:** Đếm số lượng hành khách trong xe (ghế trước + ghế sau)
- **Công Nghệ:** Thị Giác Máy Tính (phát hiện người - YOLO v5/v8 hoặc SSD) hoặc cảm biến độ sâu
- **Thực Thể Được Giám Sát:** Tài Xế + Hành Khách
- **Đầu Ra:** Số lượng hành khách (0-4 thường xuyên), bản đồ chiếm dụng ghế
- **Phụ Thuộc:** Camera bổ sung cho chế độ xem cabin, hoặc camera IR góc rộng
- **Tiêu Chí Thành Công:**
  - Độ chính xác đếm: >90% cho hành khách đứng yên
  - Phát hiện hành khách trong 4 vùng: hành khách trước, hàng ghế sau trái, hàng ghế sau giữa, hàng ghế sau phải
  - Cập nhật số lượng khi hành khách vào/ra (phát hiện thay đổi)
  - Trường hợp sử dụng: tuân thủ hạm đội (sức chứa tối đa), bảo hiểm, phân tích an toàn

---

#### PBI-031: Phát Hiện Khuôn Mặt Hành Khách

- **Ưu Tiên:** CÓ THỂ CÓ
- **Mô Tả:** Phát hiện khuôn mặt của hành khách để xác minh cụ thể chiếm dụng (cải tiến PBI-030)
- **Công Nghệ:** Thị Giác Máy Tính (phát hiện multi-mặt)
- **Thực Thể Được Giám Sát:** Hành Khách
- **Đầu Ra:** Số lượng khuôn mặt, vị trí khuôn mặt (vị trí ghế)
- **Phụ Thuộc:** PBI-030 (đếm hành khách), camera bổ sung hoặc ống kính góc rộng
- **Tiêu Chí Thành Công:**
  - Phát hiện lên tới 5 khuôn mặt đồng thời (tài xế + 4 hành khách)
  - Ánh xạ vị trí khuôn mặt thành vị trí ghế
  - Trường hợp xác thực: xác minh độ chính xác số lượng hành khách
  - Cân nhắc bảo mật: không nhận dạng khuôn mặt hành khách, chỉ phát hiện

---

### Danh Mục 9: Phụ Kiện An Toàn (Kính Mắt/Mặt Nạ)

> **Mục Đích:** Phát hiện phụ kiện ảnh hưởng đến các thuật toán phát hiện và tự thích ứng cho phù hợp.

---

#### PBI-032: Phát Hiện Kính Mắt

- **Ưu Tiên:** NÊN CÓ
- **Mô Tả:** Phát hiện nếu tài xế đeo kính mắt (ảnh hưởng đến phát hiện mắt và ngưỡng EAR)
- **Công Nghệ:** Thị Giác Máy Tính (phân loại kính mắt) hoặc AI/ML
- **Thực Thể Được Giám Sát:** Chỉ Tài Xế
- **Đầu Ra:** Trạng thái kính mắt (có/không), điều chỉnh ngưỡng EAR nếu cần
- **Phụ Thuộc:** PBI-001 (yêu cầu phát hiện mặt)
- **Tiêu Chí Thành Công:**
  - Độ chính xác phát hiện kính mắt: >90%
  - Tự động điều chỉnh ngưỡng EAR: nếu phát hiện kính mắt, giảm ngưỡng 0,02-0,03 (kính mắt gây EAR thấp hơn)
  - Phát hiện riêng kính râm (có thể chặn phát hiện mắt)
  - Cảnh báo nếu kính râm chặn điểm mốc mắt

---

#### PBI-033: Phát Hiện Mặt Nạ

- **Ưu Tiên:** CÓ THỂ CÓ
- **Mô Tả:** Phát hiện nếu tài xế đeo mặt nạ khuôn mặt (ảnh hưởng đến phát hiện điểm mốc khuôn mặt)
- **Công Nghệ:** AI/ML (phân loại mặt nạ - MobileNetV2)
- **Thực Thể Được Giám Sát:** Chỉ Tài Xế
- **Đầu Ra:** Trạng thái mặt nạ (có/không), cảnh báo nếu mặt nạ can thiệp vào phát hiện
- **Phụ Thuộc:** PBI-001 (yêu cầu phát hiện mặt)
- **Tiêu Chí Thành Công:**
  - Độ chính xác phát hiện mặt nạ: >90%
  - Cảnh báo: nếu mặt nạ được phát hiện và điểm mốc miệng thất bại, thông báo tài xế loại bỏ mặt nạ
  - Giảm nhẹ uyển chuyển: tắt phát hiện ngáp (PBI-013) nếu mặt nạ mặc
  - Trường hợp sử dụng: tuân thủ COVID-19 hoặc giám sát sau đại dịch

---

### Danh Mục 10: Quản Lý Sức Khỏe & Camera Hệ Thống

> **Mục Đích:** Giám sát sức khỏe hệ thống, trạng thái camera, và điều kiện môi trường để hoạt động đáng tin cậy.

---

#### PBI-034: Kiểm Tra Sức Khỏe Camera IR

- **Ưu Tiên:** PHẢI CÓ
- **Mô Tả:** Giám sát kết nối camera và chất lượng hình ảnh để đảm bảo hệ thống giám sát hoạt động
- **Công Nghệ:** Tích Hợp Phần Cứng + Thị Giác Máy Tính (xác thực khung hình)
- **Thực Thể Được Giám Sát:** Camera/Hệ Thống
- **Đầu Ra:** Trạng thái camera (trực tuyến/ngoại tuyến), số liệu chất lượng hình ảnh (độ sáng, độ tương phản, mờ)
- **Phụ Thuộc:** Giao diện phần cứng (camera USB)
- **Tiêu Chí Thành Công:**
  - Kiểm tra kết nối camera: phát hiện mất kết nối camera trong 2 giây
  - Xác thực khung hình: kiểm tra khung hình bị đóng băng (cùng khung >2 giây)
  - Số liệu chất lượng hình ảnh: biểu đồ độ sáng, phát hiện mờ (phương sai Laplacian)
  - Hiển thị cảnh báo "Camera Ngoại Tuyến" nếu camera không thành công
  - Ghi lại lỗi camera để bảo trì

---

#### PBI-035: Phát Hiện Ánh Sáng Yếu

- **Ưu Tiên:** NÊN CÓ
- **Mô Tả:** Phát hiện điều kiện ánh sáng không đủ ảnh hưởng đến độ chính xác phát hiện
- **Công Nghệ:** Thị Giác Máy Tính (phân tích biểu đồ độ sáng)
- **Thực Thể Được Giám Sát:** Camera/Hệ Thống
- **Đầu Ra:** Mức độ ánh sáng (đủ/không đủ), thông báo cảnh báo
- **Phụ Thuộc:** PBI-034 (kiểm tra sức khỏe camera)
- **Tiêu Chí Thành Công:**
  - Phân tích độ sáng: tính toán độ sáng trung bình/trung bình từ biểu đồ
  - Ngưỡng: nếu độ sáng trung bình <30 (thang điểm 0-255) → cảnh báo "Ánh Sáng Yếu"
  - Camera IR nên xử lý ánh sáng yếu, nhưng cảnh báo nếu chiếu sáng IR không thành công
  - Điều chỉnh tự động: tăng phơi sáng camera nếu có thể

---

#### PBI-036: Phát Hiện Che Khuất Khuôn Mặt

- **Ưu Tiên:** NÊN CÓ
- **Mô Tả:** Phát hiện khi khuôn mặt bị che khuất một phần (tay che mặt, vật, vị trí)
- **Công Nghệ:** Thị Giác Máy Tính (phân tích độ tin cậy điểm mốc)
- **Thực Thể Được Giám Sát:** Chỉ Tài Xế
- **Đầu Ra:** Trạng thái che khuất (có/không), vùng bị che khuất (mắt, miệng, v.v.), cảnh báo
- **Phụ Thuộc:** PBI-001 (yêu cầu điểm mốc khuôn mặt với điểm tin cậy)
- **Tiêu Chí Thành Công:**
  - Phát hiện che khuất: nếu >30% điểm mốc có độ tin cậy <0,5 → che khuất
  - Xác định vùng bị che khuất: mắt, miệng, toàn bộ mặt
  - Giảm nhẹ uyển chuyển: nếu mắt bị che khuất, quay trở lại chỉ ước tính posture đầu (PBI-006)
  - Cảnh báo: "Mặt bị che khuất một phần" nếu che khuất >5 giây

---

#### PBI-037: Giám Sát FPS Hệ Thống

- **Ưu Tiên:** NÊN CÓ
- **Mô Tả:** Giám sát tốc độ xử lý khung hình để đảm bảo hiệu suất theo thời gian thực
- **Công Nghệ:** Số Liệu Hệ Thống (theo dõi time.time())
- **Thực Thể Được Giám Sát:** Hệ Thống
- **Đầu Ra:** Giá trị FPS, cảnh báo hiệu suất nếu dưới ngưỡng
- **Phụ Thuộc:** Không (giám sát cấp hệ thống)
- **Tiêu Chí Thành Công:**
  - FPS Mục Tiêu: tối thiểu 15-20 FPS cho giám sát theo thời gian thực
  - Tính toán FPS: trung bình lăn trong 30 khung hình
  - Cảnh báo: nếu FPS <15 trong >5 giây → chỉ báo "Hiệu Suất Thấp"
  - Ghi lại thả FPS để phân tích tối ưu hóa
  - Hiển thị FPS trên bảng điều khiển (chế độ nhà phát triển)

---

### Danh Mục 11: Hệ Thống Cảnh Báo

> **Mục Đích:** Gửi cảnh báo kịp thời, ưu tiên cho tài xế tại các sự kiện quan trọng.

---

#### PBI-038: Cảnh Báo Âm Thanh Theo Thời Gian Thực

- **Ưu Tiên:** PHẢI CÓ
- **Mô Tả:** Phát cảnh báo âm thanh cho các sự kiện quan trọng (ngủ gật, bị phân tán, hoạt động nguy hiểm)
- **Công Nghệ:** Đầu Ra Âm Thanh (pygame/pydub cho âm thanh bíp, cảnh báo bằng giọng nói)
- **Thực Thể Được Giám Sát:** Hệ Thống
- **Đầu Ra:** Cảnh báo âm thanh được phát, loại cảnh báo được ghi lại
- **Phụ Thuộc:** Sự kiện cảnh báo từ PBI-012, PBI-016, PBI-019-025
- **Tiêu Chí Thành Công:**
  - Độ trễ cảnh báo: <500ms từ phát hiện sự kiện đến phát âm thanh
  - Loại âm thanh: bíp (ngủ gật), cảnh báo giọng nói (bị phân tán), bíp khẩn cấp (quan trọng)
  - Thời lượng cảnh báo: 1-3 giây (đáng chú ý nhưng không phiền)
  - Âm lượng: có thể điều chỉnh, mặc định 80% âm lượng hệ thống
  - Ghi lại tất cả cảnh báo với dấu thời gian, loại sự kiện, thời gian phản ứng của tài xế

---

#### PBI-039: Cảnh Báo Hình Ảnh (LED/Bảng Điều Khiển)

- **Ưu Tiên:** NÊN CÓ
- **Mô Tả:** Hiển thị cảnh báo hình ảnh trên giao diện bảng điều khiển hoặc chỉ báo LED
- **Công Nghệ:** Tích Hợp Phần Cứng (GPIO LED) hoặc Hiển Thị GUI
- **Thực Thể Được Giám Sát:** Hệ Thống
- **Đầu Ra:** Cảnh báo hình ảnh được hiển thị trên bảng điều khiển, được mã hóa màu theo mức độ nghiêm trọng
- **Phụ Thuộc:** PBI-044 (giao diện bảng điều khiển) hoặc phần cứng GPIO
- **Tiêu Chí Thành Công:**
  - Mã hóa màu: Xanh = OK, Vàng = Cảnh báo (bị phân tán), Đỏ = Quan trọng (ngủ gật)
  - Mô hình LED: đen (OK), nhấp nháy chậm (cảnh báo), nhấp nháy nhanh (quan trọng)
  - Lớp phủ bảng điều khiển: biểu tượng + thông báo văn bản cho cảnh báo hiện tại
  - Đồng bộ hóa với cảnh báo âm thanh (PBI-038)

---

#### PBI-040: Quản Lý Ưu Tiên Cảnh Báo

- **Ưu Tiên:** NÊN CÓ
- **Mô Tả:** Ưu tiên các cảnh báo đồng thời để ngăn chặn spam cảnh báo
- **Công Nghệ:** Logic Dựa Trên Quy Tắc (quản lý hàng đợi cảnh báo)
- **Thực Thể Được Giám Sát:** Hệ Thống
- **Đầu Ra:** Chuỗi cảnh báo ưu tiên, phòng chặn spam
- **Phụ Thuộc:** Tất cả các PBI tạo cảnh báo (PBI-012, PBI-016, PBI-019-025)
- **Tiêu Chí Thành Công:**
  - Thứ tự ưu tiên: Ngủ Gật (quan trọng) > Bị Phân Tán > Hoạt Động Nguy Hiểm
  - Hàng đợi cảnh báo: nếu nhiều sự kiện trong 2 giây, chỉ phát cảnh báo ưu tiên cao nhất
  - Chế độ tắt: cảnh báo cùng loại không được lặp lại trong 10 giây (trừ khi tình trạng tồi tệ hơn)
  - Ghi lại cảnh báo bị tắt để phân tích

---

### Danh Mục 12: Ghi Lại Dữ Liệu & Ghi Video

> **Mục Đích:** Ghi lại sự kiện và video để phân tích, chịu trách nhiệm và lấy bằng chứng.

---

#### PBI-041: Ghi Lại Sự Kiện

- **Ưu Tiên:** PHẢI CÓ
- **Mô Tả:** Ghi lại tất cả các sự kiện được phát hiện với dấu thời gian vào cơ sở dữ liệu (ngủ gật, bị phân tán, hoạt động, cảnh báo)
- **Công Nghệ:** Cơ Sở Dữ Liệu (SQLite cho cục bộ, PostgreSQL cho hạm đội)
- **Thực Thể Được Giám Sát:** Hệ Thống
- **Đầu Ra:** Bản ghi sự kiện trong cơ sở dữ liệu với lược đồ: event_id, session_id, event_type, timestamp, severity, confidence, metadata (JSON)
- **Phụ Thuộc:** Lược đồ cơ sở dữ liệu
- **Tiêu Chí Thành Công:**
  - Loại sự kiện: ngủ gật, bị phân tán, hoạt động (7 loại), cảnh báo được kích hoạt, lỗi hệ thống
  - Độ chính xác dấu thời gian: mili giây
  - Siêu dữ liệu: trường JSON cho dữ liệu cụ thể sự kiện (giá trị EAR, góc, điểm tin cậy)
  - Hiệu suất truy vấn: <200ms cho 10.000+ bản ghi với chỉ mục trên driver_id, timestamp

---

#### PBI-042: Ghi Lại Video (Kích Hoạt Bởi Sự Kiện)

- **Ưu Tiên:** NÊN CÓ
- **Mô Tả:** Ghi lại video clip khi xảy ra sự kiện quan trọng (±30 giây xung quanh sự kiện để có bước)
- **Công Nghệ:** Lưu Trữ Video (OpenCV VideoWriter, mã hóa MP4 với H.264)
- **Thực Thể Được Giám Sát:** Hệ Thống
- **Đầu Ra:** Tệp video được liên kết với sự kiện, được lưu trữ với dấu thời gian
- **Phụ Thuộc:** PBI-041 (ghi lại sự kiện để liên kết video)
- **Tiêu Chí Thành Công:**
  - Điều kiện kích hoạt: cảnh báo ngủ gật, bị phân tán quan trọng, hoạt động nguy hiểm
  - Thời lượng ghi lại: 30 giây trước + 30 giây sau sự kiện (60s tổng cộng)
  - Định dạng video: MP4, 720p, 10 FPS (yêu cầu lưu trữ thấp)
  - Lưu trữ: đường dẫn video được lưu trong siêu dữ liệu sự kiện (PBI-041)
  - Xóa tự động: loại bỏ video cũ hơn 30 ngày hoặc khi lưu trữ >90%
  - Bảo mật: chỉ ghi lại kích hoạt (không ghi lại liên tục)

---

#### PBI-043: Theo Dõi Phiên

- **Ưu Tiên:** NÊN CÓ
- **Mô Tả:** Theo dõi phiên lái xe (thời gian bắt đầu/kết thúc, ID tài xế, thời gian chuyến đi, tổng sự kiện)
- **Công Nghệ:** Cơ Sở Dữ Liệu (bảng phiên)
- **Thực Thể Được Giám Sát:** Hệ Thống
- **Đầu Ra:** Bản ghi phiên với lược đồ: session_id, driver_id, start_time, end_time, vehicle_id, total_events, video_path
- **Phụ Thuộc:** PBI-028 (nhận dạng tài xế), PBI-041 (ghi lại sự kiện)
- **Tiêu Chí Thành Công:**
  - Phiên tự động bắt đầu: khi tài xế được xác định hoặc bắt đầu thủ công
  - Phiên tự động kết thúc: khi xe tắt hoặc sau 5 phút không phát hiện mặt
  - Tóm tắt chuyến đi: tổng thời lượng, số lượng sự kiện theo loại, điểm an toàn
  - Liên kết tất cả sự kiện thành session_id để phân tích dựa trên chuyến đi

---

### Danh Mục 13: Bảng Điều Khiển & Giao Diện Người Dùng

> **Mục Đích:** Giao diện giám sát thời gian thực và phân tích lịch sử cho tài xế và quản lý hạm đội.

---

#### PBI-044: Bảng Điều Khiển Giám Sát Trực Tiếp

- **Ưu Tiên:** PHẢI CÓ
- **Mô Tả:** Giao diện người dùng theo thời gian thực hiển thị video camera, lớp phát hiện, trạng thái hiện tại
- **Công Nghệ:** Khung Công Việc GUI (cửa sổ OpenCV, Qt, hoặc web dựa trên Flask/React)
- **Thực Thể Được Giám Sát:** Hệ Thống
- **Đầu Ra:** Giao diện hình ảnh với lớp phát hiện (hộp mặt, điểm mốc mắt, hướng nhìn), chỉ báo trạng thái, cảnh báo hiện tại
- **Phụ Thuộc:** Tất cả các PBI phát hiện (PBI-001 đến PBI-018)
- **Tiêu Chí Thành Công:**
  - Hiển thị các phần tử:
    - Video camera với lớp phát hiện (hộp mặt, điểm mốc mắt, hướng nhìn)
    - Chỉ báo trạng thái: mức ngủ gật, điểm chú ý, hoạt động hiện tại
    - Bảng cảnh báo: thông báo cảnh báo hiện tại, màu theo mức độ nghiêm trọng
    - Sức khỏe hệ thống: FPS, trạng thái camera, ID tài xế
  - Tốc độ cập nhật: 10-15 FPS cho giao diện (có thể thấp hơn processing FPS)
  - Màu lớp: Xanh = OK, Vàng = Cảnh báo, Đỏ = Quan Trọng
  - Điều khiển bàn phím: q=thoát, s=bắt đầu/dừng, r=đặt lại, c=hiệu chỉnh

---

#### PBI-045: Bảng Điều Khiển Phân Tích Lịch Sử

- **Ưu Tiên:** CÓ THỂ CÓ
- **Mô Tả:** Xem các chuyến đi quá khứ, thống kê sự kiện, xu hướng hành vi tài xế theo thời gian
- **Công Nghệ:** Bảng Điều Khiển Web (Flask + React) hoặc ứng dụng máy tính để bàn (Qt + matplotlib)
- **Thực Thể Được Giám Sát:** Hệ Thống
- **Đầu Ra:** Biểu đồ/đồ thị sự kiện theo thời gian, điểm an toàn tài xế, tóm tắt chuyến đi
- **Phụ Thuộc:** PBI-041, PBI-043 (yêu cầu dữ liệu sự kiện và phiên)
- **Tiêu Chí Thành Công:**
  - Danh sách chuyến đi: xem tất cả các phiên quá khứ với ngày, thời lượng, số lượng sự kiện
  - Chi tiết chuyến đi: nhấp để xem lịch sự kiện, video clip (PBI-042)
  - Biểu đồ phân tích:
    - Sự kiện theo thời gian (biểu đồ đường: ngủ gật, bị phân tán, hoạt động mỗi ngày/tuần)
    - Phân bố loại sự kiện (biểu đồ tròn)
    - So sánh tài xế (biểu đồ cột: điểm an toàn cho nhiều tài xế)
  - Bộ lọc: phạm vi ngày, ID tài xế, loại sự kiện
  - Xuất: xuất CSV dữ liệu sự kiện để phân tích ngoài

---

## Tóm Tắt Ưu Tiên MoSCoW

###  PHẢI CÓ (24 mục) - MVP Để Tốt Nghiệp Luận Văn

**Phát Hiện Cốt Lõi (Nền Tảng):**
- PBI-001: Phát Hiện & Theo Dõi Mặt
- PBI-002: Phát Hiện Vùng Mắt
- PBI-003: Phát Hiện Mắt Mở (EAR)
- PBI-004: Giám Sát Tần Suất Chớp Mắt
- PBI-005: Theo Dõi Vị Trí Mắt
- PBI-006: Ước Tính Posture Đầu
- PBI-007: Theo Dõi Vị Trí Đầu
- PBI-008: Phân Loại Vùng Đầu
- PBI-009: Ước Tính Hướng Nhìn
- PBI-010: Phân Loại Vùng Hướng Nhìn

**Phát Hiện An Toàn (Tính Năng Cốt Lõi):**
- PBI-012: Phát Hiện Ngủ Gật (dựa trên EAR)
- PBI-013: Phát Hiện Ngáp
- PBI-014: Phát Hiện Vi Giấc Ngủ
- PBI-016: Phân Tán Chú Ý Do Quay Đầu
- PBI-017: Phát Hiện Nhìn Rời Khỏi Đường

**Hoạt Động Nguy Hiểm (Tất Cả 7 + Mô Hình):**
- PBI-019: Phát Hiện Gọi Điện Thoại
- PBI-020: Phát Hiện Uống Nước
- PBI-021: Phát Hiện Hút Thuốc
- PBI-022: Phát Hiện Hoạt Động Ngáp
- PBI-023: Phát Hiện Tay Không Ở Bánh Lái
- PBI-024: Phát Hiện Tay Vươn Ra Ngoài Cửa Sổ
- PBI-025: Phát Hiện Nhìn Vào Hướng Dẫn
- PBI-026: Huấn Luyện Mô Hình CNN Hoạt Động

**Cơ Sở Hạ Tầng Hệ Thống:**
- PBI-034: Kiểm Tra Sức Khỏe Camera IR
- PBI-038: Cảnh Báo Âm Thanh Theo Thời Gian Thực
- PBI-041: Ghi Lại Sự Kiện
- PBI-044: Bảng Điều Khiển Giám Sát Trực Tiếp

**Tổng Cộng:** 24 mục

---

### NÊN CÓ (17 mục) - Cải Tiến Quan Trọng

**Phát Hiện Nâng Cao:**
- PBI-011: Phát Hiện & Theo Dõi Học Sinh (cải thiện độ chính xác hướng nhìn)
- PBI-015: Tính Toán PERCLOS (xác thực khoa học)
- PBI-018: Tính Toán Điểm Chú Ý (số liệu tổng thể)

**Quản Lý Tài Xế:**
- PBI-027: Đăng Ký Khuôn Mặt Tài Xế
- PBI-028: Nhận Dạng Tài Xế
- PBI-029: Quản Lý Đa Tài Xế

**Hành Khách & Phụ Kiện:**
- PBI-030: Đếm Hành Khách
- PBI-032: Phát Hiện Kính Mắt

**Sức Khỏe Hệ Thống:**
- PBI-035: Phát Hiện Ánh Sáng Yếu
- PBI-036: Phát Hiện Che Khuất Khuôn Mặt
- PBI-037: Giám Sát FPS Hệ Thống

**Cảnh Báo & Ghi Video:**
- PBI-039: Cảnh Báo Hình Ảnh (LED/Bảng Điều Khiển)
- PBI-040: Quản Lý Ưu Tiên Cảnh Báo
- PBI-042: Ghi Lại Video (Kích Hoạt Bởi Sự Kiện)
- PBI-043: Theo Dõi Phiên

**Tổng Cộng:** 17 mục

---

###  CÓ THỂ CÓ (4 mục) - Tính Năng Tốt Là Có

**Tính Năng Nâng Cao:**
- PBI-031: Phát Hiện Khuôn Mặt Hành Khách (cải tiến PBI-030)
- PBI-033: Phát Hiện Mặt Nạ (kịch bản sau COVID)
- PBI-045: Bảng Điều Khiển Phân Tích Lịch Sử (quản lý hạm đội)

**Tổng Cộng:** 4 mục

---

### KHÔNG CÓ - Ngoài Phạm Vi Rõ Ràng

- **Phát Hiện Dây An Toàn:** Loại bỏ theo quyết định phạm vi (không bắt buộc cho luận văn)
- **Phân Tích Biểu Hiện Khuôn Mặt:** Quá phức tạp, ưu tiên thấp
- **Đồng Bộ Đám Mây / Máy Chủ Hạm Đội:** Chỉ cục bộ cho phạm vi luận văn
- **Cập Nhật Over-The-Air (OTA):** Chỉ cập nhật thủ công
- **Ứng Dụng Di Động:** Chỉ giao diện máy tính để bàn
- **Tích Hợp CAN Bus:** Khởi động/dừng thủ công
- **Hỗ Trợ Đa Camera:** Chỉ camera IR duy nhất
- **Tính Năng Lái Autonomous:** Chỉ giám sát, không kiểm soát xe
- **Phân Tích Sinh Trắc Học Nâng Cao:** Tập trung vào hành vi, không giám sát sức khỏe
- **Truyền Phát Đám Mây Thời Gian Thực:** Mối quan tâm bảo mật và băng thông

---

## Công Nghệ Sử Dụng

### Thị Giác Máy Tính & AI/ML

- **OpenCV:** Phát hiện mặt, xử lý hình ảnh, video I/O
- **dlib:** Điểm mốc khuôn mặt 68 điểm, mã hóa nhận dạng khuôn mặt
- **MediaPipe:** Lưới mặt thay thế (468 điểm mốc), theo dõi iris (PBI-011)
- **MobileNetV2 / EfficientNet-B0:** CNN nhận dạng hoạt động (PBI-026)
- **FaceNet / nhận dạng khuôn mặt dlib:** Nhận dạng tài xế (PBI-027, PBI-028)
- **YOLO v5/v8 hoặc SSD:** Phát hiện hành khách (PBI-030)

### Phần Cứng

- **Camera IR:** Camera IR USB cho hoạt động ngày/đêm (ví dụ: 720p 30 FPS với LED IR)
- **Đơn Vị Xử Lý:** Jetson Nano ($100) hoặc Raspberry Pi 4 8GB ($75)
- **Tùy Chọn:** GPIO LED cho cảnh báo hình ảnh (PBI-039)

### Khung Công Việc Phần Mềm

- **Ngôn Ngữ:** Python 3.7+ (chính)
- **Cơ Sở Dữ Liệu:** SQLite (cục bộ), PostgreSQL tùy chọn (hạm đội)
- **GUI:** Cửa sổ OpenCV (nguyên mẫu nhanh), Qt/PyQt5 (giao diện sản xuất), hoặc Flask + React (dựa trên web)
- **Âm Thanh:** pygame hoặc pydub cho âm thanh cảnh báo
- **Ghi Video:** OpenCV VideoWriter với codec H.264

### Phát Triển & Triển Khai

- **Kiểm Soát Phiên Bản:** Git + GitHub/GitLab
- **Huấn Luyện Mô Hình:** TensorFlow/Keras hoặc PyTorch
- **Kiểm Tra:** pytest (trường hợp dùng), tập dữ liệu kiểm tra với nhãn sự thật cơ bản
- **Tài Liệu:** Sphinx (tài liệu mã), Markdown (hướng dẫn người dùng)

---

## Ghi Chú Cho Triển Khai

### Các Yếu Tố Thành Công Quan Trọng

1. **Hiệu Suất Thời Gian Thực:** Đạt 15+ FPS với tất cả các mô đun PHẢI CÓ chạy
2. **Độ Chính Xác Ngủ Gật:** >90% true positive rate, <1 cảnh báo sai/giờ
3. **Huấn Luyện CNN Nhận Dạng Hoạt Động:** Sưu tập 300+ mẫu mỗi hoạt động với tăng cường dữ liệu
4. **Phát Hiện Mạnh Mẽ:** Xác thực đa phương sử dụng (kết hợp posture đầu + hướng nhìn + EAR)
5. **Chấp Nhận Người Dùng:** Tinh chỉnh ngưỡng để giảm thiểu dương tính giả (mệt mỏi cảnh báo)

### Lịch Trình Phát Triển

- **Khoảng Thời Gian Ước Tính:** 10-20 tuần
- **Sprints:** 5-10 sprints (2 tuần mỗi sprint)
- **Giai Đoạn 1 (4-5 tuần):** Phát hiện cốt lõi (PBI-001 đến PBI-010)
- **Giai Đoạn 2 (3-4 tuần):** Ngủ gật & Bị Phân Tán (PBI-012 đến PBI-018)
- **Giai Đoạn 3 (4-5 tuần):** Nhận Dạng Hoạt Động (PBI-019 đến PBI-026)
- **Giai Đoạn 4 (2-3 tuần):** Tích Hợp Hệ Thống, Cảnh Báo, Bảng Điều Khiển (PBI-034, PBI-038, PBI-041, PBI-044)
- **Giai Đoạn 5 (2-3 tuần):** Kiểm Tra, Tối Ưu Hóa, Tài Liệu

### Yêu Cầu Kiểm Tra

- **Trường Hợp Dùng:** Mỗi mô đun phát hiện (PBI-001 đến PBI-026)
- **Kiểm Tra Tích Hợp:** Hiệu suất đường ống toàn diện
- **Tập Dữ Liệu Kiểm Tra:**
  - Ngủ Gật: 100+ trường hợp được gắn nhãn (ngáp, đóng mắt)
  - Hoạt Động: 700 trường hợp (100 mỗi hoạt động × 7)
  - Bị Phân Tán: 50+ trường hợp (quay đầu, hướng nhìn rời)
- **Kiểm Tra Trường:** 5-10 phiên lái xe thực tế (1-2 giờ mỗi phiên)
- **Kiểm Tra Hiệu Năng:** Hoạt động liên tục 8 giờ (kiểm tra áp lực)

### Giảm Nhẹ Rủi Ro

1. **Nút Cổ Báng Hiệu Năng:** Tối ưu hóa mô hình CNN (lượng tử hóa, cắt xén), sử dụng threading
2. **Mệt Mỏi Cảnh báo Sai:** Ngưỡng bảo thủ ban đầu, tinh chỉnh dựa trên phản hồi người dùng
3. **Độ Chính Xác CNN Nhận Dạng Hoạt Động:** Sưu tập tập dữ liệu đa dạng (300+ mẫu/hoạt động), tăng cường dữ liệu
4. **Sai Lệch EAR Nhân Khẩu Học:** Hiệu chỉnh mỗi tài xế trong quá trình đăng ký (PBI-027)
5. **Che Khuất Camera:** Giảm nhẹ uyển chuyển (sử dụng posture đầu nếu mắt bị che)

---

## Siêu Dữ Liệu Tài Liệu

- **Được Tạo Bởi:** Quy Trình Brainstorming BMAD
- **Ngày Phiên:** 2026-03-03
- **Tệp Phiên:** `brainstorming-session-2026-03-03-004815.md`
- **Xuất:** 2026-03-04
- **Định Dạng:** Markdown (Chi Tiết Đầy Đủ)
- **Tổng PBIs:** 45 mục trên 13 danh mục
- **Phiên Bản Tài Liệu:** 1.0

---

## Các Bước Tiếp Theo

1. **Ôn Tập & Xác Thực:** Ôn tập Tập Hợp Sản Phẩm này với cố vấn luận văn
2. **Tạo Câu Chuyện Người Dùng:** Ánh xạ PBIs thành Câu Chuyện Người Dùng (đã hoàn thành trong phiên brainstorming)
3. **Xác Định Tiêu Chí Chấp Nhận:** Tiêu chí có thể kiểm tra được cho mỗi PBI (đã hoàn thành cho những câu chuyện ưu tiên)
4. **Thiết Kế Kiến Trúc:** Thiết kế kiến trúc hệ thống dựa trên đường ống mô đun (tham khảo PBI-028)
5. **Lược Đồ Cơ Sở Dữ Liệu:** Lược đồ thiết kế cho ghi lại sự kiện, theo dõi phiên, quản lý tài xế
6. **Lập Kế Hoạch Sprint:** Tạo Sprint Backlog bằng lịch 10-20 tuần
7. **Bắt Đầu Phát Triển:** Bắt đầu với Giai Đoạn 1 (Phát Hiện Cốt Lõi - PBI-001 đến PBI-010)

---

*Kết Thúc Tài Liệu Tập Hợp Sản Phẩm*
