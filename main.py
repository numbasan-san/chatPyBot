import procesomientos, time, os

print ("#########################################################\n" + 
       "/*------------------Chat Bot del ITLA------------------*/" + 
       "\n#########################################################\n" + 
       "\nSi necesita saber algo respecto al funcionamiento del \n" + 
       "programa, escriba !help para que vea todos los comandos \n"+
       "de operación.\n\n")

while True:
    
    input_user = input ("Tu: ")

    if input_user == "!help":
        print ("__________________________________________________\n\n" + 
            "/*-------------Comandos del chatbot-------------*/\n\n" + 
            "!help para consultar los comandos de ayuda.\n" + 
            "!exit para salir.\n" + 
            "!manual para saber cómo hablar con Mirko.\n" + 
            "!credit para saber quien hizo a Mirko.\n" +
            "!play para poder jugar tres en raya con Mirko.\n" + 
            "__________________________________________________\n")

    elif input_user == '!exit':
        print ("________________\n\n" + 
               'Chatbot cerrado.\n' + 
               "________________\n")
        time.sleep(3)
        break

    elif input_user == '!manual':
        print ("__________________________________________________\n\n" + 
            "/*------------------Manual------------------*/\n\n" + 
            "Debe escribir las preguntas que tenga al bot, \n" +
            "si el bot conoce la respuesta contestará, \n" + 
            "de lo contrario reconocerá que no entiende.\n" + 
            "__________________________________________________\n")

    elif input_user == '!credit':
        print ("_________________________________\n\n" + 
            "Creador: Eddy Manuel Peña Ortega.\n" + 
            "_________________________________\n")

    elif input_user == '!play':
        os.system ("python threeInLine.py")
            
    else:
        print ("Mirko: " + procesomientos.get_response (input_user))