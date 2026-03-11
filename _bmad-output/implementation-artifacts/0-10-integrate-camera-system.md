# Story 0.10: integrate-camera-system

Status: ready-for-dev

<!-- Note: Validation is optional. Run validate-create-story for quality check before dev-story. -->

## Story

As a system,
I want to reliably capture video frames from the IR camera,
so that I can process them for driver monitoring.

## Acceptance Criteria

**Scenario 1: Camera Initialization**
```
Given the system starts up
When the camera initialization is triggered
Then the IR camera should be detected
And video capture should begin successfully
And frame rate should be at least 30 FPS
```

**Scenario 2: Frame Capture**
```
Given the camera is running
When frames are requested
Then frames should be returned in RGB format
And resolution should be 640x480 or higher
And frames should have good quality (not blurry, not dark)
```

**Scenario 3: Error Handling**
```
Given the camera connection fails
When the system tries to capture frames
Then an error should be logged
And the system should attempt reconnection
And the UI should display "camera error" status
```

**Scenario 4: Night Vision (IR)**
```
Given low light conditions (night, tunnel)
When the IR camera is active
Then faces should still be detectable
And image quality should be sufficient for detection
```

## Tasks / Subtasks

- [ ] **Task 1: VideoCapture Component** (AC: Scenario 1, 2)
  - [ ] Create VideoCapture class with init_camera(), get_frame(), release() methods
  - [ ] Implement OpenCV VideoCapture integration with camera index detection
  - [ ] Add frame rate validation and configuration (30 FPS minimum)
  - [ ] Add resolution setting and validation (640x480 minimum)

- [ ] **Task 2: IR Camera Integration** (AC: Scenario 4) 
  - [ ] Implement IR camera specific settings and optimization
  - [ ] Add IR image enhancement for low-light conditions
  - [ ] Test and validate IR performance in total darkness

- [ ] **Task 3: Error Handling & Recovery** (AC: Scenario 3)
  - [ ] Implement camera connection error detection
  - [ ] Add automatic reconnection logic with exponential backoff
  - [ ] Create logging system for camera events and errors
  - [ ] Add system status reporting for UI integration

- [ ] **Task 4: Frame Preprocessing Pipeline** (AC: Scenario 2)
  - [ ] Implement frame preprocessing (resize, normalize, enhance)
  - [ ] Add frame quality validation (brightness, blur detection)
  - [ ] Create frame buffer management for smooth processing

## Dev Notes

### Architecture Requirements (CRITICAL)

**MUST FOLLOW Pipeline Architecture Pattern:**
- VideoCapture component is INPUT LAYER of the pipeline
- Frames flow sequentially: Video Input → Detection Stage → Analysis Stage → Action Stage
- Implement clear data contracts between pipeline stages

**Component Responsibilities:**
- **VideoCapture**: Interface with IR camera, capture frames (`init_camera()`, `get_frame()`, `release()`)
- **Preprocessor**: Prepare frames for detection (`preprocess()`, `enhance_ir_image()`, `normalize()`)

### Technology Stack Requirements (CRITICAL)

**Required Libraries with Versions:**
- **OpenCV**: Use latest 4.14.0-pre (NOT 4.5.5 from original spec)
  - Enhanced VideoCapture API with better hardware acceleration
  - Backward compatible with existing API patterns
  - Better performance on edge devices
- **Python**: Upgrade to 3.13+ (3.8 is End-of-Life, security risk)
- **NumPy**: 1.21+ for numerical operations
- **Hardware Interface**: RPi.GPIO/Jetson.GPIO for hardware control

**OpenCV VideoCapture API Pattern:**
```python
import cv2

# Initialize camera
cap = cv2.VideoCapture(camera_index, cv2.CAP_ANY)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 30)

# Frame capture loop
ret, frame = cap.read()
if ret:
    # Process frame
    pass

# Cleanup
cap.release()
```

### Project Structure Requirements

**File Organization (MUST follow architecture):**
```
src/
├── input_layer/
│   ├── video_capture.py      # VideoCapture component
│   ├── preprocessor.py       # Frame preprocessing  
│   └── __init__.py
├── config/
│   └── camera_config.yaml    # Camera configuration
├── utils/
│   ├── logging.py           # Centralized logging
│   └── system_monitor.py    # System health monitoring
└── main.py                  # Application entry poitn
```

**Configuration Management:**
- Store camera settings in `config/camera_config.yaml`
- Use PyYAML for configuration file parsing
- Configurable thresholds (frame rate, resolution, quality metrics)

### Hardware Integration Requirements

**Camera Interface:**
- **Connection**: USB 2.0/3.0 interface
- **Power**: Bus-powered via USB (5V)
- **Position**: Dashboard mounted, 20-40cm from driver, 10-15° downward angle
- **IR Capability**: Must work in total darkness

**Performance Requirements:**
- **Frame Rate**: Minimum 30 FPS (target)  
- **Resolution**: Minimum 640x480 (can scale up)
- **Latency**: <100ms from capture to processing
- **Resource Usage**: Monitor CPU/memory consumption

### Testing Requirements

**Unit Tests Required:**
- Camera initialization and connection testing
- Frame capture validation
- Error handling and recovery scenarios
- IR performance testing

**Integration Tests Required:**
- End-to-end camera pipeline testing
- Hardware compatibility testing (multiple camera models)
- Performance benchmarking on target hardware (Jetson Nano/RPi 4)

**Test Data:**
- IR camera test footage in various lighting conditions
- Synthetic test patterns for quality validation

### Critical Implementation Notes

**Error Prevention:**
- Always check `cap.isOpened()` before frame operations
- Implement proper resource cleanup in finally blocks
- Use context managers for camera resource management
- Add frame validation (empty frame detection)

**Performance Optimization:**
- Use hardware acceleration when available (CUDA on Jetson)
- Implement frame buffering to prevent blocking
- Consider threading for camera I/O to maintain real-time performance
- Profile memory usage to prevent leaks

**Security Considerations:**
- Validate camera input to prevent injection attacks
- Secure camera device access permissions
- Log security events appropriately

### Latest Technical Updates

**OpenCV 4.14.0-pre Advantages:**
- Enhanced hardware acceleration support for edge devices
- Better USB camera detection and enumeration
- Improved error handling and recovery mechanisms
- New VideoCapture properties for fine-tuned control

**Python Version Recommendation:**
- **CRITICAL**: Upgrade from Python 3.8 (EOL) to Python 3.13+ for security patches
- Benefits: Better performance, security fixes, improved error messages
- Compatibility: All specified libraries support Python 3.13+

### References

- [Source: _bmad-output/guides/HUONG-DAN-DO-AN-TOT-NGHIEP.md#US-010]
- [Source: _bmad-output/architecture/ARCHITECTURE-Driver-Monitoring-System.md#Section-4-Component-View] 
- [Source: OpenCV 4.14.0-pre Documentation - VideoCapture Class]
- [Source: _bmad-output/architecture/ARCHITECTURE-Driver-Monitoring-System.md#Section-9-Technology-Stack]

## Dev Agent Record

### Agent Model Used

claude-sonnet-4

### Debug Log References

### Completion Notes List

### File List