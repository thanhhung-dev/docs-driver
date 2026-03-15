# Story 1.5: Head Pose Estimation

Status: ready-for-dev

## Story

As a **DMS System**,
I want **to calculate head orientation (pitch, yaw, roll)**,
so that **I can determine if the driver is looking away**.

## Acceptance Criteria

1. **Given** 68 facial landmarks from Story 1.4,
   **When** processed by the Pose Estimator module (using `cv2.solvePnP` with a standard 3D face model),
   **Then** the system MUST calculate Pitch, Yaw, and Roll angles in degrees (FR4, Architecture Section 10.1.3).
2. **And** the estimation error MUST be less than 5 degrees under normal lighting and orientation.
3. **And** the latency for head pose estimation MUST be under 10ms (Architecture Section 6.2).
4. **And** the estimator MUST identify head orientation according to the coordinate system defined in Architecture Section 10.1.3 (Pitch: X, Yaw: Y, Roll: Z).
5. **And** the system MUST detect "head down" (pitch > threshold) and "head turned" (yaw > threshold) states.

## Tasks / Subtasks

- [ ] **Task 1: Pose Estimator Implementation** (AC: #1, #4, #5)
  - [ ] Create `dms/detection/head_pose_estimator.py` according to Architecture Section 10.1.3.
  - [ ] Implement `HeadPoseEstimator` class with standard 3D model points (nose tip, chin, eye corners, mouth corners).
  - [ ] Initialize camera matrix assuming no lens distortion (as per Architecture).
  - [ ] Implement `estimate_pose(self, landmarks: np.ndarray)` method.
  - [ ] Use `cv2.solvePnP` and `cv2.Rodrigues` to compute rotation matrix and Euler angles.
  - [ ] Implement `is_head_turned(self, yaw, threshold=30.0)` and `is_head_down(self, pitch, threshold=20.0)`.
- [ ] **Task 2: Performance Profiling** (AC: #3)
  - [ ] Measure execution time for pose estimation.
  - [ ] Ensure the 3D model points and camera matrix are initialized only once.
- [ ] **Task 3: Pipeline Integration** (AC: #1)
  - [ ] Update `dms/main.py` to import `HeadPoseEstimator`.
  - [ ] Integrate into the main loop after landmark extraction.
  - [ ] Display the estimated Pitch, Yaw, and Roll on the debug UI (if available) or log them.
- [ ] **Task 4: Unit Testing** (AC: #1, #2)
  - [ ] Create `tests/test_head_pose_estimator.py`.
  - [ ] Add test cases with simulated landmarks representing different poses.
  - [ ] Compare results with expected angles to verify the 5-degree accuracy.

## Dev Notes

### Architecture Patterns and Constraints
- **Pattern**: Detection Layer component.
- **Algorithm**: `solvePnP` is an iterative algorithm that provides a good balance between speed and precision for real-time systems.
- **Tech Choice**: Uses standard OpenCV PnP functions.

### Project Structure Notes
- **File**: `dms/detection/head_pose_estimator.py`
- **Integration**: `dms/main.py`
- **Tests**: `tests/test_head_pose_estimator.py`

### References
- [Source: _bmad-output/architecture/ARCHITECTURE-Driver-Monitoring-System.md#Section 10.1.3] (Head Pose Estimator Detailed Design)
- [Source: _bmad-output/planning-artifacts/epics.md#Story 1.5] (Original Story Requirements)

## Dev Agent Record

### Agent Model Used

Gemini 2.0 Flash (as BMad Method Execution Agent)

### Debug Log References

### Completion Notes List

### File List
- dms/detection/head_pose_estimator.py
- dms/main.py
- tests/test_head_pose_estimator.py
