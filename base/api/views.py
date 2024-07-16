from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from .serializers import RoomSerializer

#function bases views we use @api_view
@api_view(['GET'])
#shows all routes in our api
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id'
    ]
    return Response(routes) 


@api_view(['GET'])
def getRooms(request):
    rooms=Room.objects.all() #objects cannot be converted to JSON data i.e we use serializers
    serializer = RoomSerializer(rooms, many=True) #many tells if there are many objects we are serialisizng
    return Response(serializer.data)

@api_view(['GET'])
def getRoom(request, pk):
    room=Room.objects.get(id=pk)
    serializer = RoomSerializer(room, many=False) #many is false as we fetching only a single room
    return Response(serializer.data)