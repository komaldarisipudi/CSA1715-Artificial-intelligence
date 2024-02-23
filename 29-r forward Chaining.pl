% Define some example rules
rule(has_fever, patient).
rule(has_cough, patient).
rule(has_runny_nose, patient).

rule(has_flu, patient) :-
    has_fever,
    has_cough.

rule(has_cold, patient) :-
    has_runny_nose,
    has_cough.

% Forward chaining inference
infer(Patient, Disease) :-
    rule(Disease, Patient),
    check_rule(Patient, Disease).

check_rule(Patient, Disease) :-
    rule(Disease, Patient),
    \+ fact(Disease, Patient), % Check if the conclusion is not already known
    \+ (rule(Premise, Patient), \+ fact(Premise, Patient)), % Check if all premises are known
    assertz(fact(Disease, Patient)), % Assert the conclusion as a fact
    write('Inferred '), write(Disease), write(' for '), write(Patient), nl,
    fail. % Fail to backtrack and find more inferences

% Facts database (initialize with known facts)
% For example, patient john has fever and cough
fact(has_fever, john).
fact(has_cough, john).

% Example query:
% infer(john, Disease).
