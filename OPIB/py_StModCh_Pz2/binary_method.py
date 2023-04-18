


# c = a^b mod p
# Бинарный алгоритм выстрого возведения в степень по модулю числа работает следующим образом:
# необходимо b представить в двоичной системе счисления, подсчитать количество разрядов n и
# по количеству этих разрядов n просчитать все числа (num[0] = a, num[1] = num[0]^2 mod p, ..., numn[n] = num[n-1]^2 mod p).
# в результате ответ будет произведением всех num[i] в степени в соответсвии со степенью b

num_input = int(input('Число:'))
pow_input = int(input('Степень:'))
mod_input = int(input('Модуль:'))

def bin_method():
    len_bin = len(bin(pow_input))-2 # число разрядов степени в двоичной сс
    
    all_bin = []
    for i in range(2, len(bin(pow_input))):
        all_bin.append(int(bin(pow_input)[i]))
    all_bin.reverse()
    
    print('Все разряды:', all_bin)

    all_num = []
    all_num.append(num_input)
    for i in range(1, len_bin):
        all_num.append(pow(all_num[i-1],2) % mod_input)

    print('Все числа:', all_num)

    answer = 1
    for i in range(len_bin):
        answer = answer * pow(all_num[i], all_bin[i])
    return answer % mod_input

print(bin_method(), '=',pow(num_input,pow_input) % mod_input)