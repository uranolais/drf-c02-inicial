import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from faker import Faker
from random import choice
from escola.models import Curso

def criar_cursos(quantidade_de_cursos):
    fake = Faker('pt_BR')
    niveis = ['B', 'I', 'A']

    for _ in range(quantidade_de_cursos):
        codigo = fake.unique.random_number(digits=3)
        descricao = fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
        nivel = choice(niveis)
        Curso.objects.create(codigo=codigo, descricao=descricao, nivel=nivel)

criar_cursos(3)
