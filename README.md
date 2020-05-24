# Django DevOps
---
Objectives:
- Test out django project production setup locally

Development containerized Django web-app with 
- Postgres.

Production containerized Django web-app with 
- Postgres, 
- Gunicorn,
- > Production-grade WSGI HTTP (application) server.
- Nginx
- > As a reverse proxy for Gunicorn to handle client requests as well as serving up static files.
 
For actual deployment to a production environment e.g. AWS,
 - Use fully managed database service -- like RDS (rather than managing an Postgres instance within a container).
 - Use Non-root user for the db and nginx services.
