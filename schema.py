import json

import graphene


class Query(graphene.ObjectType):
    hello = graphene.String()

    def resolve_hello(self, info):
        return "world"


schema = graphene.Schema(query=Query)

result = schema.execute(
    '''
    {
        hello
    }
    '''
)

dictResult = dict(result.data.items())
finalResult = json.dumps(dictResult)
print(finalResult)
