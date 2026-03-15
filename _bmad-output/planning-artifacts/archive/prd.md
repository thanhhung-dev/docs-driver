---
stepsCompleted: ['step-01-init', 'step-02-discovery', 'step-02b-vision', 'step-02c-executive-summary', 'step-03-success', 'step-05-domain', 'step-06-innovation', 'step-08-scoping', 'step-09-functional', 'step-10-nonfunctional', 'step-11-polish']
inputDocuments: []
workflowType: 'prd'
classification:
  projectType: iot_embedded
  domain: automotive
  complexity: high
  projectContext: brownfield
---

# Product Requirements Document - Driver Monitoring System (DMS)

**Author:** hung-thanh
**Date:** Tuesday, March 10, 2026

## 1. Executive Summary

Dự án "Hệ thống Giám sát Tài xế (DMS)" nhằm mục đích phát triển một nguyên mẫu hệ thống nhúng/IoT hoạt động trong lĩnh vực ô tô. Tầm nhìn cốt lõi là xây dựng một nguyên mẫu DMS có độ chính xác cao, có khả năng phân tích toàn diện các yếu tố trạng thái của tài xế (bao gồm buồn ngủ, mất tập trung và các hành vi nguy hiểm) trên các thiết bị phần cứng phổ thông (như Jetson Nano hoặc Raspberry Pi 4). Mục tiêu cuối cùng là chứng minh tính khả thi của việc triển khai một giải pháp giám sát tài xế hiệu quả và đáng tin cậy trong bối cảnh đồ án tốt nghiệp.

Hệ thống này nổi bật không chỉ vì khả năng phát hiện buồn ngủ đơn thuần, mà bởi nó hoạt động như một công cụ đánh giá rủi ro toàn diện. Bằng cách kết hợp dữ liệu từ nhiều phân tích về trạng thái của tài xế, DMS cung cấp các cảnh báo an toàn thông minh và chính xác hơn. Điều này được thực hiện hiệu quả trên phần cứng biên (edge hardware) có chi phí thấp, cho thấy tiềm năng áp dụng rộng rãi. Insight cốt lõi là một hệ thống DMS thực sự hiệu quả đòi hỏi sự tổng hợp và phân tích đa yếu tố, thay vì chỉ dựa vào một chỉ số đơn lẻ, từ đó tạo ra một mạng lưới an toàn mạnh mẽ và đáng tin cậy hơn cho người lái xe.

Dự án được phân loại là một **Hệ thống nhúng/IoT (iot_embedded)** trong **lĩnh vực ô tô (automotive)**. Mức độ phức tạp được đánh giá là **cao (high)** do các yêu cầu về hiệu suất thời gian thực, độ chính xác cao và các tiêu chuẩn an toàn. Đây là một **dự án brownfield** do có sẵn các tài liệu kiến trúc ban đầu.

## 2. Success Criteria

### 2.1 User Success (Thành công của Người dùng)

Người dùng sẽ coi hệ thống là thành công nếu nó đóng vai trò như một người bạn đồng hành đáng tin cậy, giúp họ nhận thức được các dấu hiệu mệt mỏi hoặc mất tập trung từ sớm. Tiêu chí thành công chính là:

*   **Cảnh báo sớm và nhẹ nhàng:** Hệ thống có khả năng đưa ra các cảnh báo ở mức độ thấp (ví dụ: một tiếng "ping" nhẹ hoặc đèn LED thay đổi màu sắc) ngay khi phát hiện các dấu hiệu ban đầu của sự mệt mỏi hoặc mất tập trung.
*   **Độ tin cậy cao, ít phiền nhiễu:** Người dùng tin tưởng vào các cảnh báo và không cảm thấy bị làm phiền bởi các cảnh báo sai. Tỷ lệ cảnh báo sai (false positives) phải đủ thấp để không gây ra "sự mỏi mệt vì cảnh báo" (alert fatigue).
*   **Tạo cảm giác an tâm:** Người dùng cảm thấy an toàn và tự tin hơn khi lái xe, biết rằng có một "phụ lái" ảo đang theo dõi và hỗ trợ họ.

