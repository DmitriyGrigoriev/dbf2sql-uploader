import json
import logging
from dramatiq.middleware import Middleware

LOGGER = logging.getLogger("django_dramatiq.ImportTablesAdminMiddleware")


class ImportTablesAdminMiddleware(Middleware):
    """This middleware update ImportTable.message_id field.
    """
    def update_message_id(self, message):
        from src.apps.core.models import ImportTables

        message_data = json.loads(message.encode().decode('utf-8'))
        message_data.update({"message_id": message.message_id})

        if 'kwargs' in message_data and 'table_pk' in message_data['kwargs']:
            table_pk = message_data['kwargs']['table_pk']
            message_id = message_data['message_id']
            redis_message_id = message_data['options']['redis_message_id']
            record_to_update = ImportTables.tables.filter(pk=table_pk)
            record_to_update.update(message_id=message_id, redis_message_id=redis_message_id)

    def after_enqueue(self, broker, message, delay):
        self.update_message_id(message=message)

    def before_process_message(self, broker, message):
        self.update_message_id(message=message)

    def after_skip_message(self, broker, message):
        self.after_process_message(broker, message)

    def after_process_message(self, broker, message, *, result=None, exception=None):
        self.update_message_id(message=message)
