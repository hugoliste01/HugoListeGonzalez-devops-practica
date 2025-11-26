class Usuario:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
        
    def is_admin():
        return False
    
    def __str__(self):
        return f"{self.name} ({self.email})"
    
class Cliente(Usuario):
    def __init__(self, id, name, email, dir):
        self.id = id
        self.name = name
        self.email = email
        self.dir = dir

class Administrador(Usuario):
    def is_admin():
        return True