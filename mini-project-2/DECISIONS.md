1. Why does `DATABASE_URL` use `mongo` as the hostname instead of `localhost`? What would happen if you kept `localhost`?
we access the database via the service name using a docker network

2. What does `depends_on` in `docker-compose.yml` do? Does it guarantee MongoDB is fully ready before FastAPI starts — and if not, what would?
this ensures the API starts after mongodb and mongodb also needs to be ready

3. What is the purpose of the volume in the `mongo` service? What happens to your data if you remove it and run `docker compose down`?
this ensures that the data remains on the computer even if the container is deleted

4. Why do we copy `requirements.txt` and run `pip install` before copying the rest of the app code in the Dockerfile?
even if the code changes the pip install command doesnt need to be repeated as long as the library remains the same,this speeds up the process