### 2.2 Project Success (Thành công của Đồ án)

Là một đồ án tốt nghiệp, dự án được coi là thành công khi đạt được các mục tiêu học thuật và kỹ thuật sau:

*   **Chứng minh tính khả thi:** Hệ thống hoàn chỉnh (end-to-end) hoạt động ổn định trên phần cứng mục tiêu (Jetson Nano hoặc Raspberry Pi 4), đáp ứng các chỉ số hiệu suất cốt lõi (≥15 FPS, độ trễ <200ms).
*   **Chứng minh khả năng mở rộng:** Thể hiện được khả năng tích hợp một module phát hiện hành vi mới vào kiến trúc hệ thống một cách nhanh chóng (ví dụ: dưới 2 ngày công) mà không cần thay đổi cấu trúc lõi.
*   **Hoàn thành tài liệu:** Toàn bộ tài liệu thiết kế, báo cáo kết quả và mã nguồn được hoàn thiện, có chất lượng cao, sẵn sàng cho việc đánh giá của hội đồng.

### 2.3 Technical Success (Thành công về Kỹ thuật)

Thành công về mặt kỹ thuật được đo lường bằng các chỉ số hiệu suất và độ chính xác cụ thể đã được đề ra trong tài liệu kiến trúc:

*   **Hiệu suất:** Tốc độ xử lý video đạt tối thiểu 15 khung hình mỗi giây (FPS).
*   **Độ trễ:** Thời gian từ khi phát hiện sự kiện đến khi đưa ra cảnh báo dưới 200 mili giây.
*   **Độ chính xác:** Phát hiện trạng thái buồn ngủ: ≥ 90%; Nhận dạng hoạt động (ví dụ: mất tập trung): ≥ 85%.
*   **Hiệu quả tài nguyên:** Hệ thống có thể hoạt động ổn định trên các thiết bị biên có cấu hình hạn chế.

### 2.4 Measurable Outcomes (Kết quả có thể đo lường)

*   **Tỷ lệ phát hiện đúng (True Positive Rate) cho buồn ngủ:** > 90% trên tập dữ liệu thử nghiệm.
*   **Tỷ lệ cảnh báo sai (False Positive Rate) cho tất cả các sự kiện:** < 5% trong các kịch bản lái xe bình thường.
*   **Thời gian tích hợp module mới:** < 16 giờ làm việc.
*   **Tài liệu được hội đồng đánh giá "Tốt" trở lên.**

## 3. Product Scope Overview (Tổng quan Phạm vi Sản phẩm)

### 3.1 MVP - Sản phẩm Khả dụng Tối thiểu (Mục tiêu cho Đồ án)

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

### 3.2 Post-MVP Features (Tính năng phát triển sau Đồ án)

Các tính năng có thể phát triển sau khi hoàn thành MVP: Hỗ trợ đa nền tảng phần cứng, xây dựng giao diện người dùng đồ họa (GUI) nâng cao, cá nhân hóa cho từng tài xế, và hoàn thiện cơ chế cập nhật OTA (Over-The-Air) từ xa.

### 3.3 Vision (Tầm nhìn Tương lai)

Định hướng dài hạn cho sản phẩm: Tích hợp với hệ thống của xe, kết nối đám mây để quản lý đội xe, cá nhân hóa theo từng tài xế.

## 4. User Journeys (Hành trình Người dùng)

### 4.1 Hành trình 1: Tài xế Anh Minh - Phát hiện và Cảnh báo Sớm

**Persona:** Anh Minh, kỹ sư phần mềm trẻ, thường lái xe về nhà muộn trên đường cao tốc quen thuộc. Nỗi lo lắng của anh là những khoảnh khắc mất tập trung ngắn ngủi khi mệt mỏi có thể dẫn đến nguy hiểm.

**Cảnh mở đầu:** Anh Minh khởi động xe và bắt đầu chuyến đi đêm. Hệ thống DMS được cài đặt trên xe bắt đầu hoạt động một cách thầm lặng.

