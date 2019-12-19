#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import resolution as r
import model_checking

def model_checking_ans():
    # P
    formula_p_1 = model_checking.Formula("P")
    # P => Q
    formula_p_2 = model_checking.Formula("P")
    formula_q = model_checking.Formula("Q")
    imply = model_checking.Implication(False, formula_p_2, formula_q)
    # KB: {P, P => Q}
    conj_kb = model_checking.Conjunction(False, formula_p_1, imply)
    # Query: Q
    formula_query = model_checking.Formula("Q")
    return model_checking.print_ans(conj_kb, formula_query)


def resolution_ans():
    formula_p_1 = r.Formula("P")
    # P => Q
    formula_p_2 = r.Formula("P")
    formula_q = r.Formula("Q")
    # CNF
    # P=>Q turn to !PvQ
    formula_p_2.negation = True
    imply_list = [formula_p_2, formula_q]
    kb = [[formula_p_1], imply_list]
    alpha = r.Formula("Q", neg=True)  # alpha means negated alpha
    return r.pl_resolution(kb, alpha)

if __name__ == "__main__":
    print("Modus Ponens test")
    print("Knowledge base:\n P=>Q \n P""")
    print("Query: Q")
    print("Ans with model checking: {} \nAns with resolution: {} \n".format(model_checking_ans(), resolution_ans()))