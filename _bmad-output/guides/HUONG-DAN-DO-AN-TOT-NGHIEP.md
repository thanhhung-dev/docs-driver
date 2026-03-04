# 🎓 HƯỚNG DẪN CHI TIẾT - QUY TRÌNH LÀM ĐỒ ÁN TỐT NGHIỆP
## Driver Monitoring System using Computer Vision & AI

**Sinh viên:** Hung Thanh  
**Ngày tạo:** 2026-03-03  
**Tổng thời gian dự án:** 12 tuần  
**Tổng deliverables:** 13 items

---

## 📋 MỤC LỤC

1. [Overview - 13 Deliverables](#overview)
2. [Roadmap Tổng thể - Timeline](#roadmap)
3. [Chi tiết Từng Deliverable](#chi-tiet)
   - [1. Proposal](#1-proposal)
   - [2. Project Plan](#2-project-plan)
   - [3. Product Backlog](#3-product-backlog)
   - [4. User Stories](#4-user-stories)
   - [5. Architecture](#5-architecture)
   - [6. Database Design](#6-database-design)
   - [7. UI/Interfaces](#7-ui-interfaces)
   - [8. Test Plan](#8-test-plan)
   - [9. Test Cases](#9-test-cases)
   - [10. Sprint Backlog](#10-sprint-backlog)
   - [11. Code Standard](#11-code-standard)
   - [12. Meeting Minutes](#12-meeting-minutes)
   - [13. Reflection](#13-reflection)
4. [Timeline Chi tiết 12 Tuần](#timeline)
5. [Dependencies Map](#dependencies)
6. [Tools Recommendation](#tools)
7. [Top 10 Tips](#tips)

---

<a name="overview"></a>
## 📊 OVERVIEW - 13 DELIVERABLES

### **Phase 1: Initiation & Planning (Tuần 1-2)** 📋
- ✅ Proposal
- ✅ Project Plan

### **Phase 2: Requirements & Design (Tuần 3-5)** 🎨
- ✅ Product Backlog
- ✅ User Stories
- ✅ Architecture
- ✅ Database Design
- ✅ UI/Interfaces

### **Phase 3: Development (Tuần 6-9)** 💻
- ✅ Sprint Backlog
- ✅ Code Standard
- ✅ Meeting minutes

### **Phase 4: Testing & Closure (Tuần 10-12)** ✅
- ✅ Test Plan
- ✅ Test Cases
- ✅ Reflection

---

<a name="roadmap"></a>
## 🗺️ ROADMAP TỔNG THỂ - TIMELINE 12 TUẦN

```
Week 1-2: INITIATION & PLANNING
├── Proposal ✍️
├── Project Plan 📅
└── Initial research 📚

Week 3-4: REQUIREMENTS (Sprint 1)
├── Product Backlog 📦
├── User Stories 📖
├── Architecture Design 🏗️
└── Development: Foundation

Week 5-6: DESIGN (Sprint 2)
├── Database Design 🗄️
├── UI/Interfaces Design 🎨
├── Test Plan 🧪
└── Development: Core features

Week 7-8: DEVELOPMENT (Sprint 3)
├── Sprint Backlog updates 🏃
├── Code Standard enforcement 💻
├── Test Cases writing ✅
├── Meeting minutes 📝
└── Development: Advanced features

Week 9-10: DEVELOPMENT (Sprint 4)
├── Continue coding 💻
├── Test execution 🧪
├── Bug fixes 🐛
└── Documentation updates 📄

Week 11: TESTING & POLISH (Sprint 5)
├── Integration testing 🔗
├── Performance testing ⚡
├── Final bug fixes 🐛
└── Code cleanup 🧹

Week 12: CLOSURE
├── Final testing ✅
├── Documentation completion 📚
├── Reflection writing 🤔
├── Presentation preparation 🎤
└── Final submission 📤
```

---

<a name="chi-tiet"></a>
## 📑 CHI TIẾT TỪNG DELIVERABLE

---

<a name="1-proposal"></a>
### **1. PROPOSAL (Đề xuất Dự án)** 📄

**Mục đích:** Thuyết phục giáo viên hướng dẫn chấp thuận đề tài

**Nội dung cần có:**

#### **1.1. Problem Statement (Phát biểu Vấn đề)**
```
Vấn đề:
- Tai nạn giao thông do lái xe buồn ngủ, mất tập trung
- Thống kê: X% tai nạn do yếu tố con người
- Nhu cầu giám sát hành vi lái xe real-time

Impact:
- Thiệt hại về người và tài sản
- Chi phí y tế, bảo hiểm cao
- Ảnh hưởng đến an toàn cộng đồng
```

#### **1.2. Solution Overview (Tổng quan Giải pháp)**
```
Đề xuất:
Hệ thống AI/Computer Vision giám sát hành vi lái xe real-time

Cách thức hoạt động:
1. Camera IR ghi hình người lái
2. AI models phát hiện các dấu hiệu nguy hiểm
3. Cảnh báo real-time khi phát hiện rủi ro
4. Logging và analytics
```

#### **1.3. Objectives (Mục tiêu)**
```
Mục tiêu chính:
- Phát hiện 7+ hoạt động nguy hiểm (gọi điện, uống nước, hút thuốc, v.v.)
- Độ chính xác phát hiện >90%
- Phát hiện buồn ngủ với độ trễ <2 giây
- Real-time processing >15 FPS

Mục tiêu phụ:
- Hoạt động trong điều kiện ánh sáng khác nhau
- Xử lý được khi lái xe đeo kính/khẩu trang
- Giao diện thân thiện với người dùng
```

#### **1.4. Scope (Phạm vi)**
```
IN SCOPE (Bao gồm):
✅ Phát hiện buồn ngủ (eye closure, yawning)
✅ Phát hiện mất tập trung (head pose, gaze direction)
✅ Phát hiện hoạt động nguy hiểm (calling, drinking, smoking)
✅ Cảnh báo audio/visual real-time
✅ Logging events vào database
✅ Dashboard hiển thị status
✅ Xác thực người lái (face recognition)

OUT OF SCOPE (Không bao gồm):
❌ Mobile app
❌ Cloud synchronization
❌ Multi-vehicle fleet management
❌ Integration với hệ thống xe
❌ Autonomous driving features
```

#### **1.5. Technology Stack**
```
Hardware:
- IR Camera (Night vision capable)
- Raspberry Pi 4 / Jetson Nano
- Audio speaker (cho warning)
- Display screen (optional)

Software:
- Programming Language: Python 3.8+
- Computer Vision: OpenCV, dlib
- Deep Learning: TensorFlow / PyTorch
- Face Detection: MTCNN, Haar Cascade
- Database: PostgreSQL / SQLite
- Frontend (optional): React.js / Flask web UI
- Version Control: Git/GitHub
```

#### **1.6. Expected Outcomes (Kết quả Mong đợi)**
```
Deliverables:
- Working prototype system
- Source code với documentation
- Trained AI models
- Test results và evaluation metrics
- User manual
- Technical documentation
- Presentation slides

Performance Metrics:
- Drowsiness detection accuracy: >90%
- Activity recognition accuracy: >85%
- False positive rate: <5%
- System latency: <100ms
- FPS: >15
```

#### **1.7. Timeline (Kế hoạch Tổng thể)**
```
Phase 1 (Week 1-2): Planning & Setup
Phase 2 (Week 3-5): Requirements & Design
Phase 3 (Week 6-9): Development
Phase 4 (Week 10-12): Testing & Closure
```

**Độ dài:** 3-5 trang

**Tools:** Microsoft Word, Google Docs

**Template Structure:**
```
1. Cover Page
2. Problem Statement (1 trang)
3. Proposed Solution (1 trang)
4. Objectives & Scope (1 trang)
5. Technology Stack (0.5 trang)
6. Timeline & Expected Outcomes (0.5 trang)
7. References
```

**BMAD Support:** ❌ Không có workflow trực tiếp

**Thứ tự thực hiện:** Tuần 1

---

<a name="2-project-plan"></a>
### **2. PROJECT PLAN (Kế hoạch Dự án)** 📅

**Mục đích:** Lập kế hoạch chi tiết cho toàn bộ dự án

**Nội dung cần có:**

#### **2.1. Work Breakdown Structure (WBS)**
```
Driver Monitoring System
│
├── 1. Project Management
│   ├── 1.1 Planning
│   ├── 1.2 Meetings
│   └── 1.3 Documentation
│
├── 2. Requirements
│   ├── 2.1 Product Backlog
│   ├── 2.2 User Stories
│   └── 2.3 Acceptance Criteria
│
├── 3. Design
│   ├── 3.1 System Architecture
│   ├── 3.2 Database Design
│   └── 3.3 UI/UX Design
│
├── 4. Development
│   ├── 4.1 Camera Integration
│   ├── 4.2 Face Detection
│   ├── 4.3 Eye Tracking
│   ├── 4.4 Drowsiness Detection
│   ├── 4.5 Activity Recognition
│   ├── 4.6 Alert System
│   └── 4.7 Database Integration
│
├── 5. Testing
│   ├── 5.1 Unit Testing
│   ├── 5.2 Integration Testing
│   ├── 5.3 System Testing
│   └── 5.4 Acceptance Testing
│
└── 6. Deployment & Documentation
    ├── 6.1 System Deployment
    ├── 6.2 User Manual
    └── 6.3 Technical Documentation
```

#### **2.2. Gantt Chart**
```
Tạo Gantt chart với timeline:

Task                        | W1 | W2 | W3 | W4 | W5 | W6 | W7 | W8 | W9 | W10| W11| W12|
----------------------------|----|----|----|----|----|----|----|----|----|----|----|----|
Proposal                    |████|    |    |    |    |    |    |    |    |    |    |    |
Project Plan                |████|████|    |    |    |    |    |    |    |    |    |    |
Product Backlog             |    |    |████|    |    |    |    |    |    |    |    |    |
User Stories                |    |    |████|████|    |    |    |    |    |    |    |    |
Architecture Design         |    |    |    |████|    |    |    |    |    |    |    |    |
Database Design             |    |    |    |    |████|    |    |    |    |    |    |    |
UI Design                   |    |    |    |    |████|    |    |    |    |    |    |    |
Sprint 1: Foundation        |    |    |    |████|████|    |    |    |    |    |    |    |
Sprint 2: Core Features     |    |    |    |    |    |████|████|    |    |    |    |    |
Sprint 3: Advanced Features |    |    |    |    |    |    |    |████|████|    |    |    |
Sprint 4: Polish            |    |    |    |    |    |    |    |    |    |████|    |    |
Sprint 5: Testing           |    |    |    |    |    |    |    |    |    |    |████|    |
Final Documentation         |    |    |    |    |    |    |    |    |    |    |    |████|
```

#### **2.3. Resource Allocation**
```
Human Resources:
- Student Developer: Hung Thanh (Full-time, 40h/week)
- Advisor: Prof. Nguyen Van A (Consultation, 2h/week)

Hardware Resources:
- Development laptop (Week 1-12)
- IR Camera (Week 3-12)
- Raspberry Pi 4 (Week 5-12)
- Test devices (Week 8-12)

Software Resources:
- Python, OpenCV (Free)
- TensorFlow (Free)
- GitHub (Free)
- Cloud GPU (Optional, if needed)
```

#### **2.4. Risk Management**
```
RISK 1: Model Accuracy không đạt yêu cầu
├── Probability: Medium (40%)
├── Impact: High
├── Mitigation:
│   ├── Research pre-trained models
│   ├── Collect diverse training data
│   ├── Consult with advisor early
│   └── Have backup simpler algorithms
└── Contingency: Reduce accuracy target to 85%

RISK 2: Hardware delay/malfunction
├── Probability: Medium (30%)
├── Impact: Medium
├── Mitigation:
│   ├── Order hardware early (Week 1)
│   ├── Have backup camera
│   └── Test on laptop first before hardware
└── Contingency: Use laptop webcam for demo

RISK 3: Dataset không đủ/không đa dạng
├── Probability: High (50%)
├── Impact: Medium
├── Mitigation:
│   ├── Use public datasets (CEW, YawDD)
│   ├── Collect custom data from volunteers
│   └── Data augmentation techniques
└── Contingency: Focus on fewer activities with better data

RISK 4: Timeline delay
├── Probability: Medium (35%)
├── Impact: High
├── Mitigation:
│   ├── Weekly progress tracking
│   ├── Buffer time in schedule
│   └── Prioritize must-have features
└── Contingency: Reduce scope, focus on core features

RISK 5: Technical roadblocks
├── Probability: Medium (40%)
├── Impact: Medium
├── Mitigation:
│   ├── Research thoroughly before implementing
│   ├── Ask advisor for guidance
│   └── Active in online communities (Stack Overflow)
└── Contingency: Use simpler alternative approaches
```

#### **2.5. Budget (Ngân sách)**
```
Item                          | Cost      | Notes
------------------------------|-----------|------------------
IR Camera                     | $50-100   | One-time
Raspberry Pi 4 (4GB)          | $55       | One-time
MicroSD Card 64GB             | $15       | One-time
Power Supply                  | $10       | One-time
Camera Mount                  | $10       | One-time
Audio Speaker                 | $20       | One-time
Optional: Cloud GPU (Colab)   | $0        | Free tier
Optional: Domain/Hosting      | $20/year  | If web deploy
------------------------------|-----------|------------------
TOTAL ESTIMATE                | $180-230  |

Funding: Personal / School support
```

#### **2.6. Communication Plan**
```
Stakeholder: Advisor (Prof. Nguyen Van A)
├── Meeting Frequency: Bi-weekly (Every 2 weeks)
├── Meeting Duration: 1 hour
├── Meeting Format: In-person / Zoom
├── Agenda:
│   ├── Progress update
│   ├── Demo (if applicable)
│   ├── Blockers discussion
│   ├── Technical guidance
│   └── Next sprint planning
└── Communication Channel: Email (weekly updates)

Stakeholder: Self (Progress Tracking)
├── Daily standup (self): 15 min
├── Sprint retrospective: End of each sprint
└── Documentation: Update weekly
```

#### **2.7. Milestones**
```
Milestone 1: Proposal Approved
├── Week: 1
├── Deliverable: Approved proposal document
└── Criteria: Advisor sign-off

Milestone 2: Requirements Complete
├── Week: 4
├── Deliverable: Product Backlog + User Stories
└── Criteria: All features identified and prioritized

Milestone 3: Design Complete
├── Week: 5
├── Deliverable: Architecture + Database + UI Design
└── Criteria: Design reviewed and approved

Milestone 4: MVP Demo
├── Week: 7
├── Deliverable: Working prototype with core features
└── Criteria: Drowsiness detection working at >85% accuracy

Milestone 5: Feature Complete
├── Week: 10
├── Deliverable: All features implemented
└── Criteria: All must-have features done and tested

Milestone 6: Final Submission
├── Week: 12
├── Deliverable: Complete system + documentation
└── Criteria: All deliverables submitted, ready for defense
```

**Độ dài:** 10-15 trang

**Tools:**
- Microsoft Project (professional)
- Trello + Google Sheets (simple)
- Jira (Agile)
- GanttProject (free Gantt chart software)
- Draw.io (WBS diagram)

**BMAD Support:** ❌ Không có workflow trực tiếp

**Thứ tự thực hiện:** Tuần 1-2

---

<a name="3-product-backlog"></a>
### **3. PRODUCT BACKLOG** 📦

**Mục đích:** Danh sách TẤT CẢ features/requirements của hệ thống, có ưu tiên

**Format chuẩn:**

| ID   | Feature | Description | Priority | Story Points | Status |
|------|---------|-------------|----------|--------------|--------|
| F001 | Driver Authentication | Xác thực người lái qua khuôn mặt | Must Have | 13 | To Do |
| F002 | Drowsiness Detection | Phát hiện buồn ngủ qua mắt/ngáp | Must Have | 21 | To Do |
| F003 | Distraction Detection | Phát hiện mất tập trung | Must Have | 13 | To Do |
| F004 | Activity Recognition | Phát hiện hoạt động nguy hiểm | Must Have | 21 | To Do |
| F005 | Real-time Alert System | Cảnh báo audio/visual | Must Have | 8 | To Do |
| F006 | Eye Tracking | Theo dõi vị trí và trạng thái mắt | Must Have | 13 | To Do |
| F007 | Head Pose Estimation | Ước lượng hướng đầu | Should Have | 13 | To Do |
| F008 | Gaze Direction Tracking | Theo dõi hướng nhìn | Should Have | 13 | To Do |
| F009 | Mask/Glasses Detection | Phát hiện khẩu trang/kính | Should Have | 8 | To Do |
| F010 | Passenger Counting | Đếm số hành khách | Could Have | 8 | To Do |
| F011 | Camera Health Check | Kiểm tra camera hoạt động | Should Have | 5 | To Do |
| F012 | Event Logging | Ghi log các sự kiện | Must Have | 5 | To Do |
| F013 | Dashboard UI | Giao diện hiển thị status | Should Have | 13 | To Do |
| F014 | Historical Analytics | Phân tích dữ liệu lịch sử | Could Have | 13 | To Do |
| F015 | Driver Enrollment | Đăng ký người lái mới | Should Have | 8 | To Do |

#### **3.1. Phân loại MoSCoW**

**MUST HAVE (Core Safety Features)** - Không thể thiếu
```
F001: Driver Drowsiness Detection
├── Description: Phát hiện buồn ngủ qua EAR (Eye Aspect Ratio)
├── Acceptance: Accuracy >90%, Latency <2s
└── Priority: Highest

F002: Driver Distraction Detection
├── Description: Phát hiện mất tập trung qua head pose
├── Acceptance: Accuracy >85%, False positive <5%
└── Priority: Highest

F003: Dangerous Activity Detection
├── Activities: Calling, Drinking, Smoking, Hands off wheel
├── Acceptance: Accuracy >85% cho mỗi activity
└── Priority: Highest

F004: Real-time Warning System
├── Description: Audio + Visual alerts khi phát hiện nguy hiểm
├── Acceptance: Latency <100ms, Clear và không làm phiền
└── Priority: Highest

F005: Eye Tracking & Blink Detection
├── Description: Theo dõi vị trí mắt, tần số chớp mắt
├── Acceptance: Detect eyes trong 95% frames
└── Priority: High

F006: Event Logging
├── Description: Ghi lại tất cả events vào database
├── Acceptance: 100% events được log với timestamp
└── Priority: High

F007: Face Detection & Tracking
├── Description: Phát hiện và theo dõi khuôn mặt người lái
├── Acceptance: Detection rate >95%, FPS >15
└── Priority: Highest (Foundation cho tất cả)
```

**SHOULD HAVE (Enhanced Features)** - Rất quan trọng
```
F008: Driver Authentication
├── Description: Xác thực người lái qua face recognition
├── Acceptance: Recognition accuracy >95%
└── Priority: Medium-High

F009: Mask/Glasses Detection
├── Description: Phát hiện khi đeo khẩu trang/kính
├── Acceptance: System vẫn hoạt động với mask/glasses
└── Priority: Medium-High

F010: Camera Health Check
├── Description: Phát hiện camera bị che/hỏng/di chuyển
├── Acceptance: Detect malfunction trong 2s
└── Priority: Medium

F011: Head Pose Monitoring
├── Description: Ước lượng góc xoay đầu (yaw, pitch, roll)
├── Acceptance: Accuracy ±5 degrees
└── Priority: Medium

F012: Dashboard UI
├── Description: Giao diện hiển thị status real-time
├── Acceptance: Update UI <100ms, Clear visualization
└── Priority: Medium

F013: Driver Enrollment
├── Description: Đăng ký người lái mới vào hệ thống
├── Acceptance: Enrollment process <1 minute
└── Priority: Medium
```

**COULD HAVE (Nice to Have)** - Nếu có thời gian
```
F014: Passenger Counting
├── Description: Đếm số hành khách trong xe
├── Acceptance: Count accuracy >85%
└── Priority: Low

F015: Gaze Zone Mapping
├── Description: Xác định zone người lái đang nhìn (road, mirror, phone)
├── Acceptance: Zone classification accuracy >80%
└── Priority: Low

F016: Facial Expression Analysis
├── Description: Phân tích biểu cảm (angry, stressed, happy)
├── Acceptance: Expression classification accuracy >75%
└── Priority: Low

F017: Historical Analytics Dashboard
├── Description: Dashboard phân tích dữ liệu lịch sử
├── Acceptance: Generate reports với charts
└── Priority: Low
```

**WON'T HAVE (Out of Scope)** - Không làm trong đồ án này
```
❌ Mobile App
❌ Cloud Synchronization
❌ Multi-vehicle Fleet Management
❌ Voice Control
❌ Integration với vehicle systems
❌ Autonomous driving features
```

#### **3.2. Product Backlog Example (Chi tiết)**

```markdown
# PRODUCT BACKLOG - Driver Monitoring System

**Version:** 1.0  
**Date:** 2026-03-03  
**Owner:** Hung Thanh

---

## EPIC 1: Core Detection System

### F001: Face Detection & Tracking
**Priority:** Must Have  
**Story Points:** 13  
**Sprint:** 1  

**Description:**
Implement real-time face detection and tracking system using OpenCV/dlib to locate and track driver's face in video stream.

**Acceptance Criteria:**
- Face detected in >95% of frames (good lighting)
- Face detection works at >15 FPS
- Multiple face detection (but track only driver)
- Recovery when face temporarily lost

**Technical Notes:**
- Use MTCNN or Haar Cascade for detection
- Implement face tracking to reduce computation
- Handle edge cases: sunglasses, partial occlusion

**Dependencies:** None (Foundation)

---

### F002: Eye Tracking & Detection
**Priority:** Must Have  
**Story Points:** 13  
**Sprint:** 1-2  

**Description:**
Detect and track eye locations, calculate Eye Aspect Ratio (EAR) for drowsiness detection.

**Acceptance Criteria:**
- Eyes detected when face detected
- EAR calculated correctly
- Blink detection functional
- Works with glasses

**Technical Notes:**
- Use dlib 68-point facial landmarks
- EAR formula: (||p2-p6|| + ||p3-p5||) / (2||p1-p4||)
- Threshold: EAR < 0.25 for closed eyes

**Dependencies:** F001 (Face Detection)

---

### F003: Drowsiness Detection
**Priority:** Must Have  
**Story Points:** 21  
**Sprint:** 2  

**Description:**
Detect drowsiness based on eye closure duration, blink frequency, and yawning.

**Acceptance Criteria:**
- Detect eye closure >2 seconds → Alert
- Detect yawning → Warning
- Low blink frequency (<10/min) → Warning
- Accuracy >90%
- False positive rate <5%

**Technical Notes:**
- Use EAR for eye closure
- Use MAR (Mouth Aspect Ratio) for yawning
- Implement temporal smoothing (avoid false positives)
- Test with drowsy driver dataset (CEW, YawDD)

**Dependencies:** F002 (Eye Tracking)

---

### F004: Distraction Detection
**Priority:** Must Have  
**Story Points:** 13  
**Sprint:** 2-3  

**Description:**
Detect when driver is distracted by monitoring head pose and gaze direction.

**Acceptance Criteria:**
- Detect head turn >30° → Warning
- Detect prolonged look away (>3s) → Alert
- Accuracy >85%

**Technical Notes:**
- Use head pose estimation (solvePnP)
- Define gaze zones (road, mirror, phone, passenger)
- Implement thresholds for alert triggering

**Dependencies:** F001 (Face Detection)

---

### F005: Activity Recognition
**Priority:** Must Have  
**Story Points:** 21  
**Sprint:** 3-4  

**Description:**
Detect dangerous driver activities: calling, drinking, smoking, yawning, hands off wheel, arm out window.

**Acceptance Criteria:**
- Detect calling (phone near ear) >85% accuracy
- Detect drinking (object near mouth) >85% accuracy
- Detect smoking (object near mouth, specific shape) >80% accuracy
- Detect hands off wheel (steering wheel visible) >85% accuracy

**Technical Notes:**
- Use CNN for activity classification
- Options: Custom CNN, Transfer learning (MobileNet, ResNet)
- Dataset: State Farm Distracted Driver Dataset
- May need hand detection (MediaPipe Hands)

**Dependencies:** F001 (Face Detection), F002 (Eye Tracking)

---

## EPIC 2: Alert & Warning System

### F006: Real-time Alert System
**Priority:** Must Have  
**Story Points:** 8  
**Sprint:** 2  

**Description:**
Trigger audio and visual alerts when dangerous conditions detected.

**Acceptance Criteria:**
- Audio alert plays within 100ms of detection
- Visual alert displays on screen
- Alert levels: Info, Warning, Critical
- Alert can be acknowledged
- No alert fatigue (smart triggering)

**Technical Notes:**
- Use pygame for audio
- Color-coded visual alerts (yellow, orange, red)
- Implement alert queue (avoid spam)
- Configurable alert sounds

**Dependencies:** F003, F004, F005 (Detection features)

---

## EPIC 3: Data & Analytics

### F007: Event Logging
**Priority:** Must Have  
**Story Points:** 5  
**Sprint:** 2  

**Description:**
Log all detection events to database for later analysis.

**Acceptance Criteria:**
- All events logged with timestamp
- Event details: type, severity, confidence
- Snapshot image saved (optional)
- Query interface for historical data

**Technical Notes:**
- Use SQLite (simple) or PostgreSQL (scalable)
- Schema: events table with foreign keys
- Consider storage size (limit snapshots)

**Dependencies:** Database Design

---

## EPIC 4: UI & User Experience

### F008: Dashboard UI
**Priority:** Should Have  
**Story Points:** 13  
**Sprint:** 4  

**Description:**
Real-time dashboard showing driver status, detected events, and system health.

**Acceptance Criteria:**
- Live camera feed displayed
- Status indicators for all monitored attributes
- Event history visible
- UI updates <100ms

**Technical Notes:**
- Options: Tkinter, PyQt5, Flask web UI
- Consider performance (UI shouldn't slow detection)
- Responsive design

**Dependencies:** All detection features

---

## EPIC 5: System Health & Robustness

### F009: Camera Health Check
**Priority:** Should Have  
**Story Points:** 5  
**Sprint:** 4  

**Description:**
Detect camera malfunctions, blockages, or movement.

**Acceptance Criteria:**
- Detect camera blocked (black frames)
- Detect camera moved (scene change)
- Detect camera malfunction (error)
- Alert user to camera issues

**Technical Notes:**
- Check frame quality (brightness, blur)
- Compare frames for movement detection
- Handle camera reconnection

**Dependencies:** Camera Integration

---

## EPIC 6: Authentication & Enrollment

### F010: Driver Authentication
**Priority:** Should Have  
**Story Points:** 13  
**Sprint:** 4  

**Description:**
Authenticate driver identity using face recognition.

**Acceptance Criteria:**
- Recognition accuracy >95%
- Authentication time <2 seconds
- Support multiple enrolled drivers
- Handle face changes (beard, glasses)

**Technical Notes:**
- Use face_recognition library or FaceNet
- Store face embeddings (not images)
- Implement 1:N matching

**Dependencies:** F001 (Face Detection)

---

### F011: Driver Enrollment
**Priority:** Should Have  
**Story Points:** 8  
**Sprint:** 5  

**Description:**
Allow new drivers to enroll in system.

**Acceptance Criteria:**
- Enrollment captures multiple face angles
- Enrollment completes in <1 minute
- Face data stored securely
- Can update enrollment

**Technical Notes:**
- Capture 10-20 face images
- Generate face embeddings
- UI for enrollment process

**Dependencies:** F010 (Authentication)

---

## Story Points Reference:

- 1-2: Trivial (few hours)
- 3-5: Simple (1 day)
- 8: Medium (2-3 days)
- 13: Complex (1 week)
- 21: Very Complex (2 weeks)
- 40: Epic (break down further)

## Total Story Points: ~180 (Adjusted for 10 weeks development)
```

**Tools:**
- Google Sheets (simple)
- Jira (professional)
- Trello (visual)
- Notion (structured)

**BMAD Support:** ✅ `/bmad-brainstorming` - ĐANG DÙNG workflow này!

**Thứ tự thực hiện:** Tuần 3-4

---

<a name="4-user-stories"></a>
### **4. USER STORIES** 📖

**Mục đích:** Mô tả features từ góc nhìn người dùng, có acceptance criteria

**Format chuẩn Agile:**

```markdown
# USER STORIES - Driver Monitoring System

---

## US-001: Detect Driver Drowsiness

**Epic:** Core Detection System  
**Feature:** F003 (Drowsiness Detection)  
**Priority:** Must Have  
**Story Points:** 21  
**Sprint:** 2

### User Story:
```
As a fleet manager
I want the system to detect when a driver shows signs of drowsiness
So that I can prevent accidents caused by falling asleep at the wheel
```

### Acceptance Criteria:

**Scenario 1: Prolonged Eye Closure**
```
Given the driver is being monitored by the camera
When the system detects closed eyes for more than 2 seconds
Then an audio warning should be triggered immediately
And the event should be logged with timestamp and severity "HIGH"
And a snapshot image should be saved
```

**Scenario 2: Frequent Yawning**
```
Given the driver is being monitored
When the driver yawns 3 or more times within 1 minute
Then a visual + audio alert should activate
And the severity level should be marked as "MEDIUM"
And the event should be logged
```

**Scenario 3: Low Blink Frequency**
```
Given the driver has been monitored for at least 2 minutes
When the blink frequency is less than 10 blinks per minute
Then a warning indicator should display
And the severity should be marked as "LOW"
```

**Scenario 4: False Positive Handling**
```
Given the driver briefly closes eyes (e.g., long blink)
When eye closure duration is less than 2 seconds
Then no alert should be triggered
But the blink should be counted for frequency tracking
```

### Technical Acceptance Criteria:
- [ ] Drowsiness detection accuracy >90% (tested on CEW dataset)
- [ ] False positive rate <5%
- [ ] System latency from detection to alert <100ms
- [ ] Works in various lighting conditions
- [ ] Works when driver wearing glasses

### Definition of Done:
- [ ] Code implemented and unit tested
- [ ] Integration tested with camera feed
- [ ] Accuracy tested on test dataset
- [ ] Alert system integrated
- [ ] Event logging functional
- [ ] Code reviewed and documented
- [ ] Demo to advisor approved

### Notes:
- Test with real drowsy driver videos
- Consider driver wearing sunglasses (IR camera helps)
- May need to adjust thresholds based on testing

### Dependencies:
- US-002: Eye Tracking
- US-010: Camera Integration

---

## US-002: Track Driver Eyes

**Epic:** Core Detection System  
**Feature:** F002 (Eye Tracking)  
**Priority:** Must Have  
**Story Points:** 13  
**Sprint:** 1-2

### User Story:
```
As a system
I want to accurately track the driver's eye locations and status
So that I can calculate metrics for drowsiness and attention detection
```

### Acceptance Criteria:

**Scenario 1: Eye Detection**
```
Given a driver's face is detected in the frame
When the face is in good lighting and relatively frontal
Then both eyes should be detected and located
And eye landmarks should be identified (6 points per eye)
```

**Scenario 2: Eye Aspect Ratio Calculation**
```
Given both eyes are detected
When eye landmarks are available
Then Eye Aspect Ratio (EAR) should be calculated for each eye
And the average EAR should be computed
And EAR value should be between 0.0 and 1.0
```

**Scenario 3: Blink Detection**
```
Given eyes are being tracked
When EAR drops below threshold (0.25) then rises above
Then a blink event should be detected
And blink count should increment
And blink frequency should be calculated (blinks per minute)
```

**Scenario 4: Glasses Handling**
```
Given the driver is wearing regular glasses
When face and eyes are detected
Then eye tracking should still function correctly
And EAR calculation should remain accurate
```

### Technical Acceptance Criteria:
- [ ] Eyes detected in >95% of frames where face is visible
- [ ] EAR calculation accuracy validated
- [ ] Blink detection sensitivity tuned (detect blinks, not false positives)
- [ ] Performance: Eye detection at >20 FPS
- [ ] Works with various face angles (±30 degrees)

### Definition of Done:
- [ ] dlib 68-point facial landmarks integrated
- [ ] EAR calculation implemented and tested
- [ ] Blink detection algorithm implemented
- [ ] Unit tests written and passing
- [ ] Performance benchmarked
- [ ] Works on test videos

### Notes:
- EAR formula: EAR = (||p2-p6|| + ||p3-p5||) / (2||p1-p4||)
- Threshold 0.25 is standard, may need tuning
- Consider temporal smoothing for noise reduction

### Dependencies:
- US-010: Camera Integration
- US-011: Face Detection

---

## US-003: Alert Driver When Distracted

**Epic:** Alert & Warning System  
**Feature:** F006 (Real-time Alert)  
**Priority:** Must Have  
**Story Points:** 8  
**Sprint:** 2

### User Story:
```
As a driver
I want to receive immediate alerts when the system detects I'm distracted
So that I can refocus my attention on the road and drive safely
```

### Acceptance Criteria:

**Scenario 1: Audio Alert**
```
Given a dangerous condition is detected (drowsiness, distraction, etc.)
When the confidence level is above threshold (>0.8)
Then an audio alert should play within 100ms
And the alert sound should be loud enough to be heard while driving
And the alert should match the severity (different sounds for different levels)
```

**Scenario 2: Visual Alert**
```
Given a dangerous condition is detected
When the alert is triggered
Then a visual warning should display on screen
And the color should indicate severity:
  - Yellow: Low severity warning
  - Orange: Medium severity warning
  - Red: Critical alert
And the alert message should clearly state the issue
```

**Scenario 3: Alert Acknowledgement**
```
Given an alert is currently active
When the driver corrects the behavior (e.g., opens eyes, looks forward)
Then the alert should automatically dismiss after 2 seconds
And the event should be logged as "resolved"
```

**Scenario 4: Alert Fatigue Prevention**
```
Given multiple alerts triggered in short time
When conditions are continuously dangerous
Then alerts should be throttled (e.g., max 1 alert per 5 seconds)
But the continuous dangerous state should be logged
```

### Technical Acceptance Criteria:
- [ ] Audio latency <100ms from detection
- [ ] Visual alert displays within 50ms
- [ ] Alert queue prevents spam
- [ ] Different alert sounds for severity levels
- [ ] Alert volume configurable
- [ ] Alert system doesn't slow down detection (<5% performance impact)

### Definition of Done:
- [ ] Audio alert system implemented (pygame/pydub)
- [ ] Visual alert UI implemented
- [ ] Alert queue and throttling logic implemented
- [ ] Tested with different alert scenarios
- [ ] User testing confirms alerts are clear and not annoying
- [ ] Integration tested with all detection features

### Notes:
- Consider haptic feedback if hardware available
- Test alert effectiveness (not too annoying, not too subtle)
- May need "Do Not Disturb" mode for testing

### Dependencies:
- US-001: Drowsiness Detection
- US-004: Distraction Detection
- US-005: Activity Recognition

---

## US-004: Detect Driver Distraction

**Epic:** Core Detection System  
**Feature:** F004 (Distraction Detection)  
**Priority:** Must Have  
**Story Points:** 13  
**Sprint:** 2-3

### User Story:
```
As a safety officer
I want the system to detect when a driver is not paying attention to the road
So that I can intervene before a distraction leads to an accident
```

### Acceptance Criteria:

**Scenario 1: Head Turned Away**
```
Given the driver's face is being tracked
When the head pose shows yaw angle >30 degrees (looking left/right)
And this state persists for >2 seconds
Then a distraction alert should be triggered
And the gaze direction should be logged
```

**Scenario 2: Looking Down (Phone)**
```
Given the driver's head pose is being monitored
When the pitch angle <-20 degrees (looking down)
And this state persists for >1.5 seconds
Then a "looking at phone" alert should be triggered
And severity should be marked as "HIGH"
```

**Scenario 3: Looking at Passenger**
```
Given the driver is looking to the side
When the yaw angle is >45 degrees for >3 seconds
Then a "not watching road" alert should trigger
```

**Scenario 4: Brief Glance (Mirror Check)**
```
Given the driver briefly looks away
When the look-away duration is <1 second
Then no alert should be triggered (normal mirror check)
But the event should be logged for frequency analysis
```

### Technical Acceptance Criteria:
- [ ] Head pose estimation accuracy ±5 degrees
- [ ] Distraction detection accuracy >85%
- [ ] False positive rate <5% (don't alert on mirror checks)
- [ ] Works at various face distances from camera
- [ ] Real-time processing (>15 FPS)

### Definition of Done:
- [ ] Head pose estimation implemented (solvePnP)
- [ ] Gaze direction zones defined and tested
- [ ] Temporal thresholds tuned
- [ ] Tested on distracted driver dataset
- [ ] Integration with alert system
- [ ] Accuracy metrics documented

### Notes:
- Use 3D head model + 2D facial landmarks for pose estimation
- Define gaze zones: Road (front), Left Mirror, Right Mirror, Rear Mirror, Down (phone), Passenger
- Consider normal driving behaviors (mirror checks are OK)

### Dependencies:
- US-011: Face Detection
- US-003: Alert System

---

## US-005: Recognize Dangerous Activities

**Epic:** Core Detection System  
**Feature:** F005 (Activity Recognition)  
**Priority:** Must Have  
**Story Points:** 21  
**Sprint:** 3-4

### User Story:
```
As a fleet manager
I want the system to recognize when drivers are performing dangerous activities
So that I can identify risky behaviors and provide targeted training
```

### Acceptance Criteria:

**Scenario 1: Detect Phone Use (Calling)**
```
Given the driver is being monitored
When the system detects:
  - Hand near face/ear
  - Phone-shaped object visible
  - Head tilted (typical calling posture)
Then classify as "calling" activity
And trigger alert with severity "HIGH"
And log event with confidence score
```

**Scenario 2: Detect Drinking**
```
Given the driver is being monitored
When the system detects:
  - Object moving toward mouth
  - Drinking motion pattern
  - Bottle/cup shape
Then classify as "drinking" activity
And trigger alert with severity "MEDIUM"
```

**Scenario 3: Detect Smoking**
```
Given the driver is being monitored
When the system detects:
  - Small object near mouth repeatedly
  - Smoking gesture pattern
Then classify as "smoking" activity
And trigger alert with severity "MEDIUM"
```

**Scenario 4: Detect Hands Off Wheel**
```
Given the driver should have hands on wheel
When the system detects:
  - No hands visible on steering wheel
  - Duration >3 seconds
Then trigger "hands off wheel" alert
And severity "HIGH"
```

### Technical Acceptance Criteria:
- [ ] Activity classification accuracy >85% per activity
- [ ] Multi-class confusion matrix documented
- [ ] Real-time inference <50ms per frame
- [ ] Works with different hand sizes, objects
- [ ] Handles occlusions gracefully

### Definition of Done:
- [ ] Activity recognition model trained and tested
- [ ] Achieved target accuracy on validation set
- [ ] Integrated with detection pipeline
- [ ] Alert triggering logic implemented
- [ ] Event logging with activity labels
- [ ] Performance optimized for real-time

### Notes:
- Options: Train custom CNN, use transfer learning (MobileNetV2, ResNet50)
- Dataset: State Farm Distracted Driver Dataset
- Consider hand detection (MediaPipe Hands) + object detection
- May need data augmentation for robustness

### Dependencies:
- US-011: Face Detection
- US-003: Alert System
- Dataset collection/preparation

---

## US-010: Integrate Camera System

**Epic:** Foundation  
**Feature:** Foundation  
**Priority:** Must Have  
**Story Points:** 8  
**Sprint:** 1

### User Story:
```
As a system
I want to reliably capture video frames from the IR camera
So that I can process them for driver monitoring
```

### Acceptance Criteria:

**Scenario 1: Camera Initialization**
```
Given the system starts up
When the camera initialization is triggered
Then the IR camera should be detected
And video capture should begin successfully
And frame rate should be at least 30 FPS
```

**Scenario 2: Frame Capture**
```
Given the camera is running
When frames are requested
Then frames should be returned in RGB format
And resolution should be 640x480 or higher
And frames should have good quality (not blurry, not dark)
```

**Scenario 3: Error Handling**
```
Given the camera connection fails
When the system tries to capture frames
Then an error should be logged
And the system should attempt reconnection
And the UI should display "camera error" status
```

**Scenario 4: Night Vision (IR)**
```
Given low light conditions (night, tunnel)
When the IR camera is active
Then faces should still be detectable
And image quality should be sufficient for detection
```

### Technical Acceptance Criteria:
- [ ] Camera capture rate: 30 FPS
- [ ] Frame processing pipeline doesn't drop frames
- [ ] IR mode works in total darkness
- [ ] Camera auto-reconnects if disconnected
- [ ] Resource cleanup on exit

### Definition of Done:
- [ ] OpenCV VideoCapture implemented
- [ ] Frame preprocessing pipeline implemented
- [ ] Error handling and recovery implemented
- [ ] Tested with actual IR camera hardware
- [ ] Performance benchmarked

### Notes:
- Use OpenCV cv2.VideoCapture()
- Consider frame buffering for smooth processing
- Test with multiple camera models/brands

### Dependencies: None (Foundation)

---

## US-011: Detect and Track Driver Face

**Epic:** Foundation  
**Feature:** F001 (Face Detection)  
**Priority:** Must Have  
**Story Points:** 13  
**Sprint:** 1

### User Story:
```
As a system
I want to accurately detect and track the driver's face in real-time
So that I can perform further analysis on facial features
```

### Acceptance Criteria:

**Scenario 1: Face Detection**
```
Given a video frame from the camera
When the frame contains a driver's face
Then the face should be detected
And bounding box coordinates should be returned
And detection should work at >15 FPS
```

**Scenario 2: Face Tracking**
```
Given a face has been detected in previous frames
When processing subsequent frames
Then the same face should be tracked (not re-detected)
And tracking should be more efficient than detection
And tracking should recover if face temporarily lost
```

**Scenario 3: Multiple Faces**
```
Given multiple faces appear in frame (driver + passenger)
When faces are detected
Then the system should identify which is the driver
And focus only on driver's face
```

**Scenario 4: Edge Cases**
```
Given various challenging conditions:
  - Driver wearing sunglasses
  - Driver wearing mask (partial face)
  - Profile view (not frontal)
  - Motion blur
When face detection is attempted
Then face should still be detected in >85% of cases
```

### Technical Acceptance Criteria:
- [ ] Face detection rate >95% (frontal, good lighting)
- [ ] Face detection rate >85% (with sunglasses/mask)
- [ ] Processing speed >15 FPS
- [ ] Tracking reduces computation by 30%+
- [ ] Works with face at 30-100cm from camera

### Definition of Done:
- [ ] Face detection algorithm selected and implemented (MTCNN/Haar/HOG)
- [ ] Face tracking implemented (dlib correlation tracker)
- [ ] Multi-face handling implemented
- [ ] Edge cases tested and documented
- [ ] Performance benchmarked
- [ ] Integration tested with camera feed

### Notes:
- Options: MTCNN (accurate), Haar Cascade (fast), HOG (balanced)
- Consider using dlib for tracking after initial detection
- Test with various face angles, lighting, occlusions

### Dependencies:
- US-010: Camera Integration

---

## US-020: Authenticate Driver Identity

**Epic:** Authentication & Enrollment  
**Feature:** F010 (Driver Authentication)  
**Priority:** Should Have  
**Story Points:** 13  
**Sprint:** 4

### User Story:
```
As a fleet manager
I want the system to authenticate the driver's identity
So that I can ensure only authorized drivers operate the vehicle
```

### Acceptance Criteria:

**Scenario 1: Successful Authentication**
```
Given a driver is enrolled in the system
When the driver sits in the vehicle
And their face is captured by the camera
Then the system should recognize the driver within 2 seconds
And display "Authenticated: [Driver Name]"
And allow monitoring to begin
```

**Scenario 2: Unknown Driver**
```
Given an unknown person sits in the vehicle
When their face is captured
Then the system should show "Unknown Driver"
And prompt for enrollment or manual identification
And optionally disable vehicle start
```

**Scenario 3: Authentication Confidence**
```
Given face recognition is performed
When the confidence score is computed
Then authentication should succeed if confidence >0.85
And authentication should fail if confidence <0.85
And the confidence score should be logged
```

**Scenario 4: Appearance Changes**
```
Given an enrolled driver has changed appearance (beard, glasses)
When authentication is attempted
Then the system should still recognize them (>90% cases)
Or prompt for re-enrollment if confidence consistently low
```

### Technical Acceptance Criteria:
- [ ] Recognition accuracy >95% (enrolled drivers)
- [ ] False acceptance rate <2%
- [ ] False rejection rate <5%
- [ ] Authentication time <2 seconds
- [ ] Supports up to 50 enrolled drivers

### Definition of Done:
- [ ] Face recognition model integrated (face_recognition/FaceNet)
- [ ] Face embeddings database created
- [ ] Authentication logic implemented
- [ ] Tested with multiple enrolled users
- [ ] Edge cases handled (lighting, angles)
- [ ] Performance meets requirements

### Notes:
- Use face_recognition library (built on dlib)
- Store face embeddings (128D vectors), not raw images
- Implement 1:N matching against enrolled database
- Consider re-authentication periodically during trip

### Dependencies:
- US-011: Face Detection
- US-021: Driver Enrollment

---

## US-021: Enroll New Driver

**Epic:** Authentication & Enrollment  
**Feature:** F011 (Driver Enrollment)  
**Priority:** Should Have  
**Story Points:** 8  
**Sprint:** 5

### User Story:
```
As a system administrator
I want to enroll new drivers into the system
So that they can be authenticated and monitored
```

### Acceptance Criteria:

**Scenario 1: Enrollment Process**
```
Given a new driver needs to be enrolled
When the enrollment process is started
Then the system should prompt the driver to:
  1. Enter their name
  2. Position face in frame
  3. Capture 10-15 face images from different angles
And the process should complete in less than 1 minute
```

**Scenario 2: Face Capture**
```
Given the enrollment is in progress
When face images are being captured
Then the system should guide the driver:
  - "Look straight ahead" (capture)
  - "Turn slightly left" (capture)
  - "Turn slightly right" (capture)
  - "Tilt head up" (capture)
  - "Tilt head down" (capture)
And ensure good image quality (lighting, blur check)
```

**Scenario 3: Enrollment Validation**
```
Given face images are captured
When generating face embeddings
Then all embeddings should be similar (same person)
And outliers should be rejected
And enrollment should succeed with >10 valid images
```

**Scenario 4: Update Enrollment**
```
Given a driver is already enrolled
When their appearance has changed significantly
Then they should be able to re-enroll
And update their face data
And old data should be archived (not deleted)
```

### Technical Acceptance Criteria:
- [ ] Enrollment captures 10-15 good quality images
- [ ] Enrollment time <1 minute
- [ ] Face embeddings stored securely
- [ ] Duplicate enrollment prevented (same person)
- [ ] UI provides clear instructions

### Definition of Done:
- [ ] Enrollment UI implemented
- [ ] Face capture logic with quality checks
- [ ] Face embedding generation and storage
- [ ] Duplicate detection implemented
- [ ] Update enrollment functionality
- [ ] User tested for ease of use

### Notes:
- Store embeddings in database with driver metadata
- Consider privacy: encrypt embeddings, don't store raw images
- UI can be simple (terminal) or graphical (tkinter)

### Dependencies:
- US-011: Face Detection
- US-020: Driver Authentication
- Database schema design

---

## Template for Additional User Stories:

```markdown
## US-XXX: [User Story Title]

**Epic:** [Epic Name]  
**Feature:** [Feature ID]  
**Priority:** [Must/Should/Could/Won't Have]  
**Story Points:** [1/2/3/5/8/13/21]  
**Sprint:** [Sprint Number]

### User Story:
```
As a [role]
I want [feature]
So that [benefit]
```

### Acceptance Criteria:

**Scenario 1: [Scenario Name]**
```
Given [precondition]
When [action]
Then [expected result]
And [additional result]
```

### Technical Acceptance Criteria:
- [ ] [Technical requirement 1]
- [ ] [Technical requirement 2]

### Definition of Done:
- [ ] Code implemented
- [ ] Unit tests written
- [ ] Integration tested
- [ ] Code reviewed
- [ ] Documented

### Notes:
[Additional context, technical notes, research needed]

### Dependencies:
- US-XXX: [Dependent story]
```

---

## User Story Mapping:

```
Driver Monitoring System - User Story Map

USER ACTIVITIES (Horizontal):
[Setup] → [Monitor] → [Alert] → [Review] → [Maintain]

STORIES (Vertical by Activity):

Setup:
├── US-021: Enroll Driver
├── US-010: Camera Integration
└── US-030: System Configuration

Monitor:
├── US-011: Face Detection
├── US-002: Eye Tracking
├── US-001: Drowsiness Detection
├── US-004: Distraction Detection
└── US-005: Activity Recognition

Alert:
├── US-003: Alert Driver
└── US-031: Alert Configuration

Review:
├── US-040: View Event History
├── US-041: Generate Reports
└── US-042: Analytics Dashboard

Maintain:
├── US-050: Camera Health Check
└── US-051: System Diagnostics
```

---

## Acceptance Criteria Checklist:

For each User Story, ensure acceptance criteria includes:

✅ **Functional Criteria**
- Happy path scenario
- Alternative flows
- Edge cases
- Error handling

✅ **Non-Functional Criteria**
- Performance (speed, latency)
- Accuracy (if ML/AI)
- Usability (if UI)
- Reliability (uptime, error recovery)

✅ **Given-When-Then Format**
- Clear preconditions
- Specific actions
- Measurable outcomes

✅ **Definition of Done**
- Code complete
- Tests written and passing
- Documented
- Reviewed
- Demo ready

```

**Tools:**
- Jira (professional, integrated with Agile)
- Notion (structured, collaborative)
- Google Docs (simple)
- Confluence (documentation platform)

**BMAD Support:** ✅ `/bmad-brainstorming` - Workflow này sẽ tạo User Stories!

**Thứ tự thực hiện:** Tuần 3-4 (cùng với Product Backlog)

---

<a name="5-architecture"></a>
### **5. ARCHITECTURE (Kiến trúc Hệ thống)** 🏗️

**Mục đích:** Thiết kế kiến trúc tổng thể của hệ thống

**Nội dung cần có:**

#### **5.1. System Architecture Diagram (High-Level)**

```
┌─────────────────────────────────────────────────────────────┐
│                    DRIVER MONITORING SYSTEM                  │
└─────────────────────────────────────────────────────────────┘

┌──────────────┐
│  IR CAMERA   │
│  (Hardware)  │
└──────┬───────┘
       │ Video Stream
       ↓
┌──────────────────────────────────────────────────────────────┐
│                    INPUT LAYER                                │
├──────────────────────────────────────────────────────────────┤
│  • Camera Capture Module                                     │
│  • Frame Buffer & Queue                                      │
│  • Image Preprocessing                                       │
└──────────────────┬───────────────────────────────────────────┘
                   │ Preprocessed Frames
                   ↓
┌──────────────────────────────────────────────────────────────┐
│                  DETECTION LAYER                              │
├──────────────────────────────────────────────────────────────┤
│  ┌─────────────────┐  ┌──────────────────┐                 │
│  │ Face Detection  │  │  Eye Tracking    │                 │
│  │  & Tracking     │  │  & Blink Detect  │                 │
│  └────────┬────────┘  └────────┬─────────┘                 │
│           │                     │                            │
│           └──────────┬──────────┘                            │
│                      │                                       │
│  ┌──────────────────┴──────────────────┐                   │
│  │     Feature Extraction               │                   │
│  │  • Facial Landmarks (68 points)     │                   │
│  │  • EAR (Eye Aspect Ratio)           │                   │
│  │  • MAR (Mouth Aspect Ratio)         │                   │
│  │  • Head Pose (yaw, pitch, roll)     │                   │
│  └──────────────────┬──────────────────┘                   │
└───────────────────────────────────────────────────────────┘
                       │ Features
                       ↓
┌──────────────────────────────────────────────────────────────┐
│               AI/ML INFERENCE LAYER                           │
├──────────────────────────────────────────────────────────────┤
│  ┌──────────────────┐  ┌──────────────────┐                │
│  │ Drowsiness Model │  │ Distraction Model│                │
│  │  (Rule-based +   │  │  (Head Pose)     │                │
│  │   Threshold)     │  │                  │                │
│  └──────┬───────────┘  └──────┬───────────┘                │
│         │                      │                             │
│  ┌──────┴──────────────────────┴───────┐                   │
│  │    Activity Recognition Model        │                   │
│  │    (CNN - MobileNetV2)               │                   │
│  │ • Calling, Drinking, Smoking, etc.   │                   │
│  └──────────────────┬───────────────────┘                   │
└───────────────────────────────────────────────────────────┘
                       │ Detection Results
                       ↓
┌──────────────────────────────────────────────────────────────┐
│                 BUSINESS LOGIC LAYER                          │
├──────────────────────────────────────────────────────────────┤
│  ┌───────────────────────────────────────┐                  │
│  │      Decision Engine & Rules          │                  │
│  │  • Severity Assessment                │                  │
│  │  • Alert Thresholding                 │                  │
│  │  • Temporal Smoothing                 │                  │
│  │  • False Positive Filtering           │                  │
│  └──────────────────┬────────────────────┘                  │
└───────────────────────────────────────────────────────────┘
                       │ Decisions
                       ↓
┌──────────────────────────────────────────────────────────────┐
│                    OUTPUT LAYER                               │
├──────────────────────────────────────────────────────────────┤
│  ┌────────────────┐  ┌─────────────────┐  ┌──────────────┐ │
│  │  Alert System  │  │   Data Layer    │  │  UI Layer    │ │
│  │                │  │                 │  │              │ │
│  │ • Audio Alert  │  │ • Event Logging │  │ • Dashboard  │ │
│  │ • Visual Alert │  │ • Database      │  │ • Live Feed  │ │
│  │ • LED/Haptic   │  │ • Snapshots     │  │ • Status     │ │
│  └────────────────┘  └─────────────────┘  └──────────────┘ │
└──────────────────────────────────────────────────────────────┘
```

#### **5.2. Component Architecture (Detailed)**

```
PROJECT STRUCTURE:

driver_monitoring/
│
├── main.py                      # Entry point
│
├── config/
│   ├── config.yaml              # Configuration file
│   └── constants.py             # Constants and thresholds
│
├── src/
│   │
│   ├── core/                    # Core functionality
│   │   ├── __init__.py
│   │   ├── camera.py            # Camera capture & preprocessing
│   │   ├── face_detector.py    # Face detection & tracking
│   │   ├── eye_tracker.py      # Eye detection & EAR calculation
│   │   ├── head_pose.py        # Head pose estimation
│   │   └── monitor.py          # Main monitoring orchestration
│   │
│   ├── ml/                      # Machine Learning
│   │   ├── __init__.py
│   │   ├── models/
│   │   │   ├── drowsiness_model.pkl
│   │   │   └── activity_model.h5
│   │   ├── inference.py        # Model inference
│   │   ├── preprocessor.py     # Data preprocessing for ML
│   │   └── trainer.py          # Model training (if custom)
│   │
│   ├── detectors/               # Detection modules
│   │   ├── __init__.py
│   │   ├── drowsiness.py       # Drowsiness detection logic
│   │   ├── distraction.py      # Distraction detection logic
│   │   └── activity.py         # Activity recognition logic
│   │
│   ├── decision/                # Business logic
│   │   ├── __init__.py
│   │   ├── rules_engine.py     # Decision rules
│   │   ├── severity.py         # Severity assessment
│   │   └── temporal.py         # Temporal smoothing
│   │
│   ├── alerts/                  # Alert system
│   │   ├── __init__.py
│   │   ├── audio_alert.py      # Audio warnings
│   │   ├── visual_alert.py     # Visual warnings
│   │   └── alert_manager.py    # Alert queue & management
│   │
│   ├── data/                    # Data layer
│   │   ├── __init__.py
│   │   ├── database.py         # Database operations
│   │   ├── models.py           # ORM models (SQLAlchemy)
│   │   └── logger.py           # Event logging
│   │
│   ├── ui/                      # User interface
│   │   ├── __init__.py
│   │   ├── dashboard.py        # Main dashboard UI
│   │   ├── widgets.py          # UI widgets
│   │   └── renderer.py         # Frame rendering
│   │
│   └── utils/                   # Utilities
│       ├── __init__.py
│       ├── config_loader.py    # Config file loader
│       ├── timer.py            # Performance timing
│       └── helpers.py          # Helper functions
│
├── tests/                       # Unit & integration tests
│   ├── test_camera.py
│   ├── test_face_detector.py
│   ├── test_drowsiness.py
│   └── ...
│
├── data/                        # Data storage
│   ├── models/                 # Trained models
│   ├── datasets/               # Training data
│   ├── logs/                   # Log files
│   └── snapshots/              # Event snapshots
│
├── docs/                        # Documentation
│   ├── architecture.md
│   ├── api.md
│   └── user_manual.md
│
├── requirements.txt             # Python dependencies
├── README.md                    # Project README
└── .gitignore                   # Git ignore file
```

#### **5.3. Technology Stack**

```yaml
Hardware:
  Camera: IR Camera (850nm, 30 FPS, USB 3.0)
  Computer: Raspberry Pi 4 (4GB RAM) / Jetson Nano
  Storage: 64GB microSD card
  Audio: USB Speaker / 3.5mm audio out
  Optional: LED indicators, haptic feedback

Software Stack:

  Language:
    - Python 3.8+
    
  Computer Vision:
    - OpenCV 4.5+ (cv2)
    - dlib 19.22+ (facial landmarks)
    
  Deep Learning:
    - TensorFlow 2.8+ / PyTorch 1.10+
    - TensorFlow Lite (for edge deployment)
    - Pre-trained: MobileNetV2, ResNet50
    
  Face Detection:
    - MTCNN (Multi-task CNN)
    - Haar Cascade (backup, faster)
    - dlib HOG face detector
    
  Database:
    - SQLite (simple, embedded)
    - PostgreSQL (if scalable needed)
    - SQLAlchemy (ORM)
    
  UI Framework:
    - Option 1: Tkinter (simple GUI)
    - Option 2: PyQt5 (advanced GUI)
    - Option 3: Flask + HTML/CSS/JS (web-based)
    
  Audio:
    - pygame (audio playback)
    - pydub (audio processing)
    
  Utilities:
    - NumPy (numerical computing)
    - SciPy (scientific computing)
    - Matplotlib (visualization)
    - Pillow (image processing)
    
  Testing:
    - pytest (unit testing)
    - unittest (standard library)
    
  Version Control:
    - Git
    - GitHub (repository hosting)
    
  Documentation:
    - Sphinx (API documentation)
    - Markdown (README, docs)
    
  Deployment:
    - Docker (containerization)
    - systemd (auto-start service)
```

#### **5.4. Design Patterns Used**

```python
1. SINGLETON PATTERN
   Usage: Camera, Database connection
   
   class CameraCapture:
       _instance = None
       
       def __new__(cls):
           if cls._instance is None:
               cls._instance = super().__new__(cls)
           return cls._instance

2. OBSERVER PATTERN
   Usage: Alert system (notify multiple alert handlers)
   
   class AlertManager:
       def __init__(self):
           self._observers = []
       
       def attach(self, observer):
           self._observers.append(observer)
       
       def notify(self, event):
           for observer in self._observers:
               observer.update(event)

3. STRATEGY PATTERN
   Usage: Different detection algorithms
   
   class DetectionStrategy(ABC):
       @abstractmethod
       def detect(self, frame):
           pass
   
   class DrowsinessDetector(DetectionStrategy):
       def detect(self, frame):
           # EAR-based detection
           pass
   
   class DistractionDetector(DetectionStrategy):
       def detect(self, frame):
           # Head pose-based detection
           pass

4. FACTORY PATTERN
   Usage: Model initialization
   
   class ModelFactory:
       @staticmethod
       def create_model(model_type):
           if model_type == "activity":
               return ActivityRecognitionModel()
           elif model_type == "drowsiness":
               return DrowsinessModel()

5. PIPELINE PATTERN
   Usage: Frame processing pipeline
   
   class ProcessingPipeline:
       def __init__(self):
           self.stages = []
       
       def add_stage(self, stage):
           self.stages.append(stage)
       
       def process(self, data):
           for stage in self.stages:
               data = stage.process(data)
           return data
```

#### **5.5. Data Flow Diagram**

```
┌─────────┐
│ Camera  │
└────┬────┘
     │ Raw Frame (BGR, 640x480, 30 FPS)
     ↓
┌─────────────────┐
│ Preprocessing   │
│ • Resize        │
│ • Color convert │
│ • Normalize     │
└────┬────────────┘
     │ Preprocessed Frame
     ↓
┌─────────────────┐
│ Face Detection  │
│ • MTCNN/Haar    │
│ • Bbox coords   │
└────┬────────────┘
     │ Face ROI + Bbox
     ↓
┌─────────────────┐
│ Landmark Detect │
│ • dlib 68-point │
│ • Eye points    │
│ • Mouth points  │
└────┬────────────┘
     │ Landmarks (68 x 2D points)
     ↓
┌──────────────────────────────┐
│ Feature Extraction           │
│ • EAR (eyes)                 │
│ • MAR (mouth)                │
│ • Head pose (3D)             │
└────┬─────────────────────────┘
     │ Features (EAR, MAR, pose)
     ↓
┌──────────────────────────────┐
│ Detection Algorithms         │
│                              │
│ ┌──────────────────────────┐│
│ │ Drowsiness Detection     ││
│ │ IF EAR < 0.25 for 2s     ││
│ │ → Drowsy                 ││
│ └──────────────────────────┘│
│                              │
│ ┌──────────────────────────┐│
│ │ Distraction Detection    ││
│ │ IF yaw > 30° for 2s      ││
│ │ → Distracted             ││
│ └──────────────────────────┘│
│                              │
│ ┌──────────────────────────┐│
│ │ Activity Recognition     ││
│ │ CNN inference            ││
│ │ → Activity class         ││
│ └──────────────────────────┘│
└────┬─────────────────────────┘
     │ Detection Results
     │ {type, confidence, severity}
     ↓
┌──────────────────────────────┐
│ Decision Engine              │
│ • Aggregate results          │
│ • Apply thresholds           │
│ • Temporal smoothing         │
│ • Severity assessment        │
└────┬─────────────────────────┘
     │ Alert Decision
     ↓
┌────────────────┬─────────────┬──────────────┐
│                │             │              │
↓                ↓             ↓              ↓
┌───────────┐  ┌─────────┐  ┌───────────┐  ┌─────────┐
│ Audio     │  │ Visual  │  │ Database  │  │   UI    │
│ Alert     │  │ Alert   │  │ Logging   │  │ Update  │
└───────────┘  └─────────┘  └───────────┘  └─────────┘
```

#### **5.6. Deployment Architecture**

```
DEVELOPMENT ENVIRONMENT:
┌────────────────────────────────┐
│  Development Laptop            │
│  • Ubuntu 20.04 / Windows 10   │
│  • Python 3.8+                 │
│  • CUDA + cuDNN (if GPU)       │
│  • IDE: VS Code / PyCharm      │
│  • USB Webcam (testing)        │
└────────────────────────────────┘

PRODUCTION ENVIRONMENT (Option 1 - Raspberry Pi):
┌────────────────────────────────┐
│  Raspberry Pi 4 (4GB RAM)      │
│  • Raspberry Pi OS (64-bit)    │
│  • Python 3.9                  │
│  • OpenCV (compiled)           │
│  • TensorFlow Lite             │
│  • IR Camera (USB 3.0)         │
│  • Audio output (3.5mm)        │
│  • Display (HDMI, optional)    │
└────────────────────────────────┘

PRODUCTION ENVIRONMENT (Option 2 - Jetson Nano):
┌────────────────────────────────┐
│  NVIDIA Jetson Nano (4GB)      │
│  • JetPack SDK                 │
│  • Python 3.8                  │
│  • OpenCV with CUDA            │
│  • TensorFlow GPU              │
│  • IR Camera (USB 3.0)         │
│  • Better performance (GPU)    │
└────────────────────────────────┘

DEPLOYMENT DIAGRAM:
┌─────────────────────────────────────────┐
│  Vehicle (In-cabin)                     │
│                                         │
│  ┌─────────────┐                       │
│  │ IR Camera   │                       │
│  │ (Dashboard  │                       │
│  │  mounted)   │                       │
│  └──────┬──────┘                       │
│         │ USB                           │
│         ↓                               │
│  ┌─────────────────────────────┐      │
│  │  Raspberry Pi 4 / Jetson    │      │
│  │                             │      │
│  │  ┌─────────────────────┐   │      │
│  │  │ Driver Monitoring   │   │      │
│  │  │ System (Python)     │   │      │
│  │  └─────────────────────┘   │      │
│  │                             │      │
│  │  ┌─────────────────────┐   │      │
│  │  │ SQLite Database     │   │      │
│  │  └─────────────────────┘   │      │
│  └──┬──────────────────┬───────┘      │
│     │ Audio            │ HDMI          │
│     ↓                  ↓               │
│  ┌────────┐      ┌──────────┐        │
│  │ Speaker│      │ Display  │        │
│  │ (Alert)│      │ (Status) │        │
│  └────────┘      └──────────┘        │
│                                        │
│  Optional:                             │
│  • 12V Power adapter (vehicle)        │
│  • 4G Modem (remote monitoring)       │
│  • GPS Module (location tracking)     │
└─────────────────────────────────────────┘
```

#### **5.7. Performance Considerations**

```yaml
Performance Requirements:
  Frame Rate: ≥15 FPS (target 20-25 FPS)
  Alert Latency: <100ms from detection
  CPU Usage: <70% (leave headroom)
  Memory: <1GB RAM
  Startup Time: <10 seconds

Optimization Strategies:

  1. Model Optimization:
     - Use MobileNetV2 (not ResNet) for activity recognition
     - Use TensorFlow Lite for inference
     - Quantize models (INT8) for edge devices
     - Prune unnecessary layers
     
  2. Frame Processing:
     - Reduce frame size (640x480 max)
     - Skip frames (process every 2nd or 3rd frame)
     - Use face tracking instead of detection every frame
     - Implement multi-threading:
       - Thread 1: Camera capture
       - Thread 2: Detection processing
       - Thread 3: UI rendering
       
  3. Algorithm Optimization:
     - Use Haar Cascade (fast) for initial detection
     - Switch to dlib only when face found
     - Cache facial landmarks for temporal smoothing
     - Batch inference if possible
     
  4. Memory Management:
     - Limit frame buffer size
     - Delete old snapshots regularly
     - Use generators instead of loading all data
     
  5. Hardware Acceleration:
     - Use OpenCV with CUDA (if GPU available)
     - Enable hardware decoding for video
     - Use NEON instructions (ARM)
```

#### **5.8. Security & Privacy Considerations**

```yaml
Privacy Concerns:
  - System captures driver's face continuously
  - Face embeddings stored for authentication
  - Event snapshots may contain PII

Security Measures:

  1. Data Encryption:
     - Encrypt face embeddings at rest
     - Encrypt database (SQLCipher)
     - Secure communication (HTTPS if networked)
     
  2. Data Minimization:
     - Don't store raw images (only embeddings)
     - Limit snapshot retention (7 days)
     - Only log essential event data
     
  3. Access Control:
     - Password-protect admin functions
     - Role-based access (admin vs driver)
     - Audit log for data access
     
  4. Compliance:
     - GDPR considerations (if EU)
     - Inform drivers about monitoring
     - Provide opt-out for non-safety features
     - Data retention policy documented

  5. Secure Deployment:
     - Disable SSH if not needed
     - Firewall rules (iptables)
     - Regular security updates
     - Secure boot (if supported)
```

#### **5.9. Scalability & Future Enhancements**

```yaml
Current Scope: Single vehicle, standalone system

Future Enhancements:

  1. Fleet Management:
     - Cloud backend (AWS/Azure/GCP)
     - Multi-vehicle dashboard
     - Real-time alerts to manager
     - Historical analytics across fleet
     
  2. Advanced Features:
     - Driver behavior scoring
     - Predictive fatigue detection
     - Route-based risk assessment
     - Integration with vehicle CAN bus
     
  3. Mobile App:
     - Driver self-monitoring
     - Trip summaries
     - Gamification (safe driving scores)
     
  4. Cloud ML:
     - Continuous model improvement
     - Federated learning across fleet
     - Personalized thresholds per driver
```

**Tools:**
- Draw.io, Lucidchart (architecture diagrams)
- PlantUML (UML diagrams)
- C4 Model (context, container, component, code)
- Mermaid (markdown diagrams)

**BMAD Support:** ❌ Không có workflow trực tiếp, có thể brainstorm architecture decisions

**Thứ tự thực hiện:** Tuần 4 (SAU Product Backlog & User Stories)

---

<a name="6-database-design"></a>
### **6. DATABASE DESIGN (Thiết kế Cơ sở Dữ liệu)** 🗄️

**Mục đích:** Thiết kế schema database để lưu trữ data

**Nội dung cần có:**

#### **6.1. Entity Relationship Diagram (ERD)**

```
┌─────────────────────────────────────────────────────────────┐
│                     ENTITY RELATIONSHIP DIAGRAM              │
└─────────────────────────────────────────────────────────────┘

┌──────────────────┐
│     drivers      │
├──────────────────┤
│ PK driver_id     │
│    name          │
│    phone         │
│    email         │
│    face_embedding│ (BLOB - 128D vector)
│    enrolled_at   │
│    status        │ (active/inactive)
│    notes         │
└────────┬─────────┘
         │ 1
         │
         │ has many
         │
         │ N
┌────────┴─────────────┐
│ monitoring_sessions  │
├──────────────────────┤
│ PK session_id        │
│ FK driver_id         │
│    start_time        │
│    end_time          │
│    duration          │
│    avg_alertness     │
│    total_events      │
│    critical_events   │
│    video_file_path   │ (optional)
│    notes             │
└────────┬─────────────┘
         │ 1
         │
         │ has many
         │
         │ N
┌────────┴─────────────┐
│   detection_events   │
├──────────────────────┤
│ PK event_id          │
│ FK session_id        │
│    event_type        │ (drowsiness/distraction/activity)
│    event_subtype     │ (calling/drinking/smoking/etc)
│    timestamp         │
│    duration          │
│    severity          │ (low/medium/high/critical)
│    confidence_score  │
│    ear_value         │ (if drowsiness)
│    head_pose_yaw     │ (if distraction)
│    head_pose_pitch   │
│    head_pose_roll    │
│    snapshot_path     │
│    resolved          │ (boolean)
│    resolved_at       │
│    notes             │
└────────┬─────────────┘
         │ 1
         │
         │ triggers
         │
         │ 1
┌────────┴─────────────┐
│      warnings        │
├──────────────────────┤
│ PK warning_id        │
│ FK event_id          │
│    warning_type      │ (audio/visual/haptic)
│    triggered_at      │
│    acknowledged_at   │
│    acknowledged_by   │
│    alert_sound       │
│    alert_message     │
└──────────────────────┘


┌──────────────────┐
│   system_logs    │
├──────────────────┤
│ PK log_id        │
│    log_level     │ (info/warning/error/critical)
│    component     │ (camera/detector/alert/etc)
│    message       │
│    stack_trace   │ (if error)
│    timestamp     │
└──────────────────┘


┌──────────────────┐
│ system_health    │
├──────────────────┤
│ PK health_id     │
│    timestamp     │
│    cpu_usage     │
│    memory_usage  │
│    fps           │
│    camera_status │
│    disk_space    │
│    temperature   │
└──────────────────┘


┌──────────────────┐
│ configurations   │
├──────────────────┤
│ PK config_key    │
│    config_value  │
│    data_type     │
│    description   │
│    updated_at    │
│    updated_by    │
└──────────────────┘
```

#### **6.2. Database Schema (SQLite)**

```sql
-- ========================================
-- DRIVER MONITORING SYSTEM - DATABASE SCHEMA
-- ========================================

-- Drivers table: Store enrolled drivers
CREATE TABLE drivers (
    driver_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT,
    email TEXT,
    face_embedding BLOB NOT NULL,  -- 128D vector (512 bytes)
    enrolled_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status TEXT DEFAULT 'active' CHECK(status IN ('active', 'inactive')),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Index for faster lookups
CREATE INDEX idx_drivers_name ON drivers(name);
CREATE INDEX idx_drivers_status ON drivers(status);

-- ========================================

-- Monitoring sessions: Each driving session
CREATE TABLE monitoring_sessions (
    session_id INTEGER PRIMARY KEY AUTOINCREMENT,
    driver_id INTEGER,
    start_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    end_time TIMESTAMP,
    duration INTEGER,  -- in seconds
    avg_alertness REAL,  -- 0.0-1.0 score
    total_events INTEGER DEFAULT 0,
    critical_events INTEGER DEFAULT 0,
    video_file_path TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (driver_id) REFERENCES drivers(driver_id) ON DELETE SET NULL
);

-- Indexes
CREATE INDEX idx_sessions_driver ON monitoring_sessions(driver_id);
CREATE INDEX idx_sessions_start ON monitoring_sessions(start_time);

-- ========================================

-- Detection events: All detected events
CREATE TABLE detection_events (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id INTEGER NOT NULL,
    event_type TEXT NOT NULL CHECK(event_type IN ('drowsiness', 'distraction', 'activity', 'authentication', 'system')),
    event_subtype TEXT,  -- calling, drinking, smoking, yawning, etc.
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    duration REAL,  -- event duration in seconds
    severity TEXT CHECK(severity IN ('low', 'medium', 'high', 'critical')),
    confidence_score REAL CHECK(confidence_score >= 0 AND confidence_score <= 1),
    
    -- Drowsiness-specific fields
    ear_value REAL,  -- Eye Aspect Ratio
    mar_value REAL,  -- Mouth Aspect Ratio (yawning)
    blink_frequency REAL,
    
    -- Distraction-specific fields
    head_pose_yaw REAL,
    head_pose_pitch REAL,
    head_pose_roll REAL,
    gaze_direction TEXT,  -- road, left_mirror, right_mirror, phone, passenger
    
    -- Activity-specific fields
    activity_class TEXT,  -- calling, drinking, smoking, hands_off_wheel
    
    -- Common fields
    snapshot_path TEXT,
    resolved BOOLEAN DEFAULT 0,
    resolved_at TIMESTAMP,
    notes TEXT,
    
    FOREIGN KEY (session_id) REFERENCES monitoring_sessions(session_id) ON DELETE CASCADE
);

-- Indexes
CREATE INDEX idx_events_session ON detection_events(session_id);
CREATE INDEX idx_events_type ON detection_events(event_type);
CREATE INDEX idx_events_severity ON detection_events(severity);
CREATE INDEX idx_events_timestamp ON detection_events(timestamp);

-- ========================================

-- Warnings: Alerts triggered by events
CREATE TABLE warnings (
    warning_id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id INTEGER NOT NULL,
    warning_type TEXT NOT NULL CHECK(warning_type IN ('audio', 'visual', 'haptic', 'combined')),
    triggered_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    acknowledged_at TIMESTAMP,
    acknowledged_by TEXT,  -- 'driver' or 'system'
    alert_sound TEXT,
    alert_message TEXT,
    FOREIGN KEY (event_id) REFERENCES detection_events(event_id) ON DELETE CASCADE
);

-- Indexes
CREATE INDEX idx_warnings_event ON warnings(event_id);
CREATE INDEX idx_warnings_triggered ON warnings(triggered_at);

-- ========================================

-- System logs: Application logs
CREATE TABLE system_logs (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    log_level TEXT NOT NULL CHECK(log_level IN ('debug', 'info', 'warning', 'error', 'critical')),
    component TEXT NOT NULL,  -- camera, face_detector, drowsiness_detector, etc.
    message TEXT NOT NULL,
    stack_trace TEXT,
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Indexes
CREATE INDEX idx_logs_level ON system_logs(log_level);
CREATE INDEX idx_logs_component ON system_logs(component);
CREATE INDEX idx_logs_timestamp ON system_logs(timestamp);

-- ========================================

-- System health: Performance metrics
CREATE TABLE system_health (
    health_id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    cpu_usage REAL,  -- percentage
    memory_usage REAL,  -- percentage
    disk_space REAL,  -- GB free
    fps REAL,  -- frames per second
    camera_status TEXT CHECK(camera_status IN ('ok', 'warning', 'error')),
    temperature REAL  -- celsius (for Raspberry Pi)
);

-- Index
CREATE INDEX idx_health_timestamp ON system_health(timestamp);

-- ========================================

-- Configurations: System settings
CREATE TABLE configurations (
    config_key TEXT PRIMARY KEY,
    config_value TEXT NOT NULL,
    data_type TEXT CHECK(data_type IN ('string', 'int', 'float', 'boolean', 'json')),
    description TEXT,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_by TEXT
);

-- Insert default configurations
INSERT INTO configurations (config_key, config_value, data_type, description) VALUES
('ear_threshold', '0.25', 'float', 'Eye Aspect Ratio threshold for drowsiness'),
('drowsiness_duration', '2.0', 'float', 'Seconds of closed eyes to trigger alert'),
('distraction_angle', '30.0', 'float', 'Head yaw angle (degrees) for distraction'),
('distraction_duration', '2.0', 'float', 'Seconds of distraction to trigger alert'),
('alert_volume', '0.8', 'float', 'Alert sound volume (0.0-1.0)'),
('fps_target', '20', 'int', 'Target frames per second'),
('snapshot_enabled', 'true', 'boolean', 'Save snapshots on events'),
('snapshot_retention_days', '7', 'int', 'Days to keep snapshots');

-- ========================================

-- Triggers: Automatically update timestamps

CREATE TRIGGER update_driver_timestamp 
AFTER UPDATE ON drivers
FOR EACH ROW
BEGIN
    UPDATE drivers SET updated_at = CURRENT_TIMESTAMP WHERE driver_id = NEW.driver_id;
END;

CREATE TRIGGER update_config_timestamp 
AFTER UPDATE ON configurations
FOR EACH ROW
BEGIN
    UPDATE configurations SET updated_at = CURRENT_TIMESTAMP WHERE config_key = NEW.config_key;
END;

-- Trigger: Auto-update session stats when events added
CREATE TRIGGER update_session_stats
AFTER INSERT ON detection_events
FOR EACH ROW
BEGIN
    UPDATE monitoring_sessions
    SET total_events = total_events + 1,
        critical_events = critical_events + CASE WHEN NEW.severity = 'critical' THEN 1 ELSE 0 END
    WHERE session_id = NEW.session_id;
END;

-- ========================================
```

#### **6.3. Sample Data & Queries**

```sql
-- ========================================
-- SAMPLE DATA
-- ========================================

-- Insert sample driver
INSERT INTO drivers (name, phone, email, face_embedding, status) VALUES
('John Doe', '+84 123456789', 'john@example.com', randomblob(512), 'active');

-- Insert sample session
INSERT INTO monitoring_sessions (driver_id, start_time) VALUES
(1, '2026-03-03 08:00:00');

-- Insert sample drowsiness event
INSERT INTO detection_events (
    session_id, event_type, event_subtype, severity, confidence_score,
    ear_value, snapshot_path
) VALUES (
    1, 'drowsiness', 'eye_closure', 'high', 0.92,
    0.18, '/data/snapshots/event_001.jpg'
);

-- Insert corresponding warning
INSERT INTO warnings (event_id, warning_type, alert_message) VALUES
(1, 'combined', 'DROWSINESS DETECTED! Please take a break.');

-- ========================================
-- USEFUL QUERIES
-- ========================================

-- 1. Get all events for a specific session
SELECT 
    e.event_id,
    e.event_type,
    e.event_subtype,
    e.severity,
    e.timestamp,
    e.confidence_score
FROM detection_events e
WHERE e.session_id = 1
ORDER BY e.timestamp DESC;

-- 2. Count events by type and severity
SELECT 
    event_type,
    severity,
    COUNT(*) as count
FROM detection_events
WHERE session_id = 1
GROUP BY event_type, severity;

-- 3. Get high severity events for a driver
SELECT 
    d.name as driver_name,
    e.event_type,
    e.event_subtype,
    e.timestamp,
    e.severity
FROM detection_events e
JOIN monitoring_sessions s ON e.session_id = s.session_id
JOIN drivers d ON s.driver_id = d.driver_id
WHERE d.driver_id = 1 
  AND e.severity IN ('high', 'critical')
ORDER BY e.timestamp DESC
LIMIT 10;

-- 4. Calculate average alertness per driver
SELECT 
    d.driver_id,
    d.name,
    COUNT(s.session_id) as total_sessions,
    AVG(s.avg_alertness) as avg_alertness_score,
    SUM(s.total_events) as total_events,
    SUM(s.critical_events) as critical_events
FROM drivers d
LEFT JOIN monitoring_sessions s ON d.driver_id = s.driver_id
GROUP BY d.driver_id, d.name;

-- 5. Get events in last 24 hours
SELECT 
    event_type,
    event_subtype,
    severity,
    timestamp
FROM detection_events
WHERE timestamp >= datetime('now', '-1 day')
ORDER BY timestamp DESC;

-- 6. Find sessions with most critical events
SELECT 
    s.session_id,
    d.name as driver_name,
    s.start_time,
    s.duration,
    s.critical_events
FROM monitoring_sessions s
JOIN drivers d ON s.driver_id = d.driver_id
WHERE s.critical_events > 0
ORDER BY s.critical_events DESC
LIMIT 10;

-- 7. Get average response time to warnings
SELECT 
    AVG(JULIANDAY(w.acknowledged_at) - JULIANDAY(w.triggered_at)) * 86400 as avg_response_seconds
FROM warnings w
WHERE w.acknowledged_at IS NOT NULL;

-- 8. System health over last hour
SELECT 
    timestamp,
    cpu_usage,
    memory_usage,
    fps,
    camera_status
FROM system_health
WHERE timestamp >= datetime('now', '-1 hour')
ORDER BY timestamp DESC;

-- 9. Most frequent event types
SELECT 
    event_type,
    event_subtype,
    COUNT(*) as frequency,
    AVG(confidence_score) as avg_confidence
FROM detection_events
GROUP BY event_type, event_subtype
ORDER BY frequency DESC;

-- 10. Driver risk scoring
SELECT 
    d.driver_id,
    d.name,
    COUNT(DISTINCT s.session_id) as total_sessions,
    SUM(CASE WHEN e.severity = 'critical' THEN 10 
             WHEN e.severity = 'high' THEN 5
             WHEN e.severity = 'medium' THEN 2
             ELSE 1 END) as risk_score
FROM drivers d
JOIN monitoring_sessions s ON d.driver_id = s.driver_id
LEFT JOIN detection_events e ON s.session_id = e.session_id
GROUP BY d.driver_id, d.name
ORDER BY risk_score DESC;
```

#### **6.4. Database Optimization**

```sql
-- ========================================
-- OPTIMIZATION STRATEGIES
-- ========================================

-- 1. Partitioning (for large datasets)
-- Create separate tables for old data
CREATE TABLE detection_events_archive AS 
SELECT * FROM detection_events 
WHERE timestamp < datetime('now', '-30 days');

DELETE FROM detection_events 
WHERE timestamp < datetime('now', '-30 days');

-- 2. Vacuum to reclaim space
VACUUM;

-- 3. Analyze for query optimization
ANALYZE;

-- 4. Additional useful indexes
CREATE INDEX idx_events_severity_timestamp ON detection_events(severity, timestamp);
CREATE INDEX idx_sessions_driver_start ON monitoring_sessions(driver_id, start_time);

-- 5. Materialized view for driver stats (manual refresh)
CREATE TABLE driver_stats AS
SELECT 
    d.driver_id,
    d.name,
    COUNT(DISTINCT s.session_id) as total_sessions,
    SUM(s.total_events) as total_events,
    SUM(s.critical_events) as critical_events,
    AVG(s.avg_alertness) as avg_alertness
FROM drivers d
LEFT JOIN monitoring_sessions s ON d.driver_id = s.driver_id
GROUP BY d.driver_id, d.name;

-- Refresh periodically (in application code)
-- DELETE FROM driver_stats; INSERT INTO driver_stats SELECT ...;
```

#### **6.5. Data Retention Policy**

```python
# Python code for data retention
import sqlite3
from datetime import datetime, timedelta

def cleanup_old_data(db_path, retention_days=30):
    """Remove data older than retention period."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cutoff_date = datetime.now() - timedelta(days=retention_days)
    
    # Archive old events
    cursor.execute('''
        INSERT INTO detection_events_archive
        SELECT * FROM detection_events
        WHERE timestamp < ?
    ''', (cutoff_date,))
    
    # Delete from main table
    cursor.execute('''
        DELETE FROM detection_events
        WHERE timestamp < ?
    ''', (cutoff_date,))
    
    # Delete old snapshots (in file system)
    cursor.execute('''
        SELECT snapshot_path FROM detection_events_archive
        WHERE snapshot_path IS NOT NULL
    ''')
    
    for (path,) in cursor.fetchall():
        try:
            os.remove(path)
        except:
            pass
    
    # Delete old logs
    cursor.execute('''
        DELETE FROM system_logs
        WHERE timestamp < ?
    ''', (cutoff_date,))
    
    conn.commit()
    conn.close()
    
    print(f"Cleaned up data older than {retention_days} days")
```

**Tools:**
- MySQL Workbench
- dbdiagram.io (online ERD)
- SQLite Browser
- DBeaver (universal DB tool)

**BMAD Support:** ❌ Không có workflow trực tiếp

**Thứ tự thực hiện:** Tuần 5 (SAU Architecture, CÙNG UI Design)

---

<a name="7-ui-interfaces"></a>
### **7. UI/INTERFACES (Giao diện Người dùng)** 🎨

**Nội dung chi tiết đã được mô tả ở phần trước (trong hướng dẫn tư vấn). Tham khảo phần "7. UI/INTERFACES" ở trên.**

**Thứ tự thực hiện:** Tuần 5 (SAU Product Backlog, CÙNG Database Design)

---

<a name="8-test-plan"></a>
### **8. TEST PLAN (Kế hoạch Kiểm thử)** 🧪

**Nội dung chi tiết đã được mô tả ở phần trước. Tham khảo phần "8. TEST PLAN" ở trên.**

**Thứ tự thực hiện:** Tuần 5-6 (Viết TRƯỚC khi coding - TDD approach)

---

<a name="9-test-cases"></a>
### **9. TEST CASES (Các Trường hợp Kiểm thử)** ✅

**Nội dung chi tiết đã được mô tả ở phần trước. Tham khảo phần "9. TEST CASES" ở trên.**

**Thứ tự thực hiện:** Tuần 6-10 (TRONG quá trình Development)

---

<a name="10-sprint-backlog"></a>
### **10. SPRINT BACKLOG** 🏃

**Nội dung chi tiết đã được mô tả ở phần trước. Tham khảo phần "10. SPRINT BACKLOG" ở trên.**

**Thứ tự thực hiện:** Tuần 4 (Tạo SAU Product Backlog), CẬP NHẬT mỗi sprint

---

<a name="11-code-standard"></a>
### **11. CODE STANDARD (Chuẩn Coding)** 💻

**Nội dung chi tiết đã được mô tả ở phần trước. Tham khảo phần "11. CODE STANDARD" ở trên.**

**Thứ tự thực hiện:** Tuần 2-3 (Định nghĩa TRƯỚC khi coding)

---

<a name="12-meeting-minutes"></a>
### **12. MEETING MINUTES (Biên bản Họp)** 📝

**Nội dung chi tiết đã được mô tả ở phần trước. Tham khảo phần "12. MEETING" ở trên.**

**Thứ tự thực hiện:** Throughout (Mỗi meeting, mỗi sprint)

---

<a name="13-reflection"></a>
### **13. REFLECTION (Đánh giá & Phản思)** 🤔

**Nội dung chi tiết đã được mô tả ở phần trước. Tham khảo phần "13. REFLECTION" ở trên.**

**Thứ tự thực hiện:** Tuần 12 (cuối dự án), nhưng ghi chú lessons learned throughout

---

<a name="timeline"></a>
## 🗓️ TIMELINE CHI TIẾT 12 TUẦN

```
═══════════════════════════════════════════════════════════════
WEEK 1: PROJECT INITIATION
═══════════════════════════════════════════════════════════════
Mon-Tue: Write Proposal
Wed-Thu: Start Project Plan, Research
Fri: Meeting with Advisor #1, Proposal approval

Deliverables: Proposal ✅

═══════════════════════════════════════════════════════════════
WEEK 2: PLANNING & SETUP
═══════════════════════════════════════════════════════════════
Mon-Tue: Complete Project Plan
Wed: Order hardware (IR camera, Raspberry Pi)
Thu-Fri: Setup development environment, Git repo

Deliverables: Project Plan ✅

═══════════════════════════════════════════════════════════════
WEEK 3: REQUIREMENTS (Sprint 1 Start)
═══════════════════════════════════════════════════════════════
Mon: Sprint 1 Planning Meeting
Tue-Thu: Product Backlog + User Stories (BRAINSTORMING!)
Fri: Architecture Design (start)

Deliverables: Product Backlog ✅, User Stories ✅ (partial)

Development Sprint 1: Camera Integration, Face Detection (start)

═══════════════════════════════════════════════════════════════
WEEK 4: DESIGN & DEVELOPMENT (Sprint 1 Continue)
═══════════════════════════════════════════════════════════════
Mon-Tue: Complete User Stories, Architecture Design
Wed: Database Design (start)
Thu-Fri: Development continues

Deliverables: User Stories ✅, Architecture ✅

Development Sprint 1: Face Detection, Eye Detection

Meeting with Advisor #2

═══════════════════════════════════════════════════════════════
WEEK 5: DESIGN & SPRINT 2 START
═══════════════════════════════════════════════════════════════
Mon: Sprint 1 Review & Retrospective
Tue: Sprint 2 Planning
Wed: Complete Database Design
Thu-Fri: UI Design, Test Plan (start)

Deliverables: Database Design ✅, UI Design ✅, Test Plan (partial)

Development Sprint 2: Drowsiness Detection, Alert System

═══════════════════════════════════════════════════════════════
WEEK 6: SPRINT 2 CONTINUE
═══════════════════════════════════════════════════════════════
Mon-Wed: Development (Drowsiness, Alerts, DB Integration)
Thu: Test Plan complete, Write Test Cases
Fri: Testing Sprint 2 features

Deliverables: Test Plan ✅, Test Cases ✅ (for completed features)

Development Sprint 2: Complete core detection features

Meeting with Advisor #3

═══════════════════════════════════════════════════════════════
WEEK 7: SPRINT 3 START - MID-TERM MILESTONE
═══════════════════════════════════════════════════════════════
Mon: Sprint 2 Review & Retrospective
Tue: Sprint 3 Planning
Wed-Fri: Development (Distraction Detection, Head Pose)

Milestone: MVP Demo to Advisor (Drowsiness detection working)

Development Sprint 3: Distraction Detection, Activity Recognition (start)

═══════════════════════════════════════════════════════════════
WEEK 8: SPRINT 3 CONTINUE
═══════════════════════════════════════════════════════════════
Mon-Thu: Development (Activity Recognition, Authentication)
Fri: Testing, Bug fixes

Development Sprint 3: Complete activity recognition features

Meeting with Advisor #4

═══════════════════════════════════════════════════════════════
WEEK 9: SPRINT 4 START - POLISH & OPTIMIZATION
═══════════════════════════════════════════════════════════════
Mon: Sprint 3 Review & Retrospective
Tue: Sprint 4 Planning
Wed-Fri: UI polish, Performance optimization

Development Sprint 4: UI enhancements, Performance tuning, Edge cases

═══════════════════════════════════════════════════════════════
WEEK 10: SPRINT 4 CONTINUE & TESTING
═══════════════════════════════════════════════════════════════
Mon-Tue: Complete Sprint 4 features
Wed-Fri: Integration testing, Bug fixes

Development Sprint 4: Final features complete

Meeting with Advisor #5

═══════════════════════════════════════════════════════════════
WEEK 11: SPRINT 5 - FINAL TESTING & BUG FIXES
═══════════════════════════════════════════════════════════════
Mon: Sprint 4 Review & Retrospective
Tue: Sprint 5 Planning (Testing & Polish)
Wed-Thu: Execute all test cases, Bug fixes
Fri: Performance testing, Final optimization

Development Sprint 5: Testing, bug fixes, documentation

═══════════════════════════════════════════════════════════════
WEEK 12: FINAL CLOSURE & SUBMISSION
═══════════════════════════════════════════════════════════════
Mon: Sprint 5 Review & Final Retrospective
Tue: Write Reflection document
Wed: Complete all documentation (README, User Manual)
Thu: Prepare presentation slides
Fri: Final submission, Practice defense

Deliverables: Reflection ✅, All documentation complete ✅

Final Meeting with Advisor #6: Thesis defense preparation

═══════════════════════════════════════════════════════════════
```

---

<a name="dependencies"></a>
## 🎯 DEPENDENCIES MAP - Thứ tự Phụ thuộc

```
Proposal
   ↓
Project Plan
   ↓
Product Backlog ← START HERE (Week 3)
   ↓
User Stories
   ↓
┌─────────────┬──────────────┬─────────────┐
↓             ↓              ↓             ↓
Architecture  Database      UI/UX      Test Plan
   ↓             ↓              ↓             ↓
   └─────────────┴──────────────┴─────────────┘
                      ↓
               Sprint Backlog
                      ↓
               Development (with Code Standard)
                      ↓
               Test Cases
                      ↓
               Testing
                      ↓
               Reflection

Throughout: Meeting minutes
```

---

<a name="tools"></a>
## 🛠️ TOOLS RECOMMENDATION

| Deliverable | Recommended Tool | Alternative | Free? |
|-------------|------------------|-------------|-------|
| Proposal | Google Docs | MS Word | ✅ |
| Project Plan | Trello + Sheets | MS Project | ✅ |
| Product Backlog | Google Sheets | Jira | ✅ |
| User Stories | Notion | Jira | ✅ |
| Architecture | Draw.io | Lucidchart | ✅ |
| Database Design | dbdiagram.io | MySQL Workbench | ✅ |
| UI Design | Figma | Adobe XD | ✅ |
| Test Plan | Google Docs | TestRail | ✅ |
| Test Cases | Excel | TestRail | ✅ |
| Sprint Backlog | Trello | Jira | ✅ |
| Code Standard | Markdown file | Confluence | ✅ |
| Meeting | Google Docs | Notion | ✅ |
| Reflection | Google Docs | MS Word | ✅ |
| Version Control | GitHub | GitLab | ✅ |
| Development | VS Code | PyCharm | ✅ |

---

<a name="tips"></a>
## 💡 TOP 10 TIPS CHO ĐỒ ÁN TỐT NGHIỆP

### **1. Bắt đầu sớm, đừng trì hoãn**
- Week 1 là quan trọng nhất
- Setup môi trường, order hardware ngay
- Đừng để deadline đến mới làm

### **2. Giao tiếp thường xuyên với giáo viên**
- Bi-weekly meetings minimum
- Email updates weekly
- Hỏi khi không chắc chắn
- Đừng ngại show progress (cả khi chưa hoàn hảo)

### **3. Document as you go**
- Đừng để tất cả documentation đến cuối
- Viết ngay sau khi làm xong
- Future you will thank present you
- Take screenshots, save examples

### **4. Use version control religiously**
- Git commit often (mỗi ngày)
- Clear commit messages
- Branch for each feature
- Push to remote regularly (backup!)

### **5. Test early, test often**
- Don't wait until the end
- Unit tests + Integration tests
- Automated testing saves time
- Test on actual hardware early

### **6. Manage scope carefully**
- Better few features done well
- Than many features done poorly
- MVP first, enhance later
- Don't add features last minute

### **7. Plan for the unexpected**
- Hardware delays (order early!)
- Technical roadblocks
- Health/personal issues
- Add buffer time (20% extra)

### **8. Learn from others**
- Read similar thesis projects
- GitHub repositories
- Research papers
- Stack Overflow, Reddit
- Don't reinvent the wheel

### **9. Take care of yourself**
- Don't burn out
- Regular breaks (Pomodoro)
- Sleep well (7-8 hours)
- Exercise, eat healthy
- Balance work and life

### **10. Backup everything**
- Code: GitHub (push daily)
- Documents: Google Drive + Local backup
- Data: External hard drive
- Models: Cloud storage
- Multiple backups!

---

## ✅ CHECKLIST TỔNG THỂ

```
PHASE 1: PLANNING (Week 1-2)
☐ Proposal written and approved
☐ Project Plan complete
☐ Hardware ordered
☐ Development environment setup
☐ Git repository created

PHASE 2: REQUIREMENTS & DESIGN (Week 3-5)
☐ Product Backlog complete
☐ User Stories written (all must-have features)
☐ Architecture designed and reviewed
☐ Database schema designed
☐ UI mockups created
☐ Test Plan written

PHASE 3: DEVELOPMENT (Week 6-10)
☐ Sprint 1: Camera + Face Detection ✓
☐ Sprint 2: Drowsiness Detection + Alerts ✓
☐ Sprint 3: Distraction + Activity Recognition ✓
☐ Sprint 4: Polish + Optimization ✓
☐ Code Standard enforced
☐ Test Cases executed
☐ Code reviewed

PHASE 4: TESTING & CLOSURE (Week 11-12)
☐ Sprint 5: Final testing complete
☐ All test cases passed (>90%)
☐ Bug fixes done
☐ Performance targets met
☐ Documentation complete
☐ Reflection written
☐ Presentation ready
☐ Final submission ✓

ONGOING:
☐ Meeting minutes after each meeting
☐ Weekly progress updates to advisor
☐ Git commits daily
☐ Backup code and docs
```

---

## 📞 SUPPORT & RESOURCES

**Official Documentation:**
- OpenCV: https://docs.opencv.org/
- dlib: http://dlib.net/
- TensorFlow: https://www.tensorflow.org/
- PyTorch: https://pytorch.org/

**Datasets:**
- CEW (Closed Eyes In The Wild): http://parnec.nuaa.edu.cn/xtan/data/ClosedEyeDatabases.html
- YawDD (Yawning Detection Dataset): https://www.kaggle.com/datasets/davidvazquezcic/yawn-dataset
- State Farm Distracted Driver: https://www.kaggle.com/c/state-farm-distracted-driver-detection

**GitHub Examples:**
- Driver Drowsiness Detection: Search "drowsiness detection" on GitHub
- Face Recognition: https://github.com/ageitgey/face_recognition

**Communities:**
- Stack Overflow
- Reddit: r/computervision, r/MachineLearning
- Raspberry Pi Forums

---

## 📝 FINAL NOTES

Tài liệu này là **hướng dẫn tổng thể** cho toàn bộ quy trình làm đồ án tốt nghiệp của bạn. Hãy:

✅ **Bookmark** tài liệu này  
✅ **Refer back** thường xuyên  
✅ **Update** khi có thay đổi  
✅ **Share** với advisor nếu cần  

**Good luck with your thesis! 🚀**

---

**Document Version:** 1.0  
**Created:** 2026-03-03  
**For:** Hung Thanh - Driver Monitoring System Thesis  
**Contact:** (Your email/phone)

═══════════════════════════════════════════════════════════════
END OF DOCUMENT
═══════════════════════════════════════════════════════════════
