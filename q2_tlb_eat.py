# Question 2: Effective Access Time using TLB

tlb_time = 10       # nanoseconds
memory_time = 80    # nanoseconds

hit_ratios = [0.90, 0.75]

print("TLB Lookup Time:", tlb_time, "ns")
print("Memory Access Time:", memory_time, "ns")

for hit_ratio in hit_ratios:
    miss_ratio = 1 - hit_ratio

    eat = (
        hit_ratio * (tlb_time + memory_time)
        + miss_ratio * (tlb_time + 2 * memory_time)
    )

    print("\nTLB Hit Ratio:", hit_ratio)
    print("TLB Miss Ratio:", round(miss_ratio, 2))
    print("Effective Access Time:", round(eat, 2), "ns")
