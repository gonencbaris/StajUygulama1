import random

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
        raise ValueError("N değeri 1 ile 99 arasında olmalıdır!")
    
    while True:
        T = random.randint(1, N // 2)
        C = N - T
        if T <= 2 * C and C <= 2 * T:
            break

    while True:
        tekler = random.sample(range(3, 5 * N + 1, 2), 2 * T)
        ciftler = random.sample(range(2, 5 * N + 1, 2), 2 * C)

        A = tekler + ciftler
        random.shuffle(A)

        if is_valid_A(A, N):
            break

    return A

# Örnek kullanım
try:
    N = int(input("Lütfen N değerini giriniz (1 ile 99 arasında olmalı): "))
    if N <= 0 or N >= 100:
        raise ValueError("N değeri 1 ile 99 arasında olmalıdır!")
    
    A = create_strong_array(N)
    print("Oluşturulan A Dizisi: ", A)

except ValueError as e:
    print("Hata: ", e)
