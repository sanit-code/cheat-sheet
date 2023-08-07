import threading
import time


def basic_types():
    # ############################## TYPES ##############################
    t1 = 3.141516               # Double-precision float
    t2 = int('14')              # Convert to int    ->  14
    t3 = str(39)                # Convert to string ->  '39'


def basic_operations():
    # ############################## BASIC OPERATIONS ##############################
    b1 = 10 ** 2                # Exponentiation        ->  100
    b2 = 5 // 2                 # Integer division      ->  2
    b3 = 7 % 5                  # Modulus               ->  2


def general():
    # ############################## RANGE ##############################
    t1 = [i for i in range(4)]              # [0,1,2,3]
    t2 = [i for i in range(0, -10, -2)]     # [0,-2,-4,-6,-8]
    for i in range(3):                      # Iterates: 0,1,2
        test = i
    for key in {'a': 1, 'b': 2}:            # Iterates: 'a', 'b'
        test = key

    # ############################## LAMBDA FUNCTION ##############################
    conditional_lambda = map(       # Conditional lambda
        lambda x, y: 1 if x > y else 0,
        [1, 2, 3],
        [3, 2, 1]
    )

    # ############################## CUSTOM EXCEPTION ##############################
    class CustomException(Exception):
        pass
    try:
        raise CustomException('Test msg')
    except CustomException as err:
        import traceback
        tb = traceback.format_exc()         # Stack trace
        msg = str(err)                      # Exception string message      ->  'Test msg'
        debug_point = True
    finally:
        bla = True

    # ############################## GENERATOR ##############################
    def seq():
        for i in range(10):
            yield i
    data = [x for x in seq()]           # -> [0,1,2,3,...,9]

    return


def classes():
    class A:
        a = 1

    class B(A):                 # Inheritance
        __b = 2                 # Private property

        @staticmethod
        def foo():              # Static method
            return 'y'
    a = A()
    b = B()
    c1 = hasattr(a, 'a')        # Has attribute     ->  True
    c2 = getattr(b, 'a')        # Get attribute     ->  1
    c3 = issubclass(B, A)       # Check subclass    ->  True

    return


def strings():
    # ############################## STRINGS ##############################
    b4 = "abc" * 3                  # String replication        ->  'abcabcabc'
    f9 = 'test'.upper()             # Upper Case                ->  'TEST'
    f10 = 'TEST'.lower()            # Lower Case                ->  'test'
    f11 = 'test'.startswith('te')   # Has prefix                ->  True
    f12 = 'test'.endswith('st')     # Has sufix                 ->  True
    f13 = 'ab cd e'.find('d ')      # Find index of substring   ->  4
    f14 = 'abcd'.find('b', 2, 4)    # Not found in [2,4)        ->  -1

    # ############################## FORMATTING ##############################
    f1 = 1003.141516
    f2 = "test"
    f3 = f"{f1:.3f}"            # Round 3 decimal places    ->  '1003.142'
    f4 = f"{f1:.2e}"            # Exponent notation         ->  '1.00e+03'
    f5 = f"{f2:>10s}"           # Align right               ->  '      test'
    f6 = f"{f2:<10s}"           # Align left                ->  'test      '
    f7 = f"{f2:^10s}"           # Align center              ->  '   test   '
    f8 = f"{f2:w^10s}"          # Add fill to any align     ->  'wwwtestwww'


def arrays():
    # ############################## ARRAYS ##############################
    lst = [1, 2, 3, 4]
    str_lst = ["4", "23", "1"]

    l1 = str_lst[1:-1]                              # Slice [1,2)               ->  ['23']
    l2 = '23' in str_lst                            # Check if value in list    ->  True
    l3 = str_lst.index('1')                         # Find string               ->  2
    str_lst.insert(2, 'x')                          # Insert at position        ::  str_lst == ['4', '23', 'x', '1']
    del str_lst[2]                                  # Remove from position      ::  str_lst == ['4', '23', '1']

    a2 = ["ab"] * 3                                 # Array replication         ->  ['ab', 'ab', 'ab']

    # ############################## BREAK STRING ##############################
    a1 = list("abcdefghijklmnopqrstuvwxyz")         # Break into letters        ->  ['a', 'b', 'c', ..., 'z']
    a2 = "  spt  by  whitespace  ".split()          # Break by whitespace       ->  ['spt', 'by', 'whitespace']
    a3 = " spt, by deli,  ok  ".split(', ')         # Break by delimiter        ->  [' spt', 'by deli', ' ok  ']

    # ############################## MAP ##############################
    a4 = map(int, str_lst)                          # Apply function to all     ->  iterable of [4,23,1]
    a5 = map(lambda x, y: x + y, a4, [5, 6, 7])     # Combine 2 lists           ->  iterable of [4+5, 23+6, 1+7]

    # ############################## REDUCERS ##############################
    from functools import reduce
    import math
    s1 = sum(lst)                                   # Sum all                   ->  10
    s2 = math.prod(lst)                             # Multiply all              ->  24
    s3 = "".join(str_lst)                           # Concatenate all           ->  '4231'
    s4 = all(n > 0 for n in lst)                    # Check all with condition  ->  True
    s5 = any(n == 2 for n in lst)                   # Check any with condition  ->  True
    s6 = reduce(lambda x, y: x * 2 + y, lst)        # Custom reduce             ->  (((1*2+2)*2+3)*2+4)

    # ############################## CUSTOM SORT ##############################
    import functools

    def comp(a, b):
        if len(a) < len(b):
            return -1
        elif len(b) > len(a):
            return 1
        return 0

    data = ['ab', 'c']
    data.sort(key=functools.cmp_to_key(comp))  # Sort with function
    data.sort(key=len) # Sort by value of specified function

    return


