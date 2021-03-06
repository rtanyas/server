from controler.registration import registration, check_user
from controler.authorization import authorization
from controler.task import create_task, edit_task, grant_access, deny_access, assign_performer, remove_performer, \
    change_status, create_comment, delete_comment
import serv.shortcuts as shortcuts

TYPE = {
    'action': 'pass',
    'action': 'action'

}
NAME = {
    'registration': registration,
    'authorization': authorization,
    'check_user': check_user,
    'create task': create_task,
    'edit task': edit_task,
    'grant access': grant_access,
    'deny access': deny_access,
    'assign performer': assign_performer,
    'remove performer': remove_performer,
    'change status': change_status,
    'create comment': create_comment,
    'delete comment': delete_comment
}


class CControler:

    @classmethod
    def handle(cls, request):
        try:

            if request['head']['type'] in TYPE and request['head']['name'] in NAME:
                controller = NAME.get(request['head']['name'])

                if 'session id' not in request['head']:
                    return controller(request['body'])
                else:
                    return controller(request['body'], request['head']['session id'])

            else:
                print('unknown_request')
                return shortcuts.unknown_request
        except Exception as err:
            print(err)
            return shortcuts.internal_server_error(err)
