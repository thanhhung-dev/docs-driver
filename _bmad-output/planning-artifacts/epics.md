---
stepsCompleted: ['step-01-validate-prerequisites', 'step-02-design-epics', 'step-03-create-stories', 'step-04-final-validation']
inputDocuments: 
  - _bmad-output/planning-artifacts/prd.md
  - _bmad-output/architecture/ARCHITECTURE-Driver-Monitoring-System-VI-FULL.md
  - _bmad-output/architecture/ARCHITECTURE-Driver-Monitoring-System.md
  - _bmad-output/ui-design/UI-INTERFACE-DESIGN-Driver-Monitoring-System.md
---

# docs-driver - Epic Breakdown

## Overview

This document provides the complete epic and story breakdown for docs-driver, decomposing the requirements from the PRD, UX Design if it exists, and Architecture requirements into implementable stories.

## Requirements Inventory

### Functional Requirements

*   **FR1:** Hệ thống PHẢI có khả năng thu nhận video đầu vào từ camera hồng ngoại được kết nối.
*   **FR2:** Hệ thống PHẢI có khả năng xử lý trước khung hình video (ví dụ: chuyển sang ảnh xám, điều chỉnh độ tương phản) để chuẩn bị cho việc phát hiện.
*   **FR3:** Hệ thống PHẢI có khả năng phát hiện khuôn mặt của tài xế trong khung hình video.
*   **FR4:** Hệ thống PHẢI có khả năng ước tính tư thế đầu (pitch, yaw, roll) của tài xế.
*   **FR5:** Hệ thống PHẢI có khả năng theo dõi trạng thái mắt (ví dụ: mở/đóng, tỷ lệ EAR) của tài xế.
*   **FR6:** Hệ thống PHẢI có khả năng phát hiện hành vi ngáp của tài xế.
*   **FR7:** Hệ thống PHẢI có khả năng xác định hướng nhìn (gaze direction) của tài xế.
*   **FR8:** Hệ thống PHẢI có khả năng tổng hợp dữ liệu từ các phát hiện khuôn mặt, tư thế đầu, trạng thái mắt và ngáp để đánh giá mức độ buồn ngủ của tài xế.
*   **FR9:** Hệ thống PHẢI có khả năng tổng hợp dữ liệu từ hướng đầu và hướng nhìn để đánh giá mức độ mất tập trung của tài xế.
*   **FR10:** Hệ thống PHẢI có khả năng xác định sự kiện "ngủ gật ngắn" (microsleep) của tài xế.
*   **FR10.1:** Hệ thống PHẢI có khả năng phát hiện tài xế đang **sử dụng điện thoại** khi gọi điện.
*   **FR10.2:** Hệ thống PHẢI có khả năng phát hiện tài xế đang **uống nước** từ chai/cốc.
*   **FR10.3:** Hệ thống PHẢI có khả năng phát hiện tài xế đang **hút thuốc**.
*   **FR10.4:** Hệ thống PHẢI có khả năng phát hiện **hành vi ngáp** như một hoạt động (bổ sung cho việc phát hiện dựa trên chỉ số).
*   **FR10.5:** Hệ thống PHẢI có khả năng phát hiện khi **tay tài xế không đặt trên vô lăng**.
*   **FR10.6:** Hệ thống PHẢI có khả năng phát hiện khi **tay tài xế vươn ra ngoài cửa sổ**.
*   **FR10.7:** Hệ thống PHẢI có khả năng phát hiện tài xế đang **nhìn vào thiết bị định vị** (điện thoại/GPS).
*   **FR11:** Hệ thống PHẢI có khả năng kích hoạt cảnh báo sớm, nhẹ nhàng (ví dụ: tín hiệu âm thanh nhẹ, đèn LED chuyển màu) khi phát hiện dấu hiệu ban đầu của sự buồn ngủ hoặc mất tập trung.
*   **FR12:** Hệ thống PHẢI có khả năng kích hoạt cảnh báo khẩn cấp, rõ ràng (ví dụ: âm thanh dồn dập, đèn LED nhấp nháy) khi phát hiện tình trạng nguy hiểm cao (ví dụ: ngủ gật ngắn hoặc các hành vi nguy hiểm).
*   **FR13:** Hệ thống PHẢI có khả năng ghi lại chi tiết mọi sự kiện cảnh báo (loại cảnh báo, thời gian, mức độ, các chỉ số liên quan) vào một tệp log hoặc cơ sở dữ liệu trên thiết bị.
*   **FR14:** Hệ thống PHẢI có khả năng lưu trữ một hình ảnh (ảnh chụp nhanh) tại thời điểm xảy ra cảnh báo khẩn cấp.
*   **FR15:** Người dùng (ví dụ: giảng viên/người đánh giá) PHẢI có khả năng truy cập và xem lại các tệp log sự kiện đã ghi.
*   **FR16:** Người dùng (ví dụ: giảng viên/người đánh giá) PHẢI có khả năng xem lại các hình ảnh bằng chứng đã lưu.
*   **FR17:** Hệ thống PHẢI có khả năng tải và áp dụng các thông số cấu hình từ một tệp (ví dụ: ngưỡng cảnh báo, độ nhạy).
*   **FR18:** Hệ thống PHẢI có khả năng điều chỉnh độ nhạy của các thuật toán phát hiện và cảnh báo thông qua cấu hình.

