from pymongo import MongoClient


class DatabaseManager:
    def __init__(self):
        self.client = MongoClient("localhost", 27017)
        self.database = self.client["Database"]

    def create_table(self):
        pass

    def add_data(self, table_name, **kwargs):
        self.database[table_name].insert_one(kwargs)

    def get_existing_relations(self):
        result = self.database["student_advisor"].find()
        return [(i['student_id'], i['advisor_id'],) for i in result]

    def delete_row(self, table_name, row_id):
        if table_name == "advisor":
            self.database[table_name].delete_one({"advisor_id": row_id})
        else:
            self.database[table_name].delete_one({"student_id": row_id})

    def load_data(self, table_name):
        return list(self.database[table_name].find())

    def search(self, table_name, name=None, surname=None, age=None, student_id=None, advisor_id=None):
        conditions = {}
        if student_id:
            conditions["student_id"] = {"$regex": f".*{student_id}.*"}
        if advisor_id:
            conditions["advisor_id"] = {"$regex": f".*{advisor_id}.*"}
        if name:
            conditions["name"] = {"$regex": f".*{name}.*"}
        if surname:
            conditions["surname"] = {"$regex": f".*{surname}.*"}
        if age:
            conditions["age"] = {"$regex": f".*{age}.*"}

        if conditions:
            return list(self.database[table_name].find(conditions))
        else:
            return self.load_data(table_name)

    def update(self, table_name, name, surname, age, document_id):
        if table_name == "students":
            self.database[table_name].update_one({"student_id": document_id},
                                                 {"$set": {"name": name, "surname": surname, "age": age}})
        elif table_name == "advisors":
            self.database[table_name].update_one({"advisor_id": document_id},
                                                 {"$set": {"name": name, "surname": surname, "age": age}})

    def check_bd(self):
        return self.database["student_advisor"].count_documents({}) == 0

    def list_advisors_with_students_count(self, order_by):
        pipeline = [
            {"$lookup": {
                "from": "student_advisor",
                "localField": "advisor_id",
                "foreignField": "advisor_id",
                "as": "students"
            }},
            {"$project": {
                "advisor_id": 1,
                "name": 1,
                "surname": 1,
                "student_count": {"$size": "$students"}
            }},
            {"$sort": {"student_count": order_by}}
        ]
        return list(self.database["advisors"].aggregate(pipeline))

    def list_students_with_advisors_count(self, order_by):
        pipeline = [
            {"$lookup": {
                "from": "student_advisor",
                "localField": "student_id",
                "foreignField": "student_id",
                "as": "advisors"
            }},
            {"$project": {
                "student_id": 1,
                "name": 1,
                "surname": 1,
                "advisor_count": {"$size": "$advisors"}
            }},
            {"$sort": {"advisor_count": order_by}}
        ]
        return list(self.database["students"].aggregate(pipeline))


""
