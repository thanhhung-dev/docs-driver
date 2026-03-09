---
stepsCompleted: [1, 2, 3, 4, 5, 6]
inputDocuments: []
workflowType: 'research'
lastStep: 1
research_type: 'technical'
research_topic: 'Driver Monitoring System Model Techniques'
research_goals: 'Xác định các mô hình AI/ML phù hợp để phát hiện buồn ngủ, xao nhãng và hành vi tài xế đáp ứng các ràng buộc về hiệu năng thời gian thực trên thiết bị nhúng.'
user_name: 'hung-thanh'
date: '2026-03-10'
web_research_enabled: true
source_verification: true
---

# Báo cáo Nghiên cứu Kỹ thuật: Hệ thống Giám sát Tài xế (DMS)

**Ngày:** 2026-03-10
**Tác giả:** hung-thanh
**Loại nghiên cứu:** Kỹ thuật (Technical)

---

## Tổng quan Nghiên cứu (Research Overview)

Nghiên cứu này tập trung vào việc xác định các kỹ thuật mô hình AI và kiến trúc hệ thống tối ưu cho **Hệ thống Giám sát Tài xế (DMS)** trong bối cảnh công nghệ năm 2026. Phạm vi nghiên cứu bao gồm phân tích các stack công nghệ hiện đại, các mẫu kiến trúc an toàn cho ô tô (ISO 26262), và các phương pháp triển khai hiệu năng cao trên thiết bị nhúng như NVIDIA Jetson.

Các phát hiện chính cho thấy sự chuyển dịch mạnh mẽ sang các kiến trúc **Hybrid CNN-Transformer** (như YOLOv11n) và việc sử dụng **NVIDIA TensorRT** với định dạng **INT8** là yếu tố quyết định để đạt được độ trễ <30ms. Chi tiết về các đề xuất chiến lược và lộ trình triển khai được trình bày cụ thể trong phần **Khuyến nghị Nghiên cứu Kỹ thuật** của báo cáo này.

---

## Tóm tắt Điều hành (Executive Summary)

Hệ thống DMS năm 2026 đã trở thành một thành phần an toàn bắt buộc theo các quy định toàn cầu (như EU GSR2). Nghiên cứu này xác định các kỹ thuật tối ưu nhất để triển khai trên thiết bị biên (Edge) nhằm phát hiện buồn ngủ, xao nhãng và 7+ hành vi nguy hiểm với độ chính xác cao và độ trễ cực thấp.

**Các phát hiện kỹ thuật cốt lõi:**
- **Kiến trúc**: Sử dụng mô hình **Hybrid (CNN + Transformer)** để kết hợp ưu điểm của việc trích xuất đặc trưng cục bộ và bối cảnh toàn cục.
- **Tối ưu hóa**: **TensorRT INT8** là chìa khóa để chạy đa mô hình trên Jetson Orin Nano mà vẫn duy trì FPS cao.
- **Tích hợp**: Ưu tiên **gRPC** cho giao tiếp nội bộ và **FlatBuffers** để giảm thiểu độ trễ dữ liệu (Zero-Copy).
- **Tuân thủ**: Thiết kế phải đáp ứng tiêu chuẩn an toàn chức năng **ISO 26262** và bảo mật quyền riêng tư dữ liệu (xử lý hoàn toàn tại thiết bị).

---

## 1. Phân tích Stack Công nghệ (Technology Stack)

### Ngôn ngữ Lập trình
- **Python**: Dùng cho phát triển logic bậc cao và thử nghiệm mô hình AI.
- **C++**: Bắt buộc cho môi trường production để tối ưu hóa xử lý video và TensorRT, đảm bảo độ trễ <100ms.
- **Rust**: Đang nổi lên trong năm 2026 cho các ứng dụng ô tô nhờ tính an toàn bộ nhớ mà không cần Garbage Collector.

### Framework và Thư viện
- **TensorRT (NVIDIA)**: Tiêu chuẩn vàng để tăng tốc suy luận trên Jetson.
- **MediaPipe**: Lựa chọn hàng đầu cho Face Mesh 468 điểm để tính toán chỉ số EAR/MAR.
- **YOLOv11n**: Phiên bản Nano của YOLOv11 mang lại sự cân bằng hoàn hảo giữa tốc độ và độ chính xác cho nhận diện hành vi.

### Lưu trữ và Cơ sở dữ liệu
- **SQLite**: Tin cậy cho việc ghi log sự kiện và kiểm toán.
- **DuckDB**: Giải pháp thay thế SQLite cho việc phân tích dữ liệu AI trực tiếp tại thiết bị.
- **FRAM (Ferroelectric RAM)**: Loại bộ nhớ độ bền cao dùng cho EDR (Hộp đen) để lưu dữ liệu pre-crash.

---

## 2. Mẫu Tích hợp và Giao tiếp (Integration Patterns)

