---
stepsCompleted: ['step-01-validate-prerequisites', 'step-02-design-epics', 'step-03-create-stories', 'step-04-final-validation']
inputDocuments: 
  - _bmad-output/planning-artifacts/prd/index.md
  - _bmad-output/architecture/ARCHITECTURE-Driver-Monitoring-System.md
  - _bmad-output/ui-design/UI-INTERFACE-DESIGN-Driver-Monitoring-System.md
---

# docs-driver - Phân rã Epic và Story

## Tổng quan

Tài liệu này cung cấp bản phân rã chi tiết các Epic và Story cho dự án docs-driver, chuyển hóa các yêu cầu từ PRD, Thiết kế UX và Kiến trúc hệ thống thành các câu chuyện người dùng có thể triển khai được.

## Danh mục Yêu cầu

### Yêu cầu Chức năng (Functional Requirements)

*   **FR1:** Hệ thống PHẢI có khả năng thu nhận dữ liệu video từ camera hồng ngoại (IR) được kết nối.
*   **FR2:** Hệ thống PHẢI có khả năng xử lý trước các khung hình video (ví dụ: chuyển sang ảnh xám, điều chỉnh độ tương phản) để phục vụ nhận diện.
*   **FR3:** Hệ thống PHẢI có khả năng phát hiện khuôn mặt tài xế trong các khung hình video.
*   **FR4:** Hệ thống PHẢI có khả năng ước tính tư thế đầu (pitch, yaw, roll) của tài xế.
*   **FR5:** Hệ thống PHẢI có khả năng theo dõi trạng thái mắt (ví dụ: mở/đóng, tỷ lệ EAR).
*   **FR6:** Hệ thống PHẢI có khả năng phát hiện hành vi ngáp.
*   **FR7:** Hệ thống PHẢI có khả năng xác định hướng nhìn (gaze direction).
*   **FR8:** Hệ thống PHẢI có khả năng tổng hợp dữ liệu từ phát hiện khuôn mặt, tư thế đầu, trạng thái mắt và ngáp để đánh giá mức độ buồn ngủ.
*   **FR9:** Hệ thống PHẢI có khả năng tổng hợp dữ liệu từ hướng đầu và hướng nhìn để đánh giá mức độ mất tập trung.
*   **FR10:** Hệ thống PHẢI có khả năng xác định các sự kiện "ngủ gật ngắn" (microsleep).
*   **FR10.1:** Hệ thống PHẢI có khả năng phát hiện tài xế **sử dụng điện thoại** (gọi điện).
*   **FR10.2:** Hệ thống PHẢI có khả năng phát hiện tài xế đang **uống nước** từ chai/cốc.
*   **FR10.3:** Hệ thống PHẢI có khả năng phát hiện tài xế đang **hút thuốc**.
*   **FR10.4:** Hệ thống PHẢI có khả năng phát hiện **hành vi ngáp** như một hoạt động cụ thể.
*   **FR10.5:** Hệ thống PHẢI có khả năng phát hiện khi **tay không đặt trên vô lăng**.
*   **FR10.6:** Hệ thống PHẢI có khả năng phát hiện khi **tay vươn ra ngoài cửa sổ**.
*   **FR10.7:** Hệ thống PHẢI có khả năng phát hiện tài xế đang **nhìn vào các thiết bị định vị** (điện thoại/GPS).
*   **FR11:** Hệ thống PHẢI có khả năng kích hoạt các cảnh báo sớm, nhẹ nhàng (ví dụ: âm thanh nhẹ, đèn LED đổi màu) khi phát hiện dấu hiệu ban đầu của buồn ngủ hoặc mất tập trung.
*   **FR12:** Hệ thống PHẢI có khả năng kích hoạt các cảnh báo khẩn cấp, rõ ràng (ví dụ: âm thanh dồn dập, đèn LED nhấp nháy) khi phát hiện các tình huống rủi ro cao (ngủ gật ngắn hoặc hành vi nguy hiểm).
*   **FR13:** Hệ thống PHẢI có khả năng ghi nhật ký chi tiết mọi sự kiện cảnh báo (loại, thời gian, mức độ, các chỉ số) vào tệp hoặc cơ sở dữ liệu.
*   **FR14:** Hệ thống PHẢI có khả năng lưu trữ hình ảnh bằng chứng (snapshot) tại thời điểm xảy ra cảnh báo khẩn cấp.
*   **FR15:** Người dùng PHẢI có khả năng truy cập và xem lại nhật ký các sự kiện đã ghi.
*   **FR16:** Người dùng PHẢI có khả năng xem lại các hình ảnh bằng chứng đã lưu trữ.
*   **FR17:** Hệ thống PHẢI có khả năng tải và áp dụng các thông số cấu hình (ví dụ: ngưỡng cảnh báo, độ nhạy) từ một tệp tin.
*   **FR18:** Hệ thống PHẢI có khả năng điều chỉnh độ nhạy phát hiện và cảnh báo thông qua cấu hình.

