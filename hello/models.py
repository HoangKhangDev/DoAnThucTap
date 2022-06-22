from tkinter import CASCADE
from tkinter.tix import Tree
from django.db import models
from matplotlib.backend_bases import MouseEvent
# from matplotlib.pyplot import cla


# Create your models here.


class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)


<<<<<<< HEAD
class Khoa(models.Model):
    ID_Khoa = models.CharField(
        primary_key=True, max_length=200, blank=False, null=False)
    Ten_Khoa = models.CharField(max_length=200, blank=False, null=False)
    SDT_Khoa = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return f'{self.ID_Khoa} {self.Ten_Khoa}'


    
class Lop(models.Model):
    Ma_Lop = models.CharField(
        max_length=200, blank=False, null=False, primary_key=True)
    SoLuong_SV = models.IntegerField(blank=False, null=False)
    khoa = models.ForeignKey(Khoa, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.Ma_Lop}'


class CoVanHocTap(models.Model):
    Ma_CVHT = models.CharField(
        max_length=200, blank=False, null=False, primary_key=True)
    Ten_CVHT = models.CharField(max_length=200, blank=True, null=True)
    SDT_CVHT = models.CharField(max_length=10, blank=True, null=True)
    Email_CVHT = models.CharField(max_length=200, blank=True, null=True)
    Password_CVHT = models.CharField(max_length=200, blank=False, null=False)
    lop = models.ForeignKey(Lop, on_delete=models.CASCADE) 
    
class SinhVien(models.Model):
    ChucVu=[
        ('SV','SinhVien'),
        ('BCS','BanCanSu')
    ]
    GioiTinh=[
        ('Nam','Nam'),
        ('Nữ','Nữ')
    ]
    
    Ma_SV = models.IntegerField(primary_key=True, null=False)
    Ten_SV = models.CharField(max_length=200, blank=False, null=False)
    NgaySinh_SV = models.DateField(blank=True, null=True)
    SDT_SV = models.CharField(max_length=10, blank=True, null=True)
    Email_SV = models.EmailField(blank=True, null=True)
    DiaChi_SV = models.CharField(max_length=200, blank=True, null=True)
    Password_SV = models.CharField(max_length=200, blank=False, null=False)
    GioiTinh_SV = models.CharField(
        max_length=200, choices=GioiTinh,blank=True, null=True)
    ChucVu_SV = models.CharField(
        max_length=200, choices=ChucVu)
    Img_SV = models.ImageField(upload_to='',blank=True,null=True)
    lop = models.ForeignKey(Lop, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.Ma_SV} {self.Ten_SV}'


class HoiDongDanhGia(models.Model):
    Ma_HDDG = models.CharField(max_length=200, primary_key=True)
    Img_HDDG = models.ImageField(upload_to='',blank=True,null=True)
    Password_HDDG = models.CharField(max_length=200, blank=False, null=False)


class PCD(models.Model):
    Ma_PCD = models.CharField(primary_key=True, max_length=200)
    NgayLap_PCD = models.DateTimeField(blank=True,null=True)
    XepLoai = models.CharField(blank=True, null=True, max_length=200)
    DiemTong = models.IntegerField(blank=True, null=True)
    HocKy=models.CharField(blank=True, null=True, max_length=1000)
    def __str__(self):
        return f'{self.Ma_PCD}'


class ChiTietPhieuDiem(models.Model):
    Ma_CTPD = models.CharField(max_length=200, primary_key=True)
    DiemTong_SV = models.IntegerField(blank=True, null=True)
    MoTaDiem_SV = models.CharField(blank=True, null=True, max_length=1000)  
    XepLoai_SV=models.CharField(blank=True, null=True, max_length=200)
    DiemTong_HDDG = models.IntegerField(blank=True, null=True)
    MoTaDiem_HDDG = models.CharField(blank=True, null=True, max_length=1000)
    XepLoai_HDDG = models.CharField(blank=True, null=True, max_length=200)
    DiemTong_CVHT = models.IntegerField(blank=True, null=True)
    MoTaDiem_CVHT = models.CharField(blank=True, null=True, max_length=1000)
    XepLoai_CVHT = models.CharField(blank=True, null=True, max_length=200)
    pcd = models.ForeignKey(PCD, on_delete=models.CASCADE)
    sinhvien = models.ForeignKey(
        SinhVien, on_delete=models.CASCADE, blank=True, null=True)
    hoidongdanhgia = models.ForeignKey(
        HoiDongDanhGia, on_delete=models.CASCADE, blank=True, null=True)
    covanhoctap=models.ForeignKey(CoVanHocTap,on_delete=models.CASCADE, blank=True, null=True)

class ThoiGianChamDiem(models.Model):
    HocKy=models.CharField(primary_key=True,max_length=255)
    NgayBatDau = models.DateTimeField(blank=True, null=True)
    NgayKetThuc = models.DateTimeField(blank=True, null=True)
=======
class Upload_File(models.Model):
    Path = models.CharField(max_length=200)
    NameFile = models.CharField(max_length=100)
    Date_Up = models.DateTimeField(auto_now_add=True)
# class ThuatToan_Data(models.Model):
#     TenThuatToan=models.CharField(max_length=50, blank=False)
#     ID_ThuatToan=models.CharField(max_length=50, blank=False)
#     Nu=models.FloatField(blank=False)
#     Gamma=models.FloatField(blank=False)
#     Acc=models.FloatField(blank=False)
#     Path_file=models.ForeignKey(Upload_File,on_delete=models.CASCADE)
class Data_ThuatToan(models.Model):
    TenThuatToan = models.CharField(max_length=50, blank=False)
    ID_ThuatToan = models.CharField(max_length=50, blank=False)
    Nu = models.FloatField(blank=False)
    Gamma = models.FloatField(blank=False)
    Acc = models.FloatField(blank=False)
    Path_file = models.ForeignKey(Upload_File, on_delete=models.CASCADE)
class User(models.Model):
    username=models.CharField(max_length=50,blank=False)
    password=models.CharField(max_length=50,blank=False)
    name=models.CharField(max_length=50,blank=True)
    birthday = models.DateField(null=True, blank=True, auto_now_add=True)
    images=models.ImageField(blank=True)

>>>>>>> 843860894f1f6e547d14ca5d1c62d731cda7b58f
