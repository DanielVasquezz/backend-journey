def create_student(name:str, grades:list[float] | None = None) -> dict:
    if grades is None:
        grades = []
    avg = sum(grades) / len(grades) if grades else 0.0
    return {
        "name": name,
        "grades": grades,
        "average": round(avg,2),
        "passed": avg >= 6.0
    }

