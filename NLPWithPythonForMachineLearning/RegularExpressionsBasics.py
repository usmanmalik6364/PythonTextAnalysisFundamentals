# Regex are Text string for describing a search pattern.
import re
re_test = "This is a made up string to test 2 different regex methods"
re_test_messy = "This    is a made up      string to test 2 different regex methods"
re_test_messy1 = "This-is-a-made/up.string*to>>>test----2'''''different~regex~methods"

re.split('\s', re_test)
# + sign will tell python to look for one or more white spaces
re.split('\s+', re_test_messy)
# W+ will search for any nonword character and it will use that to perform the split.
result = re.split('\W+', re_test_messy1)

print(result)

# S will look one or more non white space character.
result = re.findall('\S+', re_test)
# w+ will look for all actual words and ignore all the special character and white spaces
result = re.findall('\w+', re_test_messy1)
print(result)

pep8_test = 'I try to follow PEP8 guidelines'
pep7_test = 'I try to follow PEP7 guidelines'
pep_8_test = 'I try to follow PEEP8 guidelines'

# Regex for capturing the PEP8, PEEEP8, PEP7 etc
result = re.findall('[A-Z]+[0-9]+', pep8_test)
print(result)

# Finds the matching pattern, and , replaces it.
# Takes three parameters, first is regex,
# second the text which we want to replace the matching regex with,
# third is the actual string on which we want to perform the test on
result = re.sub('[A-Z]+[0-9]+', 'PEP8 Python Styleguide', pep8_test)
print(result)
