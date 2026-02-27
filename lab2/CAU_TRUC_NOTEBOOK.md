# CẤU TRÚC NOTEBOOK LAB 2

## 📋 Tổng Quan

Notebook **TranTanPhat_2274802010644_PTDLHS_Lab2.ipynb** chứa **70+ cells** được tổ chức thành:
- **1 phần Giới thiệu** (Objective & Concepts)
- **5 phần Chính** (Phần 1-5)
- **1 phần Kết luận** (Conclusion)

---

## 🎯 Phần Giới Thiệu

### Cell 1: Tiêu đề & Mục tiêu
- Tiêu đề: "LAB 2: TRỰC QUAN HÓA DỮ LIỆU - XỬ LÝ ĐIỂM THI ĐẠI HỌC"
- Sinh viên: Trần Tấn Phát - MSSV: 2274802010644
- Ý nghĩa Lab 2 (4 điểm chính)

### Cell 2-3: Import Libraries & Load Data
- Import pandas, numpy, matplotlib, seaborn, scipy.stats
- Cấu hình style cho visualizations
- Load CSV file `processed_dulieuxettuyendaihoc.csv`
- Hiển thị info cơ bản: shape, dtypes, statistics

---

## 📊 PHẦN 1: THỐNG KÊ DỮ LIỆU (5 Subsections)

Mục tiêu: Làm quen sắp xếp dữ liệu và tính thống kê mô tả.

### 1.1 Sắp xếp DH1 tăng dần
- **Tiêu đề**: "Sắp xếp dữ liệu DH1 theo thứ tự tăng dần"
- **Code**: 
  - `df.sort_values('DH1', ascending=True)`
  - In ra STT, DH1, Min/Max values
- **Output**: Bảng sắp xếp + thống kê

### 1.2 Sắp xếp DH2 tăng dần theo GT
- **Tiêu đề**: "Sắp xếp DH2 tăng dần theo nhóm giới tính"
- **Code**:
  - `df.sort_values(['GT', 'DH2'], ascending=[True, True])`
  - In ra count by gender
- **Output**: Bảng sắp xếp + thống kê theo giới tính

### 1.3 Pivot Table DH1 theo KT
- **Tiêu đề**: "Pivot Table thống kê DH1 theo KT"
- **Code**:
  - `df.groupby('KT')['DH1'].agg(['count', 'sum', 'mean', ...])`
  - Thêm Q1, Q2, Q3
- **Output**: Bảng pivot với 10 chỉ số

### 1.4 Pivot Table DH1 theo KT + KV
- **Tiêu đề**: "Pivot Table thống kê DH1 theo KT và KV"
- **Code**:
  - Custom function `get_stats(x)` để tính 10 chỉ số
  - `df.groupby(['KT', 'KV'])['DH1'].apply(get_stats)`
- **Output**: Bảng pivot 2-level index

### 1.5 Pivot Table DH1 theo KT + KV + DT
- **Tiêu đề**: "Pivot Table thống kê DH1 theo KT, KV và DT"
- **Code**:
  - `df.groupby(['KT', 'KV', 'DT'])['DH1'].apply(get_stats)`
- **Output**: Bảng pivot 3-level index

---

## 📈 PHẦN 2: TRÌNH BÀY DỮ LIỆU (5 Subsections)

Mục tiêu: Trình bày dữ liệu bằng bảng tần số và biểu đồ.

### 2.1 Tần số & Tần suất GT (Giới tính)
- **Tiêu đề**: "Trình bày dữ liệu biến GT (Giới tính)"
- **Code**:
  - `df['GT'].value_counts()`
  - Biểu đồ cột (bar chart) + Biểu đồ tròn (pie chart)
- **Output**: Bảng tần số + 2 biểu đồ

### 2.2 Trình bày US_TBM1, US_TBM2, US_TBM3
- **Tiêu đề**: "Trình bày dữ liệu biến US_TBM1, US_TBM2, US_TBM3"
- **Code**:
  - Lặp qua 3 biến
  - `value_counts()` + bar chart cho mỗi biến
- **Output**: 3 biểu đồ + thống kê

### 2.3 DT (Dân tộc) cho học sinh nam
- **Tiêu đề**: "Trình bày DT cho học sinh nam"
- **Code**:
  - Filter: `df[df['GT'] == 'M']['DT']`
  - Bar chart
- **Output**: Biểu đồ + tần số

