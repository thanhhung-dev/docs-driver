---
stepsCompleted: ['step-01-validate-prerequisites', 'step-02-design-epics', 'step-03-create-stories', 'step-04-final-validation']
inputDocuments: 
  - _bmad-output/planning-artifacts/prd/index.md
  - _bmad-output/architecture/ARCHITECTURE-Driver-Monitoring-System.md
  - _bmad-output/ui-design/UI-INTERFACE-DESIGN-Driver-Monitoring-System.md
---

# docs-driver - Epic Breakdown

## Overview

This document provides the complete epic and story breakdown for docs-driver, decomposing the requirements from the PRD, UX Design, and Architecture requirements into implementable stories.

## Requirements Inventory

### Functional Requirements

*   **FR1:** The system MUST be able to capture video input from a connected IR camera.
*   **FR2:** The system MUST be able to pre-process video frames (e.g., grayscale conversion, contrast adjustment) for detection.
*   **FR3:** The system MUST be able to detect the driver's face in the video frames.
*   **FR4:** The system MUST be able to estimate the driver's head pose (pitch, yaw, roll).
*   **FR5:** The system MUST be able to track eye state (e.g., open/closed, EAR ratio).
*   **FR6:** The system MUST be able to detect yawning behavior.
*   **FR7:** The system MUST be able to determine gaze direction.
*   **FR8:** The system MUST be able to synthesize data from face detection, head pose, eye state, and yawning to assess drowsiness levels.
*   **FR9:** The system MUST be able to synthesize data from head orientation and gaze to assess distraction levels.
*   **FR10:** The system MUST be able to identify "microsleep" events.
*   **FR10.1:** The system MUST be able to detect driver **phone usage** (calling).
*   **FR10.2:** The system MUST be able to detect driver **drinking** from a bottle/cup.
*   **FR10.3:** The system MUST be able to detect driver **smoking**.
*   **FR10.4:** The system MUST be able to detect **yawning behavior** as an activity.
*   **FR10.5:** The system MUST be able to detect when **hands are off the steering wheel**.
*   **FR10.6:** The system MUST be able to detect when **hands are out the window**.
*   **FR10.7:** The system MUST be able to detect driver **looking at navigation devices** (phone/GPS).
*   **FR11:** The system MUST be able to trigger early, gentle alerts (e.g., light sound, LED color change) when initial signs of drowsiness or distraction are detected.
*   **FR12:** The system MUST be able to trigger clear, urgent emergency alerts (e.g., rapid sound, flashing LED) when high-risk situations (microsleep or dangerous behaviors) are detected.
*   **FR13:** The system MUST be able to log details of every alert event (type, time, level, metrics) to a file or database.
*   **FR14:** The system MUST be able to store a snapshot image at the time of an emergency alert.
*   **FR15:** Users MUST be able to access and review recorded event logs.
*   **FR16:** Users MUST be able to review stored evidence images.
*   **FR17:** The system MUST be able to load and apply configuration parameters (e.g., alert thresholds, sensitivity) from a file.
*   **FR18:** The system MUST be able to adjust detection and alert sensitivity via configuration.

### NonFunctional Requirements

*   **NFR1: Processing Speed:** The system MUST process and analyze video at a minimum of **15 FPS**.
*   **NFR2: Alert Latency:** Time from detection to alert trigger MUST be under **200 milliseconds**.
*   **NFR3: Resource Efficiency:** The system MUST run stably on edge hardware (Jetson Nano/RPi 4).
*   **NFR4: Continuous Operation:** The system MUST operate continuously for at least **4 hours**.
*   **NFR5: Video Input Error Handling:** Clear alerts for video stream interruption and automatic recovery attempts.
*   **NFR6: False Positive Mitigation:** Maintain false positive rate below **5%**.
*   **NFR7: Configurability:** Allow threshold and sensitivity adjustment via configuration file.

### Additional Requirements

#### From Architecture Document
*   **Architecture Pattern:** Pipeline Architecture (Pipes and Filters).
*   **Tech Stack:** Python 3.8, OpenCV 4.5, dlib, TensorFlow Lite, SQLite3.
*   **Hardware:** Jetson Nano or Raspberry Pi 4.
*   **Data Models:** Defined contracts for `detection_results` and `risk_event` objects.
*   **Database Schema:** SQLite schema for event logging (event_id, session_id, type, timestamp, data).
*   **Modularity:** Independent layers for Input, Detection, Analysis, Action, and Storage.

