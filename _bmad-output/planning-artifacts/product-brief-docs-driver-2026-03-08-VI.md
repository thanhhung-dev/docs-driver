---
stepsCompleted: [1, 2, 3, 4, 5]
inputDocuments: ["_bmad-output/brainstorming/brainstorming-session-2026-03-03-004815.md", "_bmad-output/proposal/PROPOSAL-Driver-Monitoring-System.md", "_bmad-output/proposal/PROPOSAL-Driver-Monitoring-System-VI.md", "_bmad-output/guides/HUONG-DAN-DO-AN-TOT-NGHIEP.md", "_bmad-output/planning-artifacts/prd.md"]
date: 2026-03-08
author: hung-thanh
---

# Tóm tắt Sản phẩm: docs-driver

## Tóm tắt Điều hành (Executive Summary)
**docs-driver** là một Hệ thống Giám sát Tài xế (DMS) tiên tiến sử dụng AI và thị giác máy tính để phát hiện các dấu hiệu mệt mỏi, buồn ngủ và xao nhãng trong thời gian thực. Dự án nhằm giảm thiểu tai nạn giao thông bằng cách cung cấp các cảnh báo tức thì và phân tích hành vi lái xe, hỗ trợ cả cá nhân và các doanh nghiệp vận tải trong việc quản lý an toàn đường bộ.

---

## Tầm nhìn Cốt lõi (Core Vision)

### Tuyên bố Vấn đề
Mỗi năm, hàng triệu vụ tai nạn giao thông xảy ra do lỗi của con người, trong đó mệt mỏi, buồn ngủ và thiếu tập trung (sử dụng điện thoại, không nhìn đường) là những nguyên nhân hàng đầu. Các hệ thống cảnh báo hiện có trên xe thường không đủ nhạy bén hoặc thiếu tính cá nhân hóa để ngăn chặn kịp thời các tình huống nguy hiểm.

### Tác động của Vấn đề
- **Con người:** Gây thương vong và tổn thất sức khỏe cho tài xế và hành khách.
- **Kinh tế:** Thiệt hại đáng kể về phương tiện, hàng hóa và chi phí bảo hiểm cho các đội xe vận tải.
- **Xã hội:** Gây áp lực lên hệ thống y tế và an toàn giao thông công cộng.

### Tại sao các giải pháp hiện tại chưa đáp ứng được
- **Hệ thống truyền thống:** Dựa vào cảm biến vô lăng hoặc cảm biến xe, đôi khi phản ứng quá chậm khi tài xế đã mất kiểm soát.
- **Thiết bị giám sát rời rạc:** Thiếu sự đồng bộ, độ trễ cao trong xử lý hình ảnh và thường gặp khó khăn trong điều kiện thiếu sáng hoặc khi tài xế đeo kính.
- **Chi phí:** Các hệ thống DMS cao cấp thường chỉ có trên các dòng xe sang, khiến đa số tài xế và doanh nghiệp nhỏ khó tiếp cận.

### Giải pháp đề xuất
Một hệ thống DMS tích hợp AI có khả năng:
- **Xử lý tại biên (Edge Processing):** Phân tích hình ảnh trực tiếp trên thiết bị để đảm bảo tính tức thời.
- **Phát hiện đa trạng thái:** Nhận diện buồn ngủ (ngáp, nhắm mắt), xao nhãng (nhìn sang bên, dùng điện thoại) và hút thuốc.
- **Cảnh báo đa phương thức:** Âm thanh, hình ảnh và thông báo đến hệ thống quản lý trung tâm.

### Các điểm khác biệt chính
- **Độ chính xác cao:** Sử dụng các mô hình Deep Learning được tối ưu hóa để nhận diện khuôn mặt và các điểm mốc (landmarks).
- **Hiệu năng mạnh mẽ:** Hoạt động hiệu quả trong mọi điều kiện ánh sáng (đèn LED hồng ngoại) và hỗ trợ tài xế đeo kính.
- **Tích hợp hệ sinh thái:** Khả năng kết nối với ứng dụng di động và nền tảng Quản lý Đội xe để theo dõi lịch sử và đánh giá rủi ro.

