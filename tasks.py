from invoke import task
import os

@task
def run(cmd):
    # Start the Unicorn server
    cmd.run("uvicorn workout_api.main:app --reload")

@task
def create_migration(cmd, d):
    # Create Database migrations.
    pythonpath = os.getcwd()

    cmd.run(f"set PYTHONPATH={pythonpath} && alembic revision --autogenerate -m '{d}'")

@task
def run_migrations(cmd):
    # Run database migrations.
    pythonpath = os.getcwd()

    cmd.run(f"set PYTHONPATH={pythonpath} && alembic upgrade head")