print("Kalkulator\n")

num_a = int(input("Masukan Nomor : "))
op = input("Masukan Operator (*, /, -, +) = ")
num_b = int(input("Masukan Nomor : "))


if op == "*":
  print("Hasil dari {} * {} adalah". format(num_a, num_b))
  print(num_a * num_b)

elif op == "-":
  print("Hasil dari {} - {} adalah". format(num_a, num_b))
  print(num_a - num_b)
  
elif op == "+":
  print("Hasil dari {} + {} adalah". format(num_a, num_b))
  print(num_a + num_b)
  
elif op == "/":
  print("Hasil dari {} / {} adalah". format(num_a, num_b))
  print(num_a / num_b)
  
else:
  print("Data tidak valid")
