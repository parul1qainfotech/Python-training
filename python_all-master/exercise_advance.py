x=[
    {"name":"parul","age":20,"subject":"computer "},
    {"name":"rajat","age":19,"subject":"ar "},
    {"name":"radhika","age":21,"subject":"it "}
]
print(sorted(x,key=lambda i: i.get("age"),reverse=True))