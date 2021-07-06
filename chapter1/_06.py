from _05 import n_gram

sequence1 = "paraparaparadise"
sequence2 = "paragraph"
X = n_gram(sequence1,2,"char")
Y = n_gram(sequence2,2,"char")
print(X)
print(Y)

union = list(set(X+Y))
intersection = list(set([n for n in X if n in Y]))
diff_X = [n for n in X if n not in Y]
diff_Y = [n for n in Y if n not in X]
print(f"union        = {union}")
print(f"intersection = {intersection}")
print(f"diff_X       = {diff_X}")
print(f"diff_Y       = {diff_Y}")
is_in_X = "se" in X
is_in_Y = "se" in Y
print(f"seはXに含まれるか？:{is_in_X}")
print(f"seはYに含まれるか？:{is_in_Y}")

