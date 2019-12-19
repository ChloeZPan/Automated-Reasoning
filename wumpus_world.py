#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import resolution as r
import model_checking

def model_checking_ans():
    not_p11 = model_checking.Formula("P11", True)  # !P(1,1)
    not_b11 = model_checking.Formula("B11", True)  # !B(1,1)
    b21_1 = model_checking.Formula("B21", True)  # B(2,1)
    conj_left_sub = model_checking.Conjunction(False, not_b11, b21_1)
    conj_left = model_checking.Conjunction(False, not_p11, conj_left_sub)  # !P(1,1) ^ !B(1,1) ^ B(2,1)

    b11 = model_checking.Formula("B11")
    p12 = model_checking.Formula("P12")
    p21 = model_checking.Formula("P21")
    disj_1 = model_checking.Disjunction(False, p12, p21)
    bi_1 = model_checking.Biconditional(False, b11, disj_1)  # B(1,1) <=> (P(1,2) V P(2,1))

    b21_2 = model_checking.Formula("B21")
    p11 = model_checking.Formula("P11")
    p22 = model_checking.Formula("P22")
    p31 = model_checking.Formula("P31")
    disj_2 = model_checking.Disjunction(False, p22, p31)
    disj_3 = model_checking.Disjunction(False, p11, disj_2)
    bi_2 = model_checking.Biconditional(False, b21_2, disj_3)  # B(2,1) <=> (P(1,1) V P(2,2) V P(3,1))

    conj_right = model_checking.Conjunction(False, bi_1, bi_2)
    conj_kb = model_checking.Conjunction(False, conj_left, conj_right)  # Knowledge base

    formula_query = model_checking.Formula("P12")
    return model_checking.print_ans(conj_kb, formula_query)


def resolution_ans():
    # Wumpus World
    not_p11 = r.Formula("P11", True)  # !P(1,1)
    not_b11 = r.Formula("B11", True)  # !B(1,1)
    b21_1 = r.Formula("B21", True)  # B(2,1)
    # !P(1,1) ^ !B(1,1) ^ B(2,1)

    b11 = r.Formula("B11")
    p12 = r.Formula("P12")
    p21 = r.Formula("P21")
    # B(1,1) <=> (P(1,2) V P(2,1))

    b21_2 = r.Formula("B21")
    p11 = r.Formula("P11")
    p22 = r.Formula("P22")
    p31 = r.Formula("P31")
    # B(2,1) <=> (P(1,1) V P(2,2) V P(3,1))

    not_p12 = r.Formula("P12", neg=True)  # !P(1,2)
    not_p21 = r.Formula("P21", neg=True)  # !P(2,1)
    not_b21 = r.Formula("B21", neg=True)  # !B(2,1)
    not_p22 = r.Formula("P22", neg=True)  # !P(2,2)
    not_p31 = r.Formula("P31", neg=True)  # !P(3,1)
    kb = [[not_p11], [not_b11], [b21_1], [not_b11, p12, p21], [not_p12, b11], [not_p21, b11], [not_b21, p11, p22, p31],
          [not_p11, b21_2], [not_p22, b21_2], [not_p31, b21_2]]
    # alpha is !P(1,2)
    alpha = r.Formula("P12")  # here alpha means negated alpha
    if r.pl_resolution(kb, alpha) is True:  # means no pit at P(1,2) is True
        return False
    elif r.pl_resolution(kb, alpha) is False:
        return True
    else:
        return 'MAYBE'


if __name__ == "__main__":
    print("Wumpus World test")
    print("Knowledge base:\n !P(1,1) ^ !B(1,1) ^ B(2,1) \n B(1,1) <=> (P(1,2) V P(2,1)) \n "
          "B(2,1) <=> (P(1,1) V P(2,2) V P(3,1))")
    print("Query: P(1,2) \n")
    print("Ans with model checking: {} \nAns with resolution: {} \n".format(model_checking_ans(), resolution_ans()))