### NonFunctional Requirements

*   **NFR1: Tốc độ xử lý khung hình:** Hệ thống PHẢI có khả năng xử lý và phân tích video đầu vào ở tốc độ tối thiểu **15 khung hình mỗi giây (FPS)** trong suốt quá trình hoạt động.
*   **NFR2: Độ trễ cảnh báo:** Thời gian từ khi hệ thống phát hiện một sự kiện cần cảnh báo (ví dụ: ngủ gật ngắn) đến khi kích hoạt cảnh báo tương ứng (âm thanh, đèn LED) PHẢI dưới **200 mili giây**.
*   **NFR3: Hiệu quả tài nguyên:** Hệ thống PHẢI có khả năng duy trì hoạt động ổn định trên phần cứng biên (Jetson Nano/Raspberry Pi 4) mà không gây quá tải tài nguyên (CPU/GPU và RAM) khi hoạt động liên tục trong thời gian dài.
*   **NFR4: Thời gian hoạt động liên tục:** Hệ thống PHẢI có khả năng hoạt động liên tục trong ít nhất **4 giờ** mà không gặp lỗi phần mềm nghiêm trọng hoặc yêu cầu khởi động lại.
*   **NFR5: Xử lý lỗi đầu vào video:** Nếu luồng video từ camera bị gián đoạn hoặc không khả dụng, hệ thống PHẢI hiển thị cảnh báo rõ ràng cho người dùng (ví dụ: đèn LED lỗi, âm thanh thông báo) và tự động cố gắng khôi phục kết nối camera.
*   **NFR6: Giảm thiểu cảnh báo sai:** Hệ thống PHẢI duy trì tỷ lệ cảnh báo sai (false positives) dưới **5%** trong các kịch bản lái xe bình thường (không có dấu hiệu buồn ngủ/mất tập trung).
*   **NFR7: Khả năng cấu hình:** Hệ thống PHẢI cho phép điều chỉnh các ngưỡng phát hiện và độ nhạy cảnh báo thông qua tệp cấu hình để tối ưu hóa độ tin cậy và sự phù hợp với các điều kiện khác nhau.

### Additional Requirements

#### From Architecture Document
*   **Starter Template:** The architecture specifies a detailed directory structure and component design that serves as a starter template for implementation.
*   **Technology Stack:** Python 3.8, OpenCV 4.5, dlib 19.22, TensorFlow Lite 2.8, SQLite3.
*   **Hardware:** Target deployment is NVIDIA Jetson Nano or Raspberry Pi 4.
*   **Data Models:** The architecture defines the data structure for `detection_results` and `risk_event` objects passed between layers.
*   **Database Schema:** Event logs must be stored in an SQLite database with a defined schema (event_id, session_id, event_type, etc.).
*   **Configuration:** System parameters (e.g., EAR thresholds) must be managed via a `config.yaml` file.
*   **Modularity:** The system must be built with independent, loosely-coupled components for each subsystem (Input, Detection, Analysis, Action, Storage).

#### From UX Design Document
*   **UI Framework:** PyQt5 is the recommended framework.
*   **Main Screen Layout:** The UI must include a live video feed panel and a status panel with real-time metrics (EAR, Drowsiness Level, Attention Score).
*   **Alert System:** Implement a 4-level alert hierarchy (Critical, High, Medium, Info) with specific colors (Red, Yellow, Blue), sounds (beeps, dings), and LED behaviors (blinking, solid).
*   **Settings Interface:** A settings screen must be provided to adjust detection thresholds and alert options.
*   **Accessibility:** UI must meet WCAG 2.1 AA contrast ratios and support keyboard navigation (Tab, Enter, Esc).

### FR Coverage Map