### Yêu cầu Phi chức năng (Non-Functional Requirements)

*   **NFR1: Tốc độ xử lý:** Hệ thống PHẢI xử lý và phân tích video ở tốc độ tối thiểu **15 FPS**.
*   **NFR2: Độ trễ cảnh báo:** Thời gian từ khi phát hiện đến khi kích hoạt cảnh báo PHẢI dưới **200 mili giây**.
*   **NFR3: Hiệu quả tài nguyên:** Hệ thống PHẢI hoạt động ổn định trên phần cứng biên (Jetson Nano/RPi 4).
*   **NFR4: Hoạt động liên tục:** Hệ thống PHẢI hoạt động liên tục trong ít nhất **4 giờ**.
*   **NFR5: Xử lý lỗi video:** Cảnh báo rõ ràng khi luồng video bị gián đoạn và tự động cố gắng khôi phục.
*   **NFR6: Giảm thiểu cảnh báo sai:** Duy trì tỷ lệ cảnh báo sai dưới **5%**.
*   **NFR7: Khả năng cấu hình:** Cho phép điều chỉnh các ngưỡng và độ nhạy thông qua tệp cấu hình.

### Yêu cầu Bổ sung

#### Từ Tài liệu Kiến trúc
*   **Mô hình Kiến trúc:** Kiến trúc Pipeline (Pipes and Filters).
*   **Công nghệ:** Python 3.8, OpenCV 4.5, dlib, TensorFlow Lite, SQLite3.
*   **Phần cứng:** Jetson Nano hoặc Raspberry Pi 4.
*   **Cơ sở dữ liệu:** Schema SQLite cho việc ghi nhật ký sự kiện (ID, Session, Loại, Thời gian, Dữ liệu).
*   **Tính Module:** Các lớp độc lập cho Input, Detection, Analysis, Action và Storage.

#### Từ Thiết kế UX
*   **Framework giao diện:** PyQt5 cho màn hình 800x480 (7-inch) hoặc 1024x600 (10-inch).
*   **Phân cấp cảnh báo:** Hệ thống 4 cấp độ (Critical, High, Medium, Info) với màu sắc và âm thanh đặc trưng.
*   **Khóa an toàn:** Màn hình cài đặt chỉ truy cập được khi xe đang dừng (Parked).
*   **Thành phần Dashboard:** Luồng video trực tiếp, các chỉ số trạng thái (EAR, Drowsiness, Attention) và dòng thời gian sự kiện.

### Bản đồ Bao phủ Yêu cầu (FR Coverage Map)

- **FR1, FR2, FR3, FR4, FR5, FR6, FR7:** Epic 1 - Thu nhận video và Nhận diện nền tảng.
- **FR8, FR9, FR10, FR11, FR12:** Epic 2 - Phân tích trạng thái và Cảnh báo.
- **FR10.1 - FR10.7:** Epic 3 - Nhận diện hành vi nguy hiểm đặc thù.
- **FR13, FR14, FR15, FR16:** Epic 4 - Quản lý dữ liệu và Bằng chứng.
- **FR17, FR18:** Epic 5 - Giao diện và Quản lý cấu hình.

## Danh sách Epic

1. **Epic 1: Hệ thống lõi và Nhận thức thị giác**: Thiết lập thu nhận video, xử lý trước và nhận diện cơ bản (mặt, mắt, đầu).
2. **Epic 2: Phân tích trạng thái và Cảnh báo**: Phân tích các đặc điểm nhận diện để xác định mức độ buồn ngủ/mất tập trung và quản lý hệ thống cảnh báo đa cấp.
3. **Epic 3: Nhận diện Hành vi nguy hiểm đặc thù**: Triển khai các mô hình AI để nhận diện 7 hành vi nguy hiểm cụ thể.
4. **Epic 4: Quản lý dữ liệu và Bằng chứng**: Ghi lại các sự kiện cảnh báo và hình ảnh bằng chứng vào SQLite và bộ nhớ cục bộ.
5. **Epic 5: Giao diện và Quản lý cấu hình**: Cung cấp giao diện dashboard và quản lý các thiết lập hệ thống.

