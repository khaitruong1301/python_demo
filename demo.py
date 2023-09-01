import pygame
import sys
import random

pygame.init()

# Khởi tạo cửa sổ game
man_hinh = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Trò Chơi Bắn Máy Bay Cải Tiến")

# Tạo máy bay
khoang_man_hinh = man_hinh.get_width()
chieu_rong_may_bay = 50
chieu_cao_may_bay = 50
vi_tri_x_may_bay = (khoang_man_hinh - chieu_rong_may_bay) // 2
vi_tri_y_may_bay = man_hinh.get_height() - chieu_cao_may_bay - 20
toc_do_may_bay = 5

may_bay = pygame.Rect(vi_tri_x_may_bay, vi_tri_y_may_bay, chieu_rong_may_bay, chieu_cao_may_bay)

# Tạo đạn
chieu_rong_dan = 5
chieu_cao_dan = 15
mau_dan = (255, 0, 0)
toc_do_dan = 10
dan = []
doi_tuong_cho_dan = 100  # Thời gian trễ giữa các lần bắn (ms)
thoi_gian_ban_dau = 0

# Tạo thiên thạch
chieu_rong_thien_thach = 30
chieu_cao_thien_thach = 30
mau_thien_thach = (150, 150, 150)
toc_do_thien_thach = 5
thien_thach = []

dong_ho = pygame.time.Clock()

while True:
    for su_kien in pygame.event.get():
        if su_kien.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    phim = pygame.key.get_pressed()
    if phim[pygame.K_LEFT]:
        may_bay.x -= toc_do_may_bay
    if phim[pygame.K_RIGHT]:
        may_bay.x += toc_do_may_bay

    # Bắn đạn
    thoi_gian_hien_tai = pygame.time.get_ticks()
    if phim[pygame.K_SPACE] and thoi_gian_hien_tai - thoi_gian_ban_dau > doi_tuong_cho_dan:
        dan_moi = pygame.Rect(may_bay.x + may_bay.width // 2 - chieu_rong_dan // 2, may_bay.y, chieu_rong_dan, chieu_cao_dan)
        dan.append(dan_moi)
        thoi_gian_ban_dau = thoi_gian_hien_tai

    # Di chuyển đạn
    for dan_moi in dan:
        dan_moi.y -= toc_do_dan
        if dan_moi.y < 0:
            dan.remove(dan_moi)

    # Tạo thiên thạch ngẫu nhiên
    if random.randint(0, 100) < 1:
        x_thien_thach = random.randint(0, khoang_man_hinh - chieu_rong_thien_thach)
        thi_tiet_thach_moi = pygame.Rect(x_thien_thach, 0, chieu_rong_thien_thach, chieu_cao_thien_thach)
        thien_thach.append(thi_tiet_thach_moi)

    # Di chuyển và kiểm tra va chạm thiên thạch
    for thi_tiet_thach_moi in thien_thach:
        thi_tiet_thach_moi.y += toc_do_thien_thach
        if thi_tiet_thach_moi.colliderect(may_bay):
            thien_thach.remove(thi_tiet_thach_moi)
        for dan_moi in dan:
            if thi_tiet_thach_moi.colliderect(dan_moi):
                dan.remove(dan_moi)
                thien_thach.remove(thi_tiet_thach_moi)

    # Di chuyển máy bay bằng chuột
    may_bay.x = pygame.mouse.get_pos()[0] - may_bay.width // 2

    # Vẽ mọi thứ lên cửa sổ
    man_hinh.fill((255, 255, 255))
    pygame.draw.rect(man_hinh, (0, 0, 255), may_bay)
    for dan_moi in dan:
        pygame.draw.rect(man_hinh, mau_dan, dan_moi)
    for thi_tiet_thach_moi in thien_thach:
        pygame.draw.rect(man_hinh, mau_thien_thach, thi_tiet_thach_moi)

    pygame.display.flip()
    dong_ho.tick(30)
