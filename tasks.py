from exceptions import TaskException


def task1(x: [float, int], y: [float, int]) -> [float, int]:
    """
    Даны действительные числа x и y.
    Вернуть (|x| − |y|) / (1+ |xy|)
    """
    return (abs(x) - abs(y)) / (1 + abs(x * y))


def task2(a: [float, int]) -> tuple[[float, int], [float, int]]:
    """
    Дана длина ребра куба.
    Вернуть кортеж с объемом куба и площадью его боковой поверхности.
    """
    if a < 0:
        raise TaskException
    return a ** 3, a ** 2


def task3(a: [float, int], b: [float, int]) -> [float, int]:
    """
    Даны два катета прямоугольного треугольника.
    Вернуть длину гипотенузы.
    """
    if a < 0 or b < 0:
        raise TaskException
    return (a ** 2 + b ** 2) ** 0.5


def task4(string: str) -> str:
    """
    На вход подаётся строка.
    Вернуть строку равную предпоследнему символу введенной строки.
    """
    return string[-2]


def task5(string: str) -> str:
    """
    На вход подаётся строка.
    Вернуть строку равную первым пяти символам введенной строки.
    """
    return string[0:5]


def task6(string: str) -> str:
    """
    На вход подаётся строка.
    Вернуть строку равную введенной строку без последних двух символов.
    """
    return string[0:-2]


def task7(string: str) -> str:
    """
    На вход подаётся строка.
    Вернуть строку равную всем элементам введенной строки с четными индексами.
    """
    return string[0::2]


def task8(string: str) -> str:
    """
    На вход подаётся строка.
    Вернуть строку равную третьему символу введенной строки.
    """
    return string[2]


def task9(string: str) -> str:
    """
    Дана строка. Если длина строки больше 10 символов, то вернуть новую строку
    с 3 восклицательными знаками в конце ('!!!') и вывести на экран.
    Если меньше 10, то вывести на экран второй символ строки
    """
    return string + "!!!" if len(string) > 10 else string[1]


