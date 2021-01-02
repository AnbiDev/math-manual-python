def funcPenjumlahan(arr):
    jumlah = 0
    for num in arr:
        jumlah += num
    return jumlah

def funcPanjangArray(arr):
    panjang = 0
    for angg in arr:
        panjang += 1
    return panjang

def funcMedian(arr):
    # cari panjang array
    panjang = funcPanjangArray(arr)
    
    if panjang % 2 == 1:      # jika ganjil
        index = panjang // 2 
    else:                   # jika genap
        index1 = panjang // 2 
        index2 = (panjang // 2) - 1  
        index = (index1 + index2) / 2
    
    # akses anggota meggunakan index median
    median =  arr[int(index)]

    return median

def cariMax(arr):
    terbesar = arr[0]
    for num in arr:
        if num > terbesar:
            terbesar = num
    return terbesar

def cariMin(arr):
    terkecil = arr[0]
    for num in arr:
      if num < terkecil:
        terkecil = num
    return terkecil 