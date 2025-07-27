import streamlit as st

# ================================
# 🎨 Background & Tema
# ================================
st.set_page_config(page_title="Kalkulator Gas Ideal", page_icon="🧪", layout="centered")

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(-45deg, #A8E6CF, #DCEDC1, #FFD3B6, #FFAAA5);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
    }

    @keyframes gradientBG {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    .block-container {
        background-color: rgba(255, 255, 255, 0.92);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 0 10px rgba(0,0,0,0.15);
    }

    h1, h2, h3, h4, h5, h6, p, label, .markdown-text-container {
        color: #004d40;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ================================
# 📂 Sidebar Navigasi
# ================================
menu = st.sidebar.selectbox("📂 Pilih Halaman", ["🏠 Home", "📊 Dashboard", "🧮 Kalkulator Gas Ideal", "👥 Tentang Kami"])

# ================================
# 🏠 HOME
# ================================
if menu == "🏠 Home":
    st.title("🧪 Aplikasi Kalkulator Gas Ideal")
    st.markdown(r"""
    ## Persamaan Gas Ideal
    \[
    PV = nRT
    \]

    **Keterangan:**
    - P : Tekanan (atm)  
    - V : Volume (L)  
    - n : Jumlah mol  
    - R : 0.0821 L·atm/mol·K  
    - T : Suhu (K)

    Aplikasi ini membantu menghitung salah satu variabel jika tiga lainnya diketahui.
    """)

# ================================
# 📊 DASHBOARD
# ================================
elif menu == "📊 Dashboard":
    st.title("📚 Penjelasan Gas Ideal")
    st.markdown("""
    ## 🌬 Apa itu Gas Ideal?

    Gas ideal adalah model teoritis dari gas yang mengikuti hukum:
    \[
    PV = nRT
    \]
    - Partikel gas dianggap tidak memiliki volume  
    - Tidak ada gaya tarik menarik antar partikel  
    - Tumbukan antar partikel bersifat lenting sempurna  

    ---

    ## 📏 Hukum-Hukum Penting

    **Hukum Boyle**  
    \[
    P_1V_1 = P_2V_2
    \] _(Suhu tetap)_

    **Hukum Charles**  
    \[
    \\frac{V_1}{T_1} = \\frac{V_2}{T_2}
    \] _(Tekanan tetap)_

    **Hukum Gay-Lussac**  
    \[
    \\frac{P_1}{T_1} = \\frac{P_2}{T_2}
    \] _(Volume tetap)_

    ---

    ## ⚛ Sifat-Sifat Gas Ideal
    1. Partikel bergerak acak
    2. Tidak ada gaya tarik menarik
    3. Volume partikel diabaikan
    4. Tumbukan lenting sempurna
    5. Energi kinetik ∝ suhu

    🔍 Tidak ada gas yang sepenuhnya ideal, tapi pendekatan ini sangat berguna!
    """)

# ================================
# 🧮 KALKULATOR GAS IDEAL
# ================================
elif menu == "🧮 Kalkulator Gas Ideal":
    st.title("🧮 Kalkulator Gas Ideal")
    st.markdown("Masukkan **3 variabel**, dan biarkan **1 variabel bernilai 0** untuk dihitung.")

    # Input variabel
    P = st.number_input("Tekanan (P) dalam atm", value=0.0)
    V = st.number_input("Volume (V) dalam liter", value=0.0)
    n = st.number_input("Jumlah mol (n)", value=0.0)
    T = st.number_input("Suhu (T) dalam Kelvin", value=0.0)
    R = 0.0821

    if st.button("🔍 Tampilkan Perhitungan"):
        kosong = sum([P == 0, V == 0, n == 0, T == 0])

        if kosong != 1:
            st.error("❗ Masukkan tepat 3 variabel, dan kosongkan 1 dengan nilai 0.")
        else:
            st.subheader("📘 Langkah-Langkah Perhitungan")
            st.latex("PV = nRT")

            if P == 0:
                st.write(f"Diketahui: n = {n} mol, T = {T} K, V = {V} L, R = {R}")
                st.latex("P = \\frac{nRT}{V}")
                hasil = (n * R * T) / V
                st.success(f"✅ Tekanan (P) = {hasil:.3f} atm")

            elif V == 0:
                st.write(f"Diketahui: n = {n} mol, T = {T} K, P = {P} atm, R = {R}")
                st.latex("V = \\frac{nRT}{P}")
                hasil = (n * R * T) / P
                st.success(f"✅ Volume (V) = {hasil:.3f} L")

            elif n == 0:
                st.write(f"Diketahui: P = {P} atm, V = {V} L, T = {T} K, R = {R}")
                st.latex("n = \\frac{PV}{RT}")
                hasil = (P * V) / (R * T)
                st.success(f"✅ Jumlah mol (n) = {hasil:.3f} mol")

            elif T == 0:
                st.write(f"Diketahui: P = {P} atm, V = {V} L, n = {n} mol, R = {R}")
                st.latex("T = \\frac{PV}{nR}")
                hasil = (P * V) / (n * R)
                st.success(f"✅ Suhu (T) = {hasil:.2f} K")

            st.caption("Perhitungan berdasarkan PV = nRT dengan R = 0.0821 L·atm/mol·K")

# ================================
# 👥 TENTANG KAMI
# ================================
elif menu == "👥 Tentang Kami":
    st.title("👥 Tentang Kami")
    st.markdown("""
    ### Tim Pengembang Aplikasi Kalkulator Gas Ideal

    Selamat datang di **PV-nRTin Aja!** 💻🧪

    Sebuah platform edukatif untuk membantu kamu memahami dan menghitung gas ideal tanpa ribet.

    **Tim Pengembang:**
    - Azka Afriyuni Suwito (2360084)
    - Dhelys Kusuma Wardani (2460356)
    - Ismi Aziz (2460393)
    - Mutia Ningrum (2460444)
    - Savira Putri Pramudita (2460514)

    ✨ Jangan biarkan tekanan gas menambah tekanan batin 🤖💨  
    """)

