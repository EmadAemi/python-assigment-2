n = int(input("Students No. : "))
scores = []
for i in range(n):
    scores.append(int(input()))
print( "Average:", sum(scores)/len(scores) )
print( "Max:", max(scores))
print( "Min:", min(scores))