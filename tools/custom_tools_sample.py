from langchain.tools import tool


@tool
def greeting_func(name:str)->str:
    """Generate a greeting message to the user"""
    return f"Hello {name} ! How do u do!"



result=greeting_func.invoke({"name":"Bhoomika"})
print(result)


print("name is:" , greeting_func.name)
print("args are" , greeting_func.args)
print("Description is:" , greeting_func.description)