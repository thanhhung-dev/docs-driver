---
stepsCompleted:
  - step-01-validate-prerequisites
  - step-02-design-epics
inputDocuments:
  - _bmad-output/planning-artifacts/prd.md
  - _bmad-output/architecture/ARCHITECTURE-Driver-Monitoring-System.md
  - _bmad-output/ui-design/UI-INTERFACE-DESIGN-Driver-Monitoring-System.md
---

# Phân rã Epic & Story: docs-driver

## Tổng quan

Tài liệu này cung cấp danh sách đầy đủ các Epic và Story cho dự án docs-driver, được phân rã từ PRD, thiết kế UX và các yêu cầu kiến trúc thành các phần việc có thể triển khai được.

## Danh mục Yêu cầu

### Yêu cầu Chức năng (Functional Requirements)

- **FR1:** Phát hiện buồn ngủ dựa trên EAR (Eye Aspect Ratio).
- **FR2:** Phát hiện ngáp dựa trên MAR (Mouth Aspect Ratio).
- **FR3:** Tính toán PERCLOS (Tỉ lệ nhắm mắt) theo thời gian thực.
- **FR4:** Phát hiện xao nhãng dựa trên tư thế đầu (Pitch, Yaw, Roll).
- **FR5:** Theo dõi hướng nhìn (Gaze tracking).
- **FR6:** Nhận diện 7 hành vi nguy hiểm (gọi điện, hút thuốc, uống nước...).
- **FR7:** Cảnh báo âm thanh khi có rủi ro.
- **FR8:** Cảnh báo hình ảnh trên dashboard.
- **FR9:** Cảnh báo qua đèn LED (Giao tiếp GPIO).
- **FR10:** Phân cấp mức độ ưu tiên cảnh báo (Nghiêm trọng, Cảnh báo, Thông tin).
- **FR11:** Đăng ký tài xế mới (Face Enrollment - 5 góc chụp).
- **FR12:** Xác thực tài xế (Face Identification) khi khởi hành.
- **FR13:** Ghi nhật ký sự kiện vào SQLite.
- **FR14:** Lưu trữ ảnh chụp vi phạm (Snapshots).
- **FR15:** Hiển thị Dashboard giám sát thời gian thực.
- **FR16:** Hiển thị chỉ số FPS và trạng thái hệ thống.
- **FR17:** Màn hình cài đặt ngưỡng (Settings) cho EAR, MAR, Head Pose.
- **FR18:** Màn hình tóm tắt chuyến đi (Trip Summary).
- **FR19:** Cơ chế tự kiểm tra phần cứng (Camera Health Check).
- **FR20:** Cơ chế tự khởi động lại (Watchdog) khi tiến trình AI treo.

### Yêu cầu Phi chức năng (Non-Functional Requirements)

- **NFR1:** Tốc độ xử lý ≥ 15 FPS trên thiết bị nhúng (Jetson Nano/RPi 4).
- **NFR2:** Độ trễ cảnh báo < 100ms từ lúc thu hình đến lúc báo động.
- **NFR3:** Độ chính xác phát hiện buồn ngủ ≥ 90%.
- **NFR4:** Độ chính xác nhận diện hành vi nguy hiểm ≥ 85%.
- **NFR5:** Hoạt động ổn định trong điều kiện thiếu sáng với Camera IR.
- **NFR6:** Xử lý được các trường hợp tài xế đeo kính hoặc khẩu trang.
- **NFR7:** Quyền riêng tư: Xử lý tại biên (Edge AI), không lưu video thô.
- **NFR8:** Giao diện tối giản, hỗ trợ điều khiển cảm ứng.
- **NFR9:** Hệ thống chịu lỗi: Tự phục hồi sau khi mất điện đột ngột.

---

## Danh sách Epic

### Epic 1: Thiết lập Hệ thống & Xác thực Người lái
Thiết lập bộ khung phần mềm, giao diện cơ bản và khả năng nhận diện tài xế để khởi động phiên làm việc an toàn.
**Mục tiêu:** Tài xế có thể đăng ký thông tin và hệ thống định danh được người lái để cá nhân hóa dữ liệu và đảm bảo tính ổn định.

### Epic 2: Giám sát Buồn ngủ & Cảnh báo Tức thì
Phát hiện các dấu hiệu mệt mỏi qua mắt/miệng và phát tín hiệu cảnh báo đa phương thức để ngăn chặn tai nạn.
**Mục tiêu:** Phát hiện dấu hiệu mệt mỏi và đưa ra cảnh báo đa phương thức để tránh tai nạn.

### Epic 3: Giám sát Xao nhãng & Hướng nhìn
Phát hiện khi tài xế không tập trung nhìn đường dựa trên tư thế đầu và hướng mắt.
**Mục tiêu:** Theo dõi hướng đầu và ánh mắt để đảm bảo tài xế đang tập trung nhìn đường.

### Epic 4: Nhận diện Hành vi Nguy hiểm
Nhận diện các hành vi như gọi điện, hút thuốc, uống nước bằng các mô hình AI chuyên sâu.
**Mục tiêu:** Xác định các hành vi rủi ro cụ thể bằng mô hình Deep Learning.

### Epic 5: Quản lý Nhật ký & Báo cáo Chuyến đi
Lưu trữ lịch sử vi phạm và tổng kết hiệu quả lái xe an toàn sau mỗi chuyến đi.
**Mục tiêu:** Lưu trữ dữ liệu sự cố và cung cấp tóm tắt hiệu suất an toàn.

### Epic 6: Tối ưu hóa & Cấu hình Hệ thống
Tùy chỉnh độ nhạy của hệ thống và tối ưu hóa hiệu năng để chạy mượt mà trên phần cứng nhúng.
**Mục tiêu:** Tùy chỉnh hệ thống và tinh chỉnh hiệu năng để triển khai trên thiết bị biên.

---

## Các Story tiêu biểu (Trích dẫn)

### Story 2.1: Phát triển Thuật toán EAR & MAR
Là một Lập trình viên, tôi muốn xây dựng logic tính toán EAR và MAR từ các điểm mốc khuôn mặt, để hệ thống có thể nhận biết trạng thái mắt và miệng.
**Tiêu chí hoàn thành:** Logic tính toán hoạt động đúng trên PC, log lại trạng thái khi nhắm mắt hoặc há miệng.

### Story 4.2: Huấn luyện & Đánh giá Mô hình Phân loại
Là một Lập trình viên, tôi muốn huấn luyện mô hình Deep Learning (như MobileNetV2) để phân loại các hành vi tài xế, để hệ thống có thể nhận diện vi phạm với độ chính xác cao.
**Tiêu chí hoàn thành:** Mô hình đạt độ chính xác >85% trên tập kiểm thử và xuất ra file model định dạng `.tflite`.

### Story 6.2: Tối ưu hóa TensorRT & TFLite
Là một Lập trình viên, tôi muốn tối ưu hóa các mô hình AI bằng TensorRT hoặc TFLite Quantization, để đảm bảo hệ thống duy trì được mức FPS mục tiêu trên Jetson/Pi.
**Tiêu chí hoàn thành:** Hệ thống duy trì ổn định >15 FPS khi chạy tất cả các mô hình đồng thời trên phần cứng nhúng.