### 2.4 KV (Khu vực) cho nam, Kinh, điểm ≥ chuẩn
- **Tiêu đề**: "Trình bày KV cho nam, dân tộc Kinh, điểm thỏa điều kiện"
- **Code**:
  - Filter: `df[(df['GT'] == 'M') & (df['DT'] == 0.0) & (df['DH1'] >= 5.0) & (df['DH2'] >= 4.0) & (df['DH3'] >= 4.0)]['KV']`
  - Bar chart
- **Output**: Biểu đồ + số lượng records

### 2.5 DH1, DH2, DH3 ≥ 5.0 khu vực 2NT
- **Tiêu đề**: "Trình bày DH1, DH2, DH3 >= 5.0 thuộc khu vực 2NT"
- **Code**:
  - Filter: `df[(df['KV'] == '2NT') & (df['DH1'] >= 5.0) & (df['DH2'] >= 5.0) & (df['DH3'] >= 5.0)]`
  - Histograms cho 3 biến
- **Output**: 3 histograms + describe()

---

## 📊 PHẦN 3: TRỰC QUAN HÓA THEO NHÓM (7 Subsections)

Mục tiêu: So sánh dữ liệu giữa các nhóm.

### 3.1 Học sinh nữ - XL1, XL2, XL3
- **Tiêu đề**: "Học sinh nữ trên nhóm XL1, XL2, XL3 (unstacked)"
- **Code**:
  - Filter: `df[df['GT'] == 'F']`
  - 3 bar charts cho XL1, XL2, XL3
- **Output**: 1x3 subplot bar charts

### 3.2 KQXT cho khối A, A1, B khu vực 1, 2
- **Tiêu đề**: "KQXT cho khối A, A1, B trong khu vực 1, 2"
- **Code**:
  - Filter: `df[(df['KT'].isin(['A', 'A1', 'B'])) & (df['KV'].isin([1, 2, '1', '2']))]`
  - `pd.crosstab()` + bar chart
- **Output**: Bảng crosstab + biểu đồ

### 3.3 Số thí sinh theo KV & KT
- **Tiêu đề**: "Số lượng thí sinh theo khu vực và khối thi"
- **Code**:
  - `pd.crosstab(df['KV'], df['KT'])`
  - Grouped bar chart
- **Output**: Bảng + biểu đồ

### 3.4 Số thí sinh đậu/rớt theo KT
- **Tiêu đề**: "Số thí sinh đậu, rớt theo khối thi"
- **Code**:
  - `pd.crosstab(df['KT'], df['KQXT'])`
  - Grouped bar chart
- **Output**: Bảng + biểu đồ

### 3.5 Số thí sinh đậu/rớt theo KV
- **Tiêu đề**: "Số thí sinh đậu, rớt theo khu vực"
- **Code**:
  - `pd.crosstab(df['KV'], df['KQXT'])`
  - Grouped bar chart
- **Output**: Bảng + biểu đồ

### 3.6 Số thí sinh đậu/rớt theo DT
- **Tiêu đề**: "Số thí sinh đậu, rớt theo dân tộc"
- **Code**:
  - `pd.crosstab(df['DT'], df['KQXT'])`
  - Grouped bar chart
- **Output**: Bảng + biểu đồ

### 3.7 Số thí sinh đậu/rớt theo GT
- **Tiêu đề**: "Số thí sinh đậu, rớt theo giới tính"
- **Code**:
  - `pd.crosstab(df['GT'], df['KQXT'])`
  - Grouped bar chart
- **Output**: Bảng + biểu đồ

---

## 🎨 PHẦN 4: TRỰC QUAN HÓA NÂNG CAO (5 Subsections)

Mục tiêu: Sử dụng các biểu đồ phức tạp hơn.

### 4.1 Biểu đồ đường Simple cho T1
- **Tiêu đề**: "Biểu đồ đường Simple cho T1"
- **Code**:
  - `ax.plot(range(len(df)), df['T1'].values, marker='o')`
  - In describe()
- **Output**: Line chart + thống kê

### 4.2 Tạo biến phân loại phanloait1
- **Tiêu đề**: "Tạo biến phân loại phanloait1 từ T1"
- **Code**:
  - Custom function: `classify_t1(score)`
  - Mapping: < 5 → 'k', 5-7 → 'tb', 7-8 → 'kh', >= 8 → 'g'
  - `df['phanloait1'] = df['T1'].apply(classify_t1)`
- **Output**: Value counts + head(20)

### 4.3 Bảng tần số phanloait1
- **Tiêu đề**: "Bảng tần số cho phanloait1"
- **Code**:
  - `df['phanloait1'].value_counts()`
  - Tính tần suất
- **Output**: Bảng tần số & tần suất

