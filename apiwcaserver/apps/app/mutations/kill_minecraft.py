import graphene
import os


class KillMinecraft(graphene.Mutation):
    status = graphene.Boolean()

    def mutate(self, info):
        result = str(os.popen("ps -ef | grep server.jar | grep -v grep | awk '{printf $2}'").read())
        os.popen("kill -9 " + result)
        return KillMinecraft(status=True)
