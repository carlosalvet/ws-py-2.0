import os
from pathlib import Path

class FileSystem:

    def __init__(self):
        print('hola desde filesystem')
    
    def file_get_contents(filename):
        print('[DEBUG]', 'Obteniendo contenido de archivo: ', filename, end=' ')
        contents = "";

        if os.path.isfile(filename):
            file = open(filename)
            if(file):
                contents = file.read()
                file.close()
            else: print(f'ERROR: El archivo no abre: {file}')
        else: print(f'Warning: El archivo no existe: {filename}')
        print('OK')

        return contents


    def file_put_contents(filepath, contents, new_line=False):
        nl = '\n' if new_line else ''
        print(f"[DEBUG] Inserting in : {filepath}, content: {contents}")
        try:
            if not os.access(filepath, os.W_OK):
                raise PermissionError("No write permissions for the file.")
            
            with open(filepath, 'a') as file:
                file.write(f'{nl}{contents}')
            return True
        except PermissionError as e:
            print(f"Permission denied: {str(e)}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
        return False
     


    def create_directory(path):
        success = True
        if not os.path.exists(path):
            success = os.makedirs(path, exist_ok=True)
        return success


    def create_file(filename):
        if Path(filename).is_file(): destroy_file(filename)

        with open(filename, 'x') as fp:
            print(f"[DEBUG] File created: {filename}")
            return True

        return False


    def destroy_file(filepath):
        try:
            os.remove(filepath)
            print("File deleted successfully.")
            return True
        except FileNotFoundError:
            print("")
        except PermissionError:
            print("Permission denied. Unable to delete the file.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

        return False


    """
	    Returns the nth lines before last line of a file (n=1 gives last line)
    """
    def read_n_to_last_line(filename, n = 1):
        num_newlines = 0
        with open(filename, 'rb') as f:
            try:
                f.seek(-2, os.SEEK_END)    
                while num_newlines < n:
                    f.seek(-2, os.SEEK_CUR)
                    if f.read(1) == b'\n':
                        num_newlines += 1
            except OSError:
                f.seek(0)
            last_line = f.readline().decode()
        return last_line
