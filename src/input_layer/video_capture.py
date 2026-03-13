
import cv2
import time
from src.utils.logging import logger

class VideoCapture:
    """
    Component for capturing video from an IR camera using OpenCV.
    Follows Pipeline Architecture Pattern as the INPUT LAYER.
    """
    def __init__(self, config=None):
        """
        Initialize the VideoCapture component.
        
        Args:
            config (dict, optional): Configuration for camera settings.
                Defaults to 640x480 @ 30 FPS on camera index 0.
        """
        self.config = config or {
            'camera_index': 0,
            'fps': 30,
            'width': 640,
            'height': 480
        }
        self.cap = None
        self.is_running = False
        self.camera_index = self.config.get('camera_index', 0)
        self.target_fps = self.config.get('fps', 30)
        self.target_width = self.config.get('width', 640)
        self.target_height = self.config.get('height', 480)

    def init_camera(self):
        """
        Initialize the camera with specified configuration and validate settings.
        
        Returns:
            bool: True if initialization and validation succeeded, False otherwise.
        """
        logger.info(f"Initializing camera at index {self.camera_index}")
        try:
            # Using cv2.CAP_ANY as recommended for 4.14.0-pre
            self.cap = cv2.VideoCapture(self.camera_index, cv2.CAP_ANY)
            
            if not self.cap.isOpened():
                logger.error(f"Failed to open camera at index {self.camera_index}")
                return False

            # Set camera properties
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.target_width)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.target_height)
            self.cap.set(cv2.CAP_PROP_FPS, self.target_fps)

            # Validate settings
            actual_width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
            actual_height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
            actual_fps = self.cap.get(cv2.CAP_PROP_FPS)

            logger.info(f"Camera initialized: {actual_width}x{actual_height} @ {actual_fps} FPS")

            # Quantitative validation as per story requirements
            if actual_width < self.target_width or actual_height < self.target_height:
                logger.error(f"Resolution validation failed. Target: {self.target_width}x{self.target_height}, Actual: {actual_width}x{actual_height}")
                self.release()
                return False

            if actual_fps < self.target_fps:
                logger.error(f"FPS validation failed. Target: {self.target_fps}, Actual: {actual_fps}")
                self.release()
                return False

            self.is_running = True
            return True

        except Exception as e:
            logger.error(f"Error initializing camera: {str(e)}")
            self.is_running = False
            return False

    def get_frame(self):
        """
        Capture a single frame from the camera.
        
        Returns:
            tuple: (bool, numpy.ndarray) - Success flag and the captured frame.
        """
        if not self.is_running or self.cap is None:
            logger.error("Attempted to get frame from uninitialized or stopped camera")
            return False, None

        try:
            ret, frame = self.cap.read()
            if not ret:
                logger.warning("Failed to capture frame")
                return False, None
            
            return True, frame
        except Exception as e:
            logger.error(f"Error during frame capture: {str(e)}")
            return False, None

    def release(self):
        """
        Release camera resources and stop the component.
        """
        if self.cap is not None:
            self.cap.release()
            self.cap = None
        
        self.is_running = False
        logger.info("Camera resources released")
