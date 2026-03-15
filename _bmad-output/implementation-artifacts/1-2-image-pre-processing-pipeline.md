# Story 1.2: Image Pre-processing Pipeline

Status: ready-for-dev

## Story

As a **DMS System**,
I want **to pre-process raw frames (grayscale, contrast)**,
so that **detection modules receive optimized input**.

## Acceptance Criteria

1. **Given** a raw BGR frame from Story 1.1,
   **When** passed through the pre-processing module,
   **Then** the frame MUST be converted to grayscale (FR2).
2. **And** contrast MUST be enhanced using CLAHE (Contrast Limited Adaptive Histogram Equalization) to handle low-light conditions (Architecture Section 6.1).
3. **And** the pre-processor MUST support optional resizing (default 640x480) for performance (Architecture Section 6.1).
4. **And** the processing time for pre-processing MUST be around 3ms per frame to maintain 15 FPS target (NFR1, Architecture Section 6.2).
5. **And** the resulting frame MUST be ready for the Detection Layer (Pipes and Filters pattern).

## Tasks / Subtasks

- [ ] **Task 1: Preprocessor Module Implementation** (AC: #1, #2, #3, #4)
  - [ ] Create `dms/input/preprocessor.py` according to Architecture Section 10.1.
  - [ ] Implement `Preprocessor` class with `__init__(self, config=None)` to load thresholds.
  - [ ] Implement `preprocess(self, frame: np.ndarray) -> np.ndarray` as the main entry point.
  - [ ] Implement `grayscale(self, frame: np.ndarray) -> np.ndarray` using `cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)`.
  - [ ] Implement `enhance_ir_image(self, frame: np.ndarray) -> np.ndarray` using CLAHE (Contrast Limited Adaptive Histogram Equalization).
  - [ ] Configure CLAHE with `clipLimit=2.0` and `tileGridSize=(8, 8)` for IR optimization.
  - [ ] Implement `normalize(self, frame: np.ndarray) -> np.ndarray` for uniform lighting adjustment if necessary.
  - [ ] Implement `resize(self, frame: np.ndarray, width: int = 640, height: int = 480) -> np.ndarray` with `cv2.INTER_AREA` interpolation.
  - [ ] Add error handling for empty or None frames (returning original or logged error).
- [ ] **Task 2: Logging and Performance Instrumentation** (AC: #4)
  - [ ] Integrate with `dms/utils/logger.py` to log preprocessing start/end if debug mode is on.
  - [ ] Implement a micro-benchmark within the `preprocess` method using `time.perf_counter()` to track execution time.
  - [ ] Log a warning if preprocessing time exceeds the 3ms budget.
- [ ] **Task 3: Pipeline Integration** (AC: #5)
  - [ ] Update `dms/main.py` (created in Story 1.1) to import `Preprocessor`.
  - [ ] Instantiate `Preprocessor` in the system initialization phase.
  - [ ] Update the main processing loop to call `preprocessor.preprocess(frame)` immediately after capture.
  - [ ] Ensure the pre-processed frame is passed to subsequent (placeholder) detection modules.
- [ ] **Task 4: Unit Testing and Validation** (AC: #1, #2, #4)
  - [ ] Create `tests/test_preprocessor.py` using `pytest`.
  - [ ] Add test cases for different frame sizes and formats.
  - [ ] Add a visual validation test: save "before" (raw BGR) and "after" (grayscale CLAHE enhanced) images to `data/snapshots/` for manual review.
  - [ ] Add a performance test: process 100 frames and assert that the average time is < 4ms.

## Dev Notes

### Architecture Patterns and Constraints
- **Pattern**: Pipeline Architecture (Pipes and Filters) [Source: _bmad-output/architecture/ARCHITECTURE-Driver-Monitoring-System.md#Section 2.1].
- **Responsibility**: `Preprocessor` is part of the **Input Layer** [Source: _bmad-output/architecture/ARCHITECTURE-Driver-Monitoring-System.md#Section 4.2].
- **Time Budget**: 3ms for the entire preprocessing step [Source: _bmad-output/architecture/ARCHITECTURE-Driver-Monitoring-System.md#Section 6.2].
- **Algorithm Choice**: CLAHE is preferred over Global Histogram Equalization to prevent noise amplification in IR images.

### Project Structure Notes
- **File**: `dms/input/preprocessor.py`
- **Integration**: `dms/main.py`
- **Tests**: `tests/test_preprocessor.py`

### References
- [Source: _bmad-output/architecture/ARCHITECTURE-Driver-Monitoring-System.md#Section 4.2] (Component Responsibilities)
- [Source: _bmad-output/architecture/ARCHITECTURE-Driver-Monitoring-System.md#Section 6.2] (Data Flow Timing)
- [Source: _bmad-output/planning-artifacts/epics.md#Story 1.2] (Original Story Requirements)

## Dev Agent Record

### Agent Model Used

Gemini 2.0 Flash (as BMad Method Execution Agent)

### Debug Log References

### Completion Notes List
- Ultimate context engine analysis completed - comprehensive developer guide created.

### File List
- dms/input/preprocessor.py
- dms/main.py
- tests/test_preprocessor.py
