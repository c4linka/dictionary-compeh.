names = {"Ewa", "Ala", "Ola", "Ania", "Ela"}
numbers = [1, 2, 3, 4, 5, 6]
celcius = {"t1": -20, "t2": -15, "t3": 0, "t4": 12, "t5": 24}


namesLenght = {
               name : len(name)
               for name in names
                }

print(namesLenght)


namesAtA = {
            name : len(name)
            for name in names
            if name.startswith("A")
            }
print(namesAtA)


exponentiation4 = {  #each number raised to 4th power
                  number : number**4
                  for number in numbers
                  }
print("Each number raised to the 4th power", exponentiation4)

multiplyedNumbers = {  #each number multiplied by itself
                  number : number*number
                  for number in numbers
                 }
print("Each number multiplied by itself:", multiplyedNumbers)


multiplyedEvenNumbers = {  #each number multiplied by itself
                  number : number*number
                  for number in range(1,101)
                  if number %2 == 0
                  }
print("Each even number between 1 and 100 multiplied by itself:",multiplyedEvenNumbers)


fahrenheit = {
              key : celcius * 1.8 +32
              for key, celcius in celcius.items()
              if celcius > 0
              if celcius < 24
              }
print(fahrenheit)

