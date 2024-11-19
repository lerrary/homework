def introspection_info(obj):
    res = {}
    res.update({'type': str(type(obj))[8:-2]})
    atr = []
    met = []
    for i in dir(obj):
        if 'method' not in str(type(getattr(obj, i))):
            atr.append(i)
    for j in dir(obj):
        if j not in atr:
            met.append(j)
    res.update({'attributes': atr})
    res.update({'methods': met})
    res.update({'module': introspection_info.__module__})
    return res

number_info = introspection_info(42)
print(number_info)
