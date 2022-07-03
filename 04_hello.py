for i in range ( 1,21):
    with open(f'tables/Multipication_table_of {i}', 'w') as f:
        for j in range(1,11):
            f.write(f"{i} x {j} = {i*j}\n")
            


