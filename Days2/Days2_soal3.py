if __name__ == '__main__' :
    x = 485
    tahun = x // 360
    sisahari = x % 360
    bulan = sisahari // 30
    sisabulan = sisahari % 30
    minggu = sisabulan // 7
    sisahari2 = sisabulan % 7
    print(f"Tahun {tahun}, Bulan {bulan}, minggu {minggu} Hari {sisahari2}")