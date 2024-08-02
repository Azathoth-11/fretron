def distribute_apples(apples, payments):
    total_weight = sum(apples)
    target_weights = [int((i/100)*total_weight) for i in payments]
    allocated = [[] for _ in payments]
    current_weights = [0] * len(payments)
    
    apples.sort(reverse=True)
    
    for apple in apples:
        for i in range(len(payments)):
            if current_weights[i] + apple <= target_weights[i]:
                allocated[i].append(apple)
                current_weights[i] += apple
                break
                
    return allocated

def run_distribute_apple():
    apples = []
    while True:
        weight = int(input("Enter apple weight in gram (-1 to stop) : "))
        if weight == -1:
            break
        apples.append(weight)

    payments = [50, 30, 20]
    names = ["Ram", "Sham", "Rahim"]

    result = distribute_apples(apples, payments)

    print("Distribution Result :")
    for name, person_apples in zip(names, result):
        print(f"{name} : {' '.join(map(str, person_apples))}")
run_distribute_apple()
## Google Logs contained some syntax helps for the code like searching for a zip function and join function.