#### From UX Design Document
*   **UI Framework:** PyQt5 for 800x480 (7-inch) or 1024x600 (10-inch) displays.
*   **Alert Hierarchy:** 4-level hierarchy (Critical, High, Medium, Info) with specific colors and sounds.
*   **Safety Lock:** Settings screen accessible only when the vehicle is parked.
*   **Dashboard Components:** Live video feed, status indicators (EAR, Drowsiness, Attention), and event timeline.

### FR Coverage Map

FR1: Epic 1 - Video capture from IR camera
FR2: Epic 1 - Video pre-processing
FR3: Epic 1 - Face detection and tracking
FR4: Epic 1 - Head pose estimation
FR5: Epic 1 - Eye state tracking
FR6: Epic 1 - Yawn detection from EAR
FR7: Epic 1 - Gaze direction determination
FR8: Epic 2 - Drowsiness assessment synthesis
FR9: Epic 2 - Distraction assessment synthesis
FR10: Epic 2 - Microsleep event identification
FR10.1: Epic 3 - Phone usage detection
FR10.2: Epic 3 - Drinking/Eating recognition
FR10.3: Epic 3 - Smoking detection
FR10.4: Epic 3 - Yawning activity recognition
FR10.5: Epic 3 - Hands-off wheel detection
FR10.6: Epic 3 - Hands out window detection
FR10.7: Epic 3 - Looking at navigation device detection
FR11: Epic 2 - Early/Gentle alert triggering
FR12: Epic 2 - Emergency/Urgent alert triggering
FR13: Epic 4 - Alert event logging (SQLite)
FR14: Epic 4 - Evidence image storage (snapshots)
FR15: Epic 4 - Access and review event logs
FR16: Epic 4 - Review evidence images
FR17: Epic 5 - Configuration loading and application
FR18: Epic 5 - Threshold and sensitivity adjustment

## Epic List

### Epic 1: Core System & Visual Perception
Hệ thống có khả năng khởi tạo, thu nhận video từ camera hồng ngoại và thực hiện các nhận diện khuôn mặt, mắt, đầu cơ bản để làm nền tảng cho mọi phân tích sau này.
**FRs covered:** FR1, FR2, FR3, FR4, FR5, FR6, FR7.

### Epic 2: State Analysis & Alerting System
Hệ thống phân tích các dữ liệu nền tảng để xác định mức độ buồn ngủ, mất tập trung và đưa ra các cảnh báo vật lý (âm thanh, LED) cũng như trên giao diện.
**FRs covered:** FR8, FR9, FR10, FR11, FR12.

### Epic 3: Specific Dangerous Activity Recognition
Tích hợp các mô hình AI chuyên biệt để phát hiện 7 hành vi nguy hiểm cụ thể như dùng điện thoại, hút thuốc, uống nước, v.v.
**FRs covered:** FR10.1, FR10.2, FR10.3, FR10.4, FR10.5, FR10.6, FR10.7.

### Epic 4: Data Logging & Evidence Management
Hệ thống tự động ghi lại nhật ký các sự kiện cảnh báo và lưu trữ hình ảnh bằng chứng vào cơ sở dữ liệu SQLite.
**FRs covered:** FR13, FR14, FR15, FR16.

### Epic 5: UI & Configuration Management
Cung cấp bảng điều khiển (Dashboard) trực quan và giao diện cài đặt để điều chỉnh các ngưỡng nhạy của hệ thống.
**FRs covered:** FR17, FR18.

---

## Epic 1: Core System & Visual Perception
Goal: Initialize the system, capture and process video, and perform foundational image detection.

### Story 1.1: Project Scaffolding and Video Capture Setup
As a **Developer**,
I want **to set up the initial project structure and capture a continuous video stream from an IR camera**,
So that **I have a modular foundation and input data for driver analysis**.

