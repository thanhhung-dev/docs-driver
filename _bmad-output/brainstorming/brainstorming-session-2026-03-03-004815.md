---
stepsCompleted: [1, 2, 3, 4]
inputDocuments: []
session_topic: 'Tạo Product Backlog và User Stories cho Driver Monitoring System (Đồ án Tốt nghiệp)'
session_goals: 'Tạo Product Backlog đầy đủ, viết User Stories chi tiết theo chuẩn Agile, xác định Acceptance Criteria rõ ràng, ưu tiên features, chuẩn bị cho Architecture và Database Design'
selected_approach: 'AI-Recommended Techniques'
techniques_used: ['Morphological Analysis', 'Role Playing', 'SCAMPER', 'Question Storming', 'MoSCoW']
ideas_generated: 195
context_file: ''
project_context: 'Đồ án tốt nghiệp - Deliverables: Proposal, Project Plan, Product Backlog, User Stories, Architecture, Database Design, UI/Interfaces, Test Plan, Test Cases, Sprint Backlog, Code Standard, Meeting, Reflection'
scope_decisions: 'Safety Belt: Removed | Authentication: TBD | Activities: 7 full | Gaze: Eye + Head | Facial Expression: Skip | Passenger Counting: Keep | Timeline: 10-20 weeks'
session_status: 'COMPLETE'
---

# Brainstorming Session Results

**Facilitator:** hung-thanh
**Date:** 2026-03-03

## Session Overview

**Topic:** Tạo Product Backlog và User Stories cho Driver Monitoring System (Đồ án Tốt nghiệp)

