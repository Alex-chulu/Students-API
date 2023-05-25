from flask import Flask 
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

# Create a dictionary of students ordered by student_id
STUDENTS = {
    '1': {'name': 'Mark', 'age': 23, 'spec': 'math'},
    '2': {'name': 'Jane', 'age': 20, 'spec': 'biology'},
    '3': {'name': 'Peter', 'age': 21, 'spec': 'history'},
    '4': {'name': 'Kate', 'age': 22, 'spec': 'science'},
    '5': {'name': 'Mary', 'age': 24, 'spec': 'literature'}
}


# Create a parser valiable
parser = reqparse.RequestParser()

# Create a class for the students
class StudentsList(Resource):
    # Create a method to get the students
    def get(self):
        return STUDENTS
    
    # Create a method to post the students. 
    # This method adds new student to the list
    def post(self):
        parser.add_argument("name")
        parser.add_argument("age")
        parser.add_argument("spec")
        
        args = parser.parse_args()
        student_id = int(max(STUDENTS.keys())) + 1
        student_id = '%i' % student_id
        
        STUDENTS[student_id] = {
            "name": args["name"],
            "age": args["age"],
            "spec": args["spec"]
        }
        return STUDENTS[student_id], 201

# Create a class for the student object that will 
# be used to get, update and delete the student
class Student(Resource):
    # Create a method to get the student
    # This method returns the student with the given id
    def get(self, student_id):
        if student_id not in STUDENTS:
            return "Not found", 404
        else:
            return STUDENTS[student_id], 200
        
    # Create a method to update the student 
    # This method updates the student with the given id     
    def put(self, student_id):
        parser.add_argument("name")
        parser.add_argument("age")
        parser.add_argument("spec")
        args = parser.parse_args()
        if student_id not in STUDENTS:
            return "Record not found", 404
        else:
            student = STUDENTS[student_id]
            student["name"] = args["name"] if args["name"] is not None else student["name"]
            student["age"] = args["age"] if args["age"] is not None else student["age"]
            student["spec"] = args["spec"] if args["spec"] is not None else student["spec"]
            return student, 200
        
    # Create a method to delete the student
    # This method deletes the student with the given id
    def delete(self, student_id):
        if student_id not in STUDENTS:
            return "Not found", 404
        else:
            del STUDENTS[student_id]
            return '', 204
        
# Add the routes
api.add_resource(Student, '/students/<student_id>')
api.add_resource(StudentsList, '/students/')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)