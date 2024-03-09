# Tubes1_Sini-Main-Sama-Om
<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->


<!-- PROJECT LOGO -->
<p align="center">
<!-- ![image](https://github.com/WazeAzure/Tubes1_Sini-Main-Sama-Om/assets/55005873/8d57e1e6-41b7-4702-9063-30aeda616aef) -->
  <img src="https://i.pinimg.com/564x/70/bd/40/70bd40d1c3c0cfeb85197110cf674d6b.jpg">
</p>


<p align="center">We Made It ALIVE🥐</p>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![image](https://github.com/WazeAzure/Tubes1_Sini-Main-Sama-Om/assets/55005873/0a3d4198-3cd5-4686-8879-823c46db6e05)

Diamonds merupakan suatu permainan programming yang mempertandingkan bot yang anda buat dengan bot dari para pemain lainnya. Setiap pemain akan memiliki sebuah bot dimana tujuan dari bot ini adalah mengumpulkan diamond sebanyak-banyaknya. Cara mengumpulkan diamond tersebut tidak sesederhana itu, akan terdapat berbagai rintangan yang akan membuat permainan ini menjadi lebih seru dan kompleks. Untuk memenangkan pertandingan, setiap pemain harus mengimplementasikan strategi permainan atau algoritmanya masing-masing.

Penjelasan lebih lanjut mengenai aturan permainan akan dijelaskan di bawah. Komponen pada permainan ini antara lain adalah:
1. Diamonds - Terdapat 2 jenis diamond yaitu diamond biru dan diamond merah. Diamond merah bernilai 2 poin, sedangkan yang biru bernilai 1 poin
2. Red Button - Ketika red button ini dilewati/dilangkahi, semua diamond (termasuk red diamond) akan di-generate kembali pada board dengan posisi acak.
3. Teleporters - Terdapat 2 teleporter yang saling terhubung satu sama lain.
4. Bot - game ini akan menggerakkan bot untuk mendapatkan diamond sebanyak banyaknya.
5. Base - digunakan untuk menyimpan diamond yang sedang dibawa. Apabila diamond disimpan ke base, score bot akan bertambah senilai diamond yang dibawa dan inventory (akan dijelaskan di bawah) bot menjadi kosong.
6. Inventory - Inventory berfungsi sebagai tempat penyimpanan sementara diamond yang telah diambil. Inventory ini memiliki kapasitas maksimum sehingga sewaktu-waktu bisa penuh.

Aturan permainan antara lain:
1. Bot akan ditempatkan pada board secara random. Masing-masing bot akan mempunyai home base, serta memiliki score dan inventory awal bernilai nol Setiap bot diberikan waktu untuk bergerak.
2. Setiap bot diberikan waktu untuk bergerak.
3. Objektif utama bot adalah mengambil diamond-diamond yang ada di peta sebanyak-banyaknya.
4. Setiap bot juga memiliki sebuah inventory, Inventory ini sewaktu-waktu bisa penuh, maka dari itu bot harus segera kembali ke home base.
5. Apabila bot menuju ke posisi home base, score bot akan bertambah senilai diamond yang tersimpan pada inventory dan inventory bot akan menjadi kosong kembali.
6. Jika bot A menimpa posisi bot B, bot B akan dikirim ke home base dan semua diamond pada inventory bot B akan hilang, diambil masuk ke inventory bot A (istilahnya tackle).
7. Terdapat beberapa fitur tambahan seperti teleporter dan red button yang dapat digunakan apabila anda menuju posisi objek tersebut.
8. Apabila waktu seluruh bot telah berakhir, maka permainan berakhir.

Strategi yang digunakan:

Algoritma greedy yang kami pilih untuk diimplementasikan pada bot merupakan gabungan dari beberapa solusi. Untuk pemilihan diamond mana yang ditarget oleh bot, kami memilih menggunakan diamond by density karena perolehan poin yang lebih space efficient. Diamond Untuk pergerakan bot, kami menggunakan gabungan dari kedua algoritma normal path dan using teleporter. Jika jarak tempuh dari normal path lebih kecil dari jarak tempuh using teleporter, maka bot akan menggunakan arahan dari normal path, begitu juga sebaliknya. Dengan demikian, bot akan mendapatkan arah dari jalur yang paling optimal.

1. Diamond By Density: Bot memilih target diamond yang memiliki poin terbesar relatif terhadap jarak pada bot. Contohnya, jika terdapat diamond dengan poin 1 berjarak 4 dari bot dan terdapat diamond dengan poin 2 berjarak 6 dari bot, maka bot akan menuju diamond dengan poin 2.
2. Normal Path: Bot bergerak melewati langkah terdekat menuju target destinasi dengan menghitung selisih sumbu x dan sumbu y lalu menjumlahkannya untuk mendapatkan distance. Distance tersebut merupakan total langkah yang perlu dilakukan bot agar mencapai tujuan. Maka, bot dapat menentukan arah gerakan mana dari 4 arah yang tersedia untuk digunakan agar mencapai tujuan.
3. Using Teleporter: Menghitung distance sama seperti Normal path namun bot menggunakan teleporter untuk mencapai target destinasi. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Built With

* [![Python][Python]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

Make sure you have basic understanding of computer and python installed :D

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Clone the repo
   ```sh
   git clone https://github.com/WazeAzure/Tubes1_Sini-Main-Sama-Om.git
   ```
2. Install dependencies.
   ```sh
   cd Tubes1_Sini-Main-Sama-Om/src
   pip install -r requirements.txt
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## How To Run

```sh
python main.py --logic OptBot --email=optbot@email.com --name=optbot --password=123456 --team etimo --host http://localhost:3000/api --board=1
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

| Nama | NIM |
| --- | --- |
| Edbert Eddyson Gunawan | 13522039 |
| Vanson Kurnialim | 13522049 |
| Habibi Galang Trianda | 10023457 |

Project Link: https://github.com/WazeAzure/Tubes1_Sini-Main-Sama-Om

Youtube Link: https://youtu.be/eS2yTg0JvDo

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
[Flask]: https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white
[Flask-url]: https://flask.palletsprojects.com/en
