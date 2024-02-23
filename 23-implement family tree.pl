% Facts about relationships
parent(john, peter).
parent(mary, peter).
parent(john, anne).
parent(mary, anne).
parent(peter, jenny).
parent(jenny, tom).

% Rules to define other relationships
father(Father, Child) :-
    parent(Father, Child),
    male(Father).

mother(Mother, Child) :-
    parent(Mother, Child),
    female(Mother).

grandparent(Grandparent, Grandchild) :-
    parent(Grandparent, Parent),
    parent(Parent, Grandchild).

ancestor(Ancestor, Descendant) :-
    parent(Ancestor, Descendant).

ancestor(Ancestor, Descendant) :-
    parent(Ancestor, Parent),
    ancestor(Parent, Descendant).

% Facts about genders
male(john).
male(peter).
male(tom).

female(mary).
female(anne).
female(jenny).

% Example queries
% ?- father(john, anne).
% ?- mother(mary, peter).
% ?- grandparent(john, tom).
% ?- ancestor(mary, tom).
