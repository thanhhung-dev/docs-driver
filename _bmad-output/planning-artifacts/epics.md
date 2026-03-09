---
stepsCompleted:
  - step-01-validate-prerequisites
  - step-02-design-epics
inputDocuments:
  - _bmad-output/planning-artifacts/prd.md
  - _bmad-output/architecture/ARCHITECTURE-Driver-Monitoring-System.md
  - _bmad-output/ui-design/UI-INTERFACE-DESIGN-Driver-Monitoring-System.md
---

# docs-driver - Epic Breakdown

## Overview

This document provides the complete epic and story breakdown for docs-driver, decomposing the requirements from the PRD, UX Design if it exists, and Architecture requirements into implementable stories.

## Requirements Inventory

### Functional Requirements

FR1: Phát hiện buồn ngủ dựa trên EAR (Eye Aspect Ratio).
FR2: Phát hiện ngáp dựa trên MAR (Mouth Aspect Ratio).
FR3: Tính toán PERCLOS (Percentage of Eye Closure) theo thời gian thực.
FR4: Phát hiện xao nhãng dựa trên Head Pose (Pitch, Yaw, Roll).
FR5: Theo dõi hướng nhìn (Gaze tracking).
FR6: Nhận diện 7 hành vi nguy hiểm (gọi điện, hút thuốc, uống nước, xao nhãng...).
FR7: Cảnh báo âm thanh (Audio alert) khi có rủi ro.
FR8: Cảnh báo hình ảnh (Visual alert) trên dashboard.
FR9: Cảnh báo qua đèn LED (GPIO interface).
FR10: Phân cấp mức độ ưu tiên cảnh báo (Critical, Warning, Info).
FR11: Đăng ký tài xế mới (Face Enrollment - 5 góc chụp).
FR12: Xác thực tài xế (Face Identification) khi khởi hành.
FR13: Ghi nhật ký sự kiện (Event Logging) vào SQLite.
FR14: Lưu trữ ảnh chụp vi phạm (Snapshots).
FR15: Hiển thị Dashboard giám sát thời gian thực.
FR16: Hiển thị chỉ số FPS và trạng thái hệ thống.
FR17: Màn hình cài đặt ngưỡng (Settings) cho EAR, MAR, Head Pose.
FR18: Màn hình tóm tắt chuyến đi (Trip Summary).
FR19: Cơ chế tự kiểm tra phần cứng (Camera Health Check).
FR20: Cơ chế tự khởi động lại (Watchdog) khi tiến trình AI treo.

### NonFunctional Requirements

NFR1: Tốc độ xử lý ≥ 15 FPS trên thiết bị nhúng (Jetson Nano/RPi 4).
NFR2: Độ trễ cảnh báo (Latency) < 100ms từ lúc thu hình đến lúc báo động.
NFR3: Độ chính xác phát hiện buồn ngủ ≥ 90%.
NFR4: Độ chính xác nhận diện hành vi nguy hiểm ≥ 85%.
NFR5: Hoạt động ổn định trong điều kiện thiếu sáng (< 10 lux) với Camera IR.
NFR6: Xử lý được các trường hợp tài xế đeo kính hoặc khẩu trang.
NFR7: Quyền riêng tư: Xử lý tại biên (Edge AI), không lưu video thô.
NFR8: Giao diện tối giản, hỗ trợ điều khiển cảm ứng (Touch-friendly).
NFR9: Hệ thống chịu lỗi: Tự phục hồi sau khi mất điện đột ngột.

### Additional Requirements

- **Kiến trúc:** Sử dụng mô hình Pipeline (Input -> Detection -> Analysis -> Action).
- **Hạ tầng:** NVIDIA Jetson Nano 4GB hoặc Raspberry Pi 4 8GB, Camera IR USB.
- **Công nghệ:** Python 3.8, OpenCV 4.5, dlib 19.22, TensorFlow Lite 2.8.
- **Giao diện:** PyQt5 cho Desktop GUI, tích hợp Video feed từ OpenCV.
- **Lưu trữ:** SQLite cho dữ liệu sự kiện, YAML cho tệp cấu hình.
- **Hệ thống nhúng:** Sử dụng thư viện GPIO (Jetson.GPIO/RPi.GPIO) để điều khiển LED.

### FR Coverage Map

