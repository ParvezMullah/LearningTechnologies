nums = [1, 2, 3, 4, 5]

square_nums = [n*n for n in nums]
print(square_nums)

even_nums = [n for n in nums if n % 2 == 0]
print(even_nums)


names = ["parvez", "atif", "aairah"]
ages = [25, 14, 3]

name_age_dict = {name: age for name, age in zip(names, ages)}
print(name_age_dict)
