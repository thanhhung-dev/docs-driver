# Story 1.1: Project Scaffolding and Video Capture Setup

Status: ready-for-dev

## Story

As a **Developer**,
I want **to set up the initial project structure and capture a continuous video stream from an IR camera**,
so that **I have a modular foundation and input data for driver analysis**.

## Acceptance Criteria

1. **Given** the target hardware (Jetson Nano/RPi 4) and the Architecture design,
   **When** the developer initializes the project,
   **Then** the system MUST follow the directory structure defined in the Architecture (Input, Detection, Analysis, Action, Storage).
2. **And** the environment MUST be configured with Python 3.8 and required libraries (OpenCV, etc.).
3. **And** the system MUST successfully open a video stream at 640x480 resolution.
4. **And** the frame capture rate MUST be at least 15 FPS (NFR1).
5. **And** if the camera is not connected, the system MUST return a specific error (NFR5).

## Tasks / Subtasks

- [ ] **Task 1: Project Scaffolding** (AC: #1, #2)
  - [ ] Create missing directories in `dms/`: `detection`, `analysis`, `action`, `storage`, `models`.
  - [ ] Create `dms/requirements.txt` with specific versions: `opencv-python==4.5.5.62`, `dlib==19.22.1`, `numpy==1.21.6`, `PyYAML==6.0`, `pygame==2.1.2`.
  - [ ] Create `dms/utils/logger.py` to fix broken imports in `video_capture.py`.
  - [ ] Create `dms/config.yaml` with default settings (640x480, 15 FPS).
- [ ] **Task 2: Video Capture Implementation** (AC: #3, #4, #5)
  - [ ] Refactor/Verify `dms/input/video_capture.py` to match architecture requirements.
  - [ ] Implement `dms/main.py` as the entry point to initialize the system and start the capture loop.
  - [ ] Implement camera connection error handling and logging.
- [ ] **Task 3: Performance Validation** (AC: #4)
  - [ ] Add FPS counter in the capture loop to verify 15 FPS target.

## Dev Notes

### Architecture Patterns and Constraints
- **Pipeline Architecture**: Follow the "Video Input → Detection → Analysis → Action" flow [Source: _bmad-output/architecture/ARCHITECTURE-Driver-Monitoring-System.md#Section 2.1].
- **Python 3.8**: Ensure compatibility with the target runtime environment.
- **OpenCV 4.5.5**: Use for video capture and image processing.
- **Error Handling**: Graceful failure if camera is not found.

### Project Structure Notes
- **Source root**: `dms/` (matching architecture).
- **Naming**: Use direct names (`input`, `detection`, etc.) as defined in the Architecture.

### References
- [Source: _bmad-output/architecture/ARCHITECTURE-Driver-Monitoring-System.md#Section 5.3] (Directory structure)
- [Source: _bmad-output/architecture/ARCHITECTURE-Driver-Monitoring-System.md#Section 10.1.1] (Face Detector design)
- [Source: _bmad-output/planning-artifacts/prd/8-non-functional-requirements-yu-cu-phi-chc-nng.md] (NFR1, NFR2)

## Dev Agent Record

### Agent Model Used

Gemini 2.0 Flash

### Debug Log References

### Completion Notes List

### File List
- dms/main.py
- dms/requirements.txt
- dms/config.yaml
- dms/utils/logger.py
- dms/input/video_capture.py
