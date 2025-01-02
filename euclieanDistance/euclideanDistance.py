import math  # Matematiksel işlemler için gerekli olan 'math' modülü içe aktarılıyor.

# Öklid mesafesini hesaplayan fonksiyon
def euclideanDistance(point1, point2):
    """
    İki nokta (point1 ve point2) arasındaki Öklid mesafesini hesaplar.
    Noktalar (x, y) formatında tuple olarak verilmelidir.
    
    Args:
        point1 (tuple): İlk nokta, örneğin (x1, y1)
        point2 (tuple): İkinci nokta, örneğin (x2, y2)
    
    Returns:
        float: İki nokta arasındaki mesafe
    """
    x1, y1 = point1  # İlk noktanın x ve y koordinatlarını alıyoruz.
    x2, y2 = point2  # İkinci noktanın x ve y koordinatlarını alıyoruz.
    
    # Öklid mesafesi formülünü uyguluyoruz.
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Noktaların tanımlanması
# 2D düzlemdeki noktaları temsil eden bir liste.
points = [(1, 2), (4, 6), (5, 1), (8, 3)]

# Mesafeleri saklayacağımız boş bir liste oluşturuyoruz.
distances = []

# Tüm noktalar arasındaki mesafeleri hesaplamak için iç içe döngü kullanıyoruz.
for i in range(len(points)):  # İlk döngü, points listesindeki her noktayı sırayla seçiyor.
    for j in range(i + 1, len(points)):  # İkinci döngü, seçilen noktadan sonraki diğer noktaları seçiyor.
        """
        Burada, bir noktadan kendisine mesafeyi hesaplamamak için j, i+1'den başlıyor.
        Örneğin, (1, 2) ile (4, 6) mesafesi hesaplanırken, tersine işlem (4, 6) ile (1, 2) tekrar hesaplanmaz.
        """
        
        # İki nokta arasındaki mesafeyi hesaplıyoruz.
        distance = euclideanDistance(points[i], points[j])
        
        # Hesaplanan mesafeyi distances listesine ekliyoruz.
        distances.append(distance)

# Tüm mesafeler hesaplandıktan sonra, en küçük mesafeyi buluyoruz.
min_distance = min(distances)  # Python'un min() fonksiyonunu kullanarak minimum mesafeyi buluyoruz.

# Minimum mesafeyi ekrana yazdırıyoruz.
print("Minimum mesafe:", min_distance)  # Örneğin, "Minimum mesafe: 3.0" şeklinde bir çıktı alınır.
