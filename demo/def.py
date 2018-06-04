# 使用任意数量实参
def make_pizza(size, *toppings):
    print('\nMaking a ' + str(size) + 
            '-inch pizza with the fllowing toppings: ')
    for topping in toppings:
        print("-" + topping)
make_pizza(12, 'mushrooms', 'green pappers', 'extra cheese')

# 使用任意数量的关键字实参
def build_profile(first, last, **user_info):
    profile = {};
    profile['first_name'] = first;
    profile['last_name'] = last;
    for key,value in user_info.items() :-
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', localtion = 'princeton', field = 'physics')
print(user_profile) 
