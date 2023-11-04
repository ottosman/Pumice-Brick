import cv2
import os
import albumentations as A

# Görüntüleri bulunduğu yol
input_folder = r'D:\Desktop2 (D)\QuarkBay\Fabrika-DONE\DATA\ayiklanmis-fabrika-4\saglam\ayiklanmis-fabrika-4-saglam-img\resized_images'

# Yeni görsellerin kaydedileceği yol
output_folder = input_folder+ r'_CLAHE'

# CLAHE dönüşümünü oluştur
transform = A.CLAHE(p=1)

# Yeni klasörü oluştur
os.makedirs(output_folder, exist_ok=True)

# Dosyaları işle
for file_name in os.listdir(input_folder):
    if file_name.lower().endswith(('.jpg', '.JPG', 'jpeg')):
        input_path = os.path.join(input_folder, file_name)
        output_path = os.path.join(output_folder, file_name)
        
        # Görüntüyü yükle ve CLAHE dönüşümünü uygula
        image = cv2.imread(input_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        transformed_image = transform(image=image)['image']
        
        # Sonuçları kaydet
        cv2.imwrite(output_path, cv2.cvtColor(transformed_image, cv2.COLOR_RGB2BGR))

print("CLAHE işlemi tamamlandı.")
