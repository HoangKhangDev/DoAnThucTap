<<<<<<< HEAD
from base64 import encode
from cmath import e
import codecs
import csv
import io
from django.conf import settings
from django.shortcuts import redirect, render
from django.http import FileResponse, HttpResponse, HttpResponseNotFound
import os
from django.templatetags.static import static
import json
import datetime
import time
from django.core.files.storage import FileSystemStorage
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from fpdf import FPDF


from .models import Greeting, SinhVien, HoiDongDanhGia, PCD, ChiTietPhieuDiem, Lop, Khoa, CoVanHocTap, ThoiGianChamDiem

# Create your views here.


def index(request):
    user = ''
    if('username' in request.session):
        # if(request.session['chucvu'] == 'HDDG'):
        #     user = HoiDongDanhGia.objects.get(
        #         Ma_HDDG=request.session['username'])
        #     if request.session['image'] != '':
        #         return render(request, "index.html", {'hoidongdanhgia': user, 'image': request.session['image']})
        #     else:
        #         return render(request, "index.html", {'hoidongdanhgia': user})
        if request.session['chucvu'] == 'SV':
            user = SinhVien.objects.get(Ma_SV=request.session['username'])
            return render(request, "index.html", {'sinhvien': user, 'image': request.session['image']})
        else:
            # user = CoVanHocTap.objects.get(Ma_CVHT=request.session['username'])
            # if request.session['image'] != '':
            #     return render(request, "index.html", {'covanhoctap': user, 'image': request.session['image']})
            # else:
            #     return render(request, "index.html", {'covanhoctap': user})
            return redirect('/info_score')
    else:
        return redirect('/login')
    # return HttpResponse('Hello from Python!')
=======
import io
from django.shortcuts import redirect, render
from django.http import HttpResponse
import json,os,base64,urllib

from numpy import array

from .models import Greeting
from django.views.decorators.csrf import csrf_protect
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .models import User, Data_ThuatToan, Upload_File
from hello.static.index import Select_Model 
from matplotlib import pyplot as plt


import os
# Create your views here.se


def index(request):
    if('username' in request.session):
        return render(request, 'home.html')
    else:
        return redirect('login')
>>>>>>> 843860894f1f6e547d14ca5d1c62d731cda7b58f


def test(request):

    return render(request, "testpage.html")


<<<<<<< HEAD
    return render(request, "db.html", {"greetings": greetings})


def info_score(request):
    user = ''
    if('username' in request.session):
        if(request.session['chucvu'] == 'HDDG'):
            user = HoiDongDanhGia.objects.get(
                Ma_HDDG=request.session['username'])
            chitietphieudiems = ChiTietPhieuDiem.objects.all()
            phieuchamdiems = PCD.objects.all()
            if request.session['image'] != '':
                return render(request, "info_score.html", {'hoidongdanhgia': user, 'image': request.session['image'], 'chitietphieudiems': chitietphieudiems, "phieuchamdiems": phieuchamdiems, "khoas": Khoa.objects.all(), "lops": Lop.objects.all()})
            else:
                return render(request, "info_score.html", {'hoidongdanhgia': user, 'chitietphieudiems': chitietphieudiems, "phieuchamdiems": phieuchamdiems, "khoas": Khoa.objects.all(), "lops": Lop.objects.all()})
        elif request.session['chucvu'] == 'SV':
            user = SinhVien.objects.get(Ma_SV=request.session['username'])
            chitietphieudiems = ChiTietPhieuDiem.objects.filter(
                sinhvien=user)
            phieuchamdiems = PCD.objects.all()
            print(phieuchamdiems)
            return render(request, "info_score.html", {'sinhvien': user, 'image': request.session['image'], 'chitietphieudiems': chitietphieudiems, "phieuchamdiems": phieuchamdiems})
        else:
            user = CoVanHocTap.objects.get(Ma_CVHT=request.session['username'])
            phieuchamdiems = []
            sinhviens = SinhVien.objects.filter(lop=user.lop)
            for sinhvien in sinhviens:
                ctpds = ChiTietPhieuDiem.objects.filter(
                    sinhvien=sinhvien)
                for i in ctpds:
                    phieuchamdiems.append(i)
            if request.session['image'] != '':
                return render(request, "info_score.html", {'covanhoctap': user, 'image': request.session['image'], "chitietphieudiems": phieuchamdiems, "phieuchamdiems": PCD.objects.all()})
            else:
                return render(request, "info_score.html", {'covanhoctap': user, "chitietphieudiems": phieuchamdiems, "phieuchamdiems": PCD.objects.all()})
    else:
        return redirect('/login')


