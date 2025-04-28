import pyodbc

class DatabaseInterface:
    def __init__(self, connection_string):
        self.conn = pyodbc.connect(connection_string)
        self.cursor = self.conn.cursor()

    def save_memory(self, input_text, response_text, emotion, intensity):
        query = "INSERT INTO Memories (input_text, response_text, emotion, intensity) VALUES (?, ?, ?, ?)"
        self.cursor.execute(query, (input_text, response_text, emotion, intensity))
        self.conn.commit()

    def update_trait(self, trait_name, trait_value):
        query = "UPDATE Traits SET trait_value = ?, last_updated = GETDATE() WHERE trait_name = ?"
        self.cursor.execute(query, (trait_value, trait_name))
        self.conn.commit()

