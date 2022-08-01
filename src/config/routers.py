import threading

env = threading.local()


def get_context_account():
    if hasattr(env, 'context_account'):
        return env.context_account
    return None


class UploadDbRouter(object):
    def _is_internal(self, model):
        return model.__module__.startswith('my_app')

    def _is_global(self, model):
        return hasattr(model, 'is_global') and model.is_global

    def _get_db(self, model):
        if self._is_internal(model):
            if self._is_global(model):
                return 'default'
            else:
                context_account = get_context_account()
                if context_account:
                    return context_account.get_database_name()
                return None
        return 'default'

    def db_for_read(self, model, **hints):
        return self._get_db(model)

    def db_for_write(self, model, **hint):
        return self._get_db(model)

    def allow_relation(self, obj1, obj2, **hints):
        return obj1._state.db == obj2._state.db

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if db == 'default':
            if app_label == 'app' and model_name != 'account':
                return False
            if app_label in ['auth']:
                return False
        else:
            if app_label == 'app' and model_name == 'account':
                return False
            if app_label in ['sites', 'sessions']:
                return False
        return True