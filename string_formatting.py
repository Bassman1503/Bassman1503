# Formatting a string using positional notation
# with curly braces. "{}" represents a placeholder
# to which input string to "format()" function
# will be feed.
#
print("{} is a beautiful {}".format("Python", "language"))


# Formatting a string using positional notation with curly
# braces and indexes. Each index refers to the correspondent
# argument feed to "format()" function.
#
print("{0} is better than other {1}, maybe better than the same {0}".format("Python", "Languages"))


# Format a string using values bound to keywords
# feeded as input to the "format()" function.
#
print("{langName} is better than {otherLangs}".format(langName= "Python", otherLangs= "other languages"))


# Formatted string literals notation.
#
langName= "Python"
otherLangs= "other languages"
print(f"{langName} is better than {otherLangs}, MAYBE")