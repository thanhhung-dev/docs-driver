# Story 1.4: Facial Landmark Extraction

Status: ready-for-dev

## Story

As a **DMS System**,
I want **to extract 68 facial landmarks from the detected face**,
so that **features like eyes and mouth can be analyzed**.

## Acceptance Criteria

1. **Given** face coordinates from Story 1.3,
   **When** processed by the Landmark Predictor module,
   **Then** the system MUST return 68 (x, y) coordinates mapping eyes, nose, mouth, and jawline (FR3, Architecture Section 10.1.1).
2. **And** the landmark extraction latency MUST be under 10ms to ensure the overall system latency remains within budget (Architecture Section 6.2).
3. **And** the landmarks MUST follow the standard dlib 68-point model (Architecture Section 10.1.1).
4. **And** the predictor MUST be robust to small head tilts and varying light conditions typical in IR imaging.

## Tasks / Subtasks

- [ ] **Task 1: Landmark Predictor Implementation** (AC: #1, #3)
  - [ ] Update `dms/detection/face_detector.py` (created in Story 1.3) to include landmark extraction.
  - [ ] Load the pre-trained `shape_predictor_68_face_landmarks.dat` model using `dlib.shape_predictor()`.
  - [ ] Implement `get_landmarks(self, frame, face_rect)` method.
  - [ ] Return a NumPy array of shape (68, 2) for downstream processing.
- [ ] **Task 2: Performance Optimization** (AC: #2)
  - [ ] Measure the inference time of `predictor(frame, face_rect)`.
  - [ ] Ensure the model is loaded only once during initialization.
  - [ ] Log performance warnings if extraction exceeds 10ms.
- [ ] **Task 3: Testing and Landmark Verification** (AC: #1, #3)
  - [ ] Update `tests/test_face_detector.py` to verify landmarks.
  - [ ] Add a visual test that draws all 68 landmarks on a sample frame and saves it for verification.
  - [ ] Verify point indices for specific features (eyes: 36-47, mouth: 48-67).

## Dev Notes

### Architecture Patterns and Constraints
- **Pattern**: Detection Layer component.
- **Model**: `shape_predictor_68_face_landmarks.dat` (~99MB). This model is a standard for real-time applications.
- **Dependency**: Requires successful face detection from Story 1.3.

### Project Structure Notes
- **File**: `dms/detection/face_detector.py` (extends existing class)
- **Model Storage**: `dms/models/shape_predictor_68_face_landmarks.dat`
- **Tests**: `tests/test_face_detector.py`

### References
- [Source: _bmad-output/architecture/ARCHITECTURE-Driver-Monitoring-System.md#Section 10.1.1] (Landmark Detector Detail)
- [Source: _bmad-output/architecture/ARCHITECTURE-Driver-Monitoring-System.md#Section 9.3] (Model Assets)
- [Source: _bmad-output/planning-artifacts/epics.md#Story 1.4] (Original Story Requirements)

## Dev Agent Record

### Agent Model Used

Gemini 2.0 Flash (as BMad Method Execution Agent)

### Debug Log References

### Completion Notes List

### File List
- dms/detection/face_detector.py
- dms/models/shape_predictor_68_face_landmarks.dat
- tests/test_face_detector.py
