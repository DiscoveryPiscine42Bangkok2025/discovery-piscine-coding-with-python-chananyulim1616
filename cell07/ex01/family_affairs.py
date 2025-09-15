dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

def find_the_redheads(dupont_family: dict) -> list:
    #use filters
    return list(filter(lambda name: dupont_family[name] == "red", dupont_family.keys()))
print(find_the_redheads(dupont_family))