class SinhVienXLDL(SinhVien):
    def init_(self, ma_sv, ho_ten, diem_mon,lap_trinh):
        self.ma_sv = ma_sv
        self.ho_ten = ho_ten
        self. diem = diem_mon
        self.lap_trinh = lap_trinh

    def xuat_thong_tin_sv(self):
        print(f"Mã SV: {self.ma_sv}, Họ Tên: {self.ho_ten}, Điểm TB: {self. diem}, Lập trình: {self.lap_trinh}")
SV1= SinhVienXLDL("PS45187","Sabini Cavini Sabyn ",10,"Python")
SV1.xuat_thong_tin_sv()

## lớp con kế thừa
class SinhVienUDPM(SinhVien):
    def _init_(self, ma_sv, ho_ten, diem_mon, lap_trinh, mang):
        super() .__init__(ma_sv, ho_ten, diem_mon)
        self.lap_trinh = lap_trinh
        self.mang = mang

    def xuat_thong_tin_sv(self):
        super().xuat_thong_tin_sv()
        print(f"Lap trinh: {self.lap_trinh}, Mang: {self.mang}")