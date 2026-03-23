def create_student(name:str, grades:list[float]) -> dict:

    average = sum(grades) / len(grades) if grades else 0.0
    return {
        "name": name,
        "grades": grades,
        "average": round(average,2),
        "passed": average >= 6.0
    }

def get_top_students(students:list[dict], top_n:int = 3 ) -> list[dict]:

    return sorted(students, key=lambda s: s["average"], reverse=True)[:top_n]

    
def class_summary(students: list[dict]) -> str:
    """Genera un reporte de la clase."""
    if not students:
        return "No hay estudiantes registrados."
    
    averages = [s["average"] for s in students] 
    passed = [s for s in students if s["passed"]]
    
    return f"""
=== Reporte de Clase ===
Total estudiantes : {len(students)}
Aprobados         : {len(passed)} ({len(passed)/len(students)*100:.0f}%)
Promedio clase    : {sum(averages)/len(averages):.2f}
Nota más alta     : {max(averages):.2f}
Nota más baja     : {min(averages):.2f}
"""

students = [
    create_student("Ana",    [9.0, 8.5, 9.5]),
    create_student("Carlos", [7.0, 8.0, 6.5]),
    create_student("María",  [5.0, 4.5, 6.0]),
    create_student("Daniel",   [8.0, 6.0, 7.0]),
    create_student("Jose",  [8.0, 5.5, 10.0]),
    create_student("Pedro", [6.0, 7.0, 8.0]),
    create_student("Juan", [4.0, 3.0, 10.0]),
    create_student("Luis", [3.0, 9.0, 7.0]),
]

print(class_summary(students))
top = get_top_students(students, top_n=2)
print("Top 2:", [s["name"] for s in top])