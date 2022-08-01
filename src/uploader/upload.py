import pyodbc
import struct
import tablib
import json
import datetime
import math
from src.db.connection.connects import AdvantageClipperConnect
# from connection.tables import AdsTables
# # from bulkxmlload.schema import XSDSchema
# from bulkxmlload.xsdschema import XSDSchema
# from bulkxmlload.xmldata import XMLData
from pydantic import ValidationError

server = 'NTB000250'
database = 'PaidData'
username = 'dimag'
password = 'DiGGma54'
conn_string = 'DRIVER={ODBC Driver 18 for SQL Server};SERVER=NTB000250;Trusted_Connection=yes;DATABASE=PaidData;TrustServerCertificate=yes;'
conn_dbf = 'driver={Advantage StreamlineSQL ODBC};DataDirectory=E:\\MyDocuments\\FoxProProjects\\Bastion\\BASE\\GTD_2022_LG\\GTD_2022_LG.add;DefaultType=FoxPro;'


def data_serializer(o):
    if isinstance(o, datetime.date) | isinstance(o, datetime.datetime):
        return o.isoformat()


def do_json_export(row):
    return json.dumps(row, default=data_serializer)


def convert(value):
    # `value` will be a string.  We'll simply add an X at the beginning at the end.
    return 'X' + value + 'X'

def datetime_as_string(value):
    tup = struct.unpack("<6hI", value)  # e.g., (2017, 5, 30, 8, 59, 37, 0, 665039700)
    return datetime(tup[0], tup[1], tup[2],
                    hour=tup[3], minute=tup[4], second=tup[5],
                    microsecond=math.floor(tup[6] / 1000.0 + 0.5))
    # ref: https: // github.com / mkleehammer / pyodbc / issues / 134  # issuecomment-281739794
    # tup = struct.unpack("<6hI2h", value)  # e.g., (2017, 3, 16, 10, 35, 18, 500000000, -6, 0)
    # return datetime(tup[0], tup[1], tup[2], tup[3], tup[4], tup[5], tup[6] // 1000,
    #                 timezone(timedelta(hours=tup[7], minutes=tup[8])))
    # return value.strftime("%m/%d/%Y, %H:%M:%S")

