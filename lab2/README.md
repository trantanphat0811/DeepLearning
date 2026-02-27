# LAB 2: Trực Quan Hóa Dữ Liệu Điểm Thi Đại Học

## Thông tin Bài Tập
- **Sinh viên**: Trần Tấn Phát
- **MSSV**: 2274802010644
- **Mục tiêu**: Thống kê, trình bày dữ liệu cơ bản và trực quan hóa dữ liệu thực tế
- **File dữ liệu**: `processed_dulieuxettuyendaihoc.csv`
- **File Jupyter Notebook**: `TranTanPhat_2274802010644_PTDLHS_Lab2.ipynb`

## 📚 Tài Liệu Hướng Dẫn Chi Tiết

Xem file **HUONG_DAN_LAB2.md** để hiểu chi tiết:
- ✅ Ý nghĩa của Lab 2 và kỹ năng cần nắm vững
- ✅ Cấu trúc 5 phần của bài tập
- ✅ Các kỹ thuật Python cần sử dụng cho mỗi phần
- ✅ Hướng dẫn từng bước với ví dụ code
- ✅ Gợi ý best practices

## Nội Dung Notebook

Notebook gồm **5 phần chính** với **72 cells** bao gồm code và visualizations:

### **PHẦN 1: THỐNG KÊ DỮ LIỆU** (5 sections)
- 1.1: Sắp xếp DH1 theo thứ tự tăng dần
- 1.2: Sắp xếp DH2 tăng dần theo nhóm giới tính
- 1.3: Pivot table thống kê DH1 theo KT (count, sum, mean, median, min, max, std, Q1, Q2, Q3)
- 1.4: Pivot table DH1 theo KT và KV
- 1.5: Pivot table DH1 theo KT, KV và DT

### **PHẦN 2: TRÌNH BÀY DỮ LIỆU** (5 sections)
- 2.1: Tần số và tần suất cho GT (giới tính) - Biểu đồ cột và tròn
- 2.2: Biểu đồ tần số cho US_TBM1, US_TBM2, US_TBM3
- 2.3: Phân tích DT cho học sinh nam
- 2.4: Phân tích KV cho nam, dân tộc Kinh, điểm ≥ tiêu chuẩn
- 2.5: Phân tích DH1, DH2, DH3 ≥ 5.0 trong khu vực 2NT

### **PHẦN 3: TRỰC QUAN HÓA THEO NHÓM PHÂN LOẠI** (7 sections)
- 3.1: Học sinh nữ - Phân loại XL1, XL2, XL3 (Unstacked bar chart)
- 3.2: KQXT cho khối A, A1, B trong khu vực 1, 2
- 3.3: Số thí sinh theo khu vực và khối thi
- 3.4: Số thí sinh đậu/rớt theo khối thi
- 3.5: Số thí sinh đậu/rớt theo khu vực
- 3.6: Số thí sinh đậu/rớt theo dân tộc
- 3.7: Số thí sinh đậu/rớt theo giới tính

### **PHẦN 4: TRỰC QUAN HÓA NÂNG CAO** (5 sections)
- 4.1: Biểu đồ đường Simple cho T1 (toán)
- 4.2: Tạo biến phân loại `phanloait1` từ T1
  - 0-5: kém (k)
  - 5-7: trung bình (tb)
  - 7-8: khá (k)
  - 8+: giỏi (g)
- 4.3: Bảng tần số cho phanloait1
- 4.4: Multiple Line Chart cho T1 phân loại bởi phanloait1
- 4.5: Drop-line Chart cho T1 phân loại bởi phanloait1

### **PHẦN 5: MỐ TẢ DỮ LIỆU VÀ KHẢO SÁT PHÂN PHỐI** (5 sections)
- 5.1: Phân tích T1 tổng thể
  - Thống kê mô tả (mean, median, mode, std, range, IQR)
  - Box Plot và 10 đại lượng chính
  - Histogram với mean/median
  - QQ-Plot cho kiểm định chuẩn
  - Kiểm định Shapiro-Wilk
  
- 5.2: Phân phối T1 theo nhóm phanloait1
  - Box Plot, Histogram, QQ-Plot cho từng nhóm
  
- 5.3: Tương quan giữa DH1 và T1
  - Covariance và Pearson correlation
  - Scatter plot với regression line
  
- 5.4: Tương quan DH1 vs T1 theo từng khu vực
  - Multiple scatter plots by region
  
- 5.5: Tương quan giữa DH1, DH2, DH3
  - Correlation matrix
  - Covariance matrix
  - Heatmap visualization
  - Scatter plot matrix (3x3)

## Dữ Liệu

**Tập dữ liệu**: 100 học sinh thi đại học

**Các biến chính**:
- **DH1, DH2, DH3**: Điểm thi 3 môn
- **T1-T6, L1-L6, etc.**: Điểm các môn trong năm
- **GT**: Giới tính (M/F)
- **DT**: Dân tộc (ethnicity)
- **KV**: Khu vực (region)
- **KT**: Khối thi (exam type: A, A1, B, C, D1)
- **XL1, XL2, XL3**: Xếp loại (classification levels)
- **US_TBM1, US_TBM2, US_TBM3**: Điểm trung bình
- **KQXT**: Kết quả xét tuyển (admission result: 0=failed, 1=passed)

## Thư viện Sử Dụng

```python
pandas         # Xử lý dữ liệu
numpy          # Tính toán số học
matplotlib     # Vẽ biểu đồ
seaborn        # Trực quan hóa nâng cao
scipy          # Thống kê
```

## Cách Chạy Notebook

1. Mở notebook trong Jupyter Lab/Notebook
2. Chạy lần lượt từ cell trên xuống dưới
3. Hoặc chạy tất cả cells một lúc (Run All)

```bash
jupyter notebook TranTanPhat_2274802010644_PTDLHS_Lab2.ipynb
```

## Kết Quả Mong Đợi

- ✅ Phân tích dữ liệu cơ bản với pivot tables
- ✅ Bảng tần số và tần suất
- ✅ Biểu đồ cột, tròn, đường
- ✅ Box plot, histogram, QQ-plot
- ✅ Scatter plots và correlation analysis
- ✅ Phân tích phân phối
- ✅ Kiểm định thống kê

## Ghi Chú

- Notebook bao gồm tất cả các yêu cầu từ phần 1-5
- Các biểu đồ được tối ưu hóa với labels rõ ràng
- Bao gồm giải thích và nhận xét cho mỗi phân tích
- Code có comments để dễ hiểu

**Hoàn thành**: Tất cả yêu cầu bài tập đã được thực hiện chi tiết ✓