def score_training(request):
    
    user = ''
    if('username' in request.session):
        if(request.session['chucvu'] == 'HDDG'):
            user = HoiDongDanhGia.objects.get(
                Ma_HDDG=request.session['username'])
            if request.session['image'] != '':
                return render(request, "scoretraining.html", {'hoidongdanhgia': user, 'image': request.session['image']})
            else:
                return render(request, "scoretraining.html", {'hoidongdanhgia': user})
        elif request.session['chucvu'] == 'SV':
            sv = SinhVien.objects.get(Ma_SV=request.session['username'])
            pcds= []
            for i in PCD.objects.all():
                ctpd=ChiTietPhieuDiem.objects.get(pcd=i)
                if ctpd.sinhvien == sv:
                    pcds.append(i)
                    
            check_is_training=True
            
            if "ThoiGianChamDiem" in request.session:
                check_is_training = False
                tgcd = ThoiGianChamDiem.objects.get(
                    HocKy=request.session['ThoiGianChamDiem'])
                for i in pcds:
                    if(tgcd.NgayBatDau <= i.NgayLap_PCD and tgcd.NgayKetThuc >= i.NgayLap_PCD):
                        check_is_training=True
                
                
            user = SinhVien.objects.get(Ma_SV=request.session['username'])
            return render(request, "scoretraining.html", {'sinhvien': user, 'image': request.session['image'], "check_is_training": check_is_training})
        else:
            user = CoVanHocTap.objects.get(Ma_CVHT=request.session['username'])
            if request.session['image'] != '':
                return render(request, "scoretraining.html", {'covanhoctap': user, 'image': request.session['image']})
            else:
                return render(request, "scoretraining.html", {'covanhoctap': user})
    else:
        return redirect('/login')


def view_scoretraining(request, Ma_CTPD):
    user = ''
    chitietphieudiem = ChiTietPhieuDiem.objects.get(Ma_CTPD=Ma_CTPD)
    MoTaDiem_SV = json.loads(chitietphieudiem.MoTaDiem_SV)
    MoTaDiem_CVHT = ''
    MoTaDiem_HDDG = ''
    if(chitietphieudiem.MoTaDiem_CVHT):
        MoTaDiem_CVHT = json.loads(chitietphieudiem.MoTaDiem_CVHT)
    if(chitietphieudiem.MoTaDiem_HDDG):
        MoTaDiem_HDDG = json.loads(chitietphieudiem.MoTaDiem_HDDG)
    if('username' in request.session):
        if(request.session['chucvu'] == 'HDDG'):
            user = HoiDongDanhGia.objects.get(
                Ma_HDDG=request.session['username'])
            if request.session['image'] != '':
                return render(request, "scoretraining.html", {'hoidongdanhgia': user, 'image': request.session['image'], "chitietphieudiem": chitietphieudiem, "chucnang": "view", "MoTaDiem_HDDG": MoTaDiem_HDDG, "MoTaDiem_SV": MoTaDiem_SV, "MoTaDiem_CVHT": MoTaDiem_CVHT, "Ma_CTPD": Ma_CTPD})
            else:
                return render(request, "scoretraining.html", {'hoidongdanhgia': user, "chitietphieudiem": chitietphieudiem, "chucnang": "view", "MoTaDiem_HDDG": MoTaDiem_HDDG, "MoTaDiem_SV": MoTaDiem_SV, "MoTaDiem_CVHT": MoTaDiem_CVHT, "Ma_CTPD": Ma_CTPD})
        elif request.session['chucvu'] == 'SV':
            if(MoTaDiem_HDDG != ''):
                MoTaDiem_SV = MoTaDiem_HDDG
            user = SinhVien.objects.get(Ma_SV=request.session['username'])
            return render(request, "scoretraining.html", {'sinhvien': user, 'image': request.session['image'], "chitietphieudiem": chitietphieudiem, "chucnang": "view", "MoTaDiem_HDDG": MoTaDiem_HDDG, "MoTaDiem_SV": MoTaDiem_SV, "MoTaDiem_CVHT": MoTaDiem_CVHT, "Ma_CTPD": Ma_CTPD})
        else:
            user = CoVanHocTap.objects.get(Ma_CVHT=request.session['username'])
            if request.session['image'] != '':
                return render(request, "scoretraining.html", {'covanhoctap': user, 'image': request.session['image'], "chitietphieudiem": chitietphieudiem, "chucnang": "view", "MoTaDiem_HDDG": MoTaDiem_HDDG, "MoTaDiem_SV": MoTaDiem_SV, "MoTaDiem_CVHT": MoTaDiem_CVHT, "Ma_CTPD": Ma_CTPD})
            else:
                return render(request, "scoretraining.html", {'covanhoctap': user, "chitietphieudiem": chitietphieudiem, "chucnang": "view", "MoTaDiem_HDDG": MoTaDiem_HDDG, "MoTaDiem_SV": MoTaDiem_SV, "MoTaDiem_CVHT": MoTaDiem_CVHT, "Ma_CTPD": Ma_CTPD})
    else:
        return redirect('/login')


