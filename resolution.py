#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Zeyi Pan'

import copy


class Formula:
    def __init__(self, sym, neg=False, lc=None, rc=None, val=None):
        self.symbol = sym  # proposition symbol
        # token indicates whether it is a negation of an atomic formula
        # negation is True --> not (sym)
        self.negation = neg
        self.left_child = lc
        self.right_child = rc
        self.truth = val  # truth value

    def __str__(self):
        return '{},{}'.format(self.symbol, self.negation)

    def __hash__(self):
        return hash(self.__dict__)

    def __eq__(self, other):
        try:
            return self.__dict__ == other.__dict__
        except AttributeError:
            return NotImplemented

    # Return True if it is a leaf node in a tree
    def is_leaf(self):
        return (self.left_child is None) and (self.right_child is None)


def str_to_bool(s):
    if s == 'True':
        return True
    elif s == 'False':
        return False
    else:
        raise ValueError


def change_to_string(formula):
    return '{}_{}'.format(formula.symbol, formula.negation)


def change_to_compare(list):
    for i in range(len(list)):
        for j in range(len(list[i])):
            list[i][j] = change_to_string(list[i][j])
        list[i] = tuple(set(list[i]))
    return list


def change_to_formula(l):
    for i in range(len(l)):
        l[i] = list(l[i])
        for j in range(len(l[i])):
            if isinstance(l[i][j], Formula):
                return l
            if isinstance(l[i][j], str):
                t = l[i][j].split('_')
                f = Formula(t[0], neg=str_to_bool(t[1]))
                l[i][j] = f
            else:
                return l
    return l


def pl_resolve(ci, cj):
    """Return all clauses that can be obtained by resolving clauses ci and cj.
    ci, cj are list [formula('p'), formula('Q')]"""
    clauses = []

    for i in range(len(ci)):
        for j in range(len(cj)):
            if ci[i].symbol == cj[j].symbol and ci[i].negation != cj[j].negation:
                temp_ci = copy.deepcopy(ci)
                temp_cj = copy.deepcopy(cj)
                temp_ci.remove(temp_ci[i])
                temp_cj.remove(temp_cj[j])
                # if (len(temp_ci) == 1 and len(temp_cj) == 1) and (temp_ci[0].symbol == temp_cj[0].symbol) \
                #         and temp_ci[0].negation != temp_cj[0].negation:
                #     clauses.append([])
                #     print(temp_cj[0], temp_ci[0])
                clauses.append(temp_ci + temp_cj)
    return clauses


def pl_resolution(kb, alpha):
    """Propositional-logic resolution: say if alpha follows from KB. [Figure 7.12]
    pl_resolution(kb, A)
    True
    """

    def pl_res(kb, alpha):
        q_list = [alpha]
        clauses = [*kb, q_list]
        new = []
        while True:
            n = len(clauses)
            pairs = [(clauses[i], clauses[j])
                     for i in range(n) for j in range(i + 1, n)]
            for (ci, cj) in pairs:
                resolvents = pl_resolve(ci, cj)
                if [] in resolvents:
                    return True
                new.extend(resolvents)
            new = change_to_compare(new)
            clauses = change_to_compare(clauses)
            if set(new).issubset(set(clauses)):
                kb = change_to_formula(kb)
                q_list = change_to_formula([q_list])
                return False
            for c in set(new):
                if c not in set(clauses):
                    clauses.append(c)
            clauses = change_to_formula(clauses)
            new = change_to_formula(new)
            kb = change_to_formula(kb)
            [q_list] = change_to_formula([q_list])
    beta = copy.deepcopy(alpha)
    beta.negation = False
    if pl_res(kb, alpha) is False and pl_res(kb, beta) is False:
        return 'MAYBE'
    elif pl_res(kb, alpha) is True:
        return True
    else:
        return False
