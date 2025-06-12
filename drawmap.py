import streamlit as st
import plotly.express as px
import pandas as pd
import json

# Hiển thị thông tin debug
st.set_page_config(layout="wide")

# Tải dữ liệu GeoJSON của Việt Nam từ URL
try:
    with open('./diaphantinh.geojson', 'r', encoding='utf-8') as file:
        geojson_data = json.load(file)  
        st.write("Đã đọc được file GeoJSON")
        # Hiển thị số lượng tỉnh trong dữ liệu
        st.write(f"Số tỉnh trong GeoJSON: {len(geojson_data['features'])}")
except Exception as e:
    st.error(f"Lỗi khi đọc file GeoJSON: {str(e)}")
    st.stop()

# Dữ liệu các tỉnh thành và màu sắc theo tên trong file GeoJSON
province_colors = {
    # Các tỉnh không thay đổi
    "Hà Nội": 3,
    "Thừa Thiên Huế": 3,
    "Lai Châu": 1,
    "Điện Biên": 3,
    "Sơn La": 2,
    "Lạng Sơn": 3,
    "Quảng Ninh": 4,
    "Thanh Hóa": 3,
    "Nghệ An": 1,
    "Hà Tĩnh": 2,
    "Cao Bằng": 1,

    # Các tỉnh hợp nhất
    "Tuyên Quang": 4,  # Tỉnh 12
    "Hà Giang": 4,
    
    "Lào Cai": 3,  # Tỉnh 13
    "Yên Bái": 3,
    
    "Thái Nguyên": 2,  # Tỉnh 14
    "Bắc Kạn": 2,
    
    "Phú Thọ": 1,  # Tỉnh 15
    "Vĩnh Phúc": 1,
    "Hòa Bình": 1,
    
    "Bắc Ninh": 1,  # Tỉnh 16
    "Bắc Giang": 1,
    
    "Hưng Yên": 1,  # Tỉnh 17
    "Thái Bình": 1,
    
    "Hải Phòng": 2,  # Tỉnh 18
    "Hải Dương": 2,
    
    "Ninh Bình": 2,  # Tỉnh 19
    "Hà Nam": 2,
    "Nam Định": 2,
    
    "Quảng Trị": 1,  # Tỉnh 20
    "Quảng Bình": 1,
    
    "Đà Nẵng": 2,  # Tỉnh 21
    "Quảng Nam": 2,
    
    "Quảng Ngãi": 1,  # Tỉnh 22
    "Kon Tum": 1,
    
    "Gia Lai": 3,  # Tỉnh 23
    "Bình Định": 3,
    
    "Khánh Hòa": 3,  # Tỉnh 24
    "Ninh Thuận": 3,
    
    "Lâm Đồng": 1,  # Tỉnh 25
    "Đăk Nông": 1,
    "Bình Thuận": 1,
    
    "Đăk Lăk": 2,  # Tỉnh 26
    "Phú Yên": 2,
    
    "TP. Hồ Chí Minh": 2,  # Tỉnh 27
    "Bà Rịa - Vũng Tàu": 2,
    "Bình Dương": 2,
    
    "Đồng Nai": 4,  # Tỉnh 28
    "Bình Phước": 4,
    
    "Tây Ninh": 3,  # Tỉnh 29
    "Long An": 3,
    
    "Cần Thơ": 2,  # Tỉnh 30
    "Sóc Trăng": 2,
    "Hậu Giang": 2,
    
    "Vĩnh Long": 3,  # Tỉnh 31
    "Bến Tre": 3,
    "Trà Vinh": 3,
    
    "Đồng Tháp": 1,  # Tỉnh 32
    "Tiền Giang": 1,
    
    "Cà Mau": 1,  # Tỉnh 33
    "Bạc Liêu": 1,
    
    "An Giang": 3,  # Tỉnh 34
    "Kiên Giang": 3
}


# Hiển thị số lượng tỉnh trong dữ liệu màu
st.write(f"Số tỉnh trong dữ liệu màu: {len(province_colors)}")

# Mảng màu tương ứng với màu đậm hơn
colors = {
    1: '#CC0000',  # Đỏ đậm
    2: '#006600',  # Xanh lá đậm
    3: "#FF00FB",  # Xanh dương đậm
    4: '#CC9900'   # Vàng đậm
}

# Tạo DataFrame từ dữ liệu tỉnh và màu
provinces = pd.DataFrame(list(province_colors.items()), columns=['Province', 'Color'])
provinces['Color'] = provinces['Color'].map(colors)

# Hiển thị DataFrame để debug
st.write("Dữ liệu tỉnh và màu:")
st.write(provinces)

try:
    # Vẽ bản đồ sử dụng Plotly Express
    fig = px.choropleth_mapbox(provinces,
                            geojson=geojson_data,
                            locations='Province',
                            featureidkey='properties.ten_tinh',
                            color='Color',
                            mapbox_style="carto-positron",
                            zoom=5,
                            center={"lat": 16.0, "lon": 106.0},
                            opacity=0.5,
                            title="Bản đồ Việt Nam với các tỉnh thành màu sắc")
    
    # Cập nhật layout
    fig.update_layout(
        margin={"r":0,"t":30,"l":0,"b":0},
        height=800
    )

    # Hiển thị bản đồ
    st.plotly_chart(fig, use_container_width=True)
except Exception as e:
    st.error(f"Lỗi khi vẽ bản đồ: {str(e)}")
