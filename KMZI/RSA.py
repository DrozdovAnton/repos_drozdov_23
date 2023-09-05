import KR_Resheto_Eratospena, KR_Algoritm_Evklida


p = int(input('\nВведите число p: '))
q = int(input('Введите число q: '))

message = input('Введите сообщение, которое нужно зашифровать: ')


#_______________ПАРАМЕТРЫ_______________

n = p * q
f_n = (p-1) * (q-1)

e = 0
d = 0

#_______________ПАРАМЕТРЫ_______________


def open_key(func_eiler): # ГЕНЕРАЦИЯ ОТКРЫТОГО КЛЮЧА 
    primes = KR_Resheto_Eratospena.resheto_eratosphena(func_eiler) 
    
    for i in range(len(primes)): 
        if KR_Algoritm_Evklida.algoritm_evklida(primes[i],f_n) != 1:
            primes[i] = 0
    
    primes = [i for i in primes if i != 0] 

    return primes[0]

e = open_key(f_n) 

def secret_key(func_eiler, e_from_open_key): # ГЕНЕРАЦИЯ СЕКРЕТНОГО КЛЮЧА
    d_list = [] # Список для выбора значения d
    d_ok = []

    for i in range(func_eiler):
        d_list.append(i+1)

    for d in d_list:
        if d * e_from_open_key % func_eiler == 1:
            d_ok.append(d)
    
    return d_ok[0]

d = secret_key(f_n, e)

def encryption(position_inp_message): # ЗАШИФРОВАНИЕ
    position_encr_message = []
    for position in position_inp_message:
        position_encr_message.append(position ** e % n)
    return position_encr_message

def decription(position_enc_message): # РАСШИФРОВАНИЕ
    position_decr_message = []
    for position in position_enc_message:
        position_decr_message.append(position ** d % n)
    return position_decr_message

def position_characters(msg): # ПОЗИЦИЯ СИМВОЛА В UNICODE
    position = []
    for i in msg:
        position.append(ord(i))
    return position

def output_message(msg_pos: list): # ВЫВОД
    out_msg = ''
    for i in msg_pos:
        out_msg += chr(i)
    print(out_msg)

def bin_character(out_position): # ДВОИЧНОЕ ПРЕДСТАВЛЕНИЕ
    out_bin_position = []
    for i in out_position:
        out_bin_position.append(bin(i))
    print(out_bin_position)

#_______________ВЫВОД_______________

print('\nn:', n, '\ne:', e, '\nd:', d)

print('\n\tИсходное сообщение:')
output_message(position_characters(message))
print(position_characters(message))
print('Двоичный вид:')
bin_character(position_characters(message))

print('\n\tЗашифрованное сообщение:')
output_message(encryption(position_characters(message)))
print(encryption(position_characters(message)))
print('Двоичный вид:')
bin_character(encryption(position_characters(message)))

print('\n\tРасшифрованное сообщение:')
output_message(decription(encryption(position_characters(message))))
print(decription(encryption(position_characters(message))))
print('Двоичный вид:')
bin_character(decription(encryption(position_characters(message))))

#________________ЭЦП________________

def create_sign(inp_message): # СОЗДАНИЕ ПОДПИСИ
    position = position_characters(inp_message)
    sign = []
    for i in position:
        sign.append(i ** d % n)
    return sign

def check_sign(sign): # ЭТАП ПОДГОТОВКИ ПАРАМЕТРА M' ДЛЯ ПРОВЕРКА ПОДЛИННОСТИ
    check_signature = []
    for i in sign:
        check_signature.append(i ** e % n)
    return check_signature

def chech_final(inp_message, sign): # ПРОВЕРКА ПОДЛИННОСТИ
    if position_characters(inp_message) == sign:
        print('Подпись истинная')
    else:
        print('Подпись ложная')

print('\n\tСоздание ЭЦП')
print('Сообщение M:', message, position_characters(message))
print('sign:', create_sign(message))
print("M':", check_sign(create_sign(message)))
chech_final(message, check_sign(create_sign(message)))

input()