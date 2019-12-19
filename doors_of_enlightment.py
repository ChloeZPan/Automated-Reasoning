#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import resolution as r
import model_checking
import time

def model_checking_ans1():
    # A <=> X
    a_1 = model_checking.Formula("A")
    x_1 = model_checking.Formula("X")
    bi_a = model_checking.Biconditional(False, a_1, x_1)

    # B <=> (Y V Z)
    b_1 = model_checking.Formula("B")
    y_1 = model_checking.Formula("Y")
    z_1 = model_checking.Formula("Z")
    disj_1 = model_checking.Disjunction(False, y_1, z_1)
    bi_b = model_checking.Biconditional(False, b_1, disj_1)

    conj_ab = model_checking.Conjunction(False, bi_a, bi_b)

    # C <=> (A ^ B)
    c_1 = model_checking.Formula("C")
    a_2 = model_checking.Formula("A")
    b_2 = model_checking.Formula("B")
    conj_1 = model_checking.Conjunction(False, a_2, b_2)
    bi_c = model_checking.Biconditional(False, c_1, conj_1)

    # D <=> (X ^ Y)
    d_1 = model_checking.Formula("D")
    x_2 = model_checking.Formula("X")
    y_2 = model_checking.Formula("Y")
    conj_2 = model_checking.Conjunction(False, x_2, y_2)
    bi_d = model_checking.Biconditional(False, d_1, conj_2)

    conj_cd = model_checking.Conjunction(False, bi_c, bi_d)
    conj_abcd = model_checking.Conjunction(False, conj_ab, conj_cd)

    # E <=> (X ^ Z)
    e_1 = model_checking.Formula("E")
    x_3 = model_checking.Formula("X")
    z_2 = model_checking.Formula("Z")
    conj_3 = model_checking.Conjunction(False, x_3, z_2)
    bi_e = model_checking.Biconditional(False, e_1, conj_3)

    # F <=> (D V E)
    f_1 = model_checking.Formula("F")
    d_2 = model_checking.Formula("D")
    e_2 = model_checking.Formula("E")
    disj_2 = model_checking.Disjunction(False, d_2, e_2)
    bi_f = model_checking.Biconditional(False, f_1, disj_2)

    conj_ef = model_checking.Conjunction(False, bi_e, bi_f)

    # G <=> (C => F)
    g_1 = model_checking.Formula("G")
    c_2 = model_checking.Formula("C")
    f_2 = model_checking.Formula("F")
    imply_1 = model_checking.Implication(False, c_2, f_2)
    bi_g = model_checking.Biconditional(False, g_1, imply_1)

    # H <=> ((G ^ H) => A)
    h_1 = model_checking.Formula("H")
    g_2 = model_checking.Formula("G")
    h_2 = model_checking.Formula("H")
    conj_4 = model_checking.Conjunction(False, g_2, h_2)
    a_3 = model_checking.Formula("A")
    imply_2 = model_checking.Implication(False, conj_4, a_3)
    bi_h = model_checking.Biconditional(False, h_1, imply_2)

    conj_gh = model_checking.Conjunction(False, bi_g, bi_h)
    conj_efgh = model_checking.Conjunction(False, conj_ef, conj_gh)
    conj_kb = model_checking.Conjunction(False, conj_abcd, conj_efgh)  # Knowledge base

    query_x = model_checking.Formula("X")
    query_y = model_checking.Formula("Y")
    query_z = model_checking.Formula("Z")
    query_w = model_checking.Formula("W")

    a1 = model_checking.print_ans(conj_kb, query_x)
    a2 = model_checking.print_ans(conj_kb, query_y)
    a3 = model_checking.print_ans(conj_kb, query_z)
    a4 = model_checking.print_ans(conj_kb, query_w)
    return [a1, a2, a3, a4]


