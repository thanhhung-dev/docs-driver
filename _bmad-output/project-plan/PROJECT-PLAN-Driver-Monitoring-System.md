# PROJECT PLAN
## Driver Monitoring System using Computer Vision & AI

---

**Project Name:** Driver Monitoring System (DMS)  
**Project Manager / Student:** Hung Thanh  
**Advisor:** [Advisor Name]  
**Start Date:** March 4, 2026  
**Target Completion Date:** May 27, 2026  
**Duration:** 12 weeks (84 days)  
**Project Type:** Undergraduate Thesis / Capstone Project  
**Status:** Planning Phase

---

## TABLE OF CONTENTS

1. [Executive Summary](#1-executive-summary)
2. [Project Organization](#2-project-organization)
3. [Work Breakdown Structure (WBS)](#3-work-breakdown-structure-wbs)
4. [Detailed Schedule & Gantt Chart](#4-detailed-schedule--gantt-chart)
5. [Sprint Planning (Agile Scrum)](#5-sprint-planning-agile-scrum)
6. [Resource Allocation](#6-resource-allocation)
7. [Risk Management Plan](#7-risk-management-plan)
8. [Quality Management Plan](#8-quality-management-plan)
9. [Communication Plan](#9-communication-plan)
10. [Budget & Cost Estimation](#10-budget--cost-estimation)
11. [Milestones & Deliverables](#11-milestones--deliverables)
12. [Success Metrics](#12-success-metrics)
13. [Assumptions & Constraints](#13-assumptions--constraints)

---

## 1. EXECUTIVE SUMMARY

### 1.1 Project Overview

The Driver Monitoring System (DMS) project aims to develop an AI-powered real-time driver safety monitoring system using computer vision and machine learning. The system will detect drowsiness, distraction, and dangerous driving activities, providing immediate alerts to prevent accidents.

### 1.2 Project Goals

- Develop working prototype system with 24+ core features
- Achieve >90% accuracy for drowsiness detection
- Achieve >85% accuracy for activity recognition
- Process video in real-time (>15 FPS)
- Complete all 13 thesis deliverables on time

### 1.3 Project Approach

The project follows **Agile Scrum methodology** with:
- 5 sprints of 2 weeks each (after 2-week planning phase)
- Weekly advisor meetings for guidance and review
- Iterative development with continuous testing
- Risk-driven prioritization (MUST HAVE features first)

### 1.4 Key Success Factors

✅ Clear prioritization using MoSCoW method (24 MUST HAVE features)  
✅ Early hardware acquisition to avoid delays  
✅ Incremental development with continuous integration  
✅ Regular advisor feedback and course correction  
✅ Comprehensive testing throughout development  
✅ Realistic timeline with buffer for unexpected issues  

---

## 2. PROJECT ORGANIZATION

### 2.1 Project Roles & Responsibilities

| Role | Name | Responsibilities | Time Commitment |
|------|------|------------------|-----------------|
| **Student / Developer** | Hung Thanh | - All development tasks<br>- System design & architecture<br>- Model training & testing<br>- Documentation<br>- Presentation preparation | Full-time (40h/week) |
| **Thesis Advisor** | [Advisor Name] | - Provide technical guidance<br>- Review deliverables<br>- Approve major decisions<br>- Evaluate final thesis | 2 hours/week (meetings) |
| **Thesis Committee** | [Committee Members] | - Evaluate proposal<br>- Review final thesis<br>- Attend defense presentation | Defense day only |

### 2.2 Stakeholders

| Stakeholder | Interest | Influence | Engagement Strategy |
|-------------|----------|-----------|---------------------|
| **Thesis Advisor** | Project success, quality | High | Weekly meetings, regular updates |
| **Thesis Committee** | Academic rigor, innovation | High | Formal presentations (proposal, defense) |
| **University Department** | Timely graduation | Medium | Submit deliverables on time |
| **Potential Users** | System usability, accuracy | Low | User testing feedback (Week 10-11) |

### 2.3 Communication Structure

```
┌─────────────────┐
│ Thesis Advisor  │
│  (Weekly Meet)  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Hung Thanh     │
│  (Developer)    │
└────────┬────────┘
         │
         ├──► Thesis Committee (Proposal & Defense)
         ├──► Peer Reviewers (Code review)
         └──► Test Users (Feedback)
```

---

## 3. WORK BREAKDOWN STRUCTURE (WBS)

### 3.1 WBS Hierarchy

```
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
│   ├── 2.1 Product Backlog Creation
│   │   ├── 2.1.1 Identify all features (45 PBIs)
│   │   ├── 2.1.2 MoSCoW prioritization
│   │   └── 2.1.3 Document Product Backlog
│   ├── 2.2 User Stories Development
│   │   ├── 2.2.1 Write User Stories (48 stories)
│   │   ├── 2.2.2 Define Acceptance Criteria (72 criteria)
│   │   └── 2.2.3 Validate with Advisor
│   └── 2.3 Requirements Validation
│       └── 2.3.1 Requirements Review Meeting
│
├── 3.0 SYSTEM DESIGN (Week 4-5)
│   ├── 3.1 Architecture Design
│   │   ├── 3.1.1 Define System Components
│   │   ├── 3.1.2 Create Component Diagram
│   │   ├── 3.1.3 Define Data Flow
│   │   ├── 3.1.4 Create Sequence Diagrams
│   │   └── 3.1.5 Define Processing Pipeline
│   ├── 3.2 Database Design
│   │   ├── 3.2.1 Define Entity-Relationship Model
│   │   ├── 3.2.2 Create ER Diagram
│   │   ├── 3.2.3 Define Table Schemas
│   │   ├── 3.2.4 Design Indexes & Relationships
│   │   └── 3.2.5 Document Database Design
│   └── 3.3 UI/Interface Design
│       ├── 3.3.1 Create Wireframes
│       ├── 3.3.2 Design Dashboard Layout
│       ├── 3.3.3 Define User Interactions
│       └── 3.3.4 Document UI Specifications
│
├── 4.0 DEVELOPMENT SETUP (Week 2-3)
│   ├── 4.1 Environment Setup
│   │   ├── 4.1.1 Install Python & Dependencies
│   │   ├── 4.1.2 Setup OpenCV, dlib, TensorFlow
│   │   ├── 4.1.3 Configure Development Tools
│   │   └── 4.1.4 Setup Virtual Environment
│   ├── 4.2 Hardware Setup
│   │   ├── 4.2.1 Acquire IR Camera
│   │   ├── 4.2.2 Acquire Jetson Nano / Raspberry Pi
│   │   ├── 4.2.3 Setup & Test Hardware
│   │   └── 4.2.4 Integrate Camera with System
│   └── 4.3 Project Structure
│       ├── 4.3.1 Create GitHub Repository
│       ├── 4.3.2 Setup Project Folder Structure
│       ├── 4.3.3 Initialize Git Version Control
│       └── 4.3.4 Setup CI/CD (Optional)
│
├── 5.0 CORE DEVELOPMENT (Week 5-9)
│   ├── 5.1 Sprint 2: Foundation (Week 5-6)
│   │   ├── 5.1.1 Camera Integration Module
│   │   ├── 5.1.2 Face Detection Module (PBI-001)
│   │   ├── 5.1.3 Eye Detection Module (PBI-002, PBI-003)
│   │   ├── 5.1.4 Head Pose Estimation (PBI-006, PBI-007)
│   │   ├── 5.1.5 Gaze Tracking Module (PBI-009, PBI-010)
│   │   └── 5.1.6 Basic Dashboard UI (PBI-044)
│   ├── 5.2 Sprint 3: Detection Algorithms (Week 7-8)
│   │   ├── 5.2.1 Drowsiness Detection (PBI-012, PBI-013, PBI-014)
│   │   ├── 5.2.2 Distraction Detection (PBI-016, PBI-017)
│   │   ├── 5.2.3 Attention Score Calculation (PBI-018)
│   │   ├── 5.2.4 Audio Alert System (PBI-038)
│   │   └── 5.2.5 Integration Testing
│   └── 5.3 Sprint 4: Activity Recognition (Week 8-9)
│       ├── 5.3.1 Collect Training Dataset (7 activities)
│       ├── 5.3.2 Label Training Data
│       ├── 5.3.3 Data Augmentation
│       ├── 5.3.4 Train Activity CNN Model (PBI-026)
│       ├── 5.3.5 Model Evaluation & Tuning
│       ├── 5.3.6 Activity Detection Integration (PBI-019 to PBI-025)
│       └── 5.3.7 Test Activity Recognition
│
├── 6.0 ADVANCED FEATURES (Week 9)
│   ├── 6.1 Database Integration
│   │   ├── 6.1.1 Implement Database Schema
│   │   ├── 6.1.2 Event Logging Module (PBI-041)
│   │   ├── 6.1.3 Session Tracking Module (PBI-043)
│   │   └── 6.1.4 Video Recording Module (PBI-042)
│   ├── 6.2 Driver Identification
│   │   ├── 6.2.1 Face Enrollment Module (PBI-027)
│   │   ├── 6.2.2 Face Recognition Module (PBI-028)
│   │   └── 6.2.3 Multi-Driver Support (PBI-029)
│   └── 6.3 System Monitoring
│       ├── 6.3.1 Camera Health Check (PBI-034)
│       ├── 6.3.2 FPS Monitoring (PBI-037)
│       └── 6.3.3 System Status Display
│
├── 7.0 TESTING (Week 10-11)
│   ├── 7.1 Test Planning
│   │   ├── 7.1.1 Create Test Plan Document
│   │   ├── 7.1.2 Define Test Scenarios
│   │   └── 7.1.3 Prepare Test Datasets
│   ├── 7.2 Test Case Development
│   │   ├── 7.2.1 Write Unit Test Cases (50+ cases)
│   │   ├── 7.2.2 Write Integration Test Cases
│   │   └── 7.2.3 Write System Test Cases
│   ├── 7.3 Test Execution
│   │   ├── 7.3.1 Execute Unit Tests
│   │   ├── 7.3.2 Execute Integration Tests
│   │   ├── 7.3.3 Execute System Tests
│   │   └── 7.3.4 Real-World Testing (8-hour drive)
│   ├── 7.4 Performance Testing
│   │   ├── 7.4.1 Accuracy Benchmarking (Drowsiness)
│   │   ├── 7.4.2 Accuracy Benchmarking (Activities)
│   │   ├── 7.4.3 FPS Performance Testing
│   │   ├── 7.4.4 Latency Testing
│   │   └── 7.4.5 False Positive Rate Analysis
│   └── 7.5 Bug Fixing
│       ├── 7.5.1 Log & Prioritize Bugs
│       ├── 7.5.2 Fix Critical Bugs
│       └── 7.5.3 Regression Testing
│
├── 8.0 DOCUMENTATION (Week 1-12, Ongoing)
│   ├── 8.1 Project Documents
│   │   ├── 8.1.1 Proposal (Week 1)
│   │   ├── 8.1.2 Project Plan (Week 2)
│   │   ├── 8.1.3 Product Backlog (Week 3)
│   │   ├── 8.1.4 User Stories (Week 3-4)
│   │   ├── 8.1.5 Architecture Design (Week 4)
│   │   ├── 8.1.6 Database Design (Week 5)
│   │   ├── 8.1.7 UI/Interface Design (Week 5)
│   │   ├── 8.1.8 Sprint Backlogs (Week 5-10)
│   │   ├── 8.1.9 Code Standard (Week 6)
│   │   ├── 8.1.10 Test Plan (Week 5)
│   │   ├── 8.1.11 Test Cases (Week 10)
│   │   ├── 8.1.12 Meeting Minutes (Weekly)
│   │   └── 8.1.13 Reflection (Week 12)
│   ├── 8.2 Technical Documentation
│   │   ├── 8.2.1 API Documentation
│   │   ├── 8.2.2 Database Documentation
│   │   ├── 8.2.3 Code Documentation (Docstrings)
│   │   └── 8.2.4 System Manual
│   └── 8.3 User Documentation
│       ├── 8.3.1 Installation Guide
│       ├── 8.3.2 User Manual
│       └── 8.3.3 Troubleshooting Guide
│
└── 9.0 CLOSURE & PRESENTATION (Week 12)
    ├── 9.1 Final System Polish
    │   ├── 9.1.1 Code Cleanup & Refactoring
    │   ├── 9.1.2 Final Testing
    │   └── 9.1.3 Performance Optimization
    ├── 9.2 Presentation Preparation
    │   ├── 9.2.1 Create Defense Slides
    │   ├── 9.2.2 Prepare Demo Video
    │   ├── 9.2.3 Rehearse Presentation
    │   └── 9.2.4 Setup Demo Environment
    ├── 9.3 Final Submission
    │   ├── 9.3.1 Compile All Documents
    │   ├── 9.3.2 Finalize Thesis Report
    │   ├── 9.3.3 Submit to Committee
    │   └── 9.3.4 Archive Project Files
    └── 9.4 Thesis Defense
        ├── 9.4.1 Present to Committee
        ├── 9.4.2 Live System Demo
        └── 9.4.3 Q&A Session
```

### 3.2 WBS Summary Statistics

| Category | Work Packages | Estimated Hours |
|----------|--------------|-----------------|
| Project Management | 13 tasks | 60 hours |
| Requirements | 7 tasks | 40 hours |
| Design | 14 tasks | 60 hours |
| Development Setup | 12 tasks | 30 hours |
| Core Development | 25 tasks | 200 hours |
| Advanced Features | 10 tasks | 60 hours |
| Testing | 15 tasks | 80 hours |
| Documentation | 22 tasks | 80 hours |
| Closure | 11 tasks | 40 hours |
| **TOTAL** | **129 tasks** | **650 hours** |

**Effort Distribution:**
- Development: 40% (260 hours)
- Testing: 12% (80 hours)
- Documentation: 22% (140 hours)
- Design: 9% (60 hours)
- Management: 9% (60 hours)
- Setup & Other: 8% (50 hours)

---

## 4. DETAILED SCHEDULE & GANTT CHART

### 4.1 12-Week Timeline Overview

| Week | Phase | Focus | Key Deliverables |
|------|-------|-------|------------------|
| **W1** | Planning | Problem definition, proposal | Proposal Document |
| **W2** | Planning | Project planning, setup | Project Plan, GitHub repo, hardware ordered |
| **W3** | Requirements | Product backlog, start Sprint 1 | Product Backlog |
| **W4** | Requirements | User stories, architecture | User Stories, Architecture Design |
| **W5** | Design + Sprint 2 | Database, UI design, foundation dev | Database Design, UI Mockups, Foundation modules |
| **W6** | Sprint 2 | Core detection modules | Face, eye, head, gaze modules working |
| **W7** | Sprint 3 | Safety detection algorithms | Drowsiness & distraction detection |
| **W8** | Sprint 3 + 4 | Activity recognition | Dataset collection, model training |
| **W9** | Sprint 4 | Advanced features | Database integration, driver ID, activities working |
| **W10** | Sprint 5 | Testing & bug fixing | Test Plan, Test Cases, bug fixes |
| **W11** | Sprint 5 | Testing & polish | Test results, performance benchmarks |
| **W12** | Closure | Documentation & defense prep | All docs complete, presentation ready |

### 4.2 Detailed Gantt Chart

```
TASK / DELIVERABLE                    | W1 | W2 | W3 | W4 | W5 | W6 | W7 | W8 | W9 |W10 |W11 |W12 |
--------------------------------------|----|----|----|----|----|----|----|----|----|----|----|----|
════════════════════════════════════════════════════════════════════════════════════════════════
PHASE 1: PLANNING
────────────────────────────────────────────────────────────────────────────────────────────────
Proposal Document                     |████|    |    |    |    |    |    |    |    |    |    |    |
Project Plan Document                 |    |████|    |    |    |    |    |    |    |    |    |    |
Literature Review                     |████|████|    |    |    |    |    |    |    |    |    |    |
Hardware Acquisition                  |    |████|████|    |    |    |    |    |    |    |    |    |
Development Environment Setup         |    |████|████|    |    |    |    |    |    |    |    |    |
GitHub Repository Setup               |    |████|    |    |    |    |    |    |    |    |    |    |
────────────────────────────────────────────────────────────────────────────────────────────────
PHASE 2: REQUIREMENTS & DESIGN
────────────────────────────────────────────────────────────────────────────────────────────────
Product Backlog (45 PBIs)             |    |    |████|    |    |    |    |    |    |    |    |    |
User Stories (48 stories)             |    |    |████|████|    |    |    |    |    |    |    |    |
Acceptance Criteria (72 criteria)     |    |    |    |████|    |    |    |    |    |    |    |    |
System Architecture Design            |    |    |    |████|████|    |    |    |    |    |    |    |
Database Schema Design                |    |    |    |    |████|    |    |    |    |    |    |    |
UI/Interface Mockups                  |    |    |    |    |████|    |    |    |    |    |    |    |
Test Plan Document                    |    |    |    |    |████|    |    |    |    |    |    |    |
────────────────────────────────────────────────────────────────────────────────────────────────
PHASE 3: DEVELOPMENT (5 Sprints)
────────────────────────────────────────────────────────────────────────────────────────────────
Sprint 2: Foundation (2 weeks)        |    |    |    |    |████|████|    |    |    |    |    |    |
  - Camera Integration                |    |    |    |    |████|    |    |    |    |    |    |    |
  - Face Detection (PBI-001)          |    |    |    |    |████|████|    |    |    |    |    |    |
  - Eye Detection (PBI-002, 003)      |    |    |    |    |    |████|    |    |    |    |    |    |
  - Head Pose (PBI-006, 007)          |    |    |    |    |    |████|    |    |    |    |    |    |
  - Gaze Tracking (PBI-009, 010)      |    |    |    |    |    |████|    |    |    |    |    |    |
  - Basic Dashboard (PBI-044)         |    |    |    |    |    |████|    |    |    |    |    |    |
Sprint 3: Core Detection (2 weeks)    |    |    |    |    |    |    |████|████|    |    |    |    |
  - Drowsiness Detection              |    |    |    |    |    |    |████|    |    |    |    |    |
  - Distraction Detection             |    |    |    |    |    |    |████|    |    |    |    |    |
  - Audio Alert System                |    |    |    |    |    |    |    |████|    |    |    |    |
  - Integration Testing               |    |    |    |    |    |    |    |████|    |    |    |    |
Sprint 4: Activity Recognition        |    |    |    |    |    |    |    |████|████|    |    |    |
  - Dataset Collection                |    |    |    |    |    |    |    |████|    |    |    |    |
  - Data Labeling & Augmentation      |    |    |    |    |    |    |    |████|    |    |    |    |
  - CNN Model Training                |    |    |    |    |    |    |    |    |████|    |    |    |
  - Activity Integration (7 types)    |    |    |    |    |    |    |    |    |████|    |    |    |
  - Database Integration              |    |    |    |    |    |    |    |    |████|    |    |    |
  - Driver Identification             |    |    |    |    |    |    |    |    |████|    |    |    |
Sprint 5: Testing & Polish (2 weeks)  |    |    |    |    |    |    |    |    |    |████|████|    |
  - Test Cases Writing                |    |    |    |    |    |    |    |    |    |████|    |    |
  - Unit Testing                      |    |    |    |    |    |    |    |    |    |████|    |    |
  - Integration Testing               |    |    |    |    |    |    |    |    |    |████|    |    |
  - Performance Benchmarking          |    |    |    |    |    |    |    |    |    |    |████|    |
  - Bug Fixing                        |    |    |    |    |    |    |    |    |    |████|████|    |
Code Standard Document                |    |    |    |    |    |████|    |    |    |    |    |    |
Sprint Backlog Updates                |    |    |    |    |████|████|████|████|████|████|    |    |
────────────────────────────────────────────────────────────────────────────────────────────────
PHASE 4: TESTING & CLOSURE
────────────────────────────────────────────────────────────────────────────────────────────────
Test Cases Document                   |    |    |    |    |    |    |    |    |    |████|    |    |
Test Execution & Results              |    |    |    |    |    |    |    |    |    |████|████|    |
Real-World Testing (8-hour drive)     |    |    |    |    |    |    |    |    |    |    |████|    |
Performance Metrics Collection        |    |    |    |    |    |    |    |    |    |    |████|    |
Final Code Cleanup                    |    |    |    |    |    |    |    |    |    |    |████|    |
────────────────────────────────────────────────────────────────────────────────────────────────
DOCUMENTATION (Ongoing)
────────────────────────────────────────────────────────────────────────────────────────────────
Weekly Meeting Minutes                |████|████|████|████|████|████|████|████|████|████|████|████|
Code Documentation (Docstrings)       |    |    |    |    |████|████|████|████|████|████|████|    |
Technical Documentation               |    |    |    |    |    |    |    |    |    |    |████|████|
User Manual                           |    |    |    |    |    |    |    |    |    |    |████|████|
Reflection Document                   |    |    |    |    |    |    |    |    |    |    |    |████|
────────────────────────────────────────────────────────────────────────────────────────────────
PRESENTATION & DEFENSE
────────────────────────────────────────────────────────────────────────────────────────────────
Defense Slides Preparation            |    |    |    |    |    |    |    |    |    |    |    |████|
Demo Video Creation                   |    |    |    |    |    |    |    |    |    |    |    |████|
Presentation Rehearsal                |    |    |    |    |    |    |    |    |    |    |    |████|
Final Submission                      |    |    |    |    |    |    |    |    |    |    |    |████|
Thesis Defense                        |    |    |    |    |    |    |    |    |    |    |    | ⚡ |
════════════════════════════════════════════════════════════════════════════════════════════════
```

### 4.3 Critical Path Analysis

**Critical Path (Cannot be delayed):**
```
Proposal → Project Plan → Architecture Design → Foundation Dev (Sprint 2) 
→ Core Detection (Sprint 3) → Activity Recognition (Sprint 4) 
→ Testing (Sprint 5) → Defense
```

**Duration:** 12 weeks  
**Float:** 0 days (no buffer in critical path tasks)

**Parallel Activities (Can run concurrently):**
- Documentation can happen alongside development
- Test case writing can start while development continues
- Dataset collection can overlap with other Sprint 4 tasks

---

## 5. SPRINT PLANNING (AGILE SCRUM)

### 5.1 Sprint Structure

Each sprint follows this structure:
- **Duration:** 2 weeks (10 working days)
- **Sprint Planning:** Day 1 (define goals, select PBIs)
- **Daily Work:** Day 2-9 (development, testing)
- **Sprint Review:** Day 10 AM (demo to advisor)
- **Sprint Retrospective:** Day 10 PM (lessons learned)

### 5.2 Sprint 2: Foundation (Week 5-6)

**Sprint Goal:** Build foundational detection modules (face, eye, head, gaze)

**Sprint Backlog:**

| PBI | Task | Priority | Estimated Effort | Assigned To |
|-----|------|----------|------------------|-------------|
| PBI-001 | Face Detection & Tracking | MUST | 8 hours | Hung Thanh |
| PBI-002 | Eye Region Detection | MUST | 6 hours | Hung Thanh |
| PBI-003 | Eye Openness Detection (EAR) | MUST | 8 hours | Hung Thanh |
| PBI-004 | Blink Frequency Monitoring | MUST | 4 hours | Hung Thanh |
| PBI-005 | Eye Location Tracking | MUST | 4 hours | Hung Thanh |
| PBI-006 | Head Pose Estimation | MUST | 10 hours | Hung Thanh |
| PBI-007 | Head Location Tracking | MUST | 4 hours | Hung Thanh |
| PBI-009 | Gaze Direction Estimation | MUST | 10 hours | Hung Thanh |
| PBI-010 | Gaze Zone Classification | MUST | 6 hours | Hung Thanh |
| PBI-044 | Basic Live Dashboard | MUST | 10 hours | Hung Thanh |
| - | Integration & Testing | - | 10 hours | Hung Thanh |
| **TOTAL** | **10 PBIs + Integration** | - | **80 hours** | - |

**Definition of Done (Sprint 2):**
- [ ] Face detected and tracked in real-time video
- [ ] Eye regions identified with EAR calculated
- [ ] Head pose (pitch, yaw, roll) estimated
- [ ] Gaze direction computed and classified into zones
- [ ] Dashboard displays camera feed with overlays
- [ ] All modules have unit tests
- [ ] Code reviewed and documented
- [ ] Demo prepared for advisor review

### 5.3 Sprint 3: Core Detection (Week 7-8)

**Sprint Goal:** Implement drowsiness and distraction detection with alerts

**Sprint Backlog:**

| PBI | Task | Priority | Estimated Effort |
|-----|------|----------|------------------|
| PBI-012 | Drowsiness Detection (EAR-based) | MUST | 8 hours |
| PBI-013 | Yawning Detection | MUST | 6 hours |
| PBI-014 | Microsleep Detection | MUST | 4 hours |
| PBI-016 | Head Turn Distraction | MUST | 6 hours |
| PBI-017 | Gaze-off-Road Detection | MUST | 6 hours |
| PBI-018 | Attention Score Calculation | SHOULD | 6 hours |
| PBI-038 | Real-time Audio Alerts | MUST | 8 hours |
| PBI-040 | Alert Priority Management | SHOULD | 4 hours |
| - | Threshold Tuning & Testing | - | 16 hours |
| - | Integration Testing | - | 16 hours |
| **TOTAL** | **8 PBIs + Testing** | - | **80 hours** |

**Definition of Done (Sprint 3):**
- [ ] Drowsiness detected via EAR, yawning, microsleep
- [ ] Distraction detected via head pose and gaze
- [ ] Audio alerts trigger correctly
- [ ] False positive rate <10% in preliminary testing
- [ ] Thresholds documented (EAR < 0.25, head yaw >45°, etc.)
- [ ] Integration with Sprint 2 modules successful
- [ ] Performance >15 FPS maintained

### 5.4 Sprint 4: Activity Recognition (Week 8-9)

**Sprint Goal:** Train and integrate activity recognition CNN for 7 dangerous activities

**Sprint Backlog:**

| PBI/Task | Description | Priority | Estimated Effort |
|----------|-------------|----------|------------------|
| - | Collect Training Dataset (300+ samples/activity) | MUST | 20 hours |
| - | Label Training Data (2100+ images) | MUST | 10 hours |
| - | Data Augmentation | MUST | 4 hours |
| PBI-026 | Train Activity CNN Model (MobileNetV2) | MUST | 16 hours |
| - | Model Evaluation & Hyperparameter Tuning | MUST | 8 hours |
| PBI-019 | Phone Calling Detection Integration | MUST | 2 hours |
| PBI-020 | Drinking Detection Integration | MUST | 2 hours |
| PBI-021 | Smoking Detection Integration | MUST | 2 hours |
| PBI-022 | Yawning Activity Detection | MUST | 2 hours |
| PBI-023 | Hands Off Wheel Detection | MUST | 2 hours |
| PBI-024 | Arm Out Window Detection | MUST | 2 hours |
| PBI-025 | Looking at Directions Detection | MUST | 2 hours |
| PBI-041 | Event Logging to Database | MUST | 6 hours |
| PBI-043 | Session Tracking | MUST | 4 hours |
| **TOTAL** | **13 PBIs/Tasks** | - | **82 hours** |

**Definition of Done (Sprint 4):**
- [ ] CNN model achieves >85% accuracy per activity
- [ ] All 7 activities integrated and detectable in real-time
- [ ] Events logged to SQLite database
- [ ] Driving sessions tracked with timestamps
- [ ] Model inference time <30ms per frame
- [ ] Confusion matrix analyzed, no cross-confusion >15%

### 5.5 Sprint 5: Testing & Polish (Week 10-11)

**Sprint Goal:** Comprehensive testing, bug fixing, and system polish

**Sprint Backlog:**

| Task Category | Specific Tasks | Estimated Effort |
|---------------|----------------|------------------|
| **Test Planning** | Write test plan, define scenarios | 8 hours |
| **Test Cases** | Write 50+ test cases (unit, integration, system) | 12 hours |
| **Unit Testing** | Test each module individually | 12 hours |
| **Integration Testing** | Test end-to-end pipeline | 12 hours |
| **Performance Testing** | Accuracy, FPS, latency benchmarks | 10 hours |
| **Real-World Testing** | 8-hour driving test, collect metrics | 8 hours |
| **Bug Fixing** | Fix critical and high-priority bugs | 20 hours |
| **Optimization** | Improve performance, reduce false positives | 8 hours |
| **Documentation** | Update technical docs, user manual | 10 hours |
| **TOTAL** | - | **100 hours** |

**Definition of Done (Sprint 5):**
- [ ] >90% drowsiness detection accuracy achieved
- [ ] >85% activity recognition accuracy per class
- [ ] >15 FPS real-time performance confirmed
- [ ] <1 false alert/hour in 8-hour test
- [ ] All critical bugs fixed
- [ ] Test results documented
- [ ] System stable with <1% crash rate

---

## 6. RESOURCE ALLOCATION

### 6.1 Human Resources

**Primary Resource: Hung Thanh (Student Developer)**

**Time Allocation (12 weeks):**
- Total available: 12 weeks × 40 hours/week = **480 hours**
- Development: 260 hours (54%)
- Testing: 80 hours (17%)
- Documentation: 80 hours (17%)
- Project Management: 60 hours (12%)

**Weekly Schedule Example:**

| Day | Time | Activity |
|-----|------|----------|
| Monday | 9:00-12:00 | Development (3h) |
| Monday | 14:00-17:00 | Development (3h) |
| Tuesday | 9:00-12:00 | Development (3h) |
| Tuesday | 14:00-17:00 | Development (3h) |
| Wednesday | 9:00-12:00 | Development (3h) |
| Wednesday | 14:00-16:00 | **Advisor Meeting** (2h) |
| Wednesday | 16:00-17:00 | Meeting minutes documentation (1h) |
| Thursday | 9:00-12:00 | Development (3h) |
| Thursday | 14:00-17:00 | Testing / Bug Fixing (3h) |
| Friday | 9:00-12:00 | Development (3h) |
| Friday | 14:00-17:00 | Documentation (3h) |
| **Weekly Total** | - | **34 hours** (excludes weekends) |

**Advisor Availability:**
- Weekly meetings: Wednesday 14:00-16:00 (2 hours)
- Email support: Within 24 hours response time
- Emergency consultation: Available on request

### 6.2 Hardware Resources

| Hardware | Purpose | Availability | Cost |
|----------|---------|--------------|------|
| **Development Laptop** | Primary development machine | Week 1-12 | $0 (existing) |
| **IR Camera** | Driver face capture | Week 3-12 (order Week 2) | $40 |
| **Jetson Nano 4GB** | Edge computing device | Week 3-12 (order Week 2) | $140 |
| **MicroSD Card (128GB)** | Storage for Jetson | Week 3-12 | $20 |
| **USB Speaker** | Audio alerts | Week 7-12 | $15 |
| **Power Supply** | Jetson power | Week 3-12 | $10 |
| **Optional: 7" Display** | Dashboard display | Week 6-12 (optional) | $60 |
| **TOTAL** | - | - | **$225-285** |

**Hardware Acquisition Timeline:**
- Week 2: Order IR camera, Jetson Nano, accessories
- Week 3: Receive hardware, begin setup
- Week 3: Test camera connectivity
- Week 5: Full system integration

### 6.3 Software Resources

**All software tools are free/open-source:**

| Software | Purpose | License | Cost |
|----------|---------|---------|------|
| Python 3.8+ | Programming language | Open Source | Free |
| OpenCV | Computer vision | Open Source | Free |
| dlib | Face landmarks | Open Source | Free |
| TensorFlow | Deep learning | Open Source | Free |
| SQLite | Database | Open Source | Free |
| Git / GitHub | Version control | Free tier | Free |
| VS Code | IDE | Open Source | Free |
| Jupyter Notebook | Model training | Open Source | Free |
| pytest | Testing framework | Open Source | Free |
| **TOTAL** | - | - | **$0** |

### 6.4 Cloud Resources (Optional)

| Resource | Purpose | Provider | Estimated Cost |
|----------|---------|----------|----------------|
| **Cloud GPU (Optional)** | Model training (if laptop GPU insufficient) | Google Colab Pro | $10/month (1-2 months) |
| **GitHub Storage** | Code repository | GitHub Free | Free |
| **Total (Optional)** | - | - | **$0-20** |

**Decision Point:** Week 8 - Evaluate if cloud GPU needed for activity CNN training

---

## 7. RISK MANAGEMENT PLAN

### 7.1 Risk Identification & Assessment

| Risk ID | Risk Description | Probability | Impact | Risk Score | Category |
|---------|------------------|-------------|--------|------------|----------|
| **R1** | Activity recognition accuracy <85% | Medium (40%) | High | **HIGH** | Technical |
| **R2** | Real-time performance <15 FPS on Jetson | Medium (30%) | High | **HIGH** | Technical |
| **R3** | Hardware delivery delayed | Low (20%) | Medium | **MEDIUM** | External |
| **R4** | Drowsiness false positive rate too high | Medium (40%) | Medium | **MEDIUM** | Technical |
| **R5** | Dataset collection takes longer than planned | Medium (30%) | Medium | **MEDIUM** | Schedule |
| **R6** | System crashes during long tests | Low (20%) | Medium | **MEDIUM** | Technical |
| **R7** | Scope creep (adding unplanned features) | High (50%) | Low | **MEDIUM** | Management |
| **R8** | Illness or personal emergency | Low (15%) | High | **MEDIUM** | Personal |
| **R9** | IR camera doesn't work well in all lighting | Medium (30%) | Low | **LOW** | Technical |
| **R10** | Advisor unavailable for critical decisions | Low (10%) | Medium | **LOW** | External |

**Risk Score Calculation:** Probability × Impact  
**Priority:** HIGH (>30%), MEDIUM (15-30%), LOW (<15%)

### 7.2 Risk Response Strategies

#### **R1: Activity Recognition Accuracy <85% (HIGH RISK)**

**Mitigation (Preventive):**
- Collect large, diverse dataset (300+ samples per activity)
- Use data augmentation (rotation, brightness, blur) to increase dataset size
- Start with pre-trained MobileNetV2 and fine-tune
- Consult advisor early if accuracy issues arise
- Allocate extra time in Sprint 4 for model tuning (Week 8-9)

**Contingency (If it happens):**
- Reduce scope to 5 most critical activities (calling, drinking, smoking, yawning, hands off wheel)
- Accept lower accuracy threshold (80%) with clear documentation
- Implement confidence thresholding to reduce false positives
- Combine with rule-based methods (e.g., hand detection for calling)

**Owner:** Hung Thanh  
**Review Date:** End of Week 8

---

#### **R2: Real-time Performance <15 FPS (HIGH RISK)**

**Mitigation (Preventive):**
- Use lightweight models (MobileNetV2, not ResNet)
- Optimize code (vectorization, avoid loops)
- Use TensorFlow Lite for model inference
- Profile code to identify bottlenecks
- Consider processing every 2nd frame if needed
- Target Jetson Nano (better GPU) instead of Raspberry Pi

**Contingency (If it happens):**
- Reduce camera resolution (720p instead of 1080p)
- Disable optional features (PERCLOS, pupil tracking)
- Skip activity recognition on some frames (run every 3rd frame)
- Use threading to parallelize face detection and CNN inference
- Accept 12-15 FPS as "near real-time"

**Owner:** Hung Thanh  
**Review Date:** End of Week 6 (after Sprint 2)

---

#### **R3: Hardware Delivery Delayed (MEDIUM RISK)**

**Mitigation (Preventive):**
- Order hardware early (Week 2)
- Choose reliable suppliers (Amazon, official distributors)
- Have backup supplier options
- Track shipment proactively

**Contingency (If it happens):**
- Use laptop webcam temporarily for development
- Develop and test with pre-recorded video datasets
- Borrow hardware from university lab if available
- Order from local store (higher cost but immediate)
- Adjust schedule: Continue with software development, integrate hardware later

**Owner:** Hung Thanh  
**Trigger:** If hardware not received by end of Week 3

---

#### **R4: Drowsiness False Positive Rate Too High (MEDIUM RISK)**

**Mitigation (Preventive):**
- Implement multi-signal fusion (EAR + PERCLOS + yawning + blink rate)
- Require 2+ indicators before triggering alert
- Use time-based thresholds (sustained drowsiness for 2+ seconds)
- Test on diverse subjects with different eye shapes
- Allow per-driver calibration of thresholds

**Contingency (If it happens):**
- Increase EAR threshold (from 0.25 to 0.22)
- Increase time threshold (from 2s to 3s)
- Add "sensitivity" setting (low/medium/high)
- Document known limitations in user manual
- Focus on recall (catch all drowsy cases) over precision

**Owner:** Hung Thanh  
**Review Date:** End of Week 7 (after Sprint 3)

---

#### **R5: Dataset Collection Takes Longer Than Planned (MEDIUM RISK)**

**Mitigation (Preventive):**
- Start dataset collection early (Week 7, parallel to Sprint 3)
- Use public datasets if available (State Farm, Kaggle)
- Recruit friends/family as volunteers for quick data collection
- Use data augmentation to multiply dataset size
- Allocate buffer time in Sprint 4

**Contingency (If it happens):**
- Reduce samples per activity (from 300 to 200)
- Focus on 5 activities instead of 7
- Use synthetic data generation (GAN, if time permits)
- Accept lower accuracy and document as "future work"
- Simulate some activities with posed photos

**Owner:** Hung Thanh  
**Trigger:** If <100 samples/activity collected by end of Week 8

---

#### **R7: Scope Creep (MEDIUM RISK)**

**Mitigation (Preventive):**
- Strict adherence to MoSCoW prioritization (24 MUST HAVE features)
- Weekly scope review with advisor
- Document all "nice to have" ideas in "Future Work" section
- Remind self: "Good enough to graduate" is the goal
- Use Product Backlog as single source of truth

**Contingency (If it happens):**
- Immediate scope freeze
- Re-evaluate timeline and cut non-MUST features
- Communicate with advisor about realistic completion
- Move SHOULD HAVE features to "Future Work"

**Owner:** Hung Thanh + Advisor  
**Review:** Weekly meetings

---

#### **R8: Illness or Personal Emergency (MEDIUM RISK)**

**Mitigation (Preventive):**
- Maintain good health (sleep, exercise)
- Keep schedule buffer (aim to finish Week 11, not Week 12)
- Regular backups of all work (GitHub + local)
- Document everything so work can resume quickly

**Contingency (If it happens):**
- Notify advisor immediately
- Work from home if possible (minor illness)
- Request timeline extension if needed (major emergency)
- Prioritize MUST HAVE features only
- Leverage existing work (brainstorming session already complete)

**Owner:** Hung Thanh  
**Trigger:** Any unplanned absence >2 days

---

### 7.3 Risk Monitoring

**Risk Review Frequency:**
- Weekly during advisor meetings
- After each sprint (Sprint Retrospective)
- Immediate review if any risk materializes

**Risk Log:**
- Maintain risk register in project documentation
- Update probability/impact as project progresses
- Document risk responses taken

---

## 8. QUALITY MANAGEMENT PLAN

### 8.1 Quality Standards

| Deliverable Type | Quality Standard | Verification Method |
|------------------|------------------|---------------------|
| **Code** | - PEP 8 compliant<br>- >70% code coverage<br>- No critical bugs | - flake8 linting<br>- pytest with coverage<br>- Manual code review |
| **Models** | - >90% drowsiness accuracy<br>- >85% activity accuracy<br>- <5% false positive rate | - Test dataset evaluation<br>- Confusion matrix analysis<br>- Real-world testing |
| **Performance** | - >15 FPS<br>- <500ms latency<br>- >99% uptime | - FPS monitoring<br>- Timestamp logging<br>- 8-hour stress test |
| **Documentation** | - Complete sections<br>- Clear language<br>- Proper formatting | - Advisor review<br>- Peer review<br>- Spell check |
| **User Interface** | - Responsive<br>- Intuitive<br>- Clear feedback | - Usability testing<br>- User feedback<br>- Task completion rate |

### 8.2 Quality Assurance Activities

**During Development:**
- Daily: Run unit tests before committing code
- Weekly: Code review (self-review + optional peer review)
- Sprint end: Integration testing, performance benchmarking

**Testing Phase (Week 10-11):**
- Unit testing: Test each module independently
- Integration testing: Test module interactions
- System testing: End-to-end functionality
- Performance testing: Accuracy, speed, reliability
- User acceptance testing: Real-world driving scenarios

### 8.3 Code Quality Standards

**Coding Conventions (PEP 8):**
```python
# Example code structure
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

**Code Review Checklist:**
- [ ] Follows PEP 8 style guide
- [ ] Functions have docstrings
- [ ] Variable names are descriptive
- [ ] No hardcoded values (use config file)
- [ ] Error handling implemented
- [ ] Unit tests written
- [ ] No commented-out code
- [ ] Performance optimized (no unnecessary loops)

### 8.4 Testing Strategy

**Test Pyramid:**
```
        ╱────────╲
       ╱   E2E    ╲      ← 10% (System tests)
      ╱────────────╲
     ╱ Integration  ╲    ← 30% (Module interactions)
    ╱────────────────╲
   ╱   Unit Tests     ╲  ← 60% (Individual functions)
  ╱────────────────────╲
```

**Test Coverage Goals:**
- Unit tests: >70% code coverage
- Integration tests: All module interfaces
- System tests: All user stories with acceptance criteria
- Performance tests: All critical metrics

---

## 9. COMMUNICATION PLAN

### 9.1 Communication Matrix

| Stakeholder | Information Needed | Frequency | Method | Responsible |
|-------------|-------------------|-----------|--------|-------------|
| **Thesis Advisor** | - Progress updates<br>- Technical decisions<br>- Blockers/risks<br>- Deliverable reviews | Weekly | - In-person meeting (2h)<br>- Email (as needed) | Hung Thanh |
| **Thesis Committee** | - Proposal approval<br>- Final thesis submission<br>- Defense scheduling | Milestone-based | - Formal documents<br>- Presentation | Hung Thanh |
| **Self (Project Log)** | - Daily progress<br>- Decisions made<br>- Lessons learned | Daily | - Git commit messages<br>- Project journal | Hung Thanh |
| **Peer Reviewers (Optional)** | - Code review requests<br>- Technical feedback | As needed | - GitHub pull requests<br>- Messaging | Hung Thanh |

### 9.2 Meeting Schedule

**Weekly Advisor Meeting (Every Wednesday 14:00-16:00)**

**Agenda Template:**
1. Progress since last meeting (10 min)
   - Completed tasks
   - Current sprint status
2. Demo (if applicable) (15 min)
   - Show working features
3. Challenges & blockers (15 min)
   - Technical issues
   - Decision points
4. Plan for next week (10 min)
   - Upcoming tasks
   - Priorities
5. Questions & guidance (10 min)

**Meeting Minutes Template:**
```
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

### 9.3 Status Reporting

**Weekly Status Report (Prepared for Wednesday meeting)**

**Format:**
```
WEEKLY STATUS REPORT
Week: [Week Number]
Date: [Date]

COMPLETED THIS WEEK:
✅ [Task 1]
✅ [Task 2]
✅ [Task 3]

IN PROGRESS:
🔄 [Task 4] - 60% complete
🔄 [Task 5] - 30% complete

PLANNED FOR NEXT WEEK:
📋 [Task 6]
📋 [Task 7]

RISKS/BLOCKERS:
⚠️ [Risk 1] - Mitigation: [action]
❌ [Blocker 1] - Need: [advisor input]

METRICS:
- Code coverage: XX%
- Test cases written: XX
- Performance: XX FPS

STATUS: 🟢 On Track / 🟡 At Risk / 🔴 Delayed
```

### 9.4 Documentation Repository

**GitHub Repository Structure:**
```
docs-driver/
├── README.md                     # Project overview
├── docs/
│   ├── proposal.md               # Deliverable 1
│   ├── project-plan.md           # Deliverable 2
│   ├── product-backlog.md        # Deliverable 3
│   ├── user-stories.md           # Deliverable 4
│   ├── architecture.md           # Deliverable 5
│   ├── database-design.md        # Deliverable 6
│   ├── ui-design.md              # Deliverable 7
│   ├── test-plan.md              # Deliverable 8
│   ├── test-cases.md             # Deliverable 9
│   ├── code-standard.md          # Deliverable 11
│   └── reflection.md             # Deliverable 13
├── meeting-minutes/              # Deliverable 12
│   ├── week-01.md
│   ├── week-02.md
│   └── ...
├── sprint-backlogs/              # Deliverable 10
│   ├── sprint-2.md
│   ├── sprint-3.md
│   └── ...
├── src/                          # Source code
├── tests/                        # Test code
├── models/                       # Trained models
├── data/                         # Datasets
└── presentations/                # Defense slides
```

---

## 10. BUDGET & COST ESTIMATION

### 10.1 Hardware Budget

| Item | Specification | Quantity | Unit Price | Total | Priority |
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
| **TOTAL (with all optional)** | - | - | - | **$320** | - |

**Hardware Budget Plan:** Target $225 (MUST + SHOULD items)

### 10.2 Software Budget

All software is open-source or free tier:

| Software | License Type | Cost |
|----------|--------------|------|
| Python, OpenCV, dlib, TensorFlow | Open Source | $0 |
| Git, GitHub (Free tier) | Free | $0 |
| VS Code, Jupyter | Open Source | $0 |
| SQLite | Open Source | $0 |
| Google Colab (Basic) | Free | $0 |
| **TOTAL** | - | **$0** |

**Optional (if needed):**
- Google Colab Pro (GPU for training): $10/month × 2 months = $20
- Total with optional: $20

### 10.3 Total Project Budget

| Category | Budgeted | Actual (to be filled) |
|----------|----------|-----------------------|
| Hardware | $225 | |
| Software | $0 | |
| Cloud Services (optional) | $0-20 | |
| Printing/Binding (thesis) | $20 | |
| Miscellaneous | $35 | |
| **TOTAL** | **$280-300** | |

**Funding Source:** Personal funds / Student stipend

---

## 11. MILESTONES & DELIVERABLES

### 11.1 Major Milestones

| ID | Milestone | Criteria | Target Date | Status |
|----|-----------|----------|-------------|--------|
| **M1** | Proposal Approved | Advisor signs proposal | Week 1 (Mar 11, 2026) | Pending |
| **M2** | Hardware Acquired | IR camera + Jetson Nano received | Week 3 (Mar 25, 2026) | Pending |
| **M3** | Architecture Complete | Design documents approved | Week 4 (Apr 1, 2026) | Pending |
| **M4** | Foundation Modules Working | Sprint 2 demo successful (face/eye/head/gaze) | Week 6 (Apr 15, 2026) | Pending |
| **M5** | Core Detection Complete | Sprint 3 demo (drowsiness + distraction) | Week 8 (Apr 29, 2026) | Pending |
| **M6** | All MUST HAVEs Implemented | 24 features working | Week 9 (May 6, 2026) | Pending |
| **M7** | Testing Complete | All metrics achieved, bugs fixed | Week 11 (May 20, 2026) | Pending |
| **M8** | Thesis Submitted | All 13 deliverables submitted | Week 12 (May 27, 2026) | Pending |
| **M9** | Defense Successful | Thesis defense passed | TBD (May 27-31, 2026) | Pending |

### 11.2 Deliverables Checklist

| # | Deliverable | Description | Due Date | Owner | Status |
|---|-------------|-------------|----------|-------|--------|
| 1 | **Proposal** | Project proposal document | Week 1 | Hung Thanh | ✅ Complete |
| 2 | **Project Plan** | This document | Week 2 | Hung Thanh | 🔄 In Progress |
| 3 | **Product Backlog** | 45 PBIs with MoSCoW priorities | Week 3 | Hung Thanh | ✅ Complete (from brainstorming) |
| 4 | **User Stories** | 48 stories with acceptance criteria | Week 4 | Hung Thanh | ✅ Complete (from brainstorming) |
| 5 | **Architecture** | System architecture document | Week 4-5 | Hung Thanh | Pending |
| 6 | **Database Design** | ER diagram, table schemas | Week 5 | Hung Thanh | Pending |
| 7 | **UI/Interfaces** | Wireframes, mockups | Week 5 | Hung Thanh | Pending |
| 8 | **Test Plan** | Test strategy and scenarios | Week 5 | Hung Thanh | Pending |
| 9 | **Test Cases** | 50+ detailed test cases | Week 10 | Hung Thanh | Pending |
| 10 | **Sprint Backlog** | Sprint 2-5 backlogs | Week 5-10 | Hung Thanh | Pending |
| 11 | **Code Standard** | Coding conventions document | Week 6 | Hung Thanh | Pending |
| 12 | **Meeting Minutes** | 12 weekly meeting notes | Week 1-12 | Hung Thanh | Ongoing |
| 13 | **Reflection** | Lessons learned, future work | Week 12 | Hung Thanh | Pending |
| - | **Working System** | Deployed prototype | Week 11 | Hung Thanh | Pending |
| - | **Source Code** | GitHub repository | Week 12 | Hung Thanh | Ongoing |
| - | **Trained Models** | CNN model files | Week 9 | Hung Thanh | Pending |
| - | **User Manual** | Installation & usage guide | Week 11 | Hung Thanh | Pending |
| - | **Defense Slides** | Presentation | Week 12 | Hung Thanh | Pending |

---

## 12. SUCCESS METRICS

### 12.1 Technical Metrics

| Metric | Target | Measurement Method | Status |
|--------|--------|--------------------|--------|
| **Drowsiness Detection Accuracy** | >90% | Test dataset (100+ labeled samples) | TBD |
| **Activity Recognition Accuracy** | >85% per class | Test dataset (7 classes, 100+ samples each) | TBD |
| **False Positive Rate (Drowsiness)** | <1 alert/hour | 8-hour real driving test with alert driver | TBD |
| **False Positive Rate (Activities)** | <5% | Confusion matrix analysis | TBD |
| **Real-time Performance (FPS)** | >15 FPS | Frame rate monitoring during operation | TBD |
| **Detection Latency** | <500ms | Timestamp logging (event to alert) | TBD |
| **System Uptime** | >99% | No crashes in 8-hour continuous test | TBD |
| **Face Detection Success Rate** | >95% | When face is visible and unoccluded | TBD |
| **Driver Identification Accuracy** | >95% | Face recognition on enrolled drivers | TBD |
| **Code Coverage** | >70% | pytest-cov report | TBD |

### 12.2 Project Management Metrics

| Metric | Target | Status |
|--------|--------|--------|
| **On-time Deliverables** | 13/13 (100%) | TBD |
| **Milestones Met** | 9/9 (100%) | TBD |
| **Budget Adherence** | Within $300 | TBD |
| **Weekly Meetings Attended** | 12/12 (100%) | TBD |
| **Meeting Minutes Documented** | 12/12 (100%) | TBD |
| **Sprint Velocity** | Consistent across sprints | TBD |
| **Unplanned Scope Changes** | 0 | TBD |

### 12.3 Academic Metrics

| Metric | Target | Status |
|--------|--------|--------|
| **Proposal Approval** | Approved by advisor | Pending |
| **Defense Attendance** | 100% committee present | TBD |
| **Defense Result** | Pass | TBD |
| **Final Grade** | ≥ Good (7.0/10) | TBD |
| **Publication/Competition (Bonus)** | Optional | TBD |

### 12.4 Quality Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Critical Bugs** | 0 at submission | Bug tracker |
| **High Priority Bugs** | <3 at submission | Bug tracker |
| **Documentation Completeness** | All sections filled | Document review |
| **Code Style Compliance** | 100% PEP 8 | flake8 report |
| **User Satisfaction (Optional)** | >4/5 rating | User testing feedback |

---

## 13. ASSUMPTIONS & CONSTRAINTS

### 13.1 Assumptions

**Technical Assumptions:**
- ✅ Jetson Nano has sufficient computing power for real-time processing (>15 FPS)
- ✅ IR camera works reliably in both day and night conditions
- ✅ Pre-trained models (dlib, MobileNetV2) are available and suitable
- ✅ OpenCV and dlib provide adequate accuracy for face/eye detection
- ✅ Training datasets for dangerous activities can be collected or found online
- ✅ SQLite is sufficient for local data storage

**Project Assumptions:**
- ✅ Student has full-time availability (40 hours/week) for 12 weeks
- ✅ Advisor is available for weekly 2-hour meetings
- ✅ Hardware will be delivered within 1-2 weeks of ordering
- ✅ No major personal emergencies or illnesses
- ✅ Development laptop has sufficient specs (i5+ CPU, 8GB+ RAM, discrete GPU optional)
- ✅ Internet access available for research and library downloads

**Scope Assumptions:**
- ✅ Single IR camera is sufficient (no multi-camera setup)
- ✅ Driver face is visible to camera (not occluded by objects)
- ✅ System operates in controlled vehicle environment (not extreme weather)
- ✅ Single driver per trip (not handling driver changes mid-trip)

### 13.2 Constraints

**Time Constraints:**
- ⏰ **12-week hard deadline** for thesis submission (May 27, 2026)
- ⏰ Defense must occur before end of academic year (late May 2026)
- ⏰ No extensions possible (graduation requirement)

**Resource Constraints:**
- 💰 **Budget limit: $300** (personal funds)
- 👤 **Single developer** (no team members)
- ⏱️ **Advisor availability: 2 hours/week** only

**Technical Constraints:**
- 🔧 **Hardware performance**: Jetson Nano GPU limits model complexity
- 🔧 **Edge computing**: All processing must happen locally (no cloud)
- 🔧 **Real-time requirement**: Must maintain >15 FPS
- 🔧 **Camera FOV**: Single camera limits field of view

**Scope Constraints:**
- 📋 **24 MUST HAVE features** are mandatory minimum
- 📋 **17 SHOULD HAVE features** are optional (time-permitting)
- 📋 **Safety belt detection** explicitly removed from scope
- 📋 **Mobile app** out of scope

**Academic Constraints:**
- 🎓 **13 deliverables** required by university
- 🎓 **Weekly meetings** mandatory
- 🎓 **Thesis defense** must demonstrate working system live
- 🎓 **Original work** (no plagiarism, proper citations required)

### 13.3 Dependencies

**External Dependencies:**
- 📦 Hardware supplier delivery time (Week 2-3)
- 👨‍🏫 Advisor availability for guidance
- 📚 Access to research papers and datasets
- 🌐 Internet connectivity for library downloads

**Internal Dependencies (Critical Path):**
- Proposal approval → Project plan → Architecture → Development
- Hardware arrival → Camera integration → All detection modules
- Dataset collection → Model training → Activity recognition
- Development complete → Testing → Defense

---

## APPENDICES

### Appendix A: Sprint Planning Template

```markdown
# Sprint [Number]: [Sprint Name]

**Sprint Duration:** [Start Date] to [End Date] (2 weeks)  
**Sprint Goal:** [One-sentence goal]

## Sprint Backlog

| PBI | Task | Priority | Estimated Effort | Actual Effort | Status |
|-----|------|----------|------------------|---------------|--------|
| PBI-XXX | Task description | MUST | Xh | | Pending |
| ... | ... | ... | ... | | |

**Total Estimated Effort:** XX hours

## Daily Progress Log

### Day 1 ([Date]):
- Completed: [tasks]
- In Progress: [tasks]
- Blockers: [issues]

### Day 2 ([Date]):
...

## Sprint Review ([Date])

**Demo:**
- [Feature 1] demonstrated to advisor
- Feedback: [feedback received]

**Completed PBIs:** X/Y  
**Velocity:** XX story points

## Sprint Retrospective

**What Went Well:**
- [Positive 1]
- [Positive 2]

**What Could Improve:**
- [Issue 1]
- [Issue 2]

**Action Items for Next Sprint:**
- [Action 1]
- [Action 2]
```

### Appendix B: Meeting Minutes Template

```markdown
# Meeting Minutes - Week [XX]

**Date:** [Date]  
**Time:** [Start Time] - [End Time]  
**Location:** [Location / Virtual]  
**Attendees:** Hung Thanh, [Advisor Name]

## Agenda
1. Progress Update
2. Demo (if applicable)
3. Challenges Discussion
4. Next Steps
5. Q&A

## Progress Since Last Meeting
- ✅ [Completed task 1]
- ✅ [Completed task 2]
- ✅ [Completed task 3]

## Demo
**Features Demonstrated:**
- [Feature 1]: [Brief description]
  - Feedback: [Advisor comments]
- [Feature 2]: [Brief description]
  - Feedback: [Advisor comments]

## Challenges & Blockers
1. **[Challenge 1]**
   - Description: [Details]
   - Advisor Guidance: [Advice given]
   - Resolution: [Action decided]

2. **[Challenge 2]**
   - Description: [Details]
   - Decision: [Decision made]

## Technical Decisions Made
- [Decision 1]: [Rationale]
- [Decision 2]: [Rationale]

## Action Items

| Action | Owner | Due Date | Status |
|--------|-------|----------|--------|
| [Action 1] | Hung Thanh | [Date] | Pending |
| [Action 2] | [Advisor Name] | [Date] | Pending |

## Plan for Next Week
- [ ] [Task 1]
- [ ] [Task 2]
- [ ] [Task 3]

## Questions Raised
- Q: [Question]
  - A: [Answer]

## Next Meeting
**Date:** [Next meeting date]  
**Time:** [Time]  
**Location:** [Location]

---

**Minutes Prepared By:** Hung Thanh  
**Date Prepared:** [Date]
```

### Appendix C: Risk Register Template

```markdown
# Risk Register

**Project:** Driver Monitoring System  
**Last Updated:** [Date]

| Risk ID | Description | Category | Probability | Impact | Score | Status | Owner | Mitigation | Contingency |
|---------|-------------|----------|-------------|--------|-------|--------|-------|------------|-------------|
| R1 | [Risk description] | Technical | 40% | High | HIGH | Active | Hung Thanh | [Mitigation strategy] | [Contingency plan] |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |

## Risk Status
- **Active:** Risk exists but has not occurred
- **Occurred:** Risk has materialized
- **Closed:** Risk no longer relevant
```

### Appendix D: Change Request Template

```markdown
# Change Request #[Number]

**Date Submitted:** [Date]  
**Submitted By:** [Name]  
**Status:** Pending / Approved / Rejected

## Change Description
[Detailed description of proposed change]

## Rationale
[Why is this change needed?]

## Impact Analysis

**Scope Impact:**
- [Scope changes]

**Schedule Impact:**
- Estimated delay: [X days/weeks]
- Affected milestones: [Milestones]

**Budget Impact:**
- Additional cost: $[Amount]

**Quality Impact:**
- [Quality implications]

## Alternatives Considered
1. [Alternative 1]
2. [Alternative 2]

## Recommendation
[Approve / Reject with rationale]

## Decision
**Date:** [Date]  
**Decision Maker:** [Advisor Name]  
**Decision:** Approved / Rejected  
**Notes:** [Additional comments]
```

---

## APPROVAL SIGNATURES

**Student Signature:** _____________________________ Date: __________  
Name: Hung Thanh

**Advisor Signature:** _____________________________ Date: __________  
Name: [Advisor Name]

---

## DOCUMENT REVISION HISTORY

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | Mar 4, 2026 | Hung Thanh | Initial project plan created |
| | | | |
| | | | |

---

**END OF PROJECT PLAN**

---

**Document Information:**
- **File Name:** PROJECT-PLAN-Driver-Monitoring-System.md
- **Version:** 1.0
- **Created:** March 4, 2026
- **Last Updated:** March 4, 2026
- **Total Pages:** ~35 pages (estimated when converted to PDF)
- **Word Count:** ~12,000 words
- **Status:** Draft (Pending Advisor Approval)
