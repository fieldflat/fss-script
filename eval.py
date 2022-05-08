import sys
from utils import Utils

class Eval:
    def __init__(self):
        """ init space """

    def dpf_2party(id: int, k_list, x: int, lmd: int, mod: int, PRG):
        # step1: setting PRG
        print("step1: recieving PRG ...")
        print("step1: done. \n")

        # step2: parse input x
        print("step2: parse input x ... ")
        x = Utils.int2bitstr(x, lmd)
        n = len(x)
        print("    x = {}".format(x))
        print("    n = {}".format(n))
        print("step2: done. \n")

        # step3: parse k_list as s0|s1|t0|t1, cw_list, w
        print("step3: parse k_list as s0|s1|t0|t1, cw_list, w ... ")
        s0 = k_list[0][0]
        s1 = k_list[0][1]
        t0 = k_list[0][2]
        t1 = k_list[0][3]
        cw_list = k_list[1]
        w = k_list[2]
        print("    s0 = {}".format(s0))
        print("    s1 = {}".format(s1))
        print("    t0 = {}".format(t0))
        print("    t1 = {}".format(t1))
        print("step3: done. \n")

        # step4: set S
        print("step4: set S ... ")
        S = s0 if x[0] == '0' else s1
        print("    S  = {}".format(S))
        print("step4: done. \n")
        # step5: set T
        print("step5: set T ... ")
        T = t0 if x[0] == '0' else t1
        print("    T  = {}".format(T))
        print("step5: done. \n")

        for i in range(0, n-1):
            # step7: parse G(S) as s0|s1|t0|t1
            print("step7: parse G(S) as s0|s1|t0|t1 ...")
            gs = PRG(S)
            print("    PRG({}) = {}".format(S, gs))
            s = {}
            t = {}
            s["0"] = gs[0:lmd]
            s["1"] = gs[lmd:2*lmd]
            t["0"] = gs[2*lmd]
            t["1"] = gs[2*lmd+1]
            print("    s0 = {}".format(s["0"]))
            print("    s1 = {}".format(s["1"]))
            print("    t0 = {}".format(t["0"]))
            print("    t1 = {}".format(t["1"]))
            print("step7: done. \n")

            # step8: parse CW
            print("step8: parse CW ...")
            cw = cw_list[2*i + int(T)]
            cs = {}
            ct = {}
            cs[T] = {
                "0": cw[0:lmd],
                "1": cw[lmd:2*lmd],
            }
            ct[T] = {
                "0": cw[2*lmd],
                "1": cw[2*lmd+1],
            }
            print("    cs = {}".format(cs))
            print("    ct = {}".format(ct))
            print("step8: done. \n")

            # step9: set S
            print("step9: set S ...")
            print("    x[(i+1)] = {} because i+1 = {} and x = {}".format(x[(i+1)], i+1, x))
            print("    s[x[(i+1)]] = {}".format(s[x[(i+1)]]))
            print("    cs[T][x[(i+1)]] = {}".format(cs[T][x[(i+1)]]))
            S = Utils.xor(s[x[(i+1)]], cs[T][x[(i+1)]], lmd)
            print("    S = {}".format(S))
            print("step9: done. \n")

            # step10: set T
            print("step10: set T ...")
            print("    x[(i+1)] = {} because i+1 = {} and x = {}".format(x[(i+1)], i+1, x))
            print("    t[x[(i+1)]] = {}".format(t[x[(i+1)]]))
            print("    ct[T][x[(i+1)]] = {}".format(ct[T][x[(i+1)]]))
            T = Utils.xor(t[x[(i+1)]], ct[T][x[(i+1)]], 1)
            print("    T = {}".format(T))
            print("step10: done. \n")

        # step12: return
        print("step12: return ... ")
        print("    S = {}".format(S))
        print("    PRG(S) = {}".format(PRG(S)))
        print("    int(PRG(S), 2) = {}".format(int(PRG(S), 2)))
        print("    w = {}".format(w))
        print("    (int(PRG(S), 2) * w) % mod = {}".format((int(PRG(S), 2) * w) % mod))
        return (int(PRG(S), 2) * w) % mod