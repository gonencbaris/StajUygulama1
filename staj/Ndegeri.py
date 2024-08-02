import random
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

def create_strong_array(N, max_sure):
    print(f"N = {N} için oluşturulmaya çalışılıyor...")
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
    while time.time() - start_time <= max_sure:
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
                    print(f"N = {N} için StrongArray başarıyla oluşturuldu.")
                    return A
        
        attempt_counter += 1
        if attempt_counter % 1000 == 0:
            print(f"{attempt_counter} permütasyon denendi...")

    print(f"N = {N} için StrongArray oluşturulamadı.")
    return None

def find_max_strong_array(max_sure_per_N):
    successful_N = []
    successful_arrays = []
    N = 2  

    while True:
        try:
            start_time = time.time()
            strong_array = create_strong_array(N, max_sure_per_N)
            if strong_array:
                successful_N.append(N)
                successful_arrays.append(strong_array)
            else:
                break  
            N += 1
            elapsed_time = time.time() - start_time
            remaining_time = max_sure_per_N - elapsed_time
            if remaining_time <= 0:
                break
        except ValueError as e:
            print(f"N = {N} için hata: {e}")
            break

    if successful_N:
        print(f"En büyük başarılı N değeri: {successful_N[-1]}")
    else:
        print("Hiçbir N değeri için StrongArray oluşturulamadı.")
    
    print("Başarılı N değerleri:", successful_N)
    print("Başarılı StrongArray dizileri:")
    for n, array in zip(successful_N, successful_arrays):
        print(f"N = {n}: {array}")
    
    if successful_N:
        print(f"En fazla {successful_N[-1]} elemanlı bir dizi ile StrongArray oluşturulabilir.")
    else:
        print("StrongArray oluşturulamadı.")

try:
    max_sure_per_N = 600 
    find_max_strong_array(max_sure_per_N)
except ValueError as e:
    print(f"Hata: {e}")