---

## Epic 1: Hệ thống lõi và Nhận thức thị giác
Mục tiêu: Khởi tạo hệ thống, thu nhận và xử lý video, thực hiện các nhận diện hình ảnh nền tảng.

### Story 1.1: Thiết lập khung dự án và Thu nhận Video
Với tư cách là **Nhà phát triển**,
Tôi muốn **thiết lập cấu trúc dự án ban đầu và thu nhận luồng video liên tục từ camera IR**,
Để **có một nền tảng module hóa và dữ liệu đầu vào cho việc phân tích tài xế**.

**Tiêu chí chấp nhận:**
**Cho trước** phần cứng mục tiêu (Jetson Nano/RPi 4) và thiết kế Kiến trúc
**Khi** nhà phát triển khởi tạo dự án
**Thì** hệ thống PHẢI tuân thủ cấu trúc thư mục định nghĩa trong Kiến trúc (Input, Detection, Analysis, Action, Storage).
**Và** môi trường PHẢI được cấu hình với Python 3.8 và các thư viện cần thiết (OpenCV, v.v.).
**Và** hệ thống PHẢI mở thành công luồng video ở độ phân giải 640x480.
**Và** tốc độ thu nhận khung hình PHẢI đạt ít nhất 15 FPS (NFR1).
**Và** nếu camera không kết nối, hệ thống PHẢI trả về lỗi cụ thể (NFR5).

### Story 1.2: Pipeline xử lý trước hình ảnh
Với tư cách là **Hệ thống DMS**,
Tôi muốn **xử lý trước các khung hình thô (ảnh xám, độ tương phản)**,
Để **các module nhận diện nhận được đầu vào tối ưu**.

**Tiêu chí chấp nhận:**
**Cho trước** một khung hình BGR thô từ camera
**Khi** đi qua module xử lý trước
**Thì** khung hình PHẢI được chuyển sang ảnh xám.
**Và** độ tương phản PHẢI được tăng cường (ví dụ: dùng CLAHE).
**Và** đầu ra PHẢI sẵn sàng cho Lớp Nhận diện.

### Story 1.3: Phát hiện và Theo dõi Khuôn mặt
Với tư cách là **Hệ thống DMS**,
Tôi muốn **phát hiện và theo dõi khuôn mặt tài xế trong thời gian thực**,
Để **có thể trích xuất các điểm mốc khuôn mặt phục vụ phân tích**.

**Tiêu chí chấp nhận:**
**Cho trước** một khung hình đã xử lý trước
**Khi** được xử lý bởi module Phát hiện khuôn mặt
**Thì** một hộp giới hạn (bounding box) của khuôn mặt PHẢI được trả về.
**Và** trạng thái "Không tìm thấy tài xế" PHẢI được báo cáo nếu không phát hiện được khuôn mặt trong khoảng thời gian chờ.

### Story 1.4: Trích xuất các điểm mốc khuôn mặt
Với tư cách là **Hệ thống DMS**,
Tôi muốn **trích xuất 68 điểm mốc khuôn mặt từ khuôn mặt đã phát hiện**,
Để **có thể phân tích các đặc điểm như mắt và miệng**.

**Tiêu chí chấp nhận:**
**Cho trước** hộp giới hạn khuôn mặt
**Khi** được xử lý bởi module Dự đoán điểm mốc (dlib/mediapipe)
**Thì** 68 tọa độ PHẢI được trả về ánh xạ đúng các vị trí mắt, mũi, miệng và hàm.

---

## Epic 2: Phân tích trạng thái và Cảnh báo
Mục tiêu: Phân tích dữ liệu nhận thức để xác định mức độ rủi ro và kích hoạt các cảnh báo vật lý và hình ảnh phù hợp.

### Story 2.1: Đánh giá mức độ buồn ngủ
Với tư cách là **Hệ thống DMS**,
Tôi muốn **tính toán điểm số buồn ngủ dựa trên chỉ số EAR và tần suất ngáp**,
Để **có thể xác định khi nào tài xế đang trở nên mệt mỏi**.

**Tiêu chí chấp nhận:**
**Cho trước** dữ liệu EAR và MAR liên tục (Epic 1)
**Khi** được xử lý bởi module Phân tích buồn ngủ
**Thì** một điểm số (0-100%) PHẢI được tạo ra.
**Và** chỉ số PERCLOS (Tỷ lệ phần trăm đóng mắt) PHẢI được tính toán trên một cửa sổ thời gian trượt.

