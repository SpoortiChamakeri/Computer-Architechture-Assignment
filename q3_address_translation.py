
# Question 3: Virtual-to-Physical Address Translation

page_size = 1024

# Virtual page number: physical frame number
page_table = {
    0: 5,
    1: 2,
    2: None,  # Page not present
    3: 7
}

addresses = [500, 1500, 2500, 3500]

print("Virtual Address | Page No. | Offset | Frame No. | Result")
print("-" * 75)

for address in addresses:
    page_number = address // page_size
    offset = address % page_size
    frame_number = page_table.get(page_number)

    if frame_number is None:
        result = "Page fault"
    else:
        physical_address = frame_number * page_size + offset
        result = f"Physical address = {physical_address}"

    print(
        f"{address:15} | {page_number:8} | "
        f"{offset:6} | {str(frame_number):9} | {result}"
    )
