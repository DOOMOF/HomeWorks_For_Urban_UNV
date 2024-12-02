from PIL import Image, ImageFilter

# Открываем изображение
image = Image.open("image.jpg")

# Изменяем размер изображения на 800x600
new_image = image.resize((800, 600))

# Применяем эффект размытия
blurred_image = new_image.filter(ImageFilter.BLUR)

# Сохраняем измененное изображение в формате PNG
blurred_image.save("output_image.png")

print("Изображение успешно обработано и сохранено.")