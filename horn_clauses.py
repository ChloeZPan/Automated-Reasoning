#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import resolution as r
import model_checking


def model_checking_ans():
    # MYTHICAL => IMMORTAL
    myth = model_checking.Formula("MYTHICAL")
    immortal_1 = model_checking.Formula("IMMORTAL")
    imply_1 = model_checking.Implication(False, myth, immortal_1)

    # !MYTHICAL => (!IMMORTAL ^ MAMMAL)
    not_myth = model_checking.Formula("MYTHICAL", True)
    not_immortal = model_checking.Formula("IMMORTAL", True)
    mammal_1 = model_checking.Formula("MAMMAL")
    conj_sub = model_checking.Conjunction(False, not_immortal, mammal_1)
    imply_2 = model_checking.Implication(False, not_myth, conj_sub)

    conj_left = model_checking.Conjunction(False, imply_1, imply_2)

    # (IMMORTAL V MAMMAL) => HORNED
    immortal_2 = model_checking.Formula("IMMORTAL")
    mammal_2 = model_checking.Formula("MAMMAL")
    disj_sub = model_checking.Disjunction(False, immortal_2, mammal_2)
    horn_1 = model_checking.Formula("HORNED")
    imply_3 = model_checking.Implication(False, disj_sub, horn_1)

    # HORNED => MAGICAL
    horn_2 = model_checking.Formula("HORNED")
    magical = model_checking.Formula("MAGICAL")
    imply_4 = model_checking.Implication(False, horn_2, magical)

    conj_right = model_checking.Conjunction(False, imply_3, imply_4)
    conj_kb = model_checking.Conjunction(False, conj_left, conj_right)  # Knowledge base

    query_myth = model_checking.Formula("MYTHICAL")
    query_magical = model_checking.Formula("MAGICAL")
    query_horn = model_checking.Formula("HORNED")

    a1 = model_checking.print_ans(conj_kb, query_myth)
    a2 = model_checking.print_ans(conj_kb, query_magical)
    a3 = model_checking.print_ans(conj_kb, query_horn)
    return [a1, a2, a3]


def resolution_ans():
    # Horn Clause
    # Mythical => Immortal
    # CNF !Mythical v Immortal
    not_myth = r.Formula("MYTHICAL", neg=True)
    immortal = r.Formula("IMMORTAL")

    # !Mythical => (!Immortal ^ Mammal)
    # CNF (Mythical v !Immortal) ^ (Mythical v Mammal)
    not_immortal = r.Formula("IMMORTAL", neg=True)
    myth = r.Formula("MYTHICAL")
    mammal = r.Formula("MAMMAL")

    # (Immortal v Mammal) => Horned
    # CNF (!Immortal v Horned) ^ (!Mammal v Horned)
    horned = r.Formula("HORNED")
    not_mammal = r.Formula("MAMMAL", neg=True)

    # Horned => Magical
    # CNF !Horned v Magical
    not_horned = r.Formula("HORNED", neg=True)
    magical = r.Formula("MAGICAL")

    # alphas
    query_myth = r.Formula("MYTHICAL", neg=True)
    query_magical = r.Formula("MAGICAL", neg=True)
    query_horn = r.Formula("HORNED", neg=True)

    # kb
    kb = [[not_myth, immortal], [myth, not_immortal], [myth, mammal], [not_immortal, horned],
          [not_mammal, horned], [not_horned, magical]]
    a1 = r.pl_resolution(kb, query_myth)
    a2 = r.pl_resolution(kb, query_magical)
    a3 = r.pl_resolution(kb, query_horn)
    return [a1, a2, a3]


if __name__ == "__main__":
    print('Horn Clauses test.')
    print('Knowledge base:')
    print('(MYTHICAL => IMMORTAL) If the unicorn is mythical, then it is immortal;')
    print('(!MYTHICAL => MAMMAL) but if it is not mythical, then it is a mortal mammal;')
    print('((IMMORTAL V MAMMAL) => HORNED) If the unicorn is either immortal or a mammal, then it is horned;')
    print('(HORNED => MAGICAL) The unicorn is magical if it is horned.')
    print('Query: MYTHICAL, MAGICAL, HORNED \n')

    # alpha is myth
    print("(1) Can we prove that the unicorn is mythical? \n -Ans with model checking {} \n "
          "-Ans with resolution {} \n".format(model_checking_ans()[0], resolution_ans()[0]))
    # alpha is magical
    print("(2) Can we prove that the unicorn is mythical? \n -Ans with model checking {} \n "
          "-Ans with resolution {} \n ".format(model_checking_ans()[1], resolution_ans()[1]))
    # alpha is horned
    print("(3) Can we prove that the unicorn is mythical? \n -Ans with model checking {} \n "
          "-Ans with resolution {} \n ".format(model_checking_ans()[2], resolution_ans()[2]))