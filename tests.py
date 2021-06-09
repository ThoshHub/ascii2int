import coverage
from ascii2int import ascii2int

cov = coverage.Coverage()
cov.start()

ascii2int("one hundred")
ascii2int("four hundred")
ascii2int("five hundred and twenty one")
ascii2int("two")
ascii2int("forty")
ascii2int("five hundred and twelve")
ascii2int("six hundred and one")
ascii2int("four hundred forty two")
ascii2int("four thousand four hundred and twelve")
ascii2int("four thousand four hundred and twenty one")
ascii2int("forty thousand four hundred and twenty one")
ascii2int("four hundred and twenty thousand four hundred and twenty one")
ascii2int("one million and forty")
ascii2int("six hundred million and two hundred thousand and forty two")
ascii2int("ten billion forty thousand four hundred and twenty one")
ascii2int("ten million and forty")
ascii2int("ten billion and forty")
ascii2int("twenty nine billion four hundred thirty two million six hundred forty seven thousand nine hundred and twenty two")
ascii2int("nine hundred and ninety nine billion nine hundred and ninety nine million nine hundred and ninety nine thousand nine hundred and ninety nine")

cov.stop()
cov.html_report(directory='covhtml')