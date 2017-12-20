from functools import reduce


def read_file(input_name):
    """
    read input matrix
    :param input_name: file name
    :return: input_arr: list of vectors
    """
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
    """
    create prebasis for given equation
    :param equation: vector
    :return: pre_basis: list of vectors
    """
    pre_basis = []
    i_not_zero = 0  # placement of first coordinate which not equals zero
    for i in range(0, len(equation)):  # search for i_not_zero
        if equation[i] != 0:
            i_not_zero = i
            break
    for i in range(0, len(equation)):  # iterate through equation coefficients
        if i == i_not_zero:  # skip
            continue
        pre_basis_vector_i = [0]*len(equation)  # initialize with zeroes
        pre_basis_vector_i[i_not_zero] = equation[i] * -1  # put inverted coefficient on place of first not zero
        pre_basis_vector_i[i] = equation[i_not_zero]  # replace coefficient with first not zero
        pre_basis.append(pre_basis_vector_i)  # for each coefficient add new vector to prebasis
    return pre_basis


def substitute(equation, pre_basis):
    """
    substitute vectors of prebasis to given equation
    :param equation: list of integers
    :param pre_basis: list of vectors
    :return: list of integers
    """
    result = []
    for vector in pre_basis:
        one_vector_result = 0  # value of substitution of single prebasis vector
        for c in range(0, len(equation)):
            one_vector_result += vector[c]*equation[c]
        result.append(one_vector_result)  # add for each prebasis vector
    return result


def multiply_pre_basis(big_pre_basis, small_pre_basis):
    """
    multiplies pre basis from equation gained from substitution and pre basis from initial equation(main prebasis)
    :param big_pre_basis: from initial(main prebasis)
    :param small_pre_basis: gained from substitution
    :return: result: list of vectors. List size equals to size of small_pre_basis(gained from substitution)
    """
    result = []
    for small_vector in small_pre_basis:
        one_vector_result = [0] * len(big_pre_basis[0])  # result from one vector of substitution prebasis
        for i_small_vector in range(0, len(small_vector)):  # for each coefficient of vector from substituion prebasis
            if small_vector[i_small_vector] != 0:  # if coefficient not zero
                for c in range(len(big_pre_basis[0])):
                    # multiply coefficient of vector from small prebasis(from substitution) with each vector from main prebasis(big), sum vectors
                    one_vector_result[c] += big_pre_basis[i_small_vector][c] * small_vector[i_small_vector]
        result.append(one_vector_result)
    return result


def GCD(a, b):  # Greatest Common Divisor
    if b == 0:
        return a
    else:
        return GCD(b, a % b)


def simplify(ar):
    """
    simplifying vectors of matrix
    :param ar: matrix of vectors
    :return: ar2: simplified matrix
    """
    ar2 = []  # for storing result(faster than deleting)
    for y in ar:
        d = reduce(GCD, y)  # searching for greatest common divisor
        if d != 1 and d != 0:
            y = list(map(lambda t: t//d, y))  # dividing by GCD
        ar2.append(y)  # append to answer
    return ar2


def solv(input_arr):
    pre_basis_main = create_pre_basis(input_arr[0])  # create prebasis for the first equation
    for Li in range(1, len(input_arr)):  # iterate through other equations
        Y = substitute(input_arr[Li], pre_basis_main)  # substitute vectors of prebasis to equation Li
        pre_basis_Y = create_pre_basis(Y)  # create prebasis from result of substitution
        pre_basis_main = multiply_pre_basis(pre_basis_main, pre_basis_Y)  # get new main prebasis
        pre_basis_main = simplify(pre_basis_main)  # simplify vectors of prebasis if possible
    return pre_basis_main


def control_main(input_name):  # for using as module
    return solv(read_file(input_name))


if __name__ == "__main__":  # if launched standalone
    file = 'generated.txt'
    import time
    start_time = time.time()
    print(solv(read_file(file)))
    end_time = time.time()
    print(end_time-start_time)