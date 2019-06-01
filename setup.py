from cx_Freeze import setup, Executable


setup(
    name = 'jpo-demo',
    version = '1.0',
    options = {"build_exe":{"packages": [
                                         "tkinter",
                                         "os",
                                         "sys",
                                         "json",
                                         "cv2"
                                         ],
                            "include_files": ['icon.ico',
                                                "logical.py",
                                                "config.py"]

                            }

                },
    description = "jpo-demo",
    executables = [Executable('main.py', icon='icon.ico')]
)