def get_dbf_data():
    # c = AdvantageClipperConnect(encoding='cp866', data_directory='E:\\TEST\\', uid='', pwd='')

    # f = AdvantageVisualFoxproConnect(uid='', pwd='', data_directory='E:\\MyDocuments\\FoxProProjects\\UpsizingWizard\\TESTDBC\\test.add')
    # d = DatabaseIntrospection(f.connection)
    # fields = d.get_table_description(f.connection.cursor(), 'XML_TABLE_DBF_TYPES')
    # pk_index = d.get_primary_key_column(f.connection.cursor(), 'XML_TABLE_DBF_TYPES')
    # with d.connection.cursor() as cursor:
    #     tables = d.table_names(cursor)
    #     pass

    # dsn = ODBCDataSourceConnect(dsn='GTData', uid='', pwd='')
    # xsd= c.generate_xsd_schema(table_name='DclHead')

    # c.connection.add_output_converter(pyodbc.SQL_TYPE_TIMESTAMP, datetime_as_string)

    # c.connection.add_output_converter(pyodbc.SQL_TYPE_DATE, datetime_as_string)
    # c.connection.add_output_converter(pyodbc.SQL_VARCHAR, convert)

    cursor = c.connection.cursor().tables(table='DclHead')
    tsql = """
    SELECT "dclhead"."num_ver", "dclhead"."data_ver", "dclhead"."typ_dcl", 
        "dclhead"."gugtk", "dclhead"."copy", "dclhead"."dcopy", "dclhead"."q_edit", 
        "dclhead"."d_edit", "dclhead"."sol", "dclhead"."max_err", "dclhead"."dd", 
        "dclhead"."tm", "dclhead"."extrnl", "dclhead"."schet", "dclhead"."stepctrl", 
        "dclhead"."typ_dtc", "dclhead"."vid_ktc", "dclhead"."frm_decl", "dclhead"."stat", 
        "dclhead"."g071", "dclhead"."g072", "dclhead"."g073", "dclhead"."g073_1", 
        "dclhead"."ui_b_1", "dclhead"."ui_b_2", "dclhead"."ui_b_3", "dclhead"."sds_srv", 
        "dclhead"."sds_num", "dclhead"."sds_cust", "dclhead"."f_decl", "dclhead"."remotepay", 
        "dclhead"."rccncode", "dclhead"."dpresent", "dclhead"."tpresent", "dclhead"."complectbl", 
        "dclhead"."g011", "dclhead"."g012", "dclhead"."g0121", "dclhead"."g0131", "dclhead"."g020", 
        "dclhead"."g02_itn", "dclhead"."g021", "dclhead"."g022", "dclhead"."g023post", "dclhead"."g0231", 
        "dclhead"."g0231c", "dclhead"."g0231n", "dclhead"."g023subd", "dclhead"."g023city", 
        "dclhead"."g023street", "dclhead"."g023build", "dclhead"."g023", "dclhead"."g024b", 
        "dclhead"."g024n", "dclhead"."g024in", "dclhead"."g027", "dclhead"."g0281", "dclhead"."g0281a", 
        "dclhead"."g02821", "dclhead"."g02822", "dclhead"."g02823", "dclhead"."g0283", "dclhead"."g022a", 
        "dclhead"."g027a", "dclhead"."g023apost", "dclhead"."g0231a", "dclhead"."g0231an", 
        "dclhead"."g023asubd", "dclhead"."g023acity", "dclhead"."g023astree", "dclhead"."g023abuild", 
        "dclhead"."g029", "dclhead"."g02e14", "dclhead"."g032", "dclhead"."g040", "dclhead"."g04", 
        "dclhead"."g05", "dclhead"."g06", "dclhead"."g07", "dclhead"."g080", "dclhead"."g08_itn", 
        "dclhead"."g081", "dclhead"."g082", "dclhead"."g083post", "dclhead"."g0831", "dclhead"."g0831c", 
        "dclhead"."g0831a", "dclhead"."g083subd", "dclhead"."g083city", "dclhead"."g083street", 
        "dclhead"."g083build", "dclhead"."g083", "dclhead"."g084b", "dclhead"."g087", "dclhead"."g0881", 
        "dclhead"."g0881a", "dclhead"."g08821", "dclhead"."g08822", "dclhead"."g08823", "dclhead"."g0883", 
        "dclhead"."g089", "dclhead"."g082a", "dclhead"."g087a", "dclhead"."g083apost", "dclhead"."g0831aa", 
        "dclhead"."g0831an", "dclhead"."g083asubd", "dclhead"."g083acity", "dclhead"."g083astree", 
        "dclhead"."g083abuild", "dclhead"."g08e14", "dclhead"."g090", "dclhead"."g09_itn", "dclhead"."g091", 
        "dclhead"."g092", "dclhead"."g092a", "dclhead"."g093post", "dclhead"."g0931", "dclhead"."g0931n", 
        "dclhead"."g093subd", "dclhead"."g093city", "dclhead"."g093street", "dclhead"."g093build", 
        "dclhead"."g093apost", "dclhead"."g0931a", "dclhead"."g0931an", "dclhead"."g093asubd", 
        "dclhead"."g093acity", "dclhead"."g093astree", "dclhead"."g093abuild", "dclhead"."g093", 
        "dclhead"."g093a", "dclhead"."g094b", "dclhead"."g097", "dclhead"."g097a", "dclhead"."g0981", 
        "dclhead"."g0981a", "dclhead"."g09821", "dclhead"."g09822", "dclhead"."g09823", "dclhead"."g0983", 
        "dclhead"."g09e14", "dclhead"."g11", "dclhead"."g11c", "dclhead"."g12", "dclhead"."g121", 
        "dclhead"."g12k", "dclhead"."g13", "dclhead"."g140", "dclhead"."g14_itn", "dclhead"."g141", 
        "dclhead"."g142", "dclhead"."g142a", "dclhead"."g143post", "dclhead"."g1431", "dclhead"."g1431n", 
        "dclhead"."g143subd", "dclhead"."g143city", "dclhead"."g143street", "dclhead"."g143build", 
        "dclhead"."aeorowner", "dclhead"."aeocntry", "dclhead"."aeonum", "dclhead"."aeokind", 
        "dclhead"."aeoregcod", "dclhead"."g143", "dclhead"."g143apost", "dclhead"."g1431a", 
        "dclhead"."g1431an", "dclhead"."g143asubd", "dclhead"."g143acity", "dclhead"."g143astree", 
        "dclhead"."g143abuild", "dclhead"."g143a", "dclhead"."g144b", "dclhead"."g147", "dclhead"."g147a", 
        "dclhead"."g1481", "dclhead"."g1481a", "dclhead"."g14821", "dclhead"."g14822", "dclhead"."g14823", 
        "dclhead"."g1483", "dclhead"."g15", "dclhead"."g15a", "dclhead"."g15ac", "dclhead"."g160", 
        "dclhead"."g16a", "dclhead"."g16", "dclhead"."g161", "dclhead"."g17a", "dclhead"."g17ac", 
        "dclhead"."g17b", "dclhead"."g180", "dclhead"."g182", "dclhead"."g19", "dclhead"."g202", 
        "dclhead"."g2021", "dclhead"."g203", "dclhead"."g210", "dclhead"."g212", "dclhead"."g221", 
        "dclhead"."g221c", "dclhead"."g222", "dclhead"."g222k", "dclhead"."g23", "dclhead"."g230", 
        "dclhead"."g231", "dclhead"."g24", "dclhead"."g270", "dclhead"."g27_itn", "dclhead"."g2710", 
        "dclhead"."g271", "dclhead"."g27", "dclhead"."g2711", "dclhead"."g2712", "dclhead"."g2810", 
        "dclhead"."g2811", "dclhead"."g28gtd_1", "dclhead"."g28gtd_2", "dclhead"."g28gtd_3", 
        "dclhead"."g281", "dclhead"."g28zajmb", "dclhead"."g281d", "dclhead"."g281dd", "dclhead"."g2831", 
        "dclhead"."g284", "dclhead"."g284d", "dclhead"."g284dd", "dclhead"."g28_itn", "dclhead"."g28okpo", 
        "dclhead"."g28inn", "dclhead"."g281oth", "dclhead"."g28zajmn", "dclhead"."g282", "dclhead"."g28211", 
        "dclhead"."g28212", "dclhead"."g28221", "dclhead"."g28222", "dclhead"."g28230", "dclhead"."g2823", 
        "dclhead"."g28240", "dclhead"."g2824", "dclhead"."g2825", "dclhead"."g30_itn", "dclhead"."g300", 
        "dclhead"."g3010", "dclhead"."g30aeoown", "dclhead"."g30aeocntr", "dclhead"."g301", 
        "dclhead"."g30aeokind", "dclhead"."g30aeorcod", "dclhead"."g3011", "dclhead"."g30", 
        "dclhead"."g30d", "dclhead"."g30post", "dclhead"."g30a", "dclhead"."g30an", "dclhead"."g30subd", 
        "dclhead"."g30city", "dclhead"."g30street", "dclhead"."g30build", "dclhead"."g30lname", 
        "dclhead"."g3012", "dclhead"."g30121", "dclhead"."g30122", "dclhead"."g4910", "dclhead"."g491", 
        "dclhead"."g492", "dclhead"."g500", "dclhead"."g50_itn", "dclhead"."g5011", "dclhead"."g5012", 
        "dclhead"."g5023", "dclhead"."g5033", "dclhead"."g504", "dclhead"."g507", "dclhead"."g5081", 
        "dclhead"."g5081a", "dclhead"."g50821", "dclhead"."g50822", "dclhead"."g50823", "dclhead"."g5083", 
        "dclhead"."g54_itn", "dclhead"."g5410", "dclhead"."g541", "dclhead"."g541d", "dclhead"."g5411", 
        "dclhead"."g5411d", "dclhead"."g5411aid", "dclhead"."g5411adid", "dclhead"."g5411modid", 
        "dclhead"."g5411doc", "dclhead"."prprov541", "dclhead"."pretype541", "dclhead"."prevnum541", 
        "dclhead"."g541_inn", "dclhead"."g541_kpp", "dclhead"."g542", "dclhead"."g542t", "dclhead"."g5441", 
        "dclhead"."g5441nm", "dclhead"."g5441mdnm", "dclhead"."g5442", "dclhead"."g5443", "dclhead"."g5444", 
        "dclhead"."g5445", "dclhead"."g544aid", "dclhead"."g544adid", "dclhead"."g544modid", 
        "dclhead"."g544doc", "dclhead"."prprov544", "dclhead"."pretype544", "dclhead"."prevnum544", 
        "dclhead"."g5446", "dclhead"."g5447", "dclhead"."g5451", "dclhead"."g5451a", "dclhead"."g54521", 
        "dclhead"."g54522", "dclhead"."g54523", "dclhead"."g5453", "dclhead"."g545aid", "dclhead"."g545adid", 
        "dclhead"."g545modid", "dclhead"."g545doc", "dclhead"."prprov545", "dclhead"."pretype545", 
        "dclhead"."prevnum545", "dclhead"."gd0", "dclhead"."gd1", "dclhead"."gd11", "dclhead"."gd2", 
        "dclhead"."gd00", "dclhead"."gd01", "dclhead"."gddf", "dclhead"."recplatv", "dclhead"."recslotm", 
        "dclhead"."rectrans", "dclhead"."recsumpp", "dclhead"."recpasp", "dclhead"."recusl", "dclhead"."pprr", 
        "dclhead"."pprv", "dclhead"."pposh", "dclhead"."pnal", "dclhead"."gnuser", "dclhead"."flduser", 
        "dclhead"."nrelise", "dclhead"."kodtop", "dclhead"."g071top", "dclhead"."g072top", 
        "dclhead"."g073top", "dclhead"."typdtop", "dclhead"."numdtop", "dclhead"."datdtop", 
        "dclhead"."fiotop", "dclhead"."dattop", "dclhead"."dmodify", "dclhead"."tmodify", 
        "dclhead"."edoc_guid", "dclhead"."edoc_id", "dclhead"."ed_procid", "dclhead"."val_contr", 
        "dclhead"."ps_contr", "dclhead"."p_status1", "dclhead"."p_status2", "dclhead"."ed_ididkmp", 
        "dclhead"."ed_idid", "dclhead"."ed_ididcnt", "dclhead"."ed_ididftc", "dclhead"."xmlvers", 
        "dclhead"."typed" 
    FROM "dclhead";
    """
    # tsql = """SELECT "dclhead"."num_ver", "dclhead"."data_ver" FROM DCLHEAD ;"""
    # tsql = "SELECT G071, G072, G073 FROM DCLHEAD WHERE G073 = '3002512';"
    # xsd = XSDSchema(connection=c.connection, t_sql=tsql, table='DclHead').schema()

    headers = [column[3] for column in c.connection.cursor().columns(table='DclHead').fetchall()]
    data = []
    with cursor.execute(tsql):
        rows = cursor.fetchone()

    for row in rows:
        data.append(data_serializer(row, default=data_serializer))

    dataset = tablib.Dataset(*data, headers=headers)

    pass

    # for row in cursor.execute(tsql):
    #     row

    with cursor.execute(tsql):
        row = cursor.fetchone()
    #     columns = [column[0] for column in cursor.description]
    #     results = []
    #     for row in cursor.fetchall():
    #         results.append(dict(zip(columns, row)))
    #
    #     XSDSchema(cursor=cursor)
    pass

    #c.execute_query("""SELECT g54523, G073 FROM DCLHEAD;""")
    # conn_dbf = get_connectstring(type=4)
    # print(conn_dbf)
    # t = AdsTables(conn_string=conn_dbf)
    # xsd = XSDSchema(table=t.tablename['DclHead']).retrieve_schema()
    # xml = XMLData(table=t.tablename['DclHead'], conn_string=conn_dbf ).retrieve_schema()

    # connection = pyodbc.connect(conn_dbf, ansi=True)
    # connection.setdecoding(pyodbc.SQL_CHAR, encoding='cp866')
    # tables = connection.cursor().tables(tableType='TABLE')

    # print('Reading data from DBF table')
    # tables = connection.cursor().tables(tableType='TABLE').fetchall()
    # for table in tables.fetchall():
        # columns = connection.cursor().columns(table=table[2], catalog=table[0]).fetchall()
        # table = Table(table, fields=columns)
        # pass

    # tsql = "SELECT g54523, G073 FROM DCLHEAD WHERE G073 = '3002512';"
    # with tables.execute(tsql):
    #     row = tables.fetchone()
    #     while row:
    #         print(str(row[0]) + " " + str(row[1]))
    #         row = tables.fetchone()


def get_data():
    # cnxn = pyodbc.connect(
    #     'DRIVER={ODBC Driver 18 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes;TrustServerCertificate=yes;')
    # cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

    cnxn = pyodbc.connect('DSN=Clipper', autocommit=True, ansi=False)

    cursor = cnxn.cursor()

    # Select Query
    tsql = "SELECT * FROM dclhead;"
    with cursor.execute(tsql):
        row = cursor.fetchone()
        while row:
            print(str(row[0]) + " " + str(row[1]))
            row = cursor.fetchone()


if __name__ == '__main__':
    try:
        get_data()
    except ValidationError as e:
        print(e)