**Goals:** 
- Tạo Product Backlog đầy đủ với tất cả features được phân loại và ưu tiên
- Viết User Stories chi tiết theo format chuẩn Agile (As a... I want... So that...)
- Xác định Acceptance Criteria rõ ràng và có thể kiểm thử cho mỗi User Story
- Phân loại features theo MoSCoW (Must have, Should have, Could have, Won't have)
- Chuẩn bị nền tảng requirements cho Architecture và Database Design

### Session Setup

## Technique Selection

**Approach:** AI-Recommended Techniques
**Analysis Context:** Tạo Product Backlog và User Stories cho Driver Monitoring System (Đồ án Tốt nghiệp)

**Recommended Techniques Sequence (4 Phases):**

**Phase 1: Feature Discovery & Classification (30-40 min)**
- **Technique:** Morphological Analysis (Deep)
- **Purpose:** Lập bản đồ toàn bộ features của hệ thống với ma trận phân loại
- **Expected Outcome:** Product Backlog draft với tất cả features được nhận diện

**Phase 2: User Story Generation (35-45 min)**  
- **Technique:** Role Playing (Collaborative)
- **Purpose:** Tạo User Stories từ góc nhìn các stakeholder khác nhau
- **Expected Outcome:** User Stories theo format "As a... I want... So that..."

**Phase 3: Acceptance Criteria Definition (25-35 min)**
- **Technique:** SCAMPER Method (Structured)
- **Purpose:** Định nghĩa Acceptance Criteria rõ ràng cho mỗi User Story
- **Expected Outcome:** Acceptance Criteria cụ thể (Given-When-Then format)

**Phase 4: Prioritization & Refinement (20-30 min)**
- **Technique:** Question Storming + MoSCoW (Deep + Structured)
- **Purpose:** Ưu tiên features và phát hiện gaps
- **Expected Outcome:** Product Backlog hoàn chỉnh với MoSCoW prioritization

**AI Rationale:** Chuỗi 4 techniques này được chọn để có hệ thống từ khám phá features (Morphological), đến viết stories từ góc nhìn user (Role Playing), định nghĩa tiêu chí chấp nhận (SCAMPER), và cuối cùng ưu tiên hóa (Question Storming + MoSCoW). Phù hợp với mục tiêu tạo Product Backlog và User Stories đầy đủ cho đồ án tốt nghiệp.

---

## 🎯 Scope Clarification (Requirements Finalization)

**Scope Decisions Made:**
- ❌ **Safety Belt Detection**: REMOVED (not in scope)
- 🔄 **Authentication**: TO BE DECIDED later (startup vs continuous)
- ✅ **Dangerous Activities**: 7 FULL activities (calling, drinking, smoking, yawning, hands off wheel, arm out window, looking at directions)
- ✅ **Gaze Tracking**: Both Eye Gaze + Head Pose required
- ❌ **Facial Expression**: SKIP (low priority, high complexity)
- ✅ **Passenger Counting**: KEEP (in scope)
- ⏱️ **Timeline**: 10-20 weeks for development

---

## Phase 1: Morphological Analysis (Feature Discovery & Classification)

**Technique:** Morphological Analysis  
**Duration:** 40 minutes  
**Objective:** Systematically discover and classify ALL features using multi-dimensional matrix

### Morphological Matrix (4 Dimensions)

| Dimension | Options |
|-----------|---------|
| **1. Detection Type** | Face Detection, Eye Monitoring, Head Monitoring, Gaze Tracking, Drowsiness Detection, Distraction Detection, Activity Recognition, Passenger Counting, System Health, Driver Enrollment |
| **2. Monitored Entity** | Driver Only, Driver + Passengers, Camera/System |
| **3. Technology Layer** | Computer Vision (CV), Infrared (IR), AI/ML Models, Rule-based Logic, Hardware Integration |
| **4. Output/Action** | Real-time Alert, Logging/Recording, Dashboard Display, Analytics/Reports |

### Product Backlog Items (45 Features Identified)

#### **Category 1: Core Face & Eye Detection (Foundation)**

**PBI-001**: Face Detection & Tracking
- **Description**: Detect and track driver's face in real-time using IR camera
- **Tech**: CV (dlib/MediaPipe) + IR Camera
- **Entity**: Driver Only
- **Output**: Face bounding box, face landmarks (68 points)
- **MoSCoW**: MUST HAVE

**PBI-002**: Eye Region Detection
- **Description**: Detect left and right eye regions from face landmarks
- **Tech**: CV (dlib facial landmarks)
- **Entity**: Driver Only
- **Output**: Eye bounding boxes, eye landmarks
- **MoSCoW**: MUST HAVE

**PBI-003**: Eye Openness Detection
- **Description**: Calculate Eye Aspect Ratio (EAR) to determine if eyes are open/closed
- **Tech**: Rule-based (EAR calculation from eye landmarks)
- **Entity**: Driver Only
- **Output**: EAR values (left, right, average), open/closed state
- **MoSCoW**: MUST HAVE

**PBI-004**: Blink Frequency Monitoring
- **Description**: Count blinks per minute to detect abnormal patterns
- **Tech**: Rule-based (EAR threshold detection)
- **Entity**: Driver Only
- **Output**: Blinks per minute, blink duration average
- **MoSCoW**: MUST HAVE

**PBI-005**: Eye Location Tracking
- **Description**: Track eye position within face region for gaze estimation
- **Tech**: CV (pupil detection)
- **Entity**: Driver Only
- **Output**: Eye center coordinates (x, y)
- **MoSCoW**: MUST HAVE

---

#### **Category 2: Head Pose & Orientation**

**PBI-006**: Head Pose Estimation
- **Description**: Estimate head orientation (pitch, yaw, roll) from facial landmarks
- **Tech**: CV (solvePnP algorithm)
- **Entity**: Driver Only
- **Output**: Euler angles (pitch, yaw, roll in degrees)
- **MoSCoW**: MUST HAVE

**PBI-007**: Head Location Tracking
- **Description**: Track head position in camera frame (left, center, right, up, down)
- **Tech**: CV (face centroid tracking)
- **Entity**: Driver Only
- **Output**: Head position zone (9 zones: center, left, right, up, down, etc.)
- **MoSCoW**: MUST HAVE

**PBI-008**: Head Zone Classification
- **Description**: Classify head position into predefined zones (looking forward, looking left/right, looking down)
- **Tech**: Rule-based (head pose thresholds)
- **Entity**: Driver Only
- **Output**: Zone label (Forward, Left, Right, Down, Extreme angles)
- **MoSCoW**: MUST HAVE

---

#### **Category 3: Eye Gaze Tracking**

**PBI-009**: Gaze Direction Estimation
- **Description**: Estimate gaze direction vector from eye landmarks and pupil position
- **Tech**: CV (gaze estimation algorithms) + AI/ML
- **Entity**: Driver Only
- **Output**: Gaze vector (3D direction), gaze angles
- **MoSCoW**: MUST HAVE

**PBI-010**: Gaze Zone Classification
- **Description**: Map gaze direction to specific zones (road, dashboard, mirrors, phone, passenger)
- **Tech**: Rule-based (gaze angle to zone mapping)
- **Entity**: Driver Only
- **Output**: Gaze zone label, dwell time per zone
- **MoSCoW**: MUST HAVE

**PBI-011**: Pupil Detection & Tracking
- **Description**: Detect and track pupil position for precise gaze estimation
- **Tech**: CV (circular Hough transform or deep learning)
- **Entity**: Driver Only
- **Output**: Pupil center coordinates, pupil diameter
- **MoSCoW**: SHOULD HAVE

---

#### **Category 4: Drowsiness Detection**

**PBI-012**: Drowsiness Detection (EAR-based)
- **Description**: Detect drowsiness using prolonged low EAR values (eyes closing)
- **Tech**: Rule-based (EAR thresholding over time)
- **Entity**: Driver Only
- **Output**: Drowsiness level (normal, mild, severe), alert trigger
- **MoSCoW**: MUST HAVE

**PBI-013**: Yawning Detection
- **Description**: Detect yawning from mouth aspect ratio (MAR) and duration
- **Tech**: CV (mouth landmarks) + Rule-based
- **Entity**: Driver Only
- **Output**: Yawn detected (yes/no), yawn count per period
- **MoSCoW**: MUST HAVE

**PBI-014**: Microsleep Detection
- **Description**: Detect very brief eye closures (0.5-3 seconds) indicating microsleep
- **Tech**: Rule-based (EAR duration analysis)
- **Entity**: Driver Only
- **Output**: Microsleep event count, timestamps
- **MoSCoW**: MUST HAVE

**PBI-015**: PERCLOS Calculation
- **Description**: Calculate Percentage of Eye Closure (PERCLOS) over time window (standard drowsiness metric)
- **Tech**: Rule-based (EAR statistical analysis)
- **Entity**: Driver Only
- **Output**: PERCLOS value (%), drowsiness risk level
- **MoSCoW**: SHOULD HAVE

---

#### **Category 5: Distraction Detection**

**PBI-016**: Head Turn Distraction
- **Description**: Detect prolonged head turns away from road (based on head pose)
- **Tech**: Rule-based (yaw angle + duration thresholds)
- **Entity**: Driver Only
- **Output**: Distraction alert, head-off-road duration
- **MoSCoW**: MUST HAVE

**PBI-017**: Gaze-off-Road Detection
- **Description**: Detect when gaze is away from forward road zone for extended time
- **Tech**: Rule-based (gaze zone + duration)
- **Entity**: Driver Only
- **Output**: Gaze-off-road duration, alert trigger
- **MoSCoW**: MUST HAVE

**PBI-018**: Attention Score Calculation
- **Description**: Calculate overall attention score combining head pose, gaze, and eye openness
- **Tech**: Rule-based or ML (weighted scoring)
- **Entity**: Driver Only
- **Output**: Attention score (0-100), attention level (high/medium/low)
- **MoSCoW**: SHOULD HAVE

---

#### **Category 6: Dangerous Activity Recognition (7 Activities)**

**PBI-019**: Phone Calling Detection
- **Description**: Detect driver holding phone to ear during call
- **Tech**: AI/ML (Activity CNN - MobileNetV2 or similar)
- **Entity**: Driver Only
- **Output**: Activity label "calling", confidence score, alert
- **MoSCoW**: MUST HAVE

**PBI-020**: Drinking Detection
- **Description**: Detect driver drinking from bottle/cup while driving
- **Tech**: AI/ML (Activity CNN)
- **Entity**: Driver Only
- **Output**: Activity label "drinking", confidence score, alert
- **MoSCoW**: MUST HAVE

**PBI-021**: Smoking Detection
- **Description**: Detect driver smoking cigarette while driving
- **Tech**: AI/ML (Activity CNN)
- **Entity**: Driver Only
- **Output**: Activity label "smoking", confidence score, alert
- **MoSCoW**: MUST HAVE

**PBI-022**: Yawning Activity Detection
- **Description**: Detect yawning as dangerous activity (different from drowsiness yawn detection)
- **Tech**: AI/ML (Activity CNN) or CV (mouth landmarks)
- **Entity**: Driver Only
- **Output**: Activity label "yawning", count, alert
- **MoSCoW**: MUST HAVE

**PBI-023**: Hands Off Wheel Detection
- **Description**: Detect when driver's hands are not on steering wheel
- **Tech**: AI/ML (Hand detection + Activity CNN) or separate hand tracking
- **Entity**: Driver Only
- **Output**: Activity label "hands_off_wheel", duration, alert
- **MoSCoW**: MUST HAVE

**PBI-024**: Arm Out Window Detection
- **Description**: Detect driver's arm extended out of window
- **Tech**: AI/ML (Activity CNN + pose estimation)
- **Entity**: Driver Only
- **Output**: Activity label "arm_out_window", duration, alert
- **MoSCoW**: MUST HAVE

**PBI-025**: Looking at Directions Detection
- **Description**: Detect driver looking at phone/GPS for navigation (head down, gaze at device)
- **Tech**: AI/ML (Activity CNN) + Gaze zone analysis
- **Entity**: Driver Only
- **Output**: Activity label "looking_at_directions", duration, alert
- **MoSCoW**: MUST HAVE

**PBI-026**: Activity CNN Model Training
- **Description**: Train deep learning model for activity recognition (all 7 activities)
- **Tech**: AI/ML (MobileNetV2, EfficientNet, or custom CNN)
- **Entity**: System
- **Output**: Trained model (.h5 or .pth file), accuracy metrics
- **MoSCoW**: MUST HAVE

---

#### **Category 7: Driver Enrollment & Identification**

**PBI-027**: Driver Face Enrollment
- **Description**: Enroll new driver by capturing and storing facial features
- **Tech**: CV (face encoding - dlib/FaceNet)
- **Entity**: Driver Only
- **Output**: Face encoding vector (128D), driver ID, stored in database
- **MoSCoW**: SHOULD HAVE

**PBI-028**: Driver Identification
- **Description**: Identify enrolled driver when they enter vehicle (face recognition)
- **Tech**: CV (face encoding comparison - cosine similarity)
- **Entity**: Driver Only
- **Output**: Driver ID, confidence score, welcome message
- **MoSCoW**: SHOULD HAVE

**PBI-029**: Multi-Driver Management
- **Description**: Support multiple enrolled drivers per vehicle
- **Tech**: Database + face recognition
- **Entity**: Driver Only
- **Output**: Driver profile selection, session association
- **MoSCoW**: SHOULD HAVE

---

#### **Category 8: Passenger Monitoring**

**PBI-030**: Passenger Counting
- **Description**: Count number of passengers in vehicle (front + rear seats)
- **Tech**: CV (person detection - YOLO/SSD) or depth sensors
- **Entity**: Driver + Passengers
- **Output**: Passenger count (0-4 typically), seat occupancy map
- **MoSCoW**: SHOULD HAVE

**PBI-031**: Passenger Face Detection
- **Description**: Detect faces of passengers for occupancy verification
- **Tech**: CV (multi-face detection)
- **Entity**: Passengers
- **Output**: Face count, face locations (seat positions)
- **MoSCoW**: COULD HAVE

---

#### **Category 9: Safety Accessories (Glasses/Mask)**

**PBI-032**: Glasses Detection
- **Description**: Detect if driver is wearing glasses (affects eye detection algorithms)
- **Tech**: CV (classifier) or AI/ML
- **Entity**: Driver Only
- **Output**: Glasses status (yes/no), adjust EAR thresholds if needed
- **MoSCoW**: SHOULD HAVE

**PBI-033**: Mask Detection
- **Description**: Detect if driver is wearing face mask (affects face landmark detection)
- **Tech**: AI/ML (mask classifier)
- **Entity**: Driver Only
- **Output**: Mask status (yes/no), warning if mask interferes with detection
- **MoSCoW**: COULD HAVE

---

#### **Category 10: System Health & Camera Management**

**PBI-034**: IR Camera Health Check
- **Description**: Monitor camera connectivity and image quality
- **Tech**: Hardware integration + CV (frame validation)
- **Entity**: Camera/System
- **Output**: Camera status (online/offline), image quality metrics
- **MoSCoW**: MUST HAVE

**PBI-035**: Low Light Detection
- **Description**: Detect insufficient lighting conditions affecting detection accuracy
- **Tech**: CV (brightness histogram analysis)
- **Entity**: Camera/System
- **Output**: Lighting level (sufficient/insufficient), warning
- **MoSCoW**: SHOULD HAVE

**PBI-036**: Face Occlusion Detection
- **Description**: Detect when face is partially occluded (hand, object, position)
- **Tech**: CV (landmark confidence analysis)
- **Entity**: Driver Only
- **Output**: Occlusion status, occluded regions, warning
- **MoSCoW**: SHOULD HAVE

**PBI-037**: System FPS Monitoring
- **Description**: Monitor processing frame rate to ensure real-time performance
- **Tech**: System metrics
- **Entity**: System
- **Output**: FPS value, performance warnings if below threshold
- **MoSCoW**: SHOULD HAVE

---

#### **Category 11: Alert System**

**PBI-038**: Real-time Audio Alerts
- **Description**: Play audio warnings for critical events (drowsiness, distraction, dangerous activities)
- **Tech**: Audio output (beep sounds, voice alerts)
- **Entity**: System
- **Output**: Audio alert played, alert type logged
- **MoSCoW**: MUST HAVE

**PBI-039**: Visual Alerts (LED/Dashboard)
- **Description**: Display visual warnings on dashboard/LED indicators
- **Tech**: Hardware integration (LED, screen display)
- **Entity**: System
- **Output**: Visual alert shown, color-coded by severity
- **MoSCoW**: SHOULD HAVE

**PBI-040**: Alert Priority Management
- **Description**: Prioritize multiple simultaneous alerts (e.g., drowsiness > distraction)
- **Tech**: Rule-based (alert queue management)
- **Entity**: System
- **Output**: Prioritized alert sequence, prevent alert spam
- **MoSCoW**: SHOULD HAVE

---

#### **Category 12: Data Logging & Recording**

**PBI-041**: Event Logging
- **Description**: Log all detected events with timestamps (drowsiness, distraction, activities, alerts)
- **Tech**: Database (SQLite/PostgreSQL)
- **Entity**: System
- **Output**: Event records in database (event_type, timestamp, severity, metadata)
- **MoSCoW**: MUST HAVE

**PBI-042**: Video Recording (Event-triggered)
- **Description**: Record video clips when critical events occur (evidence, review)
- **Tech**: Video storage (MP4 encoding)
- **Entity**: System
- **Output**: Video files linked to events, stored with timestamps
- **MoSCoW**: SHOULD HAVE

**PBI-043**: Session Tracking
- **Description**: Track driving sessions (start/end time, driver ID, trip duration)
- **Tech**: Database
- **Entity**: System
- **Output**: Session records, trip summaries
- **MoSCoW**: SHOULD HAVE

---

#### **Category 13: Dashboard & User Interface**

**PBI-044**: Live Monitoring Dashboard
- **Description**: Real-time UI showing camera feed, detection overlays, current status
- **Tech**: GUI framework (OpenCV window, Qt, or web-based)
- **Entity**: System
- **Output**: Visual interface with face/eye/gaze overlays, status indicators
- **MoSCoW**: MUST HAVE

**PBI-045**: Historical Analytics Dashboard
- **Description**: View past trips, event statistics, driver behavior trends
- **Tech**: Web dashboard or desktop app
- **Entity**: System
- **Output**: Charts/graphs of events over time, driver safety scores
- **MoSCoW**: COULD HAVE

---

### Summary Statistics

**Total PBIs Identified:** 45 features  
**Categories:** 13 functional areas  
**MoSCoW Breakdown (Initial):**
- **MUST HAVE**: 23 items (core detection, activities, alerts, logging)
- **SHOULD HAVE**: 15 items (enrollment, passengers, accessories, system health)
- **COULD HAVE**: 7 items (advanced analytics, passenger details, mask detection)
- **WON'T HAVE**: Safety belt (removed per scope decision)

**Technology Stack Required:**
- Computer Vision: OpenCV, dlib, MediaPipe
- AI/ML Models: MobileNetV2 (Activity CNN), FaceNet (enrollment), custom models
- Hardware: IR Camera
- Database: SQLite/PostgreSQL
- Framework: Python (primary), possible web UI

---



## Phase 2: Role Playing (User Story Generation)

**Technique:** Role Playing  
**Duration:** 45 minutes  
**Objective:** Generate User Stories from different stakeholder perspectives using Agile format

### Stakeholder Roles Identified

1. **👨‍✈️ Driver (Tài xế)** - Primary end-user who drives the vehicle
2. **👔 Fleet Manager (Quản lý đội xe)** - Oversees multiple drivers and vehicles
3. **🛡️ Safety Engineer (Kỹ sư An toàn)** - Designs and improves safety features
4. **👨‍💻 Developer (Lập trình viên)** - Builds and maintains the system
5. **🧪 QA Tester (Kiểm thử viên)** - Tests and validates system functionality

---

### User Stories by Stakeholder

#### 👨‍✈️ **DRIVER (Tài xế) Perspective**

**US-001: Drowsiness Alert**
- **As a** driver
- **I want** to receive immediate audio alerts when the system detects I'm drowsy (eyes closing, yawning)
- **So that** I can take action to rest or stay alert before an accident occurs
- **Related PBIs**: PBI-012, PBI-013, PBI-014, PBI-038

**US-002: Distraction Warning**
- **As a** driver
- **I want** to be warned when I look away from the road for too long
- **So that** I can refocus my attention on driving safely
- **Related PBIs**: PBI-016, PBI-017, PBI-038

**US-003: Dangerous Activity Alert**
- **As a** driver
- **I want** to be notified when I'm performing dangerous activities (calling, drinking, smoking, etc.)
- **So that** I can stop the unsafe behavior immediately
- **Related PBIs**: PBI-019 to PBI-025, PBI-038

**US-004: Hands-Free Driving Warning**
- **As a** driver
- **I want** to be alerted when my hands are off the steering wheel for extended time
- **So that** I maintain proper vehicle control
- **Related PBIs**: PBI-023, PBI-038

**US-005: Real-time Feedback Display**
- **As a** driver
- **I want** to see my current attention level and detected states on the dashboard
- **So that** I can self-correct my driving behavior proactively
- **Related PBIs**: PBI-044, PBI-018

**US-006: Driver Identification**
- **As a** driver
- **I want** the system to recognize me when I enter the vehicle
- **So that** my personalized settings and history are loaded automatically
- **Related PBIs**: PBI-028, PBI-029

**US-007: Enrollment Process**
- **As a** new driver
- **I want** to easily enroll my face into the system
- **So that** the system can identify me in future trips
- **Related PBIs**: PBI-027, PBI-029

**US-008: Privacy Control**
- **As a** driver
- **I want** to know when video recording is active and access my recorded data
- **So that** I feel my privacy is respected and understand what's being monitored
- **Related PBIs**: PBI-042, PBI-043

**US-009: System Status Awareness**
- **As a** driver
- **I want** to be notified if the camera or system is not working properly
- **So that** I know when I'm not being monitored and can take extra caution
- **Related PBIs**: PBI-034, PBI-035, PBI-037

**US-010: Glasses/Accessories Adaptation**
- **As a** driver who wears glasses
- **I want** the system to accurately detect my eye state even with glasses on
- **So that** I receive reliable drowsiness detection
- **Related PBIs**: PBI-032, PBI-003

---

#### 👔 **FLEET MANAGER (Quản lý đội xe) Perspective**

**US-011: Driver Behavior Dashboard**
- **As a** fleet manager
- **I want** to view a dashboard showing all drivers' safety scores and incident counts
- **So that** I can identify high-risk drivers who need additional training
- **Related PBIs**: PBI-045, PBI-041, PBI-043

**US-012: Historical Trip Analysis**
- **As a** fleet manager
- **I want** to review historical trips with timestamps of all safety events
- **So that** I can analyze patterns and improve fleet safety policies
- **Related PBIs**: PBI-045, PBI-041, PBI-043

**US-013: Real-time Fleet Monitoring**
- **As a** fleet manager
- **I want** to monitor all active vehicles in real-time and see current driver states
- **So that** I can intervene immediately if a driver shows dangerous behavior
- **Related PBIs**: PBI-044, PBI-043

**US-014: Automated Incident Reports**
- **As a** fleet manager
- **I want** to receive automated reports when critical events occur (severe drowsiness, repeated distractions)
- **So that** I can follow up with drivers without manually checking logs
- **Related PBIs**: PBI-041, PBI-042

**US-015: Driver Performance Metrics**
- **As a** fleet manager
- **I want** to see metrics like average attention score, distraction frequency, and drowsiness episodes per driver
- **So that** I can objectively evaluate driver performance and safety compliance
- **Related PBIs**: PBI-045, PBI-018, PBI-043

**US-016: Multi-Driver Vehicle Management**
- **As a** fleet manager
- **I want** the system to support multiple enrolled drivers per vehicle
- **So that** I can track which driver was operating each vehicle during incidents
- **Related PBIs**: PBI-029, PBI-028, PBI-043

**US-017: Video Evidence Retrieval**
- **As a** fleet manager
- **I want** to retrieve video clips of specific incidents for investigation
- **So that** I have evidence for insurance claims or disciplinary actions
- **Related PBIs**: PBI-042, PBI-041

**US-018: Passenger Occupancy Tracking**
- **As a** fleet manager
- **I want** to know passenger counts for each trip
- **So that** I can verify vehicle usage compliance and capacity regulations
- **Related PBIs**: PBI-030, PBI-031, PBI-043

---

#### 🛡️ **SAFETY ENGINEER (Kỹ sư An toàn) Perspective**

**US-019: Alert Threshold Configuration**
- **As a** safety engineer
- **I want** to configure thresholds for drowsiness detection (EAR values, duration)
- **So that** I can tune the system to reduce false positives while maintaining safety
- **Related PBIs**: PBI-012, PBI-014, PBI-015

**US-020: Multi-modal Detection Validation**
- **As a** safety engineer
- **I want** to verify that drowsiness is detected using multiple signals (EAR, blink rate, PERCLOS, yawning)
- **So that** the system is robust against individual sensor failures
- **Related PBIs**: PBI-012, PBI-013, PBI-014, PBI-015

**US-021: Gaze Zone Calibration**
- **As a** safety engineer
- **I want** to define and calibrate gaze zones (road, dashboard, mirrors, phone) for different vehicle types
- **So that** gaze-based distraction detection works accurately across vehicle models
- **Related PBIs**: PBI-010, PBI-009

**US-022: Activity Model Performance Monitoring**
- **As a** safety engineer
- **I want** to monitor the accuracy of the activity recognition CNN in production
- **So that** I can identify when model retraining is needed
- **Related PBIs**: PBI-026, PBI-019 to PBI-025

**US-023: Alert Priority Rules**
- **As a** safety engineer
- **I want** to define priority rules when multiple alerts occur simultaneously
- **So that** drivers receive the most critical warning first without alert fatigue
- **Related PBIs**: PBI-040, PBI-038, PBI-039

**US-024: Head Pose + Gaze Fusion**
- **As a** safety engineer
- **I want** to combine head pose and eye gaze data for more accurate attention detection
- **So that** the system can distinguish between legitimate mirror checks vs distractions
- **Related PBIs**: PBI-006, PBI-009, PBI-017, PBI-018

**US-025: Low-Light Performance Testing**
- **As a** safety engineer
- **I want** to test system performance under various lighting conditions (day, night, tunnel)
- **So that** I can ensure reliable detection with the IR camera in all scenarios
- **Related PBIs**: PBI-034, PBI-035

**US-026: Occlusion Handling Strategy**
- **As a** safety engineer
- **I want** the system to detect face occlusions and gracefully degrade (use head pose only)
- **So that** temporary occlusions don't cause complete monitoring failure
- **Related PBIs**: PBI-036, PBI-006

**US-027: False Positive Analysis**
- **As a** safety engineer
- **I want** to analyze false positive alerts with associated video clips
- **So that** I can identify root causes and improve detection algorithms
- **Related PBIs**: PBI-042, PBI-041

---

#### 👨‍💻 **DEVELOPER (Lập trình viên) Perspective**

**US-028: Modular Detection Pipeline**
- **As 
## Phase 3: SCAMPER Method (Acceptance Criteria Definition)

**Technique:** SCAMPER Method  
**Duration:** 35 minutes  
**Objective:** Define detailed Acceptance Criteria for high-priority User Stories using SCAMPER thinking

### SCAMPER Analysis for Acceptance Criteria

Using SCAMPER framework to ensure comprehensive, testable criteria:
- **Substitute**: Alternative detection methods if primary fails
- **Combine**: Multi-signal validation for robust detection
- **Adapt**: Adjust thresholds for different scenarios
- **Modify**: Enhance with additional metrics
- **Put to other uses**: Multi-purpose data (alerts + analytics)
- **Eliminate**: Remove redundant checks, optimize performance
- **Reverse**: Think about false negatives/positives

---

### Acceptance Criteria for Priority User Stories

#### **US-001: Drowsiness Alert** (MUST HAVE)

**Given-When-Then Format:**

**AC-001.1**: Eye Closure Detection
- **Given** the driver's eyes are detected by the system
- **When** the Eye Aspect Ratio (EAR) falls below 0.25 for more than 2 consecutive seconds
- **Then** the system shall trigger a drowsiness alert within 500ms

**AC-001.2**: PERCLOS Threshold
- **Given** eye openness is being monitored over a 60-second window
- **When** PERCLOS (Percentage of Eye Closure) exceeds 20% (eyes closed >20% of time)
- **Then** the system shall classify drowsiness level as "HIGH" and trigger audio alert

**AC-001.3**: Yawning Detection
- **Given** facial landmarks are successfully detected
- **When** Mouth Aspect Ratio (MAR) exceeds 0.6 for more than 3 seconds (yawn detected)
- **Then** the system shall increment yawn counter and trigger mild drowsiness warning after 3 yawns in 5 minutes

**AC-001.4**: Microsleep Detection
- **Given** continuous eye monitoring is active
- **When** eyes close completely (EAR < 0.2) for 0.5 to 3 seconds (microsleep)
- **Then** the system shall immediately trigger critical alert and log event with timestamp

**AC-001.5**: Alert Persistence
- **Given** a drowsiness alert has been triggered
- **When** the driver's EAR returns to normal (>0.25) for at least 5 seconds
- **Then** the alert shall stop, and the system shall log alert duration

**AC-001.6**: False Positive Prevention (SCAMPER: Combine)
- **Given** multiple drowsiness indicators are available (EAR, PERCLOS, yawning, blink rate)
- **When** at least 2 out of 4 indicators show drowsiness signs simultaneously
- **Then** confidence level increases to >80% before triggering alert (reduces false positives)

---

#### **US-002: Distraction Warning** (MUST HAVE)

**AC-002.1**: Head Turn Distraction
- **Given** head pose is estimated successfully
- **When** head yaw angle exceeds ±45° (looking left/right) for more than 2 seconds
- **Then** the system shall trigger distraction warning

**AC-002.2**: Head Down Detection
- **Given** head pose pitch angle is being monitored
- **When** pitch angle exceeds -20° (looking down at phone/dashboard) for more than 1.5 seconds
- **Then** the system shall trigger distraction alert

**AC-002.3**: Gaze-Off-Road Duration
- **Given** gaze direction is classified into zones
- **When** gaze is outside the "road" zone for cumulative 4 seconds within a 10-second window
- **Then** the system shall trigger gaze distraction warning

**AC-002.4**: Mirror Check Exception (SCAMPER: Adapt)
- **Given** head turns to side mirrors or rearview mirror
- **When** head turn duration is less than 1.5 seconds and returns to forward position
- **Then** the system shall NOT trigger distraction alert (legitimate mirror check)

**AC-002.5**: Combined Head + Gaze Validation (SCAMPER: Combine)
- **Given** both head pose and gaze direction are available
- **When** head is forward BUT gaze is off-road (e.g., looking at phone in lap)
- **Then** the system shall detect distraction using gaze as primary signal

---

#### **US-003: Dangerous Activity Alert** (MUST HAVE)

**AC-003.1**: Activity Recognition Accuracy
- **Given** the Activity CNN model is trained on 7 activities
- **When** dangerous activity is detected in video frame
- **Then** the system shall achieve minimum 85% accuracy on test dataset for each activity

**AC-003.2**: Phone Calling Detection
- **Given** video frames are processed by Activity CNN
- **When** "calling" activity is detected with confidence >75% for 3 consecutive frames (0.3 seconds at 10 FPS)
- **Then** the system shall trigger "phone calling" alert immediately

**AC-003.3**: Drinking Detection
- **Given** driver is holding a bottle/cup near mouth
- **When** "drinking" activity confidence exceeds 75% for 2 consecutive frames
- **Then** the system shall trigger "drinking while driving" alert

**AC-003.4**: Smoking Detection
- **Given** hand-to-mouth gesture is detected
- **When** "smoking" activity is classified with confidence >70% for 5 consecutive frames (1 second)
- **Then** the system shall trigger "smoking" alert

**AC-003.5**: Activity Persistence Filtering (SCAMPER: Eliminate false positives)
- **Given** an activity is detected briefly (e.g., scratching face misclassified as calling)
- **When** activity confidence drops below 50% or activity duration is less than minimum threshold
- **Then** the system shall NOT trigger alert (eliminates transient false positives)

**AC-003.6**: Multi-Activity Scenario
- **Given** driver performs multiple dangerous activities simultaneously (e.g., calling + looking down)
- **When** multiple activities are detected
- **Then** the system shall prioritize the most critical activity (calling > drinking > smoking) for alert

---

#### **US-004: Hands-Free Driving Warning** (MUST HAVE)

**AC-004.1**: Hands-Off-Wheel Detection
- **Given** Activity CNN or hand tracking module is active
- **When** "hands_off_wheel" activity is detected with confidence >80% for more than 3 seconds
- **Then** the system shall trigger immediate alert

**AC-004.2**: Two-Hands Requirement
- **Given** hand detection is active
- **When** only one hand is detected on wheel for more than 10 seconds (acceptable temporarily)
- **Then** the system shall log event but NOT trigger alert (one hand is acceptable)

**AC-004.3**: No-Hands Critical Alert
- **Given** both hands are off the wheel
- **When** duration exceeds 5 seconds
- **Then** the system shall escalate to CRITICAL alert with louder audio

**AC-004.4**: Alert Cancellation
- **Given** hands-off-wheel alert is active
- **When** at least one hand returns to wheel position for 2 consecutive seconds
- **Then** the alert shall stop and event shall be logged

---

#### **US-006: Driver Identification** (SHOULD HAVE)

**AC-006.1**: Face Recognition Speed
- **Given** an enrolled driver's face appears in camera frame
- **When** face encoding is compared against database
- **Then** identification shall complete within 100ms with minimum 95% accuracy

**AC-006.2**: Unknown Driver Handling
- **Given** a face is detected but not recognized
- **When** similarity score is below 0.6 (threshold) for all enrolled drivers
- **Then** the system shall mark session as "unknown driver" and optionally prompt enrollment

**AC-006.3**: Multi-Driver Scenario
- **Given** vehicle supports multiple enrolled drivers (e.g., 5 drivers)
- **When** driver identification runs
- **Then** the system shall correctly identify the driver with >95% accuracy even with similar-looking faces

**AC-006.4**: Session Association
- **Given** driver is successfully identified
- **When** driving session starts
- **Then** all subsequent events (drowsiness, distraction, activities) shall be associated with identified driver ID in database

---

#### **US-007: Enrollment Process** (SHOULD HAVE)

**AC-007.1**: Face Capture Quality
- **Given** driver wants to enroll in system
- **When** enrollment process captures face images
- **Then** at least 10 images shall be captured with face detection confidence >90%, covering angles: center, ±15° left/right, ±10° up/down

**AC-007.2**: Encoding Generation
- **Given** face images are captured during enrollment
- **When** face encoding is generated
- **Then** 128-dimensional encodin
g vector shall be created using dlib/FaceNet model and stored in database

**AC-007.3**: Duplicate Prevention
- **Given** a driver attempts to enroll
- **When** their face encoding matches existing driver (similarity >0.7)
- **Then** the system shall reject enrollment and notify "driver already enrolled"

**AC-007.4**: Enrollment Completion Time
- **Given** enrollment process starts
- **When** all steps complete (capture, encoding, database storage)
- **Then** total enrollment time shall not exceed 30 seconds

---

#### **US-009: System Status Awareness** (MUST HAVE)

**AC-009.1**: Camera Connectivity Check
- **Given** the system is running
- **When** camera feed is lost or no frames received for 2 seconds
- **Then** the system shall display "Camera Offline" warning and log error

**AC-009.2**: Face Detection Failure Warning
- **Given** camera is online and streaming
- **When** no face is detected for more than 10 seconds
- **Then** the system shall display "No Driver Detected" warning

**AC-009.3**: FPS Monitoring
- **Given** the system is processing video frames
- **When** FPS drops below 15 for more than 5 seconds
- **Then** the system shall log performance warning and display "Low Performance" indicator

**AC-009.4**: Low Light Detection
- **Given** camera brightness is monitored
- **When** average frame brightness falls below threshold (histogram analysis)
- **Then** the system shall check if IR illumination is active; if not, display "Low Light" warning

**AC-009.5**: System Health Dashboard Indicator
- **Given** all system components are monitored (camera, face detection, FPS, models)
- **When** any component status changes
- **Then** the dashboard shall update status indicator within 1 second (green=OK, yellow=warning, red=error)

---

#### **US-019: Alert Threshold Configuration** (SHOULD HAVE - Safety Engineer)

**AC-019.1**: Configurable EAR Threshold
- **Given** drowsiness detection uses EAR thresholds
- **When** safety engineer updates EAR threshold in configuration file (range: 0.15 to 0.30)
- **Then** the system shall reload configuration and apply new threshold without restart

**AC-019.2**: Configurable Duration Thresholds
- **Given** distraction detection uses duration thresholds
- **When** safety engineer changes duration parameters (e.g., head turn: 1-5 seconds)
- **Then** the updated thresholds shall take effect within 5 seconds

**AC-019.3**: Configuration Validation
- **Given** configuration file is edited
- **When** system loads configuration
- **Then** the system shall validate all parameters are within acceptable ranges and log errors for invalid values

**AC-019.4**: Default Configuration Fallback
- **Given** configuration file is missing or corrupted
- **When** system starts
- **Then** the system shall use hardcoded default thresholds and log warning

---

#### **US-028: Modular Detection Pipeline** (MUST HAVE - Developer)

**AC-028.1**: Independent Module Execution
- **Given** detection pipeline has modules (face, eye, head, gaze, activity)
- **When** one module fails (e.g., gaze estimation error)
- **Then** other modules shall continue functioning normally (graceful degradation)

**AC-028.2**: Module Configuration
- **Given** each detection module has configurable parameters
- **When** developer enables/disables specific modules in config
- **Then** only enabled modules shall run, reducing processing load

**AC-028.3**: Module Output Schema
- **Given** each module produces output
- **When** module completes processing
- **Then** output shall follow standardized JSON schema with fields: timestamp, confidence, detected_values, status

**AC-028.4**: Module Execution Time
- **Given** all modules run sequentially or in parallel
- **When** a single frame is processed
- **Then** total pipeline execution time shall not exceed 50ms (supports 20 FPS minimum)

---

#### **US-030: Database Schema Design** (MUST HAVE - Developer)

**AC-030.1**: Event Table Schema
- **Given** events are logged to database
- **When** event record is created
- **Then** table shall include fields: event_id (PK), session_id (FK), event_type (enum), timestamp, severity, confidence, metadata (JSON), driver_id (FK)

**AC-030.2**: Session Table Schema
- **Given** driving sessions are tracked
- **When** session record is created
- **Then** table shall include fields: session_id (PK), driver_id (FK), start_time, end_time, vehicle_id, total_events, video_path

**AC-030.3**: Driver Table Schema
- **Given** drivers are enrolled
- **When** driver record is created
- **Then** table shall include fields: driver_id (PK), name, face_encoding (BLOB/TEXT), enrollment_date, last_active

**AC-030.4**: Query Performance
- **Given** database contains 10,000+ event records
- **When** query retrieves events for specific driver and date range
- **Then** query shall complete within 200ms using proper indexes (driver_id, timestamp)

**AC-030.5**: Video Metadata Linking
- **Given** video clips are recorded for events
- **When** event record is created
- **Then** video_path or video_id shall be stored in event metadata, enabling retrieval of associated video

---

#### **US-038: Drowsiness Test Scenarios** (MUST HAVE - QA)

**AC-038.1**: True Positive Rate
- **Given** test dataset with 100 labeled drowsiness instances
- **When** system processes test dataset
- **Then** system shall correctly detect at least 90 instances (90% TPR)

**AC-038.2**: False Positive Rate
- **Given** 1-hour test drive with alert driver (no drowsiness)
- **When** system monitors driver continuously
- **Then** system shall trigger no more than 1 false drowsiness alert per hour

**AC-038.3**: EAR Calibration Test
- **Given** drivers with different eye shapes (Asian, Caucasian, etc.)
- **When** EAR threshold is tested across diverse subjects
- **Then** system shall maintain >85% accuracy across all demographics (no bias)

**AC-038.4**: Yawning Detection Accuracy
- **Given** test dataset with 50 yawning instances and 50 normal mouth movements (talking, eating)
- **When** system processes dataset
- **Then** system shall correctly classify yawning with >85% precision and >80% recall

---

#### **US-039: Activity Recognition Test Dataset** (MUST HAVE - QA)

**AC-039.1**: Per-Activity Accuracy
- **Given** test dataset with 100 instances per activity (7 activities = 700 total)
- **When** Activity CNN processes test dataset
- **Then** each activity shall achieve minimum 85% accuracy individually

**AC-039.2**: Confusion Matrix Analysis
- **Given** Activity CNN predictions on test dataset
- **When** confusion matrix is generated
- **Then** no two activities shall have cross-confusion rate exceeding 15% (e.g., calling misclassified as drinking <15% of time)

**AC-039.3**: Real-time Inference Speed
- **Given** Activity CNN model is deployed
- **When** single frame is processed
- **Then** inference time shall not exceed 30ms on target hardware (enables 30+ FPS)

**AC-039.4**: Diverse Conditions Testing
- **Given** test dataset includes various lighting, angles, and driver demographics
- **When** model is evaluated
- **Then** accuracy shall remain above 80% across all conditions (robustness)

---

#### **US-043: Alert Timing Verification** (MUST HAVE - QA)

**AC-043.1**: Detection-to-Alert Latency
- **Given** drowsiness or distraction event occurs
- **When** event is detected by system
- **Then** audio alert shall trigger within 500ms (real-time requirement)

**AC-043.2**: Alert Audio Duration
- **Given** alert is triggered
- **When** audio plays
- **Then** alert sound shall last 1-3 seconds (long enough to notice, short enough not to annoy)

**AC-043.3**: Alert Queue Management
- **Given** multiple events occur within 2 seconds
- **When** alerts are queued
- **Then** only the highest priority alert shall play, with others logged but not audio-triggered (prevent spam)

**AC-043.4**: Alert Cancellation Responsiveness
- **Given** alert is active and driver corrects behavior
- **When** event condition clears (e.g., eyes reopen)
- **Then** alert shall stop within 1 second

---

#### **US-044: False
## Phase 4: Question Storming + MoSCoW (Prioritization & Refinement)

**Techniques:** Question Storming + MoSCoW Method  
**Duration:** 30 minutes  
**Objective:** Identify gaps, risks, and finalize priority classification for all Product Backlog Items

---

### Part A: Question Storming (Gap & Risk Analysis)

#### **Category 1: Technical Feasibility Questions**

**Q1**: Can we achieve 20+ FPS with all detection modules running on target hardware (Jetson Nano/Raspberry Pi)?
- **Risk**: Performance bottleneck
- **Mitigation**: Optimize CNN models (MobileNetV2), use threading/multiprocessing, disable optional modules

**Q2**: How accurate is gaze estimation with IR camera in different lighting conditions?
- **Risk**: Gaze tracking may be unreliable in bright sunlight or complete darkness
- **Mitigation**: Combine with head pose for robust distraction detection

**Q3**: Can we train Activity CNN with sufficient accuracy (>85%) for all 7 activities?
- **Risk**: Some activities look similar (drinking vs smoking), limited training data
- **Mitigation**: Collect diverse dataset (300+ samples per activity), use data augmentation

**Q4**: How do we handle drivers with very different eye shapes (EAR calibration)?
- **Risk**: EAR thresholds may not work for all demographics
- **Mitigation**: Per-driver calibration during enrollment, adaptive thresholds

**Q5**: What happens if camera is partially occluded by sun visor or steering wheel?
- **Risk**: Intermittent face detection failures
- **Mitigation**: Face occlusion detection (PBI-036), use last known state, warn driver

#### **Category 2: User Experience Questions**

**Q6**: Will frequent false alerts cause alert fatigue and lead drivers to ignore warnings?
- **Risk**: System becomes annoying and drivers disable it
- **Mitigation**: Tune thresholds for <1 false alert/hour, alert priority management

**Q7**: How intrusive is continuous video recording? Will drivers feel uncomfortable?
- **Risk**: Privacy concerns, driver resistance
- **Mitigation**: Event-triggered recording only (±30s around events), clear privacy policy

**Q8**: Can drivers easily understand what triggered an alert?
- **Risk**: Unclear feedback leads to confusion
- **Mitigation**: Visual dashboard shows detected state (drowsy, distracted, activity), event log

**Q9**: How long does driver enrollment take? Is it convenient?
- **Risk**: Slow/complex enrollment discourages usage
- **Mitigation**: <30 second enrollment (AC-007.4), simple UI

**Q10**: What if multiple people share the same vehicle? Can system handle driver changes?
- **Risk**: Wrong driver attribution for events
- **Mitigation**: Multi-driver support (PBI-029), auto-identification at trip start

#### **Category 3: System Integration Questions**

**Q11**: How does the system integrate with existing vehicle systems (CAN bus, ignition)?
- **Risk**: Manual start/stop is cumbersome
- **Mitigation**: Auto-start when ignition on (future enhancement), for now use manual start

**Q12**: Where is data stored? Cloud or local? What about internet connectivity?
- **Risk**: Cloud dependency may fail in areas without signal
- **Mitigation**: Local database (SQLite), optional cloud sync for fleet management

**Q13**: How do we update detection models and system software in deployed vehicles?
- **Risk**: Outdated models, bugs in production
- **Mitigation**: OTA (Over-The-Air) update capability (future), manual SD card update for thesis

**Q14**: What hardware interfaces are needed? USB camera only or additional sensors?
- **Risk**: Hardware compatibility issues
- **Mitigation**: IR camera via USB, GPIO for LED alerts (optional), standard interfaces

#### **Category 4: Safety & Reliability Questions**

**Q15**: What if the system crashes while driving? Is there a watchdog?
- **Risk**: Silent failure means no monitoring
- **Mitigation**: System health monitoring (PBI-034), auto-restart on crash, LED status indicator

**Q16**: Can drowsiness detection work for drivers taking medication that causes drowsy eyes?
- **Risk**: Medical conditions may cause false positives
- **Mitigation**: Per-driver threshold tuning, medical exemption mode (future)

**Q17**: How do we prevent system hacking or tampering by drivers who want to disable monitoring?
- **Risk**: Drivers cover camera, disable software
- **Mitigation**: Camera occlusion detection, tamper-evident hardware, audit logs

**Q18**: What happens if driver is in an emergency situation (e.g., avoiding collision) and looks off-road?
- **Risk**: Alert during emergency adds stress
- **Mitigation**: Short distraction (<2 seconds) doesn't trigger alert, emergency mode (future)

#### **Category 5: Data & Privacy Questions**

**Q19**: How long is video data retained? When is it deleted?
- **Risk**: Storage fills up, old data accumulates
- **Mitigation**: Auto-delete after 30 days or when storage >90% (AC-048.4)

**Q20**: Who has access to driver monitoring data? Can drivers delete their own data?
- **Risk**: Data misuse, privacy violations
- **Mitigation**: Role-based access (driver, fleet manager, admin), driver can request deletion (GDPR-like)

**Q21**: Is face encoding storage secure? Can someone steal face data?
- **Risk**: Biometric data breach
- **Mitigation**: Encrypt face encodings in database, no raw face images stored (only encodings)

**Q22**: How do we anonymize data for fleet analytics while maintaining driver accountability?
- **Risk**: Privacy vs accountability tradeoff
- **Mitigation**: Aggregated stats anonymous, individual events linked to driver ID (fleet manager only)

#### **Category 6: Scalability & Deployment Questions**

**Q23**: Can the system scale to 100+ vehicles for fleet deployment?
- **Risk**: Database performance, central management complexity
- **Mitigation**: Each vehicle has local DB, central server aggregates data (Phase 2 feature)

**Q24**: How do we train support staff or fleet managers to use the system?
- **Risk**: Poor usability adoption
- **Mitigation**: User manual, training videos (part of deliverables)

**Q25**: What are the hardware costs per vehicle? Is it affordable for small fleet operators?
- **Risk**: High cost limits adoption
- **Mitigation**: Use Jetson Nano ($100) or Raspberry Pi 4 ($75) + IR camera ($30) = ~$150 total

#### **Category 7: Testing & Validation Questions**

**Q26**: How do we create ground truth labels for test datasets (especially activities)?
- **Risk**: Inaccurate labels lead to poor model training
- **Mitigation**: Manual labeling by 2-3 reviewers, inter-rater agreement >90%

**Q27**: Can we simulate long driving sessions (8 hours) for load testing?
- **Risk**: No access to real 8-hour drives
- **Mitigation**: Use recorded video loops, synthetic data

**Q28**: How do we test in real vehicle environments vs lab setup?
- **Risk**: Lab tests don't reflect real vibrations, lighting changes
- **Mitigation**: Field testing phase with 5-10 real drives (part of thesis testing)

**Q29**: What metrics define "success" for this thesis project?
- **Risk**: Unclear success criteria
- **Mitigation**: 
  - Drowsiness detection: >90% accuracy, <1 false alert/hour
  - Activity recognition: >85% per-activity accuracy
  - System uptime: >99% (no crashes in 8-hour test)
  - Real-time: >15 FPS

**Q30**: How do we handle edge cases discovered during testing?
- **Risk**: New bugs found late in development
- **Mitigation**: Continuous testing throughout sprints, prioritize MUST HAVE features first

---

### Part B: MoSCoW Prioritization (Final Classification)

#### **MUST HAVE (23 items)** - Core MVP for thesis graduation
These features are absolutely essential. Without them, the system doesn't work.

**Core Detection:**
1. **PBI-001**: Face Detection & Tracking
2. **PBI-002**: Eye Region Detection
3. **PBI-003**: Eye Openness Detection (EAR)
4. **PBI-004**: Blink Frequency Monitoring
5. **PBI-006**: Head Pose Estimation
6. **PBI-007**: Head Location Tracking
7. **PBI-009**: Gaze Direction Estimation
8. **PBI-010**: Gaze Zone Classification

**Safety Detection:**
9. **PBI-012**: Dro
## 🎉 Brainstorming Session Complete

### Final Summary

**Session Duration:** ~2.5 hours (4 phases completed)  
**Total Ideas/Items Generated:** 195 items
- **Product Backlog Items**: 45 features across 13 categories
- **User Stories**: 48 stories from 5 stakeholder perspectives
- **Acceptance Criteria**: 72 detailed criteria in Given-When-Then format
- **Critical Questions**: 30 questions identifying gaps and risks

---

### Key Deliverables Created

✅ **Product Backlog (Deliverable #3):**
- 45 PBIs with detailed descriptions, technology stack, and outputs
- Organized into 13 functional categories
- MoSCoW prioritization: 24 MUST HAVE, 17 SHOULD HAVE, 4 COULD HAVE

✅ **User Stories (Deliverable #4):**
- 48 User Stories in Agile format (As a... I want... So that...)
- Covers 5 stakeholder perspectives: Driver, Fleet Manager, Safety Engineer, Developer, QA Tester
- All PBIs linked to at least one User Story

✅ **Acceptance Criteria:**
- 72 testable criteria using Given-When-Then format
- Measurable thresholds (%, seconds, FPS, accuracy)
- SCAMPER-enhanced for robustness (multi-signal validation, false positive reduction)

✅ **Risk Analysis & Timeline:**
- 30 critical questions identifying technical, UX, safety, and deployment risks
- 5 high-risk items with mitigation strategies
- 10-20 week development timeline with 5-10 sprints
- Success criteria defined: >90% drowsiness accuracy, >85% activity accuracy, >15 FPS, <1 false alert/hour

---

### Scope Clarifications Documented

**In Scope:**
- ✅ 7 dangerous activities (calling, drinking, smoking, yawning, hands off wheel, arm out window, looking at directions)
- ✅ Eye Gaze + Head Pose tracking (both required)
- ✅ Passenger counting
- ✅ Driver enrollment & identification (SHOULD HAVE)
- ✅ Event-triggered video recording
- ✅ Real-time alerts + logging

**Out of Scope (WON'T HAVE):**
- ❌ Safety belt detection (removed)
- ❌ Facial expression analysis (skip)
- ❌ Cloud sync / fleet server (local only)
- ❌ OTA updates (manual only)
- ❌ Mobile app (desktop UI only)
- ❌ CAN bus integration (manual start)
- ❌ Multi-camera support (single IR camera)

**To Be Decided:**
- 🔄 Authentication: startup only vs continuous monitoring (deferred decision)

---

### Technology Stack Finalized

**Computer Vision:** OpenCV, dlib, MediaPipe  
**AI/ML Models:** MobileNetV2 (Activity CNN), FaceNet (face recognition), dlib (face landmarks)  
**Hardware:** IR Camera (USB), Jetson Nano or Raspberry Pi 4  
**Database:** SQLite (local), optional PostgreSQL for fleet  
**Framework:** Python (primary), possible web UI (Flask/React)  
**Alerts:** Audio (pygame/pydub), Visual (GPIO LED or GUI)

---

### Next Steps (Outside This Brainstorming Session)

**Step 4: Idea Organization** (BMAD workflow next step):
1. Export Product Backlog to structured document (Markdown/Excel)
2. Export User Stories with Acceptance Criteria to separate document
3. Create traceability matrix (PBI → User Story → Acceptance Criteria)

**Other Thesis Deliverables to Create:**
1. **Architecture Design** (Deliverable #5): Based on modular pipeline (PBI-028)
2. **Database Schema** (Deliverable #6): From PBI-030, PBI-041, PBI-042, PBI-043, PBI-027
3. **UI/Interface Design** (Deliverable #7): From PBI-044, PBI-045
4. **Test Plan** (Deliverable #8): Based on QA User Stories (US-038 to US-048)
5. **Test Cases** (Deliverable #9): Derived from 72 Acceptance Criteria
6. **Sprint Backlog** (Deliverable #10): Use timeline recommendation (10-20 weeks)
7. **Code Standard** (Deliverable #11): Python PEP 8, code structure guidelines
8. **Meeting Minutes** (Deliverable #12): Document sprint planning, reviews, retrospectives
9. **Reflection** (Deliverable #13): Lessons learned, challenges, future improvements

**Recommendation:** Use the comprehensive thesis guide created earlier:
`D:\HocTap\docs-driver\_bmad-output\guides\HUONG-DAN-DO-AN-TOT-NGHIEP.md`

---

### Session Metadata

**Facilitator:** hung-thanh  
**Session Date:** 2026-03-03  
**Session File:** `brainstorming-session-2026-03-03-004815.md`  
**Total Lines:** ~1200+ lines  
**Status:** ✅ **COMPLETE**

---

## 🚀 Ready to Move Forward!

All foundational requirements work is complete. You now have:
- Clear, detailed Product Backlog with priorities
- Comprehensive User Stories with testable Acceptance Criteria
- Risk mitigation strategies
- Development timeline

**You can now proceed to:**
1. Architecture design (start with system components diagram)
2. Database schema design (use suggested tables from AC-030)
3. Sprint planning (use 10-20 week timeline)

Good luck with your thesis! 🎓

