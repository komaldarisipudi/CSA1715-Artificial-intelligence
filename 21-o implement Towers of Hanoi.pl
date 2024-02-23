% hanoi(+N, +A, +B, +C, -Moves)
% Solves the Towers of Hanoi problem for N disks, with pegs A, B, and C.
% Moves represents the list of moves required to solve the problem.
hanoi(1, A, _, C, [(A, C)]) :- !.
hanoi(N, A, B, C, Moves) :-
    N > 1,
    N1 is N - 1,
    hanoi(N1, A, C, B, Moves1),
    hanoi(1, A, _, C, Moves2),
    hanoi(N1, B, A, C, Moves3),
    append([Moves1, Moves2, Moves3], Moves).

% Example usage:
% ?- hanoi(3, left, middle, right, Moves).
% Moves = [(left, right), (left, middle), (right, middle), (left, right), (middle, left), (middle, right), (left, right)] ;
% false.
