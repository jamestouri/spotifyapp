# Question 1
def sort_by_string(s, t):
  res = ''
  for i in t:
    res += i * s.count(i)
    s = s.replace(i, '')
  return res + s

# print(sort_by_string("weather", "therapyw"))

# Question 2
def decode_string(s):
  stack = []
  stack.append(["", 1])
  num = ""
  for i in s:
      if i.isdigit():
        num += i
      elif i == '[':
          stack.append(["", int(num)])
          num = ""
      elif i == ']':
          st, k = stack.pop()
          stack[-1][0] += st*k
      else:
          stack[-1][0] += i
  return stack[0][0]

# print(decode_string("3[a]2[bc]"))

# Question 3
def coin_sum(coins, total):
  table = [0] * (total + 1)
  table[0] = 1
  for coin in coins:
      for i in range(coin, len(table)):
          table[i] = table[i] + table[i - coin]

  return table[len(table) - 1]

# print(coin_sum([1, 2, 3], 4))
