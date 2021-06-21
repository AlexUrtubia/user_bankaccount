class User:
    def __init__(self, name, email): 
        self.name = name
        self.email = email
        self.cuentas = [0] # Se crea una lista con las cuentas del usuario
    # Método para crear una cuenta    
    def crear_cuenta(self, tipo_cta):
        self.cuentas.append(BankAccount(tipo_cta, saldo=0,tasa_inte=0.1)) #Añade a la lista de cuentas el __init__ de Bankaccount
        return self
    # Mediante el método deposit de BankAccount se realiza un depósito a la cuanta especificada
    def make_deposit(self, id_cta, amount):	
        self.cuentas[id_cta].deposit(amount)	# id_cta corresponde al índice de la lista de cuentas del usuario
        print(self.name,"ha depositado $",amount,"en su cuenta",self.cuentas[id_cta].tipo_cta)
        return self
    def make_withdrawal (self, id_cta, amount):
        self.cuentas[id_cta].withdraw(amount)
        print(self.name,"ha retirado $",amount,"de su cuenta",self.cuentas[id_cta].tipo_cta)
        return self
    def display_user_balance (self,id_cta):
            print(self.name,"tiene un saldo de $",self.cuentas[id_cta].saldo,"en su cuenta",self.cuentas[id_cta].tipo_cta)
            return self
    def transfer_money (self, amount, id_cta, some_user, id_cta2): # Se indica el monto, la cuenta de origen, el usuario y la cuenta de ese usuario
        if self.cuentas[id_cta].saldo >= amount:
            if self.name != some_user.name:
                self.cuentas[id_cta].withdraw(amount)
                some_user.make_deposit(id_cta2,amount)
                print(self.name,"ha transferido $",amount,"desde su cuenta",self.cuentas[id_cta].tipo_cta,"a la cuenta",some_user.cuentas[id_cta2].tipo_cta,"de",some_user.name)
            elif self.name == some_user.name: # Si es que el usuario transfiere entre sus cuentas, el print es distinto
                self.cuentas[id_cta].withdraw(amount)
                some_user.make_deposit(id_cta2,amount)
                print(self.name,"ha transferido $",amount,"desde su cuenta",self.cuentas[id_cta].tipo_cta,"a su cuenta",some_user.cuentas[id_cta2].tipo_cta)
        else:
            print("El saldo es insuficiente para realizar esta transacción \nIndique un monto igual o menor a",self.cuentas[id_cta].saldo)
        return self
    
class BankAccount:
        def __init__(self, tipo_cta, saldo=0, tasa_inte=0.01):
            self.tipo_cta = tipo_cta
            self.saldo = saldo
            self.tasa_inte = tasa_inte
    #Agrega un método de depósito a la clase BankAccount   
        def deposit(self, amount):
            self.saldo += amount
            #print(self.name,"a recibido un deposito de $",amount,"en su cuenta",self.tipo_cta)
            return self
        #Agrega un método de retiro a la clase BankAccount
        def withdraw(self, amount):
            if self.saldo >= amount:
                self.saldo -= amount
                #print("Se ha retirado $",amount,"de la cuenta",self.tipo_cta)
            else:
                print("El saldo de la cuenta",self.tipo_cta,"es insuficiente como para retirar $",amount,"\nIngrese un monto menor")
            return self
        #Agrega un método display_account_info a la clase BankAccount
        def display_account_info(self):
            print("Saldo en la cuenta",self.tipo_cta,"= $",self.saldo)
            #return self
        #Agrega un método yield_interest a la clase BankAccount
        def yield_interest(self):
            if self.saldo > 0:
                self.saldo += (self.tasa_inte*self.saldo)
                print(self.nombre,"a aumentado en $",self.saldo*self.tasa_inte,"su saldo gracias a intereses generados")
                return self

# Se instancia un usuario nuevo, que crea 2 cuentas, añade un monto a cada una de estas, 
# y posteriormente realiza retiros de dinero en ambas
# Imprime el saldo de ambas cuentas
user1=User("Alex","alex@email.com")
user1.crear_cuenta(1).crear_cuenta(2).make_deposit(1,100000).make_deposit(2,170000)
user1.make_withdrawal(1,5000).make_withdrawal(2,3000).make_withdrawal(1,7000)
user1.display_user_balance(1).display_user_balance(2)
# Se instancia un segundo usuario, que crea una cuenta y realiza un depósito
user2=User("Victoria","victoria@email.com")
user2.crear_cuenta(1).make_deposit(1,20000)
user2.display_user_balance(1)
# El primer usuario le transfiere desde su cuenta 1 a la cuenta 1 del usuario 2
user1.transfer_money(20000,1,user2,1)
# El usuario 2 crea otra cuenta y transfiere dinero desde su cuenta 1 a la cuenta 2, 
# el print de la transferencia es distinto en esta ocasión
user2.crear_cuenta(2)
user2.transfer_money(20000,1,user2,2).display_user_balance(2).display_user_balance(1)
# Se prueba una transferencia fallida por falta de fondos, indica el saldo de la cuenta, que
# a la vez, es la cantidad máxima posible a transferir
user2.transfer_money(25000,1,user1,1)