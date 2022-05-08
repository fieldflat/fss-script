import random
import sys
from utils import Utils
from party import Party


class Gen:
    def __init__(self):
        """ init section """

    # Generation of Gen key
    def dpf_2party(a: int, b: int, lmd: int, seed: bytes, mod: int):
        # step0: initializing
        print("step0: initializing")
        a_str = Utils.int2bitstr(a, lmd)
        n = len(a_str)
        party0, party1 = Party(0), Party(1)
        print("    a_str = {}".format(a_str))
        print("    n = {}".format(n))
        print("step0: done. \n")

        # step1: generate PRG
        print("step1: generate PRG ...")
        print("    lmd = {}".format(lmd))
        print("    seed = {}".format(seed))
        print("    generating PRG ...")
        PRG = Utils.prg(lmd, 2*lmd+2, seed)
        print("    PRG(a) = {}".format(PRG(a_str)))
        print("step1: done.\n")

        # step2: choose random seeds of S
        print("step2: choose random seeds of S ...")
        seed_s0, seed_s1 = Utils.get_random_bits(lmd), Utils.get_random_bits(lmd)
        seed_s0_err = Utils.get_random_bits(lmd)
        seed_s1_err = seed_s0_err
        party0.seed_s[a_str[-1]] = seed_s0
        party1.seed_s[a_str[-1]] = seed_s1
        party0.seed_s[Utils.xor(a_str[-1], "1", 1)] = seed_s0_err
        party1.seed_s[Utils.xor(a_str[-1], "1", 1)] = seed_s1_err
        party0.seed_s_tmp[a_str[-1]] = seed_s0
        party1.seed_s_tmp[a_str[-1]] = seed_s1
        party0.seed_s_tmp[Utils.xor(a_str[-1], "1", 1)] = seed_s0_err
        party1.seed_s_tmp[Utils.xor(a_str[-1], "1", 1)] = seed_s1_err
        print("    a_str[-1] = {} because a_str = {}".format(a_str[-1], a_str))
        print("    party0.seed_s['0'] = {}".format(party0.seed_s['0']))
        print("    party0.seed_s['1'] = {}".format(party0.seed_s['1']))
        print("    party1.seed_s['0'] = {}".format(party1.seed_s['0']))
        print("    party1.seed_s['1'] = {}".format(party1.seed_s['1']))
        print("step2: done. \n")

        # step3: choose random bits of T
        print("step3: choose random bits of T ... ")
        seed_t0 = Utils.get_random_bits(1)
        seed_t1 = Utils.xor("1", seed_t0, 1)
        seed_t0_err = Utils.get_random_bits(1)
        seed_t1_err = seed_t0_err
        party0.seed_t[a_str[-1]] = seed_t0
        party1.seed_t[a_str[-1]] = seed_t1
        party0.seed_t[Utils.xor(a_str[-1], "1", 1)] = seed_t0_err
        party1.seed_t[Utils.xor(a_str[-1], "1", 1)] = seed_t1_err
        party0.seed_t_tmp[a_str[-1]] = seed_t0
        party1.seed_t_tmp[a_str[-1]] = seed_t1
        party0.seed_t_tmp[Utils.xor(a_str[-1], "1", 1)] = seed_t0_err
        party1.seed_t_tmp[Utils.xor(a_str[-1], "1", 1)] = seed_t1_err
        print("    a_str[-1] = {} because a_str = {}".format(a_str[-1], a_str))
        print("    party0.seed_t['0'] = {}".format(party0.seed_t['0']))
        print("    party0.seed_t['1'] = {}".format(party0.seed_t['1']))
        print("    party1.seed_t['0'] = {}".format(party1.seed_t['0']))
        print("    party1.seed_t['1'] = {}".format(party1.seed_t['1']))
        print("step3: done. \n")

        # step4 - step13
        print("step4: for iteration ...\n")
        for i in range(1, n):
            # step5: apply seed S[i] to PRG
            print("step5: apply seed S[i] to PRG ...")
            party0.st = PRG(party0.seed_s_tmp[a_str[-i]])
            party1.st = PRG(party1.seed_s_tmp[a_str[-i]])
            party0.st_divide["s"]["0"] = party0.st[0:lmd]
            party0.st_divide["s"]["1"] = party0.st[lmd:2*lmd]
            party0.st_divide["t"]["0"] = party0.st[2*lmd]
            party0.st_divide["t"]["1"] = party0.st[2*lmd+1]
            party1.st_divide["s"]["0"] = party1.st[0:lmd]
            party1.st_divide["s"]["1"] = party1.st[lmd:2*lmd]
            party1.st_divide["t"]["0"] = party1.st[2*lmd]
            party1.st_divide["t"]["1"] = party1.st[2*lmd+1]
            print("    party0.st = PRG({}) = \t\t{}  (length: {})".format(party0.seed_s_tmp[a_str[-i]], party0.st, len(party0.st)))
            print("    party0.st_divide['s']['0'] = \t" + " " * 0 + "{}".format(party0.st_divide['s']['0']))
            print("    party0.st_divide['s']['1'] = \t" + " " * lmd + "{}".format(party0.st_divide['s']['1']))
            print("    party0.st_divide['t']['0'] = \t" + " " * (2*lmd) + "{}".format(party0.st_divide['t']['0']))
            print("    party0.st_divide['t']['1'] = \t" + " " * (2*lmd+1) + "{}".format(party0.st_divide['t']['1']))
            print("    party1.st = PRG({}) = \t\t{}  (length: {})".format(party1.seed_s_tmp[a_str[-i]], party1.st, len(party1.st)))
            print("    party1.st_divide['s']['0'] = \t" + " " * 0 + "{}".format(party1.st_divide['s']['0']))
            print("    party1.st_divide['s']['1'] = \t" + " " * lmd + "{}".format(party1.st_divide['s']['1']))
            print("    party1.st_divide['t']['0'] = \t" + " " * (2*lmd) + "{}".format(party1.st_divide['t']['0']))
            print("    party1.st_divide['t']['1'] = \t" + " " * (2*lmd+1) + "{}".format(party1.st_divide['t']['1']))
            print("step5: done. \n")

            # step6: generate cs_party0, cs_party1
            print("step6: generate cs_party0, cs_party1 ...")
            cs_party0 = {
                a_str[-(i+1)]: Utils.get_random_bits(lmd),
            }
            cs_party1 = {
                a_str[-(i+1)]: Utils.get_random_bits(lmd),
            }
            print("    cs_party0 = {}".format(cs_party0))
            print("    cs_party1 = {}".format(cs_party1))
            print("step6: done. \n")

            # step7: generate cs_party0_err, cs_party1_err
            print("step7: generate cs_party0_err, cs_party1_err ...")
            cs_party0_err = Utils.get_random_bits(lmd)
            cs_party1_err = Utils.xor(cs_party0_err, party0.st_divide['s'][Utils.xor(a_str[-(i+1)], "1", 1)], lmd)
            cs_party1_err = Utils.xor(cs_party1_err, party1.st_divide['s'][Utils.xor(a_str[-(i+1)], "1", 1)], lmd)
            cs_party0[Utils.xor(a_str[-(i+1)], "1", 1)] = cs_party0_err
            cs_party1[Utils.xor(a_str[-(i+1)], "1", 1)] = cs_party1_err
            print("    cs_party0 = {}".format(cs_party0))
            print("    cs_party1 = {}".format(cs_party1))
            print("step7: done. \n")

            # step8: generate ct_party0, ct_party1
            print("step8: generate ct_party0, ct_party1 ... ")
            ct_party0_bit = Utils.get_random_bits(1)
            ct_party1_bit = Utils.xor(ct_party0_bit, party0.st_divide['t'][a_str[-(i+1)]], 1)
            ct_party1_bit = Utils.xor(ct_party1_bit, party1.st_divide['t'][a_str[-(i+1)]], 1)
            ct_party1_bit = Utils.xor(ct_party1_bit, "1", 1)
            ct_party0 = {
                a_str[-(i+1)]: ct_party0_bit,
            }
            ct_party1 = {
                a_str[-(i+1)]: ct_party1_bit,
            }
            print("    ct_party0 = {}".format(ct_party0))
            print("    ct_party1 = {}".format(ct_party1))
            print("step8: done. \n")

            # step9: generate ct_party0_err, ct_party1_err
            print("step9: generate ct_party0_err, ct_party1_err ... ")
            ct_party0_err_bit = Utils.get_random_bits(1)
            ct_party1_err_bit = Utils.xor(ct_party0_err_bit, party0.st_divide['t'][Utils.xor(a_str[-(i+1)], "1", 1)], 1)
            ct_party1_err_bit = Utils.xor(ct_party1_err_bit, party1.st_divide['t'][Utils.xor(a_str[-(i+1)], "1", 1)], 1)
            ct_party0[Utils.xor(a_str[-(i+1)], "1", 1)] = ct_party0_err_bit
            ct_party1[Utils.xor(a_str[-(i+1)], "1", 1)] = ct_party1_err_bit
            print("    ct_party0 = {}".format(ct_party0))
            print("    ct_party1 = {}".format(ct_party1))
            print("step9: done. \n")

            # step10: set CW
            print("step10: set CW ...")
            cw = cs_party0['0'] + cs_party0['1'] + ct_party0['0'] + ct_party0['1']
            print("cw (party0)")
            print(" = {}".format(cs_party0['0']))
            print("|| " + " "*lmd + "{}".format(cs_party0['1']))
            print("|| " + " "*(2*lmd) + "{}".format(ct_party0['0']))
            print("|| " + " "*(2*lmd+1) + "{}".format(ct_party0['1']))
            print(" = {}\n".format(cw))
            party0.cw_list.append(cw)

            cw = cs_party1['0'] + cs_party1['1'] + ct_party1['0'] + ct_party1['1']
            print("cw (party1)")
            print(" = {}".format(cs_party1['0']))
            print("|| " + " "*lmd + "{}".format(cs_party1['1']))
            print("|| " + " "*(2*lmd) + "{}".format(ct_party1['0']))
            print("|| " + " "*(2*lmd+1) + "{}".format(ct_party1['1']))
            print(" = {}".format(cw))
            party1.cw_list.append(cw)
            print("step10: done. \n")

            # step11: generate next PRG's seed S
            print("step11: generate next PRG's seed S ...")
            tau0 = party0.seed_t_tmp[a_str[-i]]
            if tau0 == '0':
                party0.seed_s_tmp["0"] = \
                    Utils.xor(party0.st_divide["s"]["0"], cs_party0["0"], lmd)
                party0.seed_s_tmp["1"] = \
                    Utils.xor(party0.st_divide["s"]["1"], cs_party0["1"], lmd)
            elif tau0 == '1':
                party0.seed_s_tmp["0"] = \
                    Utils.xor(party0.st_divide["s"]["0"], cs_party1["0"], lmd)
                party0.seed_s_tmp["1"] = \
                    Utils.xor(party0.st_divide["s"]["1"], cs_party1["1"], lmd)
            else:
                print("ERROR")
                sys.exit(1)

            tau1 = party1.seed_t_tmp[a_str[-i]]
            if tau1 == '0':
                party1.seed_s_tmp["0"] = \
                    Utils.xor(party1.st_divide["s"]["0"], cs_party0["0"], lmd)
                party1.seed_s_tmp["1"] = \
                    Utils.xor(party1.st_divide["s"]["1"], cs_party0["1"], lmd)
            elif tau1 == '1':
                party1.seed_s_tmp["0"] = \
                    Utils.xor(party1.st_divide["s"]["0"], cs_party1["0"], lmd)
                party1.seed_s_tmp["1"] = \
                    Utils.xor(party1.st_divide["s"]["1"], cs_party1["1"], lmd)
            else:
                print("ERROR")
                sys.exit(1)
            print("    party0.seed_s_tmp = {}".format(party0.seed_s_tmp))
            print("    party1.seed_s_tmp = {}".format(party1.seed_s_tmp))
            print("step11: done. \n")

            # step12: generate next T ...
            print("step12: generate next T ...")
            if tau0 == '0':
                party0.seed_t_tmp["0"] = \
                    Utils.xor(party0.st_divide["t"]["0"], ct_party0["0"], 1)
                party0.seed_t_tmp["1"] = \
                    Utils.xor(party0.st_divide["t"]["1"], ct_party0["1"], 1)
            elif tau0 == '1':
                party0.seed_t_tmp["0"] = \
                    Utils.xor(party0.st_divide["t"]["0"], ct_party1["0"], 1)
                party0.seed_t_tmp["1"] = \
                    Utils.xor(party0.st_divide["t"]["1"], ct_party1["1"], 1)

            if tau1 == '0':
                party1.seed_t_tmp["0"] = \
                    Utils.xor(party1.st_divide["t"]["0"], ct_party0["0"], 1)
                party1.seed_t_tmp["1"] = \
                    Utils.xor(party1.st_divide["t"]["1"], ct_party0["1"], 1)
            elif tau1 == '1':
                party1.seed_t_tmp["0"] = \
                    Utils.xor(party1.st_divide["t"]["0"], ct_party1["0"], 1)
                party1.seed_t_tmp["1"] = \
                    Utils.xor(party1.st_divide["t"]["1"], ct_party1["1"], 1)
            print("    party0.seed_t_tmp = {}".format(party0.seed_t_tmp))
            print("    party1.seed_t_tmp = {}".format(party1.seed_t_tmp))
            print("step12: done. \n")

        print("step13: for iteration end\n")

        # step14 - step18: set w
        print("step14 - step18: set w ... ")
        w = 0
        prg_party_0 = PRG(party0.seed_s_tmp[a_str[0]])
        prg_party_1 = PRG(party1.seed_s_tmp[a_str[0]])
        if prg_party_0 != prg_party_1:
            prg_party_0 = prg_party_0
            prg_party_1 = prg_party_1
            print("    prg_party_0 = {}".format(prg_party_0))
            print("    int(PRG(*), 2) = {}".format(int(prg_party_0, 2)))
            print("    prg_party_1 = {}".format(prg_party_1))
            print("    int(PRG(*), 2) = {}".format(int(prg_party_1, 2)))
            w = (pow((int(prg_party_0, 2) + int(prg_party_1, 2)), -1, mod) * b) % mod
            print("    b = {}".format(b))
            print("    w = {}".format(w))
        else:
            print("ERROR: step14")
            sys.exit(1)

        # step19: set key
        k0_list = [[party0.seed_s["0"], party0.seed_s["1"], party0.seed_t["0"], party0.seed_t["1"]]]
        k1_list = [[party1.seed_s["0"], party1.seed_s["1"], party1.seed_t["0"], party1.seed_t["1"]]]
        list = []
        for i in range(0, n-1):
            list.append(party0.cw_list[i])
            list.append(party1.cw_list[i])
        k0_list.append(list)
        k1_list.append(list)
        k0_list.append(w)
        k1_list.append(w)

        return k0_list, k1_list, PRG
