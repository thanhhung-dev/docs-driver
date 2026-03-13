# 3. Product Scope Overview (Tổng quan Phạm vi Sản phẩm)

## 3.1 MVP - Sản phẩm Khả dụng Tối thiểu (Mục tiêu cho Đồ án)

Phiên bản MVP sẽ tập trung vào việc chứng minh các chức năng cốt lõi và đáp ứng các tiêu chí thành công của đồ án.

**MVP Approach:** "MVP Giải quyết Vấn đề" (Problem-Solving MVP). Chiến lược này tập trung vào việc chứng minh một cách thuyết phục rằng công nghệ cốt lõi của hệ thống có khả năng hoạt động hiệu quả. Mục tiêu là xây dựng một nguyên mẫu chức năng để trả lời câu hỏi: "Hệ thống có thể phát hiện một cách đáng tin cậy sự mệt mỏi, mất tập trung và các hành vi nguy hiểm trên phần cứng biên không?". Cách tiếp cận này trực tiếp giải quyết các tiêu chí thành công quan trọng nhất cho một đồ án tốt nghiệp: chứng minh tính khả thi và tiềm năng kỹ thuật.

**Resource Requirements:** Dự án yêu cầu kiến thức về Python, Computer Vision (OpenCV, Dlib), và Machine Learning (TensorFlow Lite), cùng với khả năng làm việc với phần cứng nhúng (Jetson Nano/Raspberry Pi).

**Core User Journeys Supported:**
*   **Hành trình Tài xế:** Trải nghiệm đầy đủ từ cảnh báo sớm, nhẹ nhàng đến cảnh báo khẩn cấp khi có dấu hiệu nguy hiểm rõ rệt.
*   **Hành trình Giảng viên:** Khả năng xem lại log sự kiện chi tiết và bằng chứng hình ảnh để xác thực hoạt động của hệ thống.

**Must-Have Capabilities (Các khả năng bắt buộc):**
1.  **Phát hiện Buồn ngủ:** Dựa trên các chỉ số EAR, PERCLOS, và ngáp.
2.  **Phát hiện Mất tập trung:** Dựa trên hướng đầu và hướng nhìn.
3.  **Phát hiện Hành vi Nguy hiểm:** Nhận dạng 7 hành vi cụ thể đã xác định (ví dụ: sử dụng điện thoại, uống nước, hút thuốc).
4.  **Hệ thống Cảnh báo Hai Cấp độ:** Cảnh báo sớm nhẹ nhàng (âm thanh, LED màu) và cảnh báo khẩn cấp (âm thanh dồn dập, LED nhấp nháy).
5.  **Ghi Log Sự kiện:** Ghi lại tất cả các sự kiện vào tệp log hoặc cơ sở dữ liệu SQLite.
6.  **Lưu Bằng chứng:** Tự động chụp và lưu lại hình ảnh tại thời điểm có cảnh báo khẩn cấp.
7.  **Hỗ trợ một Nền tảng:** Tối ưu hóa để hệ thống chạy ổn định và hiệu quả trên MỘT nền tảng phần cứng được chọn (Jetson Nano hoặc Raspberry Pi 4).

## 3.2 Post-MVP Features (Tính năng phát triển sau Đồ án)

Các tính năng có thể phát triển sau khi hoàn thành MVP: Hỗ trợ đa nền tảng phần cứng, xây dựng giao diện người dùng đồ họa (GUI) nâng cao, cá nhân hóa cho từng tài xế, và hoàn thiện cơ chế cập nhật OTA (Over-The-Air) từ xa.

## 3.3 Vision (Tầm nhìn Tương lai)

Định hướng dài hạn cho sản phẩm: Tích hợp với hệ thống của xe, kết nối đám mây để quản lý đội xe, cá nhân hóa theo từng tài xế.
