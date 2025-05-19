import os
from PIL import Image, ImageDraw, ImageFont
import random

# Sử dụng font viết tay
font = ImageFont.truetype('D:/Loc2023-2024/brittany_signature/BrittanySignature.ttf', 80)  # Đảm bảo đường dẫn đúng

# Danh sách chữ số
digits = list(range(10))  # 0-9

# Màu sắc, định dạng file và ánh xạ định dạng chuẩn cho Pillow
colors = {
    "blue": {"color": (0, 0, 255), "ext": "jpg", "prefix": "B", "format": "JPEG"},
    "red": {"color": (255, 0, 0), "ext": "png", "prefix": "R", "format": "PNG"}
}

# Tạo 100 ảnh (10 số × 10 ảnh mỗi số)
for digit in digits:
    for color_key, color_info in colors.items():
        for i in range(1, 6):  # Tạo 5 ảnh cho mỗi màu
            # Tạo ảnh mới: nền trắng, kích thước 100x100
            img = Image.new("RGB", (100, 100), (255, 255, 255))
            draw = ImageDraw.Draw(img)

            # Vẽ chữ số (thêm ngẫu nhiên để mô phỏng viết tay)
            x = random.randint(20, 30)
            y = random.randint(10, 20)
            draw.text((x, y), str(digit), font=font, fill=color_info["color"])

            # Định dạng tên file: [số]_[prefix]_[001-005].[ext]
            filename = f"{digit}_{color_info['prefix']}_{i:03d}.{color_info['ext']}"
            # filepath = os.path.join(output_dir, filename)

            # Lưu ảnh với định dạng chuẩn
            img.save(filename, color_info["format"])

print(f"Đã tạo 100 ảnh trong thư mục ")