def task10(string: str) -> tuple[str, [None, str]]:
    """
    Дана строка. Вернуть букву, которая находится в середине этой строки.
    Также, если эта центральная буква равна первой букве в строке, то вернуть часть строки между первым и
    последним символами исходной строки.
    (подсказка: для получения центральной буквы, найдите длину строки и разделите ее пополам.
    Для создания результирующий строки используйте срез)
    """
    c = string[len(string) // 2]
    return (c, None) if c != string[0] else (c, string[1:-1])


def task11(string: str) -> bool:
    """
    Напишите функцию которая проверяет является ли строка палиндромом.
    Палиндром — это слово или фраза, которые одинаково читаются слева направо и справа налево.
    """
    return True if string == string[::-1] else False


def task12(string: str, symbol: str) -> int:
    """
    Напишите функцию которая возвращает сколько раз символ встречается в строке
    """
    return string.count(symbol)


def task13(number: int) -> bool:
    """
    Дано число. Если это число делится на 1000 без остатка, то верните True иначе False
    """
    return number % 1000 == 0


def task14(guests_count: int) -> str:
    """
    В семье N свадьба. Они решили выбрать заведение, где будут праздновать в зависимости от количества гостей.
    Если их будет больше 50 - закажут ресторан, если от 20 до 50 - кафе, а если меньше 20 - отпразднуют дома.
    Вернуть "ресторан", "кафе", "дом" в зависимости от количества гостей.
    """
    if guests_count < 0:
        raise TaskException
    if guests_count < 20:
        place = "дом"
    elif guests_count <= 50:
        place = "кафе"
    else:
        place = "ресторан"
    return place


def task15(number: int) -> tuple[int, int]:
    """
    Дано число. Найти сумму и произведение его цифр.
    """
    a = list(str(number))
    s = 0
    p = 1
    for i in a:
        s += int(i)
        p *= int(i)
    return s, p


def task16(start: int, end: int) -> list[int]:
    """
    Два натуральных числа называют дружественными, если каждое из них равно сумме всех делителей другого,
    кроме самого этого числа. Реализовать функцию для поиска всех пар дружественных чисел в заданном диапазоне
    """
    def summa(m: int):
        summ = 1
        for i in range(2, int(m / 2)):
            if m % i == 0:
                summ += i
        return summ
    friend = []
    for j in range(start, end + 1):
        a = summa(j)
        b = summa(a)
        if b == j != a and a < end:
            friend.append(j)
    return friend


def task17(n: int) -> float:
    """
    Для заданного числа N составьте программу вычисления суммы
    S=1+1/2+1/3+1/4+...+1/N, где N – натуральное число
    """
    s = 0.0
    for i in range(1, n + 1):
        s += 1/i
    return s


def task18(number: [int, float], func_number: int) -> float:
    """
    Написать в отдельном файле 12 функций по переводу одних единиц измерения в другие.
    Импортировать написанные функции в данный файл и написать программу которая принимает на вход число и
    номер функции и возвращает результат
    1. Дюймы в сантиметры
    2. Сантиметры в дюймы
    3. Мили в километры
    4. Километры в мили
    5. Фунты в килограммы
    6. Килограммы в фунты
    7. Унции в граммы
    8. Граммы в унции
    9. Галлон в литры
    10. Литры в галлоны
    11. Пинты в литры
    12. Литры в пинты
    """


def micro_calc(a: [float, int], b: [float, int], sign: str) -> [float, int, str]:
    """
    Даны 2 действительных числа и строка с арифметическим знаком ('+', '-', ':', '*', '^')
    Необходимо вернуть результат арифметической операции
    В случае ошибки вычислений или неизвестного знака вернуть строку "error"
    """
    if sign == '+':
        return a + b
    elif sign == '-':
        return a - b
    elif sign == ':':
        if b == 0:
            raise TaskException
        return a / b
    elif sign == '*':
        return a * b
    elif sign == '^':
        return a ** b
    else:
        raise TaskException


def big_letters(phrase: str) -> str:
    """
    Напишите функцию, которая принимает строку, состоящую только из букв ASCII и пробелов, и возвращает
    эту строку печатными буквами шириной 5 символов и высотой 7 символов с одним пробелом между символами.
     - Заглавные буквы должны состоять из соответствующих заглавных букв.
     - Не имеет значения, состоит ли ввод из строчных или прописных букв.
     - Любые начальные и/или конечные пробелы во входных данных следует игнорировать.
     - Пустые строки или подобные строки, содержащие только пробелы, должны возвращать пустую строку.
     - Остальные пробелы (между буквами и/или словами) должны рассматриваться как любые другие символы.
       Это означает, что на входной пробел будет шесть пробелов в выводе или кратно шести,
       если пробелов было больше - плюс один от предыдущего символа!
     - Конечные пробелы должны быть удалены в результирующей строке.
     - Строка должна быть отформатирована таким образом, чтобы при передаче функции Python print()
       отображался желаемый результат (см., например, ниже)

      AAA  BBBB   CCC  DDDD  EEEEE FFFFF  GGG  H   H IIIII JJJJJ K   K L     M   M N   N  OOO  PPPP   QQQ  RRRR   SSS
     A   A B   B C   C D   D E     F     G   G H   H   I       J K  K  L     MM MM NN  N O   O P   P Q   Q R   R S   S
     A   A B   B C     D   D E     F     G     H   H   I       J K K   L     M M M N   N O   O P   P Q   Q R   R S
     AAAAA BBBB  C     D   D EEEEE FFFFF G GGG HHHHH   I       J KK    L     M   M N N N O   O PPPP  Q   Q RRRR   SSS
     A   A B   B C     D   D E     F     G   G H   H   I       J K K   L     M   M N   N O   O P     Q Q Q R R       S
     A   A B   B C   C D   D E     F     G   G H   H   I       J K  K  L     M   M N  NN O   O P     Q  QQ R  R  S   S
     A   A BBBB   CCC  DDDD  EEEEE F      GGG  H   H IIIII JJJJ  K   K LLLLL M   M N   N  OOO  P      QQQQ R   R  SSS

    TTTTT U   U V   V W   W X   X Y   Y ZZZZZ
      T   U   U V   V W   W X   X Y   Y     Z
      T   U   U V   V W   W X   X Y   Y     Z
      T   U   U V   V W   W  X X   Y Y     Z
      T   U   U V   V W W W   X     Y     Z
      T   U   U V   V W W W  X X    Y    Z
      T   U   U  V V  W W W X   X   Y   Z
      T    UUU    V    W W  X   X   Y   ZZZZZ
    """
    letters = {'a': [' AAA ', 'A   A', 'A   A', 'AAAAA', 'A   A', 'A   A', 'A   A'],
               'b': ['BBBB ', 'B   B', 'B   B', 'BBBB ', 'B   B', 'B   B', 'BBBB '],
               'c': [' CCC ', 'C   C', 'C    ', 'C    ', 'C    ', 'C   C', ' CCC '],
               'd': ['DDDD ', 'D   D', 'D   D', 'D   D', 'D   D', 'D   D', 'DDDD '],
               'e': ['EEEEE', 'E    ', 'E    ', 'EEEEE', 'E    ', 'E    ', 'EEEEE'],
               'f': ['FFFFF', 'F    ', 'F    ', 'FFFFF', 'F    ', 'F    ', 'F    '],
               'g': [' GGG ', 'G   G', 'G    ', 'G GGG', 'G   G', 'G   G', ' GGG '],
               'h': ['H   H', 'H   H', 'H   H', 'HHHHH', 'H   H', 'H   H', 'H   H'],
               'i': ['IIIII', '  I  ', '  I  ', '  I  ', '  I  ', '  I  ', 'IIIII'],
               'j': ['JJJJJ', '    J', '    J', '    J', '    J', '    J', 'JJJJ '],
               'k': ['K   K', 'K  K ', 'K K  ', 'KK   ', 'K K  ', 'K  K ', 'K   K'],
               'l': ['L    ', 'L    ', 'L    ', 'L    ', 'L    ', 'L    ', 'LLLLL'],
               'm': ['M   M', 'MM MM', 'M M M', 'M   M', 'M   M', 'M   M', 'M   M'],
               'n': ['N   N', 'NN  N', 'N   N', 'N N N', 'N   N', 'N  NN', 'N   N'],
               'o': [' OOO ', 'O   O', 'O   O', 'O   O', 'O   O', 'O   O', ' OOO '],
               'p': ['PPPP ', 'P   P', 'P   P', 'PPPP ', 'P    ', 'P    ', 'P    '],
               'q': [' QQQ ', 'Q   Q', 'Q   Q', 'Q   Q', 'Q Q Q', 'Q  QQ', ' QQQQ'],
               'r': ['RRRR ', 'R   R', 'R   R', 'RRRR ', 'R R  ', 'R  R ', 'R   R'],
               's': [' SSS ', 'S   S', 'S    ', ' SSS ', '    S', 'S   S', ' SSS '],
               't': ['TTTTT', '  T  ', '  T  ', '  T  ', '  T  ', '  T  ', '  T  '],
               'u': ['U   U', 'U   U', 'U   U', 'U   U', 'U   U', 'U   U', ' UUU '],
               'v': ['V   V', 'V   V', 'V   V', 'V   V', 'V   V', ' V V ', '  V  '],
               'w': ['W   W', 'W   W', 'W   W', 'W W W', 'W W W', 'W W W', ' W W '],
               'x': ['X   X', 'X   X', ' X X ', '  X  ', ' X X ', 'X   X', 'X   X'],
               'y': ['Y   Y', 'Y   Y', ' Y Y ', '  Y  ', '  Y  ', '  Y  ', '  Y  '],
               'z': ['ZZZZZ', '    Z', '   Z ', '  Z  ', ' Z   ', 'Z    ', 'ZZZZZ'],
               ' ': ['     ', '     ', '     ', '     ', '     ', '     ', '     ']}
    phrase = phrase.casefold()
    phrase = phrase.rstrip()
    phrase = phrase.strip()
    if phrase == '':
        return ''
    for el in phrase:
        if el.isalpha() is False and el != ' ':
            phrase = phrase.replace(el, '')
    bl = []
    for i in range(7):
        bl.append('')
        for ltr in phrase:
            bl[i] += letters[ltr][i] + ' '
        while bl[i][-1] == ' ':
            bl[i] = bl[i].removesuffix(' ')
        if i != 6:
            bl[i] = bl[i] + '\n'
    res = str()
    for el in bl:
        res += el
    return res


def perfect_square(square: str) -> bool:
    """
    Напишите функцию, которая проверяет входную строку. Если строка представляет собой идеальный квадрат,
    верните true, в противном случае — false.
     - Символ '.' — правильный квадрат (1x1)
     - Правильные квадраты могут содержать только '.' и необязательно '\n' (перевод строки).
     - Идеальные квадраты должны иметь одинаковую ширину и высоту.
    """
    sq_list = [[]]
    i = 0
    for el in square:
        if el == '.':
            sq_list[i] += el
        else:
            sq_list.append([])
            i += 1
    if len(sq_list) == len(sq_list[0]):
        for i in range(len(sq_list) - 1):
            if sq_list[i] != sq_list[i + 1]:
                return False
        return True
    else:
        return False


def task_with_square_brackets(string_input: str) -> str:
    """
    Напишите программу которая принимает на вход строку вида 2[a]3[bc] или 2[a2[bc]]
    и возвращает строку сгененрированную по следующим правилам:
     - нужно повторить символы заключённые в квадратные скобки столько раз, какое число указано перед скобками
     - нужно соблюдать порядок действий как с обычными скобками (первым выполняются действия внутри скобок)
     - вложенность может быть любая
     - строка на входе в функцию всегда валидна
    """

