import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 应用标题
st.title("California Housing Data (1990)")

# 加载数据
data = pd.read_csv("./housing.csv")

# 显示原始数据
st.write("Housing Data Overview", data.head())

# 最小价格滑块
min_price = st.slider("Select Minimum Median House Price", 0, 500001, 200000)

# 过滤数据

# 显示地图
st.map(filtered_data)

# 显示直方图
plt.hist(filtered_data)
st.pyplot(plt)

# 显示最终过滤后的数据
st.write("Filtered Housing Data", filtered_data)
