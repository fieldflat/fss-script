# Example (2party DPF)

```
% python main.py

[2Party DPF (Distributed Point Function)]
function f(x)
    = b if x == a
    = 0 else.
λ (lmd) is input length of PRG.
seed is PRG's seed.
mod is modulo number.


====== Input Phase ======

a = 12
b = 1
λ = 16
mod = 107

====== Gen Protocol Phase ======

step0: initializing
    a_str = 0000000000001100
    n = 16
step0: done.

step1: generate PRG ...
    lmd = 16
    seed = 54563
    generating PRG ...
    PRG(a) = 1000000111110000010000111011100011
step1: done.

step2: choose random seeds of S ...
    a_str[0] = 0 because a_str = 0000000000001100
    party0.seed_s['0'] = 0111100000111010
    party0.seed_s['1'] = 1100111101111010
    party1.seed_s['0'] = 0001100000111100
    party1.seed_s['1'] = 1100111101111010
step2: done.

step3: choose random bits of T ...
    a_str[0] = 0 because a_str = 0000000000001100
    party0.seed_t['0'] = 1
    party0.seed_t['1'] = 1
    party1.seed_t['0'] = 0
    party1.seed_t['1'] = 1
step3: done.

step4: for iteration ...

step5: apply seed S[i] to PRG ...
    party0.st = PRG(0111100000111010) = 		0001110001111000111011000110001000  (length: 34)
    party0.st_divide['s']['0'] = 	0001110001111000
    party0.st_divide['s']['1'] = 	                1110110001100010
    party0.st_divide['t']['0'] = 	                                0
    party0.st_divide['t']['1'] = 	                                 0
    party1.st = PRG(0001100000111100) = 		1111010000110111001110010000011101  (length: 34)
    party1.st_divide['s']['0'] = 	1111010000110111
    party1.st_divide['s']['1'] = 	                0011100100000111
    party1.st_divide['t']['0'] = 	                                0
    party1.st_divide['t']['1'] = 	                                 1
step5: done.

step6: generate cs_party0, cs_party1 ...
    cs_party0 = {'0': '1001000101000001'}
    cs_party1 = {'0': '1001100110110101'}
step6: done.

step7: generate cs_party0_err, cs_party1_err ...
    cs_party0 = {'0': '1001000101000001', '1': '1100001000010100'}
    cs_party1 = {'0': '1001100110110101', '1': '0001011101110001'}
step7: done.

step8: generate ct_party0, ct_party1 ...
    ct_party0 = {'0': '1'}
    ct_party1 = {'0': '0'}
step8: done.

step9: generate ct_party0_err, ct_party1_err ...
    ct_party0 = {'0': '1', '1': '0'}
    ct_party1 = {'0': '0', '1': '1'}
step9: done.

step10: set CW ...
cw (party0)
 = 1001000101000001
||                 1100001000010100
||                                 1
||                                  0
 = 1001000101000001110000100001010010

cw (party1)
 = 1001100110110101
||                 0001011101110001
||                                 0
||                                  1
 = 1001100110110101000101110111000101
step10: done.

step11: generate next PRG's seed S ...
    party0.seed_s_tmp = {'0': '1000010111001101', '1': '1111101100010011'}
    party1.seed_s_tmp = {'0': '0110010101110110', '1': '1111101100010011'}
step11: done.

step12: generate next T ...
    party0.seed_t_tmp = {'0': '0', '1': '1'}
    party1.seed_t_tmp = {'0': '1', '1': '1'}
step12: done.

step5: apply seed S[i] to PRG ...
    party0.st = PRG(1000010111001101) = 		0110000001001011111010111100011101  (length: 34)
    party0.st_divide['s']['0'] = 	0110000001001011
    party0.st_divide['s']['1'] = 	                1110101111000111
    party0.st_divide['t']['0'] = 	                                0
    party0.st_divide['t']['1'] = 	                                 1
    party1.st = PRG(0110010101110110) = 		1100011010100100100100010111100001  (length: 34)
    party1.st_divide['s']['0'] = 	1100011010100100
    party1.st_divide['s']['1'] = 	                1001000101111000
    party1.st_divide['t']['0'] = 	                                0
    party1.st_divide['t']['1'] = 	                                 1
step5: done.

step6: generate cs_party0, cs_party1 ...
    cs_party0 = {'0': '1001011110010010'}
    cs_party1 = {'0': '0010111100010011'}
step6: done.

step7: generate cs_party0_err, cs_party1_err ...
    cs_party0 = {'0': '1001011110010010', '1': '1011001111101001'}
    cs_party1 = {'0': '0010111100010011', '1': '1100100101010110'}
step7: done.

step8: generate ct_party0, ct_party1 ...
    ct_party0 = {'0': '1'}
    ct_party1 = {'0': '0'}
step8: done.

step9: generate ct_party0_err, ct_party1_err ...
    ct_party0 = {'0': '1', '1': '0'}
    ct_party1 = {'0': '0', '1': '0'}
step9: done.

step10: set CW ...
cw (party0)
 = 1001011110010010
||                 1011001111101001
||                                 1
||                                  0
 = 1001011110010010101100111110100110

cw (party1)
 = 0010111100010011
||                 1100100101010110
||                                 0
||                                  0
 = 0010111100010011110010010101011000
step10: done.

step11: generate next PRG's seed S ...
    party0.seed_s_tmp = {'0': '1111011111011001', '1': '0101100000101110'}
    party1.seed_s_tmp = {'0': '1110100110110111', '1': '0101100000101110'}
step11: done.

step12: generate next T ...
    party0.seed_t_tmp = {'0': '1', '1': '1'}
    party1.seed_t_tmp = {'0': '0', '1': '1'}
step12: done.

step5: apply seed S[i] to PRG ...
    party0.st = PRG(1111011111011001) = 		1011001110011011000000001001001111  (length: 34)
    party0.st_divide['s']['0'] = 	1011001110011011
    party0.st_divide['s']['1'] = 	                0000000010010011
    party0.st_divide['t']['0'] = 	                                1
    party0.st_divide['t']['1'] = 	                                 1
    party1.st = PRG(1110100110110111) = 		1100101101110101101100101010100111  (length: 34)
    party1.st_divide['s']['0'] = 	1100101101110101
    party1.st_divide['s']['1'] = 	                1011001010101001
    party1.st_divide['t']['0'] = 	                                1
    party1.st_divide['t']['1'] = 	                                 1
step5: done.

step6: generate cs_party0, cs_party1 ...
    cs_party0 = {'0': '1010100100111001'}
    cs_party1 = {'0': '0111010001110011'}
step6: done.

step7: generate cs_party0_err, cs_party1_err ...
    cs_party0 = {'0': '1010100100111001', '1': '0101111010001111'}
    cs_party1 = {'0': '0111010001110011', '1': '1110110010110101'}
step7: done.

step8: generate ct_party0, ct_party1 ...
    ct_party0 = {'0': '1'}
    ct_party1 = {'0': '0'}
step8: done.

step9: generate ct_party0_err, ct_party1_err ...
    ct_party0 = {'0': '1', '1': '1'}
    ct_party1 = {'0': '0', '1': '1'}
step9: done.

step10: set CW ...
cw (party0)
 = 1010100100111001
||                 0101111010001111
||                                 1
||                                  1
 = 1010100100111001010111101000111111

cw (party1)
 = 0111010001110011
||                 1110110010110101
||                                 0
||                                  1
 = 0111010001110011111011001011010101
step10: done.

step11: generate next PRG's seed S ...
    party0.seed_s_tmp = {'0': '1100011111101000', '1': '1110110000100110'}
    party1.seed_s_tmp = {'0': '0110001001001100', '1': '1110110000100110'}
step11: done.

step12: generate next T ...
    party0.seed_t_tmp = {'0': '1', '1': '0'}
    party1.seed_t_tmp = {'0': '0', '1': '0'}
step12: done.

step5: apply seed S[i] to PRG ...
    party0.st = PRG(1100011111101000) = 		0100100110000100010110101011010100  (length: 34)
    party0.st_divide['s']['0'] = 	0100100110000100
    party0.st_divide['s']['1'] = 	                0101101010110101
    party0.st_divide['t']['0'] = 	                                0
    party0.st_divide['t']['1'] = 	                                 0
    party1.st = PRG(0110001001001100) = 		0101001010110000111101010000010001  (length: 34)
    party1.st_divide['s']['0'] = 	0101001010110000
    party1.st_divide['s']['1'] = 	                1111010100000100
    party1.st_divide['t']['0'] = 	                                0
    party1.st_divide['t']['1'] = 	                                 1
step5: done.

step6: generate cs_party0, cs_party1 ...
    cs_party0 = {'0': '1101010111010010'}
    cs_party1 = {'0': '0100110100010110'}
step6: done.

step7: generate cs_party0_err, cs_party1_err ...
    cs_party0 = {'0': '1101010111010010', '1': '0000010111101010'}
    cs_party1 = {'0': '0100110100010110', '1': '1010101001011011'}
step7: done.

step8: generate ct_party0, ct_party1 ...
    ct_party0 = {'0': '0'}
    ct_party1 = {'0': '1'}
step8: done.

step9: generate ct_party0_err, ct_party1_err ...
    ct_party0 = {'0': '0', '1': '0'}
    ct_party1 = {'0': '1', '1': '1'}
step9: done.

step10: set CW ...
cw (party0)
 = 1101010111010010
||                 0000010111101010
||                                 0
||                                  0
 = 1101010111010010000001011110101000

cw (party1)
 = 0100110100010110
||                 1010101001011011
||                                 1
||                                  1
 = 0100110100010110101010100101101111
step10: done.

step11: generate next PRG's seed S ...
    party0.seed_s_tmp = {'0': '0000010010010010', '1': '1111000011101110'}
    party1.seed_s_tmp = {'0': '1000011101100010', '1': '1111000011101110'}
step11: done.

step12: generate next T ...
    party0.seed_t_tmp = {'0': '1', '1': '1'}
    party1.seed_t_tmp = {'0': '0', '1': '1'}
step12: done.

step5: apply seed S[i] to PRG ...
    party0.st = PRG(0000010010010010) = 		0110011101000101010000011000100111  (length: 34)
    party0.st_divide['s']['0'] = 	0110011101000101
    party0.st_divide['s']['1'] = 	                0100000110001001
    party0.st_divide['t']['0'] = 	                                1
    party0.st_divide['t']['1'] = 	                                 1
    party1.st = PRG(1000011101100010) = 		0111111110010011101100100101111011  (length: 34)
    party1.st_divide['s']['0'] = 	0111111110010011
    party1.st_divide['s']['1'] = 	                1011001001011110
    party1.st_divide['t']['0'] = 	                                1
    party1.st_divide['t']['1'] = 	                                 1
step5: done.

step6: generate cs_party0, cs_party1 ...
    cs_party0 = {'0': '1101101001110000'}
    cs_party1 = {'0': '0001100110011111'}
step6: done.

step7: generate cs_party0_err, cs_party1_err ...
    cs_party0 = {'0': '1101101001110000', '1': '1011111101001110'}
    cs_party1 = {'0': '0001100110011111', '1': '0100110010011001'}
step7: done.

step8: generate ct_party0, ct_party1 ...
    ct_party0 = {'0': '1'}
    ct_party1 = {'0': '0'}
step8: done.

step9: generate ct_party0_err, ct_party1_err ...
    ct_party0 = {'0': '1', '1': '1'}
    ct_party1 = {'0': '0', '1': '1'}
step9: done.

step10: set CW ...
cw (party0)
 = 1101101001110000
||                 1011111101001110
||                                 1
||                                  1
 = 1101101001110000101111110100111011

cw (party1)
 = 0001100110011111
||                 0100110010011001
||                                 0
||                                  1
 = 0001100110011111010011001001100101
step10: done.

step11: generate next PRG's seed S ...
    party0.seed_s_tmp = {'0': '0111111011011010', '1': '0000110100010000'}
    party1.seed_s_tmp = {'0': '1010010111100011', '1': '0000110100010000'}
step11: done.

step12: generate next T ...
    party0.seed_t_tmp = {'0': '1', '1': '0'}
    party1.seed_t_tmp = {'0': '0', '1': '0'}
step12: done.

step5: apply seed S[i] to PRG ...
    party0.st = PRG(0111111011011010) = 		0011000000001011011001110100100001  (length: 34)
    party0.st_divide['s']['0'] = 	0011000000001011
    party0.st_divide['s']['1'] = 	                0110011101001000
    party0.st_divide['t']['0'] = 	                                0
    party0.st_divide['t']['1'] = 	                                 1
    party1.st = PRG(1010010111100011) = 		0111101001011001001100001010110100  (length: 34)
    party1.st_divide['s']['0'] = 	0111101001011001
    party1.st_divide['s']['1'] = 	                0011000010101101
    party1.st_divide['t']['0'] = 	                                0
    party1.st_divide['t']['1'] = 	                                 0
step5: done.

step6: generate cs_party0, cs_party1 ...
    cs_party0 = {'0': '0101011001111001'}
    cs_party1 = {'0': '1010001010110111'}
step6: done.

step7: generate cs_party0_err, cs_party1_err ...
    cs_party0 = {'0': '0101011001111001', '1': '1111100011111011'}
    cs_party1 = {'0': '1010001010110111', '1': '1010111100011110'}
step7: done.

step8: generate ct_party0, ct_party1 ...
    ct_party0 = {'0': '0'}
    ct_party1 = {'0': '1'}
step8: done.

step9: generate ct_party0_err, ct_party1_err ...
    ct_party0 = {'0': '0', '1': '0'}
    ct_party1 = {'0': '1', '1': '1'}
step9: done.

step10: set CW ...
cw (party0)
 = 0101011001111001
||                 1111100011111011
||                                 0
||                                  0
 = 0101011001111001111110001111101100

cw (party1)
 = 1010001010110111
||                 1010111100011110
||                                 1
||                                  1
 = 1010001010110111101011110001111011
step10: done.

step11: generate next PRG's seed S ...
    party0.seed_s_tmp = {'0': '1001001010111100', '1': '1100100001010110'}
    party1.seed_s_tmp = {'0': '0010110000100000', '1': '1100100001010110'}
step11: done.

step12: generate next T ...
    party0.seed_t_tmp = {'0': '1', '1': '0'}
    party1.seed_t_tmp = {'0': '0', '1': '0'}
step12: done.

step5: apply seed S[i] to PRG ...
    party0.st = PRG(1001001010111100) = 		0111000000001001011110110111111110  (length: 34)
    party0.st_divide['s']['0'] = 	0111000000001001
    party0.st_divide['s']['1'] = 	                0111101101111111
    party0.st_divide['t']['0'] = 	                                1
    party0.st_divide['t']['1'] = 	                                 0
    party1.st = PRG(0010110000100000) = 		1001111100110111100011101001111001  (length: 34)
    party1.st_divide['s']['0'] = 	1001111100110111
    party1.st_divide['s']['1'] = 	                1000111010011110
    party1.st_divide['t']['0'] = 	                                0
    party1.st_divide['t']['1'] = 	                                 1
step5: done.

step6: generate cs_party0, cs_party1 ...
    cs_party0 = {'0': '1100000010101010'}
    cs_party1 = {'0': '0101011000001001'}
step6: done.

step7: generate cs_party0_err, cs_party1_err ...
    cs_party0 = {'0': '1100000010101010', '1': '1001110111000010'}
    cs_party1 = {'0': '0101011000001001', '1': '0110100000100011'}
step7: done.

step8: generate ct_party0, ct_party1 ...
    ct_party0 = {'0': '0'}
    ct_party1 = {'0': '0'}
step8: done.

step9: generate ct_party0_err, ct_party1_err ...
    ct_party0 = {'0': '0', '1': '0'}
    ct_party1 = {'0': '0', '1': '1'}
step9: done.

step10: set CW ...
cw (party0)
 = 1100000010101010
||                 1001110111000010
||                                 0
||                                  0
 = 1100000010101010100111011100001000

cw (party1)
 = 0101011000001001
||                 0110100000100011
||                                 0
||                                  1
 = 0101011000001001011010000010001101
step10: done.

step11: generate next PRG's seed S ...
    party0.seed_s_tmp = {'0': '0010011000000000', '1': '0001001101011100'}
    party1.seed_s_tmp = {'0': '0101111110011101', '1': '0001001101011100'}
step11: done.

step12: generate next T ...
    party0.seed_t_tmp = {'0': '1', '1': '1'}
    party1.seed_t_tmp = {'0': '0', '1': '1'}
step12: done.

step5: apply seed S[i] to PRG ...
    party0.st = PRG(0010011000000000) = 		1100101101111011000011101010111101  (length: 34)
    party0.st_divide['s']['0'] = 	1100101101111011
    party0.st_divide['s']['1'] = 	                0000111010101111
    party0.st_divide['t']['0'] = 	                                0
    party0.st_divide['t']['1'] = 	                                 1
    party1.st = PRG(0101111110011101) = 		0011100000000100011000101011000011  (length: 34)
    party1.st_divide['s']['0'] = 	0011100000000100
    party1.st_divide['s']['1'] = 	                0110001010110000
    party1.st_divide['t']['0'] = 	                                1
    party1.st_divide['t']['1'] = 	                                 1
step5: done.

step6: generate cs_party0, cs_party1 ...
    cs_party0 = {'0': '1011001001000100'}
    cs_party1 = {'0': '1000100111001100'}
step6: done.

step7: generate cs_party0_err, cs_party1_err ...
    cs_party0 = {'0': '1011001001000100', '1': '1001100010101011'}
    cs_party1 = {'0': '1000100111001100', '1': '1111010010110100'}
step7: done.

step8: generate ct_party0, ct_party1 ...
    ct_party0 = {'0': '0'}
    ct_party1 = {'0': '0'}
step8: done.

step9: generate ct_party0_err, ct_party1_err ...
    ct_party0 = {'0': '0', '1': '1'}
    ct_party1 = {'0': '0', '1': '1'}
step9: done.

step10: set CW ...
cw (party0)
 = 1011001001000100
||                 1001100010101011
||                                 0
||                                  1
 = 1011001001000100100110001010101101

cw (party1)
 = 1000100111001100
||                 1111010010110100
||                                 0
||                                  1
 = 1000100111001100111101001011010001
step10: done.

step11: generate next PRG's seed S ...
    party0.seed_s_tmp = {'0': '0100001010110111', '1': '1111101000011011'}
    party1.seed_s_tmp = {'0': '1000101001000000', '1': '1111101000011011'}
step11: done.

step12: generate next T ...
    party0.seed_t_tmp = {'0': '0', '1': '0'}
    party1.seed_t_tmp = {'0': '1', '1': '0'}
step12: done.

step5: apply seed S[i] to PRG ...
    party0.st = PRG(0100001010110111) = 		1001101100001100111110010011110011  (length: 34)
    party0.st_divide['s']['0'] = 	1001101100001100
    party0.st_divide['s']['1'] = 	                1111100100111100
    party0.st_divide['t']['0'] = 	                                1
    party0.st_divide['t']['1'] = 	                                 1
    party1.st = PRG(1000101001000000) = 		1000100111100100000011011100101111  (length: 34)
    party1.st_divide['s']['0'] = 	1000100111100100
    party1.st_divide['s']['1'] = 	                0000110111001011
    party1.st_divide['t']['0'] = 	                                1
    party1.st_divide['t']['1'] = 	                                 1
step5: done.

step6: generate cs_party0, cs_party1 ...
    cs_party0 = {'0': '1011100011111001'}
    cs_party1 = {'0': '0100011011110111'}
step6: done.

step7: generate cs_party0_err, cs_party1_err ...
    cs_party0 = {'0': '1011100011111001', '1': '0011010011110010'}
    cs_party1 = {'0': '0100011011110111', '1': '1100000000000101'}
step7: done.

step8: generate ct_party0, ct_party1 ...
    ct_party0 = {'0': '1'}
    ct_party1 = {'0': '0'}
step8: done.

step9: generate ct_party0_err, ct_party1_err ...
    ct_party0 = {'0': '1', '1': '1'}
    ct_party1 = {'0': '0', '1': '1'}
step9: done.

step10: set CW ...
cw (party0)
 = 1011100011111001
||                 0011010011110010
||                                 1
||                                  1
 = 1011100011111001001101001111001011

cw (party1)
 = 0100011011110111
||                 1100000000000101
||                                 0
||                                  1
 = 0100011011110111110000000000010101
step10: done.

step11: generate next PRG's seed S ...
    party0.seed_s_tmp = {'0': '0010001111110101', '1': '1100110111001110'}
    party1.seed_s_tmp = {'0': '1100111100010011', '1': '1100110111001110'}
step11: done.

step12: generate next T ...
    party0.seed_t_tmp = {'0': '0', '1': '0'}
    party1.seed_t_tmp = {'0': '1', '1': '0'}
step12: done.

step5: apply seed S[i] to PRG ...
    party0.st = PRG(0010001111110101) = 		1000001101000101100001100011101100  (length: 34)
    party0.st_divide['s']['0'] = 	1000001101000101
    party0.st_divide['s']['1'] = 	                1000011000111011
    party0.st_divide['t']['0'] = 	                                0
    party0.st_divide['t']['1'] = 	                                 0
    party1.st = PRG(1100111100010011) = 		0111111001110111100001111100111011  (length: 34)
    party1.st_divide['s']['0'] = 	0111111001110111
    party1.st_divide['s']['1'] = 	                1000011111001110
    party1.st_divide['t']['0'] = 	                                1
    party1.st_divide['t']['1'] = 	                                 1
step5: done.

step6: generate cs_party0, cs_party1 ...
    cs_party0 = {'0': '1010001101110001'}
    cs_party1 = {'0': '0100010000111101'}
step6: done.

step7: generate cs_party0_err, cs_party1_err ...
    cs_party0 = {'0': '1010001101110001', '1': '1101111111000011'}
    cs_party1 = {'0': '0100010000111101', '1': '1101111000110110'}
step7: done.

step8: generate ct_party0, ct_party1 ...
    ct_party0 = {'0': '1'}
    ct_party1 = {'0': '1'}
step8: done.

step9: generate ct_party0_err, ct_party1_err ...
    ct_party0 = {'0': '1', '1': '0'}
    ct_party1 = {'0': '1', '1': '1'}
step9: done.

step10: set CW ...
cw (party0)
 = 1010001101110001
||                 1101111111000011
||                                 1
||                                  0
 = 1010001101110001110111111100001110

cw (party1)
 = 0100010000111101
||                 1101111000110110
||                                 1
||                                  1
 = 0100010000111101110111100011011011
step10: done.

step11: generate next PRG's seed S ...
    party0.seed_s_tmp = {'0': '0010000000110100', '1': '0101100111111000'}
    party1.seed_s_tmp = {'0': '0011101001001010', '1': '0101100111111000'}
step11: done.

step12: generate next T ...
    party0.seed_t_tmp = {'0': '1', '1': '0'}
    party1.seed_t_tmp = {'0': '0', '1': '0'}
step12: done.

step5: apply seed S[i] to PRG ...
    party0.st = PRG(0010000000110100) = 		1011001100111100010000101010100101  (length: 34)
    party0.st_divide['s']['0'] = 	1011001100111100
    party0.st_divide['s']['1'] = 	                0100001010101001
    party0.st_divide['t']['0'] = 	                                0
    party0.st_divide['t']['1'] = 	                                 1
    party1.st = PRG(0011101001001010) = 		0110111100001100100111001010100001  (length: 34)
    party1.st_divide['s']['0'] = 	0110111100001100
    party1.st_divide['s']['1'] = 	                1001110010101000
    party1.st_divide['t']['0'] = 	                                0
    party1.st_divide['t']['1'] = 	                                 1
step5: done.

step6: generate cs_party0, cs_party1 ...
    cs_party0 = {'0': '1000000001111011'}
    cs_party1 = {'0': '0010010100010001'}
step6: done.

step7: generate cs_party0_err, cs_party1_err ...
    cs_party0 = {'0': '1000000001111011', '1': '1011000011100111'}
    cs_party1 = {'0': '0010010100010001', '1': '0110111011100110'}
step7: done.

step8: generate ct_party0, ct_party1 ...
    ct_party0 = {'0': '1'}
    ct_party1 = {'0': '0'}
step8: done.

step9: generate ct_party0_err, ct_party1_err ...
    ct_party0 = {'0': '1', '1': '1'}
    ct_party1 = {'0': '0', '1': '1'}
step9: done.

step10: set CW ...
cw (party0)
 = 1000000001111011
||                 1011000011100111
||                                 1
||                                  1
 = 1000000001111011101100001110011111

cw (party1)
 = 0010010100010001
||                 0110111011100110
||                                 0
||                                  1
 = 0010010100010001011011101110011001
step10: done.

step11: generate next PRG's seed S ...
    party0.seed_s_tmp = {'0': '1001011000101101', '1': '0010110001001111'}
    party1.seed_s_tmp = {'0': '1110111101110111', '1': '0010110001001111'}
step11: done.

step12: generate next T ...
    party0.seed_t_tmp = {'0': '0', '1': '0'}
    party1.seed_t_tmp = {'0': '1', '1': '0'}
step12: done.

step5: apply seed S[i] to PRG ...
    party0.st = PRG(1001011000101101) = 		0000010100100011110100110010100101  (length: 34)
    party0.st_divide['s']['0'] = 	0000010100100011
    party0.st_divide['s']['1'] = 	                1101001100101001
    party0.st_divide['t']['0'] = 	                                0
    party0.st_divide['t']['1'] = 	                                 1
    party1.st = PRG(1110111101110111) = 		1100110010000101111100000000110011  (length: 34)
    party1.st_divide['s']['0'] = 	1100110010000101
    party1.st_divide['s']['1'] = 	                1111000000001100
    party1.st_divide['t']['0'] = 	                                1
    party1.st_divide['t']['1'] = 	                                 1
step5: done.

step6: generate cs_party0, cs_party1 ...
    cs_party0 = {'1': '1111101100100111'}
    cs_party1 = {'1': '1111110101101000'}
step6: done.

step7: generate cs_party0_err, cs_party1_err ...
    cs_party0 = {'1': '1111101100100111', '0': '0111100011101101'}
    cs_party1 = {'1': '1111110101101000', '0': '1011000101001011'}
step7: done.

step8: generate ct_party0, ct_party1 ...
    ct_party0 = {'1': '1'}
    ct_party1 = {'1': '0'}
step8: done.

step9: generate ct_party0_err, ct_party1_err ...
    ct_party0 = {'1': '1', '0': '0'}
    ct_party1 = {'1': '0', '0': '1'}
step9: done.

step10: set CW ...
cw (party0)
 = 0111100011101101
||                 1111101100100111
||                                 0
||                                  1
 = 0111100011101101111110110010011101

cw (party1)
 = 1011000101001011
||                 1111110101101000
||                                 1
||                                  0
 = 1011000101001011111111010110100010
step10: done.

step11: generate next PRG's seed S ...
    party0.seed_s_tmp = {'0': '0111110111001110', '1': '0010100000001110'}
    party1.seed_s_tmp = {'0': '0111110111001110', '1': '0000110101100100'}
step11: done.

step12: generate next T ...
    party0.seed_t_tmp = {'0': '0', '1': '0'}
    party1.seed_t_tmp = {'0': '0', '1': '1'}
step12: done.

step5: apply seed S[i] to PRG ...
    party0.st = PRG(0010100000001110) = 		0100101010001101000001101101011110  (length: 34)
    party0.st_divide['s']['0'] = 	0100101010001101
    party0.st_divide['s']['1'] = 	                0000011011010111
    party0.st_divide['t']['0'] = 	                                1
    party0.st_divide['t']['1'] = 	                                 0
    party1.st = PRG(0000110101100100) = 		1110000100001010010011000000011001  (length: 34)
    party1.st_divide['s']['0'] = 	1110000100001010
    party1.st_divide['s']['1'] = 	                0100110000000110
    party1.st_divide['t']['0'] = 	                                0
    party1.st_divide['t']['1'] = 	                                 1
step5: done.

step6: generate cs_party0, cs_party1 ...
    cs_party0 = {'1': '0001010011011111'}
    cs_party1 = {'1': '1011001001111101'}
step6: done.

step7: generate cs_party0_err, cs_party1_err ...
    cs_party0 = {'1': '0001010011011111', '0': '1011111011111100'}
    cs_party1 = {'1': '1011001001111101', '0': '0001010101111011'}
step7: done.

step8: generate ct_party0, ct_party1 ...
    ct_party0 = {'1': '0'}
    ct_party1 = {'1': '0'}
step8: done.

step9: generate ct_party0_err, ct_party1_err ...
    ct_party0 = {'1': '0', '0': '0'}
    ct_party1 = {'1': '0', '0': '1'}
step9: done.

step10: set CW ...
cw (party0)
 = 1011111011111100
||                 0001010011011111
||                                 0
||                                  0
 = 1011111011111100000101001101111100

cw (party1)
 = 0001010101111011
||                 1011001001111101
||                                 1
||                                  0
 = 0001010101111011101100100111110110
step10: done.

step11: generate next PRG's seed S ...
    party0.seed_s_tmp = {'0': '1111010001110001', '1': '0001001000001000'}
    party1.seed_s_tmp = {'0': '1111010001110001', '1': '1111111001111011'}
step11: done.

step12: generate next T ...
    party0.seed_t_tmp = {'0': '1', '1': '0'}
    party1.seed_t_tmp = {'0': '1', '1': '1'}
step12: done.

step5: apply seed S[i] to PRG ...
    party0.st = PRG(0001001000001000) = 		1101010001100111000101101000101101  (length: 34)
    party0.st_divide['s']['0'] = 	1101010001100111
    party0.st_divide['s']['1'] = 	                0001011010001011
    party0.st_divide['t']['0'] = 	                                0
    party0.st_divide['t']['1'] = 	                                 1
    party1.st = PRG(1111111001111011) = 		1011111000000001001110010000110110  (length: 34)
    party1.st_divide['s']['0'] = 	1011111000000001
    party1.st_divide['s']['1'] = 	                0011100100001101
    party1.st_divide['t']['0'] = 	                                1
    party1.st_divide['t']['1'] = 	                                 0
step5: done.

step6: generate cs_party0, cs_party1 ...
    cs_party0 = {'0': '1001101100100110'}
    cs_party1 = {'0': '0101100110101110'}
step6: done.

step7: generate cs_party0_err, cs_party1_err ...
    cs_party0 = {'0': '1001101100100110', '1': '0100011110011000'}
    cs_party1 = {'0': '0101100110101110', '1': '0110100000011110'}
step7: done.

step8: generate ct_party0, ct_party1 ...
    ct_party0 = {'0': '0'}
    ct_party1 = {'0': '0'}
step8: done.

step9: generate ct_party0_err, ct_party1_err ...
    ct_party0 = {'0': '0', '1': '0'}
    ct_party1 = {'0': '0', '1': '1'}
step9: done.

step10: set CW ...
cw (party0)
 = 1001101100100110
||                 0100011110011000
||                                 0
||                                  0
 = 1001101100100110010001111001100000

cw (party1)
 = 0101100110101110
||                 0110100000011110
||                                 0
||                                  1
 = 0101100110101110011010000001111001
step10: done.

step11: generate next PRG's seed S ...
    party0.seed_s_tmp = {'0': '0100111101000001', '1': '0101000100010011'}
    party1.seed_s_tmp = {'0': '1110011110101111', '1': '0101000100010011'}
step11: done.

step12: generate next T ...
    party0.seed_t_tmp = {'0': '0', '1': '1'}
    party1.seed_t_tmp = {'0': '1', '1': '1'}
step12: done.

step5: apply seed S[i] to PRG ...
    party0.st = PRG(0100111101000001) = 		0000111100011011101101100001101000  (length: 34)
    party0.st_divide['s']['0'] = 	0000111100011011
    party0.st_divide['s']['1'] = 	                1011011000011010
    party0.st_divide['t']['0'] = 	                                0
    party0.st_divide['t']['1'] = 	                                 0
    party1.st = PRG(1110011110101111) = 		1001110010011001000010111010100100  (length: 34)
    party1.st_divide['s']['0'] = 	1001110010011001
    party1.st_divide['s']['1'] = 	                0000101110101001
    party1.st_divide['t']['0'] = 	                                0
    party1.st_divide['t']['1'] = 	                                 0
step5: done.

step6: generate cs_party0, cs_party1 ...
    cs_party0 = {'0': '1011001010001010'}
    cs_party1 = {'0': '0111101100000111'}
step6: done.

step7: generate cs_party0_err, cs_party1_err ...
    cs_party0 = {'0': '1011001010001010', '1': '1111010010010000'}
    cs_party1 = {'0': '0111101100000111', '1': '0100100100100011'}
step7: done.

step8: generate ct_party0, ct_party1 ...
    ct_party0 = {'0': '0'}
    ct_party1 = {'0': '1'}
step8: done.

step9: generate ct_party0_err, ct_party1_err ...
    ct_party0 = {'0': '0', '1': '0'}
    ct_party1 = {'0': '1', '1': '0'}
step9: done.

step10: set CW ...
cw (party0)
 = 1011001010001010
||                 1111010010010000
||                                 0
||                                  0
 = 1011001010001010111101001001000000

cw (party1)
 = 0111101100000111
||                 0100100100100011
||                                 1
||                                  0
 = 0111101100000111010010010010001110
step10: done.

step11: generate next PRG's seed S ...
    party0.seed_s_tmp = {'0': '1011110110010001', '1': '0100001010001010'}
    party1.seed_s_tmp = {'0': '1110011110011110', '1': '0100001010001010'}
step11: done.

step12: generate next T ...
    party0.seed_t_tmp = {'0': '0', '1': '0'}
    party1.seed_t_tmp = {'0': '1', '1': '0'}
step12: done.

step13: for iteration end

step14 - step18: set w ...
    prg_party_0 = 0000011101000000100010101000111000
    int(PRG(*), 2) = 486681144
    prg_party_1 = 1001111110000001101110111111011011
    int(PRG(*), 2) = 10704318427
    b = 1
    w = 27
[['0111100000111010', '1100111101111010', '1', '1'], ['1001000101000001110000100001010010', '1001100110110101000101110111000101', '1001011110010010101100111110100110', '0010111100010011110010010101011000', '1010100100111001010111101000111111', '0111010001110011111011001011010101', '1101010111010010000001011110101000', '0100110100010110101010100101101111', '1101101001110000101111110100111011', '0001100110011111010011001001100101', '0101011001111001111110001111101100', '1010001010110111101011110001111011', '1100000010101010100111011100001000', '0101011000001001011010000010001101', '1011001001000100100110001010101101', '1000100111001100111101001011010001', '1011100011111001001101001111001011', '0100011011110111110000000000010101', '1010001101110001110111111100001110', '0100010000111101110111100011011011', '1000000001111011101100001110011111', '0010010100010001011011101110011001', '0111100011101101111110110010011101', '1011000101001011111111010110100010', '1011111011111100000101001101111100', '0001010101111011101100100111110110', '1001101100100110010001111001100000', '0101100110101110011010000001111001', '1011001010001010111101001001000000', '0111101100000111010010010010001110'], 27]
[['0001100000111100', '1100111101111010', '0', '1'], ['1001000101000001110000100001010010', '1001100110110101000101110111000101', '1001011110010010101100111110100110', '0010111100010011110010010101011000', '1010100100111001010111101000111111', '0111010001110011111011001011010101', '1101010111010010000001011110101000', '0100110100010110101010100101101111', '1101101001110000101111110100111011', '0001100110011111010011001001100101', '0101011001111001111110001111101100', '1010001010110111101011110001111011', '1100000010101010100111011100001000', '0101011000001001011010000010001101', '1011001001000100100110001010101101', '1000100111001100111101001011010001', '1011100011111001001101001111001011', '0100011011110111110000000000010101', '1010001101110001110111111100001110', '0100010000111101110111100011011011', '1000000001111011101100001110011111', '0010010100010001011011101110011001', '0111100011101101111110110010011101', '1011000101001011111111010110100010', '1011111011111100000101001101111100', '0001010101111011101100100111110110', '1001101100100110010001111001100000', '0101100110101110011010000001111001', '1011001010001010111101001001000000', '0111101100000111010010010010001110'], 27]

====== Eval Protocol Phase ======

x = 12
step1: recieving PRG ...
step1: done.

step2: parse input x ...
    x = 0000000000001100
    n = 16
step2: done.

step3: parse k_list as s0|s1|t0|t1, cw_list, w ...
    s0 = 0111100000111010
    s1 = 1100111101111010
    t0 = 1
    t1 = 1
step3: done.

step4: set S ...
    S  = 0111100000111010
step4: done.

step5: set T ...
    T  = 1
step5: done.

step7: parse G(S) as s0|s1|t0|t1 ...
    PRG(0111100000111010) = 0001110001111000111011000110001000
    s0 = 0001110001111000
    s1 = 1110110001100010
    t0 = 0
    t1 = 0
step7: done.

step8: parse CW ...
    cs = {'1': {'0': '1001100110110101', '1': '0001011101110001'}}
    ct = {'1': {'0': '0', '1': '1'}}
step8: done.

step9: set S ...
    x[(i+1)] = 0 because i+1 = 1 and x = 0000000000001100
    s[x[(i+1)]] = 0001110001111000
    cs[T][x[(i+1)]] = 1001100110110101
    S = 1000010111001101
step9: done.

step10: set T ...
    x[(i+1)] = 0 because i+1 = 1 and x = 0000000000001100
    t[x[(i+1)]] = 0
    ct[T][x[(i+1)]] = 0
    T = 0
step10: done.

step7: parse G(S) as s0|s1|t0|t1 ...
    PRG(1000010111001101) = 0110000001001011111010111100011101
    s0 = 0110000001001011
    s1 = 1110101111000111
    t0 = 0
    t1 = 1
step7: done.

step8: parse CW ...
    cs = {'0': {'0': '1001011110010010', '1': '1011001111101001'}}
    ct = {'0': {'0': '1', '1': '0'}}
step8: done.

step9: set S ...
    x[(i+1)] = 0 because i+1 = 2 and x = 0000000000001100
    s[x[(i+1)]] = 0110000001001011
    cs[T][x[(i+1)]] = 1001011110010010
    S = 1111011111011001
step9: done.

step10: set T ...
    x[(i+1)] = 0 because i+1 = 2 and x = 0000000000001100
    t[x[(i+1)]] = 0
    ct[T][x[(i+1)]] = 1
    T = 1
step10: done.

step7: parse G(S) as s0|s1|t0|t1 ...
    PRG(1111011111011001) = 1011001110011011000000001001001111
    s0 = 1011001110011011
    s1 = 0000000010010011
    t0 = 1
    t1 = 1
step7: done.

step8: parse CW ...
    cs = {'1': {'0': '0111010001110011', '1': '1110110010110101'}}
    ct = {'1': {'0': '0', '1': '1'}}
step8: done.

step9: set S ...
    x[(i+1)] = 0 because i+1 = 3 and x = 0000000000001100
    s[x[(i+1)]] = 1011001110011011
    cs[T][x[(i+1)]] = 0111010001110011
    S = 1100011111101000
step9: done.

step10: set T ...
    x[(i+1)] = 0 because i+1 = 3 and x = 0000000000001100
    t[x[(i+1)]] = 1
    ct[T][x[(i+1)]] = 0
    T = 1
step10: done.

step7: parse G(S) as s0|s1|t0|t1 ...
    PRG(1100011111101000) = 0100100110000100010110101011010100
    s0 = 0100100110000100
    s1 = 0101101010110101
    t0 = 0
    t1 = 0
step7: done.

step8: parse CW ...
    cs = {'1': {'0': '0100110100010110', '1': '1010101001011011'}}
    ct = {'1': {'0': '1', '1': '1'}}
step8: done.

step9: set S ...
    x[(i+1)] = 0 because i+1 = 4 and x = 0000000000001100
    s[x[(i+1)]] = 0100100110000100
    cs[T][x[(i+1)]] = 0100110100010110
    S = 0000010010010010
step9: done.

step10: set T ...
    x[(i+1)] = 0 because i+1 = 4 and x = 0000000000001100
    t[x[(i+1)]] = 0
    ct[T][x[(i+1)]] = 1
    T = 1
step10: done.

step7: parse G(S) as s0|s1|t0|t1 ...
    PRG(0000010010010010) = 0110011101000101010000011000100111
    s0 = 0110011101000101
    s1 = 0100000110001001
    t0 = 1
    t1 = 1
step7: done.

step8: parse CW ...
    cs = {'1': {'0': '0001100110011111', '1': '0100110010011001'}}
    ct = {'1': {'0': '0', '1': '1'}}
step8: done.

step9: set S ...
    x[(i+1)] = 0 because i+1 = 5 and x = 0000000000001100
    s[x[(i+1)]] = 0110011101000101
    cs[T][x[(i+1)]] = 0001100110011111
    S = 0111111011011010
step9: done.

step10: set T ...
    x[(i+1)] = 0 because i+1 = 5 and x = 0000000000001100
    t[x[(i+1)]] = 1
    ct[T][x[(i+1)]] = 0
    T = 1
step10: done.

step7: parse G(S) as s0|s1|t0|t1 ...
    PRG(0111111011011010) = 0011000000001011011001110100100001
    s0 = 0011000000001011
    s1 = 0110011101001000
    t0 = 0
    t1 = 1
step7: done.

step8: parse CW ...
    cs = {'1': {'0': '1010001010110111', '1': '1010111100011110'}}
    ct = {'1': {'0': '1', '1': '1'}}
step8: done.

step9: set S ...
    x[(i+1)] = 0 because i+1 = 6 and x = 0000000000001100
    s[x[(i+1)]] = 0011000000001011
    cs[T][x[(i+1)]] = 1010001010110111
    S = 1001001010111100
step9: done.

step10: set T ...
    x[(i+1)] = 0 because i+1 = 6 and x = 0000000000001100
    t[x[(i+1)]] = 0
    ct[T][x[(i+1)]] = 1
    T = 1
step10: done.

step7: parse G(S) as s0|s1|t0|t1 ...
    PRG(1001001010111100) = 0111000000001001011110110111111110
    s0 = 0111000000001001
    s1 = 0111101101111111
    t0 = 1
    t1 = 0
step7: done.

step8: parse CW ...
    cs = {'1': {'0': '0101011000001001', '1': '0110100000100011'}}
    ct = {'1': {'0': '0', '1': '1'}}
step8: done.

step9: set S ...
    x[(i+1)] = 0 because i+1 = 7 and x = 0000000000001100
    s[x[(i+1)]] = 0111000000001001
    cs[T][x[(i+1)]] = 0101011000001001
    S = 0010011000000000
step9: done.

step10: set T ...
    x[(i+1)] = 0 because i+1 = 7 and x = 0000000000001100
    t[x[(i+1)]] = 1
    ct[T][x[(i+1)]] = 0
    T = 1
step10: done.

step7: parse G(S) as s0|s1|t0|t1 ...
    PRG(0010011000000000) = 1100101101111011000011101010111101
    s0 = 1100101101111011
    s1 = 0000111010101111
    t0 = 0
    t1 = 1
step7: done.

step8: parse CW ...
    cs = {'1': {'0': '1000100111001100', '1': '1111010010110100'}}
    ct = {'1': {'0': '0', '1': '1'}}
step8: done.

step9: set S ...
    x[(i+1)] = 0 because i+1 = 8 and x = 0000000000001100
    s[x[(i+1)]] = 1100101101111011
    cs[T][x[(i+1)]] = 1000100111001100
    S = 0100001010110111
step9: done.

step10: set T ...
    x[(i+1)] = 0 because i+1 = 8 and x = 0000000000001100
    t[x[(i+1)]] = 0
    ct[T][x[(i+1)]] = 0
    T = 0
step10: done.

step7: parse G(S) as s0|s1|t0|t1 ...
    PRG(0100001010110111) = 1001101100001100111110010011110011
    s0 = 1001101100001100
    s1 = 1111100100111100
    t0 = 1
    t1 = 1
step7: done.

step8: parse CW ...
    cs = {'0': {'0': '1011100011111001', '1': '0011010011110010'}}
    ct = {'0': {'0': '1', '1': '1'}}
step8: done.

step9: set S ...
    x[(i+1)] = 0 because i+1 = 9 and x = 0000000000001100
    s[x[(i+1)]] = 1001101100001100
    cs[T][x[(i+1)]] = 1011100011111001
    S = 0010001111110101
step9: done.

step10: set T ...
    x[(i+1)] = 0 because i+1 = 9 and x = 0000000000001100
    t[x[(i+1)]] = 1
    ct[T][x[(i+1)]] = 1
    T = 0
step10: done.

step7: parse G(S) as s0|s1|t0|t1 ...
    PRG(0010001111110101) = 1000001101000101100001100011101100
    s0 = 1000001101000101
    s1 = 1000011000111011
    t0 = 0
    t1 = 0
step7: done.

step8: parse CW ...
    cs = {'0': {'0': '1010001101110001', '1': '1101111111000011'}}
    ct = {'0': {'0': '1', '1': '0'}}
step8: done.

step9: set S ...
    x[(i+1)] = 0 because i+1 = 10 and x = 0000000000001100
    s[x[(i+1)]] = 1000001101000101
    cs[T][x[(i+1)]] = 1010001101110001
    S = 0010000000110100
step9: done.

step10: set T ...
    x[(i+1)] = 0 because i+1 = 10 and x = 0000000000001100
    t[x[(i+1)]] = 0
    ct[T][x[(i+1)]] = 1
    T = 1
step10: done.

step7: parse G(S) as s0|s1|t0|t1 ...
    PRG(0010000000110100) = 1011001100111100010000101010100101
    s0 = 1011001100111100
    s1 = 0100001010101001
    t0 = 0
    t1 = 1
step7: done.

step8: parse CW ...
    cs = {'1': {'0': '0010010100010001', '1': '0110111011100110'}}
    ct = {'1': {'0': '0', '1': '1'}}
step8: done.

step9: set S ...
    x[(i+1)] = 0 because i+1 = 11 and x = 0000000000001100
    s[x[(i+1)]] = 1011001100111100
    cs[T][x[(i+1)]] = 0010010100010001
    S = 1001011000101101
step9: done.

step10: set T ...
    x[(i+1)] = 0 because i+1 = 11 and x = 0000000000001100
    t[x[(i+1)]] = 0
    ct[T][x[(i+1)]] = 0
    T = 0
step10: done.

step7: parse G(S) as s0|s1|t0|t1 ...
    PRG(1001011000101101) = 0000010100100011110100110010100101
    s0 = 0000010100100011
    s1 = 1101001100101001
    t0 = 0
    t1 = 1
step7: done.

step8: parse CW ...
    cs = {'0': {'0': '0111100011101101', '1': '1111101100100111'}}
    ct = {'0': {'0': '0', '1': '1'}}
step8: done.

step9: set S ...
    x[(i+1)] = 1 because i+1 = 12 and x = 0000000000001100
    s[x[(i+1)]] = 1101001100101001
    cs[T][x[(i+1)]] = 1111101100100111
    S = 0010100000001110
step9: done.

step10: set T ...
    x[(i+1)] = 1 because i+1 = 12 and x = 0000000000001100
    t[x[(i+1)]] = 1
    ct[T][x[(i+1)]] = 1
    T = 0
step10: done.

step7: parse G(S) as s0|s1|t0|t1 ...
    PRG(0010100000001110) = 0100101010001101000001101101011110
    s0 = 0100101010001101
    s1 = 0000011011010111
    t0 = 1
    t1 = 0
step7: done.

step8: parse CW ...
    cs = {'0': {'0': '1011111011111100', '1': '0001010011011111'}}
    ct = {'0': {'0': '0', '1': '0'}}
step8: done.

step9: set S ...
    x[(i+1)] = 1 because i+1 = 13 and x = 0000000000001100
    s[x[(i+1)]] = 0000011011010111
    cs[T][x[(i+1)]] = 0001010011011111
    S = 0001001000001000
step9: done.

step10: set T ...
    x[(i+1)] = 1 because i+1 = 13 and x = 0000000000001100
    t[x[(i+1)]] = 0
    ct[T][x[(i+1)]] = 0
    T = 0
step10: done.

step7: parse G(S) as s0|s1|t0|t1 ...
    PRG(0001001000001000) = 1101010001100111000101101000101101
    s0 = 1101010001100111
    s1 = 0001011010001011
    t0 = 0
    t1 = 1
step7: done.

step8: parse CW ...
    cs = {'0': {'0': '1001101100100110', '1': '0100011110011000'}}
    ct = {'0': {'0': '0', '1': '0'}}
step8: done.

step9: set S ...
    x[(i+1)] = 0 because i+1 = 14 and x = 0000000000001100
    s[x[(i+1)]] = 1101010001100111
    cs[T][x[(i+1)]] = 1001101100100110
    S = 0100111101000001
step9: done.

step10: set T ...
    x[(i+1)] = 0 because i+1 = 14 and x = 0000000000001100
    t[x[(i+1)]] = 0
    ct[T][x[(i+1)]] = 0
    T = 0
step10: done.

step7: parse G(S) as s0|s1|t0|t1 ...
    PRG(0100111101000001) = 0000111100011011101101100001101000
    s0 = 0000111100011011
    s1 = 1011011000011010
    t0 = 0
    t1 = 0
step7: done.

step8: parse CW ...
    cs = {'0': {'0': '1011001010001010', '1': '1111010010010000'}}
    ct = {'0': {'0': '0', '1': '0'}}
step8: done.

step9: set S ...
    x[(i+1)] = 0 because i+1 = 15 and x = 0000000000001100
    s[x[(i+1)]] = 0000111100011011
    cs[T][x[(i+1)]] = 1011001010001010
    S = 1011110110010001
step9: done.

step10: set T ...
    x[(i+1)] = 0 because i+1 = 15 and x = 0000000000001100
    t[x[(i+1)]] = 0
    ct[T][x[(i+1)]] = 0
    T = 0
step10: done.

step12: return ...
    S = 1011110110010001
    PRG(S) = 0000011101000000100010101000111000
    int(PRG(S), 2) = 486681144
    w = 27
    (int(PRG(S), 2) * w) % mod = 51
51



step1: recieving PRG ...
step1: done.

step2: parse input x ...
    x = 0000000000001100
    n = 16
step2: done.

step3: parse k_list as s0|s1|t0|t1, cw_list, w ...
    s0 = 0001100000111100
    s1 = 1100111101111010
    t0 = 0
    t1 = 1
step3: done.

step4: set S ...
    S  = 0001100000111100
step4: done.

step5: set T ...
    T  = 0
step5: done.

step7: parse G(S) as s0|s1|t0|t1 ...
    PRG(0001100000111100) = 1111010000110111001110010000011101
    s0 = 1111010000110111
    s1 = 0011100100000111
    t0 = 0
    t1 = 1
step7: done.

step8: parse CW ...
    cs = {'0': {'0': '1001000101000001', '1': '1100001000010100'}}
    ct = {'0': {'0': '1', '1': '0'}}
step8: done.

step9: set S ...
    x[(i+1)] = 0 because i+1 = 1 and x = 0000000000001100
    s[x[(i+1)]] = 1111010000110111
    cs[T][x[(i+1)]] = 1001000101000001
    S = 0110010101110110
step9: done.

step10: set T ...
    x[(i+1)] = 0 because i+1 = 1 and x = 0000000000001100
    t[x[(i+1)]] = 0
    ct[T][x[(i+1)]] = 1
    T = 1
step10: done.

step7: parse G(S) as s0|s1|t0|t1 ...
    PRG(0110010101110110) = 1100011010100100100100010111100001
    s0 = 1100011010100100
    s1 = 1001000101111000
    t0 = 0
    t1 = 1
step7: done.

step8: parse CW ...
    cs = {'1': {'0': '0010111100010011', '1': '1100100101010110'}}
    ct = {'1': {'0': '0', '1': '0'}}
step8: done.

step9: set S ...
    x[(i+1)] = 0 because i+1 = 2 and x = 0000000000001100
    s[x[(i+1)]] = 1100011010100100
    cs[T][x[(i+1)]] = 0010111100010011
    S = 1110100110110111
step9: done.

step10: set T ...
    x[(i+1)] = 0 because i+1 = 2 and x = 0000000000001100
    t[x[(i+1)]] = 0
    ct[T][x[(i+1)]] = 0
    T = 0
step10: done.

step7: parse G(S) as s0|s1|t0|t1 ...
    PRG(1110100110110111) = 1100101101110101101100101010100111
    s0 = 1100101101110101
    s1 = 1011001010101001
    t0 = 1
    t1 = 1
step7: done.

step8: parse CW ...
    cs = {'0': {'0': '1010100100111001', '1': '0101111010001111'}}
    ct = {'0': {'0': '1', '1': '1'}}
step8: done.

step9: set S ...
    x[(i+1)] = 0 because i+1 = 3 and x = 0000000000001100
    s[x[(i+1)]] = 1100101101110101
    cs[T][x[(i+1)]] = 1010100100111001
    S = 0110001001001100
step9: done.

step10: set T ...
    x[(i+1)] = 0 because i+1 = 3 and x = 0000000000001100
    t[x[(i+1)]] = 1
    ct[T][x[(i+1)]] = 1
    T = 0
step10: done.

step7: parse G(S) as s0|s1|t0|t1 ...
    PRG(0110001001001100) = 0101001010110000111101010000010001
    s0 = 0101001010110000
    s1 = 1111010100000100
    t0 = 0
    t1 = 1
step7: done.

step8: parse CW ...
    cs = {'0': {'0': '1101010111010010', '1': '0000010111101010'}}
    ct = {'0': {'0': '0', '1': '0'}}
step8: done.

step9: set S ...
    x[(i+1)] = 0 because i+1 = 4 and x = 0000000000001100
    s[x[(i+1)]] = 0101001010110000
    cs[T][x[(i+1)]] = 1101010111010010
    S = 1000011101100010
step9: done.

step10: set T ...
    x[(i+1)] = 0 because i+1 = 4 and x = 0000000000001100
    t[x[(i+1)]] = 0
    ct[T][x[(i+1)]] = 0
    T = 0
step10: done.

step7: parse G(S) as s0|s1|t0|t1 ...
    PRG(1000011101100010) = 0111111110010011101100100101111011
    s0 = 0111111110010011
    s1 = 1011001001011110
    t0 = 1
    t1 = 1
step7: done.

step8: parse CW ...
    cs = {'0': {'0': '1101101001110000', '1': '1011111101001110'}}
    ct = {'0': {'0': '1', '1': '1'}}
step8: done.

step9: set S ...
    x[(i+1)] = 0 because i+1 = 5 and x = 0000000000001100
    s[x[(i+1)]] = 0111111110010011
    cs[T][x[(i+1)]] = 1101101001110000
    S = 1010010111100011
step9: done.

step10: set T ...
    x[(i+1)] = 0 because i+1 = 5 and x = 0000000000001100
    t[x[(i+1)]] = 1
    ct[T][x[(i+1)]] = 1
    T = 0
step10: done.

step7: parse G(S) as s0|s1|t0|t1 ...
    PRG(1010010111100011) = 0111101001011001001100001010110100
    s0 = 0111101001011001
    s1 = 0011000010101101
    t0 = 0
    t1 = 0
step7: done.

step8: parse CW ...
    cs = {'0': {'0': '0101011001111001', '1': '1111100011111011'}}
    ct = {'0': {'0': '0', '1': '0'}}
step8: done.

step9: set S ...
    x[(i+1)] = 0 because i+1 = 6 and x = 0000000000001100
    s[x[(i+1)]] = 0111101001011001
    cs[T][x[(i+1)]] = 0101011001111001
    S = 0010110000100000
step9: done.

step10: set T ...
    x[(i+1)] = 0 because i+1 = 6 and x = 0000000000001100
    t[x[(i+1)]] = 0
    ct[T][x[(i+1)]] = 0
    T = 0
step10: done.

step7: parse G(S) as s0|s1|t0|t1 ...
    PRG(0010110000100000) = 1001111100110111100011101001111001
    s0 = 1001111100110111
    s1 = 1000111010011110
    t0 = 0
    t1 = 1
step7: done.

step8: parse CW ...
    cs = {'0': {'0': '1100000010101010', '1': '1001110111000010'}}
    ct = {'0': {'0': '0', '1': '0'}}
step8: done.

step9: set S ...
    x[(i+1)] = 0 because i+1 = 7 and x = 0000000000001100
    s[x[(i+1)]] = 1001111100110111
    cs[T][x[(i+1)]] = 1100000010101010
    S = 0101111110011101
step9: done.

step10: set T ...
    x[(i+1)] = 0 because i+1 = 7 and x = 0000000000001100
    t[x[(i+1)]] = 0
    ct[T][x[(i+1)]] = 0
    T = 0
step10: done.

step7: parse G(S) as s0|s1|t0|t1 ...
    PRG(0101111110011101) = 0011100000000100011000101011000011
    s0 = 0011100000000100
    s1 = 0110001010110000
    t0 = 1
    t1 = 1
step7: done.

step8: parse CW ...
    cs = {'0': {'0': '1011001001000100', '1': '1001100010101011'}}
    ct = {'0': {'0': '0', '1': '1'}}
step8: done.

step9: set S ...
    x[(i+1)] = 0 because i+1 = 8 and x = 0000000000001100
    s[x[(i+1)]] = 0011100000000100
    cs[T][x[(i+1)]] = 1011001001000100
    S = 1000101001000000
step9: done.

step10: set T ...
    x[(i+1)] = 0 because i+1 = 8 and x = 0000000000001100
    t[x[(i+1)]] = 1
    ct[T][x[(i+1)]] = 0
    T = 1
step10: done.

step7: parse G(S) as s0|s1|t0|t1 ...
    PRG(1000101001000000) = 1000100111100100000011011100101111
    s0 = 1000100111100100
    s1 = 0000110111001011
    t0 = 1
    t1 = 1
step7: done.

step8: parse CW ...
    cs = {'1': {'0': '0100011011110111', '1': '1100000000000101'}}
    ct = {'1': {'0': '0', '1': '1'}}
step8: done.

step9: set S ...
    x[(i+1)] = 0 because i+1 = 9 and x = 0000000000001100
    s[x[(i+1)]] = 1000100111100100
    cs[T][x[(i+1)]] = 0100011011110111
    S = 1100111100010011
step9: done.

step10: set T ...
    x[(i+1)] = 0 because i+1 = 9 and x = 0000000000001100
    t[x[(i+1)]] = 1
    ct[T][x[(i+1)]] = 0
    T = 1
step10: done.

step7: parse G(S) as s0|s1|t0|t1 ...
    PRG(1100111100010011) = 0111111001110111100001111100111011
    s0 = 0111111001110111
    s1 = 1000011111001110
    t0 = 1
    t1 = 1
step7: done.

step8: parse CW ...
    cs = {'1': {'0': '0100010000111101', '1': '1101111000110110'}}
    ct = {'1': {'0': '1', '1': '1'}}
step8: done.

step9: set S ...
    x[(i+1)] = 0 because i+1 = 10 and x = 0000000000001100
    s[x[(i+1)]] = 0111111001110111
    cs[T][x[(i+1)]] = 0100010000111101
    S = 0011101001001010
step9: done.

step10: set T ...
    x[(i+1)] = 0 because i+1 = 10 and x = 0000000000001100
    t[x[(i+1)]] = 1
    ct[T][x[(i+1)]] = 1
    T = 0
step10: done.

step7: parse G(S) as s0|s1|t0|t1 ...
    PRG(0011101001001010) = 0110111100001100100111001010100001
    s0 = 0110111100001100
    s1 = 1001110010101000
    t0 = 0
    t1 = 1
step7: done.

step8: parse CW ...
    cs = {'0': {'0': '1000000001111011', '1': '1011000011100111'}}
    ct = {'0': {'0': '1', '1': '1'}}
step8: done.

step9: set S ...
    x[(i+1)] = 0 because i+1 = 11 and x = 0000000000001100
    s[x[(i+1)]] = 0110111100001100
    cs[T][x[(i+1)]] = 1000000001111011
    S = 1110111101110111
step9: done.

step10: set T ...
    x[(i+1)] = 0 because i+1 = 11 and x = 0000000000001100
    t[x[(i+1)]] = 0
    ct[T][x[(i+1)]] = 1
    T = 1
step10: done.

step7: parse G(S) as s0|s1|t0|t1 ...
    PRG(1110111101110111) = 1100110010000101111100000000110011
    s0 = 1100110010000101
    s1 = 1111000000001100
    t0 = 1
    t1 = 1
step7: done.

step8: parse CW ...
    cs = {'1': {'0': '1011000101001011', '1': '1111110101101000'}}
    ct = {'1': {'0': '1', '1': '0'}}
step8: done.

step9: set S ...
    x[(i+1)] = 1 because i+1 = 12 and x = 0000000000001100
    s[x[(i+1)]] = 1111000000001100
    cs[T][x[(i+1)]] = 1111110101101000
    S = 0000110101100100
step9: done.

step10: set T ...
    x[(i+1)] = 1 because i+1 = 12 and x = 0000000000001100
    t[x[(i+1)]] = 1
    ct[T][x[(i+1)]] = 0
    T = 1
step10: done.

step7: parse G(S) as s0|s1|t0|t1 ...
    PRG(0000110101100100) = 1110000100001010010011000000011001
    s0 = 1110000100001010
    s1 = 0100110000000110
    t0 = 0
    t1 = 1
step7: done.

step8: parse CW ...
    cs = {'1': {'0': '0001010101111011', '1': '1011001001111101'}}
    ct = {'1': {'0': '1', '1': '0'}}
step8: done.

step9: set S ...
    x[(i+1)] = 1 because i+1 = 13 and x = 0000000000001100
    s[x[(i+1)]] = 0100110000000110
    cs[T][x[(i+1)]] = 1011001001111101
    S = 1111111001111011
step9: done.

step10: set T ...
    x[(i+1)] = 1 because i+1 = 13 and x = 0000000000001100
    t[x[(i+1)]] = 1
    ct[T][x[(i+1)]] = 0
    T = 1
step10: done.

step7: parse G(S) as s0|s1|t0|t1 ...
    PRG(1111111001111011) = 1011111000000001001110010000110110
    s0 = 1011111000000001
    s1 = 0011100100001101
    t0 = 1
    t1 = 0
step7: done.

step8: parse CW ...
    cs = {'1': {'0': '0101100110101110', '1': '0110100000011110'}}
    ct = {'1': {'0': '0', '1': '1'}}
step8: done.

step9: set S ...
    x[(i+1)] = 0 because i+1 = 14 and x = 0000000000001100
    s[x[(i+1)]] = 1011111000000001
    cs[T][x[(i+1)]] = 0101100110101110
    S = 1110011110101111
step9: done.

step10: set T ...
    x[(i+1)] = 0 because i+1 = 14 and x = 0000000000001100
    t[x[(i+1)]] = 1
    ct[T][x[(i+1)]] = 0
    T = 1
step10: done.

step7: parse G(S) as s0|s1|t0|t1 ...
    PRG(1110011110101111) = 1001110010011001000010111010100100
    s0 = 1001110010011001
    s1 = 0000101110101001
    t0 = 0
    t1 = 0
step7: done.

step8: parse CW ...
    cs = {'1': {'0': '0111101100000111', '1': '0100100100100011'}}
    ct = {'1': {'0': '1', '1': '0'}}
step8: done.

step9: set S ...
    x[(i+1)] = 0 because i+1 = 15 and x = 0000000000001100
    s[x[(i+1)]] = 1001110010011001
    cs[T][x[(i+1)]] = 0111101100000111
    S = 1110011110011110
step9: done.

step10: set T ...
    x[(i+1)] = 0 because i+1 = 15 and x = 0000000000001100
    t[x[(i+1)]] = 0
    ct[T][x[(i+1)]] = 1
    T = 1
step10: done.

step12: return ...
    S = 1110011110011110
    PRG(S) = 1001111110000001101110111111011011
    int(PRG(S), 2) = 10704318427
    w = 27
    (int(PRG(S), 2) * w) % mod = 57
57

====== Decryption Phase ======

f(x = 12) = 1
```