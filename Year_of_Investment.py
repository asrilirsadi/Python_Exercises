# def calculate_years(principal, interest, tax, desired):
    
#     for i in range(100):
#         if principal == desired:
#             print(0)
#             break
#         elif principal > desired:
#             break
#         elif principal < desired:
#             principal = (principal*(1+interest)) - (principal*interest*tax)
#             print('After {} year -> {}'.format(i+1, principal))
    
#     print(i)

# calculate_years(1000, 0.05, 0.18, 1100)
# calculate_years(1200, 0.17, 0.05, 2000)
# calculate_years(1500, 0.07, 0.6, 5000)

# CARA LAIN:
def calculate_years(principal, interest, tax, desired):
    year = 0
    while (principal < desired):
        principal = principal + (principal*interest) - (principal*interest*tax)
        year += 1
    print(year)

calculate_years(1000, 0.05, 0.18, 1100)
calculate_years(1200, 0.17, 0.05, 2000)
calculate_years(1500, 0.07, 0.6, 5000)