**Acceptance Criteria:**
**Given** the target hardware (Jetson Nano/RPi 4) and the Architecture design
**When** the developer initializes the project
**Then** the system MUST follow the directory structure defined in the Architecture (Input, Detection, Analysis, Action, Storage).
**And** the environment MUST be configured with Python 3.8 and required libraries (OpenCV, etc.).
**And** the system MUST successfully open a video stream at 640x480 resolution.
**And** the frame capture rate MUST be at least 15 FPS (NFR1).
**And** if the camera is not connected, the system MUST return a specific error (NFR5).

### Story 1.2: Image Pre-processing Pipeline
As a **DMS System**,
I want **to pre-process raw frames (grayscale, contrast)**,
So that **detection modules receive optimized input**.

**Acceptance Criteria:**
**Given** a raw BGR frame from Story 1.1
**When** passed through the pre-processing module
**Then** the frame MUST be converted to grayscale.
**And** contrast MUST be enhanced (e.g., using CLAHE) to handle low-light conditions.
**And** the resulting frame MUST be ready for the Detection Layer.

### Story 1.3: Face Detection and Tracking
As a **DMS System**,
I want **to detect and track the driver's face in real-time**,
So that **facial landmarks can be extracted for analysis**.

**Acceptance Criteria:**
**Given** a pre-processed frame from Story 1.2
**When** processed by the Face Detector module
**Then** the system MUST return the bounding box coordinates of the driver's face.
**And** the system MUST be capable of tracking the face across consecutive frames.
**And** if no face is found after 2 seconds, the system MUST report a "Driver Not Found" status.

### Story 1.4: Facial Landmark Extraction
As a **DMS System**,
I want **to extract 68 facial landmarks from the detected face**,
So that **features like eyes and mouth can be analyzed**.

**Acceptance Criteria:**
**Given** face coordinates from Story 1.3
**When** processed by the Landmark Predictor module
**Then** the system MUST return 68 (x, y) coordinates mapping eyes, nose, mouth, and jawline.
**And** landmark extraction latency MUST be under 50ms to ensure overall performance.

### Story 1.5: Head Pose Estimation
As a **DMS System**,
I want **to calculate head orientation (pitch, yaw, roll)**,
So that **I can determine if the driver is looking away**.

**Acceptance Criteria:**
**Given** 68 facial landmarks from Story 1.4
**When** processed by the Pose Estimator module (using PnP algorithm with a standard 3D model)
**Then** the system MUST calculate Pitch, Yaw, and Roll angles in degrees.
**And** the estimation error MUST be less than 5 degrees under normal lighting.

### Story 1.6: Eye and Mouth Feature Tracking (EAR & MAR)
As a **DMS System**,
I want **to calculate EAR (Eye Aspect Ratio) and MAR (Mouth Aspect Ratio)**,
So that **drowsiness and yawning can be detected**.

**Acceptance Criteria:**
**Given** eye and mouth landmarks from Story 1.4
**When** processed by the Feature Tracker module
**Then** the system MUST return EAR values for both left and right eyes.
**And** the system MUST return MAR values to identify mouth openness for yawning.
And these values MUST be updated continuously for every frame.

---

## Epic 2: State Analysis & Alerting System
Goal: Analyze perception data to determine risk levels and trigger appropriate physical and visual alerts.

### Story 2.1: Drowsiness Level Assessment
As a **DMS System**,
I want **to calculate a drowsiness score based on EAR and yawning frequency**,
So that **I can identify when a driver is becoming tired**.

**Acceptance Criteria:**
**Given** continuous EAR and MAR data from Epic 1
**When** EAR values are below threshold (e.g., 0.25) for a period or frequent yawning is detected
**Then** the system MUST calculate a drowsiness score (0-100%).
**And** the system MUST maintain a false positive rate below 5% under normal conditions (NFR6).

### Story 2.2: Distraction Level Assessment
As a **DMS System**,
I want **to calculate an attention score based on head pose and gaze**,
So that **I can identify when a driver is not looking at the road**.

**Acceptance Criteria:**
**Given** head pose (pitch, yaw) and gaze direction data from Epic 1
**When** the driver turns their head beyond the threshold (e.g., >30 degrees) or looks away for too long
**Then** the system MUST trigger an "Inattentive" (Distracted) state.
**And** the attention score MUST be updated in real-time.

### Story 2.3: Microsleep Event Detection
As a **DMS System**,
I want **to detect "microsleep" events (eyes closed for >1 second)**,
So that **I can trigger high-priority emergency alerts**.

