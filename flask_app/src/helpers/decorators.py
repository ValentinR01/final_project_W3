from helpers.auth import AuthHandler
from models.domain import Domain
from models.role import Role


def rights_manager(request, role: str, domain: str = None):
    def decorator_rights_manager(func):
        def decorator(*args, **kwargs):
            if not request:
                token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NSwiZn" \
                        "VsbG5hbWUiOiJzYWxpbmUiLCJlbWFpbCI6InNhbGluZUBzYWxpb" \
                        "mUuY29tIiwicm9sZSI6IndvcmtlciIsImRvbWFpbiI6InJlZGFjd" \
                        "GlvbiIsImV4cCI6MTY5NzIyMDE2NSwiaWF0IjoxNjk0NjI4MTY1f" \
                        "Q.duieAudQgx8JGmWMdksZkgxL2kPdjd_J-64pUXq_Hqw"
            else:
                token = request.cookies.get('authorization')
            decode_token = AuthHandler.decode_token(token)

            role_list_endpoint = Role.get_all()
            # TODO mettre en cache les appels à la BDD
            role_list = []
            for roles in role_list_endpoint:
                role_list.append(roles.name)

            domain_list_endpoint = Domain.get_all()
            domain_list = []
            for domains in domain_list_endpoint:
                domain_list.append(domains.name)
            try:
                role_access_index = role_list.index(role)
            except ValueError:
                return {
                    "message": "Role passed to decorator doesn't exist"
                }, 404
            role_token_index = role_list.index(decode_token['role'])

            if not domain:
                if role_token_index < role_access_index:
                    return {"message": "unauthorized: the user hasn't "
                                       "the right"}, 401
                else:
                    return func(*args, **kwargs)

            if domain not in domain_list:
                return {
                    "message": "Domain passed to decorator doesn't exist"
                }, 404

            if role_token_index < role_access_index or decode_token['domain'] \
                    != domain and decode_token['role'] != "superadmin":
                return {"message": "unauthorized: the user hasn't "
                                   "the right"}, 401
            else:
                return func(*args, **kwargs)

        return decorator

    return decorator_rights_manager
