def algoritm_evklida(num_1, num_2):

    while num_1 != num_2:
            if num_1 >= num_2:
                num_1 -= num_2
            else:
                num_2 -= num_1

    if num_1 == 1:
        return 1
    else:
        return 0


