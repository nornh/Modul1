def add (l1,l2):
    c = 0
    hasil =[]
    x , y = 0, 0
    
    while x < int(len(l1)) or y < len(l2) or c:
        jumlah = c
        if x < len(l1):
            jumlah += l1[x]
            x += 1
        if y < len(l2):
            jumlah += l2[y]
            y += 1
        hasil.append(jumlah % 10)
        c = jumlah // 10
    return hasil

if __name__ == "__main__":
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    hasil = add(l1 ,l2)
    
print(hasil)