class Notificador():
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje
    
    def Notificar(self):
        raise NotImplementedError

class NotificadorPorEmail(Notificador):
    def Notificar(self):
        print(f'Enviando mensaje por Mail a {self.usuario.mail}')

class NotificadorPorTwitter(Notificador):
    def Notificar(self):
        print(f'Enviando mensaje por Twit a {self.usuario.twit}')

class NotificadorPorTelegram(Notificador):
    def Notificar(self):
        print(f'Enviando mensaje por Telegram a {self.usuario.telegram}')

#Agrega funcionalidad al código sin modificar clases, sino agregando más