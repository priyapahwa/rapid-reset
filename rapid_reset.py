import os
import shutil
import glob

flag = True

while flag:
    clean = input("Do you want to clean-up migration records and database? [y/n]: ")

    if clean == "y":
        print("Cleaning-up migration records and database...")

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        content = os.listdir(BASE_DIR)
        dirs = list()

        for dir in content:
            if os.path.isdir(os.path.join(BASE_DIR, dir)):
                dirs.append(dir)

        for dir in dirs:

            # delete __pycache__
            try:
                shutil.rmtree(os.path.join(BASE_DIR, dir, "__pycache__"))
                print("Removed: " + dir + " __pycache__")
            except Exception as e:
                pass

            # delete migrations __pycache__
            try:
                shutil.rmtree(os.path.join(BASE_DIR, dir, "migrations", "__pycache__"))
                print("Removed: " + dir + " migrations __pycache__")
            except Exception as e:
                pass

            # delete migrations
            try:
                dir_path = os.path.join(BASE_DIR, dir, "migrations")
                dir_content = os.listdir(dir_path)
                for file in dir_content:
                    if not file == "__init__.py":
                        os.remove(os.path.join(dir_path, file))
                        print("Removed: " + dir_path + " " + file)
            except Exception as e:
                pass

            # delete database
            try:
                for file in glob.glob("*.sqlite3"):
                    os.remove(file)
                    print("Removed: " + file)
            except Exception as e:
                pass

        print("Done!")
        flag = False

    elif clean == "n":
        print("Clean-up refused.")
        flag = False

    else:
        print("Invalid input.")

quit()
