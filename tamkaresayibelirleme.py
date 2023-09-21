import math


'''def full_square_num(lowest,highest):
    low_root = int(math.sqrt(lowest)) + 1
    high_root = int(math.sqrt(highest))
    if type(high_root) == int:
        high_root = high_root - 1   #eğer mesela karekökü 4 ise 4'ten küçük sayıları incelememiz gerekir.
    else:
        high_root = int(high_root) + 1 #eğer karekökü 4.6 gibi bir sayıysa da 4'ü de araştırmalı artının sebebi range alırken son sayıyı dahil etmiyor normalde
    perf_square_num_list = []
    for i in (low_root,high_root):
        print(i)
        perf_square_num = i*i
        print(perf_square_num)
        perf_square_num_list.append(perf_square_num)
    print(perf_square_num_list)


lowest = int(input("Aralığın en düşük numarasını yazınız= "))
highest = int(input("Aralığın en büyük numarasını yazınız= "))
full_square_num(lowest,highest)'''

import math
while True:
    decision= input("on/off?")
    if decision == "on":
        aralik_liste = []
        lowest = int(input("Please enter the lowest number of the range= "))
        highest = int(input("Please enter the highest number of the range= "))

        aralik_liste.append(lowest)
        aralik_liste.append(highest)
        low_sqrt = int(math.sqrt(aralik_liste[0])) + 1
        high_sqrt = int(math.sqrt(aralik_liste[1])) + 1  # range yapısında sondaki sayı sayılmadığı için highest sayının dahil olması gerekiyor o yüzden ekleme yaptık
        full_square_num_list = []
        if int(math.sqrt(lowest)) * int(math.sqrt(lowest)) == lowest:
            full_square_num_list.append(lowest)

        for i in range(low_sqrt, high_sqrt):
            full_square_num = i * i

            full_square_num_list.append(full_square_num)

        print(full_square_num_list)

    elif decision == "off":
        print("Ending the process...")
        break
    else:
        print("Please enter a valid response! ")