**Hành động gia tăng:** Khi sự mệt mỏi bắt đầu, Anh Minh ngáp nhẹ và mí mắt hơi trĩu xuống. Ngay lập tức, hệ thống phát ra một tiếng "ping" nhẹ và đèn LED chuyển sang màu vàng. Anh Minh nhận ra tín hiệu, điều chỉnh tư thế và tập trung lại.

**Cao trào:** Sau đó không lâu, Anh Minh trải qua một khoảnh khắc ngủ gật ngắn. Hệ thống phản ứng ngay lập tức với âm thanh cảnh báo dồn dập, đèn LED nhấp nháy đỏ, kéo anh ra khỏi trạng thái nguy hiểm.

**Kết thúc:** Nhờ cảnh báo kịp thời, Anh Minh đã tránh được tai nạn. Anh tấp vào lề đường để nghỉ ngơi và hoàn toàn tin tưởng vào hệ thống DMS như một người bạn đồng hành đáng tin cậy.

### 4.2 Hành trình 2: Giảng viên Thầy Hùng - Đánh giá và Xác minh

**Persona:** Thầy Hùng, giảng viên hướng dẫn đồ án tốt nghiệp, cần đánh giá và xác minh tính hiệu quả của hệ thống DMS. Nỗi lo của thầy là làm thế nào để có bằng chứng khách quan về hoạt động của hệ thống.

**Cảnh mở đầu:** Sau buổi chạy thử nghiệm, Thầy Hùng yêu cầu sinh viên chứng minh hệ thống đã hoạt động như thế nào.

**Hành động gia tăng:** Sinh viên trình bày một tệp nhật ký (log file) chi tiết, hiển thị danh sách các sự kiện được ghi lại cùng dấu thời gian và các chỉ số liên quan (ví dụ: EAR, Head_Pitch, loại cảnh báo).

**Cao trào:** Thầy Hùng chọn một sự kiện "Microsleep Alert" trong log để kiểm tra. Sinh viên hiển thị đoạn video hoặc hình ảnh được lưu lại chính xác tại thời điểm cảnh báo đó. Hình ảnh/video cho thấy rõ ràng tài xế đã nhắm mắt và gật đầu, khớp hoàn toàn với dữ liệu hệ thống.

**Kết thúc:** Thầy Hùng bị thuyết phục bởi bằng chứng khách quan và minh bạch, đánh giá cao chất lượng thực thi và khả năng xác minh kết quả của đồ án.

### 4.3 Journey Requirements Summary (Tóm tắt Yêu cầu từ Hành trình)

Các hành trình người dùng đã tiết lộ các yêu cầu quan trọng sau cho hệ thống DMS:

*   **Phát hiện trạng thái tài xế:** Cần có khả năng phát hiện buồn ngủ (bao gồm ngáp, mắt nhắm), mất tập trung (hướng đầu, hướng nhìn).
*   **Hệ thống cảnh báo đa cấp:** Cảnh báo sớm, nhẹ nhàng và cảnh báo khẩn cấp, rõ ràng.
*   **Ghi log sự kiện:** Hệ thống phải ghi lại chi tiết các sự kiện cảnh báo, bao gồm dấu thời gian, loại sự kiện và các chỉ số liên quan.
*   **Lưu trữ bằng chứng:** Có khả năng lưu trữ hình ảnh hoặc video ngắn tại thời điểm các sự kiện cảnh báo quan trọng.
*   **Cấu hình nhạy cảm:** Hệ thống cần có khả năng điều chỉnh độ nhạy của các cảnh báo.
*   **Hoạt động không xâm phạm:** Hệ thống hoạt động hiệu quả mà không gây mất tập trung hay khó chịu cho người lái xe.

## 5. IoT/Embedded Specific Requirements (Yêu cầu Đặc thù cho IoT/Nhúng)

### 5.1 Project-Type Overview

Dự án DMS là một ứng dụng nhúng/IoT được thiết kế để chạy trên các thiết bị biên có tài nguyên hạn chế như NVIDIA Jetson Nano hoặc Raspberry Pi 4. Trọng tâm là cung cấp khả năng phân tích và cảnh báo tại chỗ, không yêu cầu kết nối mạng liên tục cho hoạt động cốt lõi.

