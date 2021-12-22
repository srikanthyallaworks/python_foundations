import nox

@nox.session()
def tests(session):
    session.run("poetry", "install", external=True)
    session.run("pytest", "--cov")


@nox.session()
def lint(session):
    args = session.posargs or ['src']
    session.install("flake8")
    session.run("flake8", *args)
