# Question 1: LRU Cache Replacement Algorithm

cache_size = 3
sequence = [4, 2, 1, 6, 3, 2, 5, 4]

cache = []
hits = 0
misses = 0

print("Page\tCache Contents\tResult")

for page in sequence:
    if page in cache:
        hits += 1
        cache.remove(page)
        cache.append(page)
        result = "HIT"
    else:
        misses += 1

        if len(cache) == cache_size:
            cache.pop(0)

        cache.append(page)
        result = "MISS"

    print(f"{page}\t{cache}\t\t{result}")

total = len(sequence)

print("\nTotal accesses:", total)
print("Total hits:", hits)
print("Total misses:", misses)
print("Hit ratio:", round(hits / total, 2))
print("Miss ratio:", round(misses / total, 2))
