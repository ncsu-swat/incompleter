#Source: https://stackoverflow.com/questions/29689863/why-do-i-get-typeerror-when-trying-to-do-dot-product
sig = {'a': 1.0, 'b': 2.0, 'c': 3.0}
exp = {'a': (1.0,2.0,3.0), 'b': (1.0,2.0,3.0), 'c': (1.0,2.0,3.0)}
man_dot = {'a': 1*1+1*2+1*3, 'b': 2*1+2*2+2*3, 'c': 3*1+3*2+3*3}

weighted_dict = {}
for s in sig:
    print("this is s:\n{}".format(s))
    for e in exp:
        print("this is e:\n{}".format(e))
        weighted_dict[s] = sum(sig[s] * exp[e])
# weighted_dict should be equivalent to man_dot
# weighted_dict should be {'a': 6, 'c': 18, 'b': 12}