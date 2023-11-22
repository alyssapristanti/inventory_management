Nama    : Fathirahma Alyssa Pristanti
NPM     : 2206082215
Kelas   : PBP-F


# Adaptable Link
https://inventory-management.adaptable.app

# Tugas 2
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

# Tugas 3
# Jawaban Pertanyaan
1. **Perbedaan form Post dan Get**
    >>POST
    Post mengemas data dari forms, mengkodekannya untuk proses transmisi, mengirimkannya ke server, dan kemudian menerima responsnya.

    >>GET
    GET mengemas data yang dikirimkan ke dalam bentuk String dan menggunakannya untuk membuat URL. URL tersebut akan berisi data yang harus dikirimkan, serta key dan value dari data tersebut.
    
    GET dan POST biasanya digunakan untuk tujuan yang berbeda. Request yang sifatnya mengubah status sistem serta membuat perubahan dalam database lebih cocok untuk menggunakan POST dibandingkan dengan GET. Selain itu, POST juga cocok digunakan untuk memproses data yang jumlahnya besar atau dalam bentuk binary data, seperti gambar. Aplikasi yang menggunakan GET lebih rentan dari segi security karena akan memberikan akses ke bagian sensitif dari sistem. POST dikombinasikan dengan sistem keamanan seperti perlindungan CSRF Django sehingga memberikan kontrol terhadap akses dari sistem. Di sisi lain, GET cocok untuk hal-hal seperti web search form karena URL yang merepresentasikan GET dapat dengan mudah ditandai, disimpan, dan dikirim ulang.
2. **Perbedaan antara XML, JSON, dan HTML**
    >>XML
    XML adalah sebuah markup language dan format file yang digunakan untuk menyimpan, mengirim, dan merekonstruksi sebuah data. XML mendefinisikan sejumlah aturan untuk mengkodekan dokumen dalam format yang dapat dibaca oleh manusia dan mesin. XML telah umum digunakan untuk proses pertukaran data melalui Internet. Pada web app, XML digunakan untuk menyimpan atau melakukan pertukaran data. Data-data dalam XML bersifat self-descriptive sehingga dengan membaca XML manusia dapat mengerti informasi apa yang ingin disampaikan.

    >>JSON
    JSON adalah sebuah format file dan format pertukaran data yang menggunakan teks yang mudah dibaca oleh manusia untuk menyimpan dan mengirim objek yang terdiri atas atribut-atribut. JSON adalah format data yang umum digunakan dalam aplikasi web dan server. JSON umumnya digunakan untuk meng-serialisasi dan mengirimkan data melalui koneksi jaringan seperti internet. JSON digunakan terutama untuk mengirimkan data antara server dan aplikasi web. JSON dapat mengelola berbagai jenis data seperti String, Numbers, Booleans, Null, Arrays, dan Objects. JSON bersifat self-describing, sehingga JSON sangat mudah untuk dimengerti.

    >>HTML
    HTML adalah sebuah markup language yang digunakan oleh web untuk menginterpretasikan dan menyusun teks, gambar, dan materi lainnya menjadi sebuah halaman web. HTML terdiri atas beberapa komponen (atribut), jenis data berbasis karakter, referensi karakter, dan referensi entitas. Tag HTMl yang paling umum yaitu tag awal yang menandai awal elemen dan sering memiliki atribut yang mendefinisikan sifat elemen tersebut, contohnya adalah <p> untuk paragraf dan tag akhir yang menandai akhir elemen dan biasanya mirip dengan tag awal, tetapi dengan tanda "/" sebelum nama elemen, contohnya adalah </p> untuk menutup paragraf.

    Pada dasarnya, JSON dan XML adalah metode untuk menyimpan dan mentransfer data, sedangkan HTML adalah metode untuk menjelaskan bagaimana data ini harus ditampilkan di perangkat pengguna. Baik JSON maupun XML memiliki kelebihan dan kekurangan masing-masing; JSON lebih ringkas dibandingkan XML, tetapi XML lebih fleksibel dan aman.

3. **Alasan JSON sering digunakan dalam pertukaran data antara aplikasi web modern?**
    JSON sering digunakan dalam pertukaran data karena beberapa alasan. Pertama, JSON bersifat native bagi JavaScript dan biasanya digunakan di dalam JavaScript program sebagai literal. Selain itu, JSON juga dapat digunakan dalam bahasa pemrograman lain sehingga bersifat heterogen. Terakhir, JSON sangat mudah dibaca oleh manusia. Sebagai sebuah struktur data bahasa (language data structure), JSON sangat serbaguna. Penggunaan JSON cukup mudah jika dibandingkan dengan format lainnya.
