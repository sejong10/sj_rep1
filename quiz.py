Num_level = int(raw_input("How many leverls of pyramid do you want? "))
for i in range(1, Num_level+1):
    for Num_space in range(0, Num_level-i):
        print " ",
    for Num_star in range(0, i*2-1):
        print "*",
    print    
