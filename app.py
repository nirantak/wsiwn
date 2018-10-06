from pyswip import Prolog

prolog = Prolog()

prolog.assertz("father(michael,john)")
prolog.assertz("father(michael,gina)")

for soln in prolog.query("father(X,Y)"):
    print(soln["X"].title(), "is the father of", soln["Y"].title())