4. **Implementasi Checklist**
    >> Membuat input form untuk menambahkan objek model pada app sebelumnya

        - Membuat berkas file forms.py pada direktori main kemudian membuat struktur form yang akan menerima data dari produk baru. Kemudian data dari form tersebut akan disimpan dalam objek Item

        - Menambahkan fields dari Product yang terdiri atas name, amount, description, dan category

    >> Menambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID

        > Melihat objek dalam format HTML

            - Membuka berkas views.py pada direktori main kemudian melakukan import HTTPResponseDirect, import Item dari main.models, dan import ProductForm dari forms.py

            - Membuat sebuah fungsi bernama create_new_product yang akan menerima request dari client sebagai parameter kemudian menambahkan kode apabila form valid dan apabila request method menggunakan POST maka data akan ditambahkan secara otomatis saat client men-submit form

            - Mengubah fungsi show_main pada views.py dengan menambahkan all_products = Item.objects.all() untuk mengambil seluruh data yang ada pada objek Item yang tersimpan di dalam database kemudian menambahkan products: all_products.

            - Menambahkan kode untuk menampilkan produk yang telah ditambahkan dengan melakukan iterasi setiap produk pada objek products pada berkas main.html
        
        > Melihat objek dalam format XML

            - Membuka berkas views.py pada direktori main kemudian melakukan import HTTPResponseDirect dan import Serializers

            - Membuat sebuah fungsi bernama show_xml

            - Menambahkan variabel all_products kemudian melakukan assignment Item.objects.all() untuk mengambil seluruh data pada objek Item

            - Membuat variabel data yang akan menyimpan hasil query dari seluruh data pada Item

            - Membuat return function berupa HTTPResponse return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


        > Melihat objek dalam format JSON

            - Membuka berkas views.py pada direktori main kemudian melakukan import HTTPResponseDirect dan import Serializers

            - Membuat sebuah fungsi bernama show_xml

            - Menambahkan variabel all_products kemudian melakukan assignment Item.objects.all() untuk mengambil seluruh data pada objek Item

            - Membuat variabel data yang akan menyimpan hasil query dari seluruh data pada Item

            - Membuat return function berupa HTTPResponse return HttpResponse(serializers.serialize("json", data), content_type="application/json")

        > Melihat objek dalam format XML by ID

            - Membuka berkas views.py pada direktori main kemudian melakukan import HTTPResponseDirect dan import Serializers

            - Membuat sebuah fungsi bernama show_xml_by_id

            - Menambahkan variabel product kemudian melakukan assignment Item.objects.all() untuk mengambil seluruh data pada objek Item

            - Membuat variabel data dan menambahkan pk=id untuk menyimpan hasil query dari data pada Item dengan id tertentu

            - Membuat return function berupa HTTPResponse return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


        > Melihat objek dalam format JSON by ID

            - Membuka berkas views.py pada direktori main kemudian melakukan import HTTPResponseDirect dan import Serializers

            - Membuat sebuah fungsi bernama show_xml_by_id

            - Menambahkan variabel product kemudian melakukan assignment Item.objects.all() untuk mengambil seluruh data pada objek Item

            - Membuat variabel data dan menambahkan pk=id untuk menyimpan hasil query dari data pada Item dengan id tertentu

            - Membuat return function berupa HTTPResponse return HttpResponse(serializers.serialize("json", data), content_type="application/json")

    >> Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.

        - Melakukan import fungsi create_new_product, show_xml, show_json, show_json_by_id, show_xml_by_id

        - Menambahkan path('create-new-product', create_new_product, name='create_new_product') untuk routing HTML pada berkas urls.py di folder main
        
        - Menambahkan path('xml/', show_xml, name='show_xml') untuk routing XML pada berkas urls.py di folder main
    
        - Menambahkan path('json/', show_json, name='show_json') untuk routing JSON pada berkas urls.py di folder main


        - Menambahkan path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id') untuk routing XML by ID pada berkas urls.py di folder main
    
        - path('json/<int:id>', show_json_by_id, name='show_json_by_id') untuk routing JSON by ID pada berkas urls.py di folder main

    >> Mengakses URL dengan POSTMAN

        - HTML
          ![Alt text](<Postman HTML.png>)

        - JSON
          ![Alt text](<Postman JSON.png>)

        - XML
          ![Alt text](<Postman XML.png>)

        - JSON by ID
          ![Alt text](<Postman JSON by ID.png>)

        - XML by ID
          ![Alt text](<Postman XML by ID.png>)


    >> Menjawab beberapa pertanyaan berikut pada README.md pada root folder.
    
        - Menjawab pertanyaan dan menjelaskan implementasi checklist pada file README.md

