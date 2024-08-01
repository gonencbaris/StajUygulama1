counts =  [14, 12, 2, 3, 4, 20, 21, 11, 25, 10]

def create_B_from_A(A):
    B = [A[i] + (i + 1) for i in range(len(A))]
    return B

def is_strong_array(A):
    N = len(A) // 2
    B = create_B_from_A(A)
    
    odd_count_B = sum(1 for x in B if x % 2 != 0)
    even_count_B = len(B) - odd_count_B

    steps = []
    steps.append(f"A Dizisi: {A}")
    steps.append(f"B Dizisi: {B}")
    steps.append(f"TEK sayıların adeti: {odd_count_B}, ÇİFT sayıların adeti: {even_count_B}")

    if odd_count_B != N or even_count_B != N:
        steps.append(f"TEK sayıların adeti ({odd_count_B}) ve ÇİFT sayıların adeti ({even_count_B}) eşit değil.")
        return False, steps

    odd_sum_B = sum(x for x in B if x % 2 != 0)
    expected_odd_sum = N * (2 * N + 1)
    steps.append(f"TEK sayıların toplamı: {odd_sum_B}, Beklenen TEK sayıların toplamı: {expected_odd_sum}")

    if odd_sum_B != expected_odd_sum:
        steps.append(f"TEK sayıların toplamı ({odd_sum_B}) beklenen değere ({expected_odd_sum}) eşit değil.")
        return False, steps

    even_sum_B = sum(x for x in B if x % 2 == 0)
    sum_A = sum(A)
    steps.append(f"ÇİFT sayıların toplamı: {even_sum_B}, A dizisinin toplamı: {sum_A}")

    if even_sum_B != sum_A:
        steps.append(f"ÇİFT sayıların toplamı ({even_sum_B}) A dizisinin toplamına ({sum_A}) eşit değil.")
        return False, steps

    steps.append("Dizi StrongArray'dir.")
    return True, steps

N = len(counts) // 2
A = counts[:2 * N]

is_strong, details = is_strong_array(A)

for step in details:
    print(step)
