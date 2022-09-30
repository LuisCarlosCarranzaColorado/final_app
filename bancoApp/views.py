import datetime
import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from django.conf import settings
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Customer, Account, historia_clinica, paciente, secretario, usuario, medico,enfermero,acompanante

def home(request):
    return HttpResponse("Bienvenida a su banco.")

def newCustomer(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            customer = Customer.objects.filter(id = data['id']).first()
            if (customer):
                return HttpResponseBadRequest("Ya existe cliente con esa cédula.")

            customer = Customer(
                id = data["id"],
                firstName = data["firstName"],
                lastName = data["lastName"],
                email = data["email"],
                password = data["password"],
            )
            customer.save()
            return HttpResponse("Nuevo cliente agregado")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")

def getAllCustomers(request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        if (not customers):
            return HttpResponseBadRequest("No hay clientes en la base de datos.")

        allCustData = []
        for x in customers:
            data = {"id": x.id, "firstName": x.firstName, "lastName": x.lastName, "email": x.email}
            allCustData.append(data)
        dataJson = json.dumps(allCustData)
        #print(dataJson)
        resp = HttpResponse()
        resp.headers['Content-Type'] = "text/json"
        resp.content = dataJson
        return resp
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")

def getOneCustomer(request, id):
    if request.method == 'GET':
        try:
            token = request.META.get('HTTP_AUTHORIZATION')[7:]
            tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
            valid_data = tokenBackend.decode(token, verify=False)
            #print(valid_data)
            if valid_data['user_id'] != id:
                raise Exception
        except:
            return HttpResponse("Credenciales inválidas. Acceso no autorizado", status=401)

        customer = Customer.objects.filter(id = id).first()
        if (not customer):
            return HttpResponseBadRequest("No existe cliente con esa cédula.")

        accounts = Account.objects.filter(customer = id)
        accountsData = []
        for acc in accounts:
            data = {"number": acc.number, "balance": float(acc.balance)}
            accountsData.append(data)

        data = {
            "id": customer.id,
            "firstName": customer.firstName,
            "lastName": customer.lastName,
            "email": customer.email,
            "accounts": accountsData
        }
        dataJson = json.dumps(data)
        resp = HttpResponse()
        resp.headers['Content-Type'] = "text/json"
        resp.content = dataJson
        return resp
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")

def updateCustomer(request, id):
    if request.method == 'PUT':
        try:
            token = request.META.get('HTTP_AUTHORIZATION')[7:]
            tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
            valid_data = tokenBackend.decode(token, verify=False)
            #print(valid_data)
            if valid_data['user_id'] != id:
                raise Exception
        except:
            return HttpResponse("Credenciales inválidas. Acceso no autorizado", status=401)
        
        try:
            customer = Customer.objects.filter(id = id).first()
            if (not customer):
                return HttpResponseBadRequest("No existe cliente con esa cédula.")

            data = json.loads(request.body)
            if 'firstName' in data.keys():
                customer.firstName = data["firstName"]
            if 'lastName' in data.keys():
                customer.lastName = data["lastName"]
            if 'email' in data.keys():
                customer.email = data["email"]
            if 'password' in data.keys():
                customer.password = data["password"]
            customer.save()
            return HttpResponse("Cliente actualizado")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['PUT'], "Método inválido")

def deleteCustomer(request, id):
    if request.method == 'DELETE':
        try:
            customer = Customer.objects.filter(id = id).first()
            if (not customer):
                return HttpResponseBadRequest("No existe cliente con esa cédula.")

            customer.delete()
            return HttpResponse("Cliente eliminado")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['DELETE'], "Método inválido")

#-----------------
# Account
#-----------------