def edit_scoretraining(request, Ma_CTPD):
    user = ''
    chitietphieudiem = ChiTietPhieuDiem.objects.get(Ma_CTPD=Ma_CTPD)
    MoTaDiem_SV = json.loads(chitietphieudiem.MoTaDiem_SV)
    MoTaDiem_CVHT = ''
    MoTaDiem_HDDG = ''
    if(chitietphieudiem.MoTaDiem_CVHT):
        MoTaDiem_CVHT = json.loads(chitietphieudiem.MoTaDiem_CVHT)
    if(chitietphieudiem.MoTaDiem_HDDG):
        MoTaDiem_HDDG = json.loads(chitietphieudiem.MoTaDiem_HDDG)

    if('username' in request.session):
        if(request.session['chucvu'] == 'HDDG'):
            user = HoiDongDanhGia.objects.get(
                Ma_HDDG=request.session['username'])
            if request.session['image'] != '':
                return render(request, "scoretraining.html", {'hoidongdanhgia': user, 'image': request.session['image'], "chitietphieudiem": chitietphieudiem, "chucnang": "edit", "MoTaDiem_HDDG": MoTaDiem_HDDG, "MoTaDiem_SV": MoTaDiem_SV, "MoTaDiem_CVHT": MoTaDiem_CVHT, "Ma_CTPD": Ma_CTPD})
            else:
                return render(request, "scoretraining.html", {'hoidongdanhgia': user, "chitietphieudiem": chitietphieudiem, "chucnang": "edit", "MoTaDiem_HDDG": MoTaDiem_HDDG, "MoTaDiem_SV": MoTaDiem_SV, "MoTaDiem_CVHT": MoTaDiem_CVHT, "Ma_CTPD": Ma_CTPD})
        elif request.session['chucvu'] == 'SV':
            user = SinhVien.objects.get(Ma_SV=request.session['username'])
            return render(request, "scoretraining.html", {'sinhvien': user, 'image': request.session['image'], "chitietphieudiem": chitietphieudiem, "chucnang": "view", "MoTaDiem_HDDG": MoTaDiem_HDDG, "MoTaDiem_SV": MoTaDiem_SV, "MoTaDiem_CVHT": MoTaDiem_CVHT, "Ma_CTPD": Ma_CTPD})
        else:
            user = CoVanHocTap.objects.get(Ma_CVHT=request.session['username'])
            if request.session['image'] != '':
                return render(request, "scoretraining.html", {'covanhoctap': user, 'image': request.session['image'], "chitietphieudiem": chitietphieudiem, "chucnang": "edit", "MoTaDiem_HDDG": MoTaDiem_HDDG, "MoTaDiem_SV": MoTaDiem_SV, "MoTaDiem_CVHT": MoTaDiem_CVHT, "Ma_CTPD": Ma_CTPD})
            else:
                return render(request, "scoretraining.html", {'covanhoctap': user, "chitietphieudiem": chitietphieudiem, "chucnang": "edit", "MoTaDiem_HDDG": MoTaDiem_HDDG, "MoTaDiem_SV": MoTaDiem_SV, "MoTaDiem_CVHT": MoTaDiem_CVHT, "Ma_CTPD": Ma_CTPD})
    else:
        return redirect('/login')


