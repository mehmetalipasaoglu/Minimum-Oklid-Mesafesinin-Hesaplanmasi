# Minimum Oklid Mesafesinin Hesaplanması

##import math:
-Matematiksel işlemler, özellikle karekök hesaplama (sqrt) için gerekli modül ekleniyor.

##euclideanDistance Fonksiyonu:
-İki nokta arasındaki Öklid mesafesini hesaplıyor.
-math.sqrt() kullanılarak Öklid mesafesi formülü uygulanıyor.
-Girdi olarak (x, y) biçimindeki iki nokta alıyor ve mesafeyi döndürüyor.

##points Listesi:
-İki boyutlu düzlemdeki noktaların bir listesini tanımlıyor. Buradaki noktalar, mesafe hesaplamasında kullanılacak.

##distances Listesi:
-Hesaplanan mesafelerin saklandığı boş bir liste.

##Çift Döngü ile Mesafelerin Hesaplanması:
-İç içe döngüler, her iki nokta çifti için mesafe hesaplıyor.
-j değişkeni i+1'den başlatılıyor, böylece aynı noktalar arasındaki mesafeler tekrarlı şekilde hesaplanmıyor.

##min() ile Minimum Mesafenin Bulunması:
-distances listesi içindeki en küçük mesafeyi buluyor.

##Sonuç:
-Minimum mesafe print() ile ekrana yazdırılıyor.