def newAccount(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            cust = Customer.objects.filter(id = data["userId"]).first()
            if (not cust):
                return HttpResponseBadRequest("No existe cliente con esa cédula.")
            
            account = Account(
                number = data["number"],
                lastChangeDate = datetime.datetime.now(),
                customer = cust
            )
            account.save()
            return HttpResponse("Nueva cuenta agregada")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")

def updateAccount(request, id):
    if request.method == 'PUT':
        try:
            account = Account.objects.filter(number = id).first()
            if (not account):
                return HttpResponseBadRequest("No existe esa cuenta.")

            data = json.loads(request.body)
            account.balance = data["balance"]
            account.isActive = data["isActive"]
            account.save()
            return HttpResponse("Cuenta actualizada")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['PUT'], "Método inválido")

def deleteAccount(request, id):
    if request.method == 'DELETE':
        try:
            account = Account.objects.filter(number = id).first()
            if (not account):
                return HttpResponseBadRequest("No existe esa cuenta.")

            account.delete()
            return HttpResponse("Cuenta eliminada")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['DELETE'], "Método inválido")

#-----------------
# MODELADO HOSPITALE EN CASA
#-----------------

#-----------------
# Login
#-----------------

"""def login2(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data['email']
            password = data['password']
            print(email)
            print(password)
            Usuario = usuario.objects.filter(email = email, password = password).first()
            if (not Usuario):
                return HttpResponse("Credenciales inválidas.", status=401)

            custData = {"id": usuario.id}
            resp = HttpResponse()
            resp.headers['Content-Type'] = "text/json"
            resp.content = json.dumps(custData)
            return resp
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")"""

# Clases heredadas para mejorar el token a entregar
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super(MyTokenObtainPairSerializer, self).validate(attrs)
        data.update({'id': self.user.id})
        data.update({'rol':self.user.rol})
        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# USUARIOS

def getAllUsuarios(request):
    if request.method == 'GET':
        usuarios = usuario.objects.all()
        #usuarios = usuario.objects.filter(rol = "Médico")
        if (not usuarios):
            return HttpResponseBadRequest("No hay usuarios en la base de datos.")

        allCustData = []
        for x in usuarios:
            data = {
            "id": x.id, 
            "primer_nombre": x.primer_nombre, 
            "segundo_nombre": x.segundo_nombre,
            "primer_apellido": x.primer_apellido, 
            "segundo_apellido": x.segundo_apellido, 
            "email": x.email, 
            "no_celular": x.no_celular, 
            "rol": x.rol, 
            "password": x.password
            #"fecha_nacimiento": x.fecha_nacimiento,
            #"ubicacion_gps_latitud": float(x.ubicacion_gps_latitud),
            #"ubicacion_gps_longitud": float(x.ubicacion_gps_longitud)
            }
            allCustData.append(data)
        print(allCustData)
        dataJson = json.dumps(allCustData)
        #print(dataJson)
        resp = HttpResponse()
        resp.headers['Content-Type'] = "text/json"
        resp.content = dataJson
        return resp
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")
def getPacientes(request):
    if request.method == 'GET':
        #usuarios = usuario.objects.all()
        usuarios = usuario.objects.filter(rol = "paciente")
        if (not usuarios):
            return HttpResponseBadRequest("No hay usuarios en la base de datos.")

        allCustData = []
        for x in usuarios:
            data = {
            "no_cedula": x.no_cedula, 
            "primer_nombre": x.primer_nombre, 
            "segundo_nombre": x.segundo_nombre,
            "primer_apellido": x.primer_apellido, 
            "segundo_apellido": x.segundo_apellido, 
            "email": x.email, 
            "no_celular": x.no_celular, 
            "rol": x.rol, 
            "contrasena": x.contrasena, 
            #"fecha_nacimiento": x.fecha_nacimiento,
            "ubicacion_gps_latitud": float(x.ubicacion_gps_latitud),
            "ubicacion_gps_longitud": float(x.ubicacion_gps_longitud)
            }
            allCustData.append(data)
        print(allCustData)
        dataJson = json.dumps(allCustData)
        #print(dataJson)
        resp = HttpResponse()
        resp.headers['Content-Type'] = "text/json"
        resp.content = dataJson
        return resp
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")
def newUsuario(request):
    if request.method == 'POST':     
        try:
            data = json.loads(request.body)
            cedula = data["id"]
            email = data["email"]
            Usuario2 = usuario.objects.filter(id = cedula).first()
            if (Usuario2):
                return HttpResponseBadRequest("cedula ya existe")
            Usuario3 = usuario.objects.filter(email = email).first()    
            if (Usuario3):
                return HttpResponseBadRequest("ya existe un correo con esa cedula o con ese correo.")
            Usuario = usuario(
                id = data["id"],
                primer_nombre = data["primer_nombre"],
                segundo_nombre = data["segundo_nombre"],
                primer_apellido = data["primer_apellido"],
                segundo_apellido = data["segundo_apellido"],
                email = data["email"],
                no_celular = data["no_celular"],
                rol = data["rol"],
                password = data["password"],
                #fecha_nacimiento = data["fecha_nacimiento"],
                #ubicacion_gps_latitud = data["ubicacion_gps_latitud"],
                #ubicacion_gps_longitud = data["ubicacion_gps_longitud"],
            )
            Usuario.save()
            return HttpResponse("Nuevo usuario agregado")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")
