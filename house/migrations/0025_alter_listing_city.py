# Generated by Django 4.1.3 on 2022-12-18 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0024_alter_listing_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='city',
            field=models.CharField(choices=[('Hà Tĩnh', 'Hà Tĩnh'), ('Tuyên Quang', 'Tuyên Quang'), ('Hải Dương', 'Hải Dương'), ('Thái Nguyên', 'Thái Nguyên'), ('Hải Phòng', 'Hải Phòng'), ('Bạc Liêu', 'Bạc Liêu'), ('Phú Yên', 'Phú Yên'), ('Bắc Ninh', 'Bắc Ninh'), ('Hà Nội', 'Hà Nội'), ('TP. Hồ Chí Minh', 'TP. Hồ Chí Minh'), ('Lạng Sơn', 'Lạng Sơn'), ('Hòa Bình', 'Hòa Bình'), ('Gia Lai', 'Gia Lai'), ('Quảng Ninh', 'Quảng Ninh'), ('Bình Thuận', 'Bình Thuận'), ('Đắk Lắk', 'Đắk Lắk'), ('Trà Vinh', 'Trà Vinh'), ('Hà Giang', 'Hà Giang'), ('Bắc Kạn', 'Bắc Kạn'), ('Quảng Nam', 'Quảng Nam'), ('Thừa Thiên Huế', 'Thừa Thiên Huế'), ('Hậu Giang', 'Hậu Giang'), ('Ninh Bình', 'Ninh Bình'), ('Hà Nam', 'Hà Nam'), ('Bến Tre', 'Bến Tre'), ('Vĩnh Long', 'Vĩnh Long'), ('Khánh Hòa', 'Khánh Hòa'), ('Yên Bái', 'Yên Bái'), ('Phú Thọ', 'Phú Thọ'), ('Thái Bình', 'Thái Bình'), ('Đà Nẵng', 'Đà Nẵng'), ('Lào Cai', 'Lào Cai'), ('Bà Rịa – Vũng Tàu', 'Bà Rịa – Vũng Tàu'), ('An Giang', 'An Giang'), ('Bình Dương', 'Bình Dương'), ('Đồng Nai', 'Đồng Nai'), ('Ninh Thuận', 'Ninh Thuận'), ('Cà Mau', 'Cà Mau'), ('Đắk Nông', 'Đắk Nông'), ('Thanh Hóa', 'Thanh Hóa'), ('Tiền Giang', 'Tiền Giang'), ('Đồng Tháp', 'Đồng Tháp'), ('Sóc Trăng', 'Sóc Trăng'), ('Bình Định', 'Bình Định'), ('Lâm Đồng', 'Lâm Đồng'), ('Quảng Ngãi', 'Quảng Ngãi'), ('Hưng Yên', 'Hưng Yên'), ('Kiên Giang', 'Kiên Giang'), ('Bắc Giang', 'Bắc Giang'), ('Nghệ An', 'Nghệ An'), ('Quảng Trị', 'Quảng Trị'), ('Lai Châu', 'Lai Châu'), ('Điện Biên', 'Điện Biên'), ('Cao Bằng', 'Cao Bằng'), ('Long An', 'Long An'), ('Quảng Bình', 'Quảng Bình'), ('Nam Định', 'Nam Định'), ('Tây Ninh', 'Tây Ninh'), ('Sơn La', 'Sơn La'), ('Kon Tum', 'Kon Tum'), ('Cần Thơ', 'Cần Thơ'), ('Bình Phước', 'Bình Phước'), ('Vĩnh Phúc', 'Vĩnh Phúc')], default='TP. Hồ Chí Minh', max_length=100),
        ),
    ]
