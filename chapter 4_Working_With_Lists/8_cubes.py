first_10_cubes = [value ** 3 for value in range(1,11)]
for value_per_cube in first_10_cubes:
    print(value_per_cube) 

first_10_cubes = []
for value in range(1,11):
    cube_set = value ** 3
    first_10_cubes.append(cube_set)
for value_per_cube in first_10_cubes:
    print(value_per_cube)