def updateUsuario(request, id):
    if request.method == 'PUT':
        try:
            Usuario = usuario.objects.filter(id = id).first()
            if (not Usuario):
                return HttpResponseBadRequest("No existe usuario con esa cédula.")
            data = json.loads(request.body)
            Usuario.primer_nombre = data["primer_nombre"]
            Usuario.segundo_nombre = data["segundo_nombre"]
            Usuario.primer_apellido = data["primer_apellido"]
            Usuario.segundo_apellido = data["segundo_apellido"]
            Usuario.email = data["email"]
            Usuario.no_celular = data["no_celular"]
            Usuario.rol = data["rol"]
            Usuario.password = data["password"]
            #Usuario.fecha_nacimiento = data["fecha_nacimiento"]
            #Usuario.ubicacion_gps_latitud = data["ubicacion_gps_latitud"]
            #Usuario.ubicacion_gps_longitud = data["ubicacion_gps_longitud"]

            Usuario.save()
            return HttpResponse("usuario actualizado")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['PUT'], "Método inválido")
def deleteUsuario(request, no_cedula):
    if request.method == 'DELETE':
        try:
            Usuario = usuario.objects.filter(no_cedula = no_cedula).first()
            if (not Usuario):
                return HttpResponseBadRequest("No existe esa cedula.")

            Usuario.delete()
            return HttpResponse("usuario eliminado")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['DELETE'], "Método inválido")



# CRUD MEDICO
def newMedico(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print(data)
            llave = usuario.objects.filter(id = data["id"]).first()
            if (not llave):
                return HttpResponseBadRequest("No existe usuario con esa cédula.")
            #else:
                #llaveRol = usuario.objects.filter(rol = data["rol"]).first()
                #print("rol definido bien")
            
            Medico = medico(
                especialidad = data["especialidad"],
                no_cedula = llave
            )
            Medico.save()
            return HttpResponse("Nuevo medico agregado")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")
def getAllMedicos(request):
    if request.method == 'GET':
        Medico = medico.objects.all()
        
        if (not Medico):
            return HttpResponseBadRequest("No hay medicos en la base de datos.")

        allCustData = []
        for x in Medico:
            data = {
            "especialidad": x.especialidad, 
            "no_cedula": x.no_cedula_id,
            }
            allCustData.append(data)
        print(allCustData)
        dataJson = json.dumps(allCustData)
        #print(dataJson)
        resp = HttpResponse()
        resp.headers['Content-Type'] = "text/json"
        resp.content = dataJson
        return resp
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")
def updateMedico(request, no_cedula):
    if request.method == 'PUT':
        try:
            Medico = medico.objects.filter(no_cedula = no_cedula).first()
            if (not Medico):
                return HttpResponseBadRequest("No existe medico con esa cédula.")

            data = json.loads(request.body)

            Medico.especialidad = data["especialidad"]
            Medico.save()
            return HttpResponse("la especialidad se actualizo")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['PUT'], "Método inválido")