---

## Đối tượng Người dùng Mục tiêu

### Người dùng Chính

#### Chân dung: Anh Hùng - Tài xế đường dài (Xe container/xe khách)
- **Bối cảnh:** Lái xe xuyên đêm, chịu áp lực thời gian và mệt mỏi thể chất kéo dài.
- **Vấn đề:** Dễ rơi vào trạng thái ngủ gật (micro-sleep) mà không tự nhận diện được.
- **Thành công:** Luôn tỉnh táo nhờ cảnh báo kịp thời, giảm thiểu rủi ro tai nạn nghiêm trọng.

#### Chân dung: Bạn Lan - Tài xế cá nhân mới lái
- **Bối cảnh:** Di chuyển trong đô thị, dễ xao nhãng bởi điện thoại hoặc áp lực công việc.
- **Vấn đề:** Thiếu tập trung vào gương chiếu hậu hoặc nhìn đường, dẫn đến va chạm nhỏ.
- **Thành công:** Hình thành thói quen lái xe tập trung và an toàn hơn.

### Người dùng Phụ
- **Chủ doanh nghiệp vận tải:** Quản lý an toàn đội xe, giảm chi phí sửa chữa và bảo hiểm thông qua dữ liệu báo cáo hành vi tài xế.
- **Gia đình tài xế:** Yên tâm về sự an toàn của người thân khi lưu thông trên đường.

---

## Chỉ số Thành công (Success Metrics cho Đồ án)

### Mục tiêu Học thuật & Kỹ thuật
*   **Độ chính xác mô hình (Model Accuracy):** 
    *   Phát hiện buồn ngủ (Drowsiness): > 90%
    *   Nhận diện hoạt động nguy hiểm (Activity Recognition): > 85%
    *   Tỉ lệ dương tính giả (False Positive Rate): < 5% (Tránh cảnh báo sai gây phiền)
*   **Hiệu suất thời gian thực (Real-time Performance):**
    *   Tốc độ xử lý khung hình (FPS): > 15 FPS trên thiết bị nhúng (Raspberry Pi 4 / Jetson Nano).
    *   Độ trễ hệ thống (Latency): < 100ms từ khi phát hiện đến khi phát cảnh báo.
*   **Khả năng thích nghi (Robustness):**
    *   Hoạt động ổn định trong điều kiện thiếu sáng (sử dụng Camera IR).
    *   Xử lý được các trường hợp tài xế đeo kính hoặc khẩu trang.

---

## Phạm vi MVP (MVP Scope - Phạm vi Đồ án)

### Tính năng Cốt lõi (Core Features)
*   **Giám sát buồn ngủ:** Phát hiện nhắm mắt (Eye closure) và ngáp (Yawning) dựa trên EAR và MAR.
*   **Giám sát mất tập trung:** Theo dõi hướng đầu (Head pose) và hướng nhìn (Gaze direction).
*   **Nhận diện hành vi nguy hiểm:** Phát hiện gọi điện thoại (Calling), uống nước (Drinking), hút thuốc (Smoking).
*   **Hệ thống cảnh báo thời gian thực:** Cảnh báo bằng âm thanh và hình ảnh ngay lập tức khi phát hiện rủi ro.
*   **Ghi nhật ký sự kiện:** Lưu trữ toàn bộ dữ liệu vi phạm và ảnh chụp (Snapshots) vào cơ sở dữ liệu để phục vụ hậu kiểm.
*   **Giao diện Dashboard:** Hiển thị trạng thái giám sát thời gian thực và lịch sử các cảnh báo.
*   **Xác thực người lái:** Sử dụng nhận diện khuôn mặt để định danh tài xế trước khi bắt đầu hành trình.

### Ngoài phạm vi MVP (Out of Scope)
*   Ứng dụng di động (Mobile App).
*   Đồng bộ hóa dữ liệu đám mây (Cloud Sync).
*   Quản lý đội xe tập trung (Fleet Management).
*   Tích hợp trực tiếp vào hệ thống cơ khí/điện tử của xe.
*   Tính năng tự lái (Autonomous driving).
