# Regular Expressions
# Digits have the placeholder pattern code of /d ; Example Match=> file_25 ;patterncode => file_\d\d
# Alphanumerical => \w ; Example Match => A-b_1 ; patterncode => A-b_1
# WhiteSpace => \s ; Example Match => a b c ;pattercode => a\sb\sc
# Non Digit => \D Example Match => ABC ; patterncode => ABV
# Non Alphanumerical => \W; Example Match => *-+=) ; patterncode => \W\W\W\W\W
# NonWhiteSpace => /S Example Match => Yoyo ; patterncode => \S\S\S\S
# re is standard python library for working with regular expressions.
import re
text = "The phone number of the agent is 408-555-1234. Call soon!"
check_phone = "phone" in text
pattern = "phone"
my_match = re.search(pattern, text)
# returns the actual span of the pattern in specified text.
print(my_match.span())

all_matches = re.findall("phone", text)  # finds all the matches

# finditer allows us to iterate through the matches.
for match in re.finditer("phone", text):
    print(match)
