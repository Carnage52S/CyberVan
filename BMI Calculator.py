def bmi(weight, height):
    '''prints bmi, returns optimal'''
    bmi = (weight * 703) / height ** 2
    print(bmi)
    if bmi < 19:
        return "under"
    elif bmi < 25:
        return "optimal"
    else:
        return "over"
    

