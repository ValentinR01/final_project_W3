from models.all_tables import Role, Domain

# This is the data that will be inserted into the tables who have just a column
tables_to_fill_with_data = {
    Domain: ['redaction', 'translation', 'management', 'development'],
    Role: ['superadmin', 'worker', 'lead', 'developer']
}


def insert_init_data():
    for table, data in tables_to_fill_with_data.items():
        for value in data:
            instance = table(value)
            instance.create()
    return True
