side_lengths = []

print("Enter height, width and length on separate lines")
for i in range(3):
    n = int(input("> "))
    side_lengths.append(n)

volume = side_lengths[0] * side_lengths[1] * side_lengths[2]
side_edges = [[0, 1], [0, 2], [1, 2]]
surface_area_total = 0
for i in side_edges:
    surface_area = 2 * (side_lengths[i[0]] * side_lengths[i[1]])
    surface_area_total += surface_area

print(f"Volume: {volume}")
print(f"Surface area: {surface_area_total}")
