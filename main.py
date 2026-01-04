text = input("Matn kiriting: ")

print("Harflar soni:", len(text.replace(" ", "")))

print("Unli harflar:",
      sum(1 for c in text if c.lower() in "aeiou"))

clean = text.replace(" ", "").lower()
print("Palindrommi:", clean == clean[::-1])
