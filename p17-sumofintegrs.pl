% Base case: The sum of the first 1 integer is 1.
sumto(1, 1).

% Recursive case: The sum of the first N integers is the sum of the first N-1 integers, plus N.
sumto(N, M) :-
    N > 1,
    N1 is N - 1,
    sumto(N1, M1),
    M is M1 + N.

% Example usage:
% ?- sumto(100, N).
% N = 5050
% ?- sumto(1, 1).
