import os
import django
import random
from faker import Faker

# Configuración del entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backenduniguajira.settings')
django.setup()

# Importar los modelos
from MisApps.programsdir.models import Programsdir
from MisApps.programs.models import Programs
from MisApps.students.models import Students
from MisApps.professors.models import Professors
from MisApps.admission.models import Admission
from MisApps.loans.models import Loans
from MisApps.reports.models import Reports

# Crear una instancia de Faker
fake = Faker()

# Función para crear Programsdir
def create_programsdir(n=50):
    print(f'Creando {n} Programsdir...')
    programsdir_list = []
    for _ in range(n):
        programsdir = Programsdir(
            name=fake.name(),
            address=fake.address(),
            phone=fake.phone_number()[:12],  # Limitar a 12 caracteres
            email=fake.email(),
        )
        programsdir_list.append(programsdir)
    Programsdir.objects.bulk_create(programsdir_list)
    print(f'{n} Programsdir creados exitosamente.')

# Función para crear Programs
def create_programs(n=100):
    print(f'Creando {n} Programs...')
    programsdir_ids = list(Programsdir.objects.values_list('id', flat=True))
    if not programsdir_ids:
        print("No hay Programsdir disponibles. Asegúrate de ejecutar create_programsdir primero.")
        return
    programs_list = []
    for _ in range(n):
        program = Programs(
            name=fake.word().capitalize(),
            director_id=random.choice(programsdir_ids),
        )
        programs_list.append(program)
    Programs.objects.bulk_create(programs_list)
    print(f'{n} Programs creados exitosamente.')

# Función para crear Students
def create_students(n=200):
    print(f'Creando {n} Students...')
    program_ids = list(Programs.objects.values_list('id', flat=True))
    if not program_ids:
        print("No hay Programs disponibles. Asegúrate de ejecutar create_programs primero.")
        return
    students_list = []
    for _ in range(n):
        student = Students(
            name=fake.name(),
            address=fake.address(),
            phone=fake.phone_number()[:12],
            email=fake.email(),
            program_id=random.choice(program_ids),
        )
        students_list.append(student)
    Students.objects.bulk_create(students_list)
    print(f'{n} Students creados exitosamente.')

# Función para crear Professors
def create_professors(n=100):
    print(f'Creando {n} Professors...')
    program_ids = list(Programs.objects.values_list('id', flat=True))
    if not program_ids:
        print("No hay Programs disponibles. Asegúrate de ejecutar create_programs primero.")
        return
    professors_list = []
    for _ in range(n):
        professor = Professors(
            name=fake.name(),
            address=fake.address(),
            phone=fake.phone_number()[:12],
            email=fake.email(),
            program_id=random.choice(program_ids),
        )
        professors_list.append(professor)
    Professors.objects.bulk_create(professors_list)
    print(f'{n} Professors creados exitosamente.')

# Función para crear Admissions
def create_admissions(n=200):
    print(f'Creando {n} Admissions...')
    student_ids = list(Students.objects.values_list('id', flat=True))
    if not student_ids:
        print("No hay Students disponibles. Asegúrate de ejecutar create_students primero.")
        return
    admissions_list = []
    for _ in range(n):
        admission = Admission(
            student_id=random.choice(student_ids),
            dateadmission=fake.date_between(start_date='-5y', end_date='today'),
            status=random.choice(['activo', 'inactivo', 'pendiente']),
        )
        admissions_list.append(admission)
    Admission.objects.bulk_create(admissions_list)
    print(f'{n} Admissions creados exitosamente.')

# Función para crear Loans
def create_loans(n=300):
    print(f'Creando {n} Loans...')
    student_ids = list(Students.objects.values_list('id', flat=True))
    if not student_ids:
        print("No hay Students disponibles. Asegúrate de ejecutar create_students primero.")
        return
    loans_list = []
    for _ in range(n):
        dateloans = fake.date_between(start_date='-2y', end_date='today')
        datereturn = fake.date_between(start_date=dateloans, end_date='+30d')
        loan = Loans(
            student_id=random.choice(student_ids),
            namebook=fake.word().capitalize(),
            dateloans=dateloans,
            datereturn=datereturn,
        )
        loans_list.append(loan)
    Loans.objects.bulk_create(loans_list)
    print(f'{n} Loans creados exitosamente.')

# Función para crear Reports
def create_reports(n=300):
    print(f'Creando {n} Reports...')
    student_ids = list(Students.objects.values_list('id', flat=True))
    if not student_ids:
        print("No hay Students disponibles. Asegúrate de ejecutar create_students primero.")
        return
    reports_list = []
    for _ in range(n):
        report = Reports(
            student_id=random.choice(student_ids),
            description=fake.sentence(nb_words=10),
            date=fake.date_between(start_date='-1y', end_date='today'),
        )
        reports_list.append(report)
    Reports.objects.bulk_create(reports_list)
    print(f'{n} Reports creados exitosamente.')

if __name__ == '__main__':
    print('Iniciando la creación de datos falsos...')
    
    # Crear Programsdir primero
    create_programsdir(n=50)
    
    # Crear Programs después de Programsdir
    create_programs(n=100)
    
    # Crear Students después de Programs
    create_students(n=200)
    
    # Crear Professors después de Programs
    create_professors(n=100)
    
    # Crear Admissions después de Students
    create_admissions(n=200)
    
    # Crear Loans después de Students
    create_loans(n=300)
    
    # Crear Reports después de Students
    create_reports(n=300)
    
    print('¡Todos los datos falsos han sido creados exitosamente!')
