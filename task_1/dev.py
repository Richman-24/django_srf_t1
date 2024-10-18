

def increaser(n):
    if n <= 0:
        raise ValueError("Число должно быть > 0")
    
    res = []
    current = 1

    while len(res) < n:
        res.extend([current] * current)
        current +=1

    return res[:n]


if __name__ == "__main__":
    n = int(input("введите количество элементов последовательности: "))
    seq = increaser(n)
    print("Первые", n, "элементов последовательности:", *seq)