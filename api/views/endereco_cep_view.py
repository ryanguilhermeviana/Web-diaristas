from rest_framework.views import APIView
from ..services import cidades_atendimento_service


class EnderecoCep(APIView):
    def get(self, request, format=None):
        cep = self.request.query_params.get('cep', None)
        endereco = cidades_atendimento_service.buscar_cidade_cep(cep)
        