import random
from gen import Gen
from eval import Eval

def dpf_2party():
    summary = """
[2Party DPF (Distributed Point Function)]
function f(x)
    = b if x == a
    = 0 else.
λ (lmd) is input length of PRG.
seed is PRG's seed.
mod is modulo number.
    """

    print(summary)

    print("\n====== Input Phase ======\n")
    a = int(input("a = "))
    b = int(input("b = "))
    lmd = int(input("λ = "))
    mod = int(input("mod = "))

    print("\n====== Gen Protocol Phase ======\n")

    # Gen Protocol
    seed = random.getrandbits(lmd)
    k0_list, k1_list, PRG = Gen.dpf_2party(a, b, lmd, seed, mod)
    print(k0_list)
    print(k1_list)

    print("\n====== Eval Protocol Phase ======\n")
    x = int(input("x = "))

    # Eval Protocol
    ans0 = Eval.dpf_2party(0, k0_list, x, lmd, mod, PRG)
    print(ans0)
    print("\n\n")
    ans1 = Eval.dpf_2party(1, k1_list, x, lmd, mod, PRG)
    print(ans1)

    print("\n====== Decryption Phase ======\n")

    # Decryption phase
    if ans0 == ans1:
        print("f(x = {}) = 0".format(x))
    else:
        print("f(x = {}) = {}".format(x, (ans0 + ans1) % mod))

if __name__ == '__main__':
    dpf_2party()