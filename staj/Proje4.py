import itertools
import time

def sartlari_kontrol_et(A):
    N = len(A) // 2
    B = [A[i] + (i + 1) for i in range(2 * N)]
    
    tek_sayilar = [x for x in B if x % 2 != 0]
    cift_sayilar = [x for x in B if x % 2 == 0]
    
    sart_4_1 = (len(tek_sayilar) == N and len(cift_sayilar) == N)
    sart_4_2 = (sum(tek_sayilar) == N * (2 * N + 1) and sum(cift_sayilar) == sum(A))
    
    return sart_4_1, sart_4_2

def dizi_siralamasi(A, max_sure=20):
    N = len(A) // 2
    permutasyonlar = itertools.permutations(A)
    
    start_time = time.time()
    kontrol_edilen_permutasyon_sayisi = 0

    for perm in permutasyonlar:
        sart_4_1, sart_4_2 = sartlari_kontrol_et(perm)
        kontrol_edilen_permutasyon_sayisi += 1
        
        if kontrol_edilen_permutasyon_sayisi % 1000 == 0:
            print(f"{kontrol_edilen_permutasyon_sayisi} permutasyon kontrol edildi...")
        
        if sart_4_1 and sart_4_2:
            print(f"Toplam {kontrol_edilen_permutasyon_sayisi} permutasyon kontrol edildi.")
            return perm
        
        if time.time() - start_time > max_sure:
            print(f"{max_sure} saniye içinde uygun bir sıralama bulunamadı.")
            return None

    print(f"Toplam {kontrol_edilen_permutasyon_sayisi} permutasyon kontrol edildi.")
    return None


A = [14, 12, 20, 2, 3, 11, 4, 21, 10, 25]

result = dizi_siralamasi(A)
if result:
    print("StrongArray için uygun sıralama bulundu:", result)
else:
    print("Bu diziyi StrongArray yapacak bir sıralama mümkün değil.")
