import streamlit as st
import streamlit.components.v1 as components

# ================================
# 🎆 Background Partikel Bergerak
# ================================
components.html(
    """
    <script src="https://cdn.jsdelivr.net/npm/tsparticles@2.3.3/tsparticles.bundle.min.js"></script>
    <div id="tsparticles" style="position: fixed; width: 100%; height: 100%; z-index: -1;"></div>
    <script>
    tsParticles.load("tsparticles", {
      "particles": {
        "number": {
          "value": 60,
          "density": { "enable": true, "value_area": 800 }
        },
        "color": { "value": "#ffffff" },
        "shape": { "type": "circle" },
        "opacity": { "value": 0.4 },
        "size": { "value": 3 },
        "move": { "enable": true, "speed": 1 }
      },
      "background": { "color": "#000000" }
    });
    </script>
    """,
    height=0,
)

# ================================
# 🎨 Tema dan Styling
# ================================
st.markdown(
    """
    <style>
    .stApp {
        background-color: transparent;
    }
    .block-container {
        background-color: rgba(255, 255, 255, 0.88);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 0 10px rgba(0,0,0,0.2);
    }
    h1, h2, h3, h4, h5, h6, p, label {
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
menu = st.sidebar.selectbox("📂 Pilih Halaman", ["🏠 Home", "📊 Teori Gas Ideal", "🧮 Kalkulator", "👥 Tentang Kami"])

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
    - P = Tekanan (atm)  
    - V = Volume (L)  
    - n = Jumlah mol  
    - R = 0.0821 L·atm/mol·K  
    - T = Suhu (K)

    Aplikasi ini membantu menghitung salah satu variabel jika tiga lainnya diketahui.
    """)

# ================================
# 📊 TEORI GAS IDEAL
# ================================
elif menu == "📊 Teori Gas Ideal":
    st.title("📚 Teori dan Hukum Gas Ideal")

    st.markdown("""
    ## 🌬 Apa itu Gas Ideal?
    Gas ideal adalah model teoretis dari gas yang memenuhi persamaan:
    \[
    PV = nRT
    \]
    - Partikel gas dianggap kecil dan tidak saling tarik-menarik  
    - Tumbukan antar partikel bersifat lenting sempurna  
    - Distribusi partikel merata dan acak

    ---

    ## 📏 Hukum-Hukum Penting

    ### 1. Hukum Boyle (Tekanan vs Volume)
    \[
    P_1 V_1 = P_2 V_2 \quad (\text{suhu tetap})
    \]
    > Volume berbanding terbalik dengan tekanan  
    Contoh: Jika tekanan naik, volume turun.

    ### 2. Hukum Charles (Volume vs Suhu)
    \[
    \frac{V_1}{T_1} = \frac{V_2}{T_2} \quad (\text{tekanan tetap})
    \]
    > Volume berbanding lurus dengan suhu  
    Contoh: Gas dipanaskan, volumenya membesar.

    ### 3. Hukum Gay-Lussac (Tekanan vs Suhu)
    \[
    \frac{P_1}{T_1} = \frac{P_2}{T_2} \quad (\text{volume tetap})
    \]
    > Tekanan naik saat suhu naik, jika volume tidak berubah.

    ---

    ## ⚛ Sifat Gas Ideal:
    - Tidak ada gaya tarik menarik antar partikel
    - Volume partikel diabaikan
    - Tumbukan antar partikel lenting sempurna
    - Energi kinetik rata-rata ∝ suhu mutlak
    - Berlaku pada suhu tinggi dan tekanan rendah

    ✨ Meskipun ideal, konsep ini sangat berguna untuk pendekatan awal dalam banyak perhitungan gas!
    """)

# ================================
# 🧮 KALKULATOR GAS IDEAL
# ================================
elif menu == "🧮 Kalkulator":
    st.title("🧮 Kalkulator Gas Ideal")
    st.markdown("Masukkan **3 variabel**, dan kosongkan **1 variabel** dengan nilai **0**:")

    P = st.number_input("Tekanan (P) dalam atm", value=0.0)
    V = st.number_input("Volume (V) dalam liter", value=0.0)
    n = st.number_input("Jumlah mol (n)", value=0.0)
    T = st.number_input("Suhu (T) dalam Kelvin", value=0.0)
    R = 0.0821  # Konstanta gas

    if st.button("🔍 Hitung"):
        kosong = sum([P == 0, V == 0, n == 0, T == 0])

        if kosong != 1:
            st.error("❗ Harap isi 3 variabel dan kosongkan hanya 1 variabel dengan angka 0.")
        else:
            st.subheader("📘 Langkah Perhitungan")
            st.latex("PV = nRT")

            if P == 0:
                hasil = (n * R * T) / V
                st.latex("P = \\frac{nRT}{V}")
                st.success(f"✅ Tekanan (P) = {hasil:.3f} atm")
            elif V == 0:
                hasil = (n * R * T) / P
                st.latex("V = \\frac{nRT}{P}")
                st.success(f"✅ Volume (V) = {hasil:.3f} L")
            elif n == 0:
                hasil = (P * V) / (R * T)
                st.latex("n = \\frac{PV}{RT}")
                st.success(f"✅ Jumlah mol (n) = {hasil:.3f} mol")
            elif T == 0:
                hasil = (P * V) / (n * R)
                st.latex("T = \\frac{PV}{nR}")
                st.success(f"✅ Suhu (T) = {hasil:.2f} K")

# ================================
# 👥 TENTANG KAMI
# ================================
elif menu == "👥 Tentang Kami":
    st.title("👥 Tentang Kami")
    st.markdown("""
    ### Tim Pengembang Aplikasi Kalkulator Gas Ideal

    Selamat datang di **PV-nRTin Aja!** 💻🧪  
    Platform kalkulator interaktif untuk bantu kamu belajar dan menghitung persamaan gas ideal.

    **Kenapa dibuat?**  
    Karena rumus gas ideal itu penting — tapi bisa bikin pusing. Nah, kami bantu supaya:
    - Lebih praktis
    - Lebih paham konsep
    - Nggak ribet ngitung manual

    **Disusun oleh Kelompok 2:**
    - Azka Afriyuni Suwito (2360084)
    - Dhelys Kusuma Wardani (2460356)
    - Ismi Aziz (2460393)
    - Mutia Ningrum (2460444)
    - Savira Putri Pramudita (2460514)

    ✨ "Jangan biarkan tekanan gas menambah tekanan batin" 🤖💨  
    Terima kasih telah menggunakan aplikasi kami 🙏
    """)
