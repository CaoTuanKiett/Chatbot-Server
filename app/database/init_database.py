import sys
import os
# Thêm đường dẫn tới thư mục gốc của dự án
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database.database import SessionLocal
from app.database.models import User, VaiTro, Quyen, ChatBot, TinNhan, NguoiGui, CauHoiNguoiDung, GopY, Truong, DuLieu, Link, TaiLieu, CauHoi, VanBan

# Hàm khởi tạo dữ liệu mẫu
def init_db():
    # Tạo phiên làm việc với cơ sở dữ liệu
    db = SessionLocal()

    # Tạo dữ liệu mẫu cho bảng User
    users = [
        User(ho_ten="Nguyen Van A", ngay_sinh="1990-01-01", gioi_tinh="Nam", chuc_vu="Giáo viên", dia_chi="Hà Nội", email="nguyenvana@example.com", so_dien_thoai="123456789", thoi_gian_tao="2024-01-01", nguoi_tao="admin"),
        User(ho_ten="Tran Thi B", ngay_sinh="1992-05-10", gioi_tinh="Nữ", chuc_vu="Sinh viên", dia_chi="Hồ Chí Minh", email="tranthib@example.com", so_dien_thoai="987654321", thoi_gian_tao="2024-01-01", nguoi_tao="admin"),
        User(ho_ten="Le Minh C", ngay_sinh="1985-07-15", gioi_tinh="Nam", chuc_vu="Cán bộ", dia_chi="Đà Nẵng", email="leminhc@example.com", so_dien_thoai="112233445", thoi_gian_tao="2024-01-01", nguoi_tao="admin"),
        User(ho_ten="Pham Thi D", ngay_sinh="1995-11-30", gioi_tinh="Nữ", chuc_vu="Giảng viên", dia_chi="Hà Nội", email="phamthid@example.com", so_dien_thoai="223344556", thoi_gian_tao="2024-01-01", nguoi_tao="admin"),
        User(ho_ten="Vu Thi E", ngay_sinh="2000-09-10", gioi_tinh="Nữ", chuc_vu="Sinh viên", dia_chi="Hải Phòng", email="vuthie@example.com", so_dien_thoai="334455667", thoi_gian_tao="2024-01-01", nguoi_tao="admin")
    ]
    
    # Tạo dữ liệu mẫu cho bảng VaiTro
    vai_tros = [
        VaiTro(ten_vai_tro="Admin", mo_ta="Quản trị hệ thống", quyen_id=1),
        VaiTro(ten_vai_tro="Giảng viên", mo_ta="Giảng dạy các khóa học", quyen_id=2),
        VaiTro(ten_vai_tro="Sinh viên", mo_ta="Học các khóa học", quyen_id=3),
        VaiTro(ten_vai_tro="Cán bộ", mo_ta="Quản lý các hoạt động", quyen_id=2),
        VaiTro(ten_vai_tro="Khách", mo_ta="Không có quyền truy cập", quyen_id=4)
    ]
    
    # Tạo dữ liệu mẫu cho bảng Quyen
    quyens = [
        Quyen(ten_quyen="Quản trị", mo_ta="Quản lý toàn bộ hệ thống"),
        Quyen(ten_quyen="Quản lý học vụ", mo_ta="Quản lý các hoạt động học vụ"),
        Quyen(ten_quyen="Xem thông tin", mo_ta="Có thể xem nhưng không sửa đổi"),
        Quyen(ten_quyen="Không có quyền", mo_ta="Không có quyền truy cập vào hệ thống"),
        Quyen(ten_quyen="Tùy chỉnh", mo_ta="Có thể thay đổi thông tin và thiết lập")
    ]
    
    # Tạo dữ liệu mẫu cho bảng TinNhan
    tin_nhans = [
        TinNhan(noi_dung="Tin nhắn 1", thoi_gian_gui="2024-01-01 08:00:00", nguoi_gui_id=1),
        TinNhan(noi_dung="Tin nhắn 2", thoi_gian_gui="2024-01-02 09:00:00", nguoi_gui_id=2),
        TinNhan(noi_dung="Tin nhắn 3", thoi_gian_gui="2024-01-03 10:00:00", nguoi_gui_id=3),
        TinNhan(noi_dung="Tin nhắn 4", thoi_gian_gui="2024-01-04 11:00:00", nguoi_gui_id=4),
        TinNhan(noi_dung="Tin nhắn 5", thoi_gian_gui="2024-01-05 12:00:00", nguoi_gui_id=5)
    ]
    
    # Tạo dữ liệu mẫu cho bảng ChatBot
    chat_bots = [
        ChatBot(ten_chat_bot="ChatBot 1", mo_ta="Hỗ trợ sinh viên", token="token123", tin_nhan_id=1, cau_hoi_id=1, du_lieu_id=1, gop_y_id=1),
        ChatBot(ten_chat_bot="ChatBot 2", mo_ta="Hỗ trợ giảng viên", token="token456", tin_nhan_id=2, cau_hoi_id=2, du_lieu_id=2, gop_y_id=2),
        ChatBot(ten_chat_bot="ChatBot 3", mo_ta="Hỗ trợ cán bộ", token="token789", tin_nhan_id=3, cau_hoi_id=3, du_lieu_id=3, gop_y_id=3),
        ChatBot(ten_chat_bot="ChatBot 4", mo_ta="Hỗ trợ khách", token="token101", tin_nhan_id=4, cau_hoi_id=4, du_lieu_id=4, gop_y_id=4),
        ChatBot(ten_chat_bot="ChatBot 5", mo_ta="Hỗ trợ tất cả", token="token112", tin_nhan_id=5, cau_hoi_id=5, du_lieu_id=5, gop_y_id=5)
    ]
    
    # Tạo dữ liệu mẫu cho bảng NguoiGui
    nguoi_guis = [
        NguoiGui(nguoi_gui="Nguyen Van A"),
        NguoiGui(nguoi_gui="Tran Thi B"),
        NguoiGui(nguoi_gui="Le Minh C"),
        NguoiGui(nguoi_gui="Pham Thi D"),
        NguoiGui(nguoi_gui="Vu Thi E")
    ]
    
    # Tạo dữ liệu mẫu cho bảng CauHoiNguoiDung
    cau_hoi_nguoi_dungs = [
        CauHoiNguoiDung(ho_ten="Nguyen Van A", noi_dung="Câu hỏi 1", email="nguyenvana@example.com", trang_thai=True, thoi_gian_gui="2024-01-01"),
        CauHoiNguoiDung(ho_ten="Tran Thi B", noi_dung="Câu hỏi 2", email="tranthib@example.com", trang_thai=False, thoi_gian_gui="2024-01-02"),
        CauHoiNguoiDung(ho_ten="Le Minh C", noi_dung="Câu hỏi 3", email="leminhc@example.com", trang_thai=True, thoi_gian_gui="2024-01-03"),
        CauHoiNguoiDung(ho_ten="Pham Thi D", noi_dung="Câu hỏi 4", email="phamthid@example.com", trang_thai=False, thoi_gian_gui="2024-01-04"),
        CauHoiNguoiDung(ho_ten="Vu Thi E", noi_dung="Câu hỏi 5", email="vuthie@example.com", trang_thai=True, thoi_gian_gui="2024-01-05")
    ]
    
    # Tạo dữ liệu mẫu cho bảng GopY
    gop_ys = [
        GopY(ho_ten="Nguyen Van A", noi_dung="Góp ý 1", email="nguyenvana@example.com", thoi_gian_gui="2024-01-01"),
        GopY(ho_ten="Tran Thi B", noi_dung="Góp ý 2", email="tranthib@example.com", thoi_gian_gui="2024-01-02"),
        GopY(ho_ten="Le Minh C", noi_dung="Góp ý 3", email="leminhc@example.com", thoi_gian_gui="2024-01-03"),
        GopY(ho_ten="Pham Thi D", noi_dung="Góp ý 4", email="phamthid@example.com", thoi_gian_gui="2024-01-04"),
        GopY(ho_ten="Vu Thi E", noi_dung="Góp ý 5", email="vuthie@example.com", thoi_gian_gui="2024-01-05")
    ]

    # Tạo dữ liệu mẫu cho bảng Truong
    truong_list = [
        Truong(
            ten_truong="Trường Đại học Công nghệ Thông tin",
            ma_truong="UDN-IT",
            dia_chi="123 Đại lộ Công Nghệ, Đà Nẵng",
            so_dien_thoai="0236-1234567",
            email="contact@udn.edu.vn",
            website="https://www.udn.edu.vn",
            nguoi_dung_id=1,
            chat_bot_id=1,
            thoi_gian_tao=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ),
        Truong(
            ten_truong="Trường Đại học Bách Khoa Hà Nội",
            ma_truong="HUST",
            dia_chi="1 Đại Cồ Việt, Hà Nội",
            so_dien_thoai="024-38695131",
            email="contact@hust.edu.vn",
            website="https://www.hust.edu.vn",
            nguoi_dung_id=1,
            chat_bot_id=1,
            thoi_gian_tao=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ),
        Truong(
            ten_truong="Trường Đại học Kinh tế Quốc dân",
            ma_truong="NEU",
            dia_chi="207 Giải Phóng, Hà Nội",
            so_dien_thoai="024-37548620",
            email="contact@neu.edu.vn",
            website="https://www.neu.edu.vn",
            nguoi_dung_id=1,
            chat_bot_id=1,
            thoi_gian_tao=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ),
        Truong(
            ten_truong="Trường Đại học Sư phạm Hà Nội",
            ma_truong="HUPT",
            dia_chi="136 Xuân Thủy, Hà Nội",
            so_dien_thoai="024-37548596",
            email="contact@hup.edu.vn",
            website="https://www.hup.edu.vn",
            nguoi_dung_id=1,
            chat_bot_id=1,
            thoi_gian_tao=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ),
        Truong(
            ten_truong="Trường Đại học Ngoại thương",
            ma_truong="FTU",
            dia_chi="91 Chùa Láng, Hà Nội",
            so_dien_thoai="024-37541517",
            email="contact@ftu.edu.vn",
            website="https://www.ftu.edu.vn",
            nguoi_dung_id=1,
            chat_bot_id=1,
            thoi_gian_tao=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ),
    ]
    
    # Lặp qua và thêm dữ liệu vào cơ sở dữ liệu
    db.add_all(vai_tros + quyens + users + nguoi_guis + tin_nhans + chat_bots + cau_hoi_nguoi_dungs + gop_ys)
    db.flush()  # Ghi tạm vào DB để kiểm tra dữ liệu
    db.commit()

    print("Dữ liệu mẫu đã được thêm thành công!")

    # Đóng kết nối
    db.close()


# Gọi hàm init_db để khởi tạo dữ liệu
if __name__ == "__main__":
    init_db()
