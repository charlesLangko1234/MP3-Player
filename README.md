# MP3-Player
<h3>Membuat GUI untuk aplikasi pemutar music sederhana</h3>

<p>Dalam project ini dibuat aplikasi pemutar musik sederhana dengan menggunakan bahasa pemograman python. Lalu, dibuat juga GUI sederhana sebagai perantara yang digunakan untuk memudahkan user dalam penggunaan aplikasi ini. Berikut akan dijelaskan cara penggunaannya, beberapa package yang digunakan serta setup awal yang diperlukan untuk menjalankan codingan ini.</p>

<ul>
  <li><a href="#cara">Cara Penggunaannya</a></li>
  <li><a href="#package">Package</a></li>
  <li><a href="setup">Setup awal</a></li>
</ul>  

## Cara Penggunaan
<div id="cara"></div>

<img src="https://github.com/charlesLangko1234/MP3-Player/blob/main/Image/GUI1.png" alt="Rangkaian"/>
  Tampilan utama dari aplikasi pemutar musik yang dibuat adalah seperti pada gambar di atas. Tampilan ini berfungsi untuk menjalankan fungsi pemutaran musik, penambahan musik, mengubah volume musik, dan mempercepat atau memperlambat musik. Kotak hitam yang berada pada tengah tampilan utama, berfungsi untuk menampilkan list musik yang sudah ditambahkan dalam aplikasi. Tampilan yang dibuat masih sederhana, dan juga masih perlu pengembangan pada beberapa bagian lagi agar menjadi lebih menarik.
 

## Package
<div id="package"></div>
  Beberapa package yang digunakan dalam proses pengembangan aplikasi ini adalah :
<ul>
  <li><a href="https://docs.python.org/3/library/tkinter.html">Tkinter</a></li>
  <li><a href="https://www.pygame.org/docs/">Pygame</a></li>
  <li><a>time</a></li>
  <li><a href="https://www.delftstack.com/howto/python/python-play-mp3/">MP3</a></li>
</ul>

## Setup Awal
<div id="setup"></div>

Sebelum menggunakan code, install terlebih dahulu package diatas dengan code berikut :
<pre>
$ pip install tkinter
$ pip install pygame
$ pip install mutagen
</pre>

Setelah itu, ubah lah soruce code berikut dengan penyimpanan yang telah kalian buat :
<pre>
song = f'D:/Coding/Python/Tkinter/Song/{song}'
</pre>
