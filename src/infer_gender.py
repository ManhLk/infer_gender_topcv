from src.utils import is_vietnamese
import string
import re

male_name, female_name = [], []

with open('src/male.txt', 'r') as f:
    male_name = f.readlines()
    male_name = [name.replace('\n', '').strip() for name in male_name]

with open('src/female.txt', 'r') as f:
    female_name = f.readlines()
    female_name = [name.replace('\n', '').strip() for name in female_name]

def get_fullname(name):
    name = name.lower()
    name = name.split()[0] if '.' in name else name.split()[-1]
    name = re.sub("["+string.punctuation+"]", '', name)
    return name.strip()

def infer_gender(name):
    name = get_fullname(name)
    if not is_vietnamese(name):
        return None
    if name in male_name:
        return 'male'
    if name in female_name:
        return 'female'
    return None

if __name__ == '__main__':
    name = 'duong N.'
    print(infer_gender(name))