from collections import Counter

N = int(input())
print(N)
S = [int(input()) for _ in range(N)]
print(S)

S.sort() # S라는 객체의 메소드를 호출한다는 뜻
print(sum(S)//N)
print(S[len(S)//2])
print(Counter(S).most_common())
print(max(S)-min(S))
# N = int(input())
# S = []
# for i in range(N):
#     S.append(int(input()))
    
# print(S)
