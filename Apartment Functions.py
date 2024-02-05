def apt_search1(city, max_rent, min_beds, pets_allowed = False):
    if pets_allowed:
        print(f"Welcome to GC Property Management!\n Looking up listings in {city} for {min_beds} bedroom apartments with pets allowed, all within a budget of "
              f"${max_rent} per month...")
    else:
        print(f"Welcome to GC Property Management!\n Looking up listings in {city} for {min_beds} bedroom apartments, all within a budget of ${max_rent} per month...")
print(apt_search1("Charlotte", 1200, 3, True))

def apt_search2(city, max_rent, min_beds = False, pets_allowed = False):
    if min_beds and pets_allowed:
        print(f"Welcome to GC Property Management!\n Looking up listings in {city} for 3 bedroom apartments with pets allowed, all within a budget of "
              f"${max_rent} per month...")
    elif min_beds:
        print(f"Welcome to GC Property Management!\n Looking up listings in {city} for 3 bedroom apartments, all within a budget of ${max_rent} per month...")
    elif pets_allowed:
        print(f"Welcome to GC Property Management!\n Looking up listings in {city} for apartments with pets allowed, all within a budget of ${max_rent} per month...")
    else:
        print(f"Welcome to GC Property Management!\n Looking up listings in {city} for apartments, all within a budget of ${max_rent} per month...")
print(apt_search2("Charlotte", 1300, False, True))

plus_one_hundred = lambda x: x + 100
square_num = lambda x: x * x
concatenate = lambda x: "-" + str(x)
divide_by_three = lambda x: x / 3

print(plus_one_hundred(311))
print(square_num(6))
print(concatenate("yo"))
print(divide_by_three(87))
