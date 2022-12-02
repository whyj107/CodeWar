# Optimal Taxi Fare
# https://www.codewars.com/kata/52f51502053125863c0009d7/train/python

# 나의 풀이
def calculate_optimal_fare(d, t, v1, r, v2):
    m_v1 = v1/60
    m_v2 = v2/60
    if m_v2*t >= d:
        return "0.00"
    elif m_v1*t >= d:
        x = (d - m_v2*t)/(m_v1 - m_v2)
        return f'{m_v1*x*r:0.2f}'
    else:
        return "Won't make it!"

# 다른 사람의 풀이
def calculate_optimal_fare1(d, t, taxi, r, walk):
    h = t/60.0
    if walk * h >= d: return "0.00"
    if taxi * h <  d: return "Won't make it!"
    return "%.2f" % (r * taxi * (d - walk * h) / (taxi - walk))

print(calculate_optimal_fare(8, 10, 90, 2, 6), "15.00")
print(calculate_optimal_fare(8, 10, 90, 1, 6), "7.50")
print(calculate_optimal_fare(100, 10, 500, 5, 25), "Won't make it!")