def deleteMedico(request, no_cedula):
    if request.method == 'DELETE':
        try:
            Medico = medico.objects.filter(no_cedula = no_cedula).first()
            if (not Medico):
                return HttpResponseBadRequest("No existe ese medico.")

            Medico.delete()
            return HttpResponse("medico eliminado")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['DELETE'], "Método inválido")
def getOneMedico(request, no_cedula):# último metodo actualizado
    if request.method == 'GET':
        Medico = medico.objects.filter(no_cedula = no_cedula).first()
        if (not Medico):
            return HttpResponseBadRequest("No existe medico con esa cédula.")
        print(Medico)
        Pacientes = paciente.objects.filter(id_medico = Medico.id_medico)
        accountsData=[]    
        for x in Pacientes:
                data2 = {
                        "nombres": x.no_cedula.primer_nombre + " " + x.no_cedula.primer_apellido,
                        "cedula": x.no_cedula.id,
                        "enfermero": x.id_enfermero.no_cedula.primer_nombre + " " + x.id_enfermero.no_cedula.primer_apellido
                        }
                accountsData.append(data2)
        print(accountsData)
        data = {
            "Nombre_medico": Medico.no_cedula.primer_nombre + " "+ Medico.no_cedula.primer_apellido,
            "rol": Medico.no_cedula.rol,
            "especialidad":Medico.especialidad,
            "Pacientes": accountsData
        } 
        print(data)
        dataJson = json.dumps(data)
        resp = HttpResponse()
        resp.headers['Content-Type'] = "text/json"
        resp.content = dataJson
        return resp
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")
        
# CRUD SECRETARIO

