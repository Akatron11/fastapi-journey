- Why did you choose each Pydantic field type?
ID (int)==> Student numbers must be integers because each student must have a unique numerical identity.
Enrollments (List[Enrollment])==> I created a list structure because a student can take more than one course.

- What does each validation rule protect against?
gt=0 (ID)==> Student number cannot be zero or negative.
min_length=3 (Course Name)==> Course names must have at least 3 letters.
ge=18 (Age)==>I made it mandatory for students to be 18 years of age or older. This way, the age limit will be automatically checked during data entry.

- Which endpoint uses `async` in a meaningful way, and why?
I added await asyncio.sleep(1) to the /students/{student_id} part of the project.
Reason: There is actually a waiting period when connecting to the database. By using async, I ensured that the server doesn't freeze during this waiting period and can continue responding to other processes. This is important for the application to run faster and more efficiently.