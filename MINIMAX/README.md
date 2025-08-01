# Game XO (Cờ Caro) - THUẬT TOÁN MINIMAX

Dự án này bao gồm 3 phiên bản triển khai game XO (Cờ Caro) với các mức độ tối ưu khác nhau.

## 📁 Các phiên bản

### 1. Phiên bản 4x4 cơ bản (Thực hành 16)
- **Đặc điểm**:
  - Bàn cờ 4x4 cố định
  - Kiểm tra điều kiện thắng bằng cách liệt kê thủ công
  - Code dài (~200 dòng), nhiều đoạn lặp lại

### 2. Phiên bản 5x5 cơ bản (Thực hành 17) 
- **Đặc điểm**:
  - Mở rộng từ phiên bản 4x4 lên 5x5
  - Vẫn giữ cách kiểm tra thủ công
  - Code dài hơn (~300 dòng) do nhiều điều kiện hơn

### 3. Phiên bản tối ưu
- **Đặc điểm**:
  - Hỗ trợ bàn cờ kích thước tuỳ ý (3x3, 4x4, 5x5,...)
  - Sử dụng OOP và ma trận numpy
  - Kiểm tra thắng bằng vòng lặp thông minh
  - Code ngắn gọn (~80 dòng), dễ bảo trì

## 📊 So sánh các phiên bản

| Tiêu chí            | 4x4 cơ bản | 5x5 cơ bản | Tối ưu |
|---------------------|------------|------------|--------|
| Độ dài code         | ~200 dòng  | ~300 dòng  | ~80 dòng |
| Linh hoạt kích thước| ❌         | ❌         | ✅      |
| Dễ bảo trì          | ❌         | ❌         | ✅      |
| Hiệu suất           | Trung bình | Trung bình | Cao    |
| Dễ mở rộng tính năng| ❌         | ❌         | ✅      |
