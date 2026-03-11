# 2. Success Criteria

## 2.1 User Success (Thành công của Người dùng)

Người dùng sẽ coi hệ thống là thành công nếu nó đóng vai trò như một người bạn đồng hành đáng tin cậy, giúp họ nhận thức được các dấu hiệu mệt mỏi hoặc mất tập trung từ sớm. Tiêu chí thành công chính là:

*   **Cảnh báo sớm và nhẹ nhàng:** Hệ thống có khả năng đưa ra các cảnh báo ở mức độ thấp (ví dụ: một tiếng "ping" nhẹ hoặc đèn LED thay đổi màu sắc) ngay khi phát hiện các dấu hiệu ban đầu của sự mệt mỏi hoặc mất tập trung.
*   **Độ tin cậy cao, ít phiền nhiễu:** Người dùng tin tưởng vào các cảnh báo và không cảm thấy bị làm phiền bởi các cảnh báo sai. Tỷ lệ cảnh báo sai (false positives) phải đủ thấp để không gây ra "sự mỏi mệt vì cảnh báo" (alert fatigue).
*   **Tạo cảm giác an tâm:** Người dùng cảm thấy an toàn và tự tin hơn khi lái xe, biết rằng có một "phụ lái" ảo đang theo dõi và hỗ trợ họ.

## 2.2 Project Success (Thành công của Đồ án)

Là một đồ án tốt nghiệp, dự án được coi là thành công khi đạt được các mục tiêu học thuật và kỹ thuật sau:

*   **Chứng minh tính khả thi:** Hệ thống hoàn chỉnh (end-to-end) hoạt động ổn định trên phần cứng mục tiêu (Jetson Nano hoặc Raspberry Pi 4), đáp ứng các chỉ số hiệu suất cốt lõi (≥15 FPS, độ trễ <200ms).
*   **Chứng minh khả năng mở rộng:** Thể hiện được khả năng tích hợp một module phát hiện hành vi mới vào kiến trúc hệ thống một cách nhanh chóng (ví dụ: dưới 2 ngày công) mà không cần thay đổi cấu trúc lõi.
*   **Hoàn thành tài liệu:** Toàn bộ tài liệu thiết kế, báo cáo kết quả và mã nguồn được hoàn thiện, có chất lượng cao, sẵn sàng cho việc đánh giá của hội đồng.

## 2.3 Technical Success (Thành công về Kỹ thuật)

Thành công về mặt kỹ thuật được đo lường bằng các chỉ số hiệu suất và độ chính xác cụ thể đã được đề ra trong tài liệu kiến trúc:

*   **Hiệu suất:** Tốc độ xử lý video đạt tối thiểu 15 khung hình mỗi giây (FPS).
*   **Độ trễ:** Thời gian từ khi phát hiện sự kiện đến khi đưa ra cảnh báo dưới 200 mili giây.
*   **Độ chính xác:** Phát hiện trạng thái buồn ngủ: ≥ 90%; Nhận dạng hoạt động (ví dụ: mất tập trung): ≥ 85%.
*   **Hiệu quả tài nguyên:** Hệ thống có thể hoạt động ổn định trên các thiết bị biên có cấu hình hạn chế.

## 2.4 Measurable Outcomes (Kết quả có thể đo lường)

*   **Tỷ lệ phát hiện đúng (True Positive Rate) cho buồn ngủ:** > 90% trên tập dữ liệu thử nghiệm.
*   **Tỷ lệ cảnh báo sai (False Positive Rate) cho tất cả các sự kiện:** < 5% trong các kịch bản lái xe bình thường.
*   **Thời gian tích hợp module mới:** < 16 giờ làm việc.
*   **Tài liệu được hội đồng đánh giá "Tốt" trở lên.**
