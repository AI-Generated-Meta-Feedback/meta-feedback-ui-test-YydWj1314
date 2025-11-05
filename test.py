
a = [(5, 3), (2, 1), (5, 2)]
assert insertion_sort_by_shelf(a) == [(2, 1), (5, 3), (5, 2)]


b = [(1, 100), (1, 200), (1, 300)]
assert insertion_sort_by_shelf(b) == [(1, 100), (1, 200), (1, 300)]


c = [(3, 10), (2, 20), (4, 30), (2, 40)]
assert insertion_sort_by_shelf(c) == [(2, 20), (2, 40), (3, 10), (4, 30)]


d = [(1, 7), (2, 8), (3, 9)]
assert insertion_sort_by_shelf(d) == [(1, 7), (2, 8), (3, 9)]

e = [(3, 9), (2, 8), (1, 7)]
assert insertion_sort_by_shelf(e) == [(1, 7), (2, 8), (3, 9)]

f = [(1, 7), (2, 8), (3, 9)]
assert insertion_sort_by_shelf(e) == [(1, 7), (2, 8), (3, 9)]

g = [(1, 7)]
assert insertion_sort_by_shelf(e) == [(1, 7)]

