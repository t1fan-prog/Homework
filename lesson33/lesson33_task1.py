import concurrent.futures

NUMBERS = [
   2,  # prime
   1099726899285419,
   1570341764013157,  # prime
   1637027521802551,  # prime
   1880450821379411,  # prime
   1893530391196711,  # prime
   2447109360961063,  # prime
   3,  # prime
   2772290760589219,  # prime
   3033700317376073,  # prime
   4350190374376723,
   4350190491008389,  # prime
   4350190491008390,
   4350222956688319,
   2447120421950803,
   5,  # prime
]


def is_prime(num):
    if num % 2 == 0:
        return num, num == 2
    d = 3
    while d * d <= num and num % d != 0:
        d += 2
    return num, d * d > num


with concurrent.futures.ProcessPoolExecutor() as executor:
    results = [executor.submit(is_prime, i) for i in NUMBERS]
    for f in concurrent.futures.as_completed(results):
        print(f.result())

