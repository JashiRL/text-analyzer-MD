import os
from analyzer import file_loader, smart_analyzer, topic_detector, visualizations

def menu():
    text = ""
    last_sentiment_result = None  # Guardar último resultado de sentimientos

    while True:
        print("\n=== Menú de Análisis de Texto ===")
        print("1. Cargar archivo (desde carpeta 'data' o Finder)")
        print("2. Análisis de sentimientos (inteligente)")
        print("3. Resumen (inteligente)")
        print("4. Detectar tema")
        print("5. Visualizaciones")
        print("6. Salir")

        option = input("Seleccione una opción: ")

        if option == "1":
            print("\n¿Deseas cargar un archivo desde la carpeta 'data' o desde el Finder?")
            print("1. Elegir desde la carpeta 'data'")
            print("2. Seleccionar desde el Finder")
            suboption = input("Seleccione una subopción (1 o 2): ")

            filepath = None
            if suboption == "1":
                filepath = file_loader.select_file_from_list("data")
            elif suboption == "2":
                filepath = file_loader.open_file_dialog()
            else:
                print("Opción no válida.")

            if filepath and os.path.isfile(filepath):
                try:
                    text = file_loader.load_file(filepath)
                    print(f"\nTexto cargado (primeros 500 caracteres):\n{text[:500]}")
                    last_sentiment_result = None  # Reiniciar análisis previo al cargar nuevo texto
                except Exception as e:
                    print(f"Error al leer el archivo: {e}")
            elif filepath and os.path.isdir(filepath):
                try:
                    texts = file_loader.load_files_from_folder(filepath)
                    text = "\n".join(texts)
                    print(f"\nSe cargaron {len(texts)} archivos. Muestra:\n{text[:500]}")
                    last_sentiment_result = None
                except Exception as e:
                    print(f"Error al leer archivos de la carpeta: {e}")
            else:
                print("No se pudo cargar el archivo.")

        elif option == "2":
            if not text:
                print("Primero cargue un texto.")
                continue
            result = smart_analyzer.analyze_sentiment_smart(text)
            last_sentiment_result = result
            print(f"\nAnálisis de Sentimientos ({result.get('method', '')}):")

            if "error" in result:
                print(result["error"])
            elif "summary" in result:
                for emotion, pct in result["summary"].items():
                    print(f"{emotion}: {pct}%")
                visualizations.plot_sentiment_distribution(result["summary"])
            elif "emotion" in result:
                print(f"Emoción: {result['emotion']}, Confianza: {result.get('confidence', result.get('score', 0))}%")

        elif option == "3":
            if not text:
                print("Primero cargue un texto.")
                continue
            summary = smart_analyzer.summarize_text_smart(text)
            print(f"\nResumen:\n{summary}")

        elif option == "4":
            if not text:
                print("Primero cargue un texto.")
                continue
            topic = topic_detector.extract_main_topic(text)
            print(f"\nTema principal: {topic}")

        elif option == "5":
            if not text:
                print("Primero cargue un texto.")
                continue

            while True:  # Submenú visualizaciones
                print("\n--- Visualizaciones Disponibles ---")
                print("1. Frecuencia de palabras")
                print("2. Distribución de longitud de palabras")
                print("3. Nube de palabras")
                print("4. Gráfico de sentimientos (requiere análisis previo)")
                print("5. Volver al menú principal")

                subopt = input("Seleccione una opción (1-5): ")

                if subopt == "1":
                    visualizations.plot_word_frequency(text)
                elif subopt == "2":
                    visualizations.plot_word_distribution(text)  # o plot_word_length_distribution según tu código
                elif subopt == "3":
                    visualizations.generate_wordcloud(text)
                elif subopt == "4":
                    if isinstance(last_sentiment_result, dict) and "summary" in last_sentiment_result:
                        visualizations.plot_sentiment_distribution(last_sentiment_result["summary"])
                    else:
                        print("No hay datos de sentimientos disponibles. Ejecute primero el análisis de sentimientos.")
                elif subopt == "5":
                    print("Regresando al menú principal...")
                    break
                else:
                    print("Opción no válida.")

        elif option == "6":
            print("Saliendo...")
            break

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