def delete_scoretraining(request, Ma_CTPD):
    PCD.objects.get(Ma_PCD=(Ma_CTPD.split('_')[0])).delete()
    return redirect('/info_score')


def add_score(request):
    user = ''
    if(request.method == 'POST'):
        diemTong = 0
        XepLoai = ''
        if ("Ma_CTPD" in request.POST and request.session['chucvu'] == "CVHT"):
            data = json.loads(request.POST['data'])
            ctpd = ChiTietPhieuDiem.objects.get(
                Ma_CTPD=request.POST['Ma_CTPD'])
            ctpd.DiemTong_CVHT = (data[len(data)-2]).split(':')[1]
            ctpd.MoTaDiem_CVHT = request.POST['data']

            XepLoai = (data[len(data)-1]).split(':')[1]
            diemTong = (data[len(data)-2]).split(':')[1]

            ctpd.XepLoai_CVHT = (data[len(data)-1]).split(':')[1]
            ctpd.covanhoctap = CoVanHocTap.objects.get(
                Ma_CVHT=request.session['username'])

        elif ("Ma_CTPD" in request.POST and request.session['chucvu'] == "HDDG"):
            data_1 = json.loads(request.POST['data_sv'])
            data_2 = json.loads(request.POST['data_cvht'])
            data_3 = json.loads(request.POST['data_hddg'])

            ctpd = ChiTietPhieuDiem.objects.get(
                Ma_CTPD=request.POST['Ma_CTPD'])
            ctpd.DiemTong_SV = (data_1[len(data_1)-2]).split(':')[1]
            ctpd.MoTaDiem_SV = request.POST['data_sv']
            ctpd.XepLoai_SV = (data_1[len(data_1)-1]).split(':')[1]
            ctpd.DiemTong_CVHT = (data_2[len(data_2)-2]).split(':')[1]
            ctpd.MoTaDiem_CVHT = request.POST['data_cvht']
            ctpd.XepLoai_CVHT = (data_2[len(data_2)-1]).split(':')[1]
            ctpd.DiemTong_HDDG = (data_3[len(data_3)-2]).split(':')[1]
            ctpd.MoTaDiem_HDDG = request.POST['data_hddg']
            ctpd.XepLoai_HDDG = (data_3[len(data_3)-1]).split(':')[1]

            XepLoai = (data_3[len(data_3)-1]).split(':')[1]
            diemTong = (data_3[len(data_3)-2]).split(':')[1]

            ctpd.hoidongdanhgia = HoiDongDanhGia.objects.get(
                Ma_HDDG=request.session['username'])

        else:
            data = json.loads(request.POST['data'])
            sinhvien = SinhVien.objects.get(Ma_SV=request.session['username'])
            milliseconds = int(round(time.time() * 1000))
            pcd = PCD(Ma_PCD=str(milliseconds),
                      NgayLap_PCD=datetime.datetime.now())
            pcd.save()
        # data = json.loads(request.POST['data'])
            ctpd = ChiTietPhieuDiem(Ma_CTPD=(str(pcd.Ma_PCD)+"_CTPD"),
                                    DiemTong_SV=(
                                        data[len(data)-2]).split(':')[1],
                                    MoTaDiem_SV=request.POST['data'],
                                    XepLoai_SV=(
                                        data[len(data)-1]).split(':')[1],
                                    pcd=pcd, sinhvien=sinhvien)
            XepLoai = (data[len(data)-1]).split(':')[1]
            diemTong = (data[len(data)-2]).split(':')[1]
        pcd = PCD.objects.get(Ma_PCD=ctpd.Ma_CTPD.split("_")[0])
        pcd.XepLoai = XepLoai
        pcd.DiemTong = diemTong
        if(int(diemTong) > 0):
            pcd.save()
        ctpd.save()
        return redirect('/info_score')
    else:
        if('username' in request.session):
            if(request.session['chucvu'] == 'HDDG'):
                user = HoiDongDanhGia.objects.get(
                    Ma_HDDG=request.session['username'])
                return render(request, "scoretraining.html", {'hddg': user})
            else:
                user = SinhVien.objects.get(Ma_SV=request.session['username'])
                return render(request, "scoretraining.html", {'sinhvien': user, 'image': request.session['image']})
        else:
            return redirect('/login')


