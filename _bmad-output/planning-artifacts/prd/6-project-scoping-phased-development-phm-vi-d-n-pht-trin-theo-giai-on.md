# 6. Project Scoping & Phased Development (Phạm vi Dự án & Phát triển theo Giai đoạn)

## 6.1 MVP Strategy & Philosophy

**MVP Approach:** "MVP Giải quyết Vấn đề" (Problem-Solving MVP). Chiến lược này tập trung vào việc chứng minh một cách thuyết phục rằng công nghệ cốt lõi của hệ thống có khả năng hoạt động hiệu quả. Mục tiêu là xây dựng một nguyên mẫu chức năng để trả lời câu hỏi: "Hệ thống có thể phát hiện một cách đáng tin cậy sự mệt mỏi và mất tập trung trên phần cứng biên không?". Cách tiếp cận này trực tiếp giải quyết các tiêu chí thành công quan trọng nhất cho một đồ án tốt nghiệp: chứng minh tính khả thi và tiềm năng kỹ thuật.

**Resource Requirements:** Dự án yêu cầu kiến thức về Python, Computer Vision (OpenCV, Dlib), và Machine Learning (TensorFlow Lite), cùng với khả năng làm việc với phần cứng nhúng (Jetson Nano/Raspberry Pi).

## 6.2 Post-MVP Features

**Phase 2 (Growth):**
*   **Mở rộng Nhận diện Hành vi:** Thêm các module phát hiện hành vi phức tạp khác (ví dụ: sử dụng điện thoại).
*   **Giao diện Đồ họa (GUI):** Xây dựng một dashboard đơn giản để xem lại lịch sử chuyến đi.
*   **Hoàn thiện Cập nhật OTA:** Triển khai đầy đủ cơ chế cập nhật phần mềm từ xa.

**Phase 3 (Expansion):**
*   **Tích hợp sâu hơn:** Kết nối với hệ thống CAN bus của xe.
*   **Kết nối Đám mây:** Đồng bộ hóa dữ liệu sự kiện lên một nền tảng đám mây.
*   **Cá nhân hóa:** Cho phép hệ thống tự học và điều chỉnh độ nhạy cảnh báo.

## 6.3 Risk Mitigation Strategy

**Technical Risks:**
*   **Rủi ro:** Hiệu suất trên phần cứng có thể không đạt được mục tiêu (≥15 FPS).
*   **Giảm thiểu:** Ưu tiên tối ưu hóa các thuật toán, sử dụng các mô hình AI đã được lượng tử hóa (quantized), và chọn nền tảng phần cứng mạnh hơn nếu cần.
**Market Risks:**
*   **Rủi ro (trong bối cảnh đồ án):** Tính mới của đề tài không được đánh giá cao.
*   **Giảm thiểu:** Nhấn mạnh vào khía cạnh "phân tích toàn diện" và "độ chính xác cao".
**Resource Risks:**
*   **Rủi ro:** Thời gian phát triển có thể không đủ.
*   **Giảm thiểu:** Tuân thủ nghiêm ngặt phạm vi MVP đã xác định.