### Thiết kế API và Giao thức
- **gRPC**: Lựa chọn số 1 cho các microservices nội bộ nhờ hiệu suất cao và khả năng streaming hai chiều.
- **MQTT over QUIC**: Tiêu chuẩn mới cho việc truyền telemetry từ xe lên Cloud ổn định trong điều kiện mạng yếu.
- **FlatBuffers**: Cơ chế Zero-Copy giúp truyền dữ liệu cảm biến (tọa độ mắt, hướng nhìn) với độ trễ tối thiểu.

### Kiến trúc hướng sự kiện (Event-Driven)
- Sử dụng **ZeroMQ** hoặc **Zenoh** để phát sóng (broadcast) các sự kiện "Phát hiện buồn ngủ" đến hệ thống UI, còi báo và hệ thống phanh trong vòng **dưới 10ms**.

---

## 3. Mẫu Kiến trúc và Thiết kế (Architectural Patterns)

### Kiến trúc Hệ thống
- **Hybrid Edge-Cloud**: Suy luận an toàn diễn ra tại biên (trong xe), Cloud dùng cho **Federated Learning** để cập nhật mô hình mà không cần gửi video thô ra ngoài.
- **NPU Dominance**: Tận dụng bộ tăng tốc NPU trên chip để giám sát "luôn bật" (always-on) với mức tiêu thụ điện năng cực thấp.

### Nguyên tắc Thiết kế An toàn
- **Checkerboard Pattern**: Các mô hình AI (không định sẵn) được giám sát bởi các bộ "Safety Checker" truyền thống (định sẵn) để đảm bảo an toàn tối đa.
- **Graceful Degradation**: Thiết kế hệ thống tự động trả lại quyền điều khiển hoặc tấp xe vào lề an toàn khi gặp điều kiện ngoài phạm vi hoạt động (ODD).

---

## 4. Nghiên cứu Triển khai (Implementation Research)

### Quy trình Phát triển (DevOps)
- Sử dụng **Virtual ECUs (vECUs)** và **Digital Twins** trên Cloud để thực hiện 90% việc kiểm thử mà không cần phần cứng thật.
- **Shadow Mode**: Chạy mô hình mới ngầm dưới nền để so sánh với hành vi thực của tài xế trước khi kích hoạt chính thức.

### Tối ưu hóa Hiệu năng
- **Quantization (INT8)**: Chuyển đổi mô hình từ FP32 sang INT8 giúp tăng tốc 2-4 lần trên Jetson Orin Nano.
- **Headless Operation**: Tắt giao diện GUI của Ubuntu để giải phóng ~500MB RAM cho các mô hình AI.

---

## 5. Khuyến nghị Nghiên cứu Kỹ thuật

### Lộ trình Triển khai (Implementation Roadmap)
1. **Giai đoạn 1 (Tháng 1-2)**: Lựa chọn mô hình (YOLOv11n + MediaPipe) và thực hiện quantize INT8 cho Jetson Orin Nano.
2. **Giai đoạn 2 (Tháng 3-4)**: Tích hợp driver camera hồng ngoại (NIR) và triển khai giao tiếp nội bộ bằng gRPC.
3. **Giai đoạn 3 (Tháng 5-6)**: Triển khai bộ đệm vòng EDR (20 giây) và logging sự kiện bằng DuckDB.
4. **Giai đoạn 4 (Tháng 7+)**: Kiểm thử thực địa với đa dạng nhân chủng học và tinh chỉnh qua Shadow Mode.

### Stack Công nghệ Đề xuất
- **Inference AI**: C++ với NVIDIA TensorRT và DeepStream SDK.
- **Mô hình**: YOLOv11n (Hành vi) + MediaPipe (Face Mesh/EAR/MAR).
- **Giao tiếp**: gRPC (Nội bộ); MQTT over QUIC (Cloud).
- **Lưu trữ**: SQLite (Log); DuckDB (Phân tích AI); FRAM (EDR).
- **Phần cứng**: Jetson Orin Nano Super + Camera NIR + Còi báo 12V DC.

### Chỉ số Thành công (KPIs)
- **Độ trễ suy luận**: Dưới 30ms cho các vòng lặp an toàn cốt lõi.
- **Độ chính xác**: >98% cho phát hiện buồn ngủ; >95% cho 7+ hành vi nguy hiểm.
- **Tỷ lệ báo động giả**: <3% để đảm bảo sự tin tưởng của tài xế.
- **Độ ổn định**: Uptime 99.9% với khả năng tự phục hồi qua Watchdog.

---

## Kết luận

Bản nghiên cứu kỹ thuật này khẳng định rằng việc triển khai một hệ thống DMS hiện đại năm 2026 trên thiết bị biên là hoàn toàn khả thi. Việc kết hợp giữa các kiến trúc mô hình mới (Hybrid CNN-Transformer) và các kỹ thuật tối ưu hóa phần cứng (INT8/NPU) sẽ đảm bảo hệ thống đáp ứng cả về mặt hiệu năng lẫn các tiêu chuẩn an toàn khắt khe của ngành ô tô.

**Ngày hoàn tất:** 2026-03-10
**Mức độ tin cậy:** Cao
