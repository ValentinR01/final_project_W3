from helpers.auth import AuthHandler

import logging


def rights_manager(token: str, role: str, domain: str):
    def decorator_rights_manager(func):
        def decorator(*args, **kwargs):
            decode_token = AuthHandler.decode_token(token)
            logging.info(f'---------------- le token en clair : {decode_token}')
            logging.info(f'---------------- role : {role}; domain: {domain}')

            if decode_token['role'] != role or decode_token['domain'] != domain:
                logging.error(f'------ The user is not authorized. '
                              f'The role required is {role}, and the domain '
                              f'required is :{domain} and the user role is :'
                              f'{decode_token["role"]} and the user domain is'
                              f' {decode_token["domain"]}')
                return {"message": "unauthorized : the user hasn't "
                                   "the right"}, 401
            else:
                return func(*args, **kwargs)
        return decorator
    return decorator_rights_manager
