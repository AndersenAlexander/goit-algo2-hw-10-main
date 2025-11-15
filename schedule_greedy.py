from colorama import Fore, Style, init

# Initialize colorama for Windows
init()


class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = set(can_teach_subjects)
        self.assigned_subjects = set()


def create_schedule(subjects, teachers):
    remaining_subjects = set(subjects)
    schedule = []

    while remaining_subjects:
        best_teacher = None
        best_coverage = set()

        for teacher in teachers:
            coverage = teacher.can_teach_subjects & remaining_subjects
            if len(coverage) > len(best_coverage) or (
                len(coverage) == len(best_coverage)
                and teacher.age < (best_teacher.age if best_teacher else float("inf"))
            ):
                best_teacher = teacher
                best_coverage = coverage

        if not best_teacher:
            print(
                Fore.RED
                + "It is impossible to cover all subjects with the available teachers."
                + Style.RESET_ALL
            )
            return None

        best_teacher.assigned_subjects = best_coverage
        schedule.append(best_teacher)
        remaining_subjects -= best_coverage

    return schedule


if __name__ == "__main__":
    subjects = {"Mathematics", "Physics", "Chemistry", "Computer Science", "Biology"}

    teachers = [
        Teacher(
            "John",
            "Smith",
            50,
            "john.smith@example.com",
            {"Mathematics", "Physics"},
        ),
        Teacher("Emma", "Johnson", 32, "emma.johnson@example.com", {"Chemistry"}),
        Teacher(
            "Liam",
            "Brown",
            50,
            "liam.brown@example.com",
            {"Computer Science", "Mathematics"},
        ),
        Teacher(
            "Sophia",
            "Davis",
            29,
            "sophia.davis@example.com",
            {"Biology", "Chemistry"},
        ),
        Teacher(
            "Noah",
            "Wilson",
            35,
            "noah.wilson@example.com",
            {"Physics", "Computer Science"},
        ),
        Teacher(
            "Olivia",
            "Taylor",
            42,
            "olivia.taylor@example.com",
            {"Biology"},
        ),
    ]


    schedule = create_schedule(subjects, teachers)

    if schedule:
        print(Fore.CYAN + "Class schedule:" + Style.RESET_ALL)
        for teacher in schedule:
            print(
                Fore.GREEN
                + f"{teacher.first_name} {teacher.last_name}, {teacher.age} years old, email: {teacher.email}"
                + Style.RESET_ALL
            )
            print(
                Fore.YELLOW
                + f"   Teaches: {', '.join(teacher.assigned_subjects)}\n"
                + Style.RESET_ALL
            )
