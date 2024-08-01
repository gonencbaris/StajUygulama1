import random
import time
import string
import os

# Proje-2'den alınan StrongArray oluşturma fonksiyonu
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

# Proje-5 için test girdileri oluşturma fonksiyonu
def test_girdileri_olustur(adet, min_N, max_N=None):
    if max_N is None:
        max_N = min_N

    if min_N > max_N:
        raise ValueError("Minimum N değeri, maksimum N değerinden büyük olamaz.")

    # Rastgele prefiks oluşturma
    prefiks = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))

    # Dosya yolunu oluşturma
    if not os.path.exists("test_girdileri"):
        os.makedirs("test_girdileri")

    for i in range(1, adet + 1):
        # Rastgele N değeri seçimi
        N = random.randint(min_N, max_N)
        try:
            # StrongArray oluşturma
            strong_array = create_strong_array(N)
            if strong_array:
                # StrongArray dizisini karıştırma
                random.shuffle(strong_array)
                # Dosya adı oluşturma
                dosya_adi = f"test_girdileri/girdi-{prefiks}-{i:03d}.txt"
                # Dosyaya yazma
                with open(dosya_adi, "w") as dosya:
                    dosya.write(str(strong_array))
                if i % 10 == 0:
                    print(f"{i} adet dosya oluşturuldu...")
        except ValueError as e:
            print(f"{i}. girdi oluşturulamadı: {e}")

# Örnek kullanım
test_girdileri_olustur(adet=20, min_N=5, max_N=10)
