% Facts: Student, Teacher, and Subject Code
student(john, math101).
student(emma, bio201).
student(lisa, chem301).
student(michael, phys401).

teacher(prof_smith, math101).
teacher(prof_davis, bio201).
teacher(prof_jones, chem301).
teacher(prof_wilson, phys401).

% Query to find the teacher for a given student and subject code
get_teacher(Student, SubjectCode, Teacher) :-
    student(Student, SubjectCode),
    teacher(Teacher, SubjectCode).

% Example usage:
% ?- get_teacher(john, math101, Teacher).
% Teacher = prof_smith.