def dictionary():
    # ############################## DICTIONARY ##############################
    C = {'a': 1, 'b': 2}
    D = {k: v for k, v in zip(['b', 'c'], [3, 4])}
    d1 = 'b' in C                   # Check key in dictionary   ->  True
    d2 = 2 in C.values()            # Check value in dictionary ->  True
    combine = {**C, **D}            # Value from last dict overrides -> {'a': 1, 'b': 3, 'c': 4}
    del C['b']                      # Remove from dictionary

    return


def other_data_structures():
    # ############################## SET ##############################
    A = {0, 2, 4, 6, 8}
    B = {1, 2, 3, 4, 5}
    union = A | B                   # -> {0,1,2,3,4,5,6,8}
    intersection = A & B            # -> {2,4}
    difference = A - B              # -> {0,6,8}
    sym_difference = A ^ B          # -> {0,1,3,5,6,8}
    contains = {0, 1} <= {0, 1, 2}  # Subset of     -> True
    A.add(-1)                       # Add to set
    A.remove(-1)                    # Remove from set

    # ############################## DEQUEUE ##############################
    import collections
    dq = collections.deque([1,2])   # Initialization
    dq.append(3)                    # deque([1, 2, 3])
    dq.appendleft(0)                # deque([0, 1, 2, 3])
    p1 = dq.pop()                   # deque([0, 1, 2])          -> 3
    p2 = dq.popleft()               # deque([1, 2])             -> 0

    # ############################## HEAP / PRIORITY QUEUE ##############################
    import heapq

    class Node(object):                     # Custom representation for custom comparison
        def __init__(self, priority: int, data: dict = None):
            self.prio = priority
            self.data = data

        def __lt__(self, other):
            return self.prio < other.prio

    hp = [Node(5), Node(4), Node(3), Node(2), Node(1)]
    heapq.heapify(hp)                       # hp = [1,2,3,5,4], where hp[i] <= hp[2*i+1] and hp[i] <= hp[2*i+2]
    v1 = heapq.heappop(hp)                  # ->  1
    heapq.heappush(hp, Node(0))             # hp = [0,2,3,5,4]

    return                                  # Unnecessary line for debugging


def file_examples():
    # ############################## FILE I/O ##############################
    with open("test.txt", "w") as test_file:        # Write and replace file
        test_file.write("ab\n")                     # No extra '\n' is added
        test_file.writelines(["cd\n", "ef\n", "gh"])

    # Files close automatically when "with" scope ends

    with open("test.txt", "r") as test_file:        # Read file
        a = test_file.read(5)                       # Read 5 bytes                      ->  'ab\ncd'
        b = test_file.readline(4)                   # Read max 4 bytes of current line  ->  '\n'
        c = test_file.readline()                    # Read until end of line            ->  'ef\n'
        d = test_file.read()                        # Read everything else as a string  ->  'gh'

        test_file.seek(0)                           # Return to the 0th byte
        e = test_file.readlines()                   # Read all, as a array of strings  -> ['ab\n', 'cd\n', 'ef\n', 'gh']

        debug_breakpoint = True                     # Unnecessary line used for debugging

    with open("test.txt", "a") as test_file:        # Append at end of file
        test_file.write("\nextra\n")


def regex():
    # ############################## REGEX ##############################
    import re
    r1 = re.compile(r'(\d)-(\d)')

    # Single match
    m1 = r1.search('Test 1-2 3-4 test')
    s1 = m1.groups()                                    # All groups        ->  ('1', '2')
    s2 = m1.group(0)                                    # Match             ->  '1-2'
    s3 = m1.group(1)                                    # First group       ->  '1'
    s4 = m1.group(2)                                    # Second group      ->  '2'

    # All matches
    m2 = r1.findall('Test 1-2 3-4 test')                # -> [('1', '2'), ('3', '4')]

    # Replace
    replaced = r1.sub('changed', 'Test 1-2 3-4 test')   # -> 'Test changed changed test'

    # Others
    r2 = re.compile(r'abc', re.I)                       # Case-insensitive

    return


def json():
    # ############################## JSON ##############################
    import json
    j1 = '{"a":1, "b":2}'
    j2 = json.loads(j1)                 # Parse             ->  {'a':1, 'b': 2}
    j3 = json.dumps(j2)                 # Stringify         ->  '{"a": 1, "b": 2}'

    with open("test.json", "w") as f:
        json.dump(j2, f, indent=2)      # Write to file

    with open("test.json", "r") as f:
        j4 = json.load(f)               # Parse from file   ->  {'a':1, 'b': 2}
        debug_line = True


def datetime_examples():
    # ############################## DATETIME ##############################
    from datetime import date, datetime, time
    d1 = time()                                 # Time initialized as 00:00:00
    d2 = date.today()                           # Current day
    d3 = datetime.now()                         # Current datetime
    d4 = datetime.combine(d2, d1)               # Combine date and time into datetime

    return


if __name__ == '__main__':
    basic_types()
    basic_operations()
    general()
    classes()
    strings()
    arrays()
    dictionary()
    other_data_structures()
    file_examples()
    regex()
    json()
    datetime_examples()
