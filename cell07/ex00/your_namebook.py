def array_of_names(dic:dict) -> dict:
    #captialze keys and values
    ls = []
    for key, value in dic.items():
        ls.append(f"{key.capitalize()} {value.capitalize()}")
    return ls
persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}
print(array_of_names(persons))