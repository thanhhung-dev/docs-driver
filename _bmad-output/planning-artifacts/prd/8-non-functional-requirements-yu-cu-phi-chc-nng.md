# 8. Non-Functional Requirements (Yêu cầu Phi Chức năng)

## 8.1 Performance (Hiệu suất)

*   **NFR1: Tốc độ xử lý khung hình:** Hệ thống PHẢI có khả năng xử lý và phân tích video đầu vào ở tốc độ tối thiểu **15 khung hình mỗi giây (FPS)** trong suốt quá trình hoạt động.
*   **NFR2: Độ trễ cảnh báo:** Thời gian từ khi hệ thống phát hiện một sự kiện cần cảnh báo (ví dụ: ngủ gật ngắn) đến khi kích hoạt cảnh báo tương ứng (âm thanh, đèn LED) PHẢI dưới **200 mili giây**.
*   **NFR3: Hiệu quả tài nguyên:** Hệ thống PHẢI có khả năng duy trì hoạt động ổn định trên phần cứng biên (Jetson Nano/Raspberry Pi 4) mà không gây quá tải tài nguyên (CPU/GPU và RAM) khi hoạt động liên tục trong thời gian dài.

## 8.2 Reliability (Độ tin cậy)

*   **NFR4: Thời gian hoạt động liên tục:** Hệ thống PHẢI có khả năng hoạt động liên tục trong ít nhất **4 giờ** mà không gặp lỗi phần mềm nghiêm trọng hoặc yêu cầu khởi động lại.
*   **NFR5: Xử lý lỗi đầu vào video:** Nếu luồng video từ camera bị gián đoạn hoặc không khả dụng, hệ thống PHẢI hiển thị cảnh báo rõ ràng cho người dùng (ví dụ: đèn LED lỗi, âm thanh thông báo) và tự động cố gắng khôi phục kết nối camera.
*   **NFR6: Giảm thiểu cảnh báo sai:** Hệ thống PHẢI duy trì tỷ lệ cảnh báo sai (false positives) dưới **5%** trong các kịch bản lái xe bình thường (không có dấu hiệu buồn ngủ/mất tập trung).
*   **NFR7: Khả năng cấu hình:** Hệ thống PHẢI cho phép điều chỉnh các ngưỡng phát hiện và độ nhạy cảnh báo thông qua tệp cấu hình để tối ưu hóa độ tin cậy và sự phù hợp với các điều kiện khác nhau.