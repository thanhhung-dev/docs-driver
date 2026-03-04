# Product Backlog - Driver Monitoring System

**Project:** Driver Monitoring System (DMS) - Đồ án Tốt nghiệp  
**Generated:** 2026-03-04  
**Source:** Brainstorming Session 2026-03-03-004815  
**Total Items:** 45 Product Backlog Items (PBIs)

---

## Table of Contents

1. [Product Backlog Overview](#product-backlog-overview)
2. [Morphological Analysis Matrix](#morphological-analysis-matrix)
3. [Product Backlog Items by Category](#product-backlog-items-by-category)
4. [MoSCoW Prioritization Summary](#moscow-prioritization-summary)
5. [Technology Stack](#technology-stack)

---

## Product Backlog Overview

This Product Backlog was created using **Morphological Analysis** technique to systematically discover and classify all features of the Driver Monitoring System.

### Summary Statistics

- **Total PBIs:** 45 features
- **Functional Categories:** 13 areas
- **MoSCoW Breakdown:**
  - **MUST HAVE:** 24 items (core MVP features)
  - **SHOULD HAVE:** 17 items (important enhancements)
  - **COULD HAVE:** 4 items (nice-to-have features)
  - **WON'T HAVE:** Safety belt detection (removed per scope decision)

---

## Morphological Analysis Matrix

The following 4-dimensional matrix was used to systematically explore all possible features:

| Dimension | Options |
|-----------|---------|
| **1. Detection Type** | Face Detection, Eye Monitoring, Head Monitoring, Gaze Tracking, Drowsiness Detection, Distraction Detection, Activity Recognition, Passenger Counting, System Health, Driver Enrollment |
| **2. Monitored Entity** | Driver Only, Driver + Passengers, Camera/System |
| **3. Technology Layer** | Computer Vision (CV), Infrared (IR), AI/ML Models, Rule-based Logic, Hardware Integration |
| **4. Output/Action** | Real-time Alert, Logging/Recording, Dashboard Display, Analytics/Reports |

---

## Product Backlog Items by Category

### Category 1: Core Face & Eye Detection (Foundation)

> **Purpose:** Foundation layer for all driver monitoring capabilities. Must detect and track facial features reliably.

---

#### PBI-001: Face Detection & Tracking

- **Priority:** MUST HAVE
- **Description:** Detect and track driver's face in real-time using IR camera
- **Technology:** Computer Vision (dlib/MediaPipe) + IR Camera
- **Monitored Entity:** Driver Only
- **Output:** Face bounding box, face landmarks (68 points)
- **Dependencies:** None (foundation feature)
- **Success Criteria:**
  - Face detection confidence >90%
  - Detection works in all lighting conditions (day/night) with IR camera
  - 68-point facial landmarks extracted successfully
  - Frame rate: minimum 15 FPS

---

#### PBI-002: Eye Region Detection

- **Priority:** MUST HAVE
- **Description:** Detect left and right eye regions from face landmarks
- **Technology:** Computer Vision (dlib facial landmarks)
- **Monitored Entity:** Driver Only
- **Output:** Eye bounding boxes, eye landmarks
- **Dependencies:** PBI-001 (requires face detection)
- **Success Criteria:**
  - Both eyes detected with >95% accuracy when face is visible
  - Eye landmarks (6 points per eye) extracted
  - Handles partial occlusion (one eye visible)

---

#### PBI-003: Eye Openness Detection

- **Priority:** MUST HAVE
- **Description:** Calculate Eye Aspect Ratio (EAR) to determine if eyes are open/closed
- **Technology:** Rule-based (EAR calculation from eye landmarks)
- **Monitored Entity:** Driver Only
- **Output:** EAR values (left, right, average), open/closed state
- **Dependencies:** PBI-002 (requires eye landmarks)
- **Success Criteria:**
  - EAR calculation accurate to 2 decimal places
  - Open/closed classification threshold: EAR < 0.25 = closed
  - Works with glasses (PBI-032 enhancement)

---

#### PBI-004: Blink Frequency Monitoring

- **Priority:**  MUST HAVE
- **Description:** Count blinks per minute to detect abnormal patterns (drowsiness indicator)
- **Technology:** Rule-based (EAR threshold detection)
- **Monitored Entity:** Driver Only
- **Output:** Blinks per minute, blink duration average
- **Dependencies:** PBI-003 (requires EAR calculation)
- **Success Criteria:**
  - Blink detection: EAR drops below 0.25 for 100-400ms
  - Count blinks accurately over 60-second rolling window
  - Normal range: 15-20 blinks/min; Low: <10 (drowsiness); High: >30 (stress)

---

#### PBI-005: Eye Location Tracking

- **Priority:**  MUST HAVE
- **Description:** Track eye position within face region for gaze estimation
- **Technology:** Computer Vision (pupil detection)
- **Monitored Entity:** Driver Only
- **Output:** Eye center coordinates (x, y)
- **Dependencies:** PBI-002 (requires eye region)
- **Success Criteria:**
  - Pupil center located with ±3 pixel accuracy
  - Updates at frame rate (15-20 Hz minimum)
  - Foundation for gaze estimation (PBI-009)

---

### Category 2: Head Pose & Orientation

> **Purpose:** Track head movement to detect distraction, combined with gaze for robust attention monitoring.

---

#### PBI-006: Head Pose Estimation

- **Priority:** MUST HAVE
- **Description:** Estimate head orientation (pitch, yaw, roll) from facial landmarks using 3D pose estimation
- **Technology:** Computer Vision (solvePnP algorithm)
- **Monitored Entity:** Driver Only
- **Output:** Euler angles (pitch, yaw, roll in degrees)
- **Dependencies:** PBI-001 (requires face landmarks)
- **Success Criteria:**
  - Pitch/Yaw/Roll angles calculated with ±5° accuracy
  - Range: Yaw ±90°, Pitch ±60°, Roll ±45°
  - Update rate: 15+ Hz

---

#### PBI-007: Head Location Tracking

- **Priority:** MUST HAVE
- **Description:** Track head position in camera frame (left, center, right, up, down)
- **Technology:** Computer Vision (face centroid tracking)
- **Monitored Entity:** Driver Only
- **Output:** Head position zone (9 zones: center, left, right, up, down, combinations)
- **Dependencies:** PBI-001 (requires face bounding box)
- **Success Criteria:**
  - 9-zone grid classification (3x3: left/center/right × up/center/down)
  - Position updates in real-time

---

#### PBI-008: Head Zone Classification

- **Priority:** MUST HAVE
- **Description:** Classify head pose into meaningful zones (looking forward, left/right turn, looking down)
- **Technology:** Rule-based (head pose angle thresholds)
- **Monitored Entity:** Driver Only
- **Output:** Zone label (Forward, Left, Right, Down, Extreme angles)
- **Dependencies:** PBI-006 (requires head pose angles)
- **Success Criteria:**
  - Forward zone: Yaw ±20°, Pitch ±15°
  - Left/Right: Yaw >±20°
  - Down: Pitch <-15° (looking at phone/dashboard)
  - Extreme: Yaw >±60° or Pitch >±45° (severe distraction)

---

### Category 3: Eye Gaze Tracking

> **Purpose:** Precise gaze direction to detect where driver is looking (road, mirrors, phone, passenger).

---

#### PBI-009: Gaze Direction Estimation

- **Priority:**  MUST HAVE
- **Description:** Estimate gaze direction vector from eye landmarks and pupil position
- **Technology:** Computer Vision (gaze estimation algorithms) + AI/ML
- **Monitored Entity:** Driver Only
- **Output:** Gaze vector (3D direction), gaze angles
- **Dependencies:** PBI-005 (requires pupil position), PBI-006 (requires head pose for calibration)
- **Success Criteria:**
  - Gaze angle accuracy: ±5° (acceptable for zone-based detection)
  - Works with head pose fusion for robust estimation
  - Handles IR camera limitations

---

#### PBI-010: Gaze Zone Classification

- **Priority:**  MUST HAVE
- **Description:** Map gaze direction to specific zones (road ahead, dashboard, side mirrors, rearview mirror, phone/lap, passenger)
- **Technology:** Rule-based (gaze angle to zone mapping)
- **Monitored Entity:** Driver Only
- **Output:** Gaze zone label, dwell time per zone
- **Dependencies:** PBI-009 (requires gaze direction)
- **Success Criteria:**
  - 6+ zones defined: Road, Dashboard, Left Mirror, Right Mirror, Rearview Mirror, Phone/Lap, Passenger
  - Dwell time tracking: cumulative time per zone over 10-second window
  - Distraction threshold: >4 seconds off-road in 10-second window

---

#### PBI-011: Pupil Detection & Tracking

- **Priority:** SHOULD HAVE
- **Description:** Detect and track pupil position for precise gaze estimation (enhancement to PBI-005)
- **Technology:** Computer Vision (circular Hough transform or deep learning - MediaPipe Iris)
- **Monitored Entity:** Driver Only
- **Output:** Pupil center coordinates, pupil diameter
- **Dependencies:** PBI-002 (requires eye region)
- **Success Criteria:**
  - Pupil center accuracy: ±2 pixels
  - Pupil diameter measured (useful for stress/cognitive load research - future)
  - Improves gaze estimation accuracy from ±5° to ±3°

---

### Category 4: Drowsiness Detection

> **Purpose:** Multi-modal drowsiness detection using eye closure, blink patterns, yawning, and statistical metrics.

---

#### PBI-012: Drowsiness Detection (EAR-based)

- **Priority:**  MUST HAVE
- **Description:** Detect drowsiness using prolonged low EAR values (eyes closing for extended periods)
- **Technology:** Rule-based (EAR thresholding over time)
- **Monitored Entity:** Driver Only
- **Output:** Drowsiness level (normal, mild, severe), alert trigger
- **Dependencies:** PBI-003 (requires EAR values)
- **Success Criteria:**
  - Mild drowsiness: EAR <0.25 for 2-3 seconds → warning
  - Severe drowsiness: EAR <0.25 for >3 seconds → critical alert
  - Combined with blink rate (PBI-004) for robustness
  - Target: >90% detection accuracy, <1 false alert/hour

---

#### PBI-013: Yawning Detection

- **Priority:**  MUST HAVE
- **Description:** Detect yawning from Mouth Aspect Ratio (MAR) and duration
- **Technology:** Computer Vision (mouth landmarks from dlib) + Rule-based
- **Monitored Entity:** Driver Only
- **Output:** Yawn detected (yes/no), yawn count per period
- **Dependencies:** PBI-001 (requires face landmarks including mouth)
- **Success Criteria:**
  - MAR calculation: distance between upper/lower lips vs mouth width
  - Yawn threshold: MAR >0.6 for >2 seconds
  - Drowsiness indicator: 3+ yawns in 5 minutes → alert
  - Distinguish yawning from talking/eating (duration + MAR threshold)

---

#### PBI-014: Microsleep Detection

- **Priority:**  MUST HAVE
- **Description:** Detect very brief eye closures (0.5-3 seconds) indicating microsleep episodes
- **Technology:** Rule-based (EAR duration analysis)
- **Monitored Entity:** Driver Only
- **Output:** Microsleep event count, timestamps
- **Dependencies:** PBI-003 (requires EAR values)
- **Success Criteria:**
  - Microsleep: EAR <0.2 (fully closed) for 0.5-3 seconds
  - Distinguish from normal blinks (<0.4 seconds) and prolonged closure (>3 seconds)
  - Immediate critical alert on detection (extremely dangerous)
  - Log all microsleep events for analysis

---

#### PBI-015: PERCLOS Calculation

- **Priority:** SHOULD HAVE
- **Description:** Calculate Percentage of Eye Closure (PERCLOS) - industry-standard drowsiness metric
- **Technology:** Rule-based (EAR statistical analysis over time window)
- **Monitored Entity:** Driver Only
- **Output:** PERCLOS value (%), drowsiness risk level
- **Dependencies:** PBI-003 (requires EAR values)
- **Success Criteria:**
  - PERCLOS = % of time eyes closed in 60-second window
  - Calculation: count frames where EAR <0.25, divide by total frames
  - Thresholds: <10% = alert, 10-20% = mild drowsiness, >20% = severe drowsiness
  - Provides scientific validation for drowsiness detection

---

### Category 5: Distraction Detection

> **Purpose:** Detect when driver's attention is not on the road using head pose and gaze data.

---

#### PBI-016: Head Turn Distraction

- **Priority:**  MUST HAVE
- **Description:** Detect prolonged head turns away from road (based on head pose yaw angle)
- **Technology:** Rule-based (yaw angle + duration thresholds)
- **Monitored Entity:** Driver Only
- **Output:** Distraction alert, head-off-road duration
- **Dependencies:** PBI-006 (requires head pose angles)
- **Success Criteria:**
  - Distraction threshold: Yaw >±45° for >2 seconds → alert
  - Exception: Yaw 20-45° for <1.5 seconds = mirror check (no alert)
  - Extreme distraction: Yaw >±75° for >1 second → critical alert
  - Log distraction events with duration and angle

---

#### PBI-017: Gaze-off-Road Detection

- **Priority:**  MUST HAVE
- **Description:** Detect when gaze is away from forward road zone for extended time
- **Technology:** Rule-based (gaze zone + duration from PBI-010)
- **Monitored Entity:** Driver Only
- **Output:** Gaze-off-road duration, alert trigger
- **Dependencies:** PBI-010 (requires gaze zone classification)
- **Success Criteria:**
  - Gaze-off-road threshold: cumulative 4 seconds in 10-second window
  - Combined with head pose for robust detection (head forward but gaze at phone)
  - Distinguish mirror checks (brief gaze shifts) from distraction

---

#### PBI-018: Attention Score Calculation

- **Priority:** SHOULD HAVE
- **Description:** Calculate overall attention score (0-100) combining head pose, gaze, and eye openness
- **Technology:** Rule-based or ML (weighted scoring algorithm)
- **Monitored Entity:** Driver Only
- **Output:** Attention score (0-100), attention level (high/medium/low)
- **Dependencies:** PBI-006, PBI-009, PBI-003 (requires head, gaze, eye data)
- **Success Criteria:**
  - Score calculation: weighted average of head forward (40%), gaze on road (40%), eyes open (20%)
  - High attention: score >80 (green), Medium: 50-80 (yellow), Low: <50 (red alert)
  - Real-time score display on dashboard (PBI-044)
  - Rolling average over 10-second window for stability

---

### Category 6: Dangerous Activity Recognition (7 Activities)

> **Purpose:** Detect dangerous driver behaviors using AI/ML activity classification CNN.

---

#### PBI-019: Phone Calling Detection

- **Priority:**  MUST HAVE
- **Description:** Detect driver holding phone to ear during call
- **Technology:** AI/ML (Activity CNN - MobileNetV2 or EfficientNet)
- **Monitored Entity:** Driver Only
- **Output:** Activity label "calling", confidence score, alert
- **Dependencies:** PBI-026 (requires trained Activity CNN model)
- **Success Criteria:**
  - Detection accuracy: >85% on test dataset
  - Confidence threshold: >75% for 3 consecutive frames (0.3s at 10 FPS) → alert
  - Distinguish from scratching face, adjusting hair (temporal consistency)

---

#### PBI-020: Drinking Detection

- **Priority:**  MUST HAVE
- **Description:** Detect driver drinking from bottle/cup while driving
- **Technology:** AI/ML (Activity CNN)
- **Monitored Entity:** Driver Only
- **Output:** Activity label "drinking", confidence score, alert
- **Dependencies:** PBI-026 (requires trained Activity CNN model)
- **Success Criteria:**
  - Detection accuracy: >85%
  - Confidence threshold: >75% for 2 consecutive frames → alert
  - Detect various containers (bottle, cup, can)

---

#### PBI-021: Smoking Detection

- **Priority:**  MUST HAVE
- **Description:** Detect driver smoking cigarette while driving
- **Technology:** AI/ML (Activity CNN)
- **Monitored Entity:** Driver Only
- **Output:** Activity label "smoking", confidence score, alert
- **Dependencies:** PBI-026 (requires trained Activity CNN model)
- **Success Criteria:**
  - Detection accuracy: >85%
  - Confidence threshold: >70% for 5 consecutive frames (1 second) → alert
  - Detect hand-to-mouth gesture with cigarette

---

#### PBI-022: Yawning Activity Detection

- **Priority:**  MUST HAVE
- **Description:** Detect yawning as dangerous activity using Activity CNN (alternative/complement to PBI-013)
- **Technology:** AI/ML (Activity CNN) or CV (mouth landmarks)
- **Monitored Entity:** Driver Only
- **Output:** Activity label "yawning", count, alert
- **Dependencies:** PBI-026 (Activity CNN) OR PBI-013 (landmark-based)
- **Success Criteria:**
  - Two approaches: CNN-based (PBI-022) and landmark-based (PBI-013)
  - Use both for validation, or choose one based on accuracy
  - Target: >85% accuracy for CNN approach

---

#### PBI-023: Hands Off Wheel Detection

- **Priority:**  MUST HAVE
- **Description:** Detect when driver's hands are not on steering wheel
- **Technology:** AI/ML (Hand detection + Activity CNN) or separate hand tracking module
- **Monitored Entity:** Driver Only
- **Output:** Activity label "hands_off_wheel", duration, alert
- **Dependencies:** PBI-026 (Activity CNN) or separate hand detection model
- **Success Criteria:**
  - Detection accuracy: >80% (challenging due to wheel occlusion)
  - Alert threshold: both hands off wheel >3 seconds → alert, >5 seconds → critical
  - One hand off wheel >10 seconds → warning (acceptable temporarily)

---

#### PBI-024: Arm Out Window Detection

- **Priority:**  MUST HAVE
- **Description:** Detect driver's arm extended out of window
- **Technology:** AI/ML (Activity CNN + pose estimation)
- **Monitored Entity:** Driver Only
- **Output:** Activity label "arm_out_window", duration, alert
- **Dependencies:** PBI-026 (Activity CNN)
- **Success Criteria:**
  - Detection accuracy: >85%
  - Confidence threshold: >75% for 2 seconds → alert
  - Detect arm position outside normal frame bounds

---

#### PBI-025: Looking at Directions Detection

- **Priority:**  MUST HAVE
- **Description:** Detect driver looking at phone/GPS for navigation (head down, gaze at device in lap)
- **Technology:** AI/ML (Activity CNN) + Gaze zone analysis (PBI-010)
- **Monitored Entity:** Driver Only
- **Output:** Activity label "looking_at_directions", duration, alert
- **Dependencies:** PBI-026 (Activity CNN), PBI-010 (gaze zones)
- **Success Criteria:**
  - Combined detection: head pitch <-20° (looking down) + gaze at lap zone
  - Alert threshold: >2 seconds looking at directions → warning
  - Distinguish from dashboard glances (shorter duration, different angle)

---

#### PBI-026: Activity CNN Model Training

- **Priority:**  MUST HAVE
- **Description:** Train deep learning model for activity recognition covering all 7 dangerous activities
- **Technology:** AI/ML (MobileNetV2, EfficientNet-B0, or custom CNN architecture)
- **Monitored Entity:** System
- **Output:** Trained model file (.h5 or .pth), accuracy metrics, confusion matrix
- **Dependencies:** Dataset collection (300+ samples per activity with augmentation)
- **Success Criteria:**
  - Overall accuracy: >85% on test dataset (70% of labeled data)
  - Per-activity accuracy: >85% for each of 7 activities
  - Confusion matrix: no two activities with >15% cross-confusion
  - Inference time: <30ms per frame (enables 30+ FPS)
  - Model size: <20MB for embedded deployment (MobileNetV2)
  - Training dataset: 300+ samples per activity, diverse conditions (lighting, angles, demographics)

---

### Category 7: Driver Enrollment & Identification

> **Purpose:** Identify drivers using face recognition for personalized monitoring and accountability.

---

#### PBI-027: Driver Face Enrollment

- **Priority:** SHOULD HAVE
- **Description:** Enroll new driver by capturing face images and storing facial features (encodings)
- **Technology:** Computer Vision (face encoding - dlib face_recognition or FaceNet)
- **Monitored Entity:** Driver Only
- **Output:** 128D face encoding vector, driver ID, stored in database
- **Dependencies:** PBI-001 (requires face detection)
- **Success Criteria:**
  - Capture 10+ face images during enrollment (angles: center, ±15° left/right, ±10° up/down)
  - Face detection confidence >90% for all captured images
  - Generate 128D encoding vector using dlib/FaceNet
  - Store in database with driver metadata (name, ID, enrollment date)
  - Enrollment time: <30 seconds
  - Duplicate prevention: reject if similarity >0.7 with existing driver

---

#### PBI-028: Driver Identification

- **Priority:** SHOULD HAVE
- **Description:** Identify enrolled driver when they enter vehicle using face recognition
- **Technology:** Computer Vision (face encoding comparison - cosine similarity or Euclidean distance)
- **Monitored Entity:** Driver Only
- **Output:** Driver ID, confidence score, welcome message
- **Dependencies:** PBI-027 (requires enrolled drivers), PBI-001 (requires face detection)
- **Success Criteria:**
  - Identification speed: <100ms per frame
  - Accuracy: >95% for enrolled drivers
  - Similarity threshold: >0.6 = match, <0.6 = unknown driver
  - Handle unknown drivers: prompt for enrollment or continue as "guest"
  - Associate all session events with identified driver ID

---

#### PBI-029: Multi-Driver Management

- **Priority:** SHOULD HAVE
- **Description:** Support multiple enrolled drivers per vehicle (e.g., family car, shared fleet vehicle)
- **Technology:** Database + face recognition
- **Monitored Entity:** Driver Only
- **Output:** Driver profile selection, session association with driver ID
- **Dependencies:** PBI-027, PBI-028 (requires enrollment and identification)
- **Success Criteria:**
  - Support 5-10 enrolled drivers per vehicle
  - Auto-identify driver at session start (first 5 seconds)
  - Allow manual driver selection if auto-identification fails
  - Store per-driver settings (EAR thresholds, alert preferences - future enhancement)
  - Track per-driver statistics (safety score, incident history)

---

### Category 8: Passenger Monitoring

> **Purpose:** Count passengers for compliance tracking (fleet management use case).

---

#### PBI-030: Passenger Counting

- **Priority:** SHOULD HAVE
- **Description:** Count number of passengers in vehicle (front + rear seats)
- **Technology:** Computer Vision (person detection - YOLO v5/v8 or SSD) or depth sensors
- **Monitored Entity:** Driver + Passengers
- **Output:** Passenger count (0-4 typically), seat occupancy map
- **Dependencies:** Additional camera(s) for cabin view, or wide-angle IR camera
- **Success Criteria:**
  - Count accuracy: >90% for stationary passengers
  - Detect passengers in 4 zones: front passenger, rear left, rear center, rear right
  - Update count when passengers enter/exit (detect changes)
  - Use case: fleet compliance (max capacity), insurance, safety analysis

---

#### PBI-031: Passenger Face Detection

- **Priority:**  COULD HAVE
- **Description:** Detect faces of passengers for occupancy verification (enhancement to PBI-030)
- **Technology:** Computer Vision (multi-face detection)
- **Monitored Entity:** Passengers
- **Output:** Face count, face locations (seat positions)
- **Dependencies:** PBI-030 (passenger counting), additional camera or wide-angle lens
- **Success Criteria:**
  - Detect up to 5 faces simultaneously (driver + 4 passengers)
  - Map face locations to seat positions
  - Validation use case: verify passenger count accuracy
  - Privacy consideration: no passenger face recognition, only detection

---

### Category 9: Safety Accessories (Glasses/Mask)

> **Purpose:** Detect accessories that affect detection algorithms and adapt accordingly.

---

#### PBI-032: Glasses Detection

- **Priority:** SHOULD HAVE
- **Description:** Detect if driver is wearing glasses (affects eye detection and EAR thresholds)
- **Technology:** Computer Vision (glasses classifier) or AI/ML
- **Monitored Entity:** Driver Only
- **Output:** Glasses status (yes/no), adjust EAR thresholds if needed
- **Dependencies:** PBI-001 (requires face detection)
- **Success Criteria:**
  - Glasses detection accuracy: >90%
  - Auto-adjust EAR threshold: if glasses detected, reduce threshold by 0.02-0.03 (glasses cause lower EAR)
  - Detect sunglasses separately (may block eye detection)
  - Warning if sunglasses block eye landmarks

---

#### PBI-033: Mask Detection

- **Priority:**  COULD HAVE
- **Description:** Detect if driver is wearing face mask (affects face landmark detection)
- **Technology:** AI/ML (mask classifier - MobileNetV2)
- **Monitored Entity:** Driver Only
- **Output:** Mask status (yes/no), warning if mask interferes with detection
- **Dependencies:** PBI-001 (requires face detection)
- **Success Criteria:**
  - Mask detection accuracy: >90%
  - Warning: if mask detected and mouth landmarks fail, notify driver to remove mask
  - Graceful degradation: disable yawning detection (PBI-013) if mask worn
  - Use case: COVID-19 compliance or post-pandemic monitoring

---

### Category 10: System Health & Camera Management

> **Purpose:** Monitor system health, camera status, and environmental conditions for reliable operation.

---

#### PBI-034: IR Camera Health Check

- **Priority:**  MUST HAVE
- **Description:** Monitor camera connectivity and image quality to ensure monitoring system is operational
- **Technology:** Hardware integration + Computer Vision (frame validation)
- **Monitored Entity:** Camera/System
- **Output:** Camera status (online/offline), image quality metrics (brightness, contrast, blur)
- **Dependencies:** Hardware interface (USB camera)
- **Success Criteria:**
  - Camera connectivity check: detect camera disconnection within 2 seconds
  - Frame validation: check for frozen frames (same frame >2 seconds)
  - Image quality metrics: brightness histogram, blur detection (Laplacian variance)
  - Display "Camera Offline" warning if camera fails
  - Log camera failures for maintenance

---

#### PBI-035: Low Light Detection

- **Priority:** SHOULD HAVE
- **Description:** Detect insufficient lighting conditions affecting detection accuracy
- **Technology:** Computer Vision (brightness histogram analysis)
- **Monitored Entity:** Camera/System
- **Output:** Lighting level (sufficient/insufficient), warning message
- **Dependencies:** PBI-034 (camera health check)
- **Success Criteria:**
  - Brightness analysis: calculate mean/median brightness from histogram
  - Threshold: if mean brightness <30 (0-255 scale) → "Low Light" warning
  - IR camera should handle low light, but warn if IR illumination fails
  - Automatic adjustment: increase camera exposure if possible

---

#### PBI-036: Face Occlusion Detection

- **Priority:** SHOULD HAVE
- **Description:** Detect when face is partially occluded (hand covering face, object, position)
- **Technology:** Computer Vision (landmark confidence analysis)
- **Monitored Entity:** Driver Only
- **Output:** Occlusion status (yes/no), occluded regions (eyes, mouth, etc.), warning
- **Dependencies:** PBI-001 (requires face landmarks with confidence scores)
- **Success Criteria:**
  - Occlusion detection: if >30% of landmarks have confidence <0.5 → occluded
  - Identify occluded regions: eyes, mouth, full face
  - Graceful degradation: if eyes occluded, fall back to head pose only (PBI-006)
  - Warning: "Face partially blocked" if occlusion >5 seconds

---

#### PBI-037: System FPS Monitoring

- **Priority:** SHOULD HAVE
- **Description:** Monitor processing frame rate to ensure real-time performance
- **Technology:** System metrics (time.time() tracking)
- **Monitored Entity:** System
- **Output:** FPS value, performance warnings if below threshold
- **Dependencies:** None (system-level monitoring)
- **Success Criteria:**
  - Target FPS: 15-20 FPS minimum for real-time monitoring
  - FPS calculation: rolling average over 30 frames
  - Warning: if FPS <15 for >5 seconds → "Low Performance" indicator
  - Log FPS drops for optimization analysis
  - Display FPS on dashboard (developer mode)

---

### Category 11: Alert System

> **Purpose:** Deliver timely, prioritized alerts to driver for critical events.

---

#### PBI-038: Real-time Audio Alerts

- **Priority:**  MUST HAVE
- **Description:** Play audio warnings for critical events (drowsiness, distraction, dangerous activities)
- **Technology:** Audio output (pygame/pydub for beep sounds, voice alerts)
- **Monitored Entity:** System
- **Output:** Audio alert played, alert type logged
- **Dependencies:** Alert events from PBI-012, PBI-016, PBI-019-025
- **Success Criteria:**
  - Alert latency: <500ms from event detection to audio playback
  - Audio types: beep (drowsiness), voice warning (distraction), urgent beep (critical)
  - Alert duration: 1-3 seconds (noticeable but not annoying)
  - Volume: adjustable, default 80% system volume
  - Log all alerts with timestamp, event type, driver response time

---

#### PBI-039: Visual Alerts (LED/Dashboard)

- **Priority:** SHOULD HAVE
- **Description:** Display visual warnings on dashboard UI or LED indicators
- **Technology:** Hardware integration (GPIO LED) or GUI display
- **Monitored Entity:** System
- **Output:** Visual alert shown on dashboard, color-coded by severity
- **Dependencies:** PBI-044 (dashboard UI) or GPIO hardware
- **Success Criteria:**
  - Color coding: Green = OK, Yellow = Warning (distraction), Red = Critical (drowsiness)
  - LED patterns: solid (OK), slow blink (warning), fast blink (critical)
  - Dashboard overlay: icon + text message for current alert
  - Synchronize with audio alerts (PBI-038)

---

#### PBI-040: Alert Priority Management

- **Priority:** SHOULD HAVE
- **Description:** Prioritize multiple simultaneous alerts to prevent alert spam
- **Technology:** Rule-based (alert queue management)
- **Monitored Entity:** System
- **Output:** Prioritized alert sequence, spam prevention
- **Dependencies:** All alert-generating PBIs (PBI-012, PBI-016, PBI-019-025)
- **Success Criteria:**
  - Priority order: Drowsiness (critical) > Distraction > Dangerous Activities
  - Alert queue: if multiple events within 2 seconds, play only highest priority
  - Suppression: same alert type not repeated within 10 seconds (unless condition worsens)
  - Log suppressed alerts for analysis

---

### Category 12: Data Logging & Recording

> **Purpose:** Record events and video for analysis, accountability, and evidence.

---

#### PBI-041: Event Logging

- **Priority:**  MUST HAVE
- **Description:** Log all detected events with timestamps to database (drowsiness, distraction, activities, alerts)
- **Technology:** Database (SQLite for local, PostgreSQL for fleet)
- **Monitored Entity:** System
- **Output:** Event records in database with schema: event_id, session_id, event_type, timestamp, severity, confidence, metadata (JSON)
- **Dependencies:** Database schema (see AC-030 from User Stories)
- **Success Criteria:**
  - Event types: drowsiness, distraction, activity (7 types), alert_triggered, system_error
  - Timestamp precision: milliseconds
  - Metadata: JSON field for event-specific data (EAR values, angles, confidence scores)
  - Query performance: <200ms for 10,000+ records with indexes on driver_id, timestamp

---

#### PBI-042: Video Recording (Event-triggered)

- **Priority:** SHOULD HAVE
- **Description:** Record video clips when critical events occur (±30 seconds around event for context)
- **Technology:** Video storage (OpenCV VideoWriter, MP4 encoding with H.264)
- **Monitored Entity:** System
- **Output:** Video files linked to events, stored with timestamps
- **Dependencies:** PBI-041 (event logging to link videos)
- **Success Criteria:**
  - Trigger conditions: drowsiness alert, critical distraction, dangerous activity
  - Recording duration: 30 seconds before + 30 seconds after event (60s total)
  - Video format: MP4, 720p, 10 FPS (low storage requirements)
  - Storage: video_path stored in event metadata (PBI-041)
  - Auto-deletion: remove videos older than 30 days or when storage >90%
  - Privacy: event-triggered only (not continuous recording)

---

#### PBI-043: Session Tracking

- **Priority:** SHOULD HAVE
- **Description:** Track driving sessions (start/end time, driver ID, trip duration, total events)
- **Technology:** Database (session table)
- **Monitored Entity:** System
- **Output:** Session records with schema: session_id, driver_id, start_time, end_time, vehicle_id, total_events, video_path
- **Dependencies:** PBI-028 (driver identification), PBI-041 (event logging)
- **Success Criteria:**
  - Session auto-start: when driver identified or manual start
  - Session auto-end: when vehicle turned off or after 5 minutes no face detected
  - Trip summary: total duration, event counts by type, safety score
  - Link all events to session_id for trip-based analysis

---

### Category 13: Dashboard & User Interface

> **Purpose:** Real-time monitoring interface and historical analytics for drivers and fleet managers.

---

#### PBI-044: Live Monitoring Dashboard

- **Priority:**  MUST HAVE
- **Description:** Real-time UI showing camera feed, detection overlays, current status
- **Technology:** GUI framework (OpenCV window, Qt, or web-based with Flask/React)
- **Monitored Entity:** System
- **Output:** Visual interface with face/eye/gaze overlays, status indicators, current alerts
- **Dependencies:** All detection PBIs (PBI-001 to PBI-018)
- **Success Criteria:**
  - Display elements:
    - Camera feed with overlays (face box, eye landmarks, gaze direction)
    - Status indicators: drowsiness level, attention score, current activity
    - Alert panel: current alert message, severity color-coded
    - System health: FPS, camera status, driver ID
  - Update rate: 10-15 FPS for UI (can be lower than processing FPS)
  - Overlay colors: Green = OK, Yellow = Warning, Red = Critical
  - Keyboard controls: q=quit, s=start/stop, r=reset, c=calibrate

---

#### PBI-045: Historical Analytics Dashboard

- **Priority:**  COULD HAVE
- **Description:** View past trips, event statistics, driver behavior trends over time
- **Technology:** Web dashboard (Flask + React) or desktop app (Qt + matplotlib)
- **Monitored Entity:** System
- **Output:** Charts/graphs of events over time, driver safety scores, trip summaries
- **Dependencies:** PBI-041, PBI-043 (requires event and session data)
- **Success Criteria:**
  - Trip list: view all past sessions with date, duration, event counts
  - Trip details: click to see event timeline, video clips (PBI-042)
  - Analytics charts:
    - Events over time (line chart: drowsiness, distraction, activities per day/week)
    - Event type distribution (pie chart)
    - Driver comparison (bar chart: safety scores for multiple drivers)
  - Filters: date range, driver ID, event type
  - Export: CSV export of event data for external analysis

---

## MoSCoW Prioritization Summary

###  MUST HAVE (24 items) - MVP for Thesis Graduation

**Core Detection (Foundation):**
- PBI-001: Face Detection & Tracking
- PBI-002: Eye Region Detection
- PBI-003: Eye Openness Detection (EAR)
- PBI-004: Blink Frequency Monitoring
- PBI-005: Eye Location Tracking
- PBI-006: Head Pose Estimation
- PBI-007: Head Location Tracking
- PBI-008: Head Zone Classification
- PBI-009: Gaze Direction Estimation
- PBI-010: Gaze Zone Classification

**Safety Detection (Core Features):**
- PBI-012: Drowsiness Detection (EAR-based)
- PBI-013: Yawning Detection
- PBI-014: Microsleep Detection
- PBI-016: Head Turn Distraction
- PBI-017: Gaze-off-Road Detection

**Dangerous Activities (All 7 + Model):**
- PBI-019: Phone Calling Detection
- PBI-020: Drinking Detection
- PBI-021: Smoking Detection
- PBI-022: Yawning Activity Detection
- PBI-023: Hands Off Wheel Detection
- PBI-024: Arm Out Window Detection
- PBI-025: Looking at Directions Detection
- PBI-026: Activity CNN Model Training

**System Infrastructure:**
- PBI-034: IR Camera Health Check
- PBI-038: Real-time Audio Alerts
- PBI-041: Event Logging
- PBI-044: Live Monitoring Dashboard

**Total:** 24 items

---

### SHOULD HAVE (17 items) - Important Enhancements

**Enhanced Detection:**
- PBI-011: Pupil Detection & Tracking (improves gaze accuracy)
- PBI-015: PERCLOS Calculation (scientific validation)
- PBI-018: Attention Score Calculation (overall metric)

**Driver Management:**
- PBI-027: Driver Face Enrollment
- PBI-028: Driver Identification
- PBI-029: Multi-Driver Management

**Passenger & Accessories:**
- PBI-030: Passenger Counting
- PBI-032: Glasses Detection

**System Health:**
- PBI-035: Low Light Detection
- PBI-036: Face Occlusion Detection
- PBI-037: System FPS Monitoring

**Alerts & Recording:**
- PBI-039: Visual Alerts (LED/Dashboard)
- PBI-040: Alert Priority Management
- PBI-042: Video Recording (Event-triggered)
- PBI-043: Session Tracking

**Total:** 17 items

---

###  COULD HAVE (4 items) - Nice-to-Have Features

**Advanced Features:**
- PBI-031: Passenger Face Detection (enhances PBI-030)
- PBI-033: Mask Detection (post-COVID scenario)
- PBI-045: Historical Analytics Dashboard (fleet management)

**Total:** 4 items

---

### WON'T HAVE - Explicitly Out of Scope

- **Safety Belt Detection:** Removed per scope decision (not required for thesis)
- **Facial Expression Analysis:** Too complex, low priority
- **Cloud Sync / Fleet Server:** Local-only for thesis scope
- **OTA (Over-The-Air) Updates:** Manual updates only
- **Mobile App:** Desktop UI only
- **CAN Bus Integration:** Manual system start/stop
- **Multi-Camera Support:** Single IR camera only

---

## Technology Stack

### Computer Vision & AI/ML

- **OpenCV:** Face detection, image processing, video I/O
- **dlib:** 68-point facial landmarks, face recognition encodings
- **MediaPipe:** Alternative face mesh (468 landmarks), iris tracking (PBI-011)
- **MobileNetV2 / EfficientNet-B0:** Activity recognition CNN (PBI-026)
- **FaceNet / dlib face_recognition:** Driver identification (PBI-027, PBI-028)
- **YOLO v5/v8 or SSD:** Passenger detection (PBI-030)

### Hardware

- **IR Camera:** USB IR camera for day/night operation (e.g., 720p 30 FPS with IR LEDs)
- **Processing Unit:** Jetson Nano ($100) or Raspberry Pi 4 8GB ($75)
- **Optional:** GPIO LED for visual alerts (PBI-039)

### Software Framework

- **Language:** Python 3.7+ (primary)
- **Database:** SQLite (local), optional PostgreSQL (fleet)
- **GUI:** OpenCV window (quick prototype), Qt/PyQt5 (production UI), or Flask + React (web-based)
- **Audio:** pygame or pydub for alert sounds
- **Video Recording:** OpenCV VideoWriter with H.264 codec

### Development & Deployment

- **Version Control:** Git + GitHub/GitLab
- **Model Training:** TensorFlow/Keras or PyTorch
- **Testing:** pytest (unit tests), test datasets with ground truth labels
- **Documentation:** Sphinx (code docs), Markdown (user manual)

---

## Notes for Implementation

### Critical Success Factors

1. **Real-time Performance:** Achieve 15+ FPS with all MUST HAVE modules running
2. **Drowsiness Accuracy:** >90% true positive rate, <1 false alert/hour
3. **Activity CNN Training:** Collect 300+ samples per activity with data augmentation
4. **Robust Detection:** Multi-modal validation (combine head pose + gaze + EAR)
5. **User Acceptance:** Tune thresholds to minimize false positives (alert fatigue)

### Development Timeline

- **Estimated Duration:** 10-20 weeks
- **Sprints:** 5-10 sprints (2-week sprints)
- **Phase 1 (4-5 weeks):** Core detection (PBI-001 to PBI-010)
- **Phase 2 (3-4 weeks):** Drowsiness & distraction (PBI-012 to PBI-018)
- **Phase 3 (4-5 weeks):** Activity recognition (PBI-019 to PBI-026)
- **Phase 4 (2-3 weeks):** System integration, alerts, dashboard (PBI-034, PBI-038, PBI-041, PBI-044)
- **Phase 5 (2-3 weeks):** Testing, optimization, documentation

### Testing Requirements

- **Unit Tests:** Each detection module (PBI-001 to PBI-026)
- **Integration Tests:** End-to-end pipeline performance
- **Test Datasets:**
  - Drowsiness: 100+ labeled instances (yawning, eye closure)
  - Activities: 700 instances (100 per activity × 7)
  - Distraction: 50+ instances (head turns, gaze-off)
- **Field Testing:** 5-10 real driving sessions (1-2 hours each)
- **Performance Testing:** 8-hour continuous operation (stress test)

### Risk Mitigation

1. **Performance Bottleneck:** Optimize CNN models (quantization, pruning), use threading
2. **False Alert Fatigue:** Conservative thresholds initially, tune based on user feedback
3. **Activity CNN Accuracy:** Collect diverse dataset (300+ samples/activity), data augmentation
4. **EAR Demographic Bias:** Per-driver calibration during enrollment (PBI-027)
5. **Camera Occlusion:** Graceful degradation (use head pose if eyes blocked)

---

## Document Metadata

- **Generated by:** BMAD Brainstorming Workflow
- **Session Date:** 2026-03-03
- **Session File:** `brainstorming-session-2026-03-03-004815.md`
- **Exported:** 2026-03-04
- **Format:** Markdown (Full Details)
- **Total PBIs:** 45 items across 13 categories
- **Document Version:** 1.0

---

## Next Steps

1. **Review & Validate:** Review this Product Backlog with thesis advisor
2. **Create User Stories:** Map PBIs to User Stories (already done in brainstorming session)
3. **Define Acceptance Criteria:** Testable criteria for each PBI (already done for priority stories)
4. **Architecture Design:** Design system architecture based on modular pipeline (PBI-028 reference)
5. **Database Schema:** Design schema for event logging, session tracking, driver management
6. **Sprint Planning:** Create Sprint Backlog using 10-20 week timeline
7. **Start Development:** Begin with Phase 1 (Core Detection - PBI-001 to PBI-010)

---

*End of Product Backlog Document*
