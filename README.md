# Database Manager using MongoDB


This project provides a DatabaseManager class that interacts with a MongoDB database to perform CRUD operations and complex queries.

Installation
Clone the repository:

bash
Copy code
git clone https://github.com/Aleksandre16/Swap-Relation-DB-To-No-SQL-DB
Install the required dependencies:

bash
Copy code
pip install pymongo
Ensure that MongoDB is installed and running on your local machine.

Usage
Import the DatabaseManager class into your Python script:

python
Copy code
from database_manager import DatabaseManager
Create an instance of the DatabaseManager class:

python
Copy code
db_manager = DatabaseManager()
Use the DatabaseManager instance to perform various operations on the MongoDB database, such as adding data, querying data, updating data, and deleting data.

Example Usage:
python
Copy code
# Add data to the "students" collection
db_manager.add_data("students", student_id="S001", name="John", surname="Doe", age=20)

# Query data from the "students" collection
students = db_manager.search("students", name="John")

# Update data in the "students" collection
db_manager.update("students", name="Jane", surname="Smith", age=21, document_id="S001")

# Delete data from the "students" collection
db_manager.delete_row("students", row_id="S001")
Functionality
Create Table: Not applicable for MongoDB since it is schemaless.

Add Data: Insert a document into a specified collection.

Get Existing Relations: Retrieve existing relations (student-advisor pairs) from the "student_advisor" collection.

Delete Row: Delete a document from a specified collection based on the provided row identifier.

Load Data: Load all documents from a specified collection.

Search: Search documents in a specified collection based on provided criteria.

Update: Update a document in a specified collection based on provided data and document identifier.

Check Database: Check if a specified collection is empty in the MongoDB database.

List Advisors with Students Count: Retrieve advisors along with the count of students they advise, ordered by the count of students.

List Students with Advisors Count: Retrieve students along with the count of advisors they have, ordered by the count of advisors.

Homework
Implement the provided DatabaseManager class using MongoDB instead of SQLite. Ensure that the functionality remains the same, and replace any SQL queries with equivalent MongoDB operations.
