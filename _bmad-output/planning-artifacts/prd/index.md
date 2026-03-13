# Product Requirements Document - Driver Monitoring System (DMS)

## Table of Contents

- [Product Requirements Document - Driver Monitoring System (DMS)](#table-of-contents)
  - [stepsCompleted: ['step-01-init', 'step-02-discovery', 'step-02b-vision', 'step-02c-executive-summary', 'step-03-success', 'step-05-domain', 'step-06-innovation', 'step-08-scoping', 'step-09-functional', 'step-10-nonfunctional', 'step-11-polish']
inputDocuments: []
workflowType: 'prd'
classification:
projectType: iot_embedded
domain: automotive
complexity: high
projectContext: brownfield](#stepscompleted-step-01-init-step-02-discovery-step-02b-vision-step-02c-executive-summary-step-03-success-step-05-domain-step-06-innovation-step-08-scoping-step-09-functional-step-10-nonfunctional-step-11-polish-inputdocuments-workflowtype-prd-classification-projecttype-iotembedded-domain-automotive-complexity-high-projectcontext-brownfield)
  - [1. Executive Summary](./1-executive-summary.md)
  - [2. Success Criteria](./2-success-criteria.md)
    - [2.1 User Success (Thành công của Người dùng)](./2-success-criteria.md#21-user-success-thnh-cng-ca-ngi-dng)
    - [2.2 Project Success (Thành công của Đồ án)](./2-success-criteria.md#22-project-success-thnh-cng-ca-n)
    - [2.3 Technical Success (Thành công về Kỹ thuật)](./2-success-criteria.md#23-technical-success-thnh-cng-v-k-thut)
    - [2.4 Measurable Outcomes (Kết quả có thể đo lường)](./2-success-criteria.md#24-measurable-outcomes-kt-qu-c-th-o-lng)
  - [3. Product Scope Overview (Tổng quan Phạm vi Sản phẩm)](./3-product-scope-overview-tng-quan-phm-vi-sn-phm.md)
    - [3.1 MVP - Sản phẩm Khả dụng Tối thiểu (Mục tiêu cho Đồ án)](./3-product-scope-overview-tng-quan-phm-vi-sn-phm.md#31-mvp-sn-phm-kh-dng-ti-thiu-mc-tiu-cho-n)
    - [3.2 Post-MVP Features (Tính năng phát triển sau Đồ án)](./3-product-scope-overview-tng-quan-phm-vi-sn-phm.md#32-post-mvp-features-tnh-nng-pht-trin-sau-n)
    - [3.3 Vision (Tầm nhìn Tương lai)](./3-product-scope-overview-tng-quan-phm-vi-sn-phm.md#33-vision-tm-nhn-tng-lai)
  - [4. User Journeys (Hành trình Người dùng)](./4-user-journeys-hnh-trnh-ngi-dng.md)
    - [4.1 Hành trình 1: Tài xế Anh Minh - Phát hiện và Cảnh báo Sớm](./4-user-journeys-hnh-trnh-ngi-dng.md#41-hnh-trnh-1-ti-x-anh-minh-pht-hin-v-cnh-bo-sm)
    - [4.2 Hành trình 2: Giảng viên Thầy Hùng - Đánh giá và Xác minh](./4-user-journeys-hnh-trnh-ngi-dng.md#42-hnh-trnh-2-ging-vin-thy-hng-nh-gi-v-xc-minh)
    - [4.3 Journey Requirements Summary (Tóm tắt Yêu cầu từ Hành trình)](./4-user-journeys-hnh-trnh-ngi-dng.md#43-journey-requirements-summary-tm-tt-yu-cu-t-hnh-trnh)
  - [5. IoT/Embedded Specific Requirements (Yêu cầu Đặc thù cho IoT/Nhúng)](./5-iotembedded-specific-requirements-yu-cu-c-th-cho-iotnhng.md)
    - [5.1 Project-Type Overview](./5-iotembedded-specific-requirements-yu-cu-c-th-cho-iotnhng.md#51-project-type-overview)
    - [5.2 Technical Architecture Considerations](./5-iotembedded-specific-requirements-yu-cu-c-th-cho-iotnhng.md#52-technical-architecture-considerations)
    - [5.3 Hardware Requirements](./5-iotembedded-specific-requirements-yu-cu-c-th-cho-iotnhng.md#53-hardware-requirements)
    - [5.4 Connectivity Protocol](./5-iotembedded-specific-requirements-yu-cu-c-th-cho-iotnhng.md#54-connectivity-protocol)
    - [5.5 Power Profile](./5-iotembedded-specific-requirements-yu-cu-c-th-cho-iotnhng.md#55-power-profile)
    - [5.6 Security Model](./5-iotembedded-specific-requirements-yu-cu-c-th-cho-iotnhng.md#56-security-model)
    - [5.7 Update Mechanism](./5-iotembedded-specific-requirements-yu-cu-c-th-cho-iotnhng.md#57-update-mechanism)
    - [5.8 Implementation Considerations](./5-iotembedded-specific-requirements-yu-cu-c-th-cho-iotnhng.md#58-implementation-considerations)
  - [6. Project Scoping & Phased Development (Phạm vi Dự án & Phát triển theo Giai đoạn)](./6-project-scoping-phased-development-phm-vi-d-n-pht-trin-theo-giai-on.md)
    - [6.1 MVP Strategy & Philosophy](./6-project-scoping-phased-development-phm-vi-d-n-pht-trin-theo-giai-on.md#61-mvp-strategy-philosophy)
    - [6.2 Post-MVP Features](./6-project-scoping-phased-development-phm-vi-d-n-pht-trin-theo-giai-on.md#62-post-mvp-features)
    - [6.3 Risk Mitigation Strategy](./6-project-scoping-phased-development-phm-vi-d-n-pht-trin-theo-giai-on.md#63-risk-mitigation-strategy)
  - [7. Functional Requirements (Các Yêu cầu Chức năng)](./7-functional-requirements-cc-yu-cu-chc-nng.md)
    - [7.1 Quản lý Đầu vào Video](./7-functional-requirements-cc-yu-cu-chc-nng.md#71-qun-l-u-vo-video)
    - [7.2 Phát hiện và Phân tích Trạng thái Tài xế](./7-functional-requirements-cc-yu-cu-chc-nng.md#72-pht-hin-v-phn-tch-trng-thi-ti-x)
      - [7.2.1 Phát hiện Hành vi Nguy hiểm](./7-functional-requirements-cc-yu-cu-chc-nng.md#721-pht-hin-hnh-vi-nguy-him)
    - [7.3 Quản lý Cảnh báo](./7-functional-requirements-cc-yu-cu-chc-nng.md#73-qun-l-cnh-bo)
    - [7.4 Quản lý Dữ liệu và Bằng chứng](./7-functional-requirements-cc-yu-cu-chc-nng.md#74-qun-l-d-liu-v-bng-chng)
    - [7.5 Quản lý Cấu hình](./7-functional-requirements-cc-yu-cu-chc-nng.md#75-qun-l-cu-hnh)
  - [8. Non-Functional Requirements (Yêu cầu Phi Chức năng)](./8-non-functional-requirements-yu-cu-phi-chc-nng.md)
    - [8.1 Performance (Hiệu suất)](./8-non-functional-requirements-yu-cu-phi-chc-nng.md#81-performance-hiu-sut)
    - [8.2 Reliability (Độ tin cậy)](./8-non-functional-requirements-yu-cu-phi-chc-nng.md#82-reliability-tin-cy)
