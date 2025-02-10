# A 1000번: A+B
a, b = map(int, input().split())
print(a+b)

#그냥 더함


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

#그냥 함


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

#모든 경우를 다 때려넣음


# D 10811번: 바구니 뒤집기
a, b = map(int, input().split())
num = []
bucket = list(range(1, a+1))
for i in range(b):
    num.append(list(map(int, input().split())))
for n in range(len(num)):
    i = num[n][0] - 1
    j = num[n][1]
    new_bucket = bucket[i : j] #뒤집을 범위로 새로운 리스트 생성
    new_bucket.reverse() #뒤집음
    bucket[i : j] = new_bucket #교체
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

#1에서 한 번씩 갈 때마다 6*횟수 + 방향에 따른 값 이 더해짐
#근데 이 방향에 따른 값은 영향이 미비하기 때문에 무시 가능
#그래서 그냥 1보다 작아질 때까지 뺌


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

#소수의 정의에 집중
#N이라는 수를 1~N까지로 모두 나눠보고
#나누어 떨어지는 경우마다 cnt_zero를 1씩 더함
#다 나눴을 때 cnt_zero = 2라면 약수가 두 개 (1, 자기자신)밖에 없다는 뜻이므로 소수


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

#최대한 5kg으로 많이 묶는 것이 목표이므로
#5의 배수라면 일단 5로 나눔 이때 3과 5의 공배수인 15의 배수 처리
#아니면 5의 배수가 될 때까지 3을 뺌 (3의 배수가 될 때까지 5를 빼는 것 보다 늘 5kg으로 많이 묶을 수 있음)
#그러다가 5의 배수가 되면 묶음
#0이 되면 3의 배수이므로 3으로 묶음
#그게 아니면 못 몪음


# H 11651번: 좌표 정렬하기 2
N = int(input()) 
L = []

for i in range(N):
    a, b = map(int, input().split())
    L.append([a, b])

L_sorted = sorted(L, key=lambda p: (p[1], p[0]))

for x, y in L_sorted:
    print(x, y)

#좌표를 싹 다 받아서 리스트에 저장하고
#그냥 그 리스트를 정렬


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

#[단어, 단어 길이] 로 이루어진 리스트 생성
#좌표 정렬과 동일하게 단어 길이로 먼저 정렬, 그 후 사전식 정렬
#같은 것을 제거하기 위해 반복문 안에 조건문을 넣어서 처리


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

#처음에 그냥 리스트로 했다가 시간 초과 걸려서 시간복잡도 측면에서 효율적인 집합으로 변경
#교집합 생성
#확인해야할 수들과 교집합을 비교해서 있으면 1 없으면 0


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
for i in sorted(never_heard_seen):
    print(i)

#순서가 상관 없고 시간복잡도 측면에서 효율적인 집합으로 저장
#교집합을 리스트로 변경하고 예제 출력대로 알파벳순 정렬후 출력