#name = "Marius"
#print(f"Hello, {name}!!!")
#print("Hello, world!!!")
#question = input("Cum te cheama? ")
#print(f"Salut, {question}.")
server = "spribe"
ERROR_THRESHOLD = 5
total_requests = int(input("Introduceti numarul total de cereri: "))
failed_requests = int(input("Introduceti numarul de cereri esuate: "))
if total_requests == 0:
    print("Numarul total de cereri nu poate fi zero.")
else:
    error_rate = (failed_requests / total_requests) * 100
    print(f"Serverul {server} are {error_rate:.4f}% erori.")
    if error_rate > ERROR_THRESHOLD:
        print("ALERTA")
    else:
        print("OK")
# test git
#test 2