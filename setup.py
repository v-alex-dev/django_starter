from setuptools import setup, find_packages

setup(
    name='django_starter',                 # Le nom de ton package
    version='0.1.0',                       # La version initiale de ton package
    packages=find_packages(),              # Trouve automatiquement tous les packages
    install_requires=[                    # Les dépendances nécessaires
        'django',
        'python-decouple',
    ],
    entry_points={                        # Point d'entrée pour exécuter le script
        'console_scripts': [
            'django-starter=django_starter.cli:main',  # commande `django-starter` appelle la fonction main dans cli.py
        ],
    },
    include_package_data=True,             # Inclut les fichiers supplémentaires (README, LICENSE, etc.)
    long_description=open('README.md').read(),  # Lis le README pour une description longue
    long_description_content_type='text/markdown',  # Spécifie le type de contenu du README
    author='Ton Nom',                     # Ton nom
    author_email='ton_email@example.com',  # Ton email
    url='https://github.com/toncompte/django_starter',  # Lien vers le dépôt GitHub (si tu en as un)
    classifiers=[                          # Classificateurs pour décrire ton package
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',               # Version minimale de Python
)
