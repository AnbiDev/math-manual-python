import variabel as var
import library as lib

def main():
    listku = list(map(int, input().split(" ")))

    var.jumlah = lib.funcPenjumlahan(listku)
    var.rata_rata = lib.funcPenjumlahan(listku) / lib.funcPanjangArray(listku)
    var.nilai_tengah = lib.funcMedian(listku)
    var.terbesar = lib.cariMax(listku)
    var.terkecil = lib.cariMin(listku)

    print(var.jumlah)
    print(var.rata_rata)
    print(var.nilai_tengah)
    print(var.terbesar)
    print(var.terkecil)

if __name__ == "__main__":
    main()