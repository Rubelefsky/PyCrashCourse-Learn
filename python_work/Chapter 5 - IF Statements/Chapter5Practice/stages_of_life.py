# 5-6. Stages of Life: Write an if-elif-else chain that determines a person’s stage of life.
age = 67

if age < 2:
    stage = 'baby'
elif age < 4:
    stage = 'toddler'
elif age < 13:
    stage = 'kid'
elif age < 20:
    stage = 'teenager'
elif age < 65:
    stage = 'adult'
else:
    stage = 'elder'


print(f"You are a {stage}.")