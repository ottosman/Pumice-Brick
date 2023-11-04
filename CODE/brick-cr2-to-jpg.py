import os
from PIL import Image

# Dosya yolu
input_folder = r"D:\Desktop2 (D)\QuarkBay\Fabrika-DONE\DATA\ayiklanmis-fabrika-4\saglam\ayiklanmis-fabrika-4-saglam-img"
output_folder = os.path.join(input_folder, "JPG")

# Eğer çıktı klasörü yoksa oluştur
os.makedirs(output_folder, exist_ok=True)

# CR2 dosyalarını bul
cr2_files = [f for f in os.listdir(input_folder) if f.endswith(".CR2")]

# Her bir CR2 dosyasını dönüştür
for cr2_file in cr2_files:
    cr2_path = os.path.join(input_folder, cr2_file)
    output_path = os.path.join(output_folder, cr2_file.replace(".CR2", ".jpg"))
    
    # Dönüştürme işlemi
    img = Image.open(cr2_path)
    img.save(output_path, "JPEG")

print("Dönüştürme tamamlandı.")
