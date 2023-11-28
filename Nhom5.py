
class SinhVien:
    def __init__(self, ma_so, ho_ten, lop, khoa, so_tien_da_thanh_toan):
        self.ma_so = ma_so
        self.ho_ten = ho_ten
        self.lop = lop
        self.khoa = khoa
        self.so_tien_da_thanh_toan = so_tien_da_thanh_toan

class ChiSoDienNuoc:
    don_gia_dien = 2200
    don_gia_nuoc = 3000
    def __init__(self, thang, dien_dau, dien_cuoi, nuoc_dau, nuoc_cuoi):
        self.thang = thang
        self.dien_dau = dien_dau
        self.dien_cuoi = dien_cuoi
        self.nuoc_dau = nuoc_dau
        self.nuoc_cuoi = nuoc_cuoi
        self.tien_dien = (dien_cuoi - dien_dau) * ChiSoDienNuoc.don_gia_dien
        self.tien_nuoc = (nuoc_cuoi -nuoc_dau) *  ChiSoDienNuoc.don_gia_nuoc  
# chua xong

    def tinh_tong_tien_dien_nuoc(self):
        return self.tien_dien +self.tien_nuoc

class PhongKyTucXa:
    def __init__(self, ma_phong, vi_tri, co_dieu_hoa, loai_phong, so_luong_giuong, so_luong_nha_ve_sinh, chi_so_dien_nuoc):
        self.ma_phong = ma_phong
        self.vi_tri = vi_tri
        self.co_dieu_hoa = co_dieu_hoa
        self.loai_phong = loai_phong
        self.danh_sach_sv = []
        self.so_luong_giuong = so_luong_giuong
        self.so_luong_nha_ve_sinh = so_luong_nha_ve_sinh
        self.chi_so_dien_nuoc = chi_so_dien_nuoc
        self.tong_tien_can_tra = 0
    def them_sinh_vien(self, sinh_vien):
        if len(self.danh_sach_sv) < self.so_luong_giuong:
            self.danh_sach_sv.append(sinh_vien)
            return True
        return False
    def tinh_tong_tien_phong(self):
        tong_tien_dien_nuoc = self.chi_so_dien_nuoc.tinh_tong_tien_dien_nuoc()
        self.tong_tien_phong = len(self.danh_sach_sv) * 36000
        if self.co_dieu_hoa:
            tong_tien_phong += len(self.danh_sach_sv) * 50000
        self.tong_tien_can_tra = tong_tien_phong + tong_tien_dien_nuoc
        
class QuanLyPhong:
    def __init__(self):
        self.danh_sach_phong = []
    def them_phong(self, phong):
        self.danh_sach_phong.append(phong)
#Them moi phong
def them_moi_phong(self):
    print("\n--- Thêm mới phòng ký túc xá ---")
    ma_phong = input("Nhập mã phòng: ")
    vi_tri = input("Nhập vị trí phòng (ví dụ: Tầng 1, Toà A): ")
    co_dieu_hoa = input("Phòng có điều hòa không? (có/không): ")
    loai_phong = input("Loại phòng (nam/nữ): ")
    so_luong_giuong = int(input("Số lượng giường trong phòng: "))
    so_luong_nha_ve_sinh = int(input("Số lượng nhà vệ sinh trong phòng: "))
    thang_hien_tai = input("Nhập tháng hiện tại (MM/YYYY): ")
    dien_dau = float(input("Nhập chỉ số điện đầu tháng: "))
    dien_cuoi = float(input("Nhập chỉ số điện cuối tháng: "))
    nuoc_dau = float(input("Nhập chỉ số nước đầu tháng: "))
    nuoc_cuoi = float(input("Nhập chỉ số nước cuối tháng: "))
    chi_so_dien_nuoc = ChiSoDienNuoc(thang_hien_tai, dien_dau, dien_cuoi, nuoc_dau, nuoc_cuoi)
    phong_moi = PhongKyTucXa(ma_phong, vi_tri, co_dieu_hoa.lower() == 'có', loai_phong, so_luong_giuong, so_luong_nha_ve_sinh)
    self.quan_ly_phong.them_phong(phong_moi)
    print("Đã thêm phòng mới thành công")

#Hien thi danh sach phong
def hien_thi_danh_sach_phong_theo_tong_tien(self):
    print("\n--- Danh sách phòng theo tổng tiền cần trả ---")
    print("1. Sắp xếp từ cao xuống thấp")
    print("2. Sắp xếp từ thấp lên cao")
    choice = input("Chọn cách sắp xếp: ")
    if choice == '1':
    # Sắp xếp từ cao xuống thấp
        self.quan_ly_phong.danh_sach_phong.sort(key=lambda x: x.tong_tien_can_tra, reverse=True)
    elif choice == '2':
    # Sắp xếp từ thấp lên cao
        self.quan_ly_phong.danh_sach_phong.sort(key=lambda x: x.tong_tien_can_tra)
    else:
        print("Lựa chọn không hợp lệ.")
        return
    # Hiển thị danh sách phòng đã sắp xếp
    for i, phong in enumerate(self.quan_ly_phong.danh_sach_phong):
        print(f"{i+1}. Mã phòng: {phong.ma_phong}, Tổng tiền cần trả: {phong.tong_tien_can_tra}")