# Tugas 4
# Jawaban Pertanyaan
1. **Django UserCreationForm, kelebihan dan kekurangannya**
    >> Django UserCreationForm
    Django UserCreation Form digunakan untuk membuat user baru di dalam sebuah web applications. Django UserCreationForm terdiri atas 3 field yaitu username, password 1, dan password 2 (password 1 dan password 2 digunakan untuk melakukan verifikasi password)

    >> Kelebihan UserCreationForm
        - Mudah digunakan
        
        - Menyediakan validasi untuk memastikan bahwa input pengguna valid

        - Dapat menyesuaikan tampilan form

        - Dapat mengirimkan pesan kesalahan

    >> Kekurangan UserCreationForm
        - Tidak mendukung adanya fitur lanjutan seperti two factor authentication

        - Ada keterbatasan dalam validasi yang bersifat kostumisasi

        - Desain UI/UX yang kurang menarik
2. **Perbedaan antara autentikasi & otorisasi dan alasan keduanya penting**
    >> Autentikasi
    Autentikasi adalah proses melakukan verifikasi identitas pengguna dan memastikan bahwa pengguna yang mengakses adalah orang yang sebenarnya dan sudah melakukan registrasi sebelumnya. Contoh dari proses autentikasi adalah memastikan bahwa username dan password yang dimasukkan sesuai dengan username dan password yang telah didaftarkan sebelumnya

    >> Otorisasi
    Otorisasasi adalah proses untuk memberikan akses dan memutuskan apa saja fitur-fitur atau halaman yang dapat diakses oleh pengguna yang sebelumnya sudah diautentikasi. Contoh dari proses otorisasi adalah apabila user sudah melakukan login maka ia dapat melihat landing page dari suatu website

    >> Alasan keduanya penting
    - Autentikasi penting untuk melindungi data dari pengguna dari akses yang tidak sah
    - Otorisasi penting untuk mengontrol akses ke beberapa bagian atau fitur yang ada dalam sebuah aplikasi
3. **Pengertian Cookies dan pengimplementasiannya di Django untuk mengelola data sesi pengguna**
    >> Pengertian Cookies
    Cookies adalah bagian yang digunakan untuk melakukan rekam jejak dan aktivitas pengguna ketika melakukan penelusuran di dalam sebuah website. Cookies adalah file yang disimpan di dalam komputer pengguna. Cookie memungkinkan website untuk dapat mengetahui yang telah dilakukan pengguna dan waktunya.

    >> Pengimplementasian di Django untuk mengelola data sesi pengguna
    - Mengidentifikasi pengguna saat pertama kali mengunjungi situs web tertentu

    - Menyimpan data session pengguna dan detail seperti waktu

    - Melacak aktivitas pengguna

4. **Apakah cookies aman secara default atau ada risiko potensial yang harus diwaspadai?**
    Cookies tidak sepenuhnya aman secara default karena akan ada beberapa risiko potensial yang perlu diwaaspadai seperti pencurian data atau informasi, penyadapan data, pemalsuan cookie, dan Cookies Cross-Site Scripting (XSS). Beberapa cara untuk mengurangi risiko potensial dari cookie adalah sebagai berikut:
    - Melakukan enkripsi untuk mengakses data-data yang sifatnya sensitif

    - Mengakses web menggunakan format HTTPS

    - Simpan hanya informasi yang benar-benar diperlukan dalam cookie
    
