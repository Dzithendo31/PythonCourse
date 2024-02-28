## Pushback
- if you want to match the letter "b" only if it is preceded by the letter "a", you can use the lookbehind assertion
- So you can match a pattern only if is preceded(behind) by another pattern.

  ```python
text = "apple banana orange"
pattern = r'(?<=banana\s)\w+'
# Using re.findall() to find all matches
matches = re.findall(pattern, text)
print(matches)  # Output: ['orange']
