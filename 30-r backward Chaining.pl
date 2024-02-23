% Define some example rules
rule(patient_has_disease, Patient) :-
    has_symptom(Patient, fever),
    has_symptom(Patient, cough).

rule(patient_has_disease, Patient) :-
    has_symptom(Patient, runny_nose),
    has_symptom(Patient, cough).

% Predicates to check if patient has symptoms
has_symptom(john, fever).
has_symptom(john, cough).

has_symptom(sarah, runny_nose).
has_symptom(sarah, cough).

% Backward chaining inference
infer_disease(Patient, Disease) :-
    rule(patient_has_disease, Patient),
    check_rule(Patient, Disease).

check_rule(Patient, Disease) :-
    rule(patient_has_disease, Patient),
    \+ fact(patient_has_disease, Patient, Disease), % Check if the conclusion is not already known
    \+ (rule(_, Patient), \+ infer_symptoms(Patient, _)), % Check if any premise can't be inferred
    assertz(fact(patient_has_disease, Patient, Disease)), % Assert the conclusion as a fact
    write('Inferred '), write(Disease), write(' for '), write(Patient), nl,
    fail. % Fail to backtrack and find more inferences

% Predicates to infer symptoms based on patient's observations
infer_symptoms(Patient, Symptom) :-
    has_symptom(Patient, Symptom).

% Facts database (initially empty but populated during inference)
fact(patient_has_disease, _, _) :- false.

% Example query:
% infer_disease(john, Disease).