5. **Implementasi checklist**
    >> Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar
        
        > Fungsi registrasi

            - Membuka fungsi views.py yang ada pada subdirektori main

            - Melakukan import redirect, UserCreationForm, messages

            - Membuat fungsi dengan nama register_account yang menerima parameter berupa request

            - Apabila request menggunakan POST, maka akan membuat UserCreationForm baru dengan memasukkan QueryDict sesuai dengan input user

            - Kemudian, akan dilakukan validasi isi input dari form tersebut. Apabila isi input valid, maka form akan disimpan kemudian akan menampilkan message bahwa user telah berhasil melakukan registrasi

            - Akan dilakukan redirect setelah form berhasil disimpan

            - Apabila request selain POST, maka akan membuat UserCreationForm juga namun tidak menggunakan request POST di parameternya

        > Fungsi login

            - Membuka fungsi views.py yang ada pada subdirektori main

            - Melakukan import autenthicate dan login

            - Membuat fungsi dengan nama login_user yang menerima parameter berupa request

            - Mengambil input pada field username dan password kemudian mengassign sebagai variabel username dan password

            - Melakukan autentikasi apakah input yang dimasukkan sesuai dengan username dan password yang terdaftar

            - Apabila proses autentikasi berhasil maka user telah berhasil login

            - Apabila proses autentikasi gagal maka akan menampilkan message gagal login

        > Fungsi logout

            - Membuka fungsi views.py yang ada pada subdirektori main

            - Melakukan import autenthicate dan login

            - Membuat fungsi dengan nama login_user yang menerima parameter berupa request

            - Menghapus sesi user yang telah masuk dengan logout(request)

            - Setelah berhasil logout, user akan diarahkan ke halaman login

    >> Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal
        
        - Membuat akun pengguna dengan username hello@ui yang terdiri atas 3 data item, yaitu pulpen, AC, dan kursi. Masing-masing dari item tersebut memiliki field name, description, category, date added, dan amount

        - Membuat akun pengguna dengan username miaw@ui yang terdiri atas 3 data item, yaitu pensil, lampu, dan meja. Masing-masing dari item tersebut memiliki field name, description, category, date added, dan amount
                
    >> Menghubungkan model Item dengan User

        - Membuka models.py pada subdirektori main

        - Melakukan import User
        
        - Menambahkan user = models.ForeignKey(User, on_delete=models.CASCADE) pada model Item yang sudah dibuat sebelumnya

        - Membuka views.py pada subdirektori main

        - Mengubah fungsi create_new_product dengan menambahkan commit=False untuk dilakukan proses otorisasai sehingga data yang disimpan pada database sudah sesuai dan spesifik untuk user tertentu

    >> Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi

        - Membuka views.py pada subdirektori main

        - Melakukan import datetime, HttpResponseRedirect, dan reverse

        - Melakukan modifikasi pada fungsi login_user dengan mengganti kode pada block if User is Not None menjadi
            if user is not None:
                login(request, user)
                response = HttpResponseRedirect(reverse("main:show_main"))
                response.set_cookie('last_login', str(datetime.datetime.now())) --> untuk membuat cookie last_login yang akan menampilkan last login beserta waktunya dan menambahkan ke dalam response
                return response

        - Mengubah fungsi show_main dengan menambahkan 'last_login': request.COOKIES['last_login'] untuk menambahkan informasi cookie last_login

        - Menambahkan fungsi logout_user dengan response.delete_cookie('last_login') untuk menghapus cookie apabila user telah melakukan logout

        - Membuka berkas.html pada subdirektori main

        - Menambahkan <h5>Last login session: {{ last_login }}</h5> untuk menampilkan data last_login
        
    >> Menjawab beberapa pertanyaan berikut pada README.md pada root folder

        - Menjawab pertanyaan dan menjelaskan implementasi checklist pada file README.md

# Tugas 5
# Jawaban Pertanyaan
1. **Manfaat element selector CSS dan waktu yang tepat untuk menggunakannya**
    >> Element selector
        Manfaat dari element selector adalah ketika ingin menargetkan semua elemen dengan jenis yang sama di halaman web. Manfaatnya adalah memungkinkan  untuk menerapkan design umum pada semua elemen tersebut. Contohnya adalah menggunakan element selector untuk mengubah gaya semua elemen <p> (paragraf) di halaman web. Penggunaan element selector cocok ketika ingin menerapkan design atau gaya yang sama pada banyak elemen.
    
    >> Class selector
        Manfaat dari class selector adalah memungkinkan untuk melakukan pengelompokkan elemen-elemen dengan karakteristik yang sama dan memberikan design atau gaya yang sama. Selain itu, class selector memungkinkan untuk menggunakan gaya yang sama pada beberapa elemen dalam halaman yang berbeda. Ini membuat kode CSS lebih efisien dan memudahkan dalam melakukan maintenance. Contohnya adalah class selector untuk memberi gaya khusus kepada elemen-elemen dengan kelas "button" sehingga tombol tersebut memiliki tampilan tombol yang seragam. Penggunaan class selector cocok ketika ingin menggunakan selector yang sama lebih dari satu kali di dalam suatu halaman.

    >> ID Selector
        Manfaat utama ID selector adalah kemampuannya untuk mengidentifikasi elemen secara unik di halaman web. Ini berguna jika ingin memberikan gaya atau interaksi yang sangat khusus pada satu elemen tertentu. Elemen yang diidentifikasi oleh ID selector memiliki prioritas yang lebih tinggi daripada selector lainnya. ID selector cocok digunakan untuk mengidentifikasi elemen secara unik dan memberikan gaya atau perilaku khusus pada elemen tersebut.

