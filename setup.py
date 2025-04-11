from setuptools import setup, find_packages
from typing import List


BAR_E_DOT = '-e .'
# Create function that fetch all packages from requirements.txt
def packages(file_name:str) -> List[str]:
    
    requirements = []
    with open(file_name) as file_obj:
        # Read all lines from requirements.txt and store them in a list
        requirements = file_obj.readlines()
        
        # Replace /n with empty string
        requirements = [req.replace("\n", "") for req in requirements]
        
        if BAR_E_DOT in requirements:
            requirements.remove(BAR_E_DOT)
        
        return requirements
        
        

# Set Setup Parameters
setup(
    name = "Demo Project",
    version = "0.1.0",
    author = "Abu Bakar",
    author_email = "abubakarrajput6947@gmail.com",
    description = "This is a demo project",
    packages = find_packages(),
    install_requires = packages('requirements.txt'),
)