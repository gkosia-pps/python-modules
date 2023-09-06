from jinja2 import Environment, FileSystemLoader

env_str  = Environment()


# {{ var }}: when rendering will replace the key passed with value
template_str = env_str.from_string("Hello {{name}}")
templ_str = template_str.render(name="Gav")
print(templ_str)
## ********************************************************

env_file = Environment(loader = FileSystemLoader("."))
template_file = env_file.get_template("07_jinja2_text.tmpl")

file_str = template_file.render(
     name="Zac"
    ,time = "2023-01-01 15:00:00"
    ,age= 45
    ,loop_ex = [
         {"name": "gav", "age": 35}
        ,{"name": "zac", "age": 27}
    ]

)
print(file_str)                       