def model_checking_ans2():
    # A <=> X
    a_1 = model_checking.Formula("A")
    x_1 = model_checking.Formula("X")
    bi_a = model_checking.Biconditional(False, a_1, x_1)

    # H <=> ((G ^ H) => A)
    h_1 = model_checking.Formula("H")
    g_1 = model_checking.Formula("G")
    h_2 = model_checking.Formula("H")
    conj_1 = model_checking.Conjunction(False, g_1, h_2)
    a_2 = model_checking.Formula("A")
    imply_1 = model_checking.Implication(False, conj_1, a_2)
    bi_h = model_checking.Biconditional(False, h_1, imply_1)

    conj_left = model_checking.Conjunction(False, bi_a, bi_h)

    # C <=> (A ^ ?)
    c_1 = model_checking.Formula("C")
    a_3 = model_checking.Formula("A")
    unknown_1 = model_checking.Formula("Unknown 1")
    conj_2 = model_checking.Conjunction(False, a_3, unknown_1)
    bi_c = model_checking.Biconditional(False, c_1, conj_2)

    # G <=> (C => ?)
    g_2 = model_checking.Formula("G")
    c_2 = model_checking.Formula("C")
    unknown_2 = model_checking.Formula("Unknown 2")
    imply_2 = model_checking.Implication(False, c_2, unknown_2)
    bi_g = model_checking.Biconditional(False, g_2, imply_2)

    conj_right = model_checking.Conjunction(False, bi_c, bi_g)
    conj_kb = model_checking.Conjunction(False, conj_left, conj_right)  # Knowledge base

    query_x = model_checking.Formula("X")
    query_y = model_checking.Formula("Y")
    query_z = model_checking.Formula("Z")
    query_w = model_checking.Formula("W")

    a1 = model_checking.print_ans(conj_kb, query_x)
    a2 = model_checking.print_ans(conj_kb, query_y)
    a3 = model_checking.print_ans(conj_kb, query_z)
    a4 = model_checking.print_ans(conj_kb, query_w)
    return [a1, a2, a3, a4]


def resolution_ans1():
    # The Doors of Enlightment
    # A <=> X
    # CNF (!A v X) ^ (!X v A)
    a = r.Formula("A")
    not_a = r.Formula("A", neg=True)
    x = r.Formula("X")
    not_x = r.Formula("X", neg=True)

    # B <=> (Y v Z)
    # CNF (!B v Y v Z) ^ (!Y v !Z v B)
    b = r.Formula("B")
    y = r.Formula("Y")
    z = r.Formula("Z")
    not_b = r.Formula("B", neg=True)
    not_y = r.Formula("Y", neg=True)
    not_z = r.Formula("Z", neg=True)

    # C <=> (A ^ B)
    # CNF (!C v A) ^ (!C v B) ^ (!A v !B v C)
    c = r.Formula("C")
    not_c = r.Formula("C", neg=True)

    # D <=> (X ^ Y)
    # CNF (!D v X) ^ (!D v Y) ^ (!X v !Y v D)
    d = r.Formula("D")
    not_d = r.Formula("D", neg=True)

    # E <=> (X ^ Z)
    # CNF (!E v X) ^ (!E v Z) ^ (!X v !Z v E)
    e = r.Formula("E")
    not_e = r.Formula("E", neg=True)

    # F <=> (D v E)
    # CNF (!F v D v E) ^ (D v !F) ^ (E v F)
    f = r.Formula("F")
    not_f = r.Formula("F", neg=True)

    # G <=> (C => F)
    # CNF (!G v !C v F) ^ (C v G) ^ (!F v G)
    g = r.Formula("G")
    not_g = r.Formula("G", neg=True)

    # H <=> ((G ^ H) => A)
    # CNF (!G v !H v A) ^ (G v H) ^ (H) ^(!A v H)
    h = r.Formula("H")
    not_h = r.Formula("H", neg=True)

    # # kb
    kb = [[not_a, x], [not_x, a], [not_b, y, z], [not_y, not_z, b], [not_c, a], [not_c, b], [not_a, not_b, c],
          [not_d, x], [not_d, y], [not_x, not_y, d], [not_e, x], [not_e, z], [not_x, not_z, e],
          [not_f, d, e], [not_f, d], [e, f], [not_g, not_c, f], [c, g], [not_f, g], [not_g, not_h, a], [g, h],
          [h], [not_a, h]]

    # alphas
    q_x = r.Formula("X", neg=True)
    q_y = r.Formula("Y", neg=True)
    q_z = r.Formula("Z", neg=True)
    q_w = r.Formula("W", neg=True)

    a1 = r.pl_resolution(kb, q_x)
    a2 = "Run too long. Cannot get answer"  # r.pl_resolution(kb, q_y)
    a3 = "Run too long. Cannot get answer"  # r.pl_resolution(kb, q_z)
    a4 = "Run too long. Cannot get answer"  # r.pl_resolution(kb, q_w)
    return [a1, a2, a3, a4]