2. **Jelaskan HTML5 Tag yang kamu ketahui**
    >> <'header'>
        Digunakan untuk menunjukkan bagian atas dari sebuah elemen konten atau halaman. Biasanya berisi judul, logo, atau elemen navigasi.

    >> <'body'>
        Elemen utama yang berisi semua konten yang akan ditampilkan di halaman web, termasuk teks, gambar, tautan, dan elemen-elemen lainnya.

    >> <'button'>
        Membuat tombol yang dapat diklik oleh pengguna. Digunakan untuk memicu tindakan atau peristiwa tertentu saat diklik.

    >> <'div'>
        Elemen yang sering digunakan untuk mengelompokkan dan mengatur konten. Ini adalah elemen blok yang memungkinkan untuk menggabungkan sejumlah elemen dalam satu grup.

    >> <'meta'>
        Digunakan untuk menyisipkan metadata ke dalam dokumen HTML. Metadata ini bisa berisi informasi tentang karakter encoding, deskripsi halaman, kata kunci, dan lain-lain. Biasanya diletakkan dalam bagian <head> dari halaman.

    >> <'table's>
        Digunakan untuk membuat tabel dalam HTML. Tabel ini terdiri atas baris (<tr>), sel (<td> untuk sel data, <th> untuk sel kepala), dan kolom.

3. **Jelaskan perbedaan antara margin dan padding**
    Margin digunakan untuk mengatur jarak antara elemen-elemen dan memengaruhi hubungan antara elemen-elemen tersebut dalam tata letak halaman, sementara padding digunakan untuk mengontrol ruang di dalam elemen dan memengaruhi tampilan dan jarak antara konten elemen dan batasnya.

4. **Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?**
    >> CSS Tailwind
        Tailwind CSS menggunakan kerangka kerja CSS "utility first" yang berarti tailwind memberikan sejumlah utilitas kerja yang dapat digunakan untuk membangun suatu tampilan. Tailwind juga memiliki tingkat kostumisasi ynag sangat tinggi. Tailwind memungkinkan adanya penyesuaian setiap aspek tampilan dengan melakukan edit konfigurasi atau menambahkan kelas khusus. Tailwind biasanya menghasilkan file yang lebih besar karena mencakup semua kelas utilitas yang disediakan. Tailwind memungkinkan adanya kendali terhadap setiap elemen tampilan dan styling yang digunakan saat menentukan styling langsung di markup HTML

    >> CSS Bootstrap
        Bootstrap memiliki pendekatan "component-based" dimana dapat menggunakan beberapa komponen yang telah ada dengan gaya bawaan. Komponen-komponen tersebut dapat digabungkan dalam markup HTML yang telah dibuat. Bootstrap memiliki tema bawaan yang dapat disesuaikan, tetapi seringkali perubahan mendalam memerlukan penyesuaian CSS tambahan. Bootstrap memiliki opsi untuk menyesuaikan komponen yang ingin digunakan, sehingga dapat mengendalikan ukuran file CSS. Bootstrap menyediakan banyak komponen yang siap pakai, yang memudahkan untuk membangun tampilan tanpa perlu menulis banyak kode CSS tambahan.

    >> Kapan menggunakan CSS Tailwind & CSS Bootstrap
        Tailwind cocok digunakan ketika ingin tingkat kustomisasi yang tinggi dan kontrol yang lebih atas styling elemen. Sedangkan bootstrap cocok untuk digunakan ketika ingin cepat membangun tampilan dengan komponen-komponen yang siap untuk digunakan.

