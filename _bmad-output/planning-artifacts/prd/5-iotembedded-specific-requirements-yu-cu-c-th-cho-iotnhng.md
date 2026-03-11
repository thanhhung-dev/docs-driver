# 5. IoT/Embedded Specific Requirements (Yêu cầu Đặc thù cho IoT/Nhúng)

## 5.1 Project-Type Overview

Dự án DMS là một ứng dụng nhúng/IoT được thiết kế để chạy trên các thiết bị biên có tài nguyên hạn chế như NVIDIA Jetson Nano hoặc Raspberry Pi 4. Trọng tâm là cung cấp khả năng phân tích và cảnh báo tại chỗ, không yêu cầu kết nối mạng liên tục cho hoạt động cốt lõi.

## 5.2 Technical Architecture Considerations

Kiến trúc kỹ thuật cần được tối ưu hóa cho môi trường nhúng, đảm bảo hiệu suất và hiệu quả tài nguyên.

## 5.3 Hardware Requirements

*   **Nền tảng chính:** NVIDIA Jetson Nano 4GB hoặc Raspberry Pi 4 8GB.
*   **Các yêu cầu bổ sung:** Không có yêu cầu phần cứng bổ sung nào ngoài các thông số kỹ thuật đã có của hai nền tảng trên và các thiết bị ngoại vi (camera hồng ngoại, đèn LED, loa).

## 5.4 Connectivity Protocol

*   **MVP:** Hoạt động hoàn toàn cục bộ (offline). Hệ thống sẽ xử lý và lưu trữ dữ liệu trực tiếp trên thiết bị, không yêu cầu kết nối internet hoặc mạng cục bộ cho chức năng giám sát chính.
*   **Tầm nhìn tương lai:** Các tính năng mở rộng có thể bao gồm kết nối mạng cho việc cập nhật dữ liệu, báo cáo từ xa hoặc quản lý đội xe.

## 5.5 Power Profile

Hệ thống được thiết kế để hoạt động khi được cắm điện liên tục.

## 5.6 Security Model

Đối với phạm vi đồ án tốt nghiệp, các yêu cầu về bảo mật không phải là ưu tiên chính.

## 5.7 Update Mechanism

*   **Cập nhật OTA (Over-The-Air):** Có kế hoạch hỗ trợ cập nhật phần mềm và mô hình AI từ xa qua cơ chế OTA trong tương lai.

## 5.8 Implementation Considerations

Việc triển khai cần tập trung vào việc sử dụng các thư viện và framework được tối ưu hóa cho thiết bị biên và ngôn ngữ lập trình hiệu quả (Python) để đạt được các mục tiêu hiệu suất.
