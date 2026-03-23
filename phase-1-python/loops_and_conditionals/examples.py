for skill in skills:
    print(skill)
for i, skill in enumerate(skills,1):
    print(f"{i}. {skill}")

for name, score in zip(names, scores):
    print(f"{name}: {score}")

while True:
    choice = input("Opcion")
    if choice == "0": break
    
for s in students:
    if s["name"] == target:break
else:
    print("No encontrado")

status = "PASS" if avg >= 6 else "FAIL"

HTTP = {
    200:"OK",
    404:"Not Found",
    500:"Internal Server Error"
}

code = 200
print(HTTP.get(code,"Unknown"))


def process(user):
    if user is None:
        if not user["active"]:
            return do_work(user)