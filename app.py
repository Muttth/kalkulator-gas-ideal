import streamlit as st

# ================================
# 🎨 Background 
# ================================
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.app.goo.gl/bbB5WwtmX7PcR7uf6");
        background-size: cover;
        background-attachment: fixed;
    }

    .block-container {
        background-color: rgba(255, 255, 255, 0.88);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 0 10px rgba(0,0,0,0.2);
    }

    h1, h2, h3, h4, h5, h6, p, label, .markdown-text-container {
        color: #00332f;
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
menu = st.sidebar.selectbox("📂 Pilih Halaman", ["🏠 Home", "📊 Teori Gas Ideal", "🧮 Kalkulator Gas Ideal", "👥 Tentang Kami"])

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

    Hitung salah satu variabel jika tiga lainnya diketahui 💡
    """)

# ================================
# 📊 Teori Gas Ideal
# ================================
elif menu == "📊 Teori Gas Ideal":
    st.title("📚 Teori dan Hukum Gas Ideal")
    st.markdown(r"""
    ## 🌬 Apa itu Gas Ideal?
    Gas ideal adalah model teoretis gas yang mengikuti hukum-hukum kinetik. Partikel gas dianggap:
    - Tidak memiliki volume
    - Tidak saling tarik-menarik
    - Tumbukan lenting sempurna

    ## ⚖️ Hukum-Hukum Penting:

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


    Tekanan akan meningkat seiring kenaikan suhu jika volume tetap.

    🧠 Semua hukum ini adalah turunan dari **persamaan gas ideal PV = nRT**

    🔍 *Catatan:* Tidak ada gas yang benar-benar ideal, tapi model ini sangat berguna dalam banyak situasi.
    """)

# ================================
# 🧮 Kalkulator Gas Ideal
# ================================
elif menu == "🧮 Kalkulator Gas Ideal":
    st.title("🧮 Kalkulator Gas Ideal")
    st.markdown("Masukkan *3 variabel*, kosongkan 1 dengan angka **0**.")

    P = st.number_input("Tekanan (P) dalam atm", value=0.0)
    V = st.number_input("Volume (V) dalam liter", value=0.0)
    n = st.number_input("Jumlah mol (n)", value=0.0)
    T = st.number_input("Suhu (T) dalam Kelvin", value=0.0)
    R = 0.0821

    if st.button("🔍 Hitung"):
        kosong = sum([P == 0, V == 0, n == 0, T == 0])
        if kosong != 1:
            st.error("❗ Harap kosongkan tepat 1 variabel dengan angka 0.")
        else:
            st.subheader("📘 Langkah Perhitungan")
            st.latex("PV = nRT")

            if P == 0:
                st.latex("P = \\frac{nRT}{V}")
                hasil = (n * R * T) / V
                st.success(f"✅ Tekanan (P) = {hasil:.3f} atm")

            elif V == 0:
                st.latex("V = \\frac{nRT}{P}")
                hasil = (n * R * T) / P
                st.success(f"✅ Volume (V) = {hasil:.3f} L")

            elif n == 0:
                st.latex("n = \\frac{PV}{RT}")
                hasil = (P * V) / (R * T)
                st.success(f"✅ Jumlah mol (n) = {hasil:.3f} mol")

            elif T == 0:
                st.latex("T = \\frac{PV}{nR}")
                hasil = (P * V) / (n * R)
                st.success(f"✅ Suhu (T) = {hasil:.2f} K")

# ================================
# 👥 Tentang Kami
# ================================
elif menu == "👥 Tentang Kami":
    st.title("👥 Tentang Kami")
    st.markdown("""
    ### Tim Pengembang PV-nRTin Aja! 💻🧪

    Kami adalah tim mahasiswa yang mengembangkan kalkulator gas ideal interaktif berbasis web untuk memudahkan pembelajaran.Selamat datang di PV-nRTin Aja! 💻🧪
    
    Sebuah platform kalkulator gas ideal yang dibuat untuk mahasiswa, pelajar, atau pejuang tugas akhir—yang sering berkutat dengan rumus legendaris PV = nRT 😵‍💫
    Di dunia teknik dan sains, perhitungan gas ideal itu penting banget, tapi jujur aja... kadang ribet 😅. 
    
    Nah, di sinilah kami hadir: biar kamu bisa fokus ke konsepnya, dan biarkan sistem kami yang ngurusin hitung-hitungan nya ✨📊
    Nama PV-nRTin Aja kami pilih bukan cuma biar catchy, tapi juga sebagai ajakan:
    💬 nggak usah ribet, tinggal masukin data... terus “PV-nRTin Aja”! 🚀
    
    Dengan tampilan simpel dan nuansa khas anak sains dan teknik, kami ingin bantu kamu belajar dengan cara yang praktis🎯
    
    Karena hidup udah cukup berat...
    
    📌 Jangan biarkan tekanan gas ikut bikin tekanan batin 🤖💨

   Terima kasih atas kunjungan dan kepercayaan Anda menggunakan aplikasi ini.
   Kami berharap aplikasi yang kami kembangkan dapat memberikan kemudahan dalam memahami konsep Hukum Gas Ideal
   serta membantu menghitung gas ideal.


    - Azka Afriyuni Suwito (2360084)  
    - Dhelys Kusuma Wardani (2460356)  
    - Ismi Aziz (2460393)  
    - Mutia Ningrum (2460444)  
    - Savira Putri Pramudita (2460514)

    💬 Motto kami: "Nggak usah ribet, tinggal masukin data, terus... PV-nRTin Aja!" 🚀

    📌 Jangan biarkan tekanan gas menambah tekanan batin 🤖💨
    """)


