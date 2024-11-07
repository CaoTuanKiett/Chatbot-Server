# models.py
from sqlalchemy import Column, Integer, String, Boolean, LargeBinary, ForeignKey
from app.database.database import Base

class User(Base):
    __tablename__ = "nguoi_dung"

    id_nguoi_dung = Column(Integer, primary_key=True, index=True)
    ho_ten = Column(String(100), index=True)
    ngay_sinh = Column(String(100), index=True)
    gioi_tinh = Column(String(100), index=True)
    chuc_vu = Column(String(100), index=True)
    dia_chi = Column(String(100), index=True)
    email = Column(String(100), unique=True, index=True)
    so_dien_thoai = Column(String(100), index=True)
    thoi_gian_tao = Column(String(100), index=True)
    nguoi_tao = Column(String(100), index=True)
    vai_tro_id = Column(Integer, ForeignKey("vai_tro.id_vai_tro") ,index=True)

class VaiTro(Base):
    __tablename__ = "vai_tro"

    id_vai_tro = Column(Integer, primary_key=True, index=True)
    ten_vai_tro = Column(String(100), index=True)
    mo_ta = Column(String(100), index=True)
    quyen_id = Column(Integer, ForeignKey("quyen.id_quyen") ,index=True)

class Quyen(Base):
    __tablename__ = "quyen"

    id_quyen = Column(Integer, primary_key=True, index=True)
    ten_quyen = Column(String(100), index=True)
    mo_ta = Column(String(100), index=True)

class ChatBot(Base):
    __tablename__ = "chat_bot"

    id_chat_bot = Column(Integer, primary_key=True, index=True)
    ten_chat_bot = Column(String(100), index=True)
    mo_ta = Column(String(100), index=True)
    token = Column(String(100), index=True)
    tin_nhan_id = Column(Integer, ForeignKey("tin_nhan.id_tin_nhan") ,index=True)
    cau_hoi_id = Column(Integer, ForeignKey("cau_hoi_nguoi_dung.id_cau_hoi") ,index=True)
    du_lieu_id = Column(Integer, ForeignKey("du_lieu.id_du_lieu") ,index=True)
    gop_y_id = Column(Integer, ForeignKey("gop_y.id_gop_y") ,index=True)

class TinNhan(Base):
    __tablename__ = "tin_nhan"

    id_tin_nhan = Column(Integer, primary_key=True, index=True)
    noi_dung = Column(String(100), index=True)
    thoi_gian_gui = Column(String(100), index=True)
    nguoi_gui_id = Column(Integer, ForeignKey("nguoi_gui.id_nguoi_gui") ,index=True)

class NguoiGui(Base):
    __tablename__ = "nguoi_gui"

    id_nguoi_gui = Column(Integer, primary_key=True, index=True)
    nguoi_gui = Column(String(100), index=True)

class CauHoiNguoiDung(Base):
    __tablename__ = "cau_hoi_nguoi_dung"

    id_cau_hoi = Column(Integer, primary_key=True, index=True)
    ho_ten = Column(String(100), index=True)
    noi_dung = Column(String(100), index=True)
    email = Column(String(100), index=True)
    trang_thai = Column(Boolean, index=True)
    thoi_gian_gui = Column(String(100), index=True)

class GopY(Base):
    __tablename__ = "gop_y"

    id_gop_y = Column(Integer, primary_key=True, index=True)
    ho_ten = Column(String(100), index=True)
    noi_dung = Column(String(100), index=True)
    email = Column(String(100), index=True)
    thoi_gian_gui = Column(String(100), index=True)

class Truong(Base):
    __tablename__ = "truong"

    id_truong = Column(Integer, primary_key=True, index=True)
    ten_truong = Column(String(100), index=True)
    ma_truong = Column(String(100), index=True)
    dia_chi = Column(String(100), index=True)
    so_dien_thoai = Column(String(100), index=True)
    email = Column(String(100), index=True)
    website = Column(String(100), index=True)
    nguoi_dung_id = Column(Integer, ForeignKey("nguoi_dung.id_nguoi_dung") ,index=True)
    chat_bot_id = Column(Integer, ForeignKey("chat_bot.id_chat_bot") ,index=True)
    thoi_gian_tao = Column(String(100), index=True)

class DuLieu(Base):
    __tablename__ = "du_lieu"

    id_du_lieu = Column(Integer, primary_key=True, index=True)
    link_id = Column(Integer, ForeignKey("link.id_link") ,index=True)
    tai_lieu_id = Column(Integer, ForeignKey("tai_lieu.id_tai_lieu") ,index=True)
    cau_hoi_id = Column(Integer, ForeignKey("cau_hoi.id_cau_hoi") ,index=True)
    van_ban_id = Column(Integer, ForeignKey("van_ban.id_van_ban") ,index=True)

class Link(Base):
    __tablename__ = "link"

    id_link = Column(Integer, primary_key=True, index=True)
    link = Column(String(100), index=True)
    thoi_gian_tao = Column(String(100), index=True)
    nguoi_tao = Column(String(100), index=True)

class TaiLieu(Base):
    __tablename__ = "tai_lieu"

    id_tai_lieu = Column(Integer, primary_key=True, index=True)
    ten_tai_lieu = Column(String(100), index=True)
    loai_tai_lieu = Column(String(100), index=True)
    kich_thuoc = Column(String(100), index=True)
    du_lieu = Column(LargeBinary, nullable=False)

class CauHoi(Base):
    __tablename__ = "cau_hoi"

    id_cau_hoi = Column(Integer, primary_key=True, index=True)
    cau_hoi = Column(String(100), index=True)
    cau_tra_loi = Column(String(100), index=True)
    thoi_gian_tao = Column(String(100), index=True)
    nguoi_tao = Column(String(100), index=True)

class VanBan(Base):
    __tablename__ = "van_ban"

    id_van_ban = Column(Integer, primary_key=True, index=True)
    noi_dung = Column(String(100), index=True)
    thoi_gian_tao = Column(String(100), index=True)
    nguoi_tao = Column(String(100), index=True)






