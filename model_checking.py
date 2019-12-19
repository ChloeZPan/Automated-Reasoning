#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy


# Basic formula class represents a literal; tree node of a formula tree
# Super class of conjunction, disjunction, implication and biconditional
class Formula:
    def __init__(self, sym, neg=False, lc=None, rc=None, val=None):
        self.symbol = sym  # proposition symbol
        # token indicates whether it is a negation of an atomic formula
        # negation is True --> not (sym)
        self.negation = neg
        self.left_child = lc
        self.right_child = rc
        self.truth = val  # truth value

    # Return True if it is a leaf node in a tree
    def is_leaf(self):
        return (self.left_child is None) and (self.right_child is None)

    # Populate a list with symbols(str) stored in the leaf nodes of a tree
    def get_leaf_symbols(self, sym_list):
        if self.is_leaf():
            sym_list.append(self.symbol)
        else:
            self.left_child.get_leaf_symbols(sym_list)
            self.right_child.get_leaf_symbols(sym_list)

    # Assign truth value to each literal according to a given model
    def assign(self, model):
        if self.is_leaf():
            self.truth = model[self.symbol]
        else:
            self.left_child.assign(model)
            self.right_child.assign(model)

    # check whether a literal is true and return the result
    def models(self):
        if self.negation is True:
            return not self.truth
        else:
            return self.truth


class Conjunction(Formula):
    def __init__(self, neg=False, lc=None, rc=None, val=None):
        Formula.__init__(self, "^", neg, lc, rc, val)  # neg is True --> not (lc ^ rc)

    # check whether a conjunction is true and return the result
    def models(self):
        if self.negation is True:
            self.truth = not (self.left_child.models() and self.right_child.models())
            return self.truth
        else:
            self.truth = self.left_child.models() and self.right_child.models()
            return self.truth


class Disjunction(Formula):
    def __init__(self, neg=False, lc=None, rc=None, val=None):
        Formula.__init__(self, "V", neg, lc, rc, val)  # neg is True --> not (lc V rc)

    # check whether a disjunction is true and return the result
    def models(self):
        if self.negation is True:
            self.truth = not (self.left_child.models() or self.right_child.models())
            return self.truth
        else:
            self.truth = self.left_child.models() or self.right_child.models()
            return self.truth


class Implication(Formula):
    def __init__(self, neg=False, lc=None, rc=None, val=None):
        Formula.__init__(self, "=>", neg, lc, rc, val)  # neg is True --> not (lc => rc)

    # check whether an implication is true and return the result
    def models(self):
        if self.negation is True:
            self.truth = self.left_child.models() and (not self.right_child.models())
            return self.truth
        else:
            self.truth = (not self.left_child.models()) or self.right_child.models()
            return self.truth


class Biconditional(Formula):
    def __init__(self, neg=False, lc=None, rc=None, val=None):
        Formula.__init__(self, "<=>", neg, lc, rc, val)  # neg is True --> not (lc <=> rc)

    # check whether a biconditional is true and return the result
    def models(self):
        if (self.left_child.models() is True and self.right_child.models() is True) \
                or (self.left_child.models() is False and self.right_child.models() is False):
            if self.negation is True:
                self.truth = False
                return self.truth
            else:
                self.truth = True
                return self.truth
        else:
            if self.negation is True:
                self.truth = True
                return self.truth
            else:
                self.truth = False
                return self.truth


# Check whether a propositional logic sentence is true according to a given model and return the result
def is_pl_true(wff, model):
    wff.assign(model)
    return wff.models()


# Check whether kb entails alpha according to a truth table
# using a truth-table enumeration algorithm
def is_tt_entails(kb, alpha):
    symbol_list = []  # a list of proposition symbols in kb and alpha (duplicates allowed)
    model = {}
    kb.get_leaf_symbols(symbol_list)
    alpha.get_leaf_symbols(symbol_list)
    symbol_set = set(symbol_list)  # a set of proposition symbols in kb and alpha (remove duplicates)
    return tt_check_all(kb, alpha, symbol_set, model)


# Check whether alpha is true under all models of kb
def tt_check_all(kb, alpha, symbol_set, model):
    if len(symbol_set) == 0:
        if is_pl_true(kb, model) is True:
            return is_pl_true(alpha, model)
        else:
            return True
    else:
        symbol_set_copy = copy.deepcopy(symbol_set)  # deep copy symbol_set to protect original symbol_set
        symbol_p = symbol_set_copy.pop()
        rest = copy.deepcopy(symbol_set_copy)
        model_copy_1 = copy.deepcopy(model)
        model_copy_2 = copy.deepcopy(model)
        model_copy_1[symbol_p] = True  # model AND {P = True}
        model_copy_2[symbol_p] = False  # model AND {P = False}
        return tt_check_all(kb, alpha, rest, model_copy_1) and tt_check_all(kb, alpha, rest, model_copy_2)


# Check whether there is no intersection between models of kb and models of alpha
# Return False if there is no intersection between models of kb and models of alpha
def is_maybe(kb, alpha):
    symbol_list = []  # a list of proposition symbols in kb and alpha (duplicates allowed)
    model = {}
    kb.get_leaf_symbols(symbol_list)
    alpha.get_leaf_symbols(symbol_list)
    symbol_set = set(symbol_list)  # a set of proposition symbols in kb and alpha (remove duplicates)
    return tt_check_all_false(kb, alpha, symbol_set, model)


# Check whether alpha is false under all models of kb
def tt_check_all_false(kb, alpha, symbol_set, model):
    if len(symbol_set) == 0:
        if is_pl_true(kb, model) is True:
            return is_pl_true(alpha, model)
        else:
            return False  # return false to ignore models that contradict the knowledge base
    else:
        symbol_set_copy = copy.deepcopy(symbol_set)  # deep copy symbol_set to protect original symbol_set
        symbol_p = symbol_set_copy.pop()
        rest = copy.deepcopy(symbol_set_copy)
        model_copy_1 = copy.deepcopy(model)
        model_copy_2 = copy.deepcopy(model)
        model_copy_1[symbol_p] = True  # model AND {P = True}
        model_copy_2[symbol_p] = False  # model AND {P = False}
        return tt_check_all_false(kb, alpha, rest, model_copy_1) or tt_check_all_false(kb, alpha, rest, model_copy_2)


def print_ans(kb, alpha):
    # kb entails alpha
    if is_tt_entails(kb, alpha) is True:
        return True
    # alpha is always false when kb is true
    elif is_maybe(kb, alpha) is False:
        return False
    # alpha may be true when kb is true
    else:
        return 'MAYBE'