FR1: Epic 1 - Thu nhận video đầu vào
FR2: Epic 1 - Xử lý trước khung hình video
FR3: Epic 1 - Phát hiện khuôn mặt
FR4: Epic 1 - Ước tính tư thế đầu
FR5: Epic 1 - Theo dõi trạng thái mắt
FR6: Epic 1 - Phát hiện hành vi ngáp (từ EAR)
FR7: Epic 1 - Xác định hướng nhìn

FR8: Epic 2 - Đánh giá mức độ buồn ngủ
FR9: Epic 2 - Đánh giá mức độ mất tập trung
FR10: Epic 2 - Xác định sự kiện "ngủ gật ngắn"
FR11: Epic 2 - Kích hoạt cảnh báo sớm, nhẹ nhàng
FR12: Epic 2 - Kích hoạt cảnh báo khẩn cấp, rõ ràng

FR10.1: Epic 3 - Phát hiện sử dụng điện thoại
FR10.2: Epic 3 - Phát hiện uống nước
FR10.3: Epic 3 - Phát hiện hút thuốc
FR10.4: Epic 3 - Phát hiện hành vi ngáp (hoạt động)
FR10.5: Epic 3 - Phát hiện tay không đặt trên vô lăng
FR10.6: Epic 3 - Phát hiện tay vươn ra ngoài cửa sổ
FR10.7: Epic 3 - Phát hiện nhìn vào thiết bị định vị

FR13: Epic 4 - Ghi lại chi tiết mọi sự kiện cảnh báo
FR14: Epic 4 - Lưu trữ hình ảnh bằng chứng
FR15: Epic 4 - Truy cập và xem lại các tệp log
FR16: Epic 4 - Xem lại các hình ảnh bằng chứng đã lưu

FR17: Epic 5 - Tải và áp dụng thông số cấu hình
FR18: Epic 5 - Điều chỉnh độ nhạy các thuật toán

## Epic List

### Epic 1: Thiết lập Hệ thống lõi và Nhận thức Hình ảnh
Hệ thống có khả năng khởi tạo, thu nhận và xử lý video, thực hiện các phát hiện hình ảnh nền tảng (khuôn mặt, mắt, đầu).
**FRs covered:** FR1, FR2, FR3, FR4, FR5, FR6, FR7.

### Epic 2: Phân tích Trạng thái & Cảnh báo cho Tài xế
Hệ thống phân tích các đặc điểm đã nhận dạng để xác định trạng thái (buồn ngủ, mất tập trung) và đưa ra các cảnh báo tương ứng (bao gồm cả các cảnh báo cho hành vi nguy hiểm).
**FRs covered:** FR8, FR9, FR10, FR11, FR12.

### Epic 3: Nhận dạng các Hành vi Nguy hiểm Cụ thể
Sử dụng mô hình AI để phát hiện 7 hành vi nguy hiểm cụ thể đã được định nghĩa (sử dụng điện thoại, hút thuốc, v.v.).
**FRs covered:** FR10.1, FR10.2, FR10.3, FR10.4, FR10.5, FR10.6, FR10.7.

### Epic 4: Ghi nhận Dữ liệu và Quản lý Bằng chứng
Hệ thống ghi lại tất cả các sự kiện, cảnh báo vào cơ sở dữ liệu và lưu trữ hình ảnh làm bằng chứng khi có cảnh báo khẩn cấp.
**FRs covered:** FR13, FR14, FR15, FR16.

### Epic 5: Cấu hình và Giao diện Người dùng
Hệ thống cung cấp giao diện cho phép người dùng điều chỉnh các ngưỡng của hệ thống, xem trạng thái hoạt động trực tiếp và quản lý các tùy chọn hệ thống.
**FRs covered:** FR17, FR18.

<!-- Repeat for each epic in epics_list (N = 1, 2, 3...) -->

## Epic 1: Thiết lập Hệ thống lõi và Nhận thức Hình ảnh
Hệ thống có khả năng khởi tạo, thu nhận và xử lý video, thực hiện các phát hiện hình ảnh nền tảng (khuôn mặt, mắt, đầu).
**FRs covered:** FR1, FR2, FR3, FR4, FR5, FR6, FR7.

### Story 1.1: Khởi tạo và Thu nhận Video từ Camera IR

As a **Hệ thống DMS**,
I want **khởi tạo và thu nhận liên tục luồng video từ camera hồng ngoại**,
So that **tôi có dữ liệu đầu vào cần thiết để bắt đầu phân tích trạng thái tài xế**.

**Acceptance Criteria:**

