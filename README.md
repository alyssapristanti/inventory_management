Nama    : Fathirahma Alyssa Pristanti
NPM     : 2206082215
Kelas   : PBP-F


# Adaptable Link
https://inventory-management.adaptable.app 

# Jawaban Pertanyaan
1. **Implementasi Checklist**
    >> Membuat proyek baru di Django
        - Membuat direktori lokal dengan nama inventory_management
        - Melakukan cd pada terminal
        - Menginisiasi repository baru pada git dengan git init
        - Membuka direktori lokal pada IDE (Visual Studio Code)
        - Membuat berkas README.md
        - Melakukan perintah git add dan git commit pada terminal
        - Mengaktifkan virtual environment pada terminal
        - Membuat file requirements.txt yang berisi package/dependencies yang dibutuhkan
        - Melakukan instalasi package dengan perintah pip install -r requirements.txt pada terminal
        - Membuat proyek django dengan nama inventory_management dengan perintah django-admin startproject inventory_management
    >> Membuat aplikasi dengan nama main pada proyek tersebut
        - Membuka terminal dan melakukan cd pada direktori utama, yaitu inventory_management
        - Mengaktifkan virtual environment
        - Melakukan perintah python3 manage.py startapp main
    >> Melakukan routing pada proyek agar dapat menjalankan aplikasi main
        - Menambahkan 'main' pada INSTALLED_APPS yang ada di berkas settings.py
    >> Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib (name dengan tipe CharField, amount dengan tipe IntegerField, description dengan tipe TextField)
        - Membuat Class bernama Item
        - Menambahkan beberapa atribut
            - Atribut Wajib:
                1. name dengan tipe CharField
                2. amount dengan tipe IntegerField
                3. description dengan tipe TextField
            - Atribut tambahan:
                1. category dengan tipe CharField
    >> Membuat fungsi views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas.
        - Membuat def show_main yang menerima parameter request
        - Membuat context yang merupakan dictionary data yang akan dikirimkan ke Views yang terdiri atas:
            1. application_name yang merupakan nama aplikasi
            2. name yang berisi data nama
            3. class yang berisi data kelas
        - Melakukan render tampilan dengan return render(request, "main.html", context)
    >> Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py
        - Menambahkan path('', include('main.urls')) pada berkas urls.py yang ada di dalam folder project
        - Menambahkan path('', show_main, name='show_main') pada berkas urls.py yang ada di dalam aplikasi main
    >> Melakukan deployment ke Adaptable
        - Melakukan perintah git add, git commit, dan git push pada terminal
        - Membuat New App pada Adaptable kemudian memilih repository proyek inventory_management sebagai basis aplikasi akun yang akan di-deploy
        - Memilih Python App Template sebagai template deployment
        - Memilih PostgreSQL sebagai basis data yang digunakan
        - Menyesuaikan versi Python yang digunakan
        - Memasukkan perintah python manage.py migrate && gunicorn inventory_management.wsgi pada bagian Start Command
        - Memasukkan nama aplikasi, yaitu inventory-management
        - Mencentang HTTP Listener on PORT kemudian melakukan deploy
        - Menyalin nama domain untuk dimasukkan ke berkas README.md
    >> Membuat sebuah README.md yang berisi tautan menuju aplikasi Adaptable yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.
        - Menjawab pertanyaan pada berkas README.md
2. **Bagan Request Client dan Penjelasannya**
    ![Alt text](Bagan.jpg)
    Alur request client ke web aplikasi berbasis Django adalah pertama client akan mengakses URL yang didefinisikan di dalam urls.py. Kemudian, permintaan tersebut diarahkan ke fungsi-fungsi yang sesuai dalam views.py. Fungsi-fungsi tersebut kemudian mengambil atau mengakses data yang didefinisikan di dalam models.py, dan kemudian hasilnya akan dikirim kepada client melalui berkas HTML yang telah dirancang dengan baik.

3. **Alasan menggunakan Virtual Environment dan Apakah bisa membuat aplikasi berbasis Django tanpa Virtual Environment**
    Virtual environment dibutuhkan untuk menghasilkan beberapa proyek Django dalam suatu sistem yang membutuhkan package/dependensi dan versi Python yang berbeda. Dengan adanya virtual environment, dapat mencegah terjadinya konflik dependensi di antara proyek-proyek tersebut. Kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment. Namun, hal tersebut tidak disarankan karena dapat menimbulkan masalah dengan dependensi proyek dan konflik dengan proyek lain. 
4. **Perbedaan MVC, MVT, dan MVVM**
    >> MVC
    1. Model: Model merepresentasikan sebuah objek yang membawa data. Model dapat memiliki logic untuk melakukan _update_ controller apabila data berubah. Namun, model tidak memiliki logic untuk menyajikan data kepada user.
    2. View: View merepresentasikan visualisasi dari data yang dimiliki oleh model. View dapat mengakses data yang dimiliki model, namun tidak mengerti apa kegunaan dari data tersebut.
    3. Controller: Controller mengatur _flow_ data dari model dan melakukan _update_ view ketika data berubah. Controller mengatur agar model dan view terpisah.

    >> MVT
    1. Model: Model membantu untuk menangani _databases_. Model merupakan _access data layer_ yang mengandung beberapa _fields_ dan _behaviors_ dari data yang disimpan. Model membantu _developers_ untuk melakukan CRUD (_create, read, update, and delete_) objek
    2. View: View digunakan untuk mengeksekusi _business logic_ dan berinterkasi secara langsung dengan Model untuk membawa data dan melakukan _render_ dari template. View mengambil data dari model. Kemudian, View dapat memberikan akses kepada template untuk mengakses data tersebut atau memprosesnya sendiri. View menerima request dari Client, mengaplkasikan _business logic_, dan menyajikan response HTTP kepada Client.
    3. Template: Template merupakan sebuah _layer_ yang dapat menangani User Interface. Template berisi HTML _code_ yang digunakan untuk me-_render_ data. Kode di template dapat berupa statis atau dinamis. Template hanya digunakan untuk menyajikan data, tidak ada _business logic_ di sini

    >> MVVM
    1. Model: Model merepresentasikan domain dari sebuah aplikasi yang terdiri atas model data, _business and validation logic_
    2. View: View merepresentasikan sebuah _user interface_ dari sebuah aplikasi yang mengimplementasikan visual. View tidak berisi data-data dan tidak dapat juga memanipulasi data-data tersebut.
    3. ViewModel: ViewModel menghubungkan antara View dan Model. ViewModel mengimplementasi dan juga menghubungkan _public properties_ dan _command_ yang digunakan View menggunakan _data binding_. Apabila terjadi perubahan, View akan menotifikasi View dengan sebuah _event_

    >> Perbedaan ketiga design pattern
    MVC digunakan untuk mengembangkan sistem perangkat lunak. Namun, MVT adalah MVC yang secara spesifik digunakan untuk pengembangan proyek Django. Kemudian, MVVM digunakan untuk pengembangan aplikasi yang berfokus pada User Interface (UI)