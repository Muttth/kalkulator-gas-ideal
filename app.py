import streamlit as st
import base64

# ===== Fungsi untuk ubah gambar ke base64 =====
def get_base64(file_path):
    with open(file_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# ===== Fungsi untuk set background lucu =====
def set_background(jpg_file):
    bin_str = get_base64(jpg_file)
    page_bg_img = f"""
    <style>
    .stApp {{
      background-image: url("data:image/jpg;base64,{bin_str}");
      background-size: cover;
      background-position: center;
      background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Panggil fungsi background
set_background("background.jpg")

# ===== Judul Aplikasi =====
st.markdown("<h1 style='text-align: center; color: navy;'>🧪 Kalkulator Gas Ideal</h1>", unsafe_allow_html=True)

# ===== Penjelasan Hukum Gas =====
with st.expander("📘 Penjelasan Hukum Gas Ideal"):
    st.markdown("""
    **Gas Ideal** mengikuti persamaan:
    
    \n\n### `PV = nRT`
    
    Dimana:
    - `P` = Tekanan (atm)
    - `V` = Volume (L)
    - `n` = Mol zat (mol)
    - `R` = Konstanta gas = 0.0821 L·atm/mol·K
    - `T` = Suhu mutlak (K)

    ---
    ### 📏 Hukum-Hukum Gas:
    - **Hukum Boyle**: Jika T konstan, maka `P1V1 = P2V2`
    - **Hukum Charles**: Jika P konstan, maka `V1/T1 = V2/T2`
    - **Hukum Gay-Lussac**: Jika V konstan, maka `P1/T1 = P2/T2`
    """)

# ===== Kalkulator Gas Ideal =====
st.subheader("🔍 Hitung Variabel Gas Ideal")

option = st.selectbox("Pilih variabel yang ingin dicari:", ["Tekanan (P)", "Volume (V)", "Mol (n)", "Suhu (T)"])

R = 0.0821

if option == "Tekanan (P)":
    V = st.number_input("Volume (L)", min_value=0.0, format="%.2f")
    n = st.number_input("Jumlah Mol (mol)", min_value=0.0, format="%.2f")
    T = st.number_input("Suhu (K)", min_value=0.0, format="%.2f")
    if st.button("Hitung Tekanan"):
        if V > 0:
            P = (n * R * T) / V
            st.success(f"Tekanan (P) = {P:.2f} atm")
        else:
            st.error("Volume tidak boleh nol!")

elif option == "Volume (V)":
    P = st.number_input("Tekanan (atm)", min_value=0.0, format="%.2f")
    n = st.number_input("Jumlah Mol (mol)", min_value=0.0, format="%.2f")
    T = st.number_input("Suhu (K)", min_value=0.0, format="%.2f")
    if st.button("Hitung Volume"):
        if P > 0:
            V = (n * R * T) / P
            st.success(f"Volume (V) = {V:.2f} L")
        else:
            st.error("Tekanan tidak boleh nol!")

elif option == "Mol (n)":
    P = st.number_input("Tekanan (atm)", min_value=0.0, format="%.2f")
    V = st.number_input("Volume (L)", min_value=0.0, format="%.2f")
    T = st.number_input("Suhu (K)", min_value=0.0, format="%.2f")
    if st.button("Hitung Mol"):
        if T > 0:
            n = (P * V) / (R * T)
            st.success(f"Mol (n) = {n:.2f} mol")
        else:
            st.error("Suhu tidak boleh nol!")

elif option == "Suhu (T)":
    P = st.number_input("Tekanan (atm)", min_value=0.0, format="%.2f")
    V = st.number_input("Volume (L)", min_value=0.0, format="%.2f")
    n = st.number_input("Jumlah Mol (mol)", min_value=0.0, format="%.2f")
    if st.button("Hitung Suhu"):
        if n > 0:
            T = (P * V) / (n * R)
            st.success(f"Suhu (T) = {T:.2f} K")
        else:
            st.error("Mol tidak boleh nol!")
