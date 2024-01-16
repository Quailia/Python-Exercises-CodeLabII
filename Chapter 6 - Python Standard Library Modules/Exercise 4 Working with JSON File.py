import json

def write_to_json(student_details):
    with open('StudentJson.json', 'w') as json_file:
        json.dump(student_details, json_file, indent=4)

def read_from_json():
    with open('StudentJson.json', 'r') as json_file:
        student_details = json.load(json_file)
    return student_details

# User input and saving
student_name = input("Enter the student name: ")
student_id = int(input("Enter the student ID: "))
course = input("Enter the course: ")

student_details = {
    "Name": student_name,
    "ID": student_id,
    "course": course
}

write_to_json(student_details)
print("Details of the Student are")
for key, value in student_details.items():
    print(f"\t{key}: {value}")

# Appending course details to student details
course_details = {
    "CourseDetails": {
        "Group": input("Enter the group: "),
        "Year": int(input("Enter the year: "))
    }
}

student_details.update(course_details)
write_to_json(student_details)

# Displaying individual values from the json
updated_student_details = read_from_json()
print(updated_student_details)
print("\nDetails of the Student are")
for key, value in updated_student_details.items():
    if isinstance(value, dict):
        for sub_key, sub_value in value.items():
            print(f"\t{sub_key}: {sub_value}")
    else:
        print(f"\t{key}: {value}")
