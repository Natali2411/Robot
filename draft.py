for i in range(len(res)):
    if v_symbol1 == res[i]["symbol"]:
        r[v_symbol1] = res[i]["askPrice"]
    if v_symbol2 == res[i]["symbol"]:
        r[v_symbol2] = res[i]["askPrice"]
    if v_symbol3 == res[i]["symbol"]:
        r[v_symbol3] = res[i]["askPrice"]
    if v_symbol4 == res[i]["symbol"]:
        r[v_symbol4] = res[i]["askPrice"]
if len(r) == 2:
    pass  # rate = float(r[v_symbol2])/float(r[v_symbol1])*float(r[v_symbol3])*float(r[v_symbol4])