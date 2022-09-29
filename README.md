Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;
https://1.bp.blogspot.com/-u-n0WYPhc3o/X9nFtvNZB-I/AAAAAAAADrE/kD5gMaz4kNQIZyaUcaJJFVpDxdKrfoOwgCLcBGAsYHQ/s602/3.%2BPython%2BDjango%2B-%2BModul%2B2_Page2_Image5.jpg
Alur sebuah permintaan diproses dengan cara permintaan yang diterima dalam server Django nantinya akan diproses oleh urls akan lanjut diproses pada views. Views akan memanggil query ke models dan database juga akan mengembalikan result dari query nya ke dalam views bila terdapat proses yang membutuhkan database. Lalu jika proses permintaan selesai, hasilnya akan dibuat ke HTML yang telah didefinisikan sebelum HTML dikembalikan kepada user.

Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Alasan mengapa kita harus menggunakan virtual environment adalah karena virtual environtment biasanya digunakan untuk project yang menggunakan bahasa python. Sedangkan project berbasis python itu dependent yang berbeda-beda antara satu dengan lainnya, maka butuh virtual environment agar dapat dijalankan tanpa harus mengubah konfigurasi pada sistem operasi yang dipakai. Kita juga tetap bisa membuat aplikasi web berbasis Django walaupun tidak menggunakan virtual environment dan caranya adalah dengan memasang libraries secara global.

Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
Pertama saya buat sebuah fungsi pada folder views.py yang bernama s_katalog utnuk pengambilan data dari model lalu mengembalikan ke dalam sebuah HTML dengan menuliskan return render(request, "katalog.html"). Kedua, saya buat routing yang tujuannya adalah untuk memetakan fungsi yang telah saya buatdi folder view.py tadi. Saya buat routing di urls.py agar nanti halaman HTML dapat berhasil ditampilan melalui browser yang saya buka. Line code yang saya tambahkan adalah path('katalog/', include('katalog.urls')),. Ketiga, saya melakukan pemetaan data yang telah saya dapatkan ke dalam HTML. Pada proses ini saya buka file HTML di templates yang berjudul katalog.html lalu saya isi bagian name dan student id menjadi nama dan npm saya. Kemudian saya lakukan iterasi terhadap variable list_katalog yang telah di render juga ke dalam HTML. Lalu saya add code sebagai berikut : 
<th>{{katalog.item_name}}</th>
        <th>{{katalog.item_price}}</th>
        <th>{{katalog.item_stock}}</th>
        <th>{{katalog.rating}}</th>
        <th>{{katalog.description}}</th>
        <th>{{katalog.item_url}}</th>
Dengan ini data yang saya masukkan ke views akan terlihat pada halaman web. Terakhir pada proses keempat, saya melakukan deployment dengan cara buka web Heroku lalu membuat aplikasi. Setelah itu kita inisiasi git repo pengerjaan kita dengan cara menuliskan git init, heroku git:remot(nama aplikasi heroku), lalu ketik git add,git commit, lalu push ke heroku master. Kemudian dari itu, projek berhasil di deploy.


Jelaskan perbedaan antara JSON, XML, dan HTML! perbedaannya adalah di json tulisan file nya adalah .json sedangkan kalau di xml .xml dan di HTML adalah .html. 
Selain itu di json bisa mengirimkan data dengan cara diuraikan dan dikirimkan melalui internet. Sedangkan di xml karena data nya lebih ter-struktur dan user bisa menggunakan xml untuk menambahkan catatan

Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

https://larastugas.herokuapp.com/mywatchlist/html/