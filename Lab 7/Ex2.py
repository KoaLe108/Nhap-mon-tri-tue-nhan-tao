import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import skew
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Giao diện
st.set_page_config(page_title="Phân loại thuốc - Gaussian Naive Bayes", layout="centered")
st.title("💊 Phân loại thuốc với Gaussian Naive Bayes")
st.subheader("Dữ liệu: `drug200.csv`")

# Đọc dữ liệu
@st.cache_data
def load_data():
    return pd.read_csv("drug200.csv")

data = load_data()
st.write("📋 Dữ liệu mẫu:")
st.dataframe(data.tail(10))

# Tách X, y
X = data.drop(['Drug'], axis=1)
y = data['Drug']

# Thống kê các giá trị danh mục
st.subheader("📊 Thống kê các đặc trưng phân loại")
col1, col2 = st.columns(2)
with col1:
    st.write("Phân phối giới tính:")
    st.bar_chart(X['Sex'].value_counts())
with col2:
    st.write("Phân phối huyết áp:")
    st.bar_chart(X['BP'].value_counts())

st.write("Phân phối Cholesterol:")
st.bar_chart(X['Cholesterol'].value_counts())
st.write("Phân phối mục tiêu (Drug):")
st.bar_chart(y.value_counts())

# Xử lý dữ liệu
X = pd.get_dummies(X, dtype='int')  # one-hot encoding
y = y.map({"drugA": 1, "drugB": 2, "drugC": 3, "drugX": 4, "DrugY": 5})

# Phân phối Na_to_K
st.subheader("📈 Phân phối cột Na_to_K")
fig, ax = plt.subplots()
sns.histplot(X['Na_to_K'], kde=True, ax=ax, color='skyblue')
ax.set_xlabel("Na_to_K")
ax.set_ylabel("Số lượng")
st.pyplot(fig)
skewness = skew(X['Na_to_K'])
st.write(f"Độ lệch phân phối (skewness): **{skewness:.2f}**")
if skewness > 0:
    st.info("📈 Phân phối lệch phải.")
elif skewness < 0:
    st.info("📉 Phân phối lệch trái.")
else:
    st.info("⚖️ Phân phối gần như đối xứng.")

# Tạo tập train, test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
st.subheader("🔀 Chia dữ liệu")
st.write(f"Tập huấn luyện: {len(X_train)} dòng")
st.write(f"Tập kiểm tra: {len(X_test)} dòng")

# Huấn luyện
gaussian = GaussianNB()
gaussian.fit(X_train, y_train)
y_pred = gaussian.predict(X_test)
y_pred_proba = gaussian.predict_proba(X_test)

# Dự đoán
mapp = {1: "drugA", 2: "drugB", 3: "drugC", 4: "drugX", 5: "DrugY"}
y_pred_trans = [mapp[i] for i in y_pred]
y_test_trans = [mapp[i] for i in y_test]

st.subheader("📋 Kết quả dự đoán (5 dòng đầu):")
result_df = pd.DataFrame({
    "Thực tế": y_test_trans[:5],
    "Dự đoán": y_pred_trans[:5],
    "Xác suất cao nhất": np.max(y_pred_proba[:5], axis=1).round(2)
})
st.dataframe(result_df)

# Báo cáo phân loại
st.subheader("📊 Báo cáo phân loại")
report = classification_report(y_test, y_pred, output_dict=True)
report_df = pd.DataFrame(report).transpose()
st.dataframe(report_df.style.format(precision=2))

# Tùy chọn hiển thị toàn bộ xác suất dự đoán
with st.expander("📦 Xem xác suất dự đoán chi tiết (tất cả nhãn)"):
    proba_df = pd.DataFrame(y_pred_proba, columns=[mapp[i] for i in range(1, 6)])
    st.dataframe(proba_df.head())

