# 4. User Journeys (Hành trình Người dùng)

## 4.1 Hành trình 1: Tài xế Anh Minh - Phát hiện và Cảnh báo Sớm

**Persona:** Anh Minh, kỹ sư phần mềm trẻ, thường lái xe về nhà muộn trên đường cao tốc quen thuộc. Nỗi lo lắng của anh là những khoảnh khắc mất tập trung ngắn ngủi khi mệt mỏi có thể dẫn đến nguy hiểm.

**Cảnh mở đầu:** Anh Minh khởi động xe và bắt đầu chuyến đi đêm. Hệ thống DMS được cài đặt trên xe bắt đầu hoạt động một cách thầm lặng.

**Hành động gia tăng:** Khi sự mệt mỏi bắt đầu, Anh Minh ngáp nhẹ và mí mắt hơi trĩu xuống. Ngay lập tức, hệ thống phát ra một tiếng "ping" nhẹ và đèn LED chuyển sang màu vàng. Anh Minh nhận ra tín hiệu, điều chỉnh tư thế và tập trung lại.

**Cao trào:** Sau đó không lâu, Anh Minh trải qua một khoảnh khắc ngủ gật ngắn. Hệ thống phản ứng ngay lập tức với âm thanh cảnh báo dồn dập, đèn LED nhấp nháy đỏ, kéo anh ra khỏi trạng thái nguy hiểm.

**Kết thúc:** Nhờ cảnh báo kịp thời, Anh Minh đã tránh được tai nạn. Anh tấp vào lề đường để nghỉ ngơi và hoàn toàn tin tưởng vào hệ thống DMS như một người bạn đồng hành đáng tin cậy.

## 4.2 Hành trình 2: Giảng viên Thầy Hùng - Đánh giá và Xác minh

**Persona:** Thầy Hùng, giảng viên hướng dẫn đồ án tốt nghiệp, cần đánh giá và xác minh tính hiệu quả của hệ thống DMS. Nỗi lo của thầy là làm thế nào để có bằng chứng khách quan về hoạt động của hệ thống.

**Cảnh mở đầu:** Sau buổi chạy thử nghiệm, Thầy Hùng yêu cầu sinh viên chứng minh hệ thống đã hoạt động như thế nào.

**Hành động gia tăng:** Sinh viên trình bày một tệp nhật ký (log file) chi tiết, hiển thị danh sách các sự kiện được ghi lại cùng dấu thời gian và các chỉ số liên quan (ví dụ: EAR, Head_Pitch, loại cảnh báo).

**Cao trào:** Thầy Hùng chọn một sự kiện "Microsleep Alert" trong log để kiểm tra. Sinh viên hiển thị đoạn video hoặc hình ảnh được lưu lại chính xác tại thời điểm cảnh báo đó. Hình ảnh/video cho thấy rõ ràng tài xế đã nhắm mắt và gật đầu, khớp hoàn toàn với dữ liệu hệ thống.

**Kết thúc:** Thầy Hùng bị thuyết phục bởi bằng chứng khách quan và minh bạch, đánh giá cao chất lượng thực thi và khả năng xác minh kết quả của đồ án.

## 4.3 Journey Requirements Summary (Tóm tắt Yêu cầu từ Hành trình)

Các hành trình người dùng đã tiết lộ các yêu cầu quan trọng sau cho hệ thống DMS:

*   **Phát hiện trạng thái tài xế:** Cần có khả năng phát hiện buồn ngủ (bao gồm ngáp, mắt nhắm), mất tập trung (hướng đầu, hướng nhìn).
*   **Hệ thống cảnh báo đa cấp:** Cảnh báo sớm, nhẹ nhàng và cảnh báo khẩn cấp, rõ ràng.
*   **Ghi log sự kiện:** Hệ thống phải ghi lại chi tiết các sự kiện cảnh báo, bao gồm dấu thời gian, loại sự kiện và các chỉ số liên quan.
*   **Lưu trữ bằng chứng:** Có khả năng lưu trữ hình ảnh hoặc video ngắn tại thời điểm các sự kiện cảnh báo quan trọng.
*   **Cấu hình nhạy cảm:** Hệ thống cần có khả năng điều chỉnh độ nhạy của các cảnh báo.
*   **Hoạt động không xâm phạm:** Hệ thống hoạt động hiệu quả mà không gây mất tập trung hay khó chịu cho người lái xe.
