try:
    result = input(user_input)
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Error: {e}")
else:
    print("Todo bien")
finally:
    print("Fin del programa")


class AppError(Exception): pass

class StudentNotFoundError(AppError):
    def __init__(self,name:str):
        super().__init__(f"Estudiante {name} no encontrado")
        self.name = name

raise StudentNotFoundError("Daniel")

with open("data.json", encoding="utf-8") as f:
    try:
        data = json.load(f)
    except ValueError as e:
        raise InvalidGradeError("") from e
    
        