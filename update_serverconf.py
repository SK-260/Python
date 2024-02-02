
def update_server_config(file_path,key, value):
    # Read the existing content of server config file
    with open(file_path, "r") as file:
        lines = file.readlines()
        file.close()
    # Update the config file for the specific key
    with open(file_path, "w") as file:
        for line in lines:
            # check if line starts with key
            if key in line:
                # Update the line with new value
                file.write(f"{key}={value}\n")
            else:
                # Keep the existing line as it is
                file.write(line)
        file.close()

# Path to server configuration file
server_config_file = "server.conf"

# Key and value for updating file
key_to_update = "MAX_CONNECTIONS"
new_value = "1000"


update_server_config(server_config_file, key_to_update,new_value)
