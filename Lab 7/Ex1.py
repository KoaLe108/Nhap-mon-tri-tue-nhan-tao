import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.naive_bayes import BernoulliNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import (
    confusion_matrix, classification_report,
    roc_curve, auc
)

# Giao diện Streamlit
st.title("Phân loại văn bản bằng Bernoulli Naive Bayes")
st.subheader("📊 Dữ liệu huấn luyện: Education.csv")

# Đọc dữ liệu từ file có sẵn
@st.cache_data
def load_data():
    return pd.read_csv("Education.csv")

data = load_data()
st.write("Dữ liệu huấn luyện ban đầu:")
st.dataframe(data.head())

# Chia dữ liệu
def split_train_test(data, ratio_test):
    np.random.seed(0)
    index_permu = np.random.permutation(len(data))
    data_permu = data.iloc[index_permu]
    test_size = int(len(data_permu) * ratio_test)
    train_set = data_permu.iloc[:-test_size]
    test_set = data_permu.iloc[-test_size:]
    return train_set.reset_index(drop=True), test_set.reset_index(drop=True)

train_set, test_set = split_train_test(data, 0.2)
X_train, y_train = train_set["Text"], train_set["Label"]
X_test, y_test = test_set["Text"], test_set["Label"]

# Hiển thị phân phối nhãn
st.write("Phân phối nhãn (train):")
st.bar_chart(y_train.value_counts())
st.write("Phân phối nhãn (test):")
st.bar_chart(y_test.value_counts())

# Chuẩn bị dữ liệu cho mô hình
y_train_bin = y_train.map({"positive": 1, "negative": 0})

count_vec = CountVectorizer(binary=True, stop_words="english")
count_vec.fit(X_train)

X_train_vec = count_vec.transform(X_train)
X_test_vec = count_vec.transform(X_test)

# Huấn luyện mô hình
model = BernoulliNB()
model.fit(X_train_vec, y_train_bin)

# Đánh giá mô hình trên tập kiểm tra
y_pred = model.predict(X_test_vec)
y_pred_proba = model.predict_proba(X_test_vec)
y_pred_trans = np.where(y_pred == 0, "negative", "positive")

conf = confusion_matrix(y_test, y_pred_trans)
TN, FP, FN, TP = conf.ravel()

accuracy = (TP + TN) / len(y_pred_trans)
precision = TP / (TP + FP)
recall = TP / (TP + FN)
f1 = round(2 * (precision * recall) / (precision + recall), 2)

st.subheader("📌 Kết quả đánh giá mô hình")
st.write(f"Accuracy: **{accuracy:.2f}**")
st.write(f"Precision: **{precision:.2f}**")
st.write(f"Recall: **{recall:.2f}**")
st.write(f"F1-score: **{f1:.2f}**")

st.text("Classification Report:")
st.text(classification_report(y_test, y_pred_trans))

# Vẽ đường cong ROC
fpr, tpr, _ = roc_curve(y_test.map({"positive": 1, "negative": 0}), y_pred_proba[:, 1])
roc_auc = auc(fpr, tpr)

st.subheader("📈 Đường cong ROC")
fig, ax = plt.subplots()
ax.plot([0, 1], [0, 1], linestyle="--", color="gray")
ax.plot(fpr, tpr, marker=".", color="green", label=f"AUC = {roc_auc:.2f}")
ax.set_xlabel("False Positive Rate")
ax.set_ylabel("True Positive Rate")
ax.set_title("ROC Curve")
ax.legend()
st.pyplot(fig)

# ======= 📥 Nhập văn bản để phân loại =======
st.subheader("📝 Phân loại văn bản người dùng nhập")

user_input = st.text_area("Nhập nội dung văn bản ở đây:")

if st.button("Phân loại văn bản"):
    if user_input.strip() == "":
        st.warning("⚠️ Vui lòng nhập nội dung văn bản trước khi phân loại.")
    else:
        user_vec = count_vec.transform([user_input])
        user_pred = model.predict(user_vec)[0]
        label = "Positive" if user_pred == 1 else "Negative"
        st.success(f"Kết quả phân loại: **{label.upper()}** 🎯")
