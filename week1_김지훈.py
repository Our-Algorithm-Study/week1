# A 1000번: A+B
a, b = map(int, input().split())
print(a+b)


# B 9498번: 시험 성적
score = int(input())
if score >= 90: 
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")


# C 2480번: 주사위 세개
a, b, c = map(int, input().split())
if a == b == c:
    print(10000 + 1000*a)
elif a == b:
    print(1000 + 100*a)
elif b == c:
    print(1000 + 100*b)
elif a == c:
    print(1000 + 100*a)
else:
    num = [a, b, c]
    print(100*max(num))


# D 10811번: 바구니 뒤집기
a, b = map(int, input().split())
num = []
bucket = list(range(1, a+1))
for i in range(b):
    num.append(list(map(int, input().split())))
for n in range(len(num)):
    i = num[n][0] - 1
    j = num[n][1]
    new_bucket = bucket[i : j]
    new_bucket.reverse()
    bucket[i : j] = new_bucket
print(*bucket)


# E 2292번: 벌집
a = int(input())

i = 1
num = 1

while a > 1:
    a -= 6*i
    num += 1
    i += 1
    
print(num)


# F 1978번: 소수 찾기
a = int(input())
b = map(int, input().split())
b = list(b)
cnt = 0
for i in range(a):
    cnt_zero = 0
    for c in range(b[i]):
        if b[i] % (c + 1) == 0:
            cnt_zero += 1
    if cnt_zero == 2:
        cnt += 1

print(cnt)


# G 2839번: 설탕 배달
N = int(input())
cnt = 0

if N % 5 == 0:
    cnt = N // 5
else:
    while N > 0:
        N -= 3
        cnt += 1
        if N % 5 == 0:
            cnt += N // 5
            break
        elif N == 0:
            cnt += N // 3
            break
        elif N == 1 or N == 2:
            cnt = -1
            break

print(cnt)


# H 11651번: 좌표 정렬하기 2
N = int(input()) 
L = []

for i in range(N):
    a, b = map(int, input().split())
    L.append([a, b])

L_sorted = sorted(L, key=lambda p: (p[1], p[0]))

for x, y in L_sorted:
    print(x, y)


# I 1181번: 단어 정렬
N = int(input())
d = []

for i in range(N):
    a = str(input())
    b = len(a)
    d.append([a, b])

d_sorted = sorted(d, key = lambda p: (p[1], p[0]))

ans = []

for o in d_sorted:
    if o[0] not in ans:
        ans.append(o[0])

for r in ans:
    print(r)


# J 10815번: 숫자 카드
N = int(input())
a = list(map(int, input().split()))
a_set = set(a)

M = int(input())
b = list(map(int, input().split()))
b_set = set(b)

ab = a_set & b_set

ans = []
for num in b:
    if num in ab:
        ans.append(1)
    else:
        ans.append(0)

print(*ans)


# K 1764번: 듣보잡
a, b = map(int, input().split())

never_heard = set()
never_seen = set()

for i in range(a):
    name = str(input())
    never_heard.add(name)

for i in range(b):
    name = str(input())
    never_seen.add(name)

never_heard_seen = list(never_heard & never_seen)
L = len(never_heard_seen)
print(L)
for i in sorted(never_heard_seen):
    print(i)