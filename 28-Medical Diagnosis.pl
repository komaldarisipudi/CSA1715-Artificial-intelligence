% Symptoms database
symptom(fever, cold).
symptom(cough, cold).
symptom(runny_nose, cold).
symptom(sore_throat, cold).
symptom(headache, flu).
symptom(fever, flu).
symptom(body_aches, flu).
symptom(fatigue, flu).
symptom(rash, measles).
symptom(fever, measles).
symptom(cough, measles).
symptom(conjunctivitis, measles).

% Rules for diagnosis
diagnosis(Patient, Disease) :-
    symptom(Symptom, Disease),
    has_symptom(Patient, Symptom).

% Predicates to check if patient has symptoms
has_symptom(Patient, Symptom) :-
    ask_patient(Patient, Symptom).

ask_patient(Patient, Symptom) :-
    format('Does ~w have ~w? (yes/no): ', [Patient, Symptom]),
    read(Response),
    Response = yes.

% Predicates to suggest treatment based on diagnosis
treatment(cold) :-
    write('Treatment for cold: Rest, fluids, and over-the-counter cold medications.'),
    nl.
treatment(flu) :-
    write('Treatment for flu: Rest, fluids, and antiviral medications prescribed by a doctor.'),
    nl.
treatment(measles) :-
    write('Treatment for measles: Rest, fluids, and over-the-counter fever reducers. Vaccination can prevent measles.'),
    nl.

% Example query:
% ?- diagnosis(john, Disease).
