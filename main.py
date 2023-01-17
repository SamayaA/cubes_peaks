from itertools import permutations

def find_sum(numbers: list) -> int:
    # так как total_sum - это сумма всех вершин
    total_sum = sum(numbers)

    # так как total_sum - то сумма
    # всех вершин, то total_sum \ 2 это сумма
    #  вершн одной грани
    # total sum - сумма суммы вершин двух граней
    #  куба, которфе не имею однинаковых вершин

    # сумма вершин одной грани
    face_sum = total_sum // 2

    return face_sum

def check_sum_digits(number: int) -> bool:
    '''
    Check if sum of digits equals 18
    '''
    peaks = []

    # get peaks values
    while (number > 0):
        peaks.append(number % 10)
        number = number // 10
    # compute sums of all surfaces of cube
    sums = []
    sums.append(peaks[0] + peaks[1] + peaks[2] + peaks[3])
    sums.append(peaks[0] + peaks[1] + peaks[4] + peaks[5])
    sums.append(peaks[4] + peaks[5] + peaks[6] + peaks[7])
    sums.append(peaks[6] + peaks[7] + peaks[2] + peaks[3])
    sums.append(peaks[1] + peaks[2] + peaks[5] + peaks[6])
    sums.append(peaks[0] + peaks[3] + peaks[4] + peaks[7])
    result = all(sum == 18 for sum in sums)
    
    return result

def get_combination() -> list:
    '''
    get all comiations with sum condition
    '''
    combinations = []
    for combination in permutations('12345678'):
        res = ''.join(combination)
        if check_sum_digits(int(res)):
            combinations.append(res)

    return combinations




if __name__ == '__main__':
    '''
    Есть кубик.
    У кубика восемь вершин и шесть плоскостей. Нормальный обычный кубик.
    Нужно пронумеровать вершины кубика числами от 1 до 8 таким образом, чтобы суммы цифр(номеров вершин) всех плоскостей были равны между собой. Т.е. сумма вершин плоскости1 = сумме вершин плоскости 2 = ….. = сумме вершин плоскости 6.
    Вопросы:
    1. Чему равна сумма вершин каждой плоскости?
    2. Сколько вариантов расположения цифр может быть, если не принимать во внимание вращение кубика в пространстве?
    '''
    values = [i for i in range(1,9,1)]
    surface_sum = find_sum(values)
    # exclude cube rotation 
    count = len(get_combination()) // 6

    print(f'1. Чему равна сумма вершин каждой плоскости? {surface_sum}')

    print(f'2. Сколько вариантов расположения цифр может быть, если не принимать во внимание вращение кубика в пространстве? {count}')

    # верхняя грань 5 8 3 2
    # нижняя грань 4 1 6 7
    