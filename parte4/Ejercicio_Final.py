from textblob import TextBlob

class AnalizadorDeSentimientos:
    def analizar_sentimiento(self, text):
        analisis = TextBlob(text)
        if analisis.sentiment.polarity > 0:
            return 'Positivo'
        elif analisis.sentiment.polarity == 0:
            return 'Neutro'
        else:
            return 'Negativo'

analizador = AnalizadorDeSentimientos()
resultado = analizador.analizar_sentimiento('')#Inserta texto en inglés para analizarlo
print(resultado)