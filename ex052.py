num = int(input("Digite um número: "))
tot = 0
for C in range(1, num + 1):
    if num % C == 0:
        print("\033[33m", end=' ')
        tot += 1
    else:
        print("\033[31m", end=' ')
    print("{} ".format(C), end=' ')
print("\n\033[mO número {} foi dicisível {} vezees".format(num, tot))
if tot == 2:
    print("E por isso ele É  PRIMO!")
else:
    print("E por isso ele NÃO É PRIMO!")