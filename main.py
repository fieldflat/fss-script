import random
from gen import Gen
from eval import Eval


if __name__ == '__main__':
    """
    function f(x)
       = b if x == a
       = 0 else.
    lmd is input length of PRG.
    seed is PRG's seed.
    """

    # Gen Protocol
    a, b = 12, 1
    lmd = 6
    mod = 294001
    seed = random.getrandbits(lmd)
    # seed = 1
    k0_list, k1_list, PRG = Gen.dpf_2party(a, b, lmd, seed, mod)
    print(k0_list)
    print(k1_list)

    print("\n===========\n")

    # Eval Protocol
    x = 10
    ans0 = Eval.dpf_2party(0, k0_list, x, lmd, mod, PRG)
    print(ans0)
    print("\n\n")
    ans1 = Eval.dpf_2party(1, k1_list, x, lmd, mod, PRG)
    print(ans1)

    # Decryption phase
    if ans0 == ans1:
        print("\n===> f(x = {}) = 0".format(x))
    else:
        print("\n===> f(x = {}) = {}".format(x, (ans0 + ans1) % mod))
