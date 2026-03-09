---
stepsCompleted:
  - step-01-init
  - step-02-discovery
  - step-02b-vision
  - step-02c-executive-summary
  - step-01b-continue
  - step-03-success
  - step-04-journeys
  - step-05-domain
  - step-06-innovation

... (giữ nguyên phần nội dung cũ cho đến hết phần Risk Mitigations trong Domain-Specific Requirements) ...

## Innovation & Novel Patterns

### Detected Innovation Areas
*   **Edge AI Performance:** Tối ưu hóa các mô hình nhận diện hành vi (7+ loại) để chạy mượt mà (>15 FPS) trên thiết bị nhúng. Đây là một thách thức kỹ thuật lớn so với việc chạy trên máy tính mạnh.
*   **Multi-state Integrated Monitoring:** Kết hợp đồng thời nhiều trạng thái (Drowsiness + Distraction + Dangerous Activities) vào một hệ thống duy nhất thay vì chỉ tập trung vào một khía cạnh.
*   **Low-cost IR Integration:** Sử dụng giải pháp Camera IR giá rẻ nhưng đạt được độ chính xác cao trong môi trường thiếu sáng, tăng tính khả thi cho việc triển khai đại trà.

### Market Context & Competitive Landscape
*   **Academic vs. Commercial:** Dự án thu hẹp khoảng cách giữa các giải pháp thương mại đắt tiền (thường chỉ có trên xe hạng sang) và các giải pháp mã nguồn mở rời rạc, tạo ra một hệ thống tích hợp hoàn chỉnh phù hợp cho nghiên cứu và thực nghiệm.

### Validation Approach
*   **Benchmarking:** Đo lường FPS và độ trễ (Latency) trực tiếp trên phần cứng đích (Jetson/Pi).
*   **Dataset Testing:** Kiểm thử độ chính xác trên các bộ dữ liệu chuẩn (như YawDD) và bộ dữ liệu tự thu thập trong các điều kiện thực tế (đeo kính, đeo khẩu trang, đêm tối).
*   **Field Testing:** Thử nghiệm thực tế với tài xế thật để đánh giá tỉ lệ cảnh báo sai (False Positives).

### Risk Mitigation
*   **Rủi ro hiệu năng:** Nếu FPS quá thấp, sẽ áp dụng các kỹ thuật như **Quantization** (chuyển đổi model sang định dạng nhẹ hơn như TensorRT hoặc TFLite).
*   **Rủi ro nhận diện:** Nếu điều kiện ánh sáng quá khắc nghiệt, sẽ điều chỉnh ngưỡng EAR/MAR động dựa trên độ sáng môi trường.


... (giữ nguyên phần nội dung cũ cho đến hết phần Journey Requirements Summary) ...

## Domain-Specific Requirements

### Compliance & Regulatory
*   **Tiêu chuẩn An toàn Chức năng (Functional Safety):** Tham chiếu các nguyên lý cơ bản của **ISO 26262** về an toàn phần mềm trong ô tô (mức độ nghiên cứu). Đảm bảo hệ thống không gây xao nhãng thêm cho tài xế.
*   **Quy định về Quyền riêng tư (Privacy):** Dữ liệu hình ảnh tài xế được xử lý tại biên (on-device). Chỉ lưu trữ vector đặc trưng (embeddings) và ảnh chụp sự kiện vi phạm (snapshots) vào database cục bộ.

### Technical Constraints
*   **Xử lý thời gian thực (Real-time):** Độ trễ từ khi camera thu hình đến khi phát âm thanh cảnh báo không vượt quá 100ms. Duy trì tốc độ xử lý > 15 FPS trên thiết bị nhúng.
*   **Điều kiện ánh sáng:** Hoạt động ổn định trong điều kiện thiếu sáng (dưới 10 lux) bằng Camera hồng ngoại (IR) và đèn LED IR.
*   **Khả năng chịu lỗi (Fault Tolerance):** Có cơ chế Watchdog tự khởi động lại tiến trình AI nếu bị treo và cảnh báo lỗi phần cứng camera.

### Integration Requirements
*   **Hardware Interface:** Giao tiếp I2C/GPIO để điều khiển còi báo động (Buzzer) hoặc LED cảnh báo ngoài màn hình.
*   **Database:** Sử dụng SQLite để lưu trữ nhật ký sự kiện, đảm bảo ghi dữ liệu nhanh và chịu được việc mất điện đột ngột.

### Risk Mitigations
*   **Rủi ro AI nhận diện sai (False Positives):** Sử dụng kỹ thuật **Temporal Smoothing** (ví dụ: cảnh báo buồn ngủ nếu mắt nhắm liên tục trong N khung hình) để giảm nhiễu.
*   **Rủi ro phần cứng quá nhiệt:** Giám sát nhiệt độ CPU/GPU của thiết bị nhúng (Jetson/Pi) và có cơ chế hạ nhiệt hoặc giảm tải xử lý khi cần.


... (giữ nguyên phần nội dung cũ cho đến hết phần Vision) ...

## User Journeys

