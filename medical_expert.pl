

:- dynamic yes/1, no/1.

#Main control

go :-
    write('What is the patient''s name? '),
    read(Patient),
    hypothesis(Patient, Disease),
    nl,
    write(Patient), write(' probably has '), write(Disease), write('.'), nl,
    undo, !.

go :-
    nl,
    write('Sorry, I am unable to diagnose the disease.'), nl,
    undo.

# Symptom Rules 

symptom(Patient, fever) :-
    verify(Patient, fever).

symptom(Patient, rash) :-
    verify(Patient, rash).

symptom(Patient, headache) :-
    verify(Patient, headache).

symptom(Patient, runny_nose) :-
    verify(Patient, runny_nose).

symptom(Patient, conjunctivitis) :-
    verify(Patient, conjunctivitis).

symptom(Patient, cough) :-
    verify(Patient, cough).

symptom(Patient, body_ache) :-
    verify(Patient, body_ache).

symptom(Patient, chills) :-
    verify(Patient, chills).

symptom(Patient, sore_throat) :-
    verify(Patient, sore_throat).

symptom(Patient, sneezing) :-
    verify(Patient, sneezing).

symptom(Patient, swollen_glands) :-
    verify(Patient, swollen_glands).
#Question Handling

ask(Patient, Symptom) :-
    format('~w, do you have ~w? (y/n): ', [Patient, Symptom]),
    read(Response),
    ( Response == y ; Response == yes ),
    assert(yes(Symptom)).

ask(Patient, Symptom) :-
    assert(no(Symptom)),
    fail.

verify(_, Symptom) :-
    yes(Symptom), !.

verify(_, Symptom) :-
    no(Symptom), !, fail.

verify(Patient, Symptom) :-
    ask(Patient, Symptom).

# Disease Rules 

hypothesis(Patient, german_measles) :-
    symptom(Patient, fever),
    symptom(Patient, headache),
    symptom(Patient, runny_nose),
    symptom(Patient, rash).

hypothesis(Patient, common_cold) :-
    symptom(Patient, headache),
    symptom(Patient, sneezing),
    symptom(Patient, sore_throat),
    symptom(Patient, runny_nose),
    symptom(Patient, chills).

hypothesis(Patient, measles) :-
    symptom(Patient, cough),
    symptom(Patient, sneezing),
    symptom(Patient, runny_nose).

hypothesis(Patient, flu) :-
    symptom(Patient, fever),
    symptom(Patient, headache),
    symptom(Patient, body_ache),
    symptom(Patient, conjunctivitis),
    symptom(Patient, chills),
    symptom(Patient, sore_throat),
    symptom(Patient, runny_nose),
    symptom(Patient, cough).

hypothesis(Patient, mumps) :-
    symptom(Patient, fever),
    symptom(Patient, swollen_glands).

hypothesis(Patient, chicken_pox) :-
    symptom(Patient, fever),
    symptom(Patient, chills),
    symptom(Patient, body_ache),
    symptom(Patient, rash).

# clean Up

undo :-
    retract(yes(_)), fail.
undo :-
    retract(no(_)), fail.
undo.
