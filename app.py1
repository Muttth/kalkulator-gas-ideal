import streamlit as st

# ================================
# 🎨 Background & Tema
# ================================
st.markdown(
    """
    <style>
    .stApp {
        background-image: ('biru dan awan');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }

    .block-container {
        background-color: rgba(255, 255, 255, 0.88);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 0 10px rgba(0,0,0,0.2);
    }

    h1, h2, h3, h4, h5, h6, p, label, .markdown-text-container {
        color: #004d40;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ================================
# ⚙️ Konfigurasi Halaman
# ================================
st.set_page_config(page_title="Kalkulator Gas Ideal", page_icon="🧪", layout="centered")

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
    st.markdown(r"""
    ## 🌬 Apa itu Gas Ideal?

    Gas ideal adalah model teoretis dari gas yang mengikuti persamaan *PV = nRT*, di mana:
    - Partikel gas dianggap tidak memiliki volume
    - Tidak ada gaya tarik-menarik antar partikel
    - Semua tumbukan antar partikel bersifat lenting sempurna

    ---

    ## 📏 Hukum-Hukum dalam Gas Ideal

    *1. Hukum Boyle*  
    Pada suhu tetap, volume berbanding terbalik dengan tekanan.  
    PV = Konstan
    
    P1.V1 = P2.V2
    
    *2. Hukum Charles*  
    Pada tekanan tetap, volume berbanding lurus dengan suhu.  
      VT = Konstan
      
      V1/T1 = V2/T2

    *3. Hukum Gay-Lussac*  
    Pada volume tetap, tekanan berbanding lurus dengan suhu.  
      P/T = Konstan
      
      (P1/T1 = P2/T2)
     
    ---


    ## ⚛ Sifat-Sifat Gas Ideal

    1. Partikel bergerak acak
    2. Tidak ada gaya tarik menarik
    3. Volume partikel diabaikan
    4. Distribusi merata
    5. Tumbukan lenting sempurna
    6. Energi kinetik ∝ suhu

    🔍 Catatan: Tidak ada gas yang 100% ideal, tapi model ini sangat berguna!
    """)

# ================================
# 🧮 KALKULATOR GAS IDEAL
# ================================
elif menu == "🧮 Kalkulator Gas Ideal":
    st.title("🧮 Kalkulator Gas Ideal")
    st.markdown("Masukkan *3 variabel*, dan **kosongkan 1 variabel** dengan angka **0**.")

    P = st.number_input("Tekanan (P) dalam atm", value=0.0)
    V = st.number_input("Volume (V) dalam liter", value=0.0)
    n = st.number_input("Jumlah mol (n)", value=0.0)
    T = st.number_input("Suhu (T) dalam Kelvin", value=0.0)
    R = 0.0821

    if st.button("🔍 Tampilkan Proses Perhitungan"):
        kosong = sum([P == 0, V == 0, n == 0, T == 0])

        if kosong != 1:
            st.error("❗ Harap isi *3 variabel* dan kosongkan hanya *1 variabel* dengan angka 0.")
        else:
            with st.spinner("Menghitung..."):
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
                    st.write(f"Diketahui: P = {P} atm, T = {T} K, V = {V} L, R = {R}")
                    st.latex("n = \\frac{PV}{RT}")
                    hasil = (P * V) / (R * T)
                    st.success(f"✅ Jumlah mol (n) = {hasil:.3f} mol")

                elif T == 0:
                    st.write(f"Diketahui: P = {P} atm, V = {V} L, n = {n} mol, R = {R}")
                    st.latex("T = \\frac{PV}{nR}")
                    hasil = (P * V) / (n * R)
                    st.success(f"✅ Suhu (T) = {hasil:.3f} K")

# ================================
# 👥 TENTANG KAMI
# ================================
elif menu == "👥 Tentang Kami":
    st.title("👥 Tentang Kami")
    st.markdown("""
    ### Tim Pengembang Aplikasi Kalkulator Gas Ideal

    Selamat datang di **PV-nRTin Aja!** 💻🧪

    Sebuah platform kalkulator gas ideal yang dibuat untuk mahasiswa, pelajar, atau pejuang tugas akhir—yang sering berkutat dengan rumus legendaris PV = nRT 😵‍💫

    Nama "PV-nRTin Aja" kami pilih bukan cuma biar catchy, tapi juga sebagai ajakan:
    💬 *nggak usah ribet, tinggal masukin data... terus PV-nRTin Aja!* 🚀

    Kami ingin bantu kamu belajar konsep gas ideal dengan cara yang lebih praktis dan menyenangkan 🎯

    Karena hidup udah cukup berat...
    📌 Jangan biarkan tekanan gas ikut bikin tekanan batin 🤖💨

    **Anggota Kelompok:**
    - Azka Afriyuni Suwito (2360084)
    - Dhelys Kusuma Wardani (2460356)
    - Ismi Aziz (2460393)
    - Mutia Ningrum (2460444)
    - Savira Putri Pramudita (2460514)
    """)
