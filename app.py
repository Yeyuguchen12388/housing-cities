import streamlit as st
from modules.data_loader import load_data
from modules.filters import apply_filters
from modules.visualizations import plot_map, plot_histogram

# 应用标题
st.title("California Housing Data (1990)")

# 加载数据
data = load_data("data/housing.csv")

# 显示原始数据
st.write("Housing Data Overview", data.head())

# 最小价格滑块
min_price = st.slider("Select Minimum Median House Price", 0, 500001, 200000)

# 过滤数据
filtered_data = apply_filters(data, min_price)

# 显示地图
plot_map(filtered_data)

# 显示直方图
plot_histogram(filtered_data)

# 显示最终过滤后的数据
st.write("Filtered Housing Data", filtered_data)