5. **Implementasi checklist**
    >> Kustomisasi halaman login, register, dan tambah inventori semenarik mungkin

        - Tampilan login

            Untuk tampilan login saya membingkai beberapa konten dengan menggunakan container. Kemudian saya menggunakan kelas d-flex, justify-content-center, dan align-items-center yang semuanya merupakan kelas Bootstrap untuk memusatkan konten login secara vertikal dan horisontal dalam container. Selain itu, saya juga menggunakan file login_register.css diluar file login untuk menambahkan beberapa styling diluar dari styling default dari Bootstrap

        - Tampilan register

            Untuk tampilan register saya melakukan hal yang serupa dengan yang dilakukan pada tampilan login yaitu dengan membingkai beberapa konten dengan menggunakan container. Kemudian saya menggunakan kelas d-flex, justify-content-center, dan align-items-center yang semuanya merupakan kelas Bootstrap untuk memusatkan konten login secara vertikal dan horisontal dalam container. Selain itu, saya juga menggunakan file login_regsiter.css diluar file login untuk menambahkan beberapa styling diluar dari styling default dari Bootstrap

        - Tampilan tambah inventori

            Untuk tampilan tambah inventori saya membingkai beberapa konten dengan menggunakan container. Kemudian saya menggunakan card untuk menyimpan beberapa konten yang berupa form, seperti name, amount, description, dan category. Selain itu, saya juga menggunakan file create_new_product.css diluar file create_new_product.html untuk menambahkan beberapa styling diluar dari styling default dari Bootstrap.

    >> Kustomisasi halaman daftar inventori menjadi lebih berwarna maupun menggunakan apporach lain seperti menggunakan Card.

        - Tampilan halaman daftar inventori
            
            Untuk tampilan daftar inventori saya menampilkan daftar produk yang dalam format grid. Kemudian dari setiap produk tersebut saya tampilkan dalam bentuk card dengan menambahkan beberapa styling. Selain itu, saya juga menggunakan file inventory_main.css diluar file invetory_main.html untuk menambahkan beberapa styling diluar dari styling default dari Bootstrap.

# Tugas 6
# Jawaban Pertanyaan
1. **Perbedaan antara asynchronus programming dengan synchronus programming**
    >> Asynchronous Programming
        Asynchronous programming adalah sebuah arsitektur non-blocking, yang berarti tidak akan menghentikan eksekusi sebuah program saat satu atau lebih operasi lain sedang berlangsung. Dalam asynchronous programming, beberapa operasi dapat berjalan secara bersamaan tanpa harus menunggu task lainnya diselesaikan terlebih dahulu. Ini sangat berguna dalam kasus seperti pemanggilan API atau operasi I/O yang memakan waktu, karena memungkinkan aplikasi untuk tetap responsif. Salah satu contoh pemrograman aplikasi yang menggunakan asynchronous programming adalah dengan pengembangan aplikasi low-code. Beberapa pengembang dapat bekerja pada proyek secara bersamaan di platform low-code, yang membantu mempercepat proses pembuatan aplikasi.

    >> Synchronous Programming
        Synchronous programming adalah sebuah arsitektur blocking yang berguna untuk pemorgraman dengan sistem reaktif. Sebagai model single-thread, synchronous programming memiliki aturan untuk mengeksekusi operasi secara satu per satu. Saat satu operasi sedang dilakukan, instruksi operasi lainnya diblokir. Penyelesaian tugas pertama akan memicu tugas berikutnya, dan seterusnya. Ini membuat eksekusi kode lebih mudah untuk dipahami dan dikelola, tetapi dapat menyebabkan aplikasi terblokir atau "hang" saat menunggu operasi yang memakan waktu lama untuk selesai.
2. **Paradigma even-driven programming dalam penerapan JavaScript dan AJAX**
    Event-driven programming adalah paradigma di mana alur eksekusi kode ditentukan oleh event atau pesan yang diterima dari sistem eksternal atau user. Dalam konteks JavaScript dan AJAX, hal ini berarti kode dapat merespons event seperti klik mouse, input keyboard, atau respons dari server. Event-driven programming adalah bagian penting dalam pemrograman dengan JavaScript dan AJAX karena memungkinkan aplikasi web untuk lebih interaktif dan responsif. Dengan mengatur event listeners dan callbacks, pengembang JavaScript dapat membuat halaman web yang lebih interaktif dan responsif terhadap masukan pengguna. Contoh dalam implementasi event-driven programming adalah sebuah tombol di halaman web yang, ketika diklik, memicu AJAX request untuk mengambil data dari server dan kemudian menampilkan data tersebut pada halaman web tanpa perlu memuat ulang halaman.
