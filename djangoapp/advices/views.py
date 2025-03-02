import requests
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Advice
from .serializers import AdviceSerializer
from rest_framework.permissions import IsAuthenticated

# Pegando conselho aleatório
@api_view(['GET'])
def random_advice(request):
    response = requests.get('https://api.adviceslip.com/advice')
    
    if response.status_code == 200:
        advice_data = response.json()
        advice = advice_data['slip']['advice']
        soltar = Advice.objects.create(advice=advice)
        serializer = AdviceSerializer(soltar)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response({'error': 'Falha ao buscar conselho'}, status=status.HTTP_400_BAD_REQUEST)


# Cria um conselho
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_advice(request):
    if request.method == 'POST':
        if 'advice' in request.data:
            advice = request.data['advice']
            if Advice.objects.filter(advice=advice).exists():
                return Response({"error": "Esse conselho já existe!"}, status=status.HTTP_400_BAD_REQUEST)
            soltar = Advice.objects.create(advice=advice)
            serializer = AdviceSerializer(soltar)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "É obrigatório passar um conselho."}, status=status.HTTP_400_BAD_REQUEST)


# Listar todos os conselhos
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_advices(request):
    soltar = Advice.objects.all()
    serializer = AdviceSerializer(soltar, many=True)
    return Response(serializer.data)


# Pegando conselho por ID
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_advice_id(request, pk):
    try:
        soltar = Advice.objects.get(pk=pk)
        serializer = AdviceSerializer(soltar)
        return Response(serializer.data)
    except Advice.DoesNotExist:
        return Response({'error': 'Conselho não encontrado'}, status=status.HTTP_404_NOT_FOUND)

# Atualizar conselho por ID
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_advice(request, pk):
    try:
        soltar = Advice.objects.get(pk=pk)
    except Advice.DoesNotExist:
        return Response({'error': 'Conselho não encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    if 'advice' in request.data:
        new_advice = request.data['advice']
        if Advice.objects.filter(advice=new_advice).exclude(pk=pk).exists():
            return Response({'error': 'Esse conselho já existe, mude para outro.'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = AdviceSerializer(soltar, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Deletar conselho por ID
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_advice(request, pk):
    try:
        advice = Advice.objects.get(pk=pk)
    except Advice.DoesNotExist:
        return Response({'error': 'Conselho não encontrado'}, status=status.HTTP_404_NOT_FOUND)

    advice.delete()
    return Response({'message': 'Conselho deletado com sucesso!'}, status=status.HTTP_202_ACCEPTED)