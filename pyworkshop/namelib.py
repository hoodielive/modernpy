def upper_case_name(name):
    return name.upper() 

name = "Larry"

upper_name = upper_case_name(name)

if __name__ == "__main__":
    name = "Larry"
    upper_name  = upper_case_name(name)
    print(f"dunder name", __name__)
