import uuid
from datetime import datetime
import json

import graphene


class User(graphene.ObjectType):
    id = graphene.ID(default_value=str(uuid.uuid4()))
    username = graphene.String()
    created_at = graphene.DateTime(default_value=datetime.now())


class Query(graphene.ObjectType):
    users = graphene.List(User, limit=graphene.Int())
    hello = graphene.String()
    is_active = graphene.Boolean()

    def resolve_hello(self, info):
        return "world"

    def resolve_is_active(self, info):
        return True

    def resolve_users(self, info, limit=None):
        users = [
            User(id=1, username='joker', created_at=datetime.now()),
            User(id=2, username='heath', created_at=datetime.now())
        ]
        return users[:limit]


class CreateUsser(graphene.Mutation):
    user = graphene.Field(User)

    class Arguments:
        username = graphene.String()

    def mutate(self, info, username):
        user = User(username=username)
        return CreateUsser(user=user)


class Mutation(graphene.ObjectType):
    create_user = CreateUsser.Field()


# override with auto_camelcase / must follow convention of camelCase
schema = graphene.Schema(query=Query, auto_camelcase=False, mutation=Mutation)

result = schema.execute(
    '''
    mutation {
        create_user(username: "khan") {
           user { 
                id
                username
                created_at
            }
        }
    }
    '''
)

dictResult = dict(result.data.items())
finalResult = json.dumps(dictResult, indent=2)
print(finalResult)
