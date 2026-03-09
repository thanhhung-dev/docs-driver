---
stepsCompleted: [1, 2, 3, 4, 5]
inputDocuments: ["_bmad-output/brainstorming/brainstorming-session-2026-03-03-004815.md", "_bmad-output/proposal/PROPOSAL-Driver-Monitoring-System.md", "_bmad-output/proposal/PROPOSAL-Driver-Monitoring-System-VI.md", "_bmad-output/guides/HUONG-DAN-DO-AN-TOT-NGHIEP.md", "_bmad-output/planning-artifacts/prd.md"]
date: 2026-03-08
author: hung-thanh
---

# Product Brief: docs-driver

## Executive Summary
**docs-driver** is an advanced Driver Monitoring System (DMS) that utilizes AI and computer vision to detect signs of fatigue, drowsiness, and distraction in real-time. The project aims to reduce traffic accidents by providing immediate alerts and analyzing driving behavior, supporting both individuals and transport enterprises in road safety management.

---

## Core Vision

### Problem Statement
Every year, millions of traffic accidents occur due to human error, with fatigue, drowsiness, and lack of focus (using phones, not looking at the road) being leading causes. Existing in-vehicle warning systems are often not sensitive enough or lack personalization to prevent dangerous situations in time.

### Problem Impact
- **Human:** Causes casualties and health losses for drivers and passengers.
- **Economic:** Significant damage to vehicles, goods, and insurance costs for transport fleets.
- **Social:** Places pressure on the healthcare system and public traffic safety.

### Why Existing Solutions Fall Short
- **Traditional Systems:** Rely on steering wheel or vehicle sensors, which sometimes react too slowly once the driver has already lost control.
- **Fragmented Monitoring Devices:** Lack of synchronization, high latency in image processing, and often struggle in low light or when the driver wears glasses.
- **Cost:** High-end DMS systems are usually only available in luxury vehicles, making them inaccessible to the majority of drivers and small businesses.

### Proposed Solution
An AI-integrated DMS system capable of:
- **Edge Processing:** Analyzing images directly on the device to ensure immediacy.
- **Multi-state Detection:** Identifying drowsiness (yawning, closed eyes), distraction (looking sideways, using a phone), and smoking.
- **Multi-modal Alerts:** Audio, visual, and notifications to a central management system.

### Key Differentiators
- **High Accuracy:** Uses optimized Deep Learning models for face and landmark recognition.
- **Robust Performance:** Effective in all lighting conditions (IR LEDs) and supports drivers wearing glasses.
- **Ecosystem Integration:** Ability to connect with mobile apps and Fleet Management platforms to track history and assess risks.

---

## Target Users

### Primary Users

#### Persona: Anh Hùng - Tài xế đường dài (Xe container/xe khách)
- **Context:** Lái xe xuyên đêm, chịu áp lực thời gian và mệt mỏi thể chất kéo dài.
- **Problem:** Dễ rơi vào trạng thái ngủ gật micro-sleep mà không tự nhận diện được.
- **Success:** Luôn tỉnh táo nhờ cảnh báo kịp thời, giảm thiểu rủi ro tai nạn nghiêm trọng.

#### Persona: Bạn Lan - Tài xế cá nhân mới lái
- **Context:** Di chuyển trong đô thị, dễ xao nhãng bởi điện thoại hoặc áp lực công việc.
- **Problem:** Thiếu tập trung vào gương chiếu hậu hoặc nhìn đường, dẫn đến va chạm nhỏ.
- **Success:** Hình thành thói quen lái xe tập trung và an toàn hơn.

### Secondary Users
- **Chủ doanh nghiệp vận tải:** Quản lý an toàn đội xe, giảm chi phí sửa chữa và bảo hiểm thông qua dữ liệu báo cáo hành vi tài xế.
- **Gia đình tài xế:** Yên tâm về sự an toàn của người thân khi lưu thông trên đường.

### User Journey (Anh Hùng - Tài xế đường dài)
- **Discovery:** Nghe từ đồng nghiệp về thiết bị hỗ trợ an toàn.
- **Onboarding:** Dễ dàng lắp đặt và kích hoạt hệ thống trên cabin.
- **Core Usage:** Hệ thống giám sát âm thầm, chỉ cảnh báo khi phát hiện dấu hiệu mệt mỏi/xao nhãng thực sự.
- **Success Moment:** Được cảnh báo và tránh được một vụ va chạm khi buồn ngủ vào lúc rạng sáng.
- **Long-term:** Cải thiện ý thức lái xe và tăng cường niềm tin từ gia đình/chủ xe.

---

## Success Metrics (Chỉ số Thành công cho Đồ án)

