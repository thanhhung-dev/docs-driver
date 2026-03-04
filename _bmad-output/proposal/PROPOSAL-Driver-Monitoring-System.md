# PROJECT PROPOSAL
## Driver Monitoring System using Computer Vision & AI

---

**Student Name:** Hung Thanh  
**Advisor:** [Advisor Name]  
**Institution:** [University Name]  
**Department:** [Department Name]  
**Date:** March 4, 2026  
**Project Type:** Undergraduate Thesis / Capstone Project  

---

## TABLE OF CONTENTS

1. [Problem Statement](#1-problem-statement)
2. [Proposed Solution](#2-proposed-solution)
3. [Project Objectives](#3-project-objectives)
4. [Project Scope](#4-project-scope)
5. [System Features](#5-system-features)
6. [Technology Stack](#6-technology-stack)
7. [Expected Outcomes](#7-expected-outcomes)
8. [Project Timeline](#8-project-timeline)
9. [Success Criteria](#9-success-criteria)
10. [References](#10-references)

---

## 1. PROBLEM STATEMENT

### 1.1 Background

Road traffic accidents are one of the leading causes of death and injury worldwide. According to the World Health Organization (WHO), approximately 1.35 million people die each year as a result of road traffic crashes, with an additional 20-50 million suffering non-fatal injuries. A significant proportion of these accidents are directly attributed to human factors, particularly:

- **Driver drowsiness and fatigue**: Studies show that 20-30% of traffic accidents are caused by drowsy driving, where drivers fall asleep at the wheel or experience microsleep episodes
- **Driver distraction**: Taking attention away from the road (e.g., using mobile phones, eating, adjusting controls) contributes to approximately 25% of all traffic accidents
- **Dangerous driving behaviors**: Activities such as smoking while driving, reaching for objects, or driving with hands off the wheel increase accident risk significantly

### 1.2 Problem Impact

The consequences of driver inattention and unsafe behaviors are severe:

**Human Impact:**
- Loss of life and permanent disabilities
- Psychological trauma for victims and families
- Reduced quality of life for accident survivors

**Economic Impact:**
- Medical treatment costs running into billions annually
- Insurance claim expenses
- Vehicle damage and property loss
- Lost productivity due to injuries and fatalities

**Social Impact:**
- Public safety concerns
- Increased traffic congestion from accidents
- Strain on emergency response services

### 1.3 Current Limitations

Existing solutions have significant limitations:

- **Manual enforcement**: Traffic police cannot monitor all drivers continuously
- **Post-accident analysis**: Dashboard cameras only provide evidence after accidents occur
- **Driver education alone**: Insufficient to prevent momentary lapses in judgment
- **Basic warning systems**: Limited to seatbelt reminders or lane departure warnings, not comprehensive driver behavior monitoring

### 1.4 Need for Solution

There is an urgent need for a proactive, real-time system that can:
- Continuously monitor driver state and behavior
- Detect early warning signs of drowsiness, distraction, and dangerous activities
- Provide immediate alerts to prevent accidents before they occur
- Log incidents for analysis and driver improvement

---

## 2. PROPOSED SOLUTION

### 2.1 Solution Overview

This project proposes the development of an **AI-powered Driver Monitoring System (DMS)** that uses computer vision and machine learning techniques to continuously monitor driver behavior and provide real-time safety interventions.

**Core Concept:**  
A single infrared (IR) camera mounted on the vehicle dashboard captures video of the driver's face. Advanced computer vision algorithms and deep learning models analyze the video stream in real-time to detect:
- Signs of drowsiness (eye closure, yawning, head nodding)
- Distraction indicators (gaze direction away from road, prolonged head turns)
- Dangerous activities (phone calling, drinking, smoking, hands off wheel, etc.)

When risky behavior is detected, the system immediately triggers audio/visual alerts to warn the driver, while simultaneously logging the event for post-trip analysis.

### 2.2 How It Works

**System Workflow:**

```
┌─────────────┐
│ IR Camera   │
│ (Captures   │
│ Driver Face)│
└──────┬──────┘
       │
       ▼
┌─────────────────────┐
│ Computer Vision     │
│ Processing Pipeline │
├─────────────────────┤
│ 1. Face Detection   │
│ 2. Eye Tracking     │
│ 3. Head Pose        │
│ 4. Gaze Direction   │
│ 5. Activity CNN     │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ AI Detection Models │
├─────────────────────┤
│ • Drowsiness Score  │
│ • Distraction Level │
│ • Activity Class    │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ Decision Engine     │
│ (Alert Logic)       │
└──────┬──────────────┘
       │
       ├──► Audio Alert (Speaker)
       ├──► Visual Warning (Dashboard)
       └──► Event Logging (Database)
```

**Key Processing Steps:**

1. **Face Detection & Tracking**: Detect driver's face using dlib or MediaPipe face detection models
2. **Facial Landmark Extraction**: Identify 68 facial landmarks for eye, mouth, and head analysis
3. **Eye State Analysis**: Calculate Eye Aspect Ratio (EAR) to determine if eyes are open or closed
4. **Head Pose Estimation**: Use solvePnP algorithm to compute head orientation (pitch, yaw, roll)
5. **Gaze Direction Estimation**: Combine eye position and head pose to determine where driver is looking
6. **Activity Recognition**: Deep learning CNN model classifies dangerous activities from video frames
7. **Multi-signal Fusion**: Combine all detection signals to make robust alert decisions
8. **Real-time Alerting**: Trigger audio warnings and visual indicators when thresholds are exceeded

### 2.3 Innovation & Advantages

**Compared to existing solutions, this system offers:**

 **Comprehensive Monitoring**: Detects multiple risk factors (drowsiness, distraction, activities) in one system  
 **Real-time Prevention**: Provides immediate warnings, not just post-accident recording  
 **AI-Powered Accuracy**: Uses machine learning models trained on diverse datasets for robust detection  
 **Night Vision Capable**: IR camera works in complete darkness  
 **Privacy-Preserving**: All processing happens locally on device, no cloud transmission  
 **Affordable Hardware**: Uses standard IR camera and edge computing device (Jetson Nano/Raspberry Pi)  
 **Data-Driven Insights**: Logs events for driver behavior analysis and improvement  

---

## 3. PROJECT OBJECTIVES

### 3.1 Primary Objectives

**Objective 1: Build a Working Real-time Driver Monitoring System**
- Develop complete end-to-end system from camera input to alert output
- Achieve real-time performance with minimum 15 FPS processing speed
- Ensure system stability with <1% crash rate during continuous operation

**Objective 2: Implement Drowsiness Detection**
- Detect drowsiness using multiple indicators:
  - Eye closure duration (Eye Aspect Ratio - EAR)
  - Blink frequency analysis
  - Yawning detection (Mouth Aspect Ratio - MAR)
  - PERCLOS (Percentage of Eye Closure) calculation
- Target detection accuracy: >90%
- Alert latency: <2 seconds from drowsiness onset

**Objective 3: Implement Distraction Detection**
- Monitor driver attention using:
  - Head pose orientation (pitch, yaw, roll angles)
  - Gaze direction and zone classification
  - Time spent looking away from road
- Distinguish between legitimate mirror checks and distractions
- Target detection accuracy: >85%

**Objective 4: Implement Dangerous Activity Recognition**
- Train deep learning model to recognize 7 dangerous activities:
  1. Phone calling (holding phone to ear)
  2. Drinking (from bottle or cup)
  3. Smoking (cigarette in hand)
  4. Yawning (drowsiness indicator)
  5. Hands off steering wheel
  6. Arm extended out window
  7. Looking at navigation/phone screen
- Target per-activity accuracy: >85%
- False positive rate: <5%

**Objective 5: Implement Driver Identification**
- Support driver enrollment via face recognition
- Automatically identify driver when entering vehicle
- Associate all events with specific driver for personalized analysis

**Objective 6: Develop Alert and Logging System**
- Real-time audio warnings for critical events
- Visual dashboard showing current driver state
- Comprehensive event logging to database
- Event-triggered video recording for evidence

### 3.2 Secondary Objectives

- Support various lighting conditions (day, night, tunnels) using IR camera
- Handle accessories (glasses, masks) without significant accuracy loss
- Provide configurable alert thresholds for different sensitivity levels
- Generate analytics dashboard for driver behavior trends
- Count passengers for occupancy tracking

### 3.3 Learning Objectives

As an educational project, this thesis aims to demonstrate:
- Application of computer vision algorithms (face detection, landmark extraction, pose estimation)
- Deep learning model training and optimization
- Real-time system design and performance optimization
- Software engineering practices (version control, testing, documentation)
- Problem-solving skills in handling real-world challenges (lighting variations, occlusions, etc.)

---

## 4. PROJECT SCOPE

### 4.1 In Scope (What WILL be included)

#### **Core Detection Features**
 **Drowsiness Detection Module**
- Eye Aspect Ratio (EAR) calculation and monitoring
- Blink frequency analysis
- Yawning detection via Mouth Aspect Ratio (MAR)
- Microsleep detection (brief eye closures 0.5-3 seconds)
- PERCLOS (Percentage of Eye Closure) calculation

 **Distraction Detection Module**
- Head pose estimation (pitch, yaw, roll angles)
- Head turn detection (looking left, right, down)
- Eye gaze direction estimation
- Gaze zone classification (road, dashboard, mirrors, passenger, phone)
- Combined head + gaze attention score

 **Dangerous Activity Recognition Module**
- 7 activities detected via CNN model:
  1. Phone calling
  2. Drinking
  3. Smoking
  4. Yawning
  5. Hands off wheel
  6. Arm out window
  7. Looking at directions/phone
- Activity CNN model training and evaluation

 **Driver Identification Module**
- Face enrollment process (capture and encoding)
- Face recognition for driver identification
- Multi-driver support per vehicle
- Session association with identified driver

 **Alert System**
- Real-time audio alerts (beep sounds, voice warnings)
- Visual alerts on dashboard
- Alert priority management (prevent alert spam)

 **Data Logging & Recording**
- Event logging to local database (SQLite)
- Event-triggered video recording (±30 seconds around events)
- Driving session tracking (start/end times, trip duration)

 **User Interface**
- Live monitoring dashboard showing:
  - Camera feed with detection overlays
  - Current driver state (drowsy, distracted, activity)
  - System health indicators (FPS, camera status)
- Historical data viewing (past trips, event counts)

 **System Health Monitoring**
- IR camera connectivity checks
- Face detection failure warnings
- FPS monitoring and performance warnings
- Low light detection

 **Passenger Monitoring**
- Passenger counting (front and rear seats)
- Occupancy tracking per trip

#### **Hardware & Software Stack**
 IR camera (night vision capable)  
 Edge computing device (Jetson Nano or Raspberry Pi 4)  
 Python-based software (OpenCV, dlib, TensorFlow/PyTorch)  
 Local database (SQLite)  
 Desktop/web-based UI  

#### **Testing & Documentation**
 Test plan with defined test scenarios  
 Test cases for all detection modules  
 Performance benchmarking (accuracy, FPS, latency)  
 User manual  
 Technical documentation  
 Source code with inline documentation  

### 4.2 Out of Scope (What will NOT be included)

 **Safety belt detection** - Removed due to scope constraints  
 **Facial expression analysis** (beyond yawning) - Low priority, high complexity  
 **Mobile app** - Desktop/web UI only  
 **Cloud synchronization** - Local storage only  
 **Fleet management server** - Single vehicle focus  
 **Over-the-air (OTA) software updates** - Manual update only  
 **CAN bus integration** - Manual system start/stop  
 **Multi-camera support** - Single IR camera only  
 **Autonomous driving features** - Monitoring only, no vehicle control  
 **Advanced biometric analysis** - Focus on behavior, not health monitoring  
 **Real-time cloud streaming** - Privacy and bandwidth concerns  

### 4.3 Assumptions & Constraints

**Assumptions:**
- Single driver per trip (multi-driver support for different trips)
- Driver face visible to camera (not occluded by objects)
- IR camera positioned on dashboard facing driver
- System has sufficient computational power (Jetson Nano or equivalent)
- Available training datasets for activity recognition

**Constraints:**
- Development timeline: 10-20 weeks
- Budget: Limited to educational resources
- Hardware: Consumer-grade IR camera and edge computing device
- Dataset size: May need to collect custom training data for activities
- Processing power: Must maintain >15 FPS on target hardware

### 4.4 Deferred Decisions (To Be Decided During Development)

 **Authentication Strategy**: Startup identification vs. continuous monitoring  
 **Video Storage Duration**: 7 days vs. 30 days retention policy  
 **Alert Aggressiveness**: Conservative (fewer false positives) vs. aggressive (higher sensitivity)  
 **Dashboard Technology**: OpenCV GUI vs. web-based dashboard (Flask/React)  

---

## 5. SYSTEM FEATURES

### 5.1 Feature Categories (13 Functional Areas)

Based on comprehensive brainstorming analysis, the system includes **45 Product Backlog Items (PBIs)** organized into 13 categories:

#### **Category 1: Core Face & Eye Detection (5 features)**
- PBI-001: Face Detection & Tracking
- PBI-002: Eye Region Detection
- PBI-003: Eye Openness Detection (EAR)
- PBI-004: Blink Frequency Monitoring
- PBI-005: Eye Location Tracking

#### **Category 2: Head Pose & Orientation (3 features)**
- PBI-006: Head Pose Estimation
- PBI-007: Head Location Tracking
- PBI-008: Head Zone Classification

#### **Category 3: Eye Gaze Tracking (3 features)**
- PBI-009: Gaze Direction Estimation
- PBI-010: Gaze Zone Classification
- PBI-011: Pupil Detection & Tracking

#### **Category 4: Drowsiness Detection (4 features)**
- PBI-012: Drowsiness Detection (EAR-based)
- PBI-013: Yawning Detection
- PBI-014: Microsleep Detection
- PBI-015: PERCLOS Calculation

#### **Category 5: Distraction Detection (3 features)**
- PBI-016: Head Turn Distraction
- PBI-017: Gaze-off-Road Detection
- PBI-018: Attention Score Calculation

#### **Category 6: Dangerous Activity Recognition (8 features)**
- PBI-019: Phone Calling Detection
- PBI-020: Drinking Detection
- PBI-021: Smoking Detection
- PBI-022: Yawning Activity Detection
- PBI-023: Hands Off Wheel Detection
- PBI-024: Arm Out Window Detection
- PBI-025: Looking at Directions Detection
- PBI-026: Activity CNN Model Training

#### **Category 7: Driver Enrollment & Identification (3 features)**
- PBI-027: Driver Face Enrollment
- PBI-028: Driver Identification
- PBI-029: Multi-Driver Management

#### **Category 8: Passenger Monitoring (2 features)**
- PBI-030: Passenger Counting
- PBI-031: Passenger Face Detection

#### **Category 9: Safety Accessories (2 features)**
- PBI-032: Glasses Detection
- PBI-033: Mask Detection

#### **Category 10: System Health & Camera Management (4 features)**
- PBI-034: IR Camera Health Check
- PBI-035: Low Light Detection
- PBI-036: Face Occlusion Detection
- PBI-037: System FPS Monitoring

#### **Category 11: Alert System (3 features)**
- PBI-038: Real-time Audio Alerts
- PBI-039: Visual Alerts (LED/Dashboard)
- PBI-040: Alert Priority Management

#### **Category 12: Data Logging & Recording (3 features)**
- PBI-041: Event Logging
- PBI-042: Video Recording (Event-triggered)
- PBI-043: Session Tracking

#### **Category 13: Dashboard & User Interface (2 features)**
- PBI-044: Live Monitoring Dashboard
- PBI-045: Historical Analytics Dashboard

### 5.2 Priority Classification (MoSCoW Method)

**MUST HAVE (24 features)** - Core MVP for thesis graduation
- All face, eye, head, gaze detection (PBI-001 to PBI-010, excluding PBI-011)
- All drowsiness detection (PBI-012 to PBI-014)
- All distraction detection (PBI-016, PBI-017)
- All 7 dangerous activities + model training (PBI-019 to PBI-026)
- Camera health + FPS monitoring (PBI-034, PBI-037)
- Audio alerts (PBI-038)
- Event logging (PBI-041)
- Live dashboard (PBI-044)

**SHOULD HAVE (17 features)** - Important but not critical
- PERCLOS calculation (PBI-015)
- Attention score (PBI-018)
- Driver enrollment + identification (PBI-027, PBI-028, PBI-029)
- Passenger counting (PBI-030)
- Glasses detection (PBI-032)
- Low light + occlusion detection (PBI-035, PBI-036)
- Visual alerts + priority management (PBI-039, PBI-040)
- Video recording + session tracking (PBI-042, PBI-043)

**COULD HAVE (4 features)** - Nice to have if time permits
- Pupil detection (PBI-011)
- Passenger face detection (PBI-031)
- Mask detection (PBI-033)
- Historical analytics dashboard (PBI-045)

### 5.3 User Stories (48 Stories from 5 Stakeholder Perspectives)

The system addresses needs of multiple stakeholders:

**Driver (10 stories)**: Real-time alerts, feedback display, enrollment, privacy control  
**Fleet Manager (8 stories)**: Behavior dashboard, historical analysis, incident reports, video evidence  
**Safety Engineer (9 stories)**: Threshold configuration, multi-modal validation, performance monitoring  
**Developer (11 stories)**: Modular pipeline, database schema, API design, deployment  
**QA Tester (10 stories)**: Test datasets, accuracy validation, performance testing, edge case handling  

---

## 6. TECHNOLOGY STACK

### 6.1 Hardware Components

| Component | Specification | Purpose | Estimated Cost |
|-----------|--------------|---------|----------------|
| **IR Camera** | 1080p, 60fps, IR night vision, USB interface | Capture driver face video in all lighting | $30-50 |
| **Computing Device** | Jetson Nano (4GB) OR Raspberry Pi 4 (8GB) | Run AI models and processing pipeline | $100-150 |
| **Audio Speaker** | USB speaker or 3.5mm jack | Play audio alerts | $10-20 |
| **Optional: LED Indicators** | RGB LED strip, GPIO-controlled | Visual warning indicators | $5-10 |
| **Optional: Display** | 7-inch HDMI touchscreen | Dashboard interface | $50-80 |
| **Storage** | 128GB+ microSD card or SSD | Store models, database, video clips | $20-40 |

**Total Hardware Budget: ~$200-300**

### 6.2 Software Stack

#### **Programming Language**
- **Python 3.8+**: Primary development language for CV and ML

#### **Computer Vision Libraries**
- **OpenCV 4.5+**: Core image processing, camera interface, drawing overlays
- **dlib 19.22+**: Facial landmark detection (68-point model), face recognition encodings
- **MediaPipe (optional)**: Alternative face mesh detection (468 landmarks)

#### **Deep Learning Frameworks**
- **TensorFlow 2.x** OR **PyTorch 1.10+**: Activity recognition CNN training and inference
- **Keras**: High-level API for model building
- **MobileNetV2** or **EfficientNet**: Lightweight CNN architectures for edge deployment

#### **Machine Learning Models**
- **Face Detection**: dlib HOG detector OR MTCNN OR MediaPipe Face Detection
- **Face Recognition**: dlib face encodings (128D vector) OR FaceNet embeddings
- **Activity Classification**: Custom-trained MobileNetV2 CNN (7 classes)

#### **Database**
- **SQLite**: Lightweight embedded database for local event storage
- **Schema**: Driver table, Session table, Event table, Video metadata table

#### **User Interface**
- **Option A (Lightweight)**: OpenCV HighGUI windows for dashboard display
- **Option B (Advanced)**: Flask + React.js web-based dashboard
- **pygame** or **pydub**: Audio alert playback

#### **Development Tools**
- **Git/GitHub**: Version control and code repository
- **Jupyter Notebook**: Model training experimentation and data analysis
- **pytest**: Unit testing framework
- **Black + flake8**: Code formatting and linting

#### **Deployment & System**
- **Linux (Ubuntu 20.04 or Jetson Linux)**: Operating system for edge device
- **systemd**: Auto-start system service on boot (optional)
- **FFmpeg**: Video encoding for event recording

### 6.3 Pre-trained Models & Datasets

**Pre-trained Models to Use:**
- dlib shape predictor 68 face landmarks model
- dlib face recognition ResNet model
- (Optional) MediaPipe Face Mesh

**Datasets for Activity Recognition Training:**
- **Custom dataset collection**: 300+ samples per activity (7 activities = 2100+ images)
- **Data augmentation**: Rotation, brightness, blur to increase dataset size
- **Public datasets (if available)**: Driver distraction datasets (e.g., State Farm dataset)

---

## 7. EXPECTED OUTCOMES

### 7.1 Deliverables

#### **Primary Deliverables (For Thesis Submission)**

1. **Working Software System**
   - Complete source code repository on GitHub
   - Installation and setup scripts
   - Configuration files for threshold tuning

2. **Trained AI Models**
   - Activity recognition CNN model file (.h5 or .pth)
   - Model training notebooks with hyperparameters
   - Model evaluation reports (accuracy, confusion matrix, precision/recall)

3. **System Documentation**
   - Technical documentation (architecture, API, database schema)
   - User manual with installation and usage instructions
   - Code documentation (docstrings, inline comments)

4. **Testing Artifacts**
   - Test plan document
   - Test cases (minimum 50+ test cases covering all modules)
   - Test execution results and bug reports
   - Performance benchmark results

5. **Project Management Documents**
   - Proposal (this document)
   - Project plan with Gantt chart
   - Product backlog (45 PBIs)
   - User stories (48 stories) with acceptance criteria
   - Sprint backlogs (for each sprint)
   - Meeting minutes (weekly advisor meetings)
   - Reflection document (lessons learned, challenges, future work)

6. **Design Documents**
   - System architecture diagram (component, deployment views)
   - Database schema (ER diagram, table definitions)
   - UI/UX mockups and wireframes

7. **Presentation Materials**
   - Thesis defense slides
   - Demo video (3-5 minutes)
   - Poster (if required)

#### **Demonstration Outputs**

- **Live demo** showing real-time detection on a test driver
- **Video clips** of system detecting various scenarios (drowsiness, distraction, activities)
- **Analytics dashboard** showing historical trip data and event statistics

### 7.2 Performance Targets

| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| **Drowsiness Detection Accuracy** | >90% | Evaluation on labeled test dataset (100+ samples) |
| **Activity Recognition Accuracy** | >85% per activity | Test dataset with 7 activity classes |
| **False Positive Rate (Drowsiness)** | <1 alert per hour | 8-hour real driving test with alert driver |
| **False Positive Rate (Activities)** | <5% | Confusion matrix analysis on test set |
| **System Latency (Detection to Alert)** | <500ms | Timestamp logging and measurement |
| **Real-time Performance (FPS)** | >15 FPS | Frame processing rate monitoring |
| **System Uptime** | >99% | No crashes during 8-hour continuous test |
| **Face Detection Success Rate** | >95% | When driver face is visible and unoccluded |
| **Driver Identification Accuracy** | >95% | Face recognition accuracy on enrolled drivers |

### 7.3 Success Criteria

The project will be considered successful if:

 All MUST HAVE features (24 PBIs) are implemented and working  
 Drowsiness detection achieves >90% accuracy  
 Activity recognition achieves >85% accuracy per class  
 System runs in real-time at >15 FPS on target hardware  
 False positive rate is acceptably low (<1 alert/hour for drowsiness)  
 System is stable with <1% crash rate during extended operation  
 All deliverables (code, docs, tests) are completed and submitted  
 Successful thesis defense with live system demonstration  

### 7.4 Impact & Benefits

**Safety Impact:**
- Reduces risk of accidents caused by drowsiness, distraction, and dangerous behaviors
- Provides immediate warnings to prevent incidents before they occur
- Creates awareness for drivers about their risky behaviors

**Educational Impact:**
- Demonstrates practical application of computer vision and machine learning
- Showcases end-to-end system development from requirements to deployment
- Provides learning experience in real-world problem-solving

**Research Contribution:**
- Comprehensive dataset of dangerous driving activities
- Insights into multi-modal detection (combining head pose, gaze, and activity recognition)
- Open-source implementation for future researchers

**Commercial Potential:**
- Foundation for commercial Driver Monitoring System product
- Applicable to fleet management, ride-sharing, trucking industries
- Scalable to insurance telematics and driver scoring applications

---

## 8. PROJECT TIMELINE

### 8.1 Overall Timeline: 12 Weeks (3 Months)

The project follows an **Agile Scrum** methodology with 5 sprints of 2 weeks each, preceded by 2 weeks of planning.

### 8.2 Phase Breakdown

#### **Phase 1: Initiation & Planning (Week 1-2)**

**Week 1:**
- Literature review on driver monitoring systems
- Review existing solutions and research papers
- Finalize problem statement and objectives
- **Deliverable**: Proposal document (this document)

**Week 2:**
- Create detailed project plan with Gantt chart
- Set up development environment (Python, OpenCV, TensorFlow)
- Acquire hardware (IR camera, Jetson Nano/Raspberry Pi)
- Set up GitHub repository and project structure
- **Deliverable**: Project Plan document

---

#### **Phase 2: Requirements & Design (Week 3-5)**

**Week 3 (Sprint 1 - Part 1):**
- Finalize product backlog (45 PBIs with MoSCoW prioritization)
- Write user stories with acceptance criteria
- Research face detection and landmark extraction methods
- **Deliverable**: Product Backlog, User Stories documents

**Week 4 (Sprint 1 - Part 2):**
- Design system architecture (component diagram, data flow)
- Define processing pipeline modules (face → eye → head → gaze → activity)
- Design database schema (Driver, Session, Event tables)
- **Deliverable**: Architecture Design document

**Week 5 (Sprint 2 - Start):**
- Design UI/UX mockups for dashboard
- Finalize database schema with ER diagram
- Write test plan with test scenarios
- Begin development: Camera integration, face detection module
- **Deliverables**: Database Design, UI/Interface mockups, Test Plan

---

#### **Phase 3: Development (Week 6-9) - 4 Sprints**

**Week 6 (Sprint 2 - Complete):**
- Implement core face and eye detection (PBI-001 to PBI-005)
- Implement head pose estimation (PBI-006 to PBI-008)
- Basic dashboard showing camera feed with overlays
- **Sprint Goal**: Foundation modules working

**Week 7 (Sprint 3 - Start):**
- Implement drowsiness detection (PBI-012 to PBI-014)
- Implement distraction detection (PBI-016, PBI-017)
- Implement audio alert system (PBI-038)
- **Sprint Goal**: Core safety detection features

**Week 8 (Sprint 3 - Complete & Sprint 4 - Start):**
- Collect and label training data for 7 dangerous activities
- Train Activity Recognition CNN (PBI-026)
- Implement activity detection integration (PBI-019 to PBI-025)
- **Sprint Goal**: Activity recognition working

**Week 9 (Sprint 4 - Complete):**
- Implement event logging and database integration (PBI-041, PBI-043)
- Implement driver enrollment and identification (PBI-027, PBI-028)
- Implement system health monitoring (PBI-034, PBI-037)
- Code cleanup and refactoring
- **Sprint Goal**: All MUST HAVE features complete

---

#### **Phase 4: Testing & Closure (Week 10-12)**

**Week 10 (Sprint 5 - Start):**
- Write detailed test cases (50+ cases)
- Execute unit tests for each module
- Integration testing (end-to-end pipeline)
- Performance benchmarking (accuracy, FPS, latency)
- Bug fixing

**Week 11 (Sprint 5 - Complete):**
- System testing with real driving scenarios
- Collect accuracy metrics and performance data
- Implement SHOULD HAVE features if time permits
- Final code review and documentation updates
- **Deliverable**: Test Cases, Test Results

**Week 12 (Final Week):**
- Complete all documentation (User Manual, Technical Docs)
- Write reflection document (lessons learned, challenges)
- Create demo video and presentation slides
- Prepare for thesis defense
- Final submission
- **Deliverables**: Reflection, Presentation, Final Submission

---

### 8.3 Gantt Chart Summary

```
PHASE/TASK                    | W1 | W2 | W3 | W4 | W5 | W6 | W7 | W8 | W9 |W10 |W11 |W12 |
------------------------------|----|----|----|----|----|----|----|----|----|----|----|----|
PHASE 1: PLANNING             |████|████|    |    |    |    |    |    |    |    |    |    |
  Proposal                    |████|    |    |    |    |    |    |    |    |    |    |    |
  Project Plan                |    |████|    |    |    |    |    |    |    |    |    |    |
PHASE 2: REQUIREMENTS         |    |    |████|████|████|    |    |    |    |    |    |    |
  Product Backlog             |    |    |████|    |    |    |    |    |    |    |    |    |
  User Stories                |    |    |████|████|    |    |    |    |    |    |    |    |
  Architecture Design         |    |    |    |████|    |    |    |    |    |    |    |    |
  Database Design             |    |    |    |    |████|    |    |    |    |    |    |    |
  UI Design                   |    |    |    |    |████|    |    |    |    |    |    |    |
PHASE 3: DEVELOPMENT          |    |    |    |    |████|████|████|████|████|    |    |    |
  Sprint 2: Foundation        |    |    |    |    |████|████|    |    |    |    |    |    |
  Sprint 3: Core Detection    |    |    |    |    |    |    |████|████|    |    |    |    |
  Sprint 4: Activities        |    |    |    |    |    |    |    |████|████|    |    |    |
PHASE 4: TESTING              |    |    |    |    |    |    |    |    |    |████|████|    |
  Test Cases & Execution      |    |    |    |    |    |    |    |    |    |████|████|    |
  Bug Fixing                  |    |    |    |    |    |    |    |    |    |████|████|    |
CLOSURE                       |    |    |    |    |    |    |    |    |    |    |    |████|
  Documentation               |    |    |    |    |    |    |    |    |    |    |████|████|
  Reflection                  |    |    |    |    |    |    |    |    |    |    |    |████|
  Defense Preparation         |    |    |    |    |    |    |    |    |    |    |    |████|
```

### 8.4 Milestones

| Milestone | Deadline | Criteria |
|-----------|----------|----------|
| **M1: Proposal Approved** | End of Week 1 | Advisor approval of project scope |
| **M2: Architecture Complete** | End of Week 4 | System design finalized and reviewed |
| **M3: Foundation Working** | End of Week 6 | Face, eye, head detection modules operational |
| **M4: Core Detection Complete** | End of Week 8 | Drowsiness and distraction detection working |
| **M5: All MUST HAVEs Done** | End of Week 9 | All 24 critical features implemented |
| **M6: Testing Complete** | End of Week 11 | All test cases executed, metrics collected |
| **M7: Project Submission** | End of Week 12 | All deliverables submitted |

---

## 9. SUCCESS CRITERIA

### 9.1 Technical Success Criteria

| Category | Criterion | Measurement |
|----------|-----------|-------------|
| **Functionality** | All 24 MUST HAVE features implemented | Feature checklist |
| **Accuracy** | Drowsiness detection >90% accuracy | Test dataset evaluation |
| **Accuracy** | Activity recognition >85% per class | Test dataset evaluation |
| **Performance** | Real-time processing >15 FPS | FPS monitoring |
| **Performance** | Detection-to-alert latency <500ms | Timestamp analysis |
| **Reliability** | System uptime >99% (8-hour test) | Crash rate monitoring |
| **Reliability** | False positive rate <1 alert/hour | Long-term testing |
| **Usability** | Dashboard clearly shows driver state | User testing feedback |

### 9.2 Project Management Success Criteria

 All deliverables completed on time (13 documents + working system)  
 Code repository well-organized with clear README  
 All code tested with >70% code coverage  
 Weekly advisor meetings attended with minutes documented  
 Project stays within budget (~$300 hardware)  

### 9.3 Academic Success Criteria

 Thesis defense presentation successfully delivered  
 Live system demonstration during defense (no critical bugs)  
 All questions from thesis committee answered satisfactorily  
 Grade: Minimum "Good" (≥7.0/10) or institutional equivalent  
 Recommendation for publication/competition (bonus achievement)  

### 9.4 Risk Mitigation

**Primary Risks & Mitigation Strategies:**

**Risk 1: Activity recognition accuracy too low**
- Mitigation: Collect larger and more diverse training dataset (300+ samples per class)
- Contingency: Reduce to 5 most important activities if 7 is too challenging

**Risk 2: Real-time performance not achieved on Raspberry Pi**
- Mitigation: Optimize models (use MobileNetV2, reduce frame resolution)
- Contingency: Upgrade to Jetson Nano (more powerful GPU)

**Risk 3: Hardware delays (IR camera or computing device not delivered)**
- Mitigation: Order early (Week 2), have backup suppliers
- Contingency: Use standard webcam temporarily, simulate with pre-recorded videos

**Risk 4: Drowsiness detection has too many false positives**
- Mitigation: Implement multi-signal fusion (EAR + PERCLOS + yawning)
- Contingency: Add per-driver calibration to tune thresholds

**Risk 5: Time constraints - cannot complete all features**
- Mitigation: Strict prioritization (MUST HAVE first), weekly progress tracking
- Contingency: Clearly document completed vs. future work; focus on quality over quantity

---

## 10. REFERENCES

### 10.1 Academic Papers

1. Soukupová, T., & Čech, J. (2016). "Real-Time Eye Blink Detection using Facial Landmarks." 21st Computer Vision Winter Workshop.
   - *Eye Aspect Ratio (EAR) method for drowsiness detection*

2. Chirra, V. R., et al. (2019). "Deep CNN: A Machine Learning Approach for Driver Drowsiness Detection Based on Eye State." Rev. d'Intelligence Artif., 33(6), 461-466.
   - *Deep learning approaches for drowsiness monitoring*

3. Dua, M., et al. (2021). "Deep CNN models-based ensemble approach to driver drowsiness detection." Neural Computing and Applications, 33, 3155-3168.
   - *Ensemble methods for improved accuracy*

4. Dwivedi, K., et al. (2014). "Driver Drowsiness Detection using Representation Learning." IEEE Intelligent Transportation Systems.
   - *Feature learning for drowsiness indicators*

5. Jabbar, R., et al. (2018). "Real-time Driver Drowsiness Detection for Android Application Using Deep Neural Networks Techniques." Procedia Computer Science, 130, 400-407.
   - *Mobile implementation considerations*

6. Liu, W., et al. (2019). "Driver Distraction Detection Based on Vehicle Dynamics Using Naturalistic Driving Data." IEEE Transactions on Intelligent Transportation Systems.
   - *Multi-modal distraction detection approaches*

7. Sandler, M., et al. (2018). "MobileNetV2: Inverted Residuals and Linear Bottlenecks." IEEE/CVF CVPR.
   - *Lightweight CNN architecture for edge devices*

### 10.2 Technical Resources

8. OpenCV Documentation: https://docs.opencv.org/
   - *Computer vision library documentation*

9. dlib C++ Library: http://dlib.net/
   - *Facial landmark detection and face recognition*

10. TensorFlow Documentation: https://www.tensorflow.org/
    - *Deep learning framework*

11. PyTorch Documentation: https://pytorch.org/
    - *Alternative deep learning framework*

### 10.3 Datasets

12. State Farm Distracted Driver Detection Dataset (Kaggle)
    - *Public dataset for driver activity classification*

13. NTHUDDD (National Tsing Hua University Driver Drowsiness Detection Dataset)
    - *Research dataset for drowsiness detection*

14. UTA-RLDD (UTA Real-Life Drowsiness Dataset)
    - *Real-world drowsiness video dataset*

### 10.4 Standards & Guidelines

15. ISO 15007-1:2014 - Road vehicles — Measurement of driver visual behaviour
    - *Industry standards for driver monitoring systems*

16. NHTSA Visual-Manual Distraction Guidelines
    - *US transportation safety guidelines*

---

## APPENDICES

### Appendix A: Product Backlog Summary (45 PBIs)

See detailed brainstorming session document for complete Product Backlog:
`_bmad-output/brainstorming/brainstorming-session-2026-03-03-004815.md`

**MoSCoW Summary:**
- **MUST HAVE**: 24 features (Core detection, activities, alerts, logging, dashboard)
- **SHOULD HAVE**: 17 features (Enrollment, passengers, system health, video recording)
- **COULD HAVE**: 4 features (Advanced analytics, mask detection, passenger details)
- **WON'T HAVE**: Safety belt detection (removed from scope)

### Appendix B: User Stories Summary (48 Stories)

**Stakeholder Breakdown:**
- Driver: 10 stories (alerts, feedback, enrollment, privacy)
- Fleet Manager: 8 stories (dashboards, reports, video evidence)
- Safety Engineer: 9 stories (configuration, validation, testing)
- Developer: 11 stories (architecture, database, API, deployment)
- QA Tester: 10 stories (test datasets, accuracy, performance)

See full user stories with acceptance criteria in brainstorming session document.

### Appendix C: Technology Decision Matrix

| Technology Choice | Option A | Option B | Selected | Rationale |
|-------------------|----------|----------|----------|-----------|
| **Computing Device** | Jetson Nano | Raspberry Pi 4 | Jetson Nano | Better GPU for CNN inference |
| **DL Framework** | TensorFlow | PyTorch | TensorFlow | Better mobile/edge support (TFLite) |
| **Face Detection** | dlib HOG | MediaPipe | dlib | Proven accuracy, easier integration |
| **Database** | SQLite | PostgreSQL | SQLite | Lightweight, embedded, sufficient for single device |
| **Dashboard UI** | OpenCV GUI | Flask + React | TBD Week 5 | Depends on time constraints |

### Appendix D: Contact Information

**Student:**  
Name: Hung Thanh  
Email: [student-email]  
GitHub: [github-username]  

**Advisor:**  
Name: [Advisor Name]  
Email: [advisor-email]  
Office: [Office Location]  
Meeting Schedule: [Day/Time]  

---

## APPROVAL

**Student Signature:** _____________________ Date: ___________

**Advisor Signature:** _____________________ Date: ___________

---

**END OF PROPOSAL**

---

**Document Information:**
- **File Name:** PROPOSAL-Driver-Monitoring-System.md
- **Version:** 1.0
- **Created:** March 4, 2026
- **Total Pages:** ~18 pages (estimated when converted to PDF)
- **Word Count:** ~7,500 words
