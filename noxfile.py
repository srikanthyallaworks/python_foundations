import nox

locations = ['src']

@nox.session()
def tests(session):
    session.run("poetry", "install", external=True)
    session.run("pytest", "--cov")


@nox.session()
def lint(session):
    args = session.posargs or locations
    session.install("flake8")
    session.run("flake8", *args)

@nox.session()
def black(session):
    args = session.posargs or locations
    session.install("black")
    session.run("black", *args)