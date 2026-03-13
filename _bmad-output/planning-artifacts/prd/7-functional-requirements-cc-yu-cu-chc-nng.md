# 7. Functional Requirements (Các Yêu cầu Chức năng)

## 7.1 Quản lý Đầu vào Video

*   **FR1:** Hệ thống PHẢI có khả năng thu nhận video đầu vào từ camera hồng ngoại được kết nối.
*   **FR2:** Hệ thống PHẢI có khả năng xử lý trước khung hình video (ví dụ: chuyển sang ảnh xám, điều chỉnh độ tương phản) để chuẩn bị cho việc phát hiện.

## 7.2 Phát hiện và Phân tích Trạng thái Tài xế

*   **FR3:** Hệ thống PHẢI có khả năng phát hiện khuôn mặt của tài xế trong khung hình video.
*   **FR4:** Hệ thống PHẢI có khả năng ước tính tư thế đầu (pitch, yaw, roll) của tài xế.
*   **FR5:** Hệ thống PHẢI có khả năng theo dõi trạng thái mắt (ví dụ: mở/đóng, tỷ lệ EAR) của tài xế.
*   **FR6:** Hệ thống PHẢI có khả năng phát hiện hành vi ngáp của tài xế.
*   **FR7:** Hệ thống PHẢI có khả năng xác định hướng nhìn (gaze direction) của tài xế.
*   **FR8:** Hệ thống PHẢI có khả năng tổng hợp dữ liệu từ các phát hiện khuôn mặt, tư thế đầu, trạng thái mắt và ngáp để đánh giá mức độ buồn ngủ của tài xế.
*   **FR9:** Hệ thống PHẢI có khả năng tổng hợp dữ liệu từ hướng đầu và hướng nhìn để đánh giá mức độ mất tập trung của tài xế.
*   **FR10:** Hệ thống PHẢI có khả năng xác định sự kiện "ngủ gật ngắn" (microsleep) của tài xế.

### 7.2.1 Phát hiện Hành vi Nguy hiểm

*   **FR10.1:** Hệ thống PHẢI có khả năng phát hiện tài xế đang **sử dụng điện thoại** khi gọi điện.
*   **FR10.2:** Hệ thống PHẢI có khả năng phát hiện tài xế đang **uống nước** từ chai/cốc.
*   **FR10.3:** Hệ thống PHẢI có khả năng phát hiện tài xế đang **hút thuốc**.
*   **FR10.4:** Hệ thống PHẢI có khả năng phát hiện **hành vi ngáp** như một hoạt động (bổ sung cho việc phát hiện dựa trên chỉ số).
*   **FR10.5:** Hệ thống PHẢI có khả năng phát hiện khi **tay tài xế không đặt trên vô lăng**.
*   **FR10.6:** Hệ thống PHẢI có khả năng phát hiện khi **tay tài xế vươn ra ngoài cửa sổ**.
*   **FR10.7:** Hệ thống PHẢI có khả năng phát hiện tài xế đang **nhìn vào thiết bị định vị** (điện thoại/GPS).

## 7.3 Quản lý Cảnh báo

*   **FR11:** Hệ thống PHẢI có khả năng kích hoạt cảnh báo sớm, nhẹ nhàng (ví dụ: tín hiệu âm thanh nhẹ, đèn LED chuyển màu) khi phát hiện dấu hiệu ban đầu của sự buồn ngủ hoặc mất tập trung.
*   **FR12:** Hệ thống PHẢI có khả năng kích hoạt cảnh báo khẩn cấp, rõ ràng (ví dụ: âm thanh dồn dập, đèn LED nhấp nháy) khi phát hiện tình trạng nguy hiểm cao (ví dụ: ngủ gật ngắn hoặc các hành vi nguy hiểm).

## 7.4 Quản lý Dữ liệu và Bằng chứng

*   **FR13:** Hệ thống PHẢI có khả năng ghi lại chi tiết mọi sự kiện cảnh báo (loại cảnh báo, thời gian, mức độ, các chỉ số liên quan) vào một tệp log hoặc cơ sở dữ liệu trên thiết bị.
*   **FR14:** Hệ thống PHẢI có khả năng lưu trữ một hình ảnh (ảnh chụp nhanh) tại thời điểm xảy ra cảnh báo khẩn cấp.
*   **FR15:** Người dùng (ví dụ: giảng viên/người đánh giá) PHẢI có khả năng truy cập và xem lại các tệp log sự kiện đã ghi.
*   **FR16:** Người dùng (ví dụ: giảng viên/người đánh giá) PHẢI có khả năng xem lại các hình ảnh bằng chứng đã lưu.

## 7.5 Quản lý Cấu hình

*   **FR17:** Hệ thống PHẢI có khả năng tải và áp dụng các thông số cấu hình từ một tệp (ví dụ: ngưỡng cảnh báo, độ nhạy).
*   **FR18:** Hệ thống PHẢI có khả năng điều chỉnh độ nhạy của các thuật toán phát hiện và cảnh báo thông qua cấu hình.