**Given** hệ thống được khởi động
**When** camera hồng ngoại được kết nối và hoạt động
**Then** hệ thống PHẢI thu nhận được luồng video ổn định ở độ phân giải và tốc độ khung hình yêu cầu (ví dụ: 640x480, 30FPS - NFR1).
**And** nếu camera không khả dụng, hệ thống PHẢI hiển thị cảnh báo lỗi và cố gắng khôi phục kết nối (NFR5).

### Story 1.2: Xử lý trước Khung hình Video

As a **Hệ thống DMS**,
I want **xử lý trước các khung hình video thô để chuẩn bị cho việc phát hiện**,
So that **các module phát hiện có thể hoạt động hiệu quả với đầu vào tối ưu**.

**Acceptance Criteria:**

**Given** một khung hình video thô đã được thu nhận (từ Story 1.1)
**When** khung hình được đưa vào module xử lý trước
**Then** hệ thống PHẢI chuyển đổi khung hình sang ảnh xám.
**And** hệ thống PHẢI điều chỉnh độ tương phản (ví dụ: bằng CLAHE).
**And** khung hình đã xử lý PHẢI sẵn sàng để chuyển đến module phát hiện.

### Story 1.3: Phát hiện và Theo dõi Khuôn mặt Tài xế

As a **Hệ thống DMS**,
I want **phát hiện và theo dõi khuôn mặt của tài xế trong luồng video theo thời gian thực**,
So that **vị trí khuôn mặt và các điểm mốc chính có thể được sử dụng cho các phân tích tiếp theo**.

**Acceptance Criteria:**

**Given** một khung hình video đã xử lý (từ Story 1.2)
**When** module phát hiện khuôn mặt xử lý khung hình
**Then** hệ thống PHẢI phát hiện được khuôn mặt của tài xế và trả về hộp giới hạn (bounding box).
**And** hệ thống PHẢI trích xuất được 68 điểm mốc trên khuôn mặt (facial landmarks).
**And** nếu không phát hiện được khuôn mặt trong một khoảng thời gian nhất định, hệ thống PHẢI thông báo tình trạng "Không phát hiện tài xế".

### Story 1.4: Ước tính Tư thế Đầu Tài xế

As a **Hệ thống DMS**,
I want **ước tính tư thế đầu (pitch, yaw, roll) của tài xế từ các điểm mốc khuôn mặt**,
So that **tôi có thể đánh giá hướng và góc quay đầu của tài xế**.

**Acceptance Criteria:**

**Given** các điểm mốc khuôn mặt đã được trích xuất (từ Story 1.3)
**When** module ước tính tư thế đầu xử lý dữ liệu điểm mốc
**Then** hệ thống PHẢI tính toán được các góc pitch (gật/ngửa), yaw (quay trái/phải) và roll (nghiêng) của đầu tài xế theo độ.
**And** các góc ước tính PHẢI có độ chính xác chấp nhận được (ví dụ: +/- 5 độ).

### Story 1.5: Theo dõi Trạng thái Mắt và Phát hiện Ngáp cơ bản

As a **Hệ thống DMS**,
I want **theo dõi trạng thái mở/đóng của mắt và phát hiện hành vi ngáp**,
So that **tôi có thể xác định các dấu hiệu ban đầu của buồn ngủ**.

**Acceptance Criteria:**

**Given** các điểm mốc khuôn mặt đã được trích xuất (từ Story 1.3)
**When** module theo dõi mắt và miệng xử lý dữ liệu điểm mốc
**Then** hệ thống PHẢI tính toán được tỷ lệ EAR (Eye Aspect Ratio) cho cả hai mắt.
**And** hệ thống PHẢI xác định được trạng thái mắt đang mở hay đóng dựa trên ngưỡng EAR.
**And** hệ thống PHẢI phát hiện được hành vi ngáp của tài xế thông qua các điểm mốc miệng (FR6).

### Story 1.6: Xác định Hướng nhìn của Tài xế

As a **Hệ thống DMS**,
I want **xác định hướng nhìn (gaze direction) của tài xế**,
So that **tôi có thể phát hiện việc tài xế không tập trung nhìn vào đường**.

**Acceptance Criteria:**

**Given** các điểm mốc mắt và vị trí đầu (từ Story 1.3 và 1.4)
**When** module xác định hướng nhìn xử lý dữ liệu
**Then** hệ thống PHẢI ước tính được vector hướng nhìn của tài xế.
**And** hệ thống PHẢI ánh xạ hướng nhìn này vào các vùng cụ thể (ví dụ: nhìn thẳng, nhìn sang gương, nhìn xuống bảng điều khiển).


