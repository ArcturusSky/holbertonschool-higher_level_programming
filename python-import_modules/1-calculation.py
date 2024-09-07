#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as cal
    a = 10
    b = 5
    addresult = cal.add(a, b)
    subresult = cal.sub(a, b)
    mulresult = cal.mul(a, b)
    divresult = cal.div(a, b)

    print("{} + {} = {}".format(a, b, addresult))
    print("{} - {} = {}".format(a, b, subresult))
    print("{} * {} = {}".format(a, b, mulresult))
    print("{} / {} = {}".format(a, b, divresult))
