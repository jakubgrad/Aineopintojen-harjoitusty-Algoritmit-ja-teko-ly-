import os 
from invoke import task
from subprocess import call
from sys import platform

root_dir_raw = os.path.dirname(os.path.abspath(__file__))
root_dir = "'"+root_dir_raw+"'"

@task
def start(ctx):
    ctx.run(f"python3 {root_dir}/src/main.py ", pty=True)

@task
def test(ctx):
    ctx.run(f"cd {root_dir} && pytest {root_dir}/src", pty=True)

@task
def coverage(ctx):
    ctx.run(f"cd {root_dir} && coverage run --branch -m pytest src", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run(f"cd {root_dir} && coverage html", pty=True)
    if platform != "win32":
        call(("xdg-open", f"{root_dir_raw}/htmlcov/index.html"))

@task
def lint(ctx):
    ctx.run(f"cd {root_dir} && pylint src", pty=True)

@task
def format(ctx):
    ctx.run(f"cd {root_dir} && autopep8 --in-place --recursive src", pty=True)

