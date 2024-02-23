% Facts about birds and their flying abilities
bird(canary).
bird(sparrow).
bird(ostrich).

can_fly(canary).
can_fly(sparrow).
cannot_fly(ostrich).

% Rules to determine if a bird can fly
flies(Bird) :-
    can_fly(Bird),
    format('~w can fly.~n', [Bird]).

flies(Bird) :-
    bird(Bird),
    \+ can_fly(Bird),
    format('~w cannot fly.~n', [Bird]).

% Example queries
% ?- flies(canary).
% ?- flies(sparrow).
% ?- flies(ostrich).