def resolution_ans2():
    # The Doors of Enlightment
    # A <=> X
    # CNF (!A v X) ^ (!X v A)
    a = r.Formula("A")
    not_a = r.Formula("A", neg=True)
    x = r.Formula("X")
    not_x = r.Formula("X", neg=True)

    # C <=> (A ^ B)
    # CNF (!C v A) ^ (!C v B) ^ (!A v !B v C)
    c = r.Formula("C")
    not_c = r.Formula("C", neg=True)

    # G <=> (C => F)
    # CNF (!G v !C v F) ^ (C v G) ^ (!F v G)
    g = r.Formula("G")
    not_g = r.Formula("G", neg=True)

    # H <=> ((G ^ H) => A)
    # CNF (!G v !H v A) ^ (G v H) ^ (H) ^(!A v H)
    h = r.Formula("H")
    not_h = r.Formula("H", neg=True)
    # A <=> X
    # CNF (!A v X) ^ (!X v A)
    # H <=> ((G ^ H) => A)
    # CNF (!G v !H v A) ^ (G v H) ^ (H) ^(!A v H)
    # C <=> (A ^ ?)
    # CNF (!C v A) ^ (!C v ?) ^ (!A v !? v C)
    unknown_1 = r.Formula("Unknown 1")
    not_unknown_1 = r.Formula("Unknown 1", neg=True)
    # G <=> (C => ?)
    # CNF (!G v !C v ?) ^ (C v G) ^ (!? v G)
    unknown_2 = r.Formula("Unknown 2")
    not_unknown_2 = r.Formula("Unknown 2", neg=True)
    # alphas
    q_x = r.Formula("X", neg=True)
    q_y = r.Formula("Y", neg=True)
    q_z = r.Formula("Z", neg=True)
    q_w = r.Formula("W", neg=True)

    kb = [[not_a, x], [not_x, a], [not_g, not_h, a], [g, h], [not_a, h],
          [not_c, a], [not_c, unknown_1], [not_a, not_unknown_1, c], [not_g, not_c, unknown_2],
          [c, g], [not_unknown_2, g]]
    a1 = "Run too long. Cannot get answer"  # r.pl_resolution(kb, q_x)
    a2 = "Run too long. Cannot get answer"  # r.pl_resolution(kb, q_y)
    a3 = "Run too long. Cannot get answer"  # r.pl_resolution(kb, q_z)
    a4 = "Run too long. Cannot get answer"  # r.pl_resolution(kb, q_w)
    return [a1, a2, a3, a4]


if __name__ == "__main__":
    print('The Doors of Enlightenment test.')
    print()
    print('(a) Smullyan\'s problem:')
    print('Knowledge base:')
    print('A: X is a good door. (A <=> X)')
    print('B: At least one of the doors Y or Z is good. (B <=> (Y V Z))')
    print('C: A and B are both knights. (C <=> (A ^ B))')
    print('D: X and Y are both good doors. (D <=> (X ^ Y))')
    print('E: X and Z are both good doors. (E <=> (X ^ Z))')
    print('F: Either D or E is a knight. (F <=> (D V E))')
    print('G: If C is a knight, so is F. (G <=> (C => F))')
    print('H: If G and I (meaning H) are knights, so is A. (H <=> ((G ^ H) => A))')
    print('Query: X, Y, Z, W')
    print("Query: X \n-Ans with model checking: {} \n"
          "-Ans with resolution: {} \n".format(model_checking_ans1()[0], resolution_ans1()[0]))
    print("Query: Y \n-Ans with model checking: {} \n"
          "-Ans with resolution: {} \n".format(model_checking_ans1()[1], resolution_ans1()[1]))
    print("Query: Z \n-Ans with model checking: {} \n"
          "-Ans with resolution: {} \n".format(model_checking_ans1()[2], resolution_ans1()[2]))
    print("Query: W \n-Ans with model checking: {} \n"
          "-Ans with resolution: {} \n".format(model_checking_ans1()[3], resolution_ans1()[3]))

    print()
    print('(b) Liu\'s problem:')
    print('Knowledge base:')
    print('A: X is a good door. (A <=> X)')
    print('H: If G and I (meaning H) are knights, so is A. (H <=> ((G ^ H) => A))')
    print('C: A and ... are both knights. (C <=> (A ^ ?))')
    print('G: If C is a knight, then ... (G <=> (C => ?))')
    print('Query: X, Y, Z, W')
    print("Query: X \n-Ans with model checking: {} \n"
          "-Ans with resolution: {} \n".format(model_checking_ans2()[0], resolution_ans2()[0]))
    print("Query: Y \n-Ans with model checking: {} \n"
          "-Ans with resolution: {} \n".format(model_checking_ans2()[1], resolution_ans2()[1]))
    print("Query: Z \n-Ans with model checking: {} \n"
          "-Ans with resolution: {} \n".format(model_checking_ans2()[2], resolution_ans2()[2]))
    print("Query: W \n-Ans with model checking: {} \n "
          "-Ans with resolution: {} \n".format(model_checking_ans2()[3], resolution_ans2()[3]))
