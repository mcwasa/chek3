import random

def generate_random_user_agent():
    versions = [
        random.randint(9, 11),
        random.randint(99, 149),
        random.randint(4500, 4999),
        random.randint(35, 99),
        random.randint(99, 175),
        random.randint(0, 5),
        random.randint(0, 5)
    ]

    user_agent = f"Mozilla/5.0 (Windows NT 10.0; {versions[0]}; Win64; x64){chr(random.randint(97, 122))}{chr(random.randint(65, 90))}{chr(random.randint(97, 122))}) AppleWebKit/537.36 (KHTML, like Gecko){versions[1]}.0.{versions[2]}.{versions[3]} Chrome/{versions[4]}.0.{versions[5]}.{versions[6]} Safari/537.36"
    
    return user_agent

random_user_agent = generate_random_user_agent()
print(random_user_agent)
