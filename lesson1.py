def number_split(num):
    s = num // 2
    if num % 2 != 0:
        return [s, s + 1]
    else:
        return [s, s]

print(number_split(4))
print(number_split(10))
print(number_split(11))
print(number_split(-9))

#inp = input("yozing; ")

# def asc_desc_none(lst,s):
#     if s == "Asc":
#         lst.sort()
#         return lst
#     elif s == "des":
#         lst.sort(reverse=True)
#         return lst
#     return lst
#
# print(asc_desc_none([4,3,2,1], "Asc"))
# print(asc_desc_none([7,8,11,66], "des"))
# print(asc_desc_none([1,2,3,4], "none"))

def seriec_recictence(lst):
    m = sum(lst)
    if m > 1:
        return m, "ohms"
    return m, "ohm"

print(seriec_recictence([1,5,6,3]))
print(seriec_recictence([16,3.5,6]))
print(seriec_recictence([0.5,0.5]))