### Mục tiêu Học thuật & Kỹ thuật
*   **Độ chính xác mô hình (Model Accuracy):** 
    *   Phát hiện buồn ngủ (Drowsiness): > 90%
    *   Nhận diện hoạt động nguy hiểm (Activity Recognition): > 85%
    *   Tỉ lệ dương tính giả (False Positive Rate): < 5% (Tránh cảnh báo sai gây phiền)
*   **Hiệu suất thời gian thực (Real-time Performance):**
    *   Tốc độ xử lý khung hình (FPS): > 15 FPS trên thiết bị nhúng (Raspberry Pi 4 / Jetson Nano).
    *   Độ trễ hệ thống (Latency): < 100ms từ khi phát hiện đến khi phát cảnh báo.
*   **Khả năng thích nghi (Robustness):**
    *   Hoạt động ổn định trong điều kiện thiếu sáng (sử dụng Camera IR).
    *   Xử lý được các trường hợp tài xế đeo kính hoặc khẩu trang.

### Tiêu chí Hoàn thành Đồ án (Deliverables)
*   **Sản phẩm phần cứng:** Một Prototype hoạt động ổn định, có thể demo trực tiếp trước hội đồng.
*   **Mã nguồn (Source Code):** Tổ chức code sạch, đúng tiêu chuẩn, có đầy đủ Unit Test và tài liệu hướng dẫn (README, API docs).
*   **Báo cáo (Documentation):** Hoàn thành đầy đủ 13 đầu mục tài liệu theo yêu cầu (Proposal, Architecture, Test Plan, Reflection...).
*   **Tập dữ liệu (Dataset):** Xây dựng hoặc tổng hợp được bộ dữ liệu thử nghiệm đa dạng (buồn ngủ, ngáp, gọi điện, hút thuốc...).

### Chỉ số đánh giá từ Hội đồng (KPIs cho buổi Bảo vệ)
*   **Demo thành công:** Hệ thống phát hiện và cảnh báo đúng ít nhất 7 loại hành vi nguy hiểm ngay tại chỗ.
*   **Trả lời phản biện:** Giải trình rõ ràng về kiến trúc hệ thống, lựa chọn thuật toán (EAR, MAR, CNN...) và các kỹ thuật tối ưu hóa.

---

## MVP Scope (Phạm vi Đồ án)

### Tính năng Cốt lõi (Core Features)
*   **Giám sát buồn ngủ (Drowsiness Detection):** Phát hiện nhắm mắt (Eye closure) và ngáp (Yawning) dựa trên EAR và MAR.
*   **Giám sát mất tập trung (Distraction Detection):** Theo dõi hướng đầu (Head pose) và hướng nhìn (Gaze direction).
*   **Nhận diện hành vi nguy hiểm (Activity Recognition):** Phát hiện gọi điện thoại (Calling), uống nước (Drinking), hút thuốc (Smoking).
*   **Hệ thống cảnh báo thời gian thực (Real-time Alert):** Cảnh báo bằng âm thanh (Audio) và hình ảnh (Visual) ngay lập tức khi phát hiện rủi ro.
*   **Ghi nhật ký sự kiện (Event Logging):** Lưu trữ toàn bộ dữ liệu vi phạm và ảnh chụp (Snapshots) vào cơ sở dữ liệu để phục vụ hậu kiểm.
*   **Giao diện Dashboard:** Hiển thị trạng thái giám sát thời gian thực và lịch sử các cảnh báo.
*   **Xác thực người lái (Driver Authentication):** Sử dụng nhận diện khuôn mặt để định danh tài xế trước khi bắt đầu hành trình.

### Ngoài phạm vi MVP (Out of Scope)
*   Ứng dụng di động (Mobile App).
*   Đồng bộ hóa dữ liệu đám mây (Cloud Sync).
*   Quản lý đội xe tập trung (Fleet Management).
*   Tích hợp trực tiếp vào hệ thống cơ khí/điện tử của xe.
*   Tính năng tự lái (Autonomous driving).

### Tiêu chí Thành công của MVP
*   Hệ thống chạy ổn định trên phần cứng nhúng (Raspberry Pi/Jetson Nano).
*   Vượt qua các bài kiểm tra Unit Test và Integration Test đã lập kế hoạch.
*   Đạt được độ chính xác >90% trong điều kiện thử nghiệm thực tế cho các tính năng cốt lõi.

### Tầm nhìn Tương lai (Future Vision)
*   Mở rộng hệ thống ADAS (Hỗ trợ lái xe nâng cao) tích hợp cảnh báo va chạm.
*   Phát triển phiên bản kết nối Cloud để quản lý tập trung cho các hãng vận tải lớn.
*   Ứng dụng AI để phân tích tâm lý và mức độ căng thẳng của tài xế qua nét mặt.
