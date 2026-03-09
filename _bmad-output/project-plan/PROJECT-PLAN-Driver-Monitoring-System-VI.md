# KẾ HOẠCH DỰ ÁN
## Hệ thống Giám sát Tài xế sử dụng Thị giác Máy tính và AI

---

**Tên dự án:** Driver Monitoring System (DMS)  
**Quản lý dự án / Sinh viên thực hiện:** Hung Thanh  
**Giảng viên hướng dẫn:** [Advisor Name]  
**Ngày bắt đầu:** March 4, 2026  
**Ngày hoàn thành mục tiêu:** May 27, 2026  
**Thời lượng:** 12 tuần (84 ngày)  
**Loại dự án:** Khóa luận tốt nghiệp / Capstone Project  
**Trạng thái:** Giai đoạn lập kế hoạch

---

## MỤC LỤC

1. [Tóm tắt điều hành](#1-tóm-tắt-điều-hành)
2. [Tổ chức dự án](#2-tổ-chức-dự-án)
3. [Cấu trúc phân rã công việc (WBS)](#3-cấu-trúc-phân-rã-công-việc-wbs)
4. [Lịch chi tiết và biểu đồ Gantt](#4-lịch-chi-tiết-và-biểu-đồ-gantt)
5. [Lập kế hoạch Sprint (Agile Scrum)](#5-lập-kế-hoạch-sprint-agile-scrum)
6. [Phân bổ nguồn lực](#6-phân-bổ-nguồn-lực)
7. [Kế hoạch quản lý rủi ro](#7-kế-hoạch-quản-lý-rủi-ro)
8. [Kế hoạch quản lý chất lượng](#8-kế-hoạch-quản-lý-chất-lượng)
9. [Kế hoạch truyền thông](#9-kế-hoạch-truyền-thông)
10. [Ngân sách và ước tính chi phí](#10-ngân-sách-và-ước-tính-chi-phí)
11. [Mốc và sản phẩm bàn giao](#11-mốc-và-sản-phẩm-bàn-giao)
12. [Chỉ số thành công](#12-chỉ-số-thành-công)
13. [Giả định và ràng buộc](#13-giả-định-và-ràng-buộc)

---

## 1. TÓM TẮT ĐIỀU HÀNH

### 1.1 Tổng quan dự án

Dự án Driver Monitoring System (DMS) hướng tới xây dựng một hệ thống giám sát an toàn tài xế theo thời gian thực, sử dụng AI, thị giác máy tính và học máy. Hệ thống phát hiện buồn ngủ, mất tập trung và các hành vi lái xe nguy hiểm, sau đó phát cảnh báo tức thời để hỗ trợ phòng tránh tai nạn.

### 1.2 Mục tiêu dự án

- Xây dựng nguyên mẫu hoạt động với 24+ tính năng cốt lõi
- Đạt độ chính xác >90% cho phát hiện buồn ngủ
- Đạt độ chính xác >85% cho nhận diện hành vi
- Xử lý video thời gian thực (>15 FPS)
- Hoàn thành đúng hạn 13 đầu mục bàn giao của khóa luận

### 1.3 Cách tiếp cận dự án

Dự án theo **phương pháp Agile Scrum** với:
- 5 sprint, mỗi sprint 2 tuần (sau 2 tuần lập kế hoạch ban đầu)
- Họp giảng viên hướng dẫn hằng tuần để review và điều chỉnh
- Phát triển lặp, kiểm thử liên tục
- Ưu tiên theo rủi ro (làm MUST HAVE trước)

### 1.4 Yếu tố thành công then chốt

- Ưu tiên rõ ràng bằng phương pháp MoSCoW (24 tính năng MUST HAVE)
- Mua phần cứng sớm để tránh chậm tiến độ
- Phát triển tăng dần, tích hợp liên tục
- Nhận phản hồi định kỳ từ giảng viên để chỉnh hướng kịp thời
- Kiểm thử toàn diện xuyên suốt quá trình phát triển
- Lịch trình thực tế, có đệm cho tình huống phát sinh

---

## 2. TỔ CHỨC DỰ ÁN

### 2.1 Vai trò và trách nhiệm

| Vai trò | Người phụ trách | Trách nhiệm | Mức độ cam kết thời gian |
|------|------|------------------|-----------------|
| **Sinh viên / Lập trình viên** | Hung Thanh | - Toàn bộ công việc phát triển<br>- Thiết kế hệ thống & kiến trúc<br>- Huấn luyện và kiểm thử mô hình<br>- Tài liệu hóa<br>- Chuẩn bị thuyết trình bảo vệ | Toàn thời gian (40h/tuần) |
| **Giảng viên hướng dẫn** | [Advisor Name] | - Tư vấn kỹ thuật<br>- Rà soát sản phẩm bàn giao<br>- Phê duyệt quyết định quan trọng<br>- Đánh giá khóa luận cuối kỳ | 2 giờ/tuần (họp) |
| **Hội đồng khóa luận** | [Committee Members] | - Đánh giá đề cương<br>- Rà soát báo cáo cuối kỳ<br>- Tham dự buổi bảo vệ | Chỉ ngày bảo vệ |

### 2.2 Các bên liên quan

| Bên liên quan | Mối quan tâm | Mức ảnh hưởng | Chiến lược tương tác |
|-------------|----------|-----------|---------------------|
| **Giảng viên hướng dẫn** | Thành công và chất lượng dự án | Cao | Họp hằng tuần, cập nhật thường xuyên |
| **Hội đồng khóa luận** | Tính học thuật, tính đổi mới | Cao | Trình bày chính thức (đề cương, bảo vệ) |
| **Khoa/Bộ môn** | Tốt nghiệp đúng hạn | Trung bình | Nộp đúng hạn các đầu mục yêu cầu |
| **Người dùng tiềm năng** | Khả năng sử dụng, độ chính xác | Thấp | Lấy phản hồi trong giai đoạn test người dùng (Tuần 10-11) |

### 2.3 Cấu trúc trao đổi thông tin

```
┌─────────────────┐
│ Giảng viên      │
│ (Họp hằng tuần) │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Hung Thanh     │
│  (Developer)    │
└────────┬────────┘
         │
         ├──► Hội đồng (Đề cương & Bảo vệ)
         ├──► Reviewer đồng cấp (Code review)
         └──► Người dùng test (Feedback)
```

---

## 3. CẤU TRÚC PHÂN RÃ CÔNG VIỆC (WBS)

### 3.1 Cây WBS

```text
Driver Monitoring System Project
│
├── 1.0 PROJECT MANAGEMENT (Ongoing)
│   ├── 1.1 Planning & Scheduling
│   │   ├── 1.1.1 Create Proposal
│   │   ├── 1.1.2 Create Project Plan
│   │   └── 1.1.3 Sprint Planning Sessions
│   ├── 1.2 Monitoring & Control
│   │   ├── 1.2.1 Weekly Progress Tracking
│   │   ├── 1.2.2 Risk Monitoring
│   │   └── 1.2.3 Schedule Adjustments
│   └── 1.3 Meetings & Communication
│       ├── 1.3.1 Weekly Advisor Meetings
│       ├── 1.3.2 Meeting Minutes Documentation
│       └── 1.3.3 Status Reports
│
├── 2.0 REQUIREMENTS ANALYSIS (Week 3-4)
├── 3.0 SYSTEM DESIGN (Week 4-5)
├── 4.0 DEVELOPMENT SETUP (Week 2-3)
├── 5.0 CORE DEVELOPMENT (Week 5-9)
├── 6.0 ADVANCED FEATURES (Week 9)
├── 7.0 TESTING (Week 10-11)
├── 8.0 DOCUMENTATION (Week 1-12, Ongoing)
└── 9.0 CLOSURE & PRESENTATION (Week 12)
```

### 3.2 Thống kê tổng quan WBS

| Hạng mục | Gói công việc | Giờ ước tính |
|----------|--------------|-----------------|
| Quản lý dự án | 13 tác vụ | 60 giờ |
| Phân tích yêu cầu | 7 tác vụ | 40 giờ |
| Thiết kế | 14 tác vụ | 60 giờ |
| Thiết lập phát triển | 12 tác vụ | 30 giờ |
| Phát triển lõi | 25 tác vụ | 200 giờ |
| Tính năng nâng cao | 10 tác vụ | 60 giờ |
| Kiểm thử | 15 tác vụ | 80 giờ |
| Tài liệu | 22 tác vụ | 80 giờ |
| Kết thúc | 11 tác vụ | 40 giờ |
| **TỔNG** | **129 tác vụ** | **650 giờ** |

**Phân bổ nỗ lực:**
- Development: 40% (260 giờ)
- Testing: 12% (80 giờ)
- Documentation: 22% (140 giờ)
- Design: 9% (60 giờ)
- Management: 9% (60 giờ)
- Setup & Other: 8% (50 giờ)

---

## 4. LỊCH CHI TIẾT VÀ BIỂU ĐỒ GANTT

### 4.1 Tổng quan lộ trình 12 tuần

| Tuần | Giai đoạn | Trọng tâm | Sản phẩm chính |
|------|-------|-------|------------------|
| **W1** | Lập kế hoạch | Xác định bài toán, đề cương | Proposal |
| **W2** | Lập kế hoạch | Kế hoạch dự án, setup | Project Plan, repo, đặt phần cứng |
| **W3** | Yêu cầu | Product backlog, bắt đầu Sprint 1 | Product Backlog |
| **W4** | Yêu cầu | User stories, kiến trúc | User Stories, Architecture |
| **W5** | Thiết kế + Sprint 2 | CSDL, UI, nền tảng phát triển | Database Design, UI Mockups, modules nền tảng |
| **W6** | Sprint 2 | Module nhận diện cốt lõi | Face, eye, head, gaze hoạt động |
| **W7** | Sprint 3 | Thuật toán an toàn | Drowsiness + distraction |
| **W8** | Sprint 3 + 4 | Nhận diện hành vi | Thu thập dữ liệu, train model |
| **W9** | Sprint 4 | Tính năng nâng cao | DB integration, driver ID, hoạt động |
| **W10** | Sprint 5 | Kiểm thử và sửa lỗi | Test Plan, Test Cases, bug fixes |
| **W11** | Sprint 5 | Kiểm thử và hoàn thiện | Test results, benchmark |
| **W12** | Kết thúc | Tài liệu và chuẩn bị bảo vệ | Full docs, presentation |

### 4.2 Biểu đồ Gantt chi tiết

```text
TASK / DELIVERABLE                    | W1 | W2 | W3 | W4 | W5 | W6 | W7 | W8 | W9 |W10 |W11 |W12 |
--------------------------------------|----|----|----|----|----|----|----|----|----|----|----|----|
Proposal Document                     |████|    |    |    |    |    |    |    |    |    |    |    |
Project Plan Document                 |    |████|    |    |    |    |    |    |    |    |    |    |
Literature Review                     |████|████|    |    |    |    |    |    |    |    |    |    |
Hardware Acquisition                  |    |████|████|    |    |    |    |    |    |    |    |    |
Development Environment Setup         |    |████|████|    |    |    |    |    |    |    |    |    |
GitHub Repository Setup               |    |████|    |    |    |    |    |    |    |    |    |    |
...
Thesis Defense                        |    |    |    |    |    |    |    |    |    |    |    | ⚡ |
```

### 4.3 Phân tích đường găng

**Đường găng (không được trễ):**

```text
Proposal → Project Plan → Architecture Design → Foundation Dev (Sprint 2)
→ Core Detection (Sprint 3) → Activity Recognition (Sprint 4)
→ Testing (Sprint 5) → Defense
```

**Thời lượng:** 12 tuần  
**Độ trễ cho phép:** 0 ngày (không có buffer trên đường găng)

**Các hoạt động chạy song song:**
- Tài liệu hóa có thể chạy cùng phát triển
- Viết test case có thể bắt đầu trước khi kết thúc toàn bộ development
- Thu thập dữ liệu có thể chồng lấn với các việc khác của Sprint 4

---

## 5. LẬP KẾ HOẠCH SPRINT (AGILE SCRUM)

### 5.1 Cấu trúc Sprint

Mỗi sprint theo cấu trúc:
- **Thời lượng:** 2 tuần (10 ngày làm việc)
- **Sprint Planning:** Ngày 1 (chốt mục tiêu, chọn PBI)
- **Daily Work:** Ngày 2-9 (phát triển, kiểm thử)
- **Sprint Review:** Ngày 10 buổi sáng (demo cho giảng viên)
- **Sprint Retrospective:** Ngày 10 buổi chiều (rút kinh nghiệm)

### 5.2 Sprint 2: Nền tảng (Tuần 5-6)

**Mục tiêu Sprint:** Xây dựng các module nền tảng (face, eye, head, gaze)

| PBI | Task | Priority | Effort ước tính | Assigned To |
|-----|------|----------|------------------|-------------|
| PBI-001 | Face Detection & Tracking | MUST | 8 giờ | Hung Thanh |
| PBI-002 | Eye Region Detection | MUST | 6 giờ | Hung Thanh |
| PBI-003 | Eye Openness Detection (EAR) | MUST | 8 giờ | Hung Thanh |
| PBI-004 | Blink Frequency Monitoring | MUST | 4 giờ | Hung Thanh |
| PBI-005 | Eye Location Tracking | MUST | 4 giờ | Hung Thanh |
| PBI-006 | Head Pose Estimation | MUST | 10 giờ | Hung Thanh |
| PBI-007 | Head Location Tracking | MUST | 4 giờ | Hung Thanh |
| PBI-009 | Gaze Direction Estimation | MUST | 10 giờ | Hung Thanh |
| PBI-010 | Gaze Zone Classification | MUST | 6 giờ | Hung Thanh |
| PBI-044 | Basic Live Dashboard | MUST | 10 giờ | Hung Thanh |
| - | Integration & Testing | - | 10 giờ | Hung Thanh |
| **TOTAL** | **10 PBI + Integration** | - | **80 giờ** | - |

**Definition of Done (Sprint 2):**
- [ ] Face được detect và track realtime
- [ ] Eye region được xác định và tính EAR
- [ ] Head pose (pitch, yaw, roll) được ước lượng
- [ ] Gaze direction được tính và phân vùng
- [ ] Dashboard hiển thị camera feed + overlay
- [ ] Tất cả module có unit test
- [ ] Code được review và có tài liệu
- [ ] Có bản demo cho buổi review với giảng viên

### 5.3 Sprint 3: Phát hiện cốt lõi (Tuần 7-8)

**Mục tiêu Sprint:** Triển khai phát hiện buồn ngủ, mất tập trung và cảnh báo

| PBI | Task | Priority | Effort ước tính |
|-----|------|----------|------------------|
| PBI-012 | Drowsiness Detection (EAR-based) | MUST | 8 giờ |
| PBI-013 | Yawning Detection | MUST | 6 giờ |
| PBI-014 | Microsleep Detection | MUST | 4 giờ |
| PBI-016 | Head Turn Distraction | MUST | 6 giờ |
| PBI-017 | Gaze-off-Road Detection | MUST | 6 giờ |
| PBI-018 | Attention Score Calculation | SHOULD | 6 giờ |
| PBI-038 | Real-time Audio Alerts | MUST | 8 giờ |
| PBI-040 | Alert Priority Management | SHOULD | 4 giờ |
| - | Threshold Tuning & Testing | - | 16 giờ |
| - | Integration Testing | - | 16 giờ |
| **TOTAL** | **8 PBI + Testing** | - | **80 giờ** |

**Definition of Done (Sprint 3):**
- [ ] Phát hiện buồn ngủ qua EAR, ngáp, microsleep
- [ ] Phát hiện mất tập trung qua head pose và gaze
- [ ] Cảnh báo âm thanh kích hoạt đúng
- [ ] Tỉ lệ false positive <10% (kiểm thử sơ bộ)
- [ ] Ngưỡng được tài liệu hóa (EAR < 0.25, head yaw >45°, ...)
- [ ] Tích hợp thành công với module Sprint 2
- [ ] Duy trì hiệu năng >15 FPS

### 5.4 Sprint 4: Nhận diện hành vi (Tuần 8-9)

**Mục tiêu Sprint:** Huấn luyện và tích hợp CNN cho 7 hành vi nguy hiểm

| PBI/Task | Mô tả | Priority | Effort ước tính |
|----------|-------------|----------|------------------|
| - | Thu thập tập train (300+ mẫu/hành vi) | MUST | 20 giờ |
| - | Gán nhãn dữ liệu (2100+ ảnh) | MUST | 10 giờ |
| - | Data augmentation | MUST | 4 giờ |
| PBI-026 | Train Activity CNN (MobileNetV2) | MUST | 16 giờ |
| - | Đánh giá model và tuning | MUST | 8 giờ |
| PBI-019 | Tích hợp phát hiện gọi điện | MUST | 2 giờ |
| PBI-020 | Tích hợp phát hiện uống nước | MUST | 2 giờ |
| PBI-021 | Tích hợp phát hiện hút thuốc | MUST | 2 giờ |
| PBI-022 | Tích hợp phát hiện ngáp | MUST | 2 giờ |
| PBI-023 | Tích hợp phát hiện rời tay lái | MUST | 2 giờ |
| PBI-024 | Tích hợp phát hiện đưa tay ra cửa sổ | MUST | 2 giờ |
| PBI-025 | Tích hợp phát hiện nhìn chỉ đường | MUST | 2 giờ |
| PBI-041 | Ghi event vào database | MUST | 6 giờ |
| PBI-043 | Theo dõi phiên lái | MUST | 4 giờ |
| **TOTAL** | **13 PBI/Task** | - | **82 giờ** |

**Definition of Done (Sprint 4):**
- [ ] CNN đạt >85% accuracy theo từng hành vi
- [ ] 7 hành vi đều detect được realtime
- [ ] Event được log vào SQLite
- [ ] Session lái xe được lưu timestamp
- [ ] Inference time <30ms/frame
- [ ] Phân tích confusion matrix, cross-confusion không vượt 15%

### 5.5 Sprint 5: Kiểm thử và hoàn thiện (Tuần 10-11)

**Mục tiêu Sprint:** Kiểm thử toàn diện, sửa lỗi và hoàn thiện hệ thống

| Nhóm công việc | Công việc cụ thể | Effort ước tính |
|---------------|------------------|------------------|
| **Lập kế hoạch test** | Viết test plan, định nghĩa kịch bản | 8 giờ |
| **Test cases** | Viết 50+ test case (unit/integration/system) | 12 giờ |
| **Unit testing** | Test từng module | 12 giờ |
| **Integration testing** | Test pipeline end-to-end | 12 giờ |
| **Performance testing** | Benchmark accuracy, FPS, latency | 10 giờ |
| **Real-world testing** | Chạy test 8 giờ thực tế | 8 giờ |
| **Bug fixing** | Sửa lỗi critical và high | 20 giờ |
| **Optimization** | Tối ưu hiệu năng, giảm false positive | 8 giờ |
| **Documentation** | Cập nhật tài liệu kỹ thuật, user manual | 10 giờ |
| **TOTAL** | - | **100 giờ** |

**Definition of Done (Sprint 5):**
- [ ] Accuracy phát hiện buồn ngủ >90%
- [ ] Accuracy nhận diện hành vi >85% theo lớp
- [ ] Hiệu năng realtime >15 FPS
- [ ] <1 false alert/giờ trong bài test 8 giờ
- [ ] Đã sửa toàn bộ lỗi critical
- [ ] Kết quả test được tài liệu hóa
- [ ] Hệ thống ổn định, tỉ lệ crash <1%

---

## 6. PHÂN BỔ NGUỒN LỰC

### 6.1 Nguồn lực con người

**Nguồn lực chính:** Hung Thanh (Student Developer)

**Phân bổ thời gian (12 tuần):**
- Tổng thời gian khả dụng: 12 tuần × 40 giờ/tuần = **480 giờ**
- Development: 260 giờ (54%)
- Testing: 80 giờ (17%)
- Documentation: 80 giờ (17%)
- Project Management: 60 giờ (12%)

**Lịch tuần tham chiếu:**

| Ngày | Thời gian | Hoạt động |
|-----|------|----------|
| Monday | 9:00-12:00 | Development (3h) |
| Monday | 14:00-17:00 | Development (3h) |
| Tuesday | 9:00-12:00 | Development (3h) |
| Tuesday | 14:00-17:00 | Development (3h) |
| Wednesday | 9:00-12:00 | Development (3h) |
| Wednesday | 14:00-16:00 | Advisor Meeting (2h) |
| Wednesday | 16:00-17:00 | Meeting minutes (1h) |
| Thursday | 9:00-12:00 | Development (3h) |
| Thursday | 14:00-17:00 | Testing / Bug Fixing (3h) |
| Friday | 9:00-12:00 | Development (3h) |
| Friday | 14:00-17:00 | Documentation (3h) |
| **Weekly Total** | - | **34 giờ** (không gồm cuối tuần) |

**Khả dụng của giảng viên:**
- Họp hằng tuần: Wednesday 14:00-16:00 (2 giờ)
- Hỗ trợ qua email: phản hồi trong 24 giờ
- Tư vấn khẩn: theo yêu cầu

### 6.2 Nguồn lực phần cứng

| Phần cứng | Mục đích | Thời gian dùng | Chi phí |
|----------|---------|--------------|------|
| **Laptop phát triển** | Máy chính để phát triển | Week 1-12 | $0 (sẵn có) |
| **IR Camera** | Thu ảnh khuôn mặt tài xế | Week 3-12 (đặt Week 2) | $40 |
| **Jetson Nano 4GB** | Thiết bị edge computing | Week 3-12 (đặt Week 2) | $140 |
| **MicroSD Card (128GB)** | Lưu trữ cho Jetson | Week 3-12 | $20 |
| **USB Speaker** | Cảnh báo âm thanh | Week 7-12 | $15 |
| **Power Supply** | Cấp nguồn Jetson | Week 3-12 | $10 |
| **Tùy chọn: màn hình 7"** | Hiển thị dashboard | Week 6-12 (optional) | $60 |
| **TOTAL** | - | - | **$225-285** |

**Mốc mua phần cứng:**
- Week 2: đặt IR camera, Jetson Nano và phụ kiện
- Week 3: nhận hàng, bắt đầu setup
- Week 3: kiểm tra kết nối camera
- Week 5: tích hợp full hệ thống

### 6.3 Nguồn lực phần mềm

| Phần mềm | Mục đích | License | Chi phí |
|----------|---------|---------|------|
| Python 3.8+ | Ngôn ngữ lập trình | Open Source | Free |
| OpenCV | Computer vision | Open Source | Free |
| dlib | Landmark khuôn mặt | Open Source | Free |
| TensorFlow | Deep learning | Open Source | Free |
| SQLite | Cơ sở dữ liệu | Open Source | Free |
| Git / GitHub | Quản lý phiên bản | Free tier | Free |
| VS Code | IDE | Open Source | Free |
| Jupyter Notebook | Huấn luyện mô hình | Open Source | Free |
| pytest | Framework kiểm thử | Open Source | Free |
| **TOTAL** | - | - | **$0** |

### 6.4 Tài nguyên cloud (tùy chọn)

| Tài nguyên | Mục đích | Nhà cung cấp | Chi phí ước tính |
|----------|---------|----------|----------------|
| **Cloud GPU (Optional)** | Train model nếu laptop không đủ | Google Colab Pro | $10/tháng (1-2 tháng) |
| **GitHub Storage** | Lưu trữ mã nguồn | GitHub Free | Free |
| **Tổng (tùy chọn)** | - | - | **$0-20** |

**Điểm quyết định:** Week 8 - đánh giá có cần cloud GPU cho train CNN hay không.

---

## 7. KẾ HOẠCH QUẢN LÝ RỦI RO

### 7.1 Nhận diện và đánh giá rủi ro

| Risk ID | Mô tả rủi ro | Xác suất | Tác động | Điểm rủi ro | Nhóm |
|---------|------------------|-------------|--------|------------|----------|
| **R1** | Độ chính xác nhận diện hành vi <85% | Medium (40%) | High | **HIGH** | Technical |
| **R2** | Hiệu năng realtime <15 FPS trên Jetson | Medium (30%) | High | **HIGH** | Technical |
| **R3** | Giao phần cứng bị trễ | Low (20%) | Medium | **MEDIUM** | External |
| **R4** | Tỉ lệ false positive buồn ngủ cao | Medium (40%) | Medium | **MEDIUM** | Technical |
| **R5** | Thu thập dataset lâu hơn kế hoạch | Medium (30%) | Medium | **MEDIUM** | Schedule |
| **R6** | Hệ thống crash khi test dài | Low (20%) | Medium | **MEDIUM** | Technical |
| **R7** | Scope creep (thêm tính năng ngoài kế hoạch) | High (50%) | Low | **MEDIUM** | Management |
| **R8** | Ốm đau hoặc sự cố cá nhân | Low (15%) | High | **MEDIUM** | Personal |
| **R9** | IR camera hoạt động kém ở điều kiện sáng khác nhau | Medium (30%) | Low | **LOW** | Technical |
| **R10** | Giảng viên không sẵn cho quyết định quan trọng | Low (10%) | Medium | **LOW** | External |

**Cách tính điểm rủi ro:** Xác suất × Tác động  
**Ưu tiên:** HIGH (>30%), MEDIUM (15-30%), LOW (<15%)

### 7.2 Chiến lược phản ứng rủi ro

#### **R1: Độ chính xác nhận diện hành vi <85% (HIGH)**

**Giảm thiểu (phòng ngừa):**
- Thu tập dữ liệu đa dạng (300+ mẫu/hành vi)
- Tăng dữ liệu bằng augmentation (xoay, sáng tối, blur)
- Bắt đầu từ MobileNetV2 pretrained rồi fine-tune
- Trao đổi sớm với giảng viên khi accuracy thấp
- Chừa thời gian tuning trong Sprint 4

**Phương án dự phòng (nếu xảy ra):**
- Thu hẹp còn 5 hành vi quan trọng nhất
- Chấp nhận ngưỡng accuracy thấp hơn (80%) và nêu rõ trong báo cáo
- Dùng confidence threshold để giảm false positive
- Kết hợp thêm luật rule-based

**Owner:** Hung Thanh  
**Review Date:** End of Week 8

#### **R2: Hiệu năng realtime <15 FPS (HIGH)**

**Giảm thiểu (phòng ngừa):**
- Dùng model nhẹ (MobileNetV2, tránh ResNet)
- Tối ưu code (vectorization, giảm loop dư)
- Dùng TensorFlow Lite cho inference
- Profile để tìm bottleneck
- Xử lý cách khung hình (mỗi 2 frame)
- Ưu tiên Jetson Nano thay Raspberry Pi

**Phương án dự phòng (nếu xảy ra):**
- Hạ độ phân giải camera (720p thay 1080p)
- Tắt tính năng phụ
- Chạy nhận diện hành vi mỗi 3 frame
- Dùng threading để song song hóa
- Chấp nhận 12-15 FPS là gần realtime

**Owner:** Hung Thanh  
**Review Date:** End of Week 6

#### **R3: Trễ giao phần cứng (MEDIUM)**

**Giảm thiểu:**
- Đặt sớm từ tuần 2
- Chọn nhà cung cấp uy tín
- Có nhà cung cấp dự phòng
- Theo dõi đơn hàng chủ động

**Dự phòng:**
- Dùng webcam laptop tạm thời
- Phát triển bằng video thu sẵn
- Mượn thiết bị từ phòng lab nếu có
- Mua tại cửa hàng địa phương
- Điều chỉnh lịch: làm phần mềm trước, tích hợp phần cứng sau

**Owner:** Hung Thanh  
**Trigger:** Nếu chưa nhận phần cứng cuối Week 3

#### **R4: False positive buồn ngủ cao (MEDIUM)**

**Giảm thiểu:**
- Hợp nhất nhiều tín hiệu (EAR + PERCLOS + ngáp + blink rate)
- Yêu cầu từ 2 chỉ báo trở lên mới cảnh báo
- Dùng ngưỡng theo thời gian (duy trì >2s)
- Test trên nhiều người có đặc điểm mắt khác nhau
- Cho phép hiệu chỉnh theo từng tài xế

**Dự phòng:**
- Điều chỉnh ngưỡng EAR (0.25 xuống 0.22)
- Tăng ngưỡng thời gian (2s lên 3s)
- Thêm mức độ nhạy low/medium/high
- Ghi rõ hạn chế trong user manual
- Ưu tiên recall hơn precision

**Owner:** Hung Thanh  
**Review Date:** End of Week 7

#### **R5: Thu thập dữ liệu kéo dài (MEDIUM)**

**Giảm thiểu:**
- Bắt đầu thu dữ liệu sớm từ Week 7
- Tận dụng dataset công khai (State Farm, Kaggle)
- Nhờ bạn bè/người thân tham gia thu nhanh
- Dùng augmentation để tăng quy mô dữ liệu
- Chừa buffer trong Sprint 4

**Dự phòng:**
- Giảm số mẫu/hành vi (300 xuống 200)
- Ưu tiên 5 hành vi thay vì 7
- Dùng dữ liệu tổng hợp nếu phù hợp
- Chấp nhận accuracy thấp hơn và ghi vào future work
- Mô phỏng một số hành vi bằng ảnh dàn dựng

**Owner:** Hung Thanh  
**Trigger:** Nếu <100 mẫu/hành vi vào cuối Week 8

#### **R7: Scope creep (MEDIUM)**

**Giảm thiểu:**
- Tuân thủ MoSCoW (24 MUST HAVE)
- Review phạm vi hằng tuần với giảng viên
- Đưa ý tưởng phát sinh vào mục Future Work
- Giữ mục tiêu "đủ tốt để tốt nghiệp"
- Product Backlog là nguồn sự thật duy nhất

**Dự phòng:**
- Đóng băng phạm vi ngay khi phát hiện
- Cắt bớt tính năng không thuộc MUST
- Trao đổi lại với giảng viên về khả năng hoàn thành
- Dời SHOULD HAVE sang Future Work

**Owner:** Hung Thanh + Advisor  
**Review:** Hằng tuần

#### **R8: Ốm đau hoặc sự cố cá nhân (MEDIUM)**

**Giảm thiểu:**
- Duy trì sức khỏe, ngủ nghỉ hợp lý
- Giữ buffer lịch (mục tiêu xong Week 11)
- Sao lưu thường xuyên (GitHub + local)
- Tài liệu hóa đầy đủ để dễ tiếp tục công việc

**Dự phòng:**
- Báo giảng viên ngay khi có sự cố
- Làm từ xa nếu có thể
- Xin gia hạn nếu tình huống nghiêm trọng
- Ưu tiên hoàn thành MUST HAVE
- Tận dụng các tài liệu đã hoàn thành

**Owner:** Hung Thanh  
**Trigger:** Vắng mặt ngoài kế hoạch >2 ngày

### 7.3 Theo dõi rủi ro

- Tần suất review: hằng tuần, cuối mỗi sprint, và ngay khi rủi ro xảy ra
- Duy trì risk register và cập nhật xác suất/tác động liên tục

---

## 8. KẾ HOẠCH QUẢN LÝ CHẤT LƯỢNG

### 8.1 Tiêu chuẩn chất lượng

| Loại sản phẩm | Tiêu chuẩn | Cách xác minh |
|------------------|------------------|---------------------|
| **Code** | - Tuân thủ PEP 8<br>- Coverage >70%<br>- Không có lỗi critical | - flake8<br>- pytest + coverage<br>- Code review |
| **Model** | - Accuracy buồn ngủ >90%<br>- Accuracy hành vi >85%<br>- False positive <5% | - Test dataset<br>- Confusion matrix<br>- Test thực tế |
| **Hiệu năng** | - >15 FPS<br>- Latency <500ms<br>- Uptime >99% | - FPS monitoring<br>- Timestamp logging<br>- Stress test 8 giờ |
| **Tài liệu** | - Đủ nội dung<br>- Diễn đạt rõ ràng<br>- Format chuẩn | - Advisor review<br>- Peer review<br>- Spell check |
| **Giao diện** | - Responsive<br>- Dễ dùng<br>- Phản hồi rõ ràng | - Usability test<br>- User feedback |

### 8.2 Hoạt động đảm bảo chất lượng

**Trong quá trình phát triển:**
- Hằng ngày: chạy unit test trước khi commit
- Hằng tuần: self-review và (nếu có) peer review
- Cuối sprint: integration test và benchmark hiệu năng

**Giai đoạn kiểm thử (Week 10-11):**
- Unit test từng module
- Integration test liên kết module
- System test toàn luồng
- Performance test: accuracy, tốc độ, độ ổn định
- User acceptance test trong điều kiện thực tế

### 8.3 Chuẩn chất lượng code

```python
# Ví dụ cấu trúc code
class FaceDetector:
    """Detects and tracks driver face in video stream.

    Attributes:
        detector: dlib face detector instance
        predictor: dlib shape predictor for landmarks
    """

    def __init__(self, model_path: str):
        """Initialize face detector with model path."""
        pass

    def detect_face(self, frame: np.ndarray) -> Optional[Rectangle]:
        """Detect face in frame.

        Args:
            frame: Input image as numpy array

        Returns:
            Face bounding box or None if no face detected
        """
        pass
```

**Checklist code review:**
- [ ] Tuân thủ PEP 8
- [ ] Hàm có docstring
- [ ] Tên biến rõ nghĩa
- [ ] Không hardcode (dùng config)
- [ ] Có xử lý lỗi
- [ ] Có unit test
- [ ] Không để code comment-out
- [ ] Tối ưu hiệu năng, tránh xử lý dư thừa

### 8.4 Chiến lược kiểm thử

```text
        ╱────────╲
       ╱   E2E    ╲      ← 10% (System tests)
      ╱────────────╲
     ╱ Integration  ╲    ← 30% (Module interactions)
    ╱────────────────╲
   ╱   Unit Tests     ╲  ← 60% (Individual functions)
  ╱────────────────────╲
```

**Mục tiêu coverage:**
- Unit tests: >70%
- Integration tests: bao phủ toàn bộ interface giữa module
- System tests: bao phủ user stories + acceptance criteria
- Performance tests: bao phủ chỉ số trọng yếu

---

## 9. KẾ HOẠCH TRUYỀN THÔNG

### 9.1 Ma trận truyền thông

| Bên liên quan | Thông tin cần nhận | Tần suất | Phương thức | Người phụ trách |
|-------------|-------------------|-----------|--------|-------------|
| **Giảng viên hướng dẫn** | Tiến độ, quyết định kỹ thuật, blocker/risk, review deliverable | Hằng tuần | Họp trực tiếp + email | Hung Thanh |
| **Hội đồng khóa luận** | Đề cương, nộp khóa luận, lịch bảo vệ | Theo mốc | Tài liệu chính thức + thuyết trình | Hung Thanh |
| **Bản thân (Project log)** | Tiến độ hằng ngày, quyết định, bài học | Hằng ngày | Git commit + project journal | Hung Thanh |
| **Reviewer đồng cấp** | Yêu cầu review code, phản hồi kỹ thuật | Khi cần | Pull request + nhắn tin | Hung Thanh |

### 9.2 Lịch họp

**Họp giảng viên hằng tuần (Wednesday 14:00-16:00)**

**Mẫu agenda:**
1. Tiến độ từ buổi họp trước
2. Demo (nếu có)
3. Khó khăn / blocker
4. Kế hoạch tuần tới
5. Hỏi đáp và định hướng

**Mẫu biên bản họp:**

```text
MEETING MINUTES
Date: [Date]
Attendees: Hung Thanh, [Advisor Name]
Duration: 2 hours

PROGRESS SINCE LAST MEETING:
- [Completed task 1]
- [Completed task 2]

DEMO:
- [Feature demonstrated]
- [Feedback received]

CHALLENGES DISCUSSED:
- [Challenge 1]
  - Advisor guidance: [advice given]
- [Challenge 2]
  - Decision: [decision made]

ACTION ITEMS:
- [Action 1] - Due: [Date] - Assigned: [Name]
- [Action 2] - Due: [Date] - Assigned: [Name]

NEXT MEETING: [Date & Time]
```

### 9.3 Báo cáo trạng thái

```text
WEEKLY STATUS REPORT
Week: [Week Number]
Date: [Date]

COMPLETED THIS WEEK:
- [Task 1]
- [Task 2]
- [Task 3]

IN PROGRESS:
- [Task 4] - 60% complete
- [Task 5] - 30% complete

PLANNED FOR NEXT WEEK:
- [Task 6]
- [Task 7]

RISKS/BLOCKERS:
- [Risk 1] - Mitigation: [action]
- [Blocker 1] - Need: [advisor input]

METRICS:
- Code coverage: XX%
- Test cases written: XX
- Performance: XX FPS

STATUS: On Track / At Risk / Delayed
```

### 9.4 Cấu trúc kho tài liệu

```text
docs-driver/
├── README.md
├── docs/
│   ├── proposal.md
│   ├── project-plan.md
│   ├── product-backlog.md
│   ├── user-stories.md
│   ├── architecture.md
│   ├── database-design.md
│   ├── ui-design.md
│   ├── test-plan.md
│   ├── test-cases.md
│   ├── code-standard.md
│   └── reflection.md
├── meeting-minutes/
├── sprint-backlogs/
├── src/
├── tests/
├── models/
├── data/
└── presentations/
```

---

## 10. NGÂN SÁCH VÀ ƯỚC TÍNH CHI PHÍ

### 10.1 Ngân sách phần cứng

| Hạng mục | Cấu hình | Số lượng | Đơn giá | Thành tiền | Ưu tiên |
|------|---------------|----------|------------|-------|----------|
| **IR Camera** | 1080p, 60fps, USB, IR night vision | 1 | $40 | $40 | MUST |
| **Jetson Nano** | 4GB RAM, quad-core ARM CPU, 128-core GPU | 1 | $140 | $140 | MUST |
| **MicroSD Card** | 128GB UHS-1 | 1 | $20 | $20 | MUST |
| **Power Supply** | 5V 4A barrel jack | 1 | $10 | $10 | MUST |
| **USB Speaker** | 3W, USB-powered | 1 | $15 | $15 | SHOULD |
| **7" Display** | HDMI touchscreen (optional) | 1 | $60 | $60 | COULD |
| **Case/Enclosure** | Acrylic case for Jetson | 1 | $15 | $15 | COULD |
| **Shipping** | Combined shipping | - | $20 | $20 | - |
| **SUBTOTAL (MUST)** | - | - | - | **$210** | - |
| **SUBTOTAL (with SHOULD)** | - | - | - | **$225** | - |
| **TOTAL (all optional)** | - | - | - | **$320** | - |

**Kế hoạch ngân sách phần cứng:** mục tiêu $225 (MUST + SHOULD)

### 10.2 Ngân sách phần mềm

| Phần mềm | License | Chi phí |
|----------|--------------|------|
| Python, OpenCV, dlib, TensorFlow | Open Source | $0 |
| Git, GitHub (Free tier) | Free | $0 |
| VS Code, Jupyter | Open Source | $0 |
| SQLite | Open Source | $0 |
| Google Colab (Basic) | Free | $0 |
| **TOTAL** | - | **$0** |

**Tùy chọn:** Google Colab Pro (GPU train model): $10/tháng x 2 tháng = $20

### 10.3 Tổng ngân sách dự án

| Hạng mục | Dự trù | Thực tế (điền sau) |
|----------|----------|-----------------------|
| Hardware | $225 | |
| Software | $0 | |
| Cloud (optional) | $0-20 | |
| In ấn/đóng quyển | $20 | |
| Dự phòng khác | $35 | |
| **TOTAL** | **$280-300** | |

**Nguồn kinh phí:** cá nhân / học bổng sinh viên

---

## 11. MỐC VÀ SẢN PHẨM BÀN GIAO

### 11.1 Các mốc chính

| ID | Mốc | Tiêu chí | Mốc thời gian | Trạng thái |
|----|-----------|----------|-------------|--------|
| **M1** | Proposal Approved | Advisor ký duyệt đề cương | Week 1 (Mar 11, 2026) | Pending |
| **M2** | Hardware Acquired | Nhận IR camera + Jetson Nano | Week 3 (Mar 25, 2026) | Pending |
| **M3** | Architecture Complete | Tài liệu thiết kế được duyệt | Week 4 (Apr 1, 2026) | Pending |
| **M4** | Foundation Modules Working | Demo Sprint 2 thành công | Week 6 (Apr 15, 2026) | Pending |
| **M5** | Core Detection Complete | Demo Sprint 3 thành công | Week 8 (Apr 29, 2026) | Pending |
| **M6** | All MUST HAVEs Implemented | 24 tính năng hoạt động | Week 9 (May 6, 2026) | Pending |
| **M7** | Testing Complete | Đạt chỉ số, sửa lỗi xong | Week 11 (May 20, 2026) | Pending |
| **M8** | Thesis Submitted | Nộp đủ 13 deliverables | Week 12 (May 27, 2026) | Pending |
| **M9** | Defense Successful | Bảo vệ đạt | TBD (May 27-31, 2026) | Pending |

### 11.2 Checklist deliverables

| # | Deliverable | Mô tả | Hạn nộp | Owner | Status |
|---|-------------|-------------|----------|-------|--------|
| 1 | **Proposal** | Tài liệu đề cương | Week 1 | Hung Thanh | Complete |
| 2 | **Project Plan** | Tài liệu kế hoạch dự án | Week 2 | Hung Thanh | In Progress |
| 3 | **Product Backlog** | 45 PBI theo MoSCoW | Week 3 | Hung Thanh | Complete |
| 4 | **User Stories** | 48 stories + acceptance criteria | Week 4 | Hung Thanh | Complete |
| 5 | **Architecture** | Tài liệu kiến trúc hệ thống | Week 4-5 | Hung Thanh | Pending |
| 6 | **Database Design** | ERD + schema bảng | Week 5 | Hung Thanh | Pending |
| 7 | **UI/Interfaces** | Wireframe, mockup | Week 5 | Hung Thanh | Pending |
| 8 | **Test Plan** | Chiến lược và kịch bản kiểm thử | Week 5 | Hung Thanh | Pending |
| 9 | **Test Cases** | 50+ test case chi tiết | Week 10 | Hung Thanh | Pending |
| 10 | **Sprint Backlog** | Backlog Sprint 2-5 | Week 5-10 | Hung Thanh | Pending |
| 11 | **Code Standard** | Quy chuẩn coding | Week 6 | Hung Thanh | Pending |
| 12 | **Meeting Minutes** | 12 biên bản họp tuần | Week 1-12 | Hung Thanh | Ongoing |
| 13 | **Reflection** | Bài học rút ra, future work | Week 12 | Hung Thanh | Pending |
| - | **Working System** | Nguyên mẫu triển khai được | Week 11 | Hung Thanh | Pending |
| - | **Source Code** | Kho mã nguồn GitHub | Week 12 | Hung Thanh | Ongoing |
| - | **Trained Models** | File mô hình CNN | Week 9 | Hung Thanh | Pending |
| - | **User Manual** | Hướng dẫn cài đặt và sử dụng | Week 11 | Hung Thanh | Pending |
| - | **Defense Slides** | Slide bảo vệ | Week 12 | Hung Thanh | Pending |

---

## 12. CHỈ SỐ THÀNH CÔNG

### 12.1 Chỉ số kỹ thuật

| Chỉ số | Mục tiêu | Cách đo | Trạng thái |
|--------|--------|--------------------|--------|
| Accuracy phát hiện buồn ngủ | >90% | Test set (100+ mẫu) | TBD |
| Accuracy nhận diện hành vi | >85% mỗi lớp | Test set (7 lớp) | TBD |
| False positive (buồn ngủ) | <1 cảnh báo/giờ | Test lái xe 8 giờ | TBD |
| False positive (hành vi) | <5% | Phân tích confusion matrix | TBD |
| Hiệu năng realtime | >15 FPS | Theo dõi frame rate | TBD |
| Độ trễ phát hiện | <500ms | Timestamp logging | TBD |
| Uptime hệ thống | >99% | Không crash trong test 8 giờ | TBD |
| Tỉ lệ detect mặt | >95% | Khi mặt không bị che khuất | TBD |
| Accuracy nhận diện tài xế | >95% | Test trên tài xế đã enroll | TBD |
| Code coverage | >70% | pytest-cov | TBD |

### 12.2 Chỉ số quản lý dự án

| Chỉ số | Mục tiêu | Trạng thái |
|--------|--------|--------|
| Deliverables đúng hạn | 13/13 (100%) | TBD |
| Milestones đạt đúng hạn | 9/9 (100%) | TBD |
| Tuân thủ ngân sách | Trong $300 | TBD |
| Họp tuần với giảng viên | 12/12 (100%) | TBD |
| Biên bản họp | 12/12 (100%) | TBD |
| Sprint velocity | Ổn định theo sprint | TBD |
| Scope phát sinh ngoài kế hoạch | 0 | TBD |

### 12.3 Chỉ số học thuật

| Chỉ số | Mục tiêu | Trạng thái |
|--------|--------|--------|
| Duyệt đề cương | Advisor phê duyệt | Pending |
| Tham dự hội đồng | 100% thành viên | TBD |
| Kết quả bảo vệ | Pass | TBD |
| Điểm cuối kỳ | >= 7.0/10 | TBD |
| Công bố/thi học thuật (bonus) | Optional | TBD |

### 12.4 Chỉ số chất lượng

| Chỉ số | Mục tiêu | Cách đo |
|--------|--------|-------------|
| Lỗi critical | 0 khi nộp | Bug tracker |
| Lỗi high | <3 khi nộp | Bug tracker |
| Mức độ đầy đủ tài liệu | Đủ tất cả mục | Document review |
| Tuân thủ style code | 100% PEP 8 | flake8 report |
| Mức hài lòng người dùng (optional) | >4/5 | User feedback |

---

## 13. GIẢ ĐỊNH VÀ RÀNG BUỘC

### 13.1 Giả định

**Giả định kỹ thuật:**
- Jetson Nano đủ năng lực xử lý realtime (>15 FPS)
- IR camera hoạt động ổn định cả ngày và đêm
- Có thể dùng mô hình pretrained (dlib, MobileNetV2)
- OpenCV và dlib đủ chính xác cho face/eye detection
- Có thể thu thập hoặc tìm được dataset cho hành vi nguy hiểm
- SQLite đủ cho lưu trữ local

**Giả định dự án:**
- Sinh viên có thể làm toàn thời gian 40 giờ/tuần trong 12 tuần
- Giảng viên có thể họp 2 giờ/tuần đều đặn
- Phần cứng giao trong 1-2 tuần kể từ khi đặt
- Không có sự cố cá nhân nghiêm trọng kéo dài
- Laptop phát triển đủ cấu hình (i5+, RAM 8GB+, GPU rời là lợi thế)
- Có internet ổn định để nghiên cứu và cài thư viện

**Giả định phạm vi:**
- 1 camera IR là đủ (không cần multi-camera)
- Mặt tài xế luôn trong vùng nhìn của camera
- Hệ thống hoạt động trong điều kiện xe tiêu chuẩn
- Mỗi chuyến có 1 tài xế chính

### 13.2 Ràng buộc

**Ràng buộc thời gian:**
- Hạn cứng 12 tuần để nộp khóa luận (May 27, 2026)
- Bảo vệ phải diễn ra trước khi kết thúc năm học
- Không thể kéo dài vô thời hạn

**Ràng buộc nguồn lực:**
- Trần ngân sách: $300
- Chỉ có 1 người phát triển
- Giảng viên dành 2 giờ/tuần

**Ràng buộc kỹ thuật:**
- Giới hạn phần cứng của Jetson Nano
- Xử lý hoàn toàn tại edge (không cloud trong runtime)
- Yêu cầu realtime >15 FPS
- FOV camera đơn bị giới hạn

**Ràng buộc phạm vi:**
- 24 MUST HAVE là mức tối thiểu bắt buộc
- 17 SHOULD HAVE là tùy thời gian
- Safety belt detection loại khỏi phạm vi
- Mobile app ngoài phạm vi

**Ràng buộc học thuật:**
- Bắt buộc đủ 13 deliverables
- Họp tuần là bắt buộc
- Buổi bảo vệ cần demo live hệ thống
- Đảm bảo tính nguyên gốc học thuật, trích dẫn đầy đủ

### 13.3 Phụ thuộc

**Phụ thuộc bên ngoài:**
- Tiến độ giao phần cứng
- Khả dụng của giảng viên
- Truy cập tài liệu nghiên cứu và dataset
- Kết nối internet ổn định

**Phụ thuộc nội bộ (đường găng):**
- Proposal → Project plan → Architecture → Development
- Hardware arrival → Camera integration → Detection modules
- Dataset collection → Model training → Activity recognition
- Development complete → Testing → Defense

---

## PHỤ LỤC

### Phụ lục A: Mẫu kế hoạch Sprint

```markdown
# Sprint [Number]: [Sprint Name]

**Sprint Duration:** [Start Date] to [End Date] (2 weeks)
**Sprint Goal:** [One-sentence goal]

## Sprint Backlog

| PBI | Task | Priority | Estimated Effort | Actual Effort | Status |
|-----|------|----------|------------------|---------------|--------|
| PBI-XXX | Task description | MUST | Xh | | Pending |

**Total Estimated Effort:** XX hours

## Daily Progress Log

### Day 1 ([Date]):
- Completed: [tasks]
- In Progress: [tasks]
- Blockers: [issues]

## Sprint Review ([Date])
- Demo
- Feedback

## Sprint Retrospective
- What went well
- What could improve
- Action items
```

### Phụ lục B: Mẫu biên bản họp

```markdown
# Meeting Minutes - Week [XX]

**Date:** [Date]
**Time:** [Start Time] - [End Time]
**Location:** [Location / Virtual]
**Attendees:** Hung Thanh, [Advisor Name]

## Agenda
1. Progress Update
2. Demo
3. Challenges
4. Next Steps
5. Q&A

## Action Items
| Action | Owner | Due Date | Status |
|--------|-------|----------|--------|
| [Action 1] | Hung Thanh | [Date] | Pending |
```

### Phụ lục C: Mẫu sổ đăng ký rủi ro

```markdown
# Risk Register

**Project:** Driver Monitoring System
**Last Updated:** [Date]

| Risk ID | Description | Category | Probability | Impact | Score | Status | Owner | Mitigation | Contingency |
|---------|-------------|----------|-------------|--------|-------|--------|-------|------------|-------------|
| R1 | [Risk description] | Technical | 40% | High | HIGH | Active | Hung Thanh | [Mitigation] | [Contingency] |
```

### Phụ lục D: Mẫu yêu cầu thay đổi

```markdown
# Change Request #[Number]

**Date Submitted:** [Date]
**Submitted By:** [Name]
**Status:** Pending / Approved / Rejected

## Change Description
[Details]

## Impact Analysis
- Scope
- Schedule
- Budget
- Quality

## Decision
**Date:** [Date]
**Decision Maker:** [Advisor Name]
**Decision:** Approved / Rejected
```

---

## XÁC NHẬN PHÊ DUYỆT

**Chữ ký sinh viên:** _____________________________ Date: __________  
Name: Hung Thanh

**Chữ ký giảng viên hướng dẫn:** _____________________________ Date: __________  
Name: [Advisor Name]

---

## LỊCH SỬ PHIÊN BẢN TÀI LIỆU

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | Mar 4, 2026 | Hung Thanh | Initial project plan created |
| 1.1 | Mar 7, 2026 | Hung Thanh | Added Vietnamese version |

---

**KẾT THÚC TÀI LIỆU KẾ HOẠCH DỰ ÁN**

---

**Thông tin tài liệu:**
- **Tên file:** PROJECT-PLAN-Driver-Monitoring-System-VI.md
- **Phiên bản:** 1.1
- **Ngày tạo:** March 7, 2026
- **Cập nhật gần nhất:** March 7, 2026
- **Số trang ước tính:** ~30-35 trang (khi xuất PDF)
- **Số từ ước tính:** ~9,000-12,000 từ (tùy mức chi tiết cập nhật)
- **Trạng thái:** Draft (Pending Advisor Approval)
