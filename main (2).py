import numpy as np
count = 0
gap = 48
number = np.random.randint(1,100)    # загадали число
print ("Загадано число от 1 до 99")

while True:                        # бесконечный цикл
    predict = int(input())         # предполагаемое число
    count = count + 1
    gap = gap * 0.5
    if number == predict: break    # выход из цикла, если угадали
    elif number > predict:
        predict = predict + gap
        if number > predict:
          print (f"Угадываемое число больше {predict} ")
        else:
          print (f"Угадываемое число больше {predict-gap}, но меньше {predict} ")  
    elif number < predict:
        predict = predict - gap
        if number < predict:
          print (f"Угадываемое число меньше {predict} ")
        else:
          print (f"Угадываемое число больше {predict}, но меньше {predict+gap} ")  
        
print (f"Вы угадали число {number} за {count} попыток.")
