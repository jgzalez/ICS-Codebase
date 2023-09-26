import psutil

av_list = ["calc"]

# Busca y termina procesos
for process in psutil.process_iter(attrs=["pid", "name"]):
    for name in av_list:
        if name.lower() in process.info["name"].lower():
            try:
                process.terminate()
                print(
                    f"Proceso {process.info['name']} ({process.info['pid']}) terminado con éxito."
                )
            except Exception as e:
                print(
                    f"No se pudo terminar el proceso {process.info['name']} ({process.info['pid']}): {e}"
                )
