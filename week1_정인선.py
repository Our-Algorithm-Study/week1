{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n"
     ]
    }
   ],
   "source": [
    "# A A+B\n",
    "# 두 개의 정수를 입력받아 합을 구하는 문제\n",
    "while True: \n",
    "    a, b = map(int, input().split())  # 두 개의 정수를 입력받아 정수형으로 변환\n",
    "    if 0 < a < 10 and 0 < b < 10:  # a와 b가 1 이상 9 이하일 때만 실행\n",
    "        print(a+b)  # 두 수의 합 출력\n",
    "        break  # 조건을 만족하면 반복문 종료\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "A\n"
     ]
    }
   ],
   "source": [
    "# B 시험 성적\n",
    "# 입력받은 점수에 따라 학점을 출력하는 문제\n",
    "score = int(input())  # 정수형 점수 입력받기\n",
    "grade = \"x\"  # 초기값 설정\n",
    "\n",
    "# 점수 구간에 따라 학점 결정\n",
    "if 90 <= score <= 100:\n",
    "    grade = \"A\"\n",
    "elif 80 <= score <= 89:\n",
    "    grade = \"B\"\n",
    "elif 70 <= score <= 79: \n",
    "    grade = \"C\"\n",
    "elif 60 <= score <= 69: \n",
    "    grade = \"D\"\n",
    "else:\n",
    "    grade = \"F\"\n",
    "\n",
    "print(grade)  # 결과 출력\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "600\n"
     ]
    }
   ],
   "source": [
    "# C 주사위 세 개\n",
    "# 주사위 세 개를 던졌을 때의 상금을 계산하는 문제\n",
    "d1, d2, d3 = map(int, input().split())  # 주사위 3개의 값을 입력받음\n",
    "prize = 0  # 상금 초기화\n",
    "\n",
    "if d1 == d2 == d3:  # 세 개의 주사위 값이 같을 때\n",
    "    prize = 10000 + d1 * 1000\n",
    "elif d1 == d2 or d2 == d3 or d3 == d1:  # 두 개의 주사위 값이 같을 때\n",
    "    if d1 == d2:\n",
    "        prize = 1000 + d1 * 100\n",
    "    elif d2 == d3:\n",
    "        prize = 1000 + d2 * 100\n",
    "    else: \n",
    "        prize = 1000 + d3 * 100\n",
    "else:  # 모두 다른 값일 때\n",
    "    prize = max(d1, d2, d3) * 100  # 가장 큰 값을 기준으로 상금 계산\n",
    "\n",
    "print(prize)  # 결과 출력\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 2 3 4 5\n"
     ]
    }
   ],
   "source": [
    "# D 바구니 뒤집기\n",
    "# 특정 범위의 바구니 순서를 뒤집는 문제\n",
    "N, M = map(int, input().split())  # 바구니 개수 N과 뒤집는 횟수 M 입력받기\n",
    "basket = list(range(1, N + 1))  # 1부터 N까지 번호가 적힌 리스트 생성\n",
    "\n",
    "for b in range(M):  # M번 입력을 받음\n",
    "    i, j = map(int, input().split())  # i번째부터 j번째 바구니까지 뒤집을 구간을 입력받음\n",
    "    basket[i-1:j] = basket[i-1:j][::-1]  # 리스트 슬라이싱을 사용해 해당 구간을 역순 정렬\n",
    "\n",
    "print(*basket)  # 리스트의 요소를 공백으로 구분하여 출력\n",
    "\n",
    "#반복문 안에서 i, j = map(int, input().split())를 통해 두 개의 정수를 입력받는다. \n",
    "#여기서 i와 j는 1부터 시작하는 번호(1-based index)이지만, 파이썬 리스트는 0부터 시작하는 인덱스(0-based index)를 사용하므로, 이를 조정해야 한다.\n",
    "#이후 basket[i-1:j] = basket[i-1:j][::-1]를 실행하여 해당 범위의 바구니 순서를 뒤집는다. \n",
    "# basket[i-1:j]는 리스트에서 i-1번째부터 j-1번째까지의 부분을 가져오는 슬라이싱 연산이며, [::-1]을 적용해 해당 부분을 역순으로 변환한다. \n",
    "# 마지막으로 basket[i-1:j] = ...을 통해 원래 리스트의 해당 구간을 뒤집힌 값으로 교체한다.\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n"
     ]
    }
   ],
   "source": [
    "# F 소수 찾기\n",
    "# 입력받은 숫자들 중 소수의 개수를 찾는 문제\n",
    "\n",
    "N = int(input())  # 입력받을 숫자의 개수\n",
    "numbers = map(int, input().split())  # N개의 숫자를 입력받음\n",
    "\n",
    "def prime_num(x):\n",
    "    if x == 1:  # 1은 소수가 아님\n",
    "        return False\n",
    "    for i in range(2, x):  # 2부터 x-1까지 나누어 떨어지는지 확인\n",
    "        if x % i == 0:  # 나누어 떨어지면 소수가 아님\n",
    "            return False\n",
    "    return True  # 위 조건을 모두 통과하면 소수\n",
    "\n",
    "count = 0  # 소수 개수를 저장할 변수\n",
    "for n in numbers:\n",
    "    if prime_num(n):  # n이 소수라면\n",
    "        count += 1  # 소수 개수 증가\n",
    "\n",
    "print(count)  # 소수 개수 출력\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['pear', 'wine', 'glass']\n"
     ]
    }
   ],
   "source": [
    "# I 단어 정렬\n",
    "# 주어진 단어들을 정렬하는 문제\n",
    "\n",
    "N = int(input())  # 단어의 개수 입력받기\n",
    "words = list(set(input() for i in range(N)))  # 중복 제거 후 리스트 생성\n",
    "\n",
    "words.sort()  # 사전 순 정렬\n",
    "words.sort(key=len)  # 길이순 정렬 (길이가 같으면 사전순 유지)\n",
    "\n",
    "for word in words:  # 정렬된 단어\n",
    "    print(word)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
