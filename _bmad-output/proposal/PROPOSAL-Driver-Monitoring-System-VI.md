# ĐỀ XUẤT DỰ ÁN
## Hệ Thống Giám Sát Tài Xế Sử Dụng Thị Giác Máy Tính & AI

---

**Tên Sinh Viên:** Hung Thanh  
**Cố Vấn:** [Tên Cố Vấn]  
**Cơ Sở Giáo Dục:** [Tên Đại Học]  
**Khoa:** [Tên Khoa]  
**Ngày:** 4 Tháng 3, 2026  
**Loại Dự Án:** Luận Văn Tốt Nghiệp / Đề Tài Khóa Luận  

---

## MỤC LỤC

1. [Phát Biểu Vấn Đề](#1-phát-biểu-vấn-đề)
2. [Giải Pháp Đề Xuất](#2-giải-pháp-đề-xuất)
3. [Mục Tiêu Dự Án](#3-mục-tiêu-dự-án)
4. [Phạm Vi Dự Án](#4-phạm-vi-dự-án)
5. [Tính Năng Hệ Thống](#5-tính-năng-hệ-thống)
6. [Công Nghệ Sử Dụng](#6-công-nghệ-sử-dụng)
7. [Kết Quả Dự Kiến](#7-kết-quả-dự-kiến)
8. [Lịch Trình Dự Án](#8-lịch-trình-dự-án)
9. [Tiêu Chí Thành Công](#9-tiêu-chí-thành-công)
10. [Tài Liệu Tham Khảo](#10-tài-liệu-tham-khảo)

---

## 1. PHÁT BIỂU VẤN ĐỀ

### 1.1 Nền Tảng

Tai nạn giao thông đường bộ là một trong những nguyên nhân hàng đầu gây tử vong và thương tích trên toàn thế giới. Theo Tổ Chức Y Tế Thế Giới (WHO), khoảng 1,35 triệu người chết mỗi năm do các tai nạn giao thông đường bộ, với thêm 20-50 triệu người bị thương không tử vong. Một phần lớn các tai nạn này có thể được quy cho trực tiếp cho các yếu tố con người, đặc biệt:

- **Tài xế ngủ gật và mệt mỏi**: Các nghiên cứu cho thấy 20-30% tai nạn giao thông do lái xe khi ngủ gật, nơi tài xế ngủ quên tay lái hoặc bị ngủ gục
- **Tài xế bị phân tán chú ý**: Rút chú ý khỏi đường (ví dụ: sử dụng điện thoại di động, ăn, điều chỉnh các điều khiển) góp phần vào khoảng 25% tất cả tai nạn giao thông
- **Hành vi lái xe nguy hiểm**: Các hoạt động như hút thuốc trong khi lái xe, vươn tay lấy vật thể, hoặc lái xe với tay không được đặt trên bánh lái tăng rủi ro tai nạn đáng kể

### 1.2 Tác Động Của Vấn Đề

Hậu quả của sự bất cẩn và hành vi không an toàn của tài xế là nghiêm trọng:

**Tác Động Về Con Người:**
- Mất mạng và tàn tật vĩnh viễn
- Sang chấn tâm lý cho nạn nhân và gia đình
- Giảm chất lượng cuộc sống cho những người sống sót sau tai nạn

**Tác Động Kinh Tế:**
- Chi phí điều trị y tế lên tới hàng tỷ đô mỗi năm
- Chi phí giải quyết yêu cầu bảo hiểm
- Tổn thất tài sản và hư hỏng xe cộ
- Mất năng suất do thương tích và tử vong

**Tác Động Xã Hội:**
- Mối quan tâm về an toàn công cộng
- Tăng ùn tắc giao thông từ tai nạn
- Áp lực đè nặng trên các dịch vụ ứng cứu khẩn cấp

### 1.3 Những Hạn Chế Hiện Tại

Các giải pháp hiện có có những hạn chế đáng kể:

- **Thực thi thủ công**: Cảnh sát giao thông không thể giám sát tất cả tài xế liên tục
- **Phân tích sau tai nạn**: Camera hành trình chỉ cung cấp bằng chứng sau tai nạn xảy ra
- **Giáo dục tài xế một mình**: Không đủ để ngăn chặn những lúc mất tập trung tạm thời
- **Hệ thống cảnh báo cơ bản**: Giới hạn trong các nhắc nhở về dây an toàn hoặc cảnh báo rời khỏi làn đường, không giám sát hành vi toàn diện của tài xế

### 1.4 Nhu Cầu Giải Pháp

Có nhu cầu cấp bách đối với một hệ thống chủ động, theo thời gian thực có thể:
- Liên tục giám sát trạng thái và hành vi của tài xế
- Phát hiện các dấu hiệu cảnh báo sớm của ngủ gật, bị phân tán chú ý, và các hoạt động nguy hiểm
- Cung cấp cảnh báo tức thời để ngăn chặn tai nạn trước khi xảy ra
- Ghi lại sự kiện để phân tích và cải thiện lái xe

---

## 2. GIẢI PHÁP ĐỀ XUẤT

### 2.1 Tổng Quan Giải Pháp

Dự án này đề xuất phát triển một **Hệ Thống Giám Sát Tài Xế (DMS) Được Hỗ Trợ Bởi AI**, sử dụng các kỹ thuật thị giác máy tính và học máy để liên tục giám sát hành vi tài xế và cung cấp các can thiệp an toàn theo thời gian thực.

**Khái Niệm Cốt Lõi:**  
Một camera hồng ngoại (IR) duy nhất được gắn trên bảng điều khiển xe ghi lại video khuôn mặt của tài xế. Các thuật toán thị giác máy tính nâng cao và các mô hình học sâu phân tích dòng video theo thời gian thực để phát hiện:
- Dấu hiệu ngủ gật (đóng mắt, ngáp, cúi đầu)
- Chỉ số bị phân tán chú ý (hướng nhìn rời khỏi đường, quay đầu kéo dài)
- Hoạt động nguy hiểm (gọi điện thoại, uống nước, hút thuốc, tay không ở bánh lái, v.v.)

Khi phát hiện hành vi rủi ro, hệ thống ngay lập tức kích hoạt cảnh báo âm/hình để cảnh báo tài xế, đồng thời ghi lại sự kiện để phân tích sau chuyến đi.

### 2.2 Cách Thức Hoạt Động

**Quy Trình Làm Việc Của Hệ Thống:**

```
┌─────────────┐
│ Camera IR   │
│ (Ghi Hình   │
│ Khuôn Mặt   │
│ Tài Xế)     │
└──────┬──────┘
       │
       ▼
┌─────────────────────┐
│ Đường Ống Xử Lý     │
│ Thị Giác Máy Tính   │
├─────────────────────┤
│ 1. Phát Hiện Mặt    │
│ 2. Theo Dõi Mắt     │
│ 3. Posture Đầu      │
│ 4. Hướng Nhìn        │
│ 5. CNN Hoạt Động    │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ Mô Hình Phát Hiện AI│
├─────────────────────┤
│ • Điểm Ngủ Gật      │
│ • Mức Độ Phân Tán   │
│ • Lớp Hoạt Động     │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ Công Cụ Quyết Định  │
│ (Logic Cảnh Báo)    │
└──────┬──────────────┘
       │
       ├──► Cảnh Báo Âm Thanh (Loa)
       ├──► Cảnh Báo Hình Ảnh (Bảng Điều Khiển)
       └──► Ghi Lại Sự Kiện (Cơ Sở Dữ Liệu)
```

**Các Bước Xử Lý Chính:**

1. **Phát Hiện & Theo Dõi Mặt**: Phát hiện mặt tài xế bằng mô hình phát hiện mặt dlib hoặc MediaPipe
2. **Trích Xuất Điểm Mốc Khuôn Mặt**: Xác định 68 điểm mốc khuôn mặt để phân tích mắt, miệng, và đầu
3. **Phân Tích Trạng Thái Mắt**: Tính tỷ lệ Eye Aspect Ratio (EAR) để xác định mắt mở hay đóng
4. **Ước Tính Posture Đầu**: Sử dụng thuật toán solvePnP để tính hướng đầu (pitch, yaw, roll)
5. **Ước Tính Hướng Nhìn**: Kết hợp vị trí mắt và posture đầu để xác định tài xế đang nhìn vào đâu
6. **Nhận Dạng Hoạt Động**: Mô hình CNN học sâu phân loại các hoạt động nguy hiểm từ khung hình video
7. **Hợp Nhất Đa Tín Hiệu**: Kết hợp tất cả các tín hiệu phát hiện để đưa ra quyết định cảnh báo mạnh mẽ
8. **Cảnh Báo Theo Thời Gian Thực**: Kích hoạt cảnh báo âm thanh và chỉ báo hình ảnh khi vượt quá ngưỡng

### 2.3 Sáng Tạo & Ưu Điểm

**So với các giải pháp hiện có, hệ thống này cung cấp:**

 **Giám Sát Toàn Diện**: Phát hiện nhiều yếu tố rủi ro (ngủ gật, bị phân tán chú ý, hoạt động) trong một hệ thống  
 **Phòng Chống Theo Thời Gian Thực**: Cung cấp cảnh báo tức thời, không chỉ ghi hình sau tai nạn  
 **Chính Xác Được Hỗ Trợ Bởi AI**: Sử dụng các mô hình học máy được huấn luyện trên các tập dữ liệu đa dạng để phát hiện mạnh mẽ  
 **Khả Năng Nhìn Ban Đêm**: Camera IR hoạt động trong bóng tối hoàn toàn  
 **Bảo Vệ Quyền Riêng Tư**: Tất cả xử lý diễn ra cục bộ trên thiết bị, không truyền đến đám mây  
 **Phần Cứng Giá Rẻ**: Sử dụng camera IR tiêu chuẩn và thiết bị tính toán biên (Jetson Nano/Raspberry Pi)  
 **Thông Tin Chi Tiết Do Dữ Liệu Hướng Dẫn**: Ghi lại các sự kiện để phân tích hành vi tài xế và cải thiện  

---

## 3. MỤC TIÊU DỰ ÁN

### 3.1 Mục Tiêu Chính

**Mục Tiêu 1: Xây Dựng Hệ Thống Giám Sát Tài Xế Hoạt Động Theo Thời Gian Thực**
- Phát triển hệ thống đầu cuối hoàn chỉnh từ đầu vào camera đến đầu ra cảnh báo
- Đạt hiệu suất theo thời gian thực với tối thiểu 15 FPS tốc độ xử lý
- Đảm bảo độ ổn định hệ thống với tỷ lệ lỗi <1% trong hoạt động liên tục

**Mục Tiêu 2: Triển Khai Phát Hiện Ngủ Gật**
- Phát hiện ngủ gật bằng nhiều chỉ báo:
  - Thời gian đóng mắt (Eye Aspect Ratio - EAR)
  - Phân tích tần suất chớp mắt
  - Phát hiện ngáp (Mouth Aspect Ratio - MAR)
  - Tính toán PERCLOS (Phần Trăm Đóng Mắt)
- Độ chính xác phát hiện mục tiêu: >90%
- Độ trễ cảnh báo: <2 giây từ khi phát hiện ngủ gật

**Mục Tiêu 3: Triển Khai Phát Hiện Bị Phân Tán Chú Ý**
- Giám sát sự chú ý của tài xế bằng:
  - Hướng posture đầu (góc pitch, yaw, roll)
  - Hướng nhìn và phân loại vùng
  - Thời gian dành để nhìn rời khỏi đường
- Phân biệt giữa những kiểm tra gương hợp lệ và bị phân tán chú ý
- Độ chính xác phát hiện mục tiêu: >85%

**Mục Tiêu 4: Triển Khai Nhận Dạng Hoạt Động Nguy Hiểm**
- Huấn luyện mô hình học sâu để nhận dạng 7 hoạt động nguy hiểm:
  1. Gọi điện thoại (cầm điện thoại vào tai)
  2. Uống nước (từ chai hoặc cốc)
  3. Hút thuốc (tay cầm thuốc)
  4. Ngáp (chỉ báo ngủ gật)
  5. Tay không ở bánh lái
  6. Tay vươn ra ngoài cửa sổ
  7. Nhìn vào màn hình định hướng/điện thoại
- Độ chính xác mỗi hoạt động mục tiêu: >85%
- Tỷ lệ dương tính giả: <5%

**Mục Tiêu 5: Triển Khai Nhận Dạng Tài Xế**
- Hỗ trợ đăng ký tài xế thông qua nhận dạng khuôn mặt
- Tự động xác định tài xế khi vào xe
- Liên kết tất cả các sự kiện với tài xế cụ thể để phân tích cá nhân hóa

**Mục Tiêu 6: Phát Triển Hệ Thống Cảnh Báo và Ghi Lại**
- Cảnh báo âm thanh theo thời gian thực cho các sự kiện quan trọng
- Bảng điều khiển hình ảnh hiển thị trạng thái tài xế hiện tại
- Ghi lại sự kiện toàn diện vào cơ sở dữ liệu
- Ghi hình video được kích hoạt bởi sự kiện để lấy bằng chứng

### 3.2 Mục Tiêu Phụ

- Hỗ trợ các điều kiện ánh sáng khác nhau (ngày, đêm, hầm) bằng camera IR
- Xử lý các phụ kiện (kính mắt, mặt nạ) mà không giảm đáng kể độ chính xác
- Cung cấp các ngưỡng cảnh báo có thể cấu hình cho các mức độ nhạy cảm khác nhau
- Tạo bảng điều khiển phân tích cho các xu hướng hành vi tài xế
- Đếm số hành khách để theo dõi sự chiếm dụng

### 3.3 Mục Tiêu Học Tập

Là một dự án giáo dục, luận văn này nhằm giới thiệu:
- Ứng dụng các thuật toán thị giác máy tính (phát hiện mặt, trích xuất điểm mốc, ước tính posture)
- Huấn luyện và tối ưu hóa mô hình học sâu
- Thiết kế hệ thống theo thời gian thực và tối ưu hóa hiệu suất
- Thực hành kỹ thuật phần mềm (kiểm soát phiên bản, kiểm tra, tài liệu)
- Kỹ năng giải quyết vấn đề trong việc xử lý các thách thức thực tế (biến đổi ánh sáng, che khuất, v.v.)

---

## 4. PHẠM VI DỰ ÁN

### 4.1 Trong Phạm Vi (Những Gì SẼ Được Bao Gồm)

#### **Các Tính Năng Phát Hiện Cốt Lõi**
 **Mô Đun Phát Hiện Ngủ Gật**
- Tính toán và giám sát Eye Aspect Ratio (EAR)
- Phân tích tần suất chớp mắt
- Phát hiện ngáp thông qua Mouth Aspect Ratio (MAR)
- Phát hiện vi giấc ngủ (đóng mắt ngắn 0,5-3 giây)
- Tính toán PERCLOS (Phần Trăm Đóng Mắt)

 **Mô Đun Phát Hiện Bị Phân Tán Chú Ý**
- Ước tính posture đầu (góc pitch, yaw, roll)
- Phát hiện quay đầu (nhìn trái, phải, xuống)
- Ước tính hướng nhìn mắt
- Phân loại vùng nhìn (đường, bảng điều khiển, gương, hành khách, điện thoại)
- Điểm chú ý kết hợp đầu + mắt

 **Mô Đun Nhận Dạng Hoạt Động Nguy Hiểm**
- 7 hoạt động được phát hiện thông qua mô hình CNN:
  1. Gọi điện thoại
  2. Uống nước
  3. Hút thuốc
  4. Ngáp
  5. Tay không ở bánh lái
  6. Tay vươn ra ngoài cửa sổ
  7. Nhìn vào hướng dẫn/điện thoại
- Huấn luyện và đánh giá mô hình CNN hoạt động

 **Mô Đun Nhận Dạng Tài Xế**
- Quy trình đăng ký khuôn mặt (chụp và mã hóa)
- Nhận dạng khuôn mặt để xác định tài xế
- Hỗ trợ đa tài xế cho mỗi xe
- Liên kết phiên sử dụng với tài xế được xác định

 **Hệ Thống Cảnh Báo**
- Cảnh báo âm thanh theo thời gian thực (âm thanh bíp, cảnh báo bằng giọng nói)
- Cảnh báo hình ảnh trên bảng điều khiển
- Quản lý ưu tiên cảnh báo (ngăn chặn spam cảnh báo)

 **Ghi Lại Dữ Liệu & Ghi Lại Video**
- Ghi lại sự kiện vào cơ sở dữ liệu cục bộ (SQLite)
- Ghi lại video được kích hoạt bởi sự kiện (±30 giây xung quanh sự kiện)
- Theo dõi phiên lái xe (thời gian bắt đầu/kết thúc, thời lượng chuyến đi)

 **Giao Diện Người Dùng**
- Bảng điều khiển giám sát trực tiếp hiển thị:
  - Nguồn video camera với các lớp phát hiện
  - Trạng thái tài xế hiện tại (ngủ gật, bị phân tán, hoạt động)
  - Chỉ báo sức khỏe hệ thống (FPS, trạng thái camera)
- Xem dữ liệu lịch sử (các chuyến đi quá khứ, số lượng sự kiện)

 **Giám Sát Sức Khỏe Hệ Thống**
- Kiểm tra kết nối camera IR
- Cảnh báo lỗi phát hiện mặt
- Giám sát FPS và cảnh báo hiệu suất
- Phát hiện ánh sáng yếu

 **Giám Sát Hành Khách**
- Đếm hành khách (ghế trước và ghế sau)
- Theo dõi sự chiếm dụng trên mỗi chuyến đi

#### **Công Nghệ & Cơ Sở Dữ Liệu Phần Cứng**
 Camera IR (khả năng nhìn ban đêm)  
 Thiết bị tính toán biên (Jetson Nano hoặc Raspberry Pi 4)  
 Phần mềm dựa trên Python (OpenCV, dlib, TensorFlow/PyTorch)  
 Cơ sở dữ liệu cục bộ (SQLite)  
 Giao diện web/máy tính để bàn  

#### **Kiểm Tra & Tài Liệu**
 Kế hoạch kiểm tra với các kịch bản kiểm tra được định nghĩa  
 Các trường hợp kiểm tra cho tất cả các mô đun phát hiện  
 Kiểm tra hiệu suất (độ chính xác, FPS, độ trễ)  
 Hướng dẫn người dùng  
 Tài liệu kỹ thuật  
 Mã nguồn có tài liệu nội dòng  

### 4.2 Ngoài Phạm Vi (Những Gì KHÔNG Được Bao Gồm)

 **Phát hiện dây an toàn** - Loại bỏ do ràng buộc phạm vi  
 **Phân tích biểu hiện khuôn mặt** (ngoài ngáp) - Ưu tiên thấp, phức tạp cao  
 **Ứng dụng di động** - Chỉ giao diện máy tính để bàn/web  
 **Đồng bộ hóa đám mây** - Chỉ lưu trữ cục bộ  
 **Máy chủ quản lý hạm đội** - Tập trung vào xe đơn  
 **Cập nhật phần mềm qua không khí (OTA)** - Cập nhật thủ công chỉ  
 **Tích hợp CAN bus** - Khởi động/dừng hệ thống thủ công  
 **Hỗ trợ đa camera** - Chỉ camera IR duy nhất  
 **Tính năng lái autonomous** - Chỉ giám sát, không kiểm soát xe  
 **Phân tích sinh trắc học nâng cao** - Tập trung vào hành vi, không giám sát sức khỏe  
 **Truyền phát trực tiếp đám mây theo thời gian thực** - Mối quan tâm quyền riêng tư và băng thông  

### 4.3 Giả Định & Hạn Chế

**Giả Định:**
- Tài xế duy nhất cho mỗi chuyến đi (hỗ trợ đa tài xế cho các chuyến đi khác nhau)
- Khuôn mặt tài xế nhìn thấy camera (không bị che khuất)
- Camera IR được đặt trên bảng điều khiển hướng về tài xế
- Hệ thống có đủ sức mạnh tính toán (Jetson Nano hoặc tương đương)
- Có sẵn tập dữ liệu huấn luyện để nhận dạng hoạt động

**Hạn Chế:**
- Lịch phát triển: 10-20 tuần
- Ngân sách: Giới hạn ở các tài nguyên giáo dục
- Phần cứng: Camera IR và thiết bị tính toán biên tiêu chuẩn
- Kích thước tập dữ liệu: Có thể cần thu thập dữ liệu huấn luyện tùy chỉnh cho các hoạt động
- Sức mạnh xử lý: Phải duy trì >15 FPS trên phần cứng mục tiêu

### 4.4 Các Quyết Định Trì Hoãn (Sẽ Quyết Định Trong Quá Trình Phát Triển)

 **Chiến Lược Xác Thực**: Nhận diện khởi động vs. giám sát liên tục  
 **Thời Lượng Lưu Trữ Video**: Chính sách lưu giữ 7 ngày vs. 30 ngày  
 **Mức Độ Cảnh Báo**: Bảo thủ (ít dương tính giả hơn) vs. tích cực (nhạy cảm cao hơn)  
 **Công Nghệ Bảng Điều Khiển**: GUI OpenCV vs. bảng điều khiển dựa trên web (Flask/React)  

---

## 5. TÍNH NĂNG HỆ THỐNG

### 5.1 Danh Mục Tính Năng (13 Khu Vực Chức Năng)

Dựa trên phân tích brainstorming toàn diện, hệ thống bao gồm **45 Mục Phát Triển Sản Phẩm (PBIs)** được tổ chức thành 13 danh mục:

#### **Danh Mục 1: Phát Hiện Mặt & Mắt Cốt Lõi (5 tính năng)**
- PBI-001: Phát Hiện & Theo Dõi Mặt
- PBI-002: Phát Hiện Vùng Mắt
- PBI-003: Phát Hiện Mắt Mở (EAR)
- PBI-004: Giám Sát Tần Suất Chớp Mắt
- PBI-005: Theo Dõi Vị Trí Mắt

#### **Danh Mục 2: Posture & Hướng Đầu (3 tính năng)**
- PBI-006: Ước Tính Posture Đầu
- PBI-007: Theo Dõi Vị Trí Đầu
- PBI-008: Phân Loại Vùng Đầu

#### **Danh Mục 3: Theo Dõi Hướng Nhìn Mắt (3 tính năng)**
- PBI-009: Ước Tính Hướng Nhìn
- PBI-010: Phân Loại Vùng Nhìn
- PBI-011: Phát Hiện & Theo Dõi Học Sinh

#### **Danh Mục 4: Phát Hiện Ngủ Gật (4 tính năng)**
- PBI-012: Phát Hiện Ngủ Gật (dựa trên EAR)
- PBI-013: Phát Hiện Ngáp
- PBI-014: Phát Hiện Vi Giấc Ngủ
- PBI-015: Tính Toán PERCLOS

#### **Danh Mục 5: Phát Hiện Bị Phân Tán Chú Ý (3 tính năng)**
- PBI-016: Phân Tán Chú Ý Do Quay Đầu
- PBI-017: Phát Hiện Nhìn Rời Khỏi Đường
- PBI-018: Tính Toán Điểm Chú Ý

#### **Danh Mục 6: Nhận Dạng Hoạt Động Nguy Hiểm (8 tính năng)**
- PBI-019: Phát Hiện Gọi Điện Thoại
- PBI-020: Phát Hiện Uống Nước
- PBI-021: Phát Hiện Hút Thuốc
- PBI-022: Phát Hiện Hoạt Động Ngáp
- PBI-023: Phát Hiện Tay Không Ở Bánh Lái
- PBI-024: Phát Hiện Tay Vươn Ra Ngoài Cửa Sổ
- PBI-025: Phát Hiện Nhìn Vào Hướng Dẫn
- PBI-026: Huấn Luyện Mô Hình CNN Hoạt Động

#### **Danh Mục 7: Đăng Ký & Nhận Dạng Tài Xế (3 tính năng)**
- PBI-027: Đăng Ký Khuôn Mặt Tài Xế
- PBI-028: Nhận Dạng Tài Xế
- PBI-029: Quản Lý Đa Tài Xế

#### **Danh Mục 8: Giám Sát Hành Khách (2 tính năng)**
- PBI-030: Đếm Hành Khách
- PBI-031: Phát Hiện Khuôn Mặt Hành Khách

#### **Danh Mục 9: Phụ Kiện An Toàn (2 tính năng)**
- PBI-032: Phát Hiện Kính Mắt
- PBI-033: Phát Hiện Mặt Nạ

#### **Danh Mục 10: Quản Lý Sức Khỏe & Camera Hệ Thống (4 tính năng)**
- PBI-034: Kiểm Tra Sức Khỏe Camera IR
- PBI-035: Phát Hiện Ánh Sáng Yếu
- PBI-036: Phát Hiện Che Khuất Khuôn Mặt
- PBI-037: Giám Sát FPS Hệ Thống

#### **Danh Mục 11: Hệ Thống Cảnh Báo (3 tính năng)**
- PBI-038: Cảnh Báo Âm Thanh Theo Thời Gian Thực
- PBI-039: Cảnh Báo Hình Ảnh (LED/Bảng Điều Khiển)
- PBI-040: Quản Lý Ưu Tiên Cảnh Báo

#### **Danh Mục 12: Ghi Lại Dữ Liệu & Ghi Video (3 tính năng)**
- PBI-041: Ghi Lại Sự Kiện
- PBI-042: Ghi Lại Video (Kích Hoạt Bởi Sự Kiện)
- PBI-043: Theo Dõi Phiên

#### **Danh Mục 13: Bảng Điều Khiển & Giao Diện Người Dùng (2 tính năng)**
- PBI-044: Bảng Điều Khiển Giám Sát Trực Tiếp
- PBI-045: Bảng Điều Khiển Phân Tích Lịch Sử

### 5.2 Phân Loại Ưu Tiên (Phương Pháp MoSCoW)

**PHẢI CÓ (24 tính năng)** - MVP cốt lõi để tốt nghiệp luận văn
- Tất cả phát hiện mặt, mắt, đầu, nhìn (PBI-001 đến PBI-010, không bao gồm PBI-011)
- Tất cả phát hiện ngủ gật (PBI-012 đến PBI-014)
- Tất cả phát hiện bị phân tán chú ý (PBI-016, PBI-017)
- Tất cả 7 hoạt động nguy hiểm + huấn luyện mô hình (PBI-019 đến PBI-026)
- Sức khỏe camera + giám sát FPS (PBI-034, PBI-037)
- Cảnh báo âm thanh (PBI-038)
- Ghi lại sự kiện (PBI-041)
- Bảng điều khiển trực tiếp (PBI-044)

**NÊN CÓ (17 tính năng)** - Quan trọng nhưng không quan trọng
- Tính toán PERCLOS (PBI-015)
- Điểm chú ý (PBI-018)
- Đăng ký tài xế + nhận dạng (PBI-027, PBI-028, PBI-029)
- Đếm hành khách (PBI-030)
- Phát hiện kính mắt (PBI-032)
- Phát hiện ánh sáng yếu + che khuất (PBI-035, PBI-036)
- Cảnh báo hình ảnh + quản lý ưu tiên (PBI-039, PBI-040)
- Ghi lại video + theo dõi phiên (PBI-042, PBI-043)

**CÓ THỂ CÓ (4 tính năng)** - Tốt là có nếu còn thời gian
- Phát hiện học sinh (PBI-011)
- Phát hiện khuôn mặt hành khách (PBI-031)
- Phát hiện mặt nạ (PBI-033)
- Bảng điều khiển phân tích lịch sử (PBI-045)

---

## 6. CÔNG NGHỆ SỬ DỤNG

### 6.1 Các Thành Phần Phần Cứng

| Thành Phần | Đặc Tả | Mục Đích | Chi Phí Ước Tính |
|-----------|-------|---------|-----------------|
| **Camera IR** | 1080p, 60fps, hồng ngoại ban đêm, giao diện USB | Thu nhập video khuôn mặt tài xế trong mọi điều kiện ánh sáng | $30-50 |
| **Thiết Bị Tính Toán** | Jetson Nano (4GB) HOẶC Raspberry Pi 4 (8GB) | Chạy mô hình AI và đường ống xử lý | $100-150 |
| **Loa Âm Thanh** | Loa USB hoặc jack 3,5mm | Phát cảnh báo âm thanh | $10-20 |
| **Tùy Chọn: Chỉ Báo LED** | Dải LED RGB được kiểm soát GPIO | Chỉ báo cảnh báo trực quan | $5-10 |
| **Tùy Chọn: Màn Hình** | Màn hình cảm ứng HDMI 7 inch | Giao diện bảng điều khiển | $50-80 |
| **Bộ Nhớ** | Thẻ microSD 128GB+ hoặc SSD | Lưu trữ mô hình, cơ sở dữ liệu, video clip | $20-40 |

**Tổng Ngân Sách Phần Cứng: ~$200-300**

### 6.2 Công Nghệ Phần Mềm

#### **Ngôn Ngữ Lập Trình**
- **Python 3.8+**: Ngôn ngữ phát triển chính cho CV và ML

#### **Thư Viện Thị Giác Máy Tính**
- **OpenCV 4.5+**: Xử lý hình ảnh cốt lõi, giao diện camera, lớp vẽ
- **dlib 19.22+**: Phát hiện điểm mốc khuôn mặt (mô hình 68 điểm), mã hóa nhận dạng khuôn mặt
- **MediaPipe (tùy chọn)**: Phát hiện lưới mặt thay thế (468 điểm mốc)

#### **Khung Công Việc Học Sâu**
- **TensorFlow 2.x** HOẶC **PyTorch 1.10+**: Huấn luyện và suy luận CNN nhận dạng hoạt động
- **Keras**: API cấp cao để xây dựng mô hình
- **MobileNetV2** hoặc **EfficientNet**: Kiến trúc CNN nhẹ để triển khai biên

#### **Mô Hình Học Máy**
- **Phát Hiện Mặt**: Bộ Phát Hiện HOG dlib HOẶC MTCNN HOẶC Phát Hiện Mặt MediaPipe
- **Nhận Dạng Khuôn Mặt**: Mã hóa mặt dlib (vector 128D) HOẶC nhúng FaceNet
- **Phân Loại Hoạt Động**: MobileNetV2 CNN được huấn luyện tùy chỉnh (7 lớp)

#### **Cơ Sở Dữ Liệu**
- **SQLite**: Cơ sở dữ liệu nhúng nhẹ để lưu trữ sự kiện cục bộ
- **Lược Đồ**: Bảng Tài Xế, Bảng Phiên, Bảng Sự Kiện, Bảng Siêu Dữ Liệu Video

#### **Giao Diện Người Dùng**
- **Tùy Chọn A (Nhẹ)**: Cửa sổ OpenCV HighGUI để hiển thị bảng điều khiển
- **Tùy Chọn B (Nâng Cao)**: Bảng điều khiển dựa trên web Flask + React.js
- **pygame** hoặc **pydub**: Phát cảnh báo âm thanh

#### **Công Cụ Phát Triển**
- **Git/GitHub**: Kiểm soát phiên bản và kho lưu trữ mã
- **Jupyter Notebook**: Thử nghiệm huấn luyện mô hình và phân tích dữ liệu
- **pytest**: Khung kiểm tra dùng
- **Black + flake8**: Định dạng mã và kiểm tra

#### **Triển Khai & Hệ Thống**
- **Linux (Ubuntu 20.04 hoặc Jetson Linux)**: Hệ điều hành cho thiết bị biên
- **systemd**: Dịch vụ tự khởi động khi khởi động (tùy chọn)
- **FFmpeg**: Mã hóa video cho ghi lại sự kiện

### 6.3 Các Mô Hình & Tập Dữ Liệu Được Huấn Luyện Trước

**Mô Hình Sử Dụng Được Huấn Luyện Trước:**
- Mô hình dlib shape predictor 68 điểm mốc khuôn mặt
- Mô hình nhận dạng khuôn mặt dlib ResNet
- (Tùy chọn) MediaPipe Face Mesh

**Tập Dữ Liệu Để Huấn Luyện Nhận Dạng Hoạt Động:**
- **Sưu tập tập dữ liệu tùy chỉnh**: 300+ mẫu mỗi hoạt động (7 hoạt động = 2100+ hình ảnh)
- **Tăng dữ liệu**: Xoay, độ sáng, mờ để tăng kích thước tập dữ liệu
- **Tập dữ liệu công khai (nếu có)**: Tập dữ liệu bị phân tán chú ý của tài xế (ví dụ: Tập dữ liệu State Farm)

---

## 7. KẾT QUẢ DỰ KIẾN

### 7.1 Các Sản Phẩm Giao Hàng

#### **Sản Phẩm Giao Hàng Chính (Để Gửi Luận Văn)**

1. **Hệ Thống Phần Mềm Hoạt Động Được**
   - Kho lưu trữ mã nguồn hoàn chỉnh trên GitHub
   - Kịch bản cài đặt và thiết lập
   - Tệp cấu hình để điều chỉnh ngưỡng

2. **Mô Hình AI Được Huấn Luyện**
   - Tệp mô hình CNN nhận dạng hoạt động (.h5 hoặc .pth)
   - Notebook huấn luyện mô hình với siêu tham số
   - Báo cáo đánh giá mô hình (độ chính xác, ma trận nhầm lẫn, độ chính xác/thu hồi)

3. **Tài Liệu Hệ Thống**
   - Tài liệu kỹ thuật (kiến trúc, API, lược đồ cơ sở dữ liệu)
   - Hướng dẫn người dùng có hướng dẫn cài đặt và sử dụng
   - Tài liệu mã (docstring, bình luận nội dòng)

4. **Artifact Kiểm Tra**
   - Tài liệu kế hoạch kiểm tra
   - Các trường hợp kiểm tra (tối thiểu 50+ trường hợp bao gồm tất cả mô đun)
   - Kết quả thực hiện kiểm tra và báo cáo lỗi
   - Kết quả điểm chuẩn hiệu suất

5. **Tài Liệu Quản Lý Dự Án**
   - Đề xuất (tài liệu này)
   - Kế hoạch dự án với biểu đồ Gantt
   - Tập hợp sản phẩm (45 PBIs)
   - Câu chuyện người dùng (48 câu chuyện) với tiêu chí chấp nhận
   - Tập hợp sprint (cho mỗi sprint)
   - Biên bản cuộc họp (cuộc họp cố vấn hàng tuần)
   - Tài liệu phản ánh (bài học, thách thức, công việc trong tương lai)

6. **Tài Liệu Thiết Kế**
   - Sơ đồ kiến trúc hệ thống (thành phần, chế độ xem triển khai)
   - Lược đồ cơ sở dữ liệu (sơ đồ ER, định nghĩa bảng)
   - Bản dàn bài UI/UX và bản thiết kế

7. **Tài Liệu Trình Bày**
   - Slide bảo vệ luận văn
   - Video demo (3-5 phút)
   - Áp phích (nếu cần)

#### **Đầu Ra Trình Diễn**

- **Demo trực tiếp** cho thấy phát hiện theo thời gian thực trên tài xế kiểm tra
- **Video clip** về hệ thống phát hiện các kịch bản khác nhau (ngủ gật, bị phân tán, hoạt động)
- **Bảng điều khiển phân tích** hiển thị dữ liệu chuyến đi lịch sử và thống kê sự kiện

### 7.2 Mục Tiêu Hiệu Suất

| Số Liệu | Mục Tiêu | Phương Pháp Đo Lường |
|--------|----------|-------------------|
| **Độ Chính Xác Phát Hiện Ngủ Gật** | >90% | Đánh giá trên tập dữ liệu được gắn nhãn (100+ mẫu) |
| **Độ Chính Xác Nhận Dạng Hoạt Động** | >85% mỗi hoạt động | Tập dữ liệu kiểm tra với 7 lớp hoạt động |
| **Tỷ Lệ Dương Tính Giả (Ngủ Gật)** | <1 cảnh báo mỗi giờ | Kiểm tra lái xe 8 giờ thực tế với tài xế cảnh báo |
| **Tỷ Lệ Dương Tính Giả (Hoạt Động)** | <5% | Phân tích ma trận nhầm lẫn trên tập kiểm tra |
| **Độ Trễ Hệ Thống (Phát Hiện Đến Cảnh Báo)** | <500ms | Ghi nhật ký dấu thời gian và đo lường |
| **Hiệu Suất Theo Thời Gian Thực (FPS)** | >15 FPS | Giám sát tỷ lệ xử lý khung hình |
| **Thời Gian Hoạt Động Hệ Thống** | >99% | Không bị lỗi trong 8 giờ kiểm tra liên tục |
| **Tỷ Lệ Thành Công Phát Hiện Mặt** | >95% | Khi khuôn mặt tài xế có thể nhìn thấy và không bị che khuất |
| **Độ Chính Xác Nhận Dạng Tài Xế** | >95% | Độ chính xác nhận dạng khuôn mặt trên tài xế đăng ký |

### 7.3 Tiêu Chí Thành Công

Dự án sẽ được coi là thành công nếu:

 Tất cả tính năng PHẢI CÓ (24 PBIs) được triển khai và hoạt động  
 Phát hiện ngủ gật đạt >90% độ chính xác  
 Nhận dạng hoạt động đạt >85% độ chính xác mỗi lớp  
 Hệ thống chạy theo thời gian thực >15 FPS trên phần cứng mục tiêu  
 Tỷ lệ dương tính giả được chấp nhận <1 cảnh báo/giờ cho ngủ gật  
 Hệ thống ổn định với tỷ lệ lỗi <1% trong hoạt động kéo dài  
 Tất cả sản phẩm giao hàng (mã, tài liệu, kiểm tra) được hoàn thành và gửi  
 Bảo vệ luận văn thành công với trình diễn hệ thống trực tiếp  

### 7.4 Tác Động & Lợi Ích

**Tác Động An Toàn:**
- Giảm rủi ro tai nạn do ngủ gật, bị phân tán chú ý, và hành vi nguy hiểm
- Cung cấp cảnh báo tức thời để ngăn chặn sự cố trước khi xảy ra
- Tạo nhận thức cho tài xế về hành vi rủi ro của họ

**Tác Động Giáo Dục:**
- Giới thiệu ứng dụng thực tế của thị giác máy tính và học máy
- Giới thiệu phát triển hệ thống toàn diện từ yêu cầu đến triển khai
- Cung cấp kinh nghiệm học tập về giải quyết vấn đề thực tế

**Đóng Góp Nghiên Cứu:**
- Tập dữ liệu toàn diện về hoạt động lái xe nguy hiểm
- Thông tin chi tiết về phát hiện đa phương (kết hợp posture đầu, hướng nhìn, và nhận dạng hoạt động)
- Triển khai nguồn mở cho các nhà nghiên cứu trong tương lai

**Tiềm Năng Thương Mại:**
- Nền tảng cho sản phẩm Hệ Thống Giám Sát Tài Xế thương mại
- Có thể áp dụng cho quản lý hạm đội, chia sẻ xe, ngành vận tải đường
- Có thể mở rộng cho telematics bảo hiểm và ứng dụng tính điểm tài xế

---

## 8. LỊCH TRÌNH DỰ ÁN

### 8.1 Lịch Trình Tổng Thể: 12 Tuần (3 Tháng)

Dự án tuân theo phương pháp **Agile Scrum** với 5 sprints 2 tuần mỗi sprint, trước đó là 2 tuần lập kế hoạch.

### 8.2 Chia Giai Đoạn

#### **Giai Đoạn 1: Khởi Động & Lập Kế Hoạch (Tuần 1-2)**

**Tuần 1:**
- Ôn tập tài liệu về hệ thống giám sát tài xế
- Ôn tập các giải pháp hiện có và các kỳ báo cáo nghiên cứu
- Hoàn thiện phát biểu vấn đề và mục tiêu
- **Sản Phẩm Giao Hàng**: Tài liệu đề xuất (tài liệu này)

**Tuần 2:**
- Tạo kế hoạch dự án chi tiết với biểu đồ Gantt
- Thiết lập môi trường phát triển (Python, OpenCV, TensorFlow)
- Mua phần cứng (camera IR, Jetson Nano/Raspberry Pi)
- Thiết lập kho git và cấu trúc dự án
- **Sản Phẩm Giao Hàng**: Tài liệu Kế Hoạch Dự Án

---

#### **Giai Đoạn 2: Yêu Cầu & Thiết Kế (Tuần 3-5)**

**Tuần 3 (Sprint 1 - Phần 1):**
- Hoàn thiện tập hợp sản phẩm (45 PBIs với ưu tiên MoSCoW)
- Viết câu chuyện người dùng với tiêu chí chấp nhận
- Nghiên cứu các phương pháp phát hiện mặt và trích xuất điểm mốc
- **Sản Phẩm Giao Hàng**: Tài liệu Tập Hợp Sản Phẩm, Câu Chuyện Người Dùng

**Tuần 4 (Sprint 1 - Phần 2):**
- Thiết kế kiến trúc hệ thống (sơ đồ thành phần, luồng dữ liệu)
- Xác định mô đun đường ống xử lý (mặt → mắt → đầu → hướng nhìn → hoạt động)
- Thiết kế lược đồ cơ sở dữ liệu (bảng Tài Xế, Phiên, Sự Kiện)
- **Sản Phẩm Giao Hàng**: Tài liệu Thiết Kế Kiến Trúc

**Tuần 5 (Sprint 2 - Bắt Đầu):**
- Thiết kế bản dàn bài UI/UX cho bảng điều khiển
- Hoàn thiện lược đồ cơ sở dữ liệu với sơ đồ ER
- Viết kế hoạch kiểm tra với kịch bản kiểm tra
- Bắt đầu phát triển: Tích hợp camera, mô đun phát hiện mặt
- **Sản Phẩm Giao Hàng**: Thiết Kế Cơ Sở Dữ Liệu, Bản Dàn Bài Giao Diện, Kế Hoạch Kiểm Tra

---

#### **Giai Đoạn 3: Phát Triển (Tuần 6-9) - 4 Sprints**

**Tuần 6 (Sprint 2 - Hoàn Thành):**
- Triển khai phát hiện mặt và mắt cốt lõi (PBI-001 đến PBI-005)
- Triển khai ước tính posture đầu (PBI-006 đến PBI-008)
- Bảng điều khiển cơ bản hiển thị video camera với lớp phát hiện
- **Mục Tiêu Sprint**: Các mô đun nền tảng hoạt động

**Tuần 7 (Sprint 3 - Bắt Đầu):**
- Triển khai phát hiện ngủ gật (PBI-012 đến PBI-014)
- Triển khai phát hiện bị phân tán chú ý (PBI-016, PBI-017)
- Triển khai hệ thống cảnh báo âm thanh (PBI-038)
- **Mục Tiêu Sprint**: Các tính năng phát hiện an toàn cốt lõi

**Tuần 8 (Sprint 3 - Hoàn Thành & Sprint 4 - Bắt Đầu):**
- Sưu tập và dán nhãn dữ liệu huấn luyện cho 7 hoạt động nguy hiểm
- Huấn luyện Nhận Dạng Hoạt động CNN (PBI-026)
- Triển khai tích hợp phát hiện hoạt động (PBI-019 đến PBI-025)
- **Mục Tiêu Sprint**: Nhận dạng hoạt động hoạt động

**Tuần 9 (Sprint 4 - Hoàn Thành):**
- Triển khai ghi lại sự kiện và tích hợp cơ sở dữ liệu (PBI-041, PBI-043)
- Triển khai đăng ký tài xế và nhận dạng (PBI-027, PBI-028)
- Triển khai giám sát sức khỏe hệ thống (PBI-034, PBI-037)
- Làm sạch mã và tái cấu trúc
- **Mục Tiêu Sprint**: Tất cả tính năng PHẢI CÓ hoàn thành

---

#### **Giai Đoạn 4: Kiểm Tra & Đóng Dự Án (Tuần 10-12)**

**Tuần 10 (Sprint 5 - Bắt Đầu):**
- Viết các trường hợp kiểm tra chi tiết (50+ trường hợp)
- Thực hiện kiểm tra dùng cho mỗi mô đun
- Kiểm tra tích hợp (đường ống toàn diện)
- Điểm chuẩn hiệu suất (độ chính xác, FPS, độ trễ)
- Sửa lỗi

**Tuần 11 (Sprint 5 - Hoàn Thành):**
- Kiểm tra hệ thống với kịch bản lái xe thực tế
- Thu thập số liệu độ chính xác và dữ liệu hiệu suất
- Triển khai tính năng NÊN CÓ nếu có thời gian
- Ôn tập mã cuối cùng và cập nhật tài liệu
- **Sản Phẩm Giao Hàng**: Trường Hợp Kiểm Tra, Kết Quả Kiểm Tra

**Tuần 12 (Tuần Cuối Cùng):**
- Hoàn thành tất cả tài liệu (Hướng Dẫn Người Dùng, Tài Liệu Kỹ Thuật)
- Viết tài liệu phản ánh (bài học, thách thức)
- Tạo video demo và slide trình bày
- Chuẩn bị bảo vệ luận văn
- Gửi cuối cùng
- **Sản Phẩm Giao Hàng**: Phản Ánh, Trình Bày, Gửi Cuối Cùng

---

### 8.3 Tóm Tắt Biểu Đồ Gantt

```
GIAI ĐOẠN/NHIỆM VỤ                | T1 | T2 | T3 | T4 | T5 | T6 | T7 | T8 | T9 |T10 |T11 |T12 |
------------------------------|----|----|----|----|----|----|----|----|----|----|----|----|
GIAI ĐOẠN 1: LẬP KẾ HOẠCH     |████|████|    |    |    |    |    |    |    |    |    |    |
  Đề xuất                      |████|    |    |    |    |    |    |    |    |    |    |    |
  Kế hoạch dự án               |    |████|    |    |    |    |    |    |    |    |    |    |
GIAI ĐOẠN 2: YÊU CẦU          |    |    |████|████|████|    |    |    |    |    |    |    |
  Tập hợp sản phẩm            |    |    |████|    |    |    |    |    |    |    |    |    |
  Câu chuyện người dùng       |    |    |████|████|    |    |    |    |    |    |    |    |
  Thiết kế kiến trúc          |    |    |    |████|    |    |    |    |    |    |    |    |
  Thiết kế cơ sở dữ liệu      |    |    |    |    |████|    |    |    |    |    |    |    |
  Thiết kế giao diện           |    |    |    |    |████|    |    |    |    |    |    |    |
GIAI ĐOẠN 3: PHÁT TRIỂN       |    |    |    |    |████|████|████|████|████|    |    |    |
  Sprint 2: Nền tảng           |    |    |    |    |████|████|    |    |    |    |    |    |
  Sprint 3: Phát hiện cốt lõi  |    |    |    |    |    |    |████|████|    |    |    |    |
  Sprint 4: Hoạt động          |    |    |    |    |    |    |    |████|████|    |    |    |
GIAI ĐOẠN 4: KIỂM TRACE        |    |    |    |    |    |    |    |    |    |████|████|    |
  Trường hợp & thực hiện       |    |    |    |    |    |    |    |    |    |████|████|    |
  Sửa lỗi                      |    |    |    |    |    |    |    |    |    |████|████|    |
ĐÓNG DỰ ÁN                    |    |    |    |    |    |    |    |    |    |    |    |████|
  Tài liệu                     |    |    |    |    |    |    |    |    |    |    |████|████|
  Phản ánh                     |    |    |    |    |    |    |    |    |    |    |    |████|
  Chuẩn bị bảo vệ             |    |    |    |    |    |    |    |    |    |    |    |████|
```

### 8.4 Những Cột Mốc

| Cột Mốc | Thời Hạn | Tiêu Chí |
|---------|----------|----------|
| **M1: Đề Xuất Được Phê Chuẩn** | Cuối Tuần 1 | Phê chuẩn từ cố vấn về phạm vi dự án |
| **M2: Kiến Trúc Hoàn Thành** | Cuối Tuần 4 | Thiết kế hệ thống được hoàn thiện và ôn tập |
| **M3: Nền Tảng Hoạt Động** | Cuối Tuần 6 | Các mô đun phát hiện mặt, mắt, đầu hoạt động |
| **M4: Phát Hiện Cốt Lõi Hoàn Thành** | Cuối Tuần 8 | Phát hiện ngủ gật và bị phân tán chú ý hoạt động |
| **M5: Tất Cả PHẢI CÓ Xong** | Cuối Tuần 9 | Tất cả 24 tính năng quan trọng được triển khai |
| **M6: Kiểm Trace Hoàn Thành** | Cuối Tuần 11 | Tất cả trường hợp kiểm tra được thực hiện, số liệu được thu thập |
| **M7: Gửi Dự Án** | Cuối Tuần 12 | Tất cả sản phẩm giao hàng được gửi |

---

## 9. TIÊU CHÍ THÀNH CÔNG

### 9.1 Tiêu Chí Thành Công Kỹ Thuật

| Danh Mục | Tiêu Chí | Đo Lường |
|----------|----------|---------|
| **Chức Năng** | Tất cả 24 tính năng PHẢI CÓ được triển khai | Danh sách kiểm tra tính năng |
| **Độ Chính Xác** | Phát hiện ngủ gật >90% độ chính xác | Đánh giá tập dữ liệu kiểm tra |
| **Độ Chính Xác** | Nhận dạng hoạt động >85% mỗi lớp | Đánh giá tập dữ liệu kiểm tra |
| **Hiệu Suất** | Xử lý thời gian thực >15 FPS | Giám sát FPS |
| **Hiệu Suất** | Độ trễ phát hiện-đến-cảnh báo <500ms | Phân tích dấu thời gian |
| **Đáng Tin Cậy** | Thời gian hoạt động hệ thống >99% (8 giờ) | Giám sát tỷ lệ lỗi |
| **Đáng Tin Cậy** | Tỷ lệ dương tính giả <1 cảnh báo/giờ | Kiểm tra độ dài |
| **Dễ Sử Dụng** | Bảng điều khiển rõ ràng hiển thị trạng thái tài xế | Phản hồi kiểm tra người dùng |

### 9.2 Tiêu Chí Thành Công Quản Lý Dự Án

 Tất cả sản phẩm giao hàng hoàn thành đúng hạn (13 tài liệu + hệ thống hoạt động)  
 Kho lưu trữ mã được tổ chức tốt với README rõ ràng  
 Tất cả mã được kiểm tra với >70% phạm vi bao gồm  
 Cuộc họp cố vấn hàng tuần được tham dự với biên bản được ghi lại  
 Dự án nằm trong ngân sách (~$300 phần cứng)  

### 9.3 Tiêu Chí Thành Công Học Tập

 Trình bày bảo vệ luận văn được phân phát thành công  
 Trình diễn hệ thống trực tiếp trong bảo vệ (không có lỗi quan trọng)  
 Tất cả các câu hỏi từ ủy ban luận văn được trả lời thỏa đáng  
 Điểm: Tối thiểu "Tốt" (≥7.0/10) hoặc tương đương của cơ sở  
 Khuyến cáo xuất bản/thi đấu (thành tích thêm)  

### 9.4 Giảm Nhẹ Rủi Ro

**Rủi Ro Chính & Chiến Lược Giảm Nhẹ:**

**Rủi Ro 1: Độ chính xác nhận dạng hoạt động quá thấp**
- Giảm Nhẹ: Sưu tập tập dữ liệu lớn và đa dạng hơn (300+ mẫu mỗi lớp)
- Kế Hoạch Dự Phòng: Giảm xuống 5 hoạt động quan trọng nhất nếu 7 quá khó

**Rủi Ro 2: Hiệu suất theo thời gian thực không đạt trên Raspberry Pi**
- Giảm Nhẹ: Tối ưu hóa mô hình (sử dụng MobileNetV2, giảm độ phân giải khung hình)
- Kế Hoạch Dự Phòng: Nâng cấp lên Jetson Nano (GPU mạnh hơn)

**Rủi Ro 3: Trì hoãn phần cứng (camera IR hoặc thiết bị tính toán không được giao)**
- Giảm Nhẹ: Đặt hàng sớm (Tuần 2), có nhà cung cấp dự phòng
- Kế Hoạch Dự Phòng: Sử dụng webcam tiêu chuẩn tạm thời, mô phỏng bằng video được ghi lại

**Rủi Ro 4: Phát hiện ngủ gật có quá nhiều dương tính giả**
- Giảm Nhẹ: Triển khai hợp nhất đa tín hiệu (EAR + PERCLOS + ngáp)
- Kế Hoạch Dự Phòng: Thêm hiệu chỉnh mỗi tài xế để điều chỉnh ngưỡng

**Rủi Ro 5: Ràng buộc thời gian - không thể hoàn thành tất cả tính năng**
- Giảm Nhẹ: Ưu tiên nghiêm ngặt (PHẢI CÓ trước tiên), theo dõi tiến triển hàng tuần
- Kế Hoạch Dự Phòng: Ghi lại rõ ràng công việc đã hoàn thành vs. công việc trong tương lai; tập trung vào chất lượng hơn số lượng

---

## 10. TÀI LIỆU THAM KHẢO

### 10.1 Các Kỳ Báo Cáo Học Tập

1. Soukupová, T., & Čech, J. (2016). "Phát Hiện Chớp Mắt Thời Gian Thực Sử Dụng Điểm Mốc Khuôn Mặt." Hội Thảo Thị Giác Máy Tính Mùa Đông Thứ 21.
   - *Phương pháp Eye Aspect Ratio (EAR) để phát hiện ngủ gật*

2. Chirra, V. R., et al. (2019). "Mô Hình Deep CNN: Một Cách Tiếp Cận Học Máy Để Phát Hiện Ngủ Gật Tài Xế Dựa Trên Trạng Thái Mắt." Rev. d'Intelligence Artif., 33(6), 461-466.
   - *Các cách tiếp cận học sâu để giám sát ngủ gật*

3. Dua, M., et al. (2021). "Các Mô Hình Deep CNN-dựa trên Cách Tiếp Cận Ensemble Để Phát Hiện Ngủ Gật Tài Xế." Neural Computing and Applications, 33, 3155-3168.
   - *Các phương pháp ensemble để cải thiện độ chính xác*

4. Dwivedi, K., et al. (2014). "Phát Hiện Ngủ Gật Tài Xế Sử Dụng Học Tập Biểu Diễn." IEEE Intelligent Transportation Systems.
   - *Học tập tính năng cho các chỉ báo ngủ gật*

5. Jabbar, R., et al. (2018). "Phát Hiện Ngủ Gật Tài Xế Thời Gian Thực Cho Ứng Dụng Android Sử Dụng Các Kỹ Thuật Mạng Thần Kinh Sâu." Procedia Computer Science, 130, 400-407.
   - *Các tính năng triển khai di động*

6. Liu, W., et al. (2019). "Phát Hiện Phân Tán Chú Ý Tài Xế Dựa Trên Động Lực Học Xe Sử Dụng Dữ Liệu Lái Xe Tự Nhiên." IEEE Transactions on Intelligent Transportation Systems.
   - *Các cách tiếp cận phát hiện phân tán đa phương*

7. Sandler, M., et al. (2018). "MobileNetV2: Phần Dư Đảo Ngược và Nút Thắt Tuyến Tính." IEEE/CVF CVPR.
   - *Kiến trúc CNN nhẹ để triển khai biên*

### 10.2 Tài Nguyên Kỹ Thuật

8. Tài Liệu OpenCV: https://docs.opencv.org/
   - *Tài liệu thư viện thị giác máy tính*

9. Thư Viện dlib C++: http://dlib.net/
   - *Phát hiện điểm mốc khuôn mặt và nhận dạng*

10. Tài Liệu TensorFlow: https://www.tensorflow.org/
    - *Khung công việc học sâu*

11. Tài Liệu PyTorch: https://pytorch.org/
    - *Khung công việc học sâu thay thế*

### 10.3 Tập Dữ Liệu

12. Tập Dữ Liệu Phát Hiện Tài Xế Bị Phân Tán State Farm (Kaggle)
    - *Tập dữ liệu công khai để phân loại hoạt động tài xế*

13. NTHUDDD (Tập Dữ Liệu Phát Hiện Ngủ Gật Tài Xế Đại Học Quốc Gia Tsing Hua)
    - *Tập dữ liệu nghiên cứu để phát hiện ngủ gật*

14. UTA-RLDD (Tập Dữ Liệu Ngủ Gật Cuộc Sống Thực Đại Học UTA)
    - *Tập dữ liệu video ngủ gật thế giới thực*

### 10.4 Tiêu Chuẩn & Hướng Dẫn

15. ISO 15007-1:2014 - Xe Đường: Đo Lường Hành Vi Nhìn Của Tài Xế
    - *Tiêu chuẩn công nghiệp cho hệ thống giám sát tài xế*

16. Hướng Dẫn Phân Tán Trực Quan-Thủ Công NHTSA
    - *Hướng dẫn an toàn giao thông Hoa Kỳ*

---

## PHỤ LỤC

### Phụ Lục A: Tóm Tắt Tập Hợp Sản Phẩm (45 PBIs)

Xem tài liệu phiên brainstorming chi tiết:
`_bmad-output/brainstorming/brainstorming-session-2026-03-03-004815.md`

**Tóm Tắt MoSCoW:**
- **PHẢI CÓ**: 24 tính năng (Phát hiện cốt lõi, hoạt động, cảnh báo, ghi lại, bảng điều khiển)
- **NÊN CÓ**: 17 tính năng (Đăng ký, hành khách, sức khỏe hệ thống, ghi lại video)
- **CÓ THỂ CÓ**: 4 tính năng (Phân tích nâng cao, phát hiện mặt nạ, chi tiết hành khách)
- **KHÔNG CÓ**: Phát hiện dây an toàn (loại bỏ khỏi phạm vi)

### Phụ Lục B: Tóm Tắt Câu Chuyện Người Dùng (48 Câu Chuyện)

**Chia Nhân Vật (Stakeholder):**
- Tài Xế: 10 câu chuyện (cảnh báo, phản hồi, đăng ký, quyền riêng tư)
- Quản Lý Hạm Đội: 8 câu chuyện (bảng điều khiển, báo cáo, bằng chứng video)
- Kỹ Sư An Toàn: 9 câu chuyện (cấu hình, xác thực, kiểm tra)
- Nhà Phát Triển: 11 câu chuyện (kiến trúc, cơ sở dữ liệu, API, triển khai)
- Lập Trình Viên QA: 10 câu chuyện (tập dữ liệu kiểm tra, độ chính xác, hiệu suất)

Xem câu chuyện người dùng đầy đủ với tiêu chí chấp nhận trong tài liệu phiên brainstorming.

### Phụ Lục C: Ma Trận Quyết Định Công Nghệ

| Lựa Chọn Công Nghệ | Tùy Chọn A | Tùy Chọn B | Đã Chọn | Giải Thích |
|-------------------|-----------|-----------|--------|------------|
| **Thiết Bị Tính Toán** | Jetson Nano | Raspberry Pi 4 | Jetson Nano | GPU tốt hơn cho suy luận CNN |
| **Khung Công Việc DL** | TensorFlow | PyTorch | TensorFlow | Hỗ trợ di động/biên tốt hơn (TFLite) |
| **Phát Hiện Mặt** | dlib HOG | MediaPipe | dlib | Độ chính xác được chứng minh, tích hợp dễ hơn |
| **Cơ Sở Dữ Liệu** | SQLite | PostgreSQL | SQLite | Nhẹ, nhúng, đủ cho thiết bị duy nhất |
| **Giao Diện Bảng Điều Khiển** | GUI OpenCV | Flask + React | TBD Tuần 5 | Phụ thuộc vào ràng buộc thời gian |

### Phụ Lục D: Thông Tin Liên Hệ

**Sinh Viên:**  
Tên: Hung Thanh  
Email: [email-sinh-viên]  
GitHub: [tên-người-dùng-github]  

**Cố Vấn:**  
Tên: [Tên Cố Vấn]  
Email: [email-cố-vấn]  
Văn Phòng: [Vị Trí Văn Phòng]  
Lịch Họp: [Ngày/Giờ]  

---

## PHÊDUYỆT

**Chữ Ký Sinh Viên:** _____________________ Ngày: ___________

**Chữ Ký Cố Vấn:** _____________________ Ngày: ___________

---

**KẾT THÚC ĐỀ XUẤT**

---

**Thông Tin Tài Liệu:**
- **Tên Tệp:** PROPOSAL-Driver-Monitoring-System-VI.md
- **Phiên Bản:** 1.0
- **Tạo:** 4 Tháng 3, 2026
- **Tổng Số Trang:** ~18 trang (ước tính khi chuyển đổi thành PDF)
- **Số Từ:** ~7,500 từ
