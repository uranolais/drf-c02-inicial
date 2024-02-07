from rest_framework import serializers
from escola.models import Estudante, Curso, Matricula

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id','nome','email','cpf','data_nascimento','celular']
    
    def validate_cpf(self, cpf):
        if len(cpf) != 11:
            raise serializers.ValidationError({'cpf':'O CPF deve ter 11 dígitos'})
        return cpf
    

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []

# localhost:8000/estudante/1/matriculas
class ListaMatriculasEstudanteSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()#To vendo se ainda vou usar isso daqui
    class Meta:
        model = Matricula
        fields = ['curso','periodo']
    def get_periodo(self, obj):
        return obj.get_periodo_display()
    # get_<nome_do_campo>_display() https://docs.djangoproject.com/pt-br/4.2/ref/models/instances/#extra-instance-methods

# localhost:8000/curso/1/matriculas
class ListaMatriculasCursoSerializer(serializers.ModelSerializer):
    estudante_nome = serializers.ReadOnlyField(source = 'estudante.nome')
    class Meta:
        model = Matricula
        fields = ['estudante_nome',]

