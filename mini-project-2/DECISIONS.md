**Part A**
1. What is an ODM and why do we use Beanie instead of writing raw MongoDB queries?
ODM is like a translator between python and mongodb. mongodb stores stuff in json-ish docs, but we want to work with python classes. beanie makes the code way cleaner and easier to read since we just use python objects instead of messy dictionaries.

2. What is the role of the `Database` class — why wrap Beanie methods inside it instead of calling them directly in routes?
if we put database logic directly in our routes, the code becomes a giant mess. it's just better organization.

3. What happens if `initialize_database()` is not called on startup? What would break and why?
if this doesn't run when the app starts, the app basically doesn't know the database exists.

4. What is the difference between the `Event` document and the `EventUpdate` model, and why are they two separate classes?


**Part B**
1. Why does `DATABASE_URL` use `mongo` as the hostname instead of `localhost`? What would happen if you kept `localhost`?
we access the database via the service name using a docker network

2. What does `depends_on` in `docker-compose.yml` do? Does it guarantee MongoDB is fully ready before FastAPI starts — and if not, what would?
this ensures the API starts after mongodb and mongodb also needs to be ready

3. What is the purpose of the volume in the `mongo` service? What happens to your data if you remove it and run `docker compose down`?
this ensures that the data remains on the computer even if the container is deleted

4. Why do we copy `requirements.txt` and run `pip install` before copying the rest of the app code in the Dockerfile?
even if the code changes the pip install command doesnt need to be repeated as long as the library remains the same,this speeds up the process