### 5.2 Technical Architecture Considerations

Kiến trúc kỹ thuật cần được tối ưu hóa cho môi trường nhúng, đảm bảo hiệu suất và hiệu quả tài nguyên.

### 5.3 Hardware Requirements

*   **Nền tảng chính:** NVIDIA Jetson Nano 4GB hoặc Raspberry Pi 4 8GB.
*   **Các yêu cầu bổ sung:** Không có yêu cầu phần cứng bổ sung nào ngoài các thông số kỹ thuật đã có của hai nền tảng trên và các thiết bị ngoại vi (camera hồng ngoại, đèn LED, loa).

### 5.4 Connectivity Protocol

*   **MVP:** Hoạt động hoàn toàn cục bộ (offline). Hệ thống sẽ xử lý và lưu trữ dữ liệu trực tiếp trên thiết bị, không yêu cầu kết nối internet hoặc mạng cục bộ cho chức năng giám sát chính.
*   **Tầm nhìn tương lai:** Các tính năng mở rộng có thể bao gồm kết nối mạng cho việc cập nhật dữ liệu, báo cáo từ xa hoặc quản lý đội xe.

### 5.5 Power Profile

Hệ thống được thiết kế để hoạt động khi được cắm điện liên tục.

### 5.6 Security Model

Đối với phạm vi đồ án tốt nghiệp, các yêu cầu về bảo mật không phải là ưu tiên chính.

### 5.7 Update Mechanism

*   **Cập nhật OTA (Over-The-Air):** Có kế hoạch hỗ trợ cập nhật phần mềm và mô hình AI từ xa qua cơ chế OTA trong tương lai.

### 5.8 Implementation Considerations

Việc triển khai cần tập trung vào việc sử dụng các thư viện và framework được tối ưu hóa cho thiết bị biên và ngôn ngữ lập trình hiệu quả (Python) để đạt được các mục tiêu hiệu suất.

## 6. Project Scoping & Phased Development (Phạm vi Dự án & Phát triển theo Giai đoạn)

### 6.1 MVP Strategy & Philosophy

**MVP Approach:** "MVP Giải quyết Vấn đề" (Problem-Solving MVP). Chiến lược này tập trung vào việc chứng minh một cách thuyết phục rằng công nghệ cốt lõi của hệ thống có khả năng hoạt động hiệu quả. Mục tiêu là xây dựng một nguyên mẫu chức năng để trả lời câu hỏi: "Hệ thống có thể phát hiện một cách đáng tin cậy sự mệt mỏi và mất tập trung trên phần cứng biên không?". Cách tiếp cận này trực tiếp giải quyết các tiêu chí thành công quan trọng nhất cho một đồ án tốt nghiệp: chứng minh tính khả thi và tiềm năng kỹ thuật.

**Resource Requirements:** Dự án yêu cầu kiến thức về Python, Computer Vision (OpenCV, Dlib), và Machine Learning (TensorFlow Lite), cùng với khả năng làm việc với phần cứng nhúng (Jetson Nano/Raspberry Pi).

### 6.2 Post-MVP Features

**Phase 2 (Growth):**
*   **Mở rộng Nhận diện Hành vi:** Thêm các module phát hiện hành vi phức tạp khác (ví dụ: sử dụng điện thoại).
*   **Giao diện Đồ họa (GUI):** Xây dựng một dashboard đơn giản để xem lại lịch sử chuyến đi.
*   **Hoàn thiện Cập nhật OTA:** Triển khai đầy đủ cơ chế cập nhật phần mềm từ xa.

**Phase 3 (Expansion):**
*   **Tích hợp sâu hơn:** Kết nối với hệ thống CAN bus của xe.
*   **Kết nối Đám mây:** Đồng bộ hóa dữ liệu sự kiện lên một nền tảng đám mây.
*   **Cá nhân hóa:** Cho phép hệ thống tự học và điều chỉnh độ nhạy cảnh báo.

### 6.3 Risk Mitigation Strategy

**Technical Risks:**
*   **Rủi ro:** Hiệu suất trên phần cứng có thể không đạt được mục tiêu (≥15 FPS).
*   **Giảm thiểu:** Ưu tiên tối ưu hóa các thuật toán, sử dụng các mô hình AI đã được lượng tử hóa (quantized), và chọn nền tảng phần cứng mạnh hơn nếu cần.
**Market Risks:**
*   **Rủi ro (trong bối cảnh đồ án):** Tính mới của đề tài không được đánh giá cao.
*   **Giảm thiểu:** Nhấn mạnh vào khía cạnh "phân tích toàn diện" và "độ chính xác cao".
**Resource Risks:**
*   **Rủi ro:** Thời gian phát triển có thể không đủ.
*   **Giảm thiểu:** Tuân thủ nghiêm ngặt phạm vi MVP đã xác định.

## 7. Functional Requirements (Các Yêu cầu Chức năng)

### 7.1 Quản lý Đầu vào Video

*   **FR1:** Hệ thống PHẢI có khả năng thu nhận video đầu vào từ camera hồng ngoại được kết nối.
*   **FR2:** Hệ thống PHẢI có khả năng xử lý trước khung hình video (ví dụ: chuyển sang ảnh xám, điều chỉnh độ tương phản) để chuẩn bị cho việc phát hiện.

### 7.2 Phát hiện và Phân tích Trạng thái Tài xế

*   **FR3:** Hệ thống PHẢI có khả năng phát hiện khuôn mặt của tài xế trong khung hình video.
*   **FR4:** Hệ thống PHẢI có khả năng ước tính tư thế đầu (pitch, yaw, roll) của tài xế.
*   **FR5:** Hệ thống PHẢI có khả năng theo dõi trạng thái mắt (ví dụ: mở/đóng, tỷ lệ EAR) của tài xế.
*   **FR6:** Hệ thống PHẢI có khả năng phát hiện hành vi ngáp của tài xế.
*   **FR7:** Hệ thống PHẢI có khả năng xác định hướng nhìn (gaze direction) của tài xế.
*   **FR8:** Hệ thống PHẢI có khả năng tổng hợp dữ liệu từ các phát hiện khuôn mặt, tư thế đầu, trạng thái mắt và ngáp để đánh giá mức độ buồn ngủ của tài xế.
*   **FR9:** Hệ thống PHẢI có khả năng tổng hợp dữ liệu từ hướng đầu và hướng nhìn để đánh giá mức độ mất tập trung của tài xế.
*   **FR10:** Hệ thống PHẢI có khả năng xác định sự kiện "ngủ gật ngắn" (microsleep) của tài xế.

#### 7.2.1 Phát hiện Hành vi Nguy hiểm

*   **FR10.1:** Hệ thống PHẢI có khả năng phát hiện tài xế đang **sử dụng điện thoại** khi gọi điện.
*   **FR10.2:** Hệ thống PHẢI có khả năng phát hiện tài xế đang **uống nước** từ chai/cốc.
*   **FR10.3:** Hệ thống PHẢI có khả năng phát hiện tài xế đang **hút thuốc**.
*   **FR10.4:** Hệ thống PHẢI có khả năng phát hiện **hành vi ngáp** như một hoạt động (bổ sung cho việc phát hiện dựa trên chỉ số).
*   **FR10.5:** Hệ thống PHẢI có khả năng phát hiện khi **tay tài xế không đặt trên vô lăng**.
*   **FR10.6:** Hệ thống PHẢI có khả năng phát hiện khi **tay tài xế vươn ra ngoài cửa sổ**.
*   **FR10.7:** Hệ thống PHẢI có khả năng phát hiện tài xế đang **nhìn vào thiết bị định vị** (điện thoại/GPS).

### 7.3 Quản lý Cảnh báo

