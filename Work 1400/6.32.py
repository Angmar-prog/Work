
id = 10
ip = 0.10
d = 10
cd = id
print("День\tПробег (км)")
for da in range(1, d + 1):
    print(f"{da}\t{cd:.2f}")
    cd += cd * ip