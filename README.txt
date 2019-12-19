Project 2: Automated Reasoning

----------------------
Run in Pycharm
----------------------

-set configuration to 'modus_ponens.py', 'wumpus_world.py', 'horn_clauses.py' and 'doors_of_enlightment.py'

-The results will be displayed in console.

----------------------
Commend Line Arguments
----------------------

-The executable files are 'modus_ponens.py', 'wumpus_world.py', 'horn_clauses.py' and 'doors_of_enlightment.py'

-for LINUX (use modus_ponens.py as an example)
(1)rename file: mv modus_ponens.py modus_ponens
(2)make it executable: chmod +x modus_ponens
(3)execute: 
./modus_ponens

-for Windows
execute:
python modus_ponens.py


-----------------
Introductory Info
-----------------
The src directory has a README.txt and 6 python files.

(1) model_checking.py
contains methods for model checking

Formula class:Basic formula class represents a literal; tree node of a formula tree
# Super class of conjunction, disjunction, implication and biconditional
is_pl_true():Check whether a propositional logic sentence is true according to a given model and return the result
is_tt_entails():Check whether kb entails alpha according to a truth table
tt_check_all()：Check whether alpha is true under all models of kb
is_maybe(): Check whether there is no intersection between models of kb and models of alpha
tt_check_all_false():Check whether alpha is false under all models of kb
print_ans(): get results

(2) resolution.py
contains methods for resolution algorithms

change_to_string(), change_to_compare(), change_to_formula(), str_to_bool() are methods to make sets of objects comparable and operationable when checking resolvents with clauses in the set and inputing sentences as a Formula object.
pl_resolution(): method to implement resolution algorithm
pl_resolve(): using inside pl_resolution to get resolvents

(3) modus_ponens.py
get the results of model checking and resolution for modus ponens test

(4) wumpus_world.py
get the results of model checking and resolution for wumpus world test

(5) horn_clauses.py
get the results of model checking and resolution for horn clauses test

(6) doors_of_enlightment.py
get the results of model checking and resolution for doors of enlightenment test

-----------
Author Info
-----------
Name: Jiapeng Li (jli161)
Name: Zeyi Pan (zpan12)