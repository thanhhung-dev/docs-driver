# Story 1.3: Face Detection and Tracking

Status: ready-for-dev

## Story

As a **DMS System**,
I want **to detect and track the driver's face in real-time**,
so that **facial landmarks can be extracted for analysis**.

## Acceptance Criteria

1. **Given** a pre-processed frame from Story 1.2,
   **When** processed by the Face Detector module,
   **Then** the system MUST return the bounding box coordinates (left, top, right, bottom) of the driver's face (FR3).
2. **And** the system MUST be capable of tracking the face across consecutive frames to maintain continuity.
3. **And** if no face is found after 2 seconds (approx. 30-60 frames depending on FPS), the system MUST report a "Driver Not Found" status (Architecture Section 10.1.1).
4. **And** the face detection latency MUST be under 15ms per frame on the target hardware (Architecture Section 6.2).
5. **And** the system MUST handle single driver detection (taking the first/largest face detected) as per Architecture Section 10.1.1.

## Tasks / Subtasks

- [ ] **Task 1: Face Detector Module Implementation** (AC: #1, #3, #5)
  - [ ] Create `dms/detection/face_detector.py` according to Architecture Section 10.1.1.
  - [ ] Implement `FaceDetector` class.
  - [ ] Initialize dlib's HOG-based face detector using `dlib.get_frontal_face_detector()`.
  - [ ] Implement `detect_face(self, frame: np.ndarray)` method returning `dlib.rectangle`.
  - [ ] Implement a `no_face_counter` to track consecutive frames without a face.
  - [ ] Implement `is_no_face_alert_required(self)` returning true if counter exceeds 2 seconds threshold.
- [ ] **Task 2: Tracking Logic and Continuity** (AC: #2)
  - [ ] Implement logic to select the primary face (largest bounding box) if multiple faces are detected.
  - [ ] (Optional but recommended) Implement a simple centroid-based tracker or use dlib's correlation tracker if HOG is too slow for every frame.
- [ ] **Task 3: Pipeline Integration** (AC: #1)
  - [ ] Update `dms/main.py` to import `FaceDetector`.
  - [ ] Instantiate `FaceDetector` in the system initialization.
  - [ ] Update the main loop to pass the pre-processed frame to the `FaceDetector`.
  - [ ] Log "Driver Not Found" warning to `dms/utils/logger.py` when the threshold is hit.
- [ ] **Task 4: Unit Testing and Validation** (AC: #1, #3, #4)
  - [ ] Create `tests/test_face_detector.py`.
  - [ ] Add test cases with images containing: one face, no face, multiple faces.
  - [ ] Benchmark the detection speed to ensure it stays within the 15ms budget.

## Dev Notes

### Architecture Patterns and Constraints
- **Pattern**: Pipeline Architecture. This module resides in the **Detection Layer**.
- **Model**: dlib HOG-based detector is chosen for its balance of speed and accuracy on CPU (RPi 4) and GPU (Jetson Nano).
- **Constraint**: Latency is critical. Avoid upsampling the frame unless necessary for accuracy.

### Project Structure Notes
- **File**: `dms/detection/face_detector.py`
- **Integration**: `dms/main.py`
- **Tests**: `tests/test_face_detector.py`

### References
- [Source: _bmad-output/architecture/ARCHITECTURE-Driver-Monitoring-System.md#Section 10.1.1] (Face Detector Design)
- [Source: _bmad-output/architecture/ARCHITECTURE-Driver-Monitoring-System.md#Section 6.2] (Processing Pipeline Timing)
- [Source: _bmad-output/planning-artifacts/epics.md#Story 1.3] (Original Story Requirements)

## Dev Agent Record

### Agent Model Used

Gemini 2.0 Flash (as BMad Method Execution Agent)

### Debug Log References

### Completion Notes List

### File List
- dms/detection/face_detector.py
- dms/main.py
- tests/test_face_detector.py
