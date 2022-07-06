__a = 7
__b = 8
__c = 2


def triangle_area(a=__a, b=__b, c=__c):
    half_perimetr = (a + b + c)/3
    return pow(half_perimetr*(half_perimetr-a)*(half_perimetr-b)*(half_perimetr-c), 1/2)


def triangle_perimetr(a=__a, b=__b, c=__c):
    return a + b + c