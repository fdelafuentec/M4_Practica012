import xml.etree.ElementTree as ET

def creacion_xml():
    # Creamos el elemento root y se asignamos la variable root
    root = ET.Element("students")

    # creamos el usuario
    for i in range(5):
        student = ET.SubElement(root, "student", id=str(i+1))  # Añadimos el atributo
        name = ET.SubElement(student, "name")
        name.text = f"Student {i+1}" # Utilizamos el format con una f al principio
        surname = ET.SubElement(student, "surname")
        surname.text = "Surname"
        email = ET.SubElement(student, "email")
        email.text = f"student{i+1}@example.com"
        dni = ET.SubElement(student, "dni")
        dni.text = f"1234567{i+1}"

    # Escribimos en el xml
    tree = ET.ElementTree(root)
    tree.write("students.xml", encoding="UTF-8", xml_declaration=True)

    # imprimimos el xml por consola
    with open("students.xml", "r") as file:
        print(file.read())
