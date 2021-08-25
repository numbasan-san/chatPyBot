import procesomientos, random

def check_all_messages (message):
    highest_prob = {}

    def response (bot_response, list_of_words, single_response = False, required_words = []):
        nonlocal highest_prob
        highest_prob [bot_response] = procesomientos.message_probability (message, list_of_words, single_response, required_words)

    response ('Hola.', ['hola', 'hello', 'salutaciones', 'buenas'], single_response = True)
    response ('De nada.', ['gracias', 'thanks'], single_response = True)
    response ('Estoy bien, gracias.', ['estas', 'estás', 'vas', 'andas'], single_response = True, required_words = ['como', "cómo"])
    response ('Estamos en la Autopista Las Américas, Km. 27, PCSD, La Caleta, Boca Chica.', ['ubicados', 'ubicado', 'ubicacion', 'ubicación', 'posición', 'posicion', 'posicionados', 'localidad', 'localizados', 'direccion', 'dirección'], single_response = True)
    response ('Fue un placer servir. Tenga un buen día.', ['adios', 'despido', 'cuidate'], single_response = True)
    response ('Éstos son nuestros números: 809-738-4852 / 809-793-2557. \nÉste es nuestro coreo electrónico: info@itla.edu.do', ['contactos', 'contacto', 'numeros', 'números', 'correo'], single_response = True, required_words = ['cual', 'cuál', 'cuales'])
    response ('Las carreras que ofrece el ITLA son las siguientes: \n' + 
              'Tecnología en Desarrollo de Software,\n' + 
              'Tecnología en Redes de Información,\n' + 
              'Tecnología en Seguridad Informática,\n' + 
              'Tecnología en Multimedia,\n' + 
              'Tecnología en Sonido,\n' + 
              'Tecnología en Mecatrónica,\n' + 
              'Tecnología en Manufactura Automatizada,\n' + 
              'Tecnología en Diseño Industrial,\n' + 
              'Tecnología en Manufactura de Dispositivos Médicos,\n' + 
              'Tecnología en Inteligencia Artificial,\n' + 
              'Tecnología en Telecomunicaciones,\n' + 
              'Tecnología en Analítica y Ciencia de los Datos,\n' + 
              'Tecnología en Informática Forense,\n' + 
              'Tecnología en Energías Renovables,\n' + 
              'Tecnología en Simulaciones Interactivas y Videojuegos.', ['carreras', 'estudiar'], single_response = True)
    response ('Nuestras horas laborales son de 08:00-16:00. \nRespecto a las clases es de 08:00-22:00.', ['horas', 'hora', 'abren', 'abre', 'cierran', 'cierra', 'horario'], single_response = True)
    response ('El valor de cada crédito es de 1, 500$RD.', ['cuesta', 'coste', 'valen', 'crédito', 'creditos', 'credito', 'créditos'], single_response = True)
    response ('Las carreras pueden durar hasta 7 cuatrimestres.', ['duración', 'dura', 'duran', 'tiempo', 'cuatrimestres', 'carrera'], single_response = True)
    response ('En ese caso escribe !play para jugar juntos.', ['jugar', 'juego', 'aburrido'], single_response = True)
    
    best_match = max (highest_prob, key = highest_prob.get)

    return unknown () if highest_prob [best_match] < 1 else best_match

def unknown ():
    response = ['¿Lo puedes repetir?', 
    "No te entiendo.", 
    "Busca en internet, quizás encuentras lo que estés buscando.", 
    "Si intentas usar un comando creo que haces algo mal.\nUsa !help para ver cuál comando buscas.", 
    "Por favor, reformula tu pregunta, no entiendo \nlo que me dices."] [random.randrange(5)]

    return response