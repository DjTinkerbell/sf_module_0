def game_core_v3(number):
  count = 0
  predict = np.random.randint(1,100)
  left = 1
  right = 100

  while left <= right:
    count += 1
    mid = (left + right) // 2
    if predict == mid:
      break
    if predict < mid:
      right = mid
    else:
      left = mid
  return count
        
print (f"Ваш алгоритм угадывает число в среднем за {count} попыток.")