def search_score(request):
    user = HoiDongDanhGia.objects.get(
        Ma_HDDG=request.session['username'])
    keysearch = request.POST['key_search']
    svs = SinhVien.objects.all()
    arr_sv = []
    phieuchamdiems = PCD.objects.all()
    chitietphieudiems = []
    for i in svs:
        if(keysearch.upper() in i.Ten_SV.upper()):
            arr_sv.append(i)
    if(len(arr_sv) > 0):
        for i in (ChiTietPhieuDiem.objects.all()):
            for j in arr_sv:
                if(i.sinhvien == j):
                    chitietphieudiems.append(i)
    else:
        chitietphieudiems = ChiTietPhieuDiem.objects.all()
    if request.session['image'] != '':
        return render(request, "info_score.html", {'hoidongdanhgia': user, 'image': request.session['image'], 'chitietphieudiems': chitietphieudiems, "phieuchamdiems": phieuchamdiems, "khoas": Khoa.objects.all(), "lops": Lop.objects.all(), "key_search": " của kết quả tìm kiếm : "+keysearch})
    else:
        return render(request, "info_score.html", {'hoidongdanhgia': user, 'chitietphieudiems': chitietphieudiems, "phieuchamdiems": phieuchamdiems, "khoas": Khoa.objects.all(), "lops": Lop.objects.all(), "key_search": " của kết quả tìm kiếm : "+keysearch})


def filter_lop(request, malop):
    user = HoiDongDanhGia.objects.get(
        Ma_HDDG=request.session['username'])
    svs = SinhVien.objects.all()
    arr_sv = []
    phieuchamdiems = PCD.objects.all()
    chitietphieudiems = []
    keysearch = " Lớp "+malop
    for i in svs:
        if(i.lop == Lop.objects.get(Ma_Lop=malop)):
            arr_sv.append(i)
    if(len(arr_sv) > 0):
        for i in (ChiTietPhieuDiem.objects.all()):
            for j in arr_sv:
                if(i.sinhvien == j):
                    chitietphieudiems.append(i)

    if request.session['image'] != '':
        return render(request, "info_score.html", {'hoidongdanhgia': user, 'image': request.session['image'], 'chitietphieudiems': chitietphieudiems, "phieuchamdiems": phieuchamdiems, "khoas": Khoa.objects.all(), "lops": Lop.objects.all(), "key_search": " của "+keysearch})
    else:
        return render(request, "info_score.html", {'hoidongdanhgia': user, 'chitietphieudiems': chitietphieudiems, "phieuchamdiems": phieuchamdiems, "khoas": Khoa.objects.all(), "lops": Lop.objects.all(), "key_search": " của "+keysearch})


