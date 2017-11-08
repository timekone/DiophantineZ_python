from functools import reduce


def read_file(input_name):
    input_arr = []
    with open(input_name) as input_file:
        for line in input_file:
            l = line.split()
            int_l = []
            for ch in l:
                int_l.append(int(ch))
            input_arr.append(int_l)
    return input_arr


def create_pre_basis(equation):
    pre_basis = []
    i_not_zero = 0
    for i in range(0, len(equation)):
        if equation[i] != 0:
            i_not_zero = i
            break
    for i in range(0, len(equation)):
        if i == i_not_zero:
            continue
        pre_basis_vector_i = [0]*len(equation)
        pre_basis_vector_i[i_not_zero] = equation[i] * -1
        pre_basis_vector_i[i] = equation[i_not_zero]
        pre_basis.append(pre_basis_vector_i)
    return pre_basis


def substitute(equation, pre_basis):
    result = []
    for vector in pre_basis:
        one_vector_result = 0
        for c in range(0, len(equation)):
            one_vector_result += vector[c]*equation[c]
        result.append(one_vector_result)
    return result


def multiply_pre_basis(big_pre_basis, small_pre_basis):
    """
    multiplies pre basis from equation gained from substitution and pre basis from initial equation
    :param big_pre_basis:
    :param small_pre_basis:
    :return: result
    """
    result = []
    for small_vector in small_pre_basis:
        one_vector_result = [0] * len(big_pre_basis[0])
        for i_small_vector in range(0, len(small_vector)):
            if small_vector[i_small_vector] != 0:
                for c in range(len(big_pre_basis[0])):
                    one_vector_result[c] += big_pre_basis[i_small_vector][c] * small_vector[i_small_vector]
        result.append(one_vector_result)
    return result


def GCD(a, b):  # It takes too long!
    if b == 0:
        return a
    else:
        return GCD(b, a % b)


def simplify(ar):
    ar2 = []
    for y in ar:
        d = reduce(GCD, y)  # move from here, after redundant
        if d != 1 and d != 0:
            y = list(map(lambda t: t//d, y))
        ar2.append(y)
    return ar2


def solv(input_arr):
    pre_basis_main = create_pre_basis(input_arr[0])
    for Li in range(1, len(input_arr)):
        Y = substitute(input_arr[Li], pre_basis_main)
        pre_basis_Y = create_pre_basis(Y)
        pre_basis_main = multiply_pre_basis(pre_basis_main, pre_basis_Y)
        pre_basis_main = simplify(pre_basis_main)
    return pre_basis_main


def control_main(input_name):
    return solv(read_file(input_name))


if __name__ == "__main__":
    file = 'input(old).txt'
    print(solv(read_file(file)))
