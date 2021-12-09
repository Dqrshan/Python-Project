# # T = ("the", "quick", "brown", "fox")
# # L = []
# # for e in T:
# #     e = f"{e[1:]}{e[0]}ay"
# #     # e = e[1:] + e[0] + "ay"
# #     L.append(e)
# # print(tuple(L))

# T2 = ("hetay", "uickqay", "rownbay", "oxfay")
# L2 = []
# string = ""
# for e in T2:
#     e = f"{e[-3]}{e[0:-3]}"
#     L2.append(e)

# for i in L2:
#     string += f"{i} "
# print(string)
L = [1, 2, [3, 4], 5]
x = L[2]  # Noob coder moment
y = L[2][0:]  # Pro coder moment
print(f"x = {x}\ny = {y}")
print(x == y)
print(x is y)