### Hành trình 1: Anh Hùng - Đường dài và Cú giật mình cứu mạng (Happy Path)
*   **Bối cảnh:** 2 giờ sáng, Anh Hùng đang lái xe tải trên cao tốc vắng. Mắt anh bắt đầu lim dim, đầu hơi gục xuống.
*   **Điểm chạm (Touchpoint):** Camera IR quét khuôn mặt, hệ thống tính toán EAR liên tục thấp hơn ngưỡng 0.25 trong 3 giây.
*   **Hành động của hệ thống:** Một tiếng "Bíp" kéo dài kèm giọng nói nhắc nhở: "Anh Hùng, phát hiện buồn ngủ! Hãy dừng xe nghỉ ngơi ngay!".
*   **Kết quả:** Anh Hùng tỉnh táo lại, tấp xe vào lề đường, nhận ra mình vừa thoát một tình huống nguy hiểm. Hệ thống ghi lại sự kiện này kèm ảnh chụp vào nhật ký.

### Hành trình 2: Bạn Lan - Thói quen và Sự tập trung (Edge Case - Distraction)
*   **Bối cảnh:** Lan đang lái xe đi làm, điện thoại có thông báo. Cô cúi xuống nhìn màn hình điện thoại đặt ở hộc để đồ quá 2 giây.
*   **Điểm chạm:** Hệ thống xác định Head Pose (Pitch < -20 độ).
*   **Hành động của hệ thống:** Hiển thị biểu tượng cảnh báo màu vàng trên Dashboard và phát âm thanh nhắc nhở nhẹ: "Vui lòng tập trung nhìn đường!".
*   **Kết quả:** Lan giật mình cất điện thoại và tập trung lái xe. Cô nhận ra mình đã xao nhãng bao lâu nay mà không biết.

### Hành trình 3: Người vận hành (Admin/Operations) - Kiểm tra và Cài đặt
*   **Bối cảnh:** Trước khi chạy thử nghiệm, sinh viên/người vận hành cần đăng ký khuôn mặt cho một tài xế mới (Face Enrollment).
*   **Điểm chạm:** Giao diện Dashboard, mục "Quản lý tài xế".
*   **Hành động của hệ thống:** Yêu cầu tài xế nhìn thẳng, nghiêng trái, nghiêng phải để lấy 68 điểm landmark và lưu vector đặc trưng (128D).
*   **Kết quả:** Tài xế mới được lưu vào database, hệ thống sẵn sàng xác thực (Authentication) mỗi khi người này ngồi vào ghế lái.

### Hành trình 4: Sự cố Camera - Xử lý lỗi (Support/Troubleshooting)
*   **Bối cảnh:** Camera bị lỏng cáp hoặc bị che khuất bởi vật cản.
*   **Hành động của hệ thống:** Dashboard lập tức chuyển sang trạng thái đỏ, hiển thị lỗi "Camera Disconnected/Blocked" và phát âm thanh cảnh báo lỗi hệ thống.
*   **Kết quả:** Người dùng biết hệ thống đang không bảo vệ mình và thực hiện kiểm tra kết nối.

### Journey Requirements Summary
*   **Khả năng nhận diện:** Tính toán EAR (buồn ngủ) và Head Pose (xao nhãng) thời gian thực.
*   **Hệ thống cảnh báo:** Phân cấp nhiều mức độ (Nhắc nhở nhẹ - Cảnh báo nguy hiểm - Cảnh báo lỗi hệ thống).
*   **Quản lý dữ liệu:** Chức năng đăng ký (Enrollment) và Nhật ký sự kiện (Logging) bắt buộc.
*   **Xử lý ngoại lệ:** Cơ chế tự kiểm tra trạng thái phần cứng (Camera Health Check).


... (giữ nguyên phần nội dung cũ cho đến hết phần Project Classification) ...

## Success Criteria

### User Success
*   **Cảnh báo kịp thời:** Tài xế nhận được cảnh báo âm thanh và hình ảnh trong vòng dưới 2 giây kể từ khi có dấu hiệu buồn ngủ/xao nhãng.
*   **Độ tin cậy cao:** Tỉ lệ dương tính giả (cảnh báo sai khi tài xế vẫn tỉnh táo) thấp hơn 5%, giúp tài xế không cảm thấy bị làm phiền và luôn bật thiết bị.
*   **Hoạt động mọi điều kiện:** Hệ thống vẫn hoạt động chính xác khi tài xế đeo kính hoặc lái xe trong điều kiện thiếu sáng (ban đêm).

### Business Success
*   **Hoàn thành đúng hạn:** Đồ án được hoàn thành và bảo vệ thành công trong vòng 12 tuần với đầy đủ 13 đầu mục tài liệu.
*   **Tính khả thi cao:** Prototype hoạt động ổn định trên thiết bị nhúng (Jetson Nano/Raspberry Pi) với chi phí phần cứng tối ưu cho sinh viên.
*   **Đánh giá từ Hội đồng:** Được đánh giá cao về tính thực tiễn, khả năng áp dụng Deep Learning vào bài toán an toàn giao thông.