**Acceptance Criteria:**
**Given** continuous EAR data from Epic 1
**When** EAR values stay below the "closed eye" threshold for more than 1 second (or configured threshold)
**Then** the system MUST immediately generate a "Microsleep" risk event.
**And** this event MUST have the highest priority level (Critical).

### Story 2.4: Alert Hierarchy Management
As a **DMS System**,
I want **to manage a 4-level alert hierarchy (Critical, High, Medium, Info)**,
So that **alerts are proportional to the risk detected**.

**Acceptance Criteria:**
**Given** a detected risk event (Drowsiness, Distraction, Microsleep)
**When** the Alert Manager module processes the event
**Then** the system MUST assign the correct alert level according to definitions (e.g., Microsleep -> Critical, Prolonged Yawn -> High).
**And** higher priority alerts MUST override any lower priority alerts currently in progress.

### Story 2.5: Physical and Visual Alert Triggering
As a **DMS System**,
I want **to trigger audio beeps and LED signals alongside UI alerts**,
So that **the driver is effectively warned even if not looking at the screen**.

**Acceptance Criteria:**
**Given** an active alert event (from Story 2.4)
**When** the alert level is "Critical"
**Then** the UI MUST display a red flashing overlay.
**And** the speaker MUST play an urgent rapid beep.
**And** the LED MUST blink rapidly.
And the total latency from detection to alert trigger MUST be under 200ms (NFR2).

---

## Epic 3: Specific Dangerous Activity Recognition
Goal: Implement specialized AI models to detect specific high-risk behaviors beyond basic physiological signs.

### Story 3.1: Phone Usage Detection
As a **DMS System**,
I want **to recognize when the driver is holding a phone to their ear**,
So that **I can alert for illegal phone usage**.

**Acceptance Criteria:**
**Given** a video frame from the Detection Layer
**When** the Activity Recognizer (TensorFlow Lite) identifies the "Calling" pattern
**Then** the system MUST generate a "Dangerous Activity: Phone" risk event.
**And** this alert MUST be assigned a "High" or "Critical" priority.

### Story 3.2: Drinking/Eating Recognition
As a **DMS System**,
I want **to detect when the driver is drinking from a bottle or cup**,
So that **I can alert for multi-tasking while driving**.

**Acceptance Criteria:**
**Given** a video frame from the Detection Layer
**When** the model detects a bottle/cup near the driver's mouth area
**Then** the system MUST generate a "Dangerous Activity: Drinking" risk event.

### Story 3.3: Smoking Detection
As a **DMS System**,
I want **to detect if the driver is smoking**,
So that **safety alerts can be triggered for restricted environments**.

**Acceptance Criteria:**
**Given** a video frame from the Detection Layer
**When** the Activity Recognizer identifies smoking behavior
**Then** the system MUST generate a "Dangerous Activity: Smoking" risk event.

### Story 3.4: Yawning Activity Recognition
As a **DMS System**,
I want **to detect yawning behavior as a distinct activity**,
So that **I can trigger alerts for prolonged yawning**.

**Acceptance Criteria:**
**Given** a video frame from the Detection Layer
**When** the Activity Recognizer identifies yawning behavior (complementing EAR/MAR analysis)
**Then** the system MUST generate a "Dangerous Activity: Yawn" risk event.

### Story 3.5: Hands-Off Wheel Detection
As a **DMS System**,
I want **to detect when the driver's hands are not on the steering wheel**,
So that **I can alert for lack of vehicle control**.

**Acceptance Criteria:**
**Given** a video frame including the steering wheel area
**When** no hands are detected on the steering wheel for more than 5 seconds
**Then** the system MUST generate a "Dangerous Activity: Hands-Off" risk event.

### Story 3.6: Hands Out Window Detection
As a **DMS System**,
I want **to detect when the driver's hands are out the window**,
So that **I can alert for dangerous driving behavior**.

**Acceptance Criteria:**
**Given** a video frame from the Detection Layer
**When** the driver's hand is detected outside the window area
**Then** the system MUST generate a "Dangerous Activity: Hands Out" risk event.

