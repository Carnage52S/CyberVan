def multmult(l1, l2):
    '''multiplies all elements of both lists by each other'''
    products = []
    for i in l1:
        for j in l2:
            product = i * j
            products.append(product)
    return products