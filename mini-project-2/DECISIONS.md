1. What is an ODM and why do we use Beanie instead of writing raw MongoDB queries?
An ODM is like a translator. It lets us talk to MongoDB using Python objects instead of messy JSON-style code. We use Beanie because it’s super smart—it handles data validation automatically and works perfectly with FastAPI, saving us a lot of extra work.

2. What is the role of the `Database` class — why wrap Beanie methods inside it instead of calling them directly in routes?
Think of this as the "engine room." We put all our logic for adding, deleting, or finding data here. By keeping these tasks in one place, our main routes stay clean and short. It just makes the whole project much more organized.

3. What happens if `initialize_database()` is not called on startup? What would break and why?
The app won't be able to "talk" to the database. It’s like trying to make a phone call without a signal. The app might run, but the second you try to save or see any data, it will crash because the connection was never established.

4. What is the difference between the `Event` document and the `EventUpdate` model, and why are they two separate classes?
The Event document is the "master rulebook" for how data must look in the database. The EventUpdate model is a flexible version where everything is optional. We use it for updates so the user can change just one thing (like the time) without having to re-type all the other info.