### Story 3.7: Looking at Navigation Device Detection
As a **DMS System**,
I want **to detect driver looking at navigation devices (phone/GPS)**,
So that **I can alert for distraction**.

**Acceptance Criteria:**
**Given** a video frame from the Detection Layer
**When** head or gaze is detected towards the navigation device area for more than 3 seconds
Then the system MUST generate a "Dangerous Activity: Looking at Device" risk event.

---

## Epic 4: Data Logging & Evidence Management
Goal: Persist trip events and visual evidence for future review and auditing.

### Story 4.1: SQLite Database Integration
As a **DMS System**,
I want **to store alert events in a local SQLite database**,
So that **a record of the trip is maintained**.

**Acceptance Criteria:**
**Given** an alert event has ended
**When** the Storage module processes the event
**Then** the event details (ID, timestamp, risk type, level, metric data) MUST be saved into the `alert_events` table in SQLite.
**And** the data MUST be stored persistently across system restarts.

### Story 4.2: Evidence Image Capture
As a **DMS System**,
I want **to save a JPEG snapshot for every Critical alert**,
So that **the event can be visually verified later**.

**Acceptance Criteria:**
**Given** a "Critical" priority alert is triggered
**When** the alert starts triggering
**Then** the system MUST capture the current video frame and save it as a `.jpg` file in the `/evidence` folder.
**And** the image file path MUST be linked to the corresponding record in the SQLite database.

### Story 4.3: History Review UI (Log and Evidence Review)
As an **Administrator (Lecturer/Evaluator)**,
I want **to view a list of past alert events and their associated images**,
So that **I can assess the driver's performance**.

**Acceptance Criteria:**
**Given** the user opens the History screen on the UI
**When** data is loaded from the SQLite database
**Then** the UI MUST display a list of all recorded alerts (timestamp, risk type, level).
**And** when a specific alert is selected, the system MUST display the associated evidence image (if available).
And the system MUST support smooth navigation between records.

---

## Epic 5: UI & Configuration Management
Goal: Provide the primary user interface and allow customization of system behavior.

### Story 5.1: Real-time Monitoring Dashboard (Live Video & Gauges)
As a **User**,
I want **to see the live video feed with detection overlays (face box, landmarks)**,
So that **I can verify the system is working correctly**.

**Acceptance Criteria:**
**Given** the DMS application is running on the main Dashboard
**When** the video stream is received from Story 1.1
**Then** the UI MUST display the live video with graphic overlays (face bounding box, landmarks).
**And** the real-time gauges (EAR, Drowsiness Level, Attention Score) MUST be updated continuously.
**And** the UI MUST maintain optimal performance without reducing processing FPS (NFR1).

### Story 5.2: Configuration Loading and Management (YAML)
As a **Developer/Admin**,
I want **to load system thresholds from a YAML file**,
So that **I can tune the system without recompiling code**.

**Acceptance Criteria:**
**Given** a `config.yaml` file exists in the configuration directory
**When** the application starts
**Then** all thresholds (EAR_MIN, ALERT_COOLDOWN, volume, etc.) MUST be loaded and applied system-wide.
**And** if the config file is corrupted or missing, the system MUST use safe default values (NFR7).

### Story 5.3: Settings UI for Threshold Tuning (Safety Lock)
As an **Authorized User (when parked)**,
I want **to adjust sensitivity thresholds via a slider interface**,
So that **I can customize the system for different drivers**.

**Acceptance Criteria:**
**Given** the vehicle is in a "Parked" state
**When** the user opens the Settings screen
**Then** the system MUST provide sliders for EAR, Attention, and Volume.
**And** changes MUST be saved back to the `config.yaml` file upon confirmation.
**And** if the vehicle is not parked, the system MUST lock the settings screen (Safety Lock).

### Story 5.4: System Status and Health Dashboard (FPS, CPU, Temp)
As a **User**,
I want **to see the system's performance metrics (FPS, CPU, Temp)**,
So that **I can ensure the hardware is not overheating or overloaded**.

**Acceptance Criteria:**
**Given** the System Status screen is open
**When** the system collects hardware metrics
**Then** the UI MUST display the current FPS, CPU/Memory usage, and hardware temperature.
**And** the connectivity status of devices (Camera, GPIO) MUST be clearly shown (UX: Hardware Status).




