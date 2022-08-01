import getpass
import json
from typing import Dict, Any
from django.utils.translation import gettext_lazy as _
from pydantic import BaseSettings, validator, root_validator


class Settings(BaseSettings):
    uid: str = ''
    pwd: str = ''
    dumps: str = ''

    def make_connection_string(self):
        raise NotImplementedError('subclasses of Settings may require a make_connection_string() method')

    class Config:
        case_sensitive = False
        env_file = './var/.env'
        env_file_encoding = 'utf-8'
        validate_assignment: bool = True


    @root_validator(pre=False)
    def to_json(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        """Encode to json format"""
        cls.dumps = json.dumps(values, ensure_ascii=False, indent=2)
        return values


    def check_credentials(self, uid=None, pwd=None):
        if uid is None and len(self.uid) > 0:
            uid = self.uid

        if uid is None:
            raise ValueError(_('User ID is required for connection!'))

        if pwd is None:
            pwd = getpass.getpass(_("Password for ") + uid + " :")
            self.pwd = pwd

        try:
            assert isinstance(uid, str)
            self.uid = uid
            assert isinstance(pwd, str)
            self.pwd = pwd
        except:
            raise ValueError(_('uid/pwd entry must be string!'))


class OdbcDrivers(Settings):
    driver: str = 'ODBC Driver 18 for SQL Server'
    server: str = 'localhost'
    database: str = None
    trusted_connection: str = 'yes'
    trust_server_certificate: str = 'yes'

    class Config:
        env_prefix = 'ODBC_'


class DataSources(Settings):
    dsn: str = ''

    class Config:
        env_prefix = 'DSN_'

    @validator('dsn')
    def dsn_empty(cls, v):
        if not v:
            raise ValueError(_("Property dsn has not be empty"))
        return v


    def make_connection_string(self):
        try:
            connection_string = f"DSN={self.dsn};" \
                                f"UID={self.uid};" \
                                f"PWD={self.pwd};"


        except ValueError as e:

            raise e

        return connection_string


class AdvanatageVisualFoxpro(OdbcDrivers):
    driver: str = 'Advantage StreamlineSQL ODBC'
    data_directory: str = ''
    server: str = 'NotTheServer'
    сompression: str = ''
    default_type: str = 'Visual FoxPro'
    rows: bool = False # Show deleted rows
    language: str = 'ANSI'
    advantage_locking: str = 'ON'
    locking: str = 'Record'
    trim_trailing_space: bool = True
    uid: str = 'adssys'
    pwd: str = ''
    encoding: str = ''

    class Config:
        env_prefix = 'VFP_'

    # @validator('data_directory')
    # def data_directory_empty(cls, v):
    #     if not v:
    #         raise ValueError(_("Property data_directory has not be empty"))
    #     return v

    def make_connection_string(self):
        try:
            connection_string = f"DRIVER={{{self.driver}}};" \
                                f"DataDirectory={self.data_directory};" \
                                f"SERVER={self.server};" \
                                f"Compression={self.сompression};"\
                                f"DefaultType={self.default_type};" \
                                f"Rows={self.rows};" \
                                f"Language={self.language};" \
                                f"AdvantageLocking={self.advantage_locking};" \
                                f"Locking={self.locking};" \
                                f"TrimTrailingSpace={self.trim_trailing_space};" \
                                f"UID={self.uid};" \
                                f"Password={self.pwd};"

        except ValueError as e:

            raise e

        return connection_string


class AdvanatageClipper(AdvanatageVisualFoxpro):
    default_type: str = 'Clipper'
    language: str = 'OEM'
    advantage_locking: str = 'OFF' # Compatible
    max_table_close_cache: int = 5
    server_types: int = 6
    memo_block_size: int = 64

    class Config:
        env_prefix = 'CLI_'


    def make_connection_string(self):
        try:
            connection_string = f"DRIVER={{{self.driver}}};" \
                                f"DataDirectory={self.data_directory};" \
                                f"SERVER={self.server};" \
                                f"Compression={self.сompression};"\
                                f"DefaultType={self.default_type};" \
                                f"Rows={self.rows};" \
                                f"Language={self.language};" \
                                f"AdvantageLocking={self.advantage_locking};" \
                                f"Locking={self.locking};" \
                                f"MemoBlockSize={self.memo_block_size};" \
                                f"TrimTrailingSpace={self.trim_trailing_space};" \
                                f"UID={self.uid};" \
                                f"Password={self.pwd};"

        except ValueError as e:

            raise e

        return connection_string


# class AdsDirectoryTable(OdbcDrivers):
#     conn_type: int = Field(default=AdsType().conn_type, env='CONN_TYPE')
#     driver: str = 'Advantage StreamlineSQL ODBC'
#     data_directory: str = ''
#     server: str = 'NotTheServer'
#     сompression: str = ''
#     default_type: str = 'Clipper'
#     rows: bool = False # Show deleted rows
#     language: str = 'ANSI'
#     advantage_locking: str = 'OFF' # Compatible
#     locking: str = 'Record'
#     max_table_close_cache: int = 5
#     server_types: int = 6
#     memo_block_size: int = 64
#     trim_trailing_space: bool = True
#     uid: str = 'adssys'
#     pwd: str = ''
#
#     class Config:
#         env_prefix = 'ADS_'
#
#     @validator('conn_type')
#     def conn_type_match(cls, v):
#         if v != 4:
#             raise ValueError("Incorrect connection type value for ADS")
#         return v
#
#     @validator('data_directory')
#     def data_directory_empty(cls, v):
#         if not v:
#             raise ValueError("DATA_DIRECTORY has to not be empty")
#         return v


# class FoxproTable(OdbcSettings):
#     conn_type: int = Field(default=DbfType().conn_type, env='CONN_TYPE')
#     driver: str = 'Advantage StreamlineSQL ODBC'
#     source_type: str = 'DBF'
#     default_type: str = 'FoxPro'
#     collate: str = 'Machine'
#     exclusive: str = 'No'
#     deleted: str = 'Yes'
#     source_db: str = ''
#     is_null: str = 'No'
#
#     class Config:
#         env_prefix = 'DBF_'
#
#     @validator('conn_type')
#     def conn_type_match(cls, v):
#         if v != 3:
#             raise ValueError("Incorrect connection type value for DBF")
#         return v
#
#     @validator('source_db')
#     def source_db_empty(cls, v):
#         if not v:
#             raise ValueError("Source_db has to not be empty")
#         return v

# class AdvantageOLEProvider(OdbcSettings):
#     conn_type: int = Field(default=AdsType().conn_type, env='CONN_TYPE')
#     provider: str = 'Advantage OLE DB Provider'
#     security_mode: str = 'ADS_IGNORERIGHTS'
#     server_type: str = 'ADS_LOCAL_SERVER'
#     table_type: str = 'ADS_ADT'
#     char_type: str = 'ADS_OEM'
#     lock_mode: str = 'ADS_COMPATIBLE_LOCKING'
#     data_source: str = ''
#     user_id: str = ''
#     password: str = ''
#
#     class Config:
#         env_prefix = 'ADS_'
#
#     @validator('conn_type')
#     def conn_type_match(cls, v):
#         if v != 4:
#             raise ValueError("Incorrect connection type value")
#         return v
#
#     @validator('server_type')
#     def server_type_match(cls, v):
#         if v not in ['ADS_LOCAL_SERVER', 'ADS_REMOTE_SERVER']:
#             raise ValueError("Server type value must be only ADS_LOCAL_SERVER or ADS_REMOTE_SERVER")
#         return v
#
#     @validator('data_source')
#     def source_db_empty(cls, v):
#         if not v:
#             raise ValueError("Data_source has not to be empty")
#         return v
