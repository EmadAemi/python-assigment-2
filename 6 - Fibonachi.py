n = int(input("Enter n (n>2): "))
fibonachi = [1, 1]
for i in range(n-2):
    fibonachi.append( fibonachi[len(fibonachi)-1] + fibonachi[len(fibonachi)-2] )
print(fibonachi)