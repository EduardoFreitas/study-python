# Create a list of strings: mutants
mutants = ['charles xavier',
           'bobby drake',
           'kurt wagner',
           'max eisenhardt',
           'kitty pride']

# Create a list of tuples: mutant_list
mutant_list = list(enumerate(mutants))

# Print the list of tuples
print(mutant_list)

# Unpack and print the tuple pairs
for index1, value1 in enumerate(mutant_list):
    print(index1, value1)

# Change the start index
for index2, value2 in enumerate(mutant_list, start=1):
    print(index2, value2)

# ----------------------------------------------

mutants = ('charles xavier',
           'bobby drake',
           'kurt wagner',
           'max eisenhardt',
           'kitty pride')

powers = ('telepathy',
          'thermokinesis',
          'teleportation',
          'magnetokinesis',
          'intangibility')

# Create a zip object from mutants and powers: z1
z1 = zip(mutants, powers)

# Print the tuples in z1 by unpacking with *
print(*z1)

# Re-create a zip object from mutants and powers: z1
z1 = zip(mutants, powers)

# 'Unzip' the tuples in z1 by unpacking with * and zip(): result1, result2
result1, result2 = zip(*z1)

# Check if unpacked tuples are equivalent to original tuples
print(result1 == mutants)
print(result2 == powers)