def filter(request, keyfilter):
    key_search = keyfilter
    user = HoiDongDanhGia.objects.get(
        Ma_HDDG=request.session['username'])
    phieuchamdiems = PCD.objects.all()
    chitietphieudiems = []

    if(key_search == 'name_az'):
        tukhoa = " Tên a-z"
        chitietphieudiems = ChiTietPhieuDiem.objects.all().order_by('sinhvien')
    elif(key_search == 'name_za'):
        tukhoa = " Tên z-a"
        chitietphieudiems = ChiTietPhieuDiem.objects.all().order_by('-sinhvien')
    elif(key_search == 'id_az'):
        tukhoa = " ID a-z"
        chitietphieudiems = ChiTietPhieuDiem.objects.all().order_by('pcd')
    elif(key_search == 'id_za'):
        tukhoa = " ID z-a"
        chitietphieudiems = ChiTietPhieuDiem.objects.all().order_by('-pcd')
    elif(key_search == 'score_az'):
        tukhoa = " Điểm a-z"
        chitietphieudiems = ChiTietPhieuDiem.objects.all().order_by(
            'DiemTong_HDDG', 'DiemTong_CVHT', 'DiemTong_SV')
    elif(key_search == 'score_za'):
        tukhoa = " Điểm z-a"
        chitietphieudiems = ChiTietPhieuDiem.objects.all().order_by(
            '-DiemTong_HDDG', '-DiemTong_CVHT', '-DiemTong_SV')
    elif(key_search == 'date_az'):
        tukhoa = " Ngày cũ nhất"
        chitietphieudiems = ChiTietPhieuDiem.objects.all().order_by('pcd')
    else:
        tukhoa = " Ngày mới nhất"
        chitietphieudiems = ChiTietPhieuDiem.objects.all().order_by('-pcd')

    # if(len(arr_sv) > 0):
    #     for i in (ChiTietPhieuDiem.objects.all()):
    #         for j in arr_sv:
    #             if(i.sinhvien == j):
    #                 chitietphieudiems.append(i)
    # else:
    # chitietphieudiems = ChiTietPhieuDiem.objects.all()
    if request.session['image'] != '':
        return render(request, "info_score.html", {'hoidongdanhgia': user, 'image': request.session['image'], 'chitietphieudiems': chitietphieudiems, "phieuchamdiems": phieuchamdiems, "khoas": Khoa.objects.all(), "lops": Lop.objects.all(), "key_search": " của "+tukhoa})
    else:
        return render(request, "info_score.html", {'hoidongdanhgia': user, 'chitietphieudiems': chitietphieudiems, "phieuchamdiems": phieuchamdiems, "khoas": Khoa.objects.all(), "lops": Lop.objects.all(), "key_search": " của "+tukhoa})


def contact(request):
    user = ''
    if('username' in request.session):
        if(request.session['chucvu'] == 'HDDG'):
            user = HoiDongDanhGia.objects.get(
                Ma_HDDG=request.session['username'])
            if request.session['image'] != '':
                return render(request, "contact.html", {'hoidongdanhgia': user, 'image': request.session['image']})
            else:
                return render(request, "contact.html", {'hoidongdanhgia': user})
        elif request.session['chucvu'] == 'SV':
            user = SinhVien.objects.get(Ma_SV=request.session['username'])
            return render(request, "contact.html", {'sinhvien': user, 'image': request.session['image']})
        else:
            user = CoVanHocTap.objects.get(Ma_CVHT=request.session['username'])
            if request.session['image'] != '':
                return render(request, "contact.html", {'covanhoctap': user, 'image': request.session['image']})
            else:
                return render(request, "contact.html", {'covanhoctap': user})
    else:
        return redirect('/login')


def info_student(request):
    return render(request, "index.html")
=======
def svm_imoc(request):

    return render(request, "svm_imoc.html")


def login(request):
    if request.method == 'POST':
        username = request.POST["Username"]
        password = request.POST["Password"]
        admin = {
            'username': username,
            'password': password
        }
        request.session['username'] = username
        request.session['password'] = password
        return redirect('home')
    else:
        return render(request, 'login.html', {'users': User.objects.all()})
>>>>>>> 843860894f1f6e547d14ca5d1c62d731cda7b58f


def logout(request):
    request.session.flush()
    return redirect('/')


<<<<<<< HEAD
def login(request):
    thoigianchamdiem=ThoiGianChamDiem.objects.all()
    now = datetime.datetime.now()
    for i in thoigianchamdiem:
        if(i.NgayBatDau <= now and i.NgayKetThuc >= now):
            request.session['ThoiGianChamDiem']=i.HocKy

    sinhviens = SinhVien.objects.all()
    hoidongdanhgias = HoiDongDanhGia.objects.all()
    covanhoctaps = CoVanHocTap.objects.all()
    if(request.method == "POST"):
        request.session['username'] = request.POST['username']
        request.session['chucvu'] = request.POST['chucvu']
        if request.POST['img'] == "":
            request.session['image'] = ""
        else:
            request.session['image'] = '/media/' + request.POST['img']
        request.session['password'] = request.POST['password']
        return redirect('/')
    else:
        return render(request, "login.html", {"sinhviens": sinhviens, "hoidongdanhgias": hoidongdanhgias, 'covanhoctaps': covanhoctaps})