FR1: Epic 2 - Phát hiện buồn ngủ qua EAR
FR2: Epic 2 - Phát hiện ngáp qua MAR
FR3: Epic 2 - Tính toán chỉ số PERCLOS
FR4: Epic 3 - Phát hiện xao nhãng qua Head Pose
FR5: Epic 3 - Theo dõi hướng nhìn (Gaze)
FR6: Epic 4 - Nhận diện 7 hành vi nguy hiểm
FR7: Epic 2 - Cảnh báo âm thanh
FR8: Epic 2 - Cảnh báo hình ảnh trên Dashboard
FR9: Epic 2 - Cảnh báo qua đèn LED
FR10: Epic 2 - Phân cấp mức độ ưu tiên cảnh báo
FR11: Epic 1 - Đăng ký khuôn mặt tài xế (Enrollment)
FR12: Epic 1 - Xác thực khuôn mặt tài xế (ID)
FR13: Epic 5 - Ghi nhật ký vào SQLite
FR14: Epic 5 - Lưu ảnh chụp vi phạm (Snapshots)
FR15: Epic 5 - Hiển thị Dashboard giám sát
FR16: Epic 1 - Hiển thị FPS và trạng thái hệ thống
FR17: Epic 6 - Màn hình cài đặt ngưỡng (Settings)
FR18: Epic 5 - Màn hình tóm tắt chuyến đi (Trip Summary)
FR19: Epic 1 - Tự kiểm tra phần cứng (Health Check)
FR20: Epic 1 - Cơ chế tự phục hồi (Watchdog)

## Epic List

### Epic 1: Thiết lập Hệ thống & Xác thực Người lái (System Foundation & Driver Auth)
Thiết lập bộ khung phần mềm, giao diện cơ bản và khả năng nhận diện tài xế để khởi động phiên làm việc an toàn.
**Epic Goal:** Driver can register their information, and the system identifies who is driving to personalize the data and ensures system stability.

### Epic 2: Giám sát Buồn ngủ & Cảnh báo Tức thì (Drowsiness Monitoring & Alerting)
Phát hiện các dấu hiệu mệt mỏi qua mắt/miệng và phát tín hiệu cảnh báo đa phương thức để ngăn chặn tai nạn.
**Epic Goal:** Detect fatigue signs (eyes/mouth) and provide multi-modal alerts to prevent accidents.

### Epic 3: Giám sát Xao nhãng & Hướng nhìn (Distraction & Gaze Tracking)
Phát hiện khi tài xế không tập trung nhìn đường dựa trên tư thế đầu và hướng mắt.
**Epic Goal:** Monitor head orientation and eye gaze to ensure the driver is focused on the road.

### Epic 4: Nhận diện Hành vi Nguy hiểm (Dangerous Activity Recognition)
Nhận diện các hành vi như gọi điện, hút thuốc, uống nước bằng các mô hình AI chuyên sâu.
**Epic Goal:** Identify specific risky behaviors using deep learning models.

### Epic 5: Quản lý Nhật ký & Báo cáo Chuyến đi (Event Logging & Trip Analytics)
Lưu trữ lịch sử vi phạm và tổng kết hiệu quả lái xe an toàn sau mỗi chuyến đi.
**Epic Goal:** Store incident data and provide safety performance summaries.

### Epic 6: Tối ưu hóa & Cấu hình Hệ thống (Optimization & Configuration)
Tùy chỉnh độ nhạy của hệ thống và tối ưu hóa hiệu năng để chạy mượt mà trên phần cứng nhúng.
**Epic Goal:** System customization and performance tuning for edge deployment.

---

## Epic 1: Thiết lập Hệ thống & Xác thực Người lái

### Story 1.1: Thiết lập Môi trường Phát triển trên PC
As a Developer, I want to set up the Python environment (OpenCV, dlib, PyQt5) on a PC, so that I can develop and test algorithms efficiently.
**AC:** Development environment is ready; face detection works on PC.

### Story 1.2: Xây dựng Giao diện Dashboard (PC)
As a Developer, I want to create a Dashboard UI using PyQt5 to visualize detection results.
**AC:** UI window shows live feed and status placeholders.

### Story 1.3: Phát triển Logic Nhận diện & SQLite (PC)
As a Developer, I want to implement face enrollment and verification using SQLite on PC.
**AC:** Drivers can be enrolled and recognized in the local database.

### Story 1.4: Triển khai lên Phần cứng Nhúng (Embedded)
As a Developer, I want to port the code to Jetson/Pi and verify basic performance.
**AC:** App runs on hardware with >10 FPS.

### Story 1.5: Cơ chế Watchdog & Health Check (Embedded)
As a System Operator, I want the system to auto-restart on failure.
**AC:** Process recovers within 5s after crash.

---

## Epic 2: Giám sát Buồn ngủ & Cảnh báo Tức thì

### Story 2.1: Phát triển Thuật toán EAR & MAR (PC)
As a Developer, I want to build logic for EAR and MAR calculation from landmarks.
**AC:** Status changes correctly when eyes close or mouth opens in PC logs.

### Story 2.2: Logic Đánh giá PERCLOS & Phân cấp Cảnh báo (PC)
As a Developer, I want to implement PERCLOS and multi-level alert decisions.
**AC:** System classifies risks (Info/Warning/Critical) correctly on PC.

### Story 2.3: Tích hợp Giao diện Cảnh báo Visual (Dashboard)
As a Driver, I want to see color-coded alerts on the Dashboard.
**AC:** Red/Yellow overlays appear when drowsiness is detected.

