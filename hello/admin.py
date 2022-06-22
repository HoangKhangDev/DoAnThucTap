from django.contrib import admin
from hello.models import Khoa, Lop, SinhVien, PCD, ChiTietPhieuDiem, ThoiGianChamDiem,HoiDongDanhGia, CoVanHocTap
# Register your models here.
<<<<<<< HEAD
admin.site.register(Khoa)
admin.site.register(Lop)
admin.site.register(SinhVien)
admin.site.register(PCD)
admin.site.register(ChiTietPhieuDiem)
admin.site.register(HoiDongDanhGia)
admin.site.register(CoVanHocTap)
admin.site.register(ThoiGianChamDiem)
=======
from .models import Data_ThuatToan, User, Upload_File

admin.site.register(Upload_File)
admin.site.register(Data_ThuatToan)
admin.site.register(User)
>>>>>>> 843860894f1f6e547d14ca5d1c62d731cda7b58f
