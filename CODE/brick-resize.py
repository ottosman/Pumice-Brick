from PIL import Image
import os

# Görüntülerin bulunduğu klasör yolu
input_folder = r"D:\Desktop2 (D)\QuarkBay\Fabrika-DONE\DATA\ayiklanmis-fabrika-4\saglam\ayiklanmis-fabrika-4-saglam-img\JPG"
# Yeni boyutlar
new_width = 1296
new_height = 864

# Yeni klasörü oluştur
output_folder = os.path.join(input_folder, "resized_images")
os.makedirs(output_folder, exist_ok=True)

# Görüntüleri boyutlandır ve yeni klasöre kaydet
for filename in os.listdir(input_folder):
    if filename.endswith(".JPG") or filename.endswith(".jpg") :
        input_image_path = os.path.join(input_folder, filename)
        output_image_path = os.path.join(output_folder, f"resized_{new_width}x{new_height}_{filename}")
        
        image = Image.open(input_image_path)
        resized_image = image.resize((new_width, new_height), Image.BILINEAR)
        resized_image.save(output_image_path)

print("Görüntüler başarıyla boyutlandırıldı ve yeni klasöre kaydedildi.")