3. **Penerapan Asynchronous Programming pada AJAX**
    Asynchronous Programming pada AJAX memungkinkan JavaScript mengirim permintaan tetapi tidak menunggu respons. JavaScript dapat terus mengeksekusi tugas lain sehingga halaman tetap responsif sementara respons diproses. Permintaan asinkron dapat digunakan dengan mengatur parameter async dalam metode open. Sintaks yang digunakan untuk melakukan hal tersebut adalah

    - request.open(method,url,parameter async);

    Ini memungkinkan pengambilan data dari server dan pembaruan konten halaman web tanpa perlu melakukan refresh halaman. Menggunakan teknik ini, permintaan ke server dapat dikirim, dan kode lain dapat terus berjalan sementara menunggu respons dari server.
4. **Perbandingan antara Fetch API dan jQuery dalam AJAX**
    >> Fetch API 
        Fetch API adalah teknologi native yang hadir di sebagian besar browser modern dan memungkinkan pembuatan request HTTP yang asinkron. Fetch API memberikan kontrol lebih dan lebih fleksibel dibandingkan dengan jQuery.

    >> jQuery
        jQuery adalah library yang lebih tua dan lebih berat yang mencakup berbagai fungsi, termasuk AJAX. jQuery mungkin lebih mudah untuk diimplementasikan oleh pemula, tetapi kurang efisien dan modern dibandingkan dengan Fetch API.
    
    Menurut saya, Fetch API lebih baik karena lebih ringan, modern, dan fleksibel, serta tidak memerlukan dependensi eksternal seperti jQuery. Namun, pilihan antara keduanya juga harus dipertimbangkan berdasarkan kebutuhan proyek dan kompatibilitas browser.

5. **Implementasi Checklist**
    **AJAX GET**

    - Mengganti kode card menjadi <div class="row" id="product_cards"></div> pada file inventory_main.html

    - Menambahkan function pada inventory_main.html
    async function getProducts() {
        return fetch("{% url 'main:get_product_json' %}").then((res) => res.json())
    }
    async function refreshProducts() {
        document.getElementById("product_cards").innerHTML = ""
        const products = await getProducts()
        let htmlString = ""
        products.forEach((item) => {
            htmlString += `
            <div class="col-md-4 mb-4 card-product glass-card">
                <div class="card text-bg-light mb-3">
                    <div class="card-body">
                        <h5 class="card-title">${item.fields.name}</h5>
                        <h6 class="card-subtitle mb-2 text-muted">${item.fields.category}</h6>
                        <p class="card-text">${item.fields.description}</p>
                        <p><strong>Date Added:</strong>${item.fields.date_added}</p>
                        <p><strong>Amount:</strong> ${item.fields.amount}</p>
                        
                        <a href="/add_stock/${item.pk}/" class="btn btn-primary btn-sm">Add Stock</a>
                        <a href="/reduce_stock/${item.pk}/" class="btn btn-warning btn-sm">Reduce Stock</a>
                        <a href="/delete_product/${item.pk}/" class="btn btn-danger btn-sm" onclick="return confirm('Are you sure you want to delete this item?');">Delete Item</a>
                    </div>
                </div>
            </div>`
        })
        document.getElementById("product_cards").innerHTML = htmlString
    }

    refreshProducts()

    - Menambahkan kode pada views.py
    def get_product_json(request):
        product_item = Item.objects.filter(user=request.user)
        return HttpResponse(serializers.serialize('json', product_item))

    **AJAX POST**

    - Menambahkan function pada inventory_main.html
     async function addProduct() {
        await fetch("{% url 'main:add_product_ajax' %}", {
            method: "POST",
            body: new FormData(document.querySelector('#form'))
        })
        refreshProducts()

        document.getElementById("form").reset()
        return false
    }
    document.getElementById("button_add").onclick = addProduct

    - Menambahkan kode pada views.py
    def add_product_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        category = request.POST.get("category")
        user = request.user

        new_product = Item(name=name, amount=amount, description=description, category=category, user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

    **Melakukan perintah collectstatic.**
    
    - Menambahkan pada settings.py
        STATIC_ROOT = os.path.join(BASE_DIR, 'static')