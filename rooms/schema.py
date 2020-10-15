import graphene
from .types import RoomListResponse, RoomType
from .models import Room
from .queries import resolve_room, resolve_rooms


class Query(object):

    rooms = graphene.Field(RoomListResponse,
                           page=graphene.Int(),
                           resolver=resolve_rooms)
    room = graphene.Field(RoomType,
                          id=graphene.Int(required=True),
                          resolver=resolve_room)
