class SanPham:
    def __init__(self,ten_san_pham,gia,giam_gia):
        self.__ten_san_pham = ten_san_pham
        self.__gia = gia
        self.__giam_gia = giam_gia
    def get_ten_sp (self):
        return self.__ten_san_pham
    def set_ten_sp (self, ten_san_pham_moi):
        self.__ten_san_pham = ten_san_pham_moi
    def get_gia_sp (self):
        return self.__gia
    def set_gia_sp (self, gia_moi):
        self.__gia = gia_moi
    def get_giam_gia (self):
        return self.__giam_gia
    def set_giam_gia (self, giam_gia_moi):
         self.__giam_gia = giam_gia_moi
    def thue_nhap_khau (self):
        return self.__gia * 0.1
    def nhap_thong_tin_san_pham(self):
        self.set_ten_sp(input('Nhập tên sản phẩm: '))
        self.set_gia_sp(float(input('Nhập giá sản phẩm: ')))
        self.set_giam_gia(float(input('Nhập giảm giá sản phẩm: ')))
    def xuat_thong_tin_san_pham(self):
        print(f'Tên sản phẩm: {self.get_ten_sp()}')
        print(f'Có giá: {self.get_gia_sp()}')
        print(f'Được giảm giá: {self.get_giam_gia()}')
        print(f'Thuế nhập khẩu: {self.thue_nhap_khau()}')
    def __str__(self):
        return (f'Tên sản phẩm: {self.get_ten_sp()}\n'
                f'Có giá: {self.get_gia_sp()}\n'
                f'Được giảm giá: {self.get_giam_gia()}\n'
                f'Thuế nhập khẩu: {self.thue_nhap_khau()}')