### Story 2.4: Điều khiển Âm thanh & LED (Embedded)
As a Developer, I want to control physical buzzers and LEDs via GPIO.
**AC:** Hardware alerts trigger correctly on Jetson/Pi.

---

## Epic 3: Giám sát Xao nhãng & Hướng nhìn (Distraction & Gaze Tracking)

Phát hiện khi tài xế không tập trung nhìn đường dựa trên tư thế đầu và hướng mắt.
**Epic Goal:** Monitor head orientation and eye gaze to ensure the driver is focused on the road.

### Story 3.1: Ước lượng Tư thế Đầu (Head Pose Estimation - PC)

As a Developer,
I want to calculate Pitch, Yaw, and Roll angles from facial landmarks on a PC,
So that the system can determine if the driver is looking at the windshield.

**Acceptance Criteria:**

**Given** 68 facial landmarks extracted.
**When** The driver turns their head or tilts it down.
**Then** The system calculates Euler angles correctly and logs "Distracted" when thresholds are exceeded on the PC.

### Story 3.2: Phát triển Thuật toán Theo dõi Hướng nhìn (Gaze Tracking - PC)

As a Developer,
I want to build logic to identify iris position relative to eye corners to estimate gaze direction,
So that the system can detect distraction even if the driver doesn't turn their head.

**Acceptance Criteria:**

**Given** Eye regions extracted from the face.
**When** The driver gazes away from the safe observation area for more than 2 seconds.
**Then** The system calculates the gaze vector and records a distraction event on the PC.

### Story 3.3: Tích hợp Chỉ báo Xao nhãng trên Dashboard (PyQt5)

As a Driver,
I want to see directional arrows or distraction warning icons on the Dashboard,
So that I know I need to adjust my driving posture.

**Acceptance Criteria:**

**Given** A "Distraction" or "Gaze Away" event is triggered.
**When** Viewing the Dashboard.
**Then** A yellow warning icon appears with a gentle notification beep.

### Story 3.4: Tối ưu hóa & Nhúng lên Phần cứng (Jetson/Pi)

As a Developer,
I want to optimize the Head Pose & Gaze algorithms to ensure they don't drop FPS when running on embedded hardware,
So that the distraction monitoring system works smoothly in reality.

**Acceptance Criteria:**

**Given** The logic code is running well on the PC.
**When** Running on Jetson/Pi alongside other modules (Epic 1 & 2).
**Then** FPS remains stable (>15 FPS) and distraction alerts are triggered accurately on the hardware.

---

## Epic 4: Nhận diện Hành vi Nguy hiểm (Dangerous Activity Recognition)

Nhận diện các hành vi như gọi điện, hút thuốc, uống nước bằng các mô hình AI chuyên sâu.
**Epic Goal:** Identify specific risky behaviors using deep learning models.

### Story 4.1: Thu thập & Tiền xử lý Dữ liệu Hành vi (PC)

As a Developer,
I want to collect and label an image dataset for 7 dangerous behaviors (calling, smoking, drinking, distraction, etc.) on a PC,
So that I have clean data to train the classification model.

**Acceptance Criteria:**

**Given** Image data sources (self-captured or open datasets).
**When** Running the preprocessing scripts (resize, normalize, augmentation).
**Then** A complete dataset divided into Train/Val/Test sets is ready for training.

### Story 4.2: Huấn luyện & Đánh giá Mô hình Phân loại (PC)

As a Developer,
I want to train a Deep Learning model (e.g., MobileNetV2 or EfficientNet) to classify driver behaviors on a PC,
So that the system can recognize violations with high accuracy.

**Acceptance Criteria:**

**Given** The prepared dataset.
**When** Performing the training process on a PC (with GPU).
**Then** The model achieves >85% accuracy on the Test set and exports a model file in `.h5` or `.tflite` format.

### Story 4.3: Tích hợp Mô hình vào Pipeline Xử lý (PC)

As a Developer,
I want to integrate the trained model into the main processing loop to recognize behaviors in real-time,
So that the system can trigger corresponding alerts on the PC Dashboard.

**Acceptance Criteria:**

**Given** The successfully trained model.
**When** Running the application on a PC.
**Then** The Dashboard correctly displays the behavior labels (e.g., "Calling Detected") when the driver performs simulated actions.

### Story 4.4: Chuyển đổi & Tối ưu hóa cho Phần cứng Nhúng (Embedded)

As a Developer,
I want to convert the model to TensorRT or TFLite format and optimize it for Jetson/Pi,
So that the system maintains high FPS when integrating heavy AI modules.

**Acceptance Criteria:**

**Given** The original PC model.
**When** Running the conversion and optimization scripts (quantization).
**Then** The model runs on Jetson/Pi with low latency, and the overall FPS does not drop below 15.