## Epic 5: Cấu hình và Giao diện Người dùng
Hệ thống cung cấp giao diện cho phép người dùng điều chỉnh các ngưỡng của hệ thống, xem trạng thái hoạt động trực tiếp và quản lý các tùy chọn hệ thống.
**FRs covered:** FR17, FR18.

### Story 5.1: Xây dựng Giao diện Người dùng Chính và Hiển thị Video

As a **Người dùng**,
I want **một giao diện chính hiển thị trực tiếp luồng video từ camera**,
So that **tôi có thể theo dõi trực quan tình hình bên trong xe và xác nhận camera đang hoạt động**.

**Acceptance Criteria:**

**Given** hệ thống DMS đang hoạt động
**When** giao diện người dùng chính được khởi chạy
**Then** giao diện PHẢI hiển thị một bảng điều khiển chính với luồng video trực tiếp từ camera hồng ngoại (UX: Live Monitoring Screen).
**And** giao diện PHẢI hiển thị hình ảnh video ở độ phân giải chấp nhận được (UX: 640x480).

### Story 5.2: Hiển thị Bảng điều khiển Trạng thái Thời gian thực

As a **Người dùng**,
I want **một bảng điều khiển hiển thị các chỉ số và trạng thái quan trọng của tài xế theo thời gian thực**,
So that **tôi có thể nhanh chóng nắm bắt tình trạng buồn ngủ và mất tập trung của tài xế**.

**Acceptance Criteria:**

**Given** giao diện người dùng chính đang hiển thị (từ Story 5.1)
**When** hệ thống phân tích trạng thái tài xế (từ Epic 2, 3) tạo ra dữ liệu
**Then** bảng điều khiển PHẢI hiển thị các chỉ số như EAR (Eye Aspect Ratio), mức độ buồn ngủ, và điểm chú ý (UX: Metrics Panel).
**And** các chỉ số này PHẢI được cập nhật theo thời gian thực (UX: Component 4, NFR1).
**And** trạng thái tổng thể của tài xế PHẢI được hiển thị rõ ràng (ví dụ: "ALERT", "DROWSY", "DISTRACTED") (UX: Component 1).

### Story 5.3: Triển khai Giao diện Quản lý Cấu hình

As a **Người dùng có thẩm quyền**,
I want **một giao diện để điều chỉnh các thông số cấu hình và ngưỡng phát hiện**,
So that **tôi có thể tùy chỉnh hệ thống DMS cho phù hợp với các điều kiện lái xe hoặc tài xế cụ thể**.

**Acceptance Criteria:**

**Given** người dùng có quyền truy cập vào màn hình cài đặt (UX: Settings Screen)
**When** người dùng thay đổi các giá trị ngưỡng (ví dụ: ngưỡng EAR, ngưỡng cảnh báo) (FR17, FR18)
**Then** hệ thống PHẢI cho phép điều chỉnh các ngưỡng này thông qua các điều khiển trực quan (ví dụ: thanh trượt, hộp nhập liệu) (UX: Screen 5: Settings Screen).
**And** sau khi lưu, các thay đổi PHẢI được áp dụng ngay lập tức hoặc sau khi khởi động lại hệ thống, tùy thuộc vào loại tham số.
**And** các thay đổi cấu hình PHẢI được lưu trữ ổn định (Arch: config.yaml).

### Story 5.4: Tích hợp Hệ thống Cảnh báo vào Giao diện

As a **Người dùng**,
I want **các cảnh báo được hiển thị rõ ràng và có phân cấp trên giao diện và thông qua phần cứng**,
So that **tôi nhận biết được mức độ nghiêm trọng của tình huống và hành động phù hợp**.

**Acceptance Criteria:**

**Given** hệ thống phân tích xác định cần phải kích hoạt cảnh báo (từ Epic 2, 3)
**When** một cảnh báo được kích hoạt
**Then** giao diện PHẢI hiển thị một cảnh báo trực quan (ví dụ: banner đỏ/vàng) tùy theo mức độ nghiêm trọng (UX: Alert Banner, Alert System UI).
**And** hệ thống PHẢI phát ra âm thanh cảnh báo phù hợp với mức độ nghiêm trọng (UX: Audio Alerts).
**And** đèn LED phần cứng PHẢI nhấp nháy hoặc đổi màu theo mức độ cảnh báo (UX: LED Indicators).
**And** các cảnh báo PHẢI có cơ chế quản lý ưu tiên và tránh lặp lại liên tục để không gây phiền nhiễu (Arch: AlertManager, UX: Alert Cooldown Logic).

<!-- End story repeat -->