### Technical Success
*   **Model Accuracy:** Độ chính xác phát hiện buồn ngủ > 90%; nhận diện hành vi nguy hiểm > 85%.
*   **Real-time Processing:** Duy trì tốc độ xử lý trên 15 FPS trên thiết bị nhúng.
*   **Độ trễ hệ thống:** Thời gian từ lúc camera thu hình đến khi phát cảnh báo < 100ms.

### Measurable Outcomes
*   Hệ thống nhận diện thành công ít nhất 7 loại hành vi nguy hiểm (ngáp, nhắm mắt, nhìn nghiêng, dùng điện thoại, hút thuốc, uống nước, không nhìn đường).
*   Ghi lại chính xác 100% các sự kiện vi phạm vào database kèm ảnh chụp snapshot.

## Product Scope

### MVP - Minimum Viable Product
*   Phát hiện buồn ngủ (EAR, MAR) và xao nhãng (Head pose).
*   Nhận diện 7 hành vi nguy hiểm cốt lõi.
*   Cảnh báo âm thanh/hình ảnh tại chỗ.
*   Ghi log sự kiện vào SQLite địa phương.
*   Giao diện Dashboard theo dõi thời gian thực.
*   Xác thực người lái (Face Recognition).

### Growth Features (Post-MVP)
*   Tích hợp ADAS (Cảnh báo va chạm phía trước).
*   Phát triển giao diện quản lý tập trung cho doanh nghiệp nhỏ.
*   Tối ưu hóa các model Deep Learning để tăng FPS.

### Vision (Future)
*   Kết nối Cloud để phân tích dữ liệu hành trình quy mô lớn.
*   Tích hợp vào hệ thống xe thông minh (Connected Cars).
*   Ứng dụng AI phân tích Stress và sức khỏe tài xế.

inputDocuments:
  - _bmad-output/architecture/ARCHITECTURE-Driver-Monitoring-System.md
  - _bmad-output/database/DATABASE-DESIGN-Driver-Monitoring-System.md
  - _bmad-output/ui-design/UI-INTERFACE-DESIGN-Driver-Monitoring-System.md
  - _bmad-output/proposal/PROPOSAL-Driver-Monitoring-System.md
  - _bmad-output/project-plan/PROJECT-PLAN-Driver-Monitoring-System.md
  - _bmad-output/exports/Product-Backlog-DMS.md
  - _bmad-output/brainstorming/brainstorming-session-2026-03-03-004815.md
  - _bmad-output/guides/HUONG-DAN-DO-AN-TOT-NGHIEP.md
classification:
  projectType: iot_embedded
  domain: automotive
  complexity: medium
  projectContext: brownfield
workflowType: 'prd'
---

# Product Requirements Document - docs-driver

**Author:** BMAD Workflow
**Date:** 2026-03-06

## Executive Summary

The Driver Monitoring System (DMS) is an AI-powered safety solution designed to prevent traffic accidents caused by driver drowsiness and distraction. Using computer vision and deep learning algorithms, the system provides real-time monitoring and alerting capabilities to individual drivers through an embedded IoT platform.

**Target Users:** Individual drivers, particularly those on long-distance routes where drowsiness and distraction pose significant safety risks. The system can be extended to fleet monitoring applications for commercial transportation companies.

**Problem Statement:** Driver drowsiness and distraction are leading causes of traffic accidents. Current solutions are either too expensive for individual adoption or lack comprehensive behavior detection capabilities. This project addresses the need for an affordable, accurate, and real-time driver safety monitoring system suitable for academic validation and proof-of-concept demonstration.

**Project Scope:** This is a thesis/graduation project focused on technical validation and demonstration of AI/Computer Vision applications in real-world traffic safety scenarios. The system is designed as a functional prototype running on cost-effective embedded hardware (Jetson Nano or Raspberry Pi) with IR camera integration.

### What Makes This Special

**Multi-dimensional Behavior Detection:** Unlike basic drowsiness detection systems, this solution identifies 7 distinct types of dangerous driving behaviors including drowsiness, distraction, and other unsafe activities, providing comprehensive safety coverage.

**Real-time Performance on Embedded Hardware:** Achieves >15 FPS processing speed on affordable embedded platforms (Jetson Nano/Raspberry Pi), demonstrating that advanced AI/Computer Vision can run efficiently on resource-constrained devices without requiring cloud connectivity or expensive hardware.

**Academic Research Value:** Applies state-of-the-art AI/Computer Vision techniques (OpenCV, dlib, TensorFlow) to a practical traffic safety problem, providing technical validation of algorithmic approaches and system architecture for embedded driver monitoring applications.

**Target Performance Metrics:**
- Drowsiness detection accuracy: >90%
- Dangerous activity recognition accuracy: >85%
- Real-time processing: >15 FPS
- Cost-effective hardware deployment

## Project Classification

- **Project Type:** IoT/Embedded System
- **Domain:** Automotive (Academic/Research Context)
- **Complexity:** Medium (thesis project - proof of concept)
- **Project Context:** Brownfield (extensive project documentation, architecture, database design, UI design, and product backlog with 45 items already exist)
- **Technology Stack:** Python, OpenCV, dlib, TensorFlow, IR Camera, Jetson Nano/Raspberry Pi