*   **FR11:** Hệ thống PHẢI có khả năng kích hoạt cảnh báo sớm, nhẹ nhàng (ví dụ: tín hiệu âm thanh nhẹ, đèn LED chuyển màu) khi phát hiện dấu hiệu ban đầu của sự buồn ngủ hoặc mất tập trung.
*   **FR12:** Hệ thống PHẢI có khả năng kích hoạt cảnh báo khẩn cấp, rõ ràng (ví dụ: âm thanh dồn dập, đèn LED nhấp nháy) khi phát hiện tình trạng nguy hiểm cao (ví dụ: ngủ gật ngắn hoặc các hành vi nguy hiểm).

### 7.4 Quản lý Dữ liệu và Bằng chứng

*   **FR13:** Hệ thống PHẢI có khả năng ghi lại chi tiết mọi sự kiện cảnh báo (loại cảnh báo, thời gian, mức độ, các chỉ số liên quan) vào một tệp log hoặc cơ sở dữ liệu trên thiết bị.
*   **FR14:** Hệ thống PHẢI có khả năng lưu trữ một hình ảnh (ảnh chụp nhanh) tại thời điểm xảy ra cảnh báo khẩn cấp.
*   **FR15:** Người dùng (ví dụ: giảng viên/người đánh giá) PHẢI có khả năng truy cập và xem lại các tệp log sự kiện đã ghi.
*   **FR16:** Người dùng (ví dụ: giảng viên/người đánh giá) PHẢI có khả năng xem lại các hình ảnh bằng chứng đã lưu.

### 7.5 Quản lý Cấu hình

*   **FR17:** Hệ thống PHẢI có khả năng tải và áp dụng các thông số cấu hình từ một tệp (ví dụ: ngưỡng cảnh báo, độ nhạy).
*   **FR18:** Hệ thống PHẢI có khả năng điều chỉnh độ nhạy của các thuật toán phát hiện và cảnh báo thông qua cấu hình.

## 8. Non-Functional Requirements (Yêu cầu Phi Chức năng)

### 8.1 Performance (Hiệu suất)

*   **NFR1: Tốc độ xử lý khung hình:** Hệ thống PHẢI có khả năng xử lý và phân tích video đầu vào ở tốc độ tối thiểu **15 khung hình mỗi giây (FPS)** trong suốt quá trình hoạt động.
*   **NFR2: Độ trễ cảnh báo:** Thời gian từ khi hệ thống phát hiện một sự kiện cần cảnh báo (ví dụ: ngủ gật ngắn) đến khi kích hoạt cảnh báo tương ứng (âm thanh, đèn LED) PHẢI dưới **200 mili giây**.
*   **NFR3: Hiệu quả tài nguyên:** Hệ thống PHẢI có khả năng duy trì hoạt động ổn định trên phần cứng biên (Jetson Nano/Raspberry Pi 4) mà không gây quá tải tài nguyên (CPU/GPU và RAM) khi hoạt động liên tục trong thời gian dài.

### 8.2 Reliability (Độ tin cậy)

*   **NFR4: Thời gian hoạt động liên tục:** Hệ thống PHẢI có khả năng hoạt động liên tục trong ít nhất **4 giờ** mà không gặp lỗi phần mềm nghiêm trọng hoặc yêu cầu khởi động lại.
*   **NFR5: Xử lý lỗi đầu vào video:** Nếu luồng video từ camera bị gián đoạn hoặc không khả dụng, hệ thống PHẢI hiển thị cảnh báo rõ ràng cho người dùng (ví dụ: đèn LED lỗi, âm thanh thông báo) và tự động cố gắng khôi phục kết nối camera.
*   **NFR6: Giảm thiểu cảnh báo sai:** Hệ thống PHẢI duy trì tỷ lệ cảnh báo sai (false positives) dưới **5%** trong các kịch bản lái xe bình thường (không có dấu hiệu buồn ngủ/mất tập trung).
*   **NFR7: Khả năng cấu hình:** Hệ thống PHẢI cho phép điều chỉnh các ngưỡng phát hiện và độ nhạy cảnh báo thông qua tệp cấu hình để tối ưu hóa độ tin cậy và sự phù hợp với các điều kiện khác nhau.