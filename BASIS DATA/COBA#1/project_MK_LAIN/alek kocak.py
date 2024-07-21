from PIL import Image

# Baca gambar dasar
base_image_path = r'C:\Users\BAYU\.vscode\tttt\YURICO.jpg'
base_image = Image.open(base_image_path)

# Baca gambar dengan teks transparan
overlay_image_path = r'C:\Users\BAYU\.vscode\tttt\tulisan.jpg'
overlay_image = Image.open(overlay_image_path)

# Pastikan overlay_image memiliki mode 'RGBA' untuk mendukung transparansi
overlay_image = overlay_image.convert("RGBA")

# Sesuaikan lebar overlay_image dengan lebar base_image
base_width, base_height = base_image.size
overlay_width, overlay_height = overlay_image.size
new_overlay_height = int(base_width * overlay_height / overlay_width)
overlay_image = overlay_image.resize((base_width, new_overlay_height))

# Tentukan posisi overlay di bagian bawah gambar dasar
position = (0, base_height - new_overlay_height)

# Gabungkan kedua gambar
base_image.paste(overlay_image, position, overlay_image)

# Simpan hasilnya
output_path = 'hasil.jpg'  # Ganti dengan path untuk menyimpan gambar hasil
base_image.save(output_path)

print("Gambar berhasil digabungkan dan disimpan di", output_path)
