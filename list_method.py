list_of_colors = ["blue", "red", "white", "purple", "green"]
print(list_of_colors.index("green"))

list_of_colors.append( "wine")
print(list_of_colors)
list_of_colors.insert(3, "brown")
print(list_of_colors)
list_of_numbers = [23, 2, 34, 5, 23, 45, 65, 232, 6, 2, 44444, 54, 90,]
list_of_numbers.sort()
print(list_of_numbers)
list_of_colors.sort()
print(list_of_colors)
alpha = ["A", "a", "D", "H", "h"]
alpha.sort(key=str.lower)
print(alpha)
list_of_colors[0] = ""
list_of_colors.remove("brown")