def danh_sach_phong_co_the_them_nguoi(self):
    print("\n--- Danh sách phòng có thể thêm người vào ở ---")
    phong_co_the_them = []
    for phong in self.quan_ly_phong.danh_sach_phong:
        if len(phong.danh_sach_sv) < phong.so_luong_giuong:
            phong_co_the_them.append(phong)
    if not phong_co_the_them:
        print("Không có phòng nào có thể thêm người vào ở.")
        return
        # Hiển thị danh sách các phòng có thể thêm người
    for i, phong in enumerate(phong_co_the_them):
        print(f"{i+1}. Mã phòng: {phong.ma_phong}, Số lượng người hiện tại: {len(phong.danh_sach_sv)}/{phong.so_luong_giuong}")

def danh_sach_phong_con_no(self):
    print("\n--- Danh sách phòng còn nợ tiền ban quản lý ---")
    phong_con_no = []
    for phong in self.quan_ly_phong.danh_sach_phong:
        if phong.tong_tien_can_tra > phong.tong_tien_da_thanh_toan:
            phong_con_no.append(phong)
    if not phong_con_no:
        print("Không có phòng nào còn nợ tiền ban quản lý.")
        return
    for i, phong in enumerate(phong_con_no):
        print(f"{i+1}. Mã phòng: {phong.ma_phong}, Tổng tiền cần trả: {phong.tong_tien_can_tra}, "f"Tổng tiền đã thanh toán: {phong.tong_tien_da_thanh_toan}, Tiền còn nợ: {phong.tong_tien_can_tra - phong.tong_tien_da_thanh_toan}")

def them_sinh_vien_vao_phong(self):
    print("\n--- Thêm sinh viên vào phòng ---")
    ma_phong = input("Nhập mã phòng muốn thêm sinh viên:")
    phong_can_them = None
    for phong in self.quan_ly_phong.danh_sach_phong:
        if phong.ma_phong == ma_phong:
            phong_can_them = phong
            break
    if phong_can_them is None:
        print(f"Không tìm thấy phòng có mã {ma_phong}.")
        return
    if len(phong_can_them.danh_sach_sv) >= phong_can_them.so_luong_giuong:
        print("Phòng đã đầy, không thể thêm sinh viên vào.")
        return
    #Nhập thông tin sinh viên
    ma_sinh_vien = input("Nhập mã số sinh viên: ")
    ho_ten = input("Nhập họ tên sinh viên: ")
    gioi_tinh = input("Nhập giới tính sinh viên: ")
    lop = input("Nhập lớp sinh viên: ")
    khoa = input("Nhập khoa của sinh viên: ")
    tien_thanh_toan = float(input("Nhập số tiền đã thanh toán của sinh viên: ")) 
    # tạo đối tượng
    sinh_vien = SinhVien(ma_sinh_vien, ho_ten, gioi_tinh, lop, khoa, tien_thanh_toan)
#Menu
class Main:
    def __init__(self):
        self.quan_ly_phong = QuanLyPhong()
    def run(self):
        while True:
            print("\n--- Quản lý phòng ký túc xá ---")
            print("1. Thêm mới phòng ký túc xá")
            print("2. Hiển thị danh sách phòng theo tổng tiền cần trả")
            print("3. Hiển thị danh sách phòng có thể thêm người vào ở")
            print("4. Hiển thị danh sách phòng còn nợ tiền ban quản lý")
            print("5. Thêm sinh viên vào phòng")
            print("6. Tìm kiếm phòng ký túc xá")
            print("7. Sửa thông tin phòng")
            print("8. Xoá phòng ký túc xá")
            print("9. Thoát chương trình")
            choice = input("Nhap lua chon cua ban: ")

            if choice == '1':
                self.them_moi_phong()
            elif choice == '2':
                self.hien_thi_danh_sach_phong_theo_tong_tien()
            elif choice == '3':
                self.danh_sach_phong_co_the_them_nguoi()
            elif choice == '4':
                self.danh_sach_phong_con_no()
            elif choice == '5':
                self.them_sinh_vien_vao_phong()
            elif choice == '6':
                # Tìm kiếm phòng ký túc xá
                pass # Thêm code tương ứng
            elif choice == '7':
                # Sửa thông tin phòng
                pass # Thêm code tương ứng
            elif choice == '8':
                # Xoá phòng
                pass # Thêm code tương ứng
            elif choice == '9':
                print("Thoát chương trình.")
                break
            else:
                ("Lựa chọn không hợp lệ, vui lòng chọn lại!")
    if __name__ == "__main__":
        program = QuanLyPhong()
        program.run()