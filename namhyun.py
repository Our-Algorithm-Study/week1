# 시험 성적 9498
a = int(input())

if a >= 90 and a <= 100:
    print("A")

elif a <= 89 and a >= 80:
    print("B")
    
elif a <= 79 and a >= 70:
    print("C")
    
elif a <= 69 and a >= 60:
    print("D")
    
else:
    print("F")


# 주사위 세 개 2480
a, b, c = map(int, input().split())

answer = 0

if a == b == c:
    answer = 10000 + a * 1000
elif a != b and a != c and b != c:
    answer = max([a, b, c]) * 100
else:
    if a == b or a == c:
        answer = 100 * a + 1000
    else:
        answer = 100 * b + 1000
        
print(answer)


# 바구니 뒤집기 10811
n, m = map(int, input().split())

seq = [i for i in range(n+1)]

for p in range(m):
    i, j = map(int, input().split())
    
    for q in range((j - i + 1) // 2):
        seq[i + q], seq[j - q] = seq[j - q], seq[i + q]
        
print(*seq[1:])


# 소수 찾기 1978
import math

n = int(input())
lst = list(map(int, input().split()))

def is_prime_num(n):
    if n == 1:
        return 0
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if not n % i:
            return 0
    return 1


count = 0
for i in lst:
    if is_prime_num(i):
        count += 1
        
print(count)


# 설탕 배달 2839
n = int(input())

answer = 0

while True:
    if not n % 5:
        answer += n // 5
        break
        
    n -= 3
    answer += 1
    
    if n > 0 and n < 3:
        answer = -1
        break
        
print(answer)


# 11651 좌표 정렬하기 2
n = int(input())

lst = []
for i in range(n):
    x, y = map(int, input().split())
    
    lst.append((x, y))
    
lst.sort(key = lambda x : (x[1], x[0]))

for i in range(n):
    print(*lst[i])
  

# 1181 단어 정렬
n = int(input())

lst = set()
for i in range(n):
    lst.add(input().rstrip())
    
lst = list(lst)

lst.sort()
lst.sort(key = len)

for i in lst:
    print(i)
  

# 10815 숫자 카드
n = int(input())
lst = set(map(int, input().split()))
m = int(input())
for i in map(int, input().split()):
    print(1 if i in lst else 0, end = ' ')
  

# 1764 듣보잡
n, m = map(int, input().split())

a = set()
b = set()

for i in range(n):
    a.add(input().rstrip())
for i in range(m):
    b.add(input().rstrip())
    
c = a & b

c = list(c)
c.sort()

print(len(c))
for i in c:
    print(i)