def newSecretario(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print(data)
            llave = usuario.objects.filter(no_cedula = data["no_cedula"]).first()
            if (not llave):
                return HttpResponseBadRequest("No existe usuario con esa cédula.")
            #else:
                #llaveRol = usuario.objects.filter(rol = data["rol"]).first()
                #print("rol definido bien")
            
            Secretario = secretario(
                turno = data["turno"],
                no_cedula = llave
            )
            Secretario.save()
            return HttpResponse("Nuevo secretario agregado")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")
def getOneSecretario(request, no_cedula):
    if request.method == 'GET':
        Secretario = secretario.objects.filter(no_cedula = no_cedula).first()
        if (not Secretario):
            return HttpResponseBadRequest("No existe secretario con esa cédula.")
        Usuario=Secretario.no_cedula
        
        data = {
                "Nombre_enfermero": Usuario.primer_nombre + " "+ Usuario.primer_apellido,
                "rol": Usuario.rol,
                "turno": Secretario.turno
                }
        dataJson = json.dumps(data)
        resp = HttpResponse()
        resp.headers['Content-Type'] = "text/json"
        resp.content = dataJson
        return resp
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")

# CRUD ENFERMERO
def newEnfermero(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print(data)
            llave = usuario.objects.filter(id = data["no_cedula"]).first()
            if (not llave):
                return HttpResponseBadRequest("No existe usuario con esa cédula.")
            #else:
                #llaveRol = usuario.objects.filter(rol = data["rol"]).first()
                #print("rol definido bien")
            
            Enfermero = enfermero(
                especialidad = data["especialidad"],
                turno = data["turno"],
                no_cedula = llave
            )
            Enfermero.save()
            return HttpResponse("Nuevo secretario agregado")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")
def getOneEnfermero(request, no_cedula):
    if request.method == 'GET':
        Enfermero = enfermero.objects.filter(no_cedula = no_cedula).first()
        if (not Enfermero):
            return HttpResponseBadRequest("No existe enfermero con esa cédula.")
        Usuario=Enfermero.no_cedula
        
        data = {
                "Nombre enfermero": Usuario.primer_nombre + " "+ Usuario.primer_apellido,
                "rol": Usuario.rol,
                "especialidad": Enfermero.especialidad
                }
        dataJson = json.dumps(data)
        resp = HttpResponse()
        resp.headers['Content-Type'] = "text/json"
        resp.content = dataJson
        return resp
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")

# CRUD PACIENTE
def newPaciente(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print(data)
            llave = usuario.objects.filter(id = data["no_cedula"]).first()
            if (not llave):
                return HttpResponseBadRequest("No existe usuario con esa cédula.")
            llaveMed = medico.objects.filter(id_medico = data["id_medico"]).first()
            if (not llaveMed):
                return HttpResponseBadRequest("No existe medico asociado.")
            llaveEnf = enfermero.objects.filter(id_enfermero = data["id_enfermero"]).first()
            if (not llaveEnf):
                return HttpResponseBadRequest("No existe enfermero sociado.")
            
            Paciente = paciente(
                no_cedula = llave,
                id_medico = llaveMed,
                id_enfermero = llaveEnf
            )
            Paciente.save()
            return HttpResponse("Nuevo paciente agregado")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")
def getOnePaciente(request, no_cedula):
    if request.method == 'GET':
        Paciente = paciente.objects.filter(no_cedula = no_cedula).first()
        if (not Paciente):
            return HttpResponseBadRequest("No existe paciente con esa cédula.")
        Medico=Paciente.id_medico
        UsuarioM=Medico.no_cedula
        Enfermero=Paciente.id_enfermero
        UsuarioE=Enfermero.no_cedula
        Usuario=Paciente.no_cedula
        HC = historia_clinica.objects.filter(id_paciente = Paciente.id_paciente)
        print(HC)
        accountsData=[]        
        for x in HC:
            data2 = {
                    "id_historia": x.id_historia,
                    "Recomendaciones": x.Recomendaciones,
                    "Diagnostico": x.diagnostico
                   }
            accountsData.append(data2)
        data = {
            "Nombre paciente": Usuario.primer_nombre + " "+ Usuario.primer_apellido,
            "rol": Usuario.rol,
            "Nombre Medico": UsuarioM.primer_nombre +" "+UsuarioM.primer_apellido,
            "Especialidad Medico":Medico.especialidad,
            "Enfermero": UsuarioE.primer_nombre +" "+UsuarioE.primer_apellido,
            "turno enfermero": Enfermero.turno,
            "Historias Medicas": accountsData
        } 
        dataJson = json.dumps(data)
        resp = HttpResponse()
        resp.headers['Content-Type'] = "text/json"
        resp.content = dataJson
        return resp
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")
def getOnePacientePrueba(request, no_cedula):
    if request.method == 'GET':
        Paciente = paciente.objects.filter(no_cedula = no_cedula).first()
        if (not Paciente):
            return HttpResponseBadRequest("No existe paciente con esa cédula.")
        Medico=Paciente.id_medico
        UsuarioM=Medico.no_cedula
        Enfermero=Paciente.id_enfermero
        UsuarioE=Enfermero.no_cedula
        Usuario=Paciente.no_cedula
        HC = historia_clinica.objects.filter(id_paciente = Paciente.id_paciente)
        print(HC)
        accountsData=[]        
        for x in HC:
            data2 = {
                    "id_historia": x.id_historia,
                    "Recomendaciones": x.Recomendaciones,
                    "Diagnostico": x.diagnostico
                   }
            accountsData.append(data2)
        data = {
            "Nombre paciente": Usuario.primer_nombre + " "+ Usuario.primer_apellido,
            "rol": Usuario.rol,
            "Nombre Medico": UsuarioM.primer_nombre +" "+UsuarioM.primer_apellido,
            "Especialidad Medico":Medico.especialidad,
            "Enfermero": UsuarioE.primer_nombre +" "+UsuarioE.primer_apellido,
            "turno enfermero": Enfermero.turno,
            "Recomendaciones": accountsData
        } 
        dataJson = json.dumps(data)
        resp = HttpResponse()
        resp.headers['Content-Type'] = "text/json"
        resp.content = dataJson
        return resp
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")

# CRUD HC
def getOneHC(request, no_cedula):
    if request.method == 'GET':
        Paciente = paciente.objects.filter(no_cedula = no_cedula).first()
        if (not Paciente):
            return HttpResponseBadRequest("No existe paciente creado.")
        print(Paciente)
        Usuario = usuario.objects.filter(no_cedula = no_cedula).first()
        print(Usuario)
        Hc2 = Paciente.id_paciente    
        print(Hc2)
        Hc=historia_clinica.objects.filter(id_paciente = Hc2).first()
        if (not Hc):
            return HttpResponseBadRequest("No existe HC asociada al paciente.")
        print(Paciente)
        print(Hc)
        data = {
                "Nombre paciente": Usuario.primer_nombre + " "+ Usuario.primer_apellido,
                #"fecha_hora": Hc.fecha_hora,
                "diagnostico": Hc.diagnostico,
                "FC": Hc.FC,
                "TA": Hc.TA,
                "FR": Hc.FR,
                "Temp": Hc.Temp,
                "Oxi": Hc.Oxi,
                "Recomendaciones": Hc.Recomendaciones
                }
        dataJson = json.dumps(data)
        resp = HttpResponse()
        resp.headers['Content-Type'] = "text/json"
        resp.content = dataJson
        return resp
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")
def getAllHC(request):
    if request.method == 'GET':
        HC = historia_clinica.objects.all()
        #Usuario = usuario.objects.filter(id_cedula = Paciente.id_cedula)
        if (not HC):
            return HttpResponseBadRequest("No existen historia medicas creadas.")
        print(HC)
        Hc = []
        for x in HC:
            data = {
                #"Nombre paciente": Usuario.primer_nombre + " "+ Usuario.primer_apellido,
                #"fecha_hora": Hc.fecha_hora,
                "diagnostico": x.diagnostico,
                "FC": x.FC,
                "TA": x.TA,
                "FR": x.FR,
                "Temp": x.Temp,
                "Oxi": x.Oxi,
                "Recomendaciones": x.Recomendaciones,
                "id":x.id_historia
                }
            Hc.append(data)
        print(Hc)
        dataJson = json.dumps(Hc)
        resp = HttpResponse()
        resp.headers['Content-Type'] = "text/json"
        resp.content = dataJson
        return resp
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")
def newHC(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print(data)
            llave = paciente.objects.filter(no_cedula = data["no_cedula"]).first()
            if (not llave):
                return HttpResponseBadRequest("No existe paciente con esa cédula.")
            print(llave)
            print(llave.no_cedula)
            HC = historia_clinica(
                fecha_hora = data["fecha_hora"],
                diagnostico = data["diagnostico"],
                FC = data["FC"],
                TA = data["TA"],
                FR = data["FR"],
                Temp = data["Temp"],
                Oxi = data["Oxi"],
                Recomendaciones = data["Recomendaciones"],
                id_paciente = llave
            )
            HC.save()
            return HttpResponse("Nueva historia clinica generada agregado")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")

# acompañante
# CRUD acompañante
def newAcompanante(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print(data)
            llave = usuario.objects.filter(no_cedula = data["no_cedula"]).first()
            if (not llave):
                return HttpResponseBadRequest("No existe acompañante con esa cédula.")
            llavePac = paciente.objects.filter(id_paciente = data["id_paciente"]).first()
            if (not llavePac):
                return HttpResponseBadRequest("No existe paciente con esa.")
            Acompanante = acompanante(
                parentesco = data["parentesco"],
                no_cedula = llave,
                id_paciente = llavePac
            )
            Acompanante.save()
            return HttpResponse("Nuevo acompanante agregado")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")