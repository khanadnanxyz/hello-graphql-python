import json

import graphene


class Query(graphene.ObjectType):
    hello = graphene.String()
    is_active = graphene.Boolean()

    def resolve_hello(self, info):
        return "world"

    def resolve_is_active(self, info):
        return True


# override with auto_camelcase / must follow convention of camelCase
schema = graphene.Schema(query=Query, auto_camelcase=False)

result = schema.execute(
    '''
    {
        is_active
    }
    '''
)


dictResult = dict(result.data.items())
finalResult = json.dumps(dictResult, indent=2)
print(finalResult)
