import random
import itertools
import time

def is_valid_A(A, N):
    if len(A) != 2 * N:
        return False
    
    T = len([x for x in A if x % 2 != 0]) // 2
    C = N - T
    
    if not (T <= 2 * C and C <= 2 * T):
        return False
    
    if not all(2 <= x <= 5 * N for x in A):
        return False
    
    return True

def create_strong_array(N):
    if N >= 100 or N <= 0:
        raise ValueError("N değeri 1 ile 99 arasında olmalıdır.")
    
    print("Oluşturulmaya çalışılıyor...")
    start_time = time.time()

    while True:
        T = random.randint(1, N)
        C = N - T
        if T <= 2 * C and C <= 2 * T:
            break

    possible_odd_numbers = list(range(3, 5 * N + 1, 2))
    possible_even_numbers = list(range(2, 5 * N + 1, 2))

    if len(possible_odd_numbers) < 2 * T or len(possible_even_numbers) < 2 * C:
        raise ValueError("Yeterli sayıda uygun tek veya çift sayı bulunamadı.")

    attempt_counter = 0
    while time.time() - start_time <= 10:
        odd_numbers = random.sample(possible_odd_numbers, 2 * T)
        even_numbers = random.sample(possible_even_numbers, 2 * C)
        
        A = odd_numbers + even_numbers
        random.shuffle(A)
        
        B = [A[i] + (i + 1) for i in range(2 * N)]
        
        odd_count_B = sum(1 for x in B if x % 2 != 0)
        even_count_B = sum(1 for x in B if x % 2 == 0)
        
        if odd_count_B == N and even_count_B == N:
            odd_sum_B = sum(x for x in B if x % 2 != 0)
            total_index_sum = N * (2 * N + 1)
            
            if odd_sum_B == total_index_sum:
                even_sum_B = sum(x for x in B if x % 2 == 0)
                if even_sum_B == sum(A):
                    print("StrongArray başarıyla oluşturuldu.")
                    return A
        
        attempt_counter += 1
        if attempt_counter % 1000 == 0:
            print("Oluşturulmaya çalışılıyor...")

    print("Oluşturulamadı. Program sonlandırıldı.")
    return None

def sartlari_kontrol_et(A):
    N = len(A) // 2
    B = [A[i] + (i + 1) for i in range(2 * N)]
    
    tek_sayilar = [x for x in B if x % 2 != 0]
    cift_sayilar = [x for x in B if x % 2 == 0]
    
    sart_4_1 = (len(tek_sayilar) == N and len(cift_sayilar) == N)
    sart_4_2 = (sum(tek_sayilar) == N * (2 * N + 1) and sum(cift_sayilar) == sum(A))
    
    return sart_4_1, sart_4_2

def istatistikleri_uret(N):
    olasi_degerler = list(range(2, 5 * N + 1))
    permutasyonlar = itertools.permutations(olasi_degerler, 2 * N)
    
    sart_4_1_sayisi = 0
    sart_4_2_sayisi = 0
    her_iki_sart_sayisi = 0
    toplam_permutasyon_sayisi = 0

    start_time = time.time()
    print("İstatistikler üretiliyor...")

    for perm in permutasyonlar:
        sart_4_1, sart_4_2 = sartlari_kontrol_et(perm)
        toplam_permutasyon_sayisi += 1
        if sart_4_1:
            sart_4_1_sayisi += 1
        if sart_4_2:
            sart_4_2_sayisi += 1
        if sart_4_1 and sart_4_2:
            her_iki_sart_sayisi += 1
        
        if toplam_permutasyon_sayisi % 10000 == 0:
            elapsed_time = time.time() - start_time
            print(f"{toplam_permutasyon_sayisi} permutasyon kontrol edildi. Geçen süre: {elapsed_time:.2f} saniye.")
            if elapsed_time >30:
                break

    print(f"İstatistikler üretildi. Toplam süre: {time.time() - start_time:.2f} saniye.")
    print(f"Toplam permutasyon sayısı: {toplam_permutasyon_sayisi}")
    print(f"Şart 4.1'i sağlayan permutasyon sayısı: {sart_4_1_sayisi}")
    print(f"Şart 4.2'yi sağlayan permutasyon sayısı: {sart_4_2_sayisi}")
    print(f"Her iki şartı da sağlayan permutasyon sayısı: {her_iki_sart_sayisi}")

# Örnek kullanım
try:
    N = 5
    
    strong_array = create_strong_array(N)
    if strong_array:
        print("Oluşturulan StrongArray:", strong_array)
        istatistikleri_uret(N)
    else:
        print("StrongArray oluşturulamadı.")
except ValueError as e:
    print(f"Hata: {e}")
