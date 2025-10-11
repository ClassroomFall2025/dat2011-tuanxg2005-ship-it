class SanPham:
    def __init__(self,ten_san_pham,gia,giam_gia):
        self.ten_san_pham = ten_san_pham
        self.gia = gia
        self.giam_gia = giam_gia
    #def doc_giam_gia (self):
    #    return self.giam_gia
    #def ghi_giam_gia (self, giam_gia_moi):
    #    self.giam_gia = giam_gia_moi
    def thue_nhap_khau (self):
        return self.gia * 0.1
    def nhap_thong_tin_san_pham(self):
        self.ten_san_pham = input('Nhập tên sản phẩm: ')
        self.gia = float(input('Nhập giá sản phẩm: '))
        self.giam_gia = float(input('Nhập giảm giá sản phẩm: '))
    def xuat_thong_tin_san_pham(self):
        print(f'Tên sản phẩm: {self.ten_san_pham}')
        print(f'Có giá: {self.gia}')
        print(f'Được giảm giá: {self.giam_gia}')
        print(f'Thuế nhập khẩu: {self.thue_nhap_khau()}')
    def __str__(self):
        return (f'Tên sản phẩm: {self.ten_san_pham}\n'
                f'Có giá: {self.gia}\n'
                f'Được giảm giá: {self.giam_gia}\n'
                f'Thuế nhập khẩu: {self.thue_nhap_khau()}')


