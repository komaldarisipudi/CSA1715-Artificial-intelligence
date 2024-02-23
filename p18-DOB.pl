% Facts: Name and Date of Birth
dob(john, '1990-05-15').
dob(emma, '1985-09-20').
dob(lisa, '2000-03-10').
dob(michael, '1978-11-05').

% Query to find the date of birth for a given name
get_dob(Name, DateOfBirth) :-
    dob(Name, DateOfBirth).

% Example usage:
% ?- get_dob(john, DOB).
% DOB = '1990-05-15'.
