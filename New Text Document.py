import subprocess



while True:
    try:

        command = input("> ");
        if command.lower() == "stop":
            break
        subprocess.run(command)
    except Exception:
        print("error")
    
