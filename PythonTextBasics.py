# Text Formatting basics using f string literal.
from datetime import datetime
library = [('Author', 'Topic', 'Pages'), ('Twain', 'Rafting', 601),
           ('Feynman', 'Physics', 95), ('Hamilton', 'Mythology', 144)]

for author, topic, pages in library:  # tuple unpacking
    # text formatting for output; output padding.
    print(f"{author:{10}} {topic:{30}} {pages:>{10}}")

today = datetime(year=2021, month=8, day=24)
print(f"{today:%B %d, %Y}")