def change_password(request):
    if(request.method == 'POST'):
        if(request.session['chucvu'] == 'SV'):
            sinhvien = SinhVien.objects.get(Ma_SV=request.session['username'])
            sinhvien.Password_SV = request.POST['password']
            sinhvien.save()
            return redirect(request.POST['link'])
        if(request.session['chucvu'] == 'CVHT'):
            covanhoctap = CoVanHocTap.objects.get(
                Ma_CVHT=request.session['username'])
            covanhoctap.Password_CVHT = request.POST['password']
            covanhoctap.save()
            return redirect(request.POST['link'])
        if(request.session['chucvu'] == 'SV'):
            hoidongdanhgia = HoiDongDanhGia.objects.get(
                Ma_HDDG=request.session['username'])
            hoidongdanhgia.Password_HDDG = request.POST['password']
            hoidongdanhgia.save()
            return redirect(request.POST['link'])


def export_to_csv(request):
    data = json.loads(request.POST['data'])
    reponse = HttpResponse(content_type='text/csv')
    reponse.write(u'\ufeff'.encode('utf8'))

    writer = csv.writer(reponse)
    writer.writerow(["Mã Phiếu Điểm", "Sinh Viên", "Ngày Lập Phiếu",
                    "Điểm Sinh Viên", "Điểm Cố Vấn", "Điểm Hội Đồng", "Xếp Loại"])
    for i in data:
        pcd = PCD.objects.get(Ma_PCD=i)
        ctpd = ChiTietPhieuDiem.objects.get(pcd=pcd)
        writer.writerow([i, ctpd.sinhvien, pcd.NgayLap_PCD, ctpd.DiemTong_SV,
                         ctpd.DiemTong_CVHT, ctpd.DiemTong_HDDG, pcd.XepLoai])
    reponse['Content-Disposition'] = f"attachment; filename=InforScore{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}.csv"

    return reponse


def pdf_view(request):
    fs = FileSystemStorage()
    filename = 'mypdf.pdf'
    if fs.exists(filename):
        with fs.open(filename) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
            return response
    else:
        return HttpResponseNotFound('The requested pdf was not found in our server.')
=======
def auth_login(request):
    # if(request.method == 'POST'):
    #     print(request.POST)
    # else:
    return render(request, "login.html")


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'uploadFile/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'pages/simple_upload.html')


def process_test(request):
    if request.method == 'POST':
        # print()
        myfile = request.FILES['file-csv-open']
        fs = FileSystemStorage(settings.MEDIA_ROOT+'/media/')
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        # print(uploaded_file_url)
        array_nu, array_gamma, array_acc, x_ve = Select_Model(
            settings.MEDIA_ROOT+uploaded_file_url, settings.MEDIA_ROOT, int(request.POST['number-cut']), int(request.POST['number-age']), request.POST['select'])
        # plt.figure(figsize=(7,5))
        plt.plot(x_ve, array_acc, marker='o', linestyle='dashed',
                 label=request.POST['select'])
        # plt.plot(array_acc, x_ve,label='and')
        plt.ylabel('Accuracy')
        plt.title(request.POST['select'])
        plt.legend()
        fig=plt.gcf()
        buf=io.BytesIO()
        fig.savefig(buf,format='png')
        buf.seek(0)
        string=base64.b64encode(buf.read())
        plt.close()
        uri=urllib.parse.quote(string)
        array=[]
        for i in range(len(x_ve)):
            array.append({"accuracy":array_acc[i],"numbercut":x_ve[i]})
        return render(request, 'testpage.html', {'img': uri,"array":array})
        # return render(request, 'home.html', {
        #     'uploaded_file_url': uploaded_file_url
        # })
    else:
        return redirect('home')
>>>>>>> 843860894f1f6e547d14ca5d1c62d731cda7b58f
