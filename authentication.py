import db_table_queries

def authenticateCustomer(email,password):
    result = db_table_queries.authenticateCustomer(email,password)
    if result[0] == 0:
        return [False, ""]
    else: 
        return [True, result[1][0]]
    
def authenticateStaff(username,password):
    result = db_table_queries.authenticateStaff(username,password)
    if result[0] == 0:
        return [False, ""]
    else:
        return [True, result[1][0]]