### Story 2.3: Phát hiện sự kiện Ngủ gật ngắn (Microsleep)
Với tư cách là **Hệ thống DMS**,
Tôi muốn **phát hiện các sự kiện "ngủ gật ngắn" (mắt nhắm >1 giây)**,
Để **có thể kích hoạt các cảnh báo khẩn cấp ưu tiên cao**.

**Tiêu chí chấp nhận:**
**Cho trước** các giá trị EAR liên tục
**When** EAR duy trì dưới ngưỡng nhắm mắt trong thời gian lâu hơn quy định
**Then** một sự kiện "Microsleep" PHẢI được tạo ra ngay lập tức.

---

## Epic 3: Nhận diện Hành vi nguy hiểm đặc thù
Mục tiêu: Triển khai các mô hình AI chuyên biệt để phát hiện các hành vi rủi ro cao cụ thể vượt ra ngoài các dấu hiệu sinh lý cơ bản.

### Story 3.1: Phát hiện sử dụng điện thoại
Với tư cách là **Hệ thống DMS**,
Tôi muốn **nhận diện khi tài xế đang cầm điện thoại sát tai**,
Để **có thể cảnh báo về hành vi sử dụng điện thoại trái phép**.

**Tiêu chí chấp nhận:**
**Cho trước** một khung hình video (Lớp Nhận diện)
**Khi** module Nhận diện hành động xác định mẫu "Gọi điện"
**Thì** một sự kiện "Hành vi nguy hiểm: Điện thoại" PHẢI được tạo ra.

### Story 3.2: Nhận diện hành vi Uống nước/Ăn
Với tư cách là **Hệ thống DMS**,
Tôi muốn **phát hiện khi tài xế đang uống nước từ chai hoặc cốc**,
Để **có thể cảnh báo về việc làm việc riêng khi lái xe**.

**Tiêu chí chấp nhận:**
**Cho trước** một khung hình video
**Khi** một chai/cốc được phát hiện gần vùng miệng
**Thì** một sự kiện "Hành vi nguy hiểm: Uống nước" PHẢI được tạo ra.

### Story 3.3: Phát hiện Hút thuốc
Với tư cách là **Hệ thống DMS**,
Tôi muốn **phát hiện nếu tài xế đang hút thuốc**,
Để **có thể kích hoạt cảnh báo an toàn**.

**Tiêu chí chấp nhận:**
**Cho trước** một khung hình video
**Khi** module Nhận diện hành động xác định hành vi hút thuốc
**Thì** một sự kiện "Hành vi nguy hiểm: Hút thuốc" PHẢI được tạo ra.

---

## Epic 4: Quản lý dữ liệu và Bằng chứng
Mục tiêu: Lưu trữ các sự kiện chuyến đi và bằng chứng hình ảnh để xem lại và kiểm tra trong tương lai.

### Story 4.1: Tích hợp Cơ sở dữ liệu SQLite
Với tư cách là **Hệ thống DMS**,
Tôi muốn **lưu trữ các sự kiện cảnh báo vào cơ sở dữ liệu SQLite cục bộ**,
Để **duy trì nhật ký lịch sử của chuyến đi**.

**Tiêu chí chấp nhận:**
**Cho trước** một sự kiện cảnh báo
**Khi** sự kiện kết thúc
**Thì** các chi tiết sự kiện (ID, thời gian, loại, mức độ, dữ liệu) PHẢI được lưu vào cơ sở dữ liệu.

---

## Epic 5: Giao diện và Quản lý cấu hình
Mục tiêu: Cung cấp giao diện người dùng chính và cho phép tùy chỉnh hành vi hệ thống.

### Story 5.1: Dashboard Giám sát thời gian thực
Với tư cách là **Người dùng**,
Tôi muốn **xem luồng video trực tiếp với các lớp phủ nhận diện (hộp mặt, điểm mốc)**,
Để **tôi có thể xác nhận hệ thống đang hoạt động chính xác**.

**Tiêu chí chấp nhận:**
**Cho trước** màn hình Giám sát trực tiếp
**Khi** hệ thống đang chạy
**Thì** luồng video PHẢI được hiển thị ở tốc độ 15+ FPS.
**Và** các hộp nhận diện cùng các biểu đồ EAR/Attention PHẢI được cập nhật theo thời gian thực.