### 4.4 Multiple Line Chart theo phanloait1
- **Tiêu đề**: "Biểu đồ đường Multiple Line cho T1 phân loại bởi phanloait1"
- **Code**:
  - Loop qua 3 categories
  - `ax.plot()` cho mỗi category với màu khác nhau
- **Output**: Line chart với 3 lines + legend

### 4.5 Drop-line Chart theo phanloait1
- **Tiêu đề**: "Biểu đồ Drop-line cho T1 phân loại bởi phanloait1"
- **Code**:
  - `ax.vlines()` + `ax.scatter()`
  - Baseline ở 0
- **Output**: Drop-line chart

---

## 📉 PHẦN 5: MÔ TẢ DỮ LIỆU & PHÂN PHỐI (5 Subsections)

Mục tiêu: Phân tích phân phối và tương quan.

### 5.1 Phân tích phân phối T1
- **Tiêu đề**: "Mô tả và khảo sát phân phối cho T1"
- **Code**:
  - In: mean, median, mode, std, variance, skewness, kurtosis
  - Shapiro-Wilk test
  - Interpretation guidelines
- **Output**: Thống kê + ghi chú

#### 5.1.1 Box Plot
- `sns.boxplot(df['T1'])`
- In 10 key values: min, Q1, Q2, Q3, max, IQR, range, outlier count
- **Output**: Box plot + thống kê

#### 5.1.2 Histogram
- `plt.hist()` + mean/median lines
- **Output**: Histogram

#### 5.1.3 QQ-Plot
- `probplot()` từ scipy.stats
- **Output**: QQ-plot + interpretation

### 5.2 Phân phối T1 theo phanloait1 (3x3 subplot)
- **Tiêu đề**: "Phân phối T1 theo từng nhóm phanloait1"
- **Code**:
  - 3x3 subplot: box plot, histogram, QQ-plot cho mỗi category
  - In thống kê cho mỗi category
- **Output**: 9 subplots + thống kê

### 5.3 Tương quan DH1 vs T1
- **Tiêu đề**: "Tương quan giữa DH1 và T1"
- **Code**:
  - `np.cov()`, `df.corr()`
  - Scatter plot + regression line
  - Interpretation
- **Output**: Scatter plot + hệ số tương quan

### 5.4 Tương quan DH1 vs T1 theo KV (2x3 subplot)
- **Tiêu đề**: "Tương quan DH1 vs T1 theo từng nhóm khu vực"
- **Code**:
  - Loop qua regions
  - 6 scatter plots + regression lines
  - In correlation coefficient cho mỗi region
- **Output**: 6 subplots + correlation values

### 5.5 Ma trận tương quan DH1, DH2, DH3
- **Tiêu đề**: "Tương quan giữa DH1, DH2, DH3"
- **Code**:
  - `df[['DH1', 'DH2', 'DH3']].corr()`
  - `np.cov()`
  - `sns.heatmap()` của correlation matrix
  - In covariance matrix
- **Output**: Heatmap + 2 matrices

#### 5.5.1 Scatter Plot Matrix (3x3)
- **Code**:
  - Diagonal: histograms
  - Off-diagonal: scatter plots + regression lines
- **Output**: 3x3 scatter matrix

---

## ✅ Kết Luận

### Cell cuối: "KÊTLUẬN"
- Tóm tắt 5 phần chính
- Số lượng cells và visualizations
- Trạng thái hoàn thành

---

## 📁 File Structure

```
/Users/trantanphat/Documents/Python/PTDL_DL/TH/thư mục không có tiêu đề/
├── TranTanPhat_2274802010644_PTDLHS_Lab2.ipynb  (Notebook chính - 70+ cells)
├── processed_dulieuxettuyendaihoc.csv            (Dữ liệu - 100 rows)
├── README.md                                     (Tóm tắt nội dung)
├── HUONG_DAN_LAB2.md                            (Hướng dẫn chi tiết 5 phần)
├── MAU_CODE_LAB2.md                             (Mã gợi ý Python)
└── CAU_TRUC_NOTEBOOK.md                         (File này)
```

---

## 🎓 Kỹ năng Rèn Luyện

- ✅ Sắp xếp dữ liệu với `sort_values()`
- ✅ Pivot table & groupby aggregation
- ✅ Lọc dữ liệu với điều kiện
- ✅ Tạo biến phân loại với `apply()`
- ✅ Bar chart, pie chart, line chart
- ✅ Box plot, histogram, QQ-plot
- ✅ Scatter plot & regression line
- ✅ Heatmap & correlation matrix
- ✅ Thống kê mô tả (skewness, kurtosis, shapiro test)
- ✅ Phân tích tương quan

---

**Hoàn thành cấu trúc Lab 2!**
