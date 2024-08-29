hex_orig = ['1','9','11','27','2','12','3','12','9','12','11','1','3','13','4','3','5','15','2e','10','3','a','12','3','1','2e','16','2e','a','12',"6"]
numbers_times_4=[(int(h, 16) * 4) for h in hex_orig]
hex_numbers = [hex(num)[2:] for num in numbers_times_4]

start = "301020"
for num in hex_numbers:
    print(hex(int(start, 16)+int(num, 16))[2:], end=" ")
