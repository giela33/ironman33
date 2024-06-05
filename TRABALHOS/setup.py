# pip install cx_freeze
import cx_Freeze
executaveis = [ 
                cx_Freeze.Executable(script="main.py")]
cx_Freeze.setup(
    name = "PNGS IRONMAN",
    options={
        "build_exe":{
            "packages":["pygame"],
            "include_files":["assets"]
        }
    }, executables = executaveis
)


# python setup.py build
# puthon setup.py bdist_msi