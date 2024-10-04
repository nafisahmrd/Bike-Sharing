import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

#gather data
temperature_df = pd.read_csv("temperature.csv")
day_df = pd.read_csv("dayy.csv")
grouped = pd.read_csv("grouped.csv")

st.title('BIKE SHARING DATASET : PROYEK ANALISIS DATA')
st.header('Course Dicoding : Belajar Analisis Data dengan Python')


def suhu():
    plt.figure(figsize=(10, 6))
    sns.barplot(x='temp', y='cnt', data=temperature_df, color='Maroon', label='Total Pengguna')
    # sns.barplot(x='temp', y='registered', data=temperature_df, palette='Oranges', label='Registered Users')

    # Tambahkan judul dan label sumbu
    plt.title('Hubungan Suhu dengan Penggunaan Sepeda')
    plt.xlabel('Kisaran Suhu (°C)')
    plt.ylabel('Rata-rata Jumlah Pengguna')
    plt.xticks(rotation=45)

    # Tampilkan legenda
    plt.legend()

    # Tampilkan chart
    st.pyplot(plt)


def daily():
    # Buat pivot table dari DataFrame yang dikelompokkan
    pivot = grouped.pivot(index='weekday', columns='yr', values='cnt')

    # Atur warna untuk masing-masing tahun
    colors = ['#ff69b4', '#add8e6']  # Pink dan biru muda
   
    # Buat plot dengan ukuran figure yang diinginkan
    ax = pivot.plot(kind='bar', stacked=False, figsize=(15, 6), width=0.9, color=colors)

    # Atur judul dan label sumbu
    plt.title('Hari Terlaris untuk Penggunaan Sepeda')
    plt.xlabel('Hari dalam Seminggu')
    plt.ylabel('Jumlah Pengguna')
    plt.xticks(rotation=15)

    # Tambahkan nilai di atas masing-masing bar
    for p in ax.patches:
        ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))

    # Tampilkan plot
    st.pyplot(plt)


# no.1 : chart suhu terhadap penggunaan sepeda
st.subheader('1. Pengaruh Suhu terhadap Penggunaan Sepeda')
suhu()
st.write("""
Diagram menunjukkan hubungan positif antara suhu dan jumlah pengguna sepeda. Artinya, semakin tinggi suhu, semakin banyak orang yang memilih untuk bersepeda.

Faktor-faktor yang memengaruhi:
- Kenyamanan: Cuaca yang hangat dan cerah lebih nyaman untuk bersepeda dibandingkan cuaca dingin atau hujan.
- Aktivitas Luar Ruangan: Cuaca yang baik mendorong orang untuk beraktivitas di luar ruangan, termasuk bersepeda.
- Pakaian: Pakaian yang lebih ringan dan nyaman dapat digunakan saat cuaca hangat, sehingga lebih mudah bersepeda.

Kesimpulan:
Suhu adalah faktor penting yang mempengaruhi keputusan seseorang untuk bersepeda. Informasi ini berguna untuk mengembangkan kebijakan dan program yang mendorong penggunaan sepeda.
""")

# no.2 : clustered bar chart penggunaan sepeda setiap harinya dalam 2 tahun
st.subheader('2. Penggunaan Sepeda Setiap Harinya dalam 2 Tahun')
daily()
st.write("""
Berdasarkan diagram yang disajikan, hari Sabtu secara konsisten menunjukkan jumlah pengguna sepeda sharing terbanyak baik di tahun 2011 maupun 2012. Ini mengindikasikan bahwa banyak orang memilih untuk bersepeda pada hari Sabtu sebagai kegiatan rekreasi atau olahraga.

Faktor-faktor yang mempengaruhi:
- Akhir pekan: Hari Sabtu merupakan bagian dari akhir pekan, di mana banyak orang memiliki waktu luang lebih banyak untuk beraktivitas di luar ruangan, termasuk bersepeda.
- Cuaca: Kondisi cuaca yang cerah dan menyenangkan pada hari Sabtu mungkin mendorong lebih banyak orang untuk menggunakan sepeda.
- Aktivitas sosial: Banyak acara atau kegiatan komunitas yang diselenggarakan pada hari Sabtu, yang melibatkan penggunaan sepeda sebagai alat transportasi atau bagian dari acara tersebut.

Kesimpulan:
Dari data yang ditampilkan, dapat disimpulkan bahwa hari Sabtu adalah hari yang paling populer untuk menggunakan layanan sepeda sharing. Pola ini menunjukkan adanya preferensi masyarakat untuk bersepeda pada akhir pekan, terutama ketika kondisi cuaca mendukung.
""")

st.subheader('Kesimpulan Analisis:')
st.write("""
1. Para pengguna cenderung lebih suka menggunakan sepeda saat suhu berada dalam kondisi hangat.
2. Pada tahun 2011, hari dengan pengguna terbanyak adalah Selasa, sementara pada tahun 2012, hari dengan jumlah pengguna terbanyak jatuh pada hari Kamis. Hal ini sangat dipengaruhi oleh berbagai faktor, seperti hari libur dan kondisi cuaca setiap tahunnya.
""")

