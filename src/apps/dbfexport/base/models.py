from django.db import models


class BaseModel(models.Model):
    """Base import model"""
    is_global = False

    class Meta:
        abstract = True


class DclHead(BaseModel):
    """Abstract model DclHead.dbf"""

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dclhead'

    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    num_ver = models.CharField(max_length=8, blank=True, null=True)
    data_ver = models.DateField(blank=True, null=True)
    typ_dcl = models.CharField(max_length=2, blank=True, null=True)
    gugtk = models.BooleanField(blank=True, null=True)
    copy = models.BooleanField(blank=True, null=True)
    dcopy = models.DateField(blank=True, null=True)
    q_edit = models.IntegerField(default=0, blank=True, null=True)
    d_edit = models.DateField(blank=True, null=True)
    sol = models.IntegerField(default=0, blank=True, null=True)
    max_err = models.IntegerField(default=0, blank=True, null=True)
    dd = models.DateField(blank=True, null=True)
    tm = models.CharField(max_length=8, blank=True, null=True)
    extrnl = models.CharField(max_length=80, blank=True, null=True)
    schet = models.CharField(max_length=160, blank=True, null=True)
    stepctrl = models.CharField(max_length=20, blank=True, null=True)
    typ_dtc = models.CharField(max_length=1, blank=True, null=True)
    vid_ktc = models.CharField(max_length=1, blank=True, null=True)
    frm_decl = models.CharField(max_length=1, blank=True, null=True)
    stat = models.CharField(max_length=1, blank=True, null=True)
    g073_1 = models.CharField(max_length=6, blank=True, null=True)
    ui_b_1 = models.CharField(max_length=8, blank=True, null=True)
    ui_b_2 = models.DateField(blank=True, null=True)
    ui_b_3 = models.CharField(max_length=7, blank=True, null=True)
    sds_srv = models.CharField(max_length=4, blank=True, null=True)
    sds_num = models.IntegerField(default=0, blank=True, null=True)
    sds_cust = models.CharField(max_length=8, blank=True, null=True)
    f_decl = models.CharField(max_length=1, blank=True, null=True)
    remotepay = models.CharField(max_length=1, blank=True, null=True)
    rccncode = models.CharField(max_length=2, blank=True, null=True)
    dpresent = models.DateField(blank=True, null=True)
    tpresent = models.CharField(max_length=8, blank=True, null=True)
    complectbl = models.CharField(max_length=1, blank=True, null=True)
    g011 = models.CharField(max_length=2, blank=True, null=True)
    g012 = models.CharField(max_length=2, blank=True, null=True)
    g0121 = models.CharField(max_length=2, blank=True, null=True)
    g0131 = models.CharField(max_length=3, blank=True, null=True)
    g020 = models.CharField(max_length=15, blank=True, null=True)
    g02_itn = models.CharField(max_length=13, blank=True, null=True)
    g021 = models.CharField(max_length=12, blank=True, null=True)
    g022 = models.CharField(max_length=150, blank=True, null=True)
    g023post = models.CharField(max_length=9, blank=True, null=True)
    g0231 = models.CharField(max_length=2, blank=True, null=True)
    g0231c = models.CharField(max_length=3, blank=True, null=True)
    g0231n = models.CharField(max_length=40, blank=True, null=True)
    g023subd = models.CharField(max_length=50, blank=True, null=True)
    g023city = models.CharField(max_length=35, blank=True, null=True)
    g023street = models.CharField(max_length=50, blank=True, null=True)
    g023build = models.CharField(max_length=50, blank=True, null=True)
    g023 = models.CharField(max_length=80, blank=True, null=True)
    g024b = models.CharField(max_length=5, blank=True, null=True)
    g024n = models.CharField(max_length=10, blank=True, null=True)
    g024in = models.CharField(max_length=12, blank=True, null=True)
    g027 = models.CharField(max_length=9, blank=True, null=True)
    g0281 = models.CharField(max_length=7, blank=True, null=True)
    g0281a = models.CharField(max_length=25, blank=True, null=True)
    g02821 = models.CharField(max_length=11, blank=True, null=True)
    g02822 = models.CharField(max_length=25, blank=True, null=True)
    g02823 = models.CharField(max_length=150, blank=True, null=True)
    g0283 = models.DateField(blank=True, null=True)
    g022a = models.CharField(max_length=150, blank=True, null=True)
    g027a = models.CharField(max_length=9, blank=True, null=True)
    g023apost = models.CharField(max_length=9, blank=True, null=True)
    g0231a = models.CharField(max_length=2, blank=True, null=True)
    g0231an = models.CharField(max_length=40, blank=True, null=True)
    g023asubd = models.CharField(max_length=50, blank=True, null=True)
    g023acity = models.CharField(max_length=35, blank=True, null=True)
    g023astree = models.CharField(max_length=50, blank=True, null=True)
    g023abuild = models.CharField(max_length=50, blank=True, null=True)
    g029 = models.CharField(max_length=1, blank=True, null=True)
    g02e14 = models.CharField(max_length=1, blank=True, null=True)
    g032 = models.IntegerField(default=0, blank=True, null=True)
    g040 = models.IntegerField(default=0, blank=True, null=True)
    g04 = models.IntegerField(default=0, blank=True, null=True)
    g05 = models.IntegerField(default=0, blank=True, null=True)
    g06 = models.IntegerField(default=0, blank=True, null=True)
    g07 = models.CharField(max_length=3, blank=True, null=True)
    g080 = models.CharField(max_length=15, blank=True, null=True)
    g08_itn = models.CharField(max_length=13, blank=True, null=True)
    g081 = models.CharField(max_length=12, blank=True, null=True)
    g082 = models.CharField(max_length=150, blank=True, null=True)
    g083post = models.CharField(max_length=9, blank=True, null=True)
    g0831 = models.CharField(max_length=2, blank=True, null=True)
    g0831c = models.CharField(max_length=3, blank=True, null=True)
    g0831a = models.CharField(max_length=40, blank=True, null=True)
    g083subd = models.CharField(max_length=50, blank=True, null=True)
    g083city = models.CharField(max_length=35, blank=True, null=True)
    g083street = models.CharField(max_length=50, blank=True, null=True)
    g083build = models.CharField(max_length=50, blank=True, null=True)
    g083 = models.CharField(max_length=80, blank=True, null=True)
    g084b = models.CharField(max_length=5, blank=True, null=True)
    g087 = models.CharField(max_length=9, blank=True, null=True)
    g0881 = models.CharField(max_length=7, blank=True, null=True)
    g0881a = models.CharField(max_length=25, blank=True, null=True)
    g08821 = models.CharField(max_length=11, blank=True, null=True)
    g08822 = models.CharField(max_length=25, blank=True, null=True)
    g08823 = models.CharField(max_length=150, blank=True, null=True)
    g0883 = models.DateField(blank=True, null=True)
    g089 = models.CharField(max_length=1, blank=True, null=True)
    g082a = models.CharField(max_length=150, blank=True, null=True)
    g087a = models.CharField(max_length=9, blank=True, null=True)
    g083apost = models.CharField(max_length=9, blank=True, null=True)
    g0831aa = models.CharField(max_length=2, blank=True, null=True)
    g0831an = models.CharField(max_length=40, blank=True, null=True)
    g083asubd = models.CharField(max_length=50, blank=True, null=True)
    g083acity = models.CharField(max_length=35, blank=True, null=True)
    g083astree = models.CharField(max_length=50, blank=True, null=True)
    g083abuild = models.CharField(max_length=50, blank=True, null=True)
    g08e14 = models.CharField(max_length=1, blank=True, null=True)
    g090 = models.CharField(max_length=15, blank=True, null=True)
    g09_itn = models.CharField(max_length=13, blank=True, null=True)
    g091 = models.CharField(max_length=12, blank=True, null=True)
    g092 = models.CharField(max_length=150, blank=True, null=True)
    g092a = models.CharField(max_length=150, blank=True, null=True)
    g093post = models.CharField(max_length=9, blank=True, null=True)
    g0931 = models.CharField(max_length=2, blank=True, null=True)
    g0931n = models.CharField(max_length=40, blank=True, null=True)
    g093subd = models.CharField(max_length=50, blank=True, null=True)
    g093city = models.CharField(max_length=35, blank=True, null=True)
    g093street = models.CharField(max_length=50, blank=True, null=True)
    g093build = models.CharField(max_length=50, blank=True, null=True)
    g093apost = models.CharField(max_length=9, blank=True, null=True)
    g0931a = models.CharField(max_length=2, blank=True, null=True)
    g0931an = models.CharField(max_length=40, blank=True, null=True)
    g093asubd = models.CharField(max_length=50, blank=True, null=True)
    g093acity = models.CharField(max_length=35, blank=True, null=True)
    g093astree = models.CharField(max_length=50, blank=True, null=True)
    g093abuild = models.CharField(max_length=50, blank=True, null=True)
    g093 = models.CharField(max_length=80, blank=True, null=True)
    g093a = models.CharField(max_length=80, blank=True, null=True)
    g094b = models.CharField(max_length=5, blank=True, null=True)
    g097 = models.CharField(max_length=9, blank=True, null=True)
    g097a = models.CharField(max_length=9, blank=True, null=True)
    g0981 = models.CharField(max_length=7, blank=True, null=True)
    g0981a = models.CharField(max_length=25, blank=True, null=True)
    g09821 = models.CharField(max_length=11, blank=True, null=True)
    g09822 = models.CharField(max_length=25, blank=True, null=True)
    g09823 = models.CharField(max_length=150, blank=True, null=True)
    g0983 = models.DateField(blank=True, null=True)
    g09e14 = models.CharField(max_length=1, blank=True, null=True)
    g11 = models.CharField(max_length=2, blank=True, null=True)
    g11c = models.CharField(max_length=3, blank=True, null=True)
    g12 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    g121 = models.CharField(max_length=3, blank=True, null=True)
    g12k = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    g13 = models.CharField(max_length=8, blank=True, null=True)
    g140 = models.CharField(max_length=15, blank=True, null=True)
    g14_itn = models.CharField(max_length=13, blank=True, null=True)
    g141 = models.CharField(max_length=12, blank=True, null=True)
    g142 = models.CharField(max_length=150, blank=True, null=True)
    g142a = models.CharField(max_length=150, blank=True, null=True)
    g143post = models.CharField(max_length=9, blank=True, null=True)
    g1431 = models.CharField(max_length=2, blank=True, null=True)
    g1431n = models.CharField(max_length=40, blank=True, null=True)
    g143subd = models.CharField(max_length=50, blank=True, null=True)
    g143city = models.CharField(max_length=35, blank=True, null=True)
    g143street = models.CharField(max_length=50, blank=True, null=True)
    g143build = models.CharField(max_length=50, blank=True, null=True)
    aeorowner = models.CharField(max_length=1, blank=True, null=True)
    aeocntry = models.CharField(max_length=2, blank=True, null=True)
    aeonum = models.CharField(max_length=50, blank=True, null=True)
    aeokind = models.CharField(max_length=1, blank=True, null=True)
    aeoregcod = models.CharField(max_length=3, blank=True, null=True)
    g143 = models.CharField(max_length=80, blank=True, null=True)
    g143apost = models.CharField(max_length=9, blank=True, null=True)
    g1431a = models.CharField(max_length=2, blank=True, null=True)
    g1431an = models.CharField(max_length=40, blank=True, null=True)
    g143asubd = models.CharField(max_length=50, blank=True, null=True)
    g143acity = models.CharField(max_length=35, blank=True, null=True)
    g143astree = models.CharField(max_length=50, blank=True, null=True)
    g143abuild = models.CharField(max_length=50, blank=True, null=True)
    g143a = models.CharField(max_length=80, blank=True, null=True)
    g144b = models.CharField(max_length=5, blank=True, null=True)
    g147 = models.CharField(max_length=9, blank=True, null=True)
    g147a = models.CharField(max_length=9, blank=True, null=True)
    g1481 = models.CharField(max_length=7, blank=True, null=True)
    g1481a = models.CharField(max_length=25, blank=True, null=True)
    g14821 = models.CharField(max_length=11, blank=True, null=True)
    g14822 = models.CharField(max_length=25, blank=True, null=True)
    g14823 = models.CharField(max_length=150, blank=True, null=True)
    g1483 = models.DateField(blank=True, null=True)
    g15 = models.CharField(max_length=40, blank=True, null=True)
    g15a = models.CharField(max_length=2, blank=True, null=True)
    g15ac = models.CharField(max_length=3, blank=True, null=True)
    g160 = models.CharField(max_length=1, blank=True, null=True)
    g16a = models.CharField(max_length=2, blank=True, null=True)
    g16 = models.CharField(max_length=40, blank=True, null=True)
    g161 = models.CharField(max_length=2, blank=True, null=True)
    g17a = models.CharField(max_length=2, blank=True, null=True)
    g17ac = models.CharField(max_length=3, blank=True, null=True)
    g17b = models.CharField(max_length=40, blank=True, null=True)
    g180 = models.IntegerField(default=0, blank=True, null=True)
    g182 = models.CharField(max_length=2, blank=True, null=True)
    g19 = models.CharField(max_length=1, blank=True, null=True)
    g202 = models.CharField(max_length=3, blank=True, null=True)
    g2021 = models.CharField(max_length=50, blank=True, null=True)
    g203 = models.CharField(max_length=250, blank=True, null=True)
    g210 = models.IntegerField(default=0, blank=True, null=True)
    g212 = models.CharField(max_length=2, blank=True, null=True)
    g221 = models.CharField(max_length=3, blank=True, null=True)
    g221c = models.CharField(max_length=3, blank=True, null=True)
    g222 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    g222k = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    g23 = models.DecimalField(default=0.00, max_digits=10, decimal_places=4, blank=True, null=True)
    g230 = models.DateField(blank=True, null=True)
    g231 = models.DecimalField(default=0.00, max_digits=10, decimal_places=4, blank=True, null=True)
    g24 = models.CharField(max_length=3, blank=True, null=True)
    g270 = models.CharField(max_length=2, blank=True, null=True)
    g27_itn = models.CharField(max_length=13, blank=True, null=True)
    g2710 = models.CharField(max_length=1, blank=True, null=True)
    g271 = models.CharField(max_length=13, blank=True, null=True)
    g27 = models.CharField(max_length=40, blank=True, null=True)
    g2711 = models.DateField(blank=True, null=True)
    g2712 = models.CharField(max_length=8, blank=True, null=True)
    g2810 = models.CharField(max_length=1, blank=True, null=True)
    g2811 = models.CharField(max_length=1, blank=True, null=True)
    g28gtd_1 = models.CharField(max_length=8, blank=True, null=True)
    g28gtd_2 = models.DateField(blank=True, null=True)
    g28gtd_3 = models.CharField(max_length=7, blank=True, null=True)
    g281 = models.CharField(max_length=70, blank=True, null=True)
    g28zajmb = models.CharField(max_length=70, blank=True, null=True)
    g281d = models.DateField(blank=True, null=True)
    g281dd = models.DateField(blank=True, null=True)
    g2831 = models.CharField(max_length=2, blank=True, null=True)
    g284 = models.CharField(max_length=50, blank=True, null=True)
    g284d = models.DateField(blank=True, null=True)
    g284dd = models.DateField(blank=True, null=True)
    g28_itn = models.CharField(max_length=13, blank=True, null=True)
    g28okpo = models.CharField(max_length=10, blank=True, null=True)
    g28inn = models.CharField(max_length=12, blank=True, null=True)
    g281oth = models.CharField(max_length=30, blank=True, null=True)
    g28zajmn = models.CharField(max_length=50, blank=True, null=True)
    g282 = models.CharField(max_length=70, blank=True, null=True)
    g28211 = models.CharField(max_length=1, blank=True, null=True)
    g28212 = models.CharField(max_length=2, blank=True, null=True)
    g28221 = models.CharField(max_length=3, blank=True, null=True)
    g28222 = models.CharField(max_length=1, blank=True, null=True)
    g28230 = models.CharField(max_length=1, blank=True, null=True)
    g2823 = models.DateField(blank=True, null=True)
    g28240 = models.CharField(max_length=1, blank=True, null=True)
    g2824 = models.DateField(blank=True, null=True)
    g2825 = models.CharField(max_length=3, blank=True, null=True)
    g30_itn = models.CharField(max_length=13, blank=True, null=True)
    g300 = models.CharField(max_length=2, blank=True, null=True)
    g3010 = models.CharField(max_length=1, blank=True, null=True)
    g30aeoown = models.CharField(max_length=1, blank=True, null=True)
    g30aeocntr = models.CharField(max_length=2, blank=True, null=True)
    g301 = models.CharField(max_length=50, blank=True, null=True)
    g30aeokind = models.CharField(max_length=1, blank=True, null=True)
    g30aeorcod = models.CharField(max_length=3, blank=True, null=True)
    g3011 = models.DateField(blank=True, null=True)
    g30 = models.CharField(max_length=50, blank=True, null=True)
    g30d = models.DateField(blank=True, null=True)
    g30post = models.CharField(max_length=9, blank=True, null=True)
    g30a = models.CharField(max_length=2, blank=True, null=True)
    g30an = models.CharField(max_length=40, blank=True, null=True)
    g30subd = models.CharField(max_length=50, blank=True, null=True)
    g30city = models.CharField(max_length=35, blank=True, null=True)
    g30street = models.CharField(max_length=50, blank=True, null=True)
    g30build = models.CharField(max_length=50, blank=True, null=True)
    g30lname = models.CharField(max_length=150, blank=True, null=True)
    g3012 = models.CharField(max_length=8, blank=True, null=True)
    g30121 = models.CharField(max_length=2, blank=True, null=True)
    g30122 = models.CharField(max_length=50, blank=True, null=True)
    g4910 = models.CharField(max_length=1, blank=True, null=True)
    g491 = models.CharField(max_length=30, blank=True, null=True)
    g492 = models.DateField(blank=True, null=True)
    g500 = models.CharField(max_length=15, blank=True, null=True)
    g50_itn = models.CharField(max_length=13, blank=True, null=True)
    g5011 = models.CharField(max_length=80, blank=True, null=True)
    g5012 = models.CharField(max_length=80, blank=True, null=True)
    g5023 = models.CharField(max_length=80, blank=True, null=True)
    g5033 = models.CharField(max_length=80, blank=True, null=True)
    g504 = models.CharField(max_length=12, blank=True, null=True)
    g507 = models.CharField(max_length=9, blank=True, null=True)
    g5081 = models.CharField(max_length=2, blank=True, null=True)
    g5081a = models.CharField(max_length=6, blank=True, null=True)
    g50821 = models.CharField(max_length=11, blank=True, null=True)
    g50822 = models.CharField(max_length=25, blank=True, null=True)
    g50823 = models.CharField(max_length=80, blank=True, null=True)
    g5083 = models.DateField(blank=True, null=True)
    g54_itn = models.CharField(max_length=13, blank=True, null=True)
    g5410 = models.CharField(max_length=1, blank=True, null=True)
    g541 = models.CharField(max_length=14, blank=True, null=True)
    g541d = models.DateField(blank=True, null=True)
    g5411 = models.CharField(max_length=50, blank=True, null=True)
    g5411d = models.DateField(blank=True, null=True)
    g5411aid = models.CharField(max_length=50, blank=True, null=True)
    g5411adid = models.CharField(max_length=50, blank=True, null=True)
    g5411modid = models.CharField(max_length=10, blank=True, null=True)
    g5411doc = models.CharField(max_length=5, blank=True, null=True)
    prprov541 = models.CharField(max_length=1, blank=True, null=True)
    pretype541 = models.CharField(max_length=1, blank=True, null=True)
    prevnum541 = models.CharField(max_length=50, blank=True, null=True)
    g541_inn = models.CharField(max_length=12, blank=True, null=True)
    g541_kpp = models.CharField(max_length=9, blank=True, null=True)
    g542 = models.DateField(blank=True, null=True)
    g542t = models.CharField(max_length=8, blank=True, null=True)
    g5441 = models.CharField(max_length=150, blank=True, null=True)
    g5441nm = models.CharField(max_length=150, blank=True, null=True)
    g5441mdnm = models.CharField(max_length=150, blank=True, null=True)
    g5442 = models.CharField(max_length=50, blank=True, null=True)
    g5443 = models.CharField(max_length=250, blank=True, null=True)
    g5444 = models.CharField(max_length=50, blank=True, null=True)
    g5445 = models.DateField(blank=True, null=True)
    g544aid = models.CharField(max_length=50, blank=True, null=True)
    g544adid = models.CharField(max_length=50, blank=True, null=True)
    g544modid = models.CharField(max_length=10, blank=True, null=True)
    g544doc = models.CharField(max_length=5, blank=True, null=True)
    prprov544 = models.CharField(max_length=1, blank=True, null=True)
    pretype544 = models.CharField(max_length=1, blank=True, null=True)
    prevnum544 = models.CharField(max_length=50, blank=True, null=True)
    g5446 = models.DateField(blank=True, null=True)
    g5447 = models.CharField(max_length=50, blank=True, null=True)
    g5451 = models.CharField(max_length=7, blank=True, null=True)
    g5451a = models.CharField(max_length=25, blank=True, null=True)
    g54521 = models.CharField(max_length=11, blank=True, null=True)
    g54522 = models.CharField(max_length=25, blank=True, null=True)
    g54523 = models.CharField(max_length=150, blank=True, null=True)
    g5453 = models.DateField(blank=True, null=True)
    g545aid = models.CharField(max_length=50, blank=True, null=True)
    g545adid = models.CharField(max_length=50, blank=True, null=True)
    g545modid = models.CharField(max_length=10, blank=True, null=True)
    g545doc = models.CharField(max_length=5, blank=True, null=True)
    prprov545 = models.CharField(max_length=1, blank=True, null=True)
    pretype545 = models.CharField(max_length=1, blank=True, null=True)
    prevnum545 = models.CharField(max_length=50, blank=True, null=True)
    gd0 = models.CharField(max_length=2, blank=True, null=True)
    gd1 = models.DateField(blank=True, null=True)
    gd11 = models.CharField(max_length=8, blank=True, null=True)
    gd2 = models.CharField(max_length=4, blank=True, null=True)
    gd00 = models.CharField(max_length=250, blank=True, null=True)
    gd01 = models.CharField(max_length=250, blank=True, null=True)
    gddf = models.DateField(blank=True, null=True)
    recplatv = models.IntegerField(default=0, blank=True, null=True)
    recslotm = models.IntegerField(default=0, blank=True, null=True)
    rectrans = models.IntegerField(default=0, blank=True, null=True)
    recsumpp = models.IntegerField(default=0, blank=True, null=True)
    recpasp = models.IntegerField(default=0, blank=True, null=True)
    recusl = models.IntegerField(default=0, blank=True, null=True)
    pprr = models.DecimalField(default=0.00, max_digits=11, decimal_places=2, blank=True, null=True)
    pprv = models.DecimalField(default=0.00, max_digits=11, decimal_places=2, blank=True, null=True)
    pposh = models.DecimalField(default=0.00, max_digits=11, decimal_places=2, blank=True, null=True)
    pnal = models.DecimalField(default=0.00, max_digits=11, decimal_places=2, blank=True, null=True)
    gnuser = models.CharField(max_length=40, blank=True, null=True)
    flduser = models.CharField(max_length=40, blank=True, null=True)
    nrelise = models.CharField(max_length=10, blank=True, null=True)
    kodtop = models.CharField(max_length=3, blank=True, null=True)
    g071top = models.CharField(max_length=8, blank=True, null=True)
    g072top = models.DateField(blank=True, null=True)
    g073top = models.CharField(max_length=7, blank=True, null=True)
    typdtop = models.CharField(max_length=2, blank=True, null=True)
    numdtop = models.CharField(max_length=50, blank=True, null=True)
    datdtop = models.DateField(blank=True, null=True)
    fiotop = models.CharField(max_length=40, blank=True, null=True)
    dattop = models.DateField(blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    edoc_guid = models.CharField(max_length=32, blank=True, null=True)
    edoc_id = models.IntegerField(default=0, blank=True, null=True)
    ed_procid = models.CharField(max_length=36, blank=True, null=True)
    val_contr = models.CharField(max_length=1, blank=True, null=True)
    ps_contr = models.CharField(max_length=1, blank=True, null=True)
    p_status1 = models.IntegerField(default=0, blank=True, null=True)
    p_status2 = models.IntegerField(default=0, blank=True, null=True)
    ed_ididkmp = models.CharField(max_length=36, blank=True, null=True)
    ed_idid = models.CharField(max_length=36, blank=True, null=True)
    ed_ididcnt = models.CharField(max_length=36, blank=True, null=True)
    ed_ididftc = models.CharField(max_length=36, blank=True, null=True)
    xmlvers = models.CharField(max_length=10, blank=True, null=True)
    typed = models.CharField(max_length=2, blank=True, null=True)


class AktsHead(BaseModel):
    """Abstract model AktHead.dbf"""
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)

    edoc_guid = models.CharField(max_length=36, blank=True, null=True)
    version = models.IntegerField(default=0, blank=True, null=True)
    lnp = models.CharField(max_length=4, blank=True, null=True)
    pcategory = models.CharField(max_length=254, blank=True, null=True)
    score = models.IntegerField(default=0, blank=True, null=True)
    postcontrl = models.CharField(max_length=1, blank=True, null=True)
    resultakts = models.CharField(max_length=2, blank=True, null=True)
    change = models.CharField(max_length=1, blank=True, null=True)
    notes = models.CharField(max_length=254, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'aktshead'


class AktsMess(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    edoc_guid = models.CharField(max_length=36, blank=True, null=True)
    msg_guid = models.CharField(max_length=36, blank=True, null=True)
    version = models.IntegerField(default=0, blank=True, null=True)
    mcode = models.CharField(max_length=254, blank=True, null=True)
    mfull = models.CharField(max_length=254, blank=True, null=True)
    mshort = models.CharField(max_length=254, blank=True, null=True)
    passed = models.CharField(max_length=1, blank=True, null=True)
    mscore = models.IntegerField(default=0, blank=True, null=True)
    msection = models.IntegerField(default=0, blank=True, null=True)
    categories = models.CharField(max_length=254, blank=True, null=True)
    p_notes = models.CharField(max_length=1, blank=True, null=True)
    mtype = models.CharField(max_length=254, blank=True, null=True)
    full_xpath = models.CharField(max_length=254, blank=True, null=True)
    annotation = models.CharField(max_length=254, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'aktsmess'


class AktsPath(BaseModel):
    edoc_guid = models.CharField(max_length=36, blank=True, null=True)
    msg_guid = models.CharField(max_length=36, blank=True, null=True)
    path_guid = models.CharField(max_length=36, blank=True, null=True)
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    version = models.IntegerField(default=0, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    d_edoc_id = models.CharField(max_length=36, blank=True, null=True)
    full_xpath = models.CharField(max_length=254, blank=True, null=True)
    annotation = models.CharField(max_length=254, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'aktspath'


class CntOto(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    pr_dtc = models.CharField(max_length=1, blank=True, null=True)
    pr_ktc = models.CharField(max_length=1, blank=True, null=True)
    pr_cts = models.CharField(max_length=1, blank=True, null=True)
    pr_dk = models.CharField(max_length=1, blank=True, null=True)
    pr_act = models.CharField(max_length=1, blank=True, null=True)
    id_priz = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'cnt_oto'


class Cvc(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    k542 = models.DateField(blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    g37 = models.CharField(max_length=6, blank=True, null=True)
    g33 = models.CharField(max_length=10, blank=True, null=True)
    kortype = models.CharField(max_length=6, blank=True, null=True)
    k43 = models.CharField(max_length=2, blank=True, null=True)
    k451 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    k452 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    k38 = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    k470 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    fpay_rub = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    pen_rub = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    fpen_rub = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    kc30 = models.CharField(max_length=2, blank=True, null=True)
    nblktc1 = models.CharField(max_length=8, blank=True, null=True)
    nblktc2 = models.CharField(max_length=8, blank=True, null=True)
    nblktc1p = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'cvc'


class Dclamnum(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    series = models.CharField(max_length=9, blank=True, null=True)
    numstart = models.IntegerField(default=0, blank=True, null=True)
    numend = models.IntegerField(default=0, blank=True, null=True)
    kolvoam = models.IntegerField(default=0, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dclamnum'


class Dclavtmb(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    nud = models.CharField(max_length=12, blank=True, null=True)
    kodmrk = models.CharField(max_length=3, blank=True, null=True)
    namemrkcar = models.CharField(max_length=250, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)
    year = models.IntegerField(default=0, blank=True, null=True)
    price = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    pricev = models.CharField(max_length=3, blank=True, null=True)
    obem = models.IntegerField(default=0, blank=True, null=True)
    id = models.CharField(max_length=20, blank=True, null=True)
    nkuz = models.CharField(max_length=40, blank=True, null=True)
    kabina = models.CharField(max_length=40, blank=True, null=True)
    nsh = models.CharField(max_length=40, blank=True, null=True)
    ndv = models.CharField(max_length=40, blank=True, null=True)
    prim = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, blank=True, null=True)
    probeg = models.IntegerField(default=0, blank=True, null=True)
    probeged = models.CharField(max_length=3, blank=True, null=True)
    emergdev = models.CharField(max_length=50, blank=True, null=True)
    maxpower1 = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, blank=True, null=True)
    maxpower2 = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, blank=True, null=True)
    maxpower3 = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dclavtmb'


class Dclcont(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    container = models.CharField(max_length=17, blank=True, null=True)
    conttype = models.CharField(max_length=2, blank=True, null=True)
    contstat = models.CharField(max_length=1, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dclcont'


class Dclcrdts(BaseModel):
    numcard = models.CharField(max_length=23, blank=True, null=True)
    vin = models.CharField(max_length=20, blank=True, null=True)
    kodmrk = models.CharField(max_length=3, blank=True, null=True)
    namemrkcar = models.CharField(max_length=250, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)
    tipts = models.CharField(max_length=2, blank=True, null=True)
    tipts3 = models.CharField(max_length=3, blank=True, null=True)
    tiptsname = models.CharField(max_length=150, blank=True, null=True)
    kategts = models.CharField(max_length=2, blank=True, null=True)
    mest = models.IntegerField(default=0, blank=True, null=True)
    god = models.IntegerField(default=0, blank=True, null=True)
    moddvig = models.CharField(max_length=15, blank=True, null=True)
    numdvig = models.CharField(max_length=40, blank=True, null=True)
    numkper = models.CharField(max_length=40, blank=True, null=True)
    nummost = models.CharField(max_length=80, blank=True, null=True)
    shassi = models.CharField(max_length=40, blank=True, null=True)
    kuzov = models.CharField(max_length=40, blank=True, null=True)
    kabina = models.CharField(max_length=40, blank=True, null=True)
    zvet = models.CharField(max_length=3, blank=True, null=True)
    listcol = models.CharField(max_length=43, blank=True, null=True)
    powerls = models.DecimalField(default=0.00, max_digits=8, decimal_places=2, blank=True, null=True)
    powerkw = models.DecimalField(default=0.00, max_digits=8, decimal_places=2, blank=True, null=True)
    obdvig = models.IntegerField(default=0, blank=True, null=True)
    dvkol = models.IntegerField(default=0, blank=True, null=True)
    tipdv = models.CharField(max_length=2, blank=True, null=True)
    tipdv2 = models.CharField(max_length=2, blank=True, null=True)
    viddvig = models.CharField(max_length=2, blank=True, null=True)
    ekoclass = models.CharField(max_length=1, blank=True, null=True)
    maxmass = models.IntegerField(default=0, blank=True, null=True)
    minmass = models.IntegerField(default=0, blank=True, null=True)
    maxspeed = models.IntegerField(default=0, blank=True, null=True)
    width = models.IntegerField(default=0, blank=True, null=True)
    height = models.IntegerField(default=0, blank=True, null=True)
    length = models.IntegerField(default=0, blank=True, null=True)
    kodizgot = models.CharField(max_length=3, blank=True, null=True)
    izgotov = models.CharField(max_length=150, blank=True, null=True)
    strizg = models.CharField(max_length=2, blank=True, null=True)
    izgpost = models.CharField(max_length=9, blank=True, null=True)
    izgstr = models.CharField(max_length=2, blank=True, null=True)
    izgsubd = models.CharField(max_length=35, blank=True, null=True)
    izgcity = models.CharField(max_length=35, blank=True, null=True)
    izgstreet = models.CharField(max_length=35, blank=True, null=True)
    numodob = models.CharField(max_length=50, blank=True, null=True)
    datodob = models.DateField(blank=True, null=True)
    orgodob = models.CharField(max_length=150, blank=True, null=True)
    strvyvoz = models.CharField(max_length=2, blank=True, null=True)
    lic = models.CharField(max_length=1, blank=True, null=True)
    fam = models.CharField(max_length=30, blank=True, null=True)
    ima = models.CharField(max_length=25, blank=True, null=True)
    otc = models.CharField(max_length=25, blank=True, null=True)
    okpo = models.CharField(max_length=10, blank=True, null=True)
    inn = models.CharField(max_length=12, blank=True, null=True)
    kpp = models.CharField(max_length=9, blank=True, null=True)
    kod_dul = models.CharField(max_length=7, blank=True, null=True)
    abbrev_dul = models.CharField(max_length=25, blank=True, null=True)
    ser_dul = models.CharField(max_length=11, blank=True, null=True)
    nom_dul = models.CharField(max_length=25, blank=True, null=True)
    org_dul = models.CharField(max_length=150, blank=True, null=True)
    dat_dul = models.DateField(blank=True, null=True)
    namesob = models.CharField(max_length=150, blank=True, null=True)
    sobpost = models.CharField(max_length=9, blank=True, null=True)
    sobstr = models.CharField(max_length=2, blank=True, null=True)
    sobsubd = models.CharField(max_length=35, blank=True, null=True)
    sobcity = models.CharField(max_length=35, blank=True, null=True)
    sobstreet = models.CharField(max_length=50, blank=True, null=True)
    udvvoz = models.CharField(max_length=10, blank=True, null=True)
    datud = models.DateField(blank=True, null=True)
    lnpu = models.CharField(max_length=4, blank=True, null=True)
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    ctamogr = models.CharField(max_length=3, blank=True, null=True)
    tamogr = models.CharField(max_length=250, blank=True, null=True)
    ogrdate = models.DateField(blank=True, null=True)
    tamspec = models.CharField(max_length=250, blank=True, null=True)
    specdate = models.DateField(blank=True, null=True)
    numpts = models.CharField(max_length=15, blank=True, null=True)
    datpts = models.DateField(blank=True, null=True)
    timpts = models.CharField(max_length=8, blank=True, null=True)
    lnp = models.CharField(max_length=4, blank=True, null=True)
    work = models.IntegerField(default=0, blank=True, null=True)
    p_ts = models.CharField(max_length=1, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    g33 = models.CharField(max_length=10, blank=True, null=True)
    naimtd = models.CharField(max_length=250, blank=True, null=True)
    numtd = models.CharField(max_length=50, blank=True, null=True)
    dattd = models.DateField(blank=True, null=True)
    emergdev = models.CharField(max_length=50, blank=True, null=True)
    numz = models.CharField(max_length=23, blank=True, null=True)
    datz = models.DateField(blank=True, null=True)
    dateout = models.DateField(blank=True, null=True)
    timeout = models.CharField(max_length=8, blank=True, null=True)
    datemodi = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    imodi = models.CharField(max_length=1, blank=True, null=True)
    ind_k = models.CharField(max_length=1, blank=True, null=True)
    d_state = models.CharField(max_length=19, blank=True, null=True)
    d_unload = models.CharField(max_length=19, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)
    strizgc = models.CharField(max_length=3, blank=True, null=True)
    adrizg = models.CharField(max_length=50, blank=True, null=True)
    strvyvozc = models.CharField(max_length=3, blank=True, null=True)
    adressob = models.CharField(max_length=80, blank=True, null=True)
    ed_idid = models.CharField(max_length=36, blank=True, null=True)
    numptso = models.CharField(max_length=11, blank=True, null=True)
    datptso = models.DateField(blank=True, null=True)
    stsptso = models.CharField(max_length=1, blank=True, null=True)
    ub_idid = models.CharField(max_length=36, blank=True, null=True)
    ed_numepts = models.CharField(max_length=36, blank=True, null=True)
    yc_status = models.CharField(max_length=1, blank=True, null=True)
    yc_tpo = models.CharField(max_length=26, blank=True, null=True)
    yc_matter = models.CharField(max_length=2, blank=True, null=True)
    numepts = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dclcrdts'


class Dcldinf2(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    type_info = models.CharField(max_length=1, blank=True, null=True)
    numpredd = models.IntegerField(default=0, blank=True, null=True)
    ngr = models.CharField(max_length=2, blank=True, null=True)
    typ_ngr = models.CharField(max_length=2, blank=True, null=True)
    g32g = models.IntegerField(default=0, blank=True, null=True)
    numrec = models.IntegerField(default=0, blank=True, null=True)
    text1 = models.CharField(max_length=250, blank=True, null=True)
    text2 = models.CharField(max_length=50, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dcldinf2'


class Dcldinfo(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    ngr = models.CharField(max_length=2, blank=True, null=True)
    typ_ngr = models.CharField(max_length=2, blank=True, null=True)
    g32g = models.IntegerField(default=0, blank=True, null=True)
    numrec = models.IntegerField(default=0, blank=True, null=True)
    text1 = models.CharField(max_length=250, blank=True, null=True)
    ind_text = models.CharField(max_length=3, blank=True, null=True)
    text2 = models.CharField(max_length=50, blank=True, null=True)
    typ_izm = models.CharField(max_length=1, blank=True, null=True)
    kolvo = models.DecimalField(default=0.00, max_digits=16, decimal_places=4, blank=True, null=True)
    code_edi = models.CharField(max_length=3, blank=True, null=True)
    name_edi = models.CharField(max_length=17, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dcldinfo'


class Dcldog(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    dogn = models.CharField(max_length=50, blank=True, null=True)
    dogd = models.DateField(blank=True, null=True)
    pasp = models.CharField(max_length=25, blank=True, null=True)
    paspbank = models.CharField(max_length=70, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dcldog'


class Dcldoga(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    dogn = models.CharField(max_length=50, blank=True, null=True)
    dogd = models.DateField(blank=True, null=True)
    dogaddn = models.CharField(max_length=50, blank=True, null=True)
    dogaddd = models.DateField(blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dcldoga'


class Dcldogt(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    dogn = models.CharField(max_length=50, blank=True, null=True)
    dogd = models.DateField(blank=True, null=True)
    dognpp = models.IntegerField(default=0, blank=True, null=True)
    dogorg = models.CharField(max_length=150, blank=True, null=True)
    dogcountry = models.CharField(max_length=2, blank=True, null=True)
    origcountr = models.CharField(max_length=2, blank=True, null=True)
    terms = models.CharField(max_length=3, blank=True, null=True)
    termspoint = models.CharField(max_length=50, blank=True, null=True)
    termspass = models.CharField(max_length=250, blank=True, null=True)
    qmain = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    qadd = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    qaddmeas = models.CharField(max_length=3, blank=True, null=True)
    price = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    prval = models.CharField(max_length=3, blank=True, null=True)
    prmeas = models.CharField(max_length=3, blank=True, null=True)
    prtot = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    prtotval = models.CharField(max_length=3, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dcldogt'


class Dclkmp(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    kmpfb = models.IntegerField(default=0, blank=True, null=True)
    kmpnm = models.CharField(max_length=250, blank=True, null=True)
    kmpkod = models.CharField(max_length=10, blank=True, null=True)
    kmpadd = models.CharField(max_length=3, blank=True, null=True)
    kmpqadd = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    kmpqmain = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    kmppr = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    kmpprval = models.CharField(max_length=3, blank=True, null=True)
    kmpqk = models.IntegerField(default=0, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dclkmp'


class Dclkmpk(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    kmpfb = models.IntegerField(default=0, blank=True, null=True)
    kmpk = models.IntegerField(default=0, blank=True, null=True)
    kmpkid = models.IntegerField(default=0, blank=True, null=True)
    kmpknum = models.CharField(max_length=50, blank=True, null=True)
    kmpnm = models.CharField(max_length=250, blank=True, null=True)
    kmpkod = models.CharField(max_length=10, blank=True, null=True)
    kmpadd = models.CharField(max_length=3, blank=True, null=True)
    kmpqadd = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    kmpqmain = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    kmppr = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    kmpprval = models.CharField(max_length=3, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dclkmpk'


class Dcllistd(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    tlist = models.IntegerField(default=0, blank=True, null=True)
    lrazdel = models.IntegerField(default=0, blank=True, null=True)
    lrec = models.IntegerField(default=0, blank=True, null=True)
    quer = models.IntegerField(default=0, blank=True, null=True)
    querd = models.DateField(blank=True, null=True)
    g441 = models.CharField(max_length=5, blank=True, null=True)
    g444 = models.CharField(max_length=250, blank=True, null=True)
    g442 = models.CharField(max_length=50, blank=True, null=True)
    g443 = models.DateField(blank=True, null=True)
    lstatdoc = models.CharField(max_length=1, blank=True, null=True)
    lfrmpred = models.CharField(max_length=1, blank=True, null=True)
    lpredsaf = models.CharField(max_length=1, blank=True, null=True)
    prpresent = models.CharField(max_length=1, blank=True, null=True)
    prsdecl = models.CharField(max_length=1, blank=True, null=True)
    id_bdrd = models.CharField(max_length=36, blank=True, null=True)
    requestid = models.CharField(max_length=36, blank=True, null=True)
    docmodid = models.CharField(max_length=8, blank=True, null=True)
    executbody = models.CharField(max_length=10, blank=True, null=True)
    scanid = models.CharField(max_length=36, blank=True, null=True)
    llist = models.IntegerField(default=0, blank=True, null=True)
    lkol = models.IntegerField(default=0, blank=True, null=True)
    l071 = models.CharField(max_length=8, blank=True, null=True)
    l072 = models.DateField(blank=True, null=True)
    l073 = models.CharField(max_length=7, blank=True, null=True)
    part_num = models.IntegerField(default=0, blank=True, null=True)
    pzn_last = models.CharField(max_length=1, blank=True, null=True)
    lprim = models.CharField(max_length=128, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)
    ed_aid = models.CharField(max_length=50, blank=True, null=True)
    ed_adid = models.CharField(max_length=50, blank=True, null=True)
    ed_idid = models.CharField(max_length=36, blank=True, null=True)
    ed_lid = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dcllistd'


class Dcllisth(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    hlist = models.IntegerField(default=0, blank=True, null=True)
    g141 = models.CharField(max_length=12, blank=True, null=True)
    g142 = models.CharField(max_length=150, blank=True, null=True)
    g142a = models.CharField(max_length=150, blank=True, null=True)
    g147 = models.CharField(max_length=9, blank=True, null=True)
    g541 = models.CharField(max_length=14, blank=True, null=True)
    g541d = models.DateField(blank=True, null=True)
    tpriem = models.CharField(max_length=8, blank=True, null=True)
    dbegctrl = models.DateField(blank=True, null=True)
    tbegctrl = models.CharField(max_length=8, blank=True, null=True)
    tregistr = models.CharField(max_length=8, blank=True, null=True)
    lnpbegctrl = models.CharField(max_length=4, blank=True, null=True)
    gd0 = models.CharField(max_length=2, blank=True, null=True)
    gd1 = models.DateField(blank=True, null=True)
    gd11 = models.CharField(max_length=8, blank=True, null=True)
    gd00 = models.CharField(max_length=250, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)
    ed_idid = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dcllisth'


class Dcllistl(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    tlist = models.IntegerField(default=0, blank=True, null=True)
    dlist = models.DateField(blank=True, null=True)
    lnplist = models.CharField(max_length=4, blank=True, null=True)
    l41 = models.CharField(max_length=150, blank=True, null=True)
    l41nm = models.CharField(max_length=150, blank=True, null=True)
    l41mdnm = models.CharField(max_length=150, blank=True, null=True)
    l43 = models.CharField(max_length=250, blank=True, null=True)
    l44 = models.CharField(max_length=50, blank=True, null=True)
    l45 = models.DateField(blank=True, null=True)
    l51 = models.CharField(max_length=2, blank=True, null=True)
    l51a = models.CharField(max_length=15, blank=True, null=True)
    l521 = models.CharField(max_length=11, blank=True, null=True)
    l52 = models.CharField(max_length=25, blank=True, null=True)
    l523 = models.CharField(max_length=150, blank=True, null=True)
    l53 = models.DateField(blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dcllistl'


class Dclpasp(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    g2810 = models.CharField(max_length=1, blank=True, null=True)
    pasp = models.CharField(max_length=25, blank=True, null=True)
    paspd = models.DateField(blank=True, null=True)
    paspdd = models.DateField(blank=True, null=True)
    pasp0 = models.CharField(max_length=1, blank=True, null=True)
    pasp1 = models.CharField(max_length=25, blank=True, null=True)
    pasp1dd = models.DateField(blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dclpasp'


class Dclpk(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    pksign = models.CharField(max_length=1, blank=True, null=True)
    pkvid = models.CharField(max_length=2, blank=True, null=True)
    pkkolvo = models.IntegerField(default=0, blank=True, null=True)
    pkinf = models.CharField(max_length=150, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dclpk'


class Dclplat2(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    numpredd = models.IntegerField(default=0, blank=True, null=True)
    g470 = models.CharField(max_length=1, blank=True, null=True)
    g471 = models.CharField(max_length=4, blank=True, null=True)
    g471npp = models.IntegerField(default=0, blank=True, null=True)
    g472 = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    g4722 = models.CharField(max_length=50, blank=True, null=True)
    g4721 = models.CharField(max_length=3, blank=True, null=True)
    g473 = models.DecimalField(default=0.00, max_digits=12, decimal_places=6, blank=True, null=True)
    g4731 = models.CharField(max_length=1, blank=True, null=True)
    g4732 = models.CharField(max_length=3, blank=True, null=True)
    g4733 = models.CharField(max_length=3, blank=True, null=True)
    g4734 = models.DecimalField(default=0.00, max_digits=8, decimal_places=3, blank=True, null=True)
    npp = models.IntegerField(default=0, blank=True, null=True)
    g474 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    g4741 = models.CharField(max_length=3, blank=True, null=True)
    g475 = models.CharField(max_length=2, blank=True, null=True)
    g473z1_2 = models.CharField(max_length=1, blank=True, null=True)
    g473_2 = models.DecimalField(default=0.00, max_digits=12, decimal_places=6, blank=True, null=True)
    g4731_2 = models.CharField(max_length=1, blank=True, null=True)
    g4732_2 = models.CharField(max_length=3, blank=True, null=True)
    g4733_2 = models.CharField(max_length=3, blank=True, null=True)
    g4734_2 = models.DecimalField(default=0.00, max_digits=8, decimal_places=3, blank=True, null=True)
    g473z1_3 = models.CharField(max_length=1, blank=True, null=True)
    g473_3 = models.DecimalField(default=0.00, max_digits=12, decimal_places=6, blank=True, null=True)
    g4731_3 = models.CharField(max_length=1, blank=True, null=True)
    g4732_3 = models.CharField(max_length=3, blank=True, null=True)
    g4733_3 = models.CharField(max_length=3, blank=True, null=True)
    g4734_3 = models.DecimalField(default=0.00, max_digits=8, decimal_places=3, blank=True, null=True)
    g473z2_2 = models.IntegerField(default=0, blank=True, null=True)
    g4730 = models.DateField(blank=True, null=True)
    g4740 = models.DateField(blank=True, null=True)
    g47_nd = models.IntegerField(default=0, blank=True, null=True)
    g47_ns = models.IntegerField(default=0, blank=True, null=True)
    g47_nm = models.IntegerField(default=0, blank=True, null=True)
    g47_tr = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, blank=True, null=True)
    g47_g40 = models.IntegerField(default=0, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dclplat2'


class Dclplatr(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    g470 = models.CharField(max_length=1, blank=True, null=True)
    g471 = models.CharField(max_length=4, blank=True, null=True)
    g471npp = models.IntegerField(default=0, blank=True, null=True)
    g472 = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    g4722 = models.CharField(max_length=50, blank=True, null=True)
    g4721 = models.CharField(max_length=3, blank=True, null=True)
    g4723 = models.CharField(max_length=3, blank=True, null=True)
    g473 = models.DecimalField(default=0.00, max_digits=12, decimal_places=6, blank=True, null=True)
    g4731 = models.CharField(max_length=1, blank=True, null=True)
    g4732 = models.CharField(max_length=3, blank=True, null=True)
    g4733 = models.CharField(max_length=3, blank=True, null=True)
    g4734 = models.DecimalField(default=0.00, max_digits=8, decimal_places=3, blank=True, null=True)
    npp = models.IntegerField(default=0, blank=True, null=True)
    g474 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    g4741 = models.CharField(max_length=3, blank=True, null=True)
    g475 = models.CharField(max_length=2, blank=True, null=True)
    g473z1_2 = models.CharField(max_length=1, blank=True, null=True)
    g473_2 = models.DecimalField(default=0.00, max_digits=12, decimal_places=6, blank=True, null=True)
    g4731_2 = models.CharField(max_length=1, blank=True, null=True)
    g4732_2 = models.CharField(max_length=3, blank=True, null=True)
    g4733_2 = models.CharField(max_length=3, blank=True, null=True)
    g4734_2 = models.DecimalField(default=0.00, max_digits=8, decimal_places=3, blank=True, null=True)
    g473z1_3 = models.CharField(max_length=1, blank=True, null=True)
    g473_3 = models.DecimalField(default=0.00, max_digits=12, decimal_places=6, blank=True, null=True)
    g4731_3 = models.CharField(max_length=1, blank=True, null=True)
    g4732_3 = models.CharField(max_length=3, blank=True, null=True)
    g4733_3 = models.CharField(max_length=3, blank=True, null=True)
    g4734_3 = models.DecimalField(default=0.00, max_digits=8, decimal_places=3, blank=True, null=True)
    g473z2_2 = models.IntegerField(default=0, blank=True, null=True)
    g4730 = models.DateField(blank=True, null=True)
    g4740 = models.DateField(blank=True, null=True)
    g47_nd = models.IntegerField(default=0, blank=True, null=True)
    g47_ns = models.IntegerField(default=0, blank=True, null=True)
    g47_nm = models.IntegerField(default=0, blank=True, null=True)
    g47_tr = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, blank=True, null=True)
    g47trf = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, blank=True, null=True)
    g47_g40 = models.IntegerField(default=0, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dclplatr'


class Dclplatv(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    gb0 = models.CharField(max_length=1, blank=True, null=True)
    gb1 = models.CharField(max_length=4, blank=True, null=True)
    gb2 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    gb3 = models.CharField(max_length=3, blank=True, null=True)
    gb4 = models.DecimalField(default=0.00, max_digits=10, decimal_places=4, blank=True, null=True)
    gb5 = models.CharField(max_length=2, blank=True, null=True)
    iret = models.IntegerField(default=0, blank=True, null=True)
    g48doccode = models.CharField(max_length=5, blank=True, null=True)
    g48 = models.DateField(blank=True, null=True)
    g481 = models.CharField(max_length=1, blank=True, null=True)
    g482 = models.CharField(max_length=50, blank=True, null=True)
    g482d = models.DateField(blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dclplatv'


class Dclpredd(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    numrec = models.IntegerField(default=0, blank=True, null=True)
    g40_cntry = models.CharField(max_length=2, blank=True, null=True)
    g40_0 = models.CharField(max_length=2, blank=True, null=True)
    prevnumtyp = models.CharField(max_length=1, blank=True, null=True)
    g40_naim = models.CharField(max_length=250, blank=True, null=True)
    g40_1 = models.CharField(max_length=8, blank=True, null=True)
    g40_2 = models.DateField(blank=True, null=True)
    g40_21 = models.CharField(max_length=2, blank=True, null=True)
    g40_3 = models.CharField(max_length=9, blank=True, null=True)
    g40_31 = models.CharField(max_length=2, blank=True, null=True)
    g40_4 = models.IntegerField(default=0, blank=True, null=True)
    g40_doctyp = models.CharField(max_length=5, blank=True, null=True)
    g40tnved = models.CharField(max_length=10, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dclpredd'


class Dclquerd(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    quer = models.IntegerField(default=0, blank=True, null=True)
    querd = models.DateField(blank=True, null=True)
    qrec = models.IntegerField(default=0, blank=True, null=True)
    g441 = models.CharField(max_length=5, blank=True, null=True)
    g444 = models.CharField(max_length=250, blank=True, null=True)
    g442 = models.CharField(max_length=50, blank=True, null=True)
    g443 = models.DateField(blank=True, null=True)
    qpurpose = models.CharField(max_length=250, blank=True, null=True)
    qprim = models.CharField(max_length=250, blank=True, null=True)
    qtam = models.CharField(max_length=40, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)
    ed_aid = models.CharField(max_length=50, blank=True, null=True)
    ed_adid = models.CharField(max_length=50, blank=True, null=True)
    ed_idid = models.CharField(max_length=36, blank=True, null=True)
    ed_lid = models.CharField(max_length=36, blank=True, null=True)
    ed_snd = models.CharField(max_length=36, blank=True, null=True)
    ed_cnv = models.CharField(max_length=36, blank=True, null=True)
    ed_sts = models.CharField(max_length=1, blank=True, null=True)
    ed_idam = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dclquerd'


class Dclquerh(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    quer = models.IntegerField(default=0, blank=True, null=True)
    querd = models.DateField(blank=True, null=True)
    qnotifytyp = models.CharField(max_length=1, blank=True, null=True)
    qktam = models.CharField(max_length=8, blank=True, null=True)
    qprnedtc = models.CharField(max_length=250, blank=True, null=True)
    qdocd = models.DateField(blank=True, null=True)
    qktcd = models.DateField(blank=True, null=True)
    qfio = models.CharField(max_length=40, blank=True, null=True)
    qlnp = models.CharField(max_length=4, blank=True, null=True)
    qcomm = models.CharField(max_length=1, blank=True, null=True)
    qsend = models.CharField(max_length=50, blank=True, null=True)
    qsendpost = models.CharField(max_length=9, blank=True, null=True)
    qsendcount = models.CharField(max_length=2, blank=True, null=True)
    qsendsubd = models.CharField(max_length=50, blank=True, null=True)
    qsendcity = models.CharField(max_length=35, blank=True, null=True)
    qsendstree = models.CharField(max_length=50, blank=True, null=True)
    qsendd = models.DateField(blank=True, null=True)
    qsendtam = models.CharField(max_length=40, blank=True, null=True)
    qrecv = models.CharField(max_length=40, blank=True, null=True)
    qrecvd = models.DateField(blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)
    ed_cnv = models.CharField(max_length=36, blank=True, null=True)
    ed_idam = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dclquerh'


class Dclquern(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    quer = models.IntegerField(default=0, blank=True, null=True)
    qrec = models.IntegerField(default=0, blank=True, null=True)
    qprnedtc = models.CharField(max_length=250, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dclquern'


class Dclrinfo(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    npart = models.IntegerField(default=0, blank=True, null=True)
    gr013 = models.CharField(max_length=2, blank=True, null=True)
    gr0131 = models.CharField(max_length=5, blank=True, null=True)
    gr014 = models.DateField(blank=True, null=True)
    gr015 = models.CharField(max_length=6, blank=True, null=True)
    gr0151 = models.IntegerField(default=0, blank=True, null=True)
    gr051 = models.CharField(max_length=3, blank=True, null=True)
    kod_info = models.CharField(max_length=1, blank=True, null=True)
    npp_str = models.IntegerField(default=0, blank=True, null=True)
    gr0311 = models.CharField(max_length=2, blank=True, null=True)
    text_info = models.CharField(max_length=255, blank=True, null=True)
    point_code = models.CharField(max_length=2, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dclrinfo'


class Dclriska(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    npart = models.IntegerField(default=0, blank=True, null=True)
    gr013 = models.CharField(max_length=2, blank=True, null=True)
    gr0131 = models.CharField(max_length=5, blank=True, null=True)
    gr014 = models.DateField(blank=True, null=True)
    gr015 = models.CharField(max_length=6, blank=True, null=True)
    gr0151 = models.IntegerField(default=0, blank=True, null=True)
    gr051 = models.CharField(max_length=3, blank=True, null=True)
    npp_str = models.IntegerField(default=0, blank=True, null=True)
    gr0302 = models.CharField(max_length=4, blank=True, null=True)
    gr0302_1 = models.CharField(max_length=2, blank=True, null=True)
    gr0302_2 = models.CharField(max_length=20, blank=True, null=True)
    point_code = models.CharField(max_length=2, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dclriska'


class Dclriskb(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    npart = models.IntegerField(default=0, blank=True, null=True)
    gr013 = models.CharField(max_length=2, blank=True, null=True)
    gr0131 = models.CharField(max_length=5, blank=True, null=True)
    gr014 = models.DateField(blank=True, null=True)
    gr015 = models.CharField(max_length=6, blank=True, null=True)
    gr0151 = models.IntegerField(default=0, blank=True, null=True)
    gr051 = models.CharField(max_length=3, blank=True, null=True)
    gr0301 = models.CharField(max_length=2, blank=True, null=True)
    rez_vtd = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    rez_vtdap = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    rez_tnved = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    rez_ktc = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    point_code = models.CharField(max_length=2, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dclriskb'


class Dclriskc(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    npart = models.IntegerField(default=0, blank=True, null=True)
    gr013 = models.CharField(max_length=2, blank=True, null=True)
    gr0131 = models.CharField(max_length=5, blank=True, null=True)
    gr014 = models.DateField(blank=True, null=True)
    gr015 = models.CharField(max_length=6, blank=True, null=True)
    gr0151 = models.IntegerField(default=0, blank=True, null=True)
    gr051 = models.CharField(max_length=3, blank=True, null=True)
    point_code = models.CharField(max_length=2, blank=True, null=True)
    container = models.CharField(max_length=17, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dclriskc'


class Dclriskd(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    npart = models.IntegerField(default=0, blank=True, null=True)
    gr013 = models.CharField(max_length=2, blank=True, null=True)
    gr0131 = models.CharField(max_length=5, blank=True, null=True)
    gr014 = models.DateField(blank=True, null=True)
    gr015 = models.CharField(max_length=6, blank=True, null=True)
    gr0151 = models.IntegerField(default=0, blank=True, null=True)
    gr051 = models.CharField(max_length=3, blank=True, null=True)
    kodatr = models.CharField(max_length=2, blank=True, null=True)
    priznatr = models.CharField(max_length=1, blank=True, null=True)
    textatr = models.CharField(max_length=6, blank=True, null=True)
    point_code = models.CharField(max_length=2, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dclriskd'


class Dclriskm(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    npart = models.IntegerField(default=0, blank=True, null=True)
    gr013 = models.CharField(max_length=2, blank=True, null=True)
    gr0131 = models.CharField(max_length=5, blank=True, null=True)
    gr014 = models.DateField(blank=True, null=True)
    gr015 = models.CharField(max_length=6, blank=True, null=True)
    gr0151 = models.IntegerField(default=0, blank=True, null=True)
    gr022 = models.DateField(blank=True, null=True)
    gr022a = models.CharField(max_length=8, blank=True, null=True)
    gr023 = models.CharField(max_length=4, blank=True, null=True)
    gr024 = models.CharField(max_length=40, blank=True, null=True)
    gr025 = models.CharField(max_length=8, blank=True, null=True)
    gr0301 = models.CharField(max_length=2, blank=True, null=True)
    gr0302 = models.CharField(max_length=4, blank=True, null=True)
    gr031 = models.CharField(max_length=255, blank=True, null=True)
    gr051 = models.CharField(max_length=3, blank=True, null=True)
    gr0511 = models.IntegerField(default=0, blank=True, null=True)
    gr0512 = models.IntegerField(default=0, blank=True, null=True)
    gr0513 = models.CharField(max_length=3, blank=True, null=True)
    gr052 = models.CharField(max_length=1, blank=True, null=True)
    gr053 = models.CharField(max_length=1, blank=True, null=True)
    gr054 = models.CharField(max_length=2, blank=True, null=True)
    gr055 = models.CharField(max_length=2, blank=True, null=True)
    coordin = models.BooleanField(blank=True, null=True)
    point_code = models.CharField(max_length=2, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dclriskm'


class Dclriskp(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    num_pp = models.IntegerField(default=0, blank=True, null=True)
    num_oup = models.IntegerField(default=0, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    gr013 = models.CharField(max_length=2, blank=True, null=True)
    gr0131 = models.CharField(max_length=5, blank=True, null=True)
    gr014 = models.DateField(blank=True, null=True)
    gr015 = models.CharField(max_length=6, blank=True, null=True)
    gr0151 = models.IntegerField(default=0, blank=True, null=True)
    k470 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    k4701 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dclriskp'


class Dclrsinf(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    npart = models.IntegerField(default=0, blank=True, null=True)
    gr013 = models.CharField(max_length=2, blank=True, null=True)
    gr0131 = models.CharField(max_length=5, blank=True, null=True)
    gr014 = models.DateField(blank=True, null=True)
    gr015 = models.CharField(max_length=6, blank=True, null=True)
    gr0151 = models.IntegerField(default=0, blank=True, null=True)
    kod_inf = models.CharField(max_length=1, blank=True, null=True)
    npp_str = models.IntegerField(default=0, blank=True, null=True)
    text_inf = models.CharField(max_length=255, blank=True, null=True)
    point_code = models.CharField(max_length=2, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dclrsinf'


class Dclrsk93(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    npart = models.IntegerField(default=0, blank=True, null=True)
    g071_pd = models.CharField(max_length=8, blank=True, null=True)
    g072_pd = models.DateField(blank=True, null=True)
    g073_pd = models.CharField(max_length=7, blank=True, null=True)
    g32_pd = models.IntegerField(default=0, blank=True, null=True)
    gr013 = models.CharField(max_length=2, blank=True, null=True)
    gr0131 = models.CharField(max_length=5, blank=True, null=True)
    gr014 = models.DateField(blank=True, null=True)
    gr015 = models.CharField(max_length=6, blank=True, null=True)
    gr0151 = models.IntegerField(default=0, blank=True, null=True)
    gr051 = models.CharField(max_length=3, blank=True, null=True)
    gr0301 = models.CharField(max_length=2, blank=True, null=True)
    rez_tnved = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    gr0302 = models.CharField(max_length=4, blank=True, null=True)
    gr0302_1 = models.CharField(max_length=1, blank=True, null=True)
    gr0302_2 = models.CharField(max_length=20, blank=True, null=True)
    point_code = models.CharField(max_length=2, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dclrsk93'


class Dclrsmpr(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    npart = models.IntegerField(default=0, blank=True, null=True)
    gr0131 = models.CharField(max_length=5, blank=True, null=True)
    gr013 = models.CharField(max_length=2, blank=True, null=True)
    gr014 = models.DateField(blank=True, null=True)
    gr015 = models.CharField(max_length=6, blank=True, null=True)
    gr0151 = models.IntegerField(default=0, blank=True, null=True)
    point_code = models.CharField(max_length=2, blank=True, null=True)
    gr051 = models.CharField(max_length=3, blank=True, null=True)
    note_code = models.CharField(max_length=3, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dclrsmpr'


class Dclrsnfi(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    npart = models.IntegerField(default=0, blank=True, null=True)
    gr013 = models.CharField(max_length=2, blank=True, null=True)
    gr0131 = models.CharField(max_length=5, blank=True, null=True)
    gr014 = models.DateField(blank=True, null=True)
    gr015 = models.CharField(max_length=6, blank=True, null=True)
    gr0151 = models.IntegerField(default=0, blank=True, null=True)
    kod_inf = models.CharField(max_length=4, blank=True, null=True)
    npp_str = models.IntegerField(default=0, blank=True, null=True)
    text_inf = models.CharField(max_length=255, blank=True, null=True)
    point_code = models.CharField(max_length=2, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dclrsnfi'


class Dclslotm(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    ngr = models.CharField(max_length=2, blank=True, null=True)
    gc_01 = models.CharField(max_length=1, blank=True, null=True)
    gc_02 = models.CharField(max_length=2, blank=True, null=True)
    gc_03 = models.CharField(max_length=1, blank=True, null=True)
    nrecc = models.IntegerField(default=0, blank=True, null=True)
    krecc = models.CharField(max_length=2, blank=True, null=True)
    gc_1 = models.CharField(max_length=150, blank=True, null=True)
    gc_nresh = models.CharField(max_length=29, blank=True, null=True)
    inpi_guid = models.CharField(max_length=32, blank=True, null=True)
    gc_doc = models.CharField(max_length=50, blank=True, null=True)
    gc_doc0 = models.CharField(max_length=1, blank=True, null=True)
    gc_docd = models.DateField(blank=True, null=True)
    gc_2 = models.DateField(blank=True, null=True)
    gc_21 = models.CharField(max_length=8, blank=True, null=True)
    gc_2k = models.CharField(max_length=2, blank=True, null=True)
    gc_opoutp = models.CharField(max_length=1, blank=True, null=True)
    gc_ksoutp = models.CharField(max_length=2, blank=True, null=True)
    gc_3 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    gc_31 = models.CharField(max_length=4, blank=True, null=True)
    gc_32 = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, blank=True, null=True)
    gc_4 = models.CharField(max_length=3, blank=True, null=True)
    gc_42 = models.CharField(max_length=3, blank=True, null=True)
    gc_5 = models.CharField(max_length=70, blank=True, null=True)
    gc_6 = models.CharField(max_length=4, blank=True, null=True)
    gc_7 = models.CharField(max_length=40, blank=True, null=True)
    gc_8 = models.DateField(blank=True, null=True)
    gc_81 = models.CharField(max_length=8, blank=True, null=True)
    gc_9 = models.DateField(blank=True, null=True)
    gc_9m = models.IntegerField(default=0, blank=True, null=True)
    gc_nm_itn = models.CharField(max_length=13, blank=True, null=True)
    gc_nm = models.CharField(max_length=150, blank=True, null=True)
    gc_ogrn = models.CharField(max_length=15, blank=True, null=True)
    gc_inn = models.CharField(max_length=12, blank=True, null=True)
    gc_kpp = models.CharField(max_length=9, blank=True, null=True)
    gc_ktam = models.CharField(max_length=8, blank=True, null=True)
    gc_10 = models.DateField(blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dclslotm'


class Dclsltov(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    ngr = models.CharField(max_length=2, blank=True, null=True)
    gc_01 = models.CharField(max_length=1, blank=True, null=True)
    gc_02 = models.CharField(max_length=2, blank=True, null=True)
    gc_03 = models.CharField(max_length=1, blank=True, null=True)
    nrecc = models.IntegerField(default=0, blank=True, null=True)
    krecc = models.CharField(max_length=2, blank=True, null=True)
    gc_1 = models.CharField(max_length=150, blank=True, null=True)
    gc_nresh = models.CharField(max_length=29, blank=True, null=True)
    gc_doc = models.CharField(max_length=50, blank=True, null=True)
    gc_doc0 = models.CharField(max_length=1, blank=True, null=True)
    gc_docd = models.DateField(blank=True, null=True)
    gc_2 = models.DateField(blank=True, null=True)
    gc_21 = models.CharField(max_length=8, blank=True, null=True)
    gc_2k = models.CharField(max_length=2, blank=True, null=True)
    gc_3 = models.DateField(blank=True, null=True)
    gc_31 = models.CharField(max_length=8, blank=True, null=True)
    gc_kol = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    gc_4 = models.CharField(max_length=3, blank=True, null=True)
    gc_5 = models.CharField(max_length=70, blank=True, null=True)
    gc_6 = models.CharField(max_length=4, blank=True, null=True)
    gc_7 = models.CharField(max_length=40, blank=True, null=True)
    gc_9 = models.DateField(blank=True, null=True)
    gc_9m = models.IntegerField(default=0, blank=True, null=True)
    gc_nm_itn = models.CharField(max_length=13, blank=True, null=True)
    gc_nm = models.CharField(max_length=150, blank=True, null=True)
    gc_ogrn = models.CharField(max_length=15, blank=True, null=True)
    gc_inn = models.CharField(max_length=12, blank=True, null=True)
    gc_kpp = models.CharField(max_length=9, blank=True, null=True)
    gc_ktam = models.CharField(max_length=8, blank=True, null=True)
    gc_10 = models.DateField(blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dclsltov'


class Dclsumpp(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    gb1 = models.CharField(max_length=4, blank=True, null=True)
    gb3 = models.CharField(max_length=3, blank=True, null=True)
    gb5 = models.CharField(max_length=2, blank=True, null=True)
    iret = models.IntegerField(default=0, blank=True, null=True)
    numpdok = models.CharField(max_length=50, blank=True, null=True)
    datpdok = models.DateField(blank=True, null=True)
    sum_all = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    sumpdok = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    valpdok = models.CharField(max_length=3, blank=True, null=True)
    datpostd = models.DateField(blank=True, null=True)
    datpaymt = models.DateField(blank=True, null=True)
    innplat = models.CharField(max_length=12, blank=True, null=True)
    kppplat = models.CharField(max_length=9, blank=True, null=True)
    lnpins = models.CharField(max_length=4, blank=True, null=True)
    fioins = models.CharField(max_length=40, blank=True, null=True)
    datins = models.DateField(blank=True, null=True)
    timins = models.CharField(max_length=8, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dclsumpp'


class Dcltcim(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    numrec = models.IntegerField(default=0, blank=True, null=True)
    firstcimid = models.CharField(max_length=20, blank=True, null=True)
    lastcimid = models.CharField(max_length=20, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dcltcim'


class Dcltechd(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    g4401 = models.IntegerField(default=0, blank=True, null=True)
    g4402 = models.IntegerField(default=0, blank=True, null=True)
    g44020 = models.CharField(max_length=1, blank=True, null=True)
    g44_cust = models.CharField(max_length=8, blank=True, null=True)
    g440 = models.CharField(max_length=4, blank=True, null=True)
    g441 = models.CharField(max_length=5, blank=True, null=True)
    g441a = models.CharField(max_length=2, blank=True, null=True)
    id_bdrd = models.CharField(max_length=36, blank=True, null=True)
    prsbdrd = models.CharField(max_length=1, blank=True, null=True)
    prsfoiv = models.CharField(max_length=1, blank=True, null=True)
    prsdecl = models.CharField(max_length=1, blank=True, null=True)
    prprovid = models.CharField(max_length=1, blank=True, null=True)
    ed_aid = models.CharField(max_length=50, blank=True, null=True)
    ed_adid = models.CharField(max_length=50, blank=True, null=True)
    prevnumtyp = models.CharField(max_length=1, blank=True, null=True)
    prevnumdoc = models.CharField(max_length=50, blank=True, null=True)
    recordid = models.CharField(max_length=36, blank=True, null=True)
    executbody = models.CharField(max_length=10, blank=True, null=True)
    execname = models.CharField(max_length=250, blank=True, null=True)
    ineturl = models.CharField(max_length=255, blank=True, null=True)
    docmodeid = models.CharField(max_length=10, blank=True, null=True)
    g442 = models.CharField(max_length=50, blank=True, null=True)
    g442lic1 = models.IntegerField(default=0, blank=True, null=True)
    g442lic2 = models.IntegerField(default=0, blank=True, null=True)
    g442r = models.CharField(max_length=28, blank=True, null=True)
    g442simp = models.CharField(max_length=10, blank=True, null=True)
    g44mdp1 = models.IntegerField(default=0, blank=True, null=True)
    g44mdp2 = models.CharField(max_length=18, blank=True, null=True)
    g443 = models.DateField(blank=True, null=True)
    g444 = models.CharField(max_length=250, blank=True, null=True)
    g445 = models.CharField(max_length=150, blank=True, null=True)
    g446 = models.DateField(blank=True, null=True)
    g447 = models.DateField(blank=True, null=True)
    g4480et = models.CharField(max_length=10, blank=True, null=True)
    g4481et = models.DateField(blank=True, null=True)
    g44stper = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    g44sfcntry = models.CharField(max_length=2, blank=True, null=True)
    g44alldoc = models.IntegerField(default=0, blank=True, null=True)
    g4491 = models.DateField(blank=True, null=True)
    g4492 = models.DateField(blank=True, null=True)
    g4493 = models.CharField(max_length=2, blank=True, null=True)
    g44dd = models.DateField(blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dcltechd'


class Dclterms(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    terms = models.CharField(max_length=3, blank=True, null=True)
    termspoint = models.CharField(max_length=50, blank=True, null=True)
    termspass = models.CharField(max_length=250, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dclterms'


class Dcltois(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    numrec = models.IntegerField(default=0, blank=True, null=True)
    typeois = models.CharField(max_length=1, blank=True, null=True)
    cntrycode = models.CharField(max_length=2, blank=True, null=True)
    iporegnum = models.CharField(max_length=25, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dcltois'


class Dcltov2(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    type_info = models.CharField(max_length=1, blank=True, null=True)
    g031 = models.IntegerField(default=0, blank=True, null=True)
    g31_1 = models.CharField(max_length=250, blank=True, null=True)
    g31_7 = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    g31_71 = models.CharField(max_length=13, blank=True, null=True)
    g31_8 = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    g31_81 = models.CharField(max_length=13, blank=True, null=True)
    g31_82 = models.CharField(max_length=3, blank=True, null=True)
    g31_9 = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    g31_91 = models.CharField(max_length=13, blank=True, null=True)
    g31_92 = models.CharField(max_length=3, blank=True, null=True)
    g31_d1 = models.DateField(blank=True, null=True)
    g31_d2 = models.DateField(blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    numpredd = models.IntegerField(default=0, blank=True, null=True)
    g33 = models.CharField(max_length=10, blank=True, null=True)
    g330 = models.CharField(max_length=1, blank=True, null=True)
    g331 = models.CharField(max_length=1, blank=True, null=True)
    g332 = models.CharField(max_length=1, blank=True, null=True)
    g333 = models.CharField(max_length=4, blank=True, null=True)
    g340 = models.CharField(max_length=1, blank=True, null=True)
    g34 = models.CharField(max_length=2, blank=True, null=True)
    g35 = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    g36 = models.CharField(max_length=7, blank=True, null=True)
    g37 = models.CharField(max_length=7, blank=True, null=True)
    g38 = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    g38_1 = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    g40_g38 = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    numrec = models.IntegerField(default=0, blank=True, null=True)
    g40_0 = models.CharField(max_length=2, blank=True, null=True)
    g40_1 = models.CharField(max_length=8, blank=True, null=True)
    g40_2 = models.DateField(blank=True, null=True)
    g40_21 = models.CharField(max_length=2, blank=True, null=True)
    g40_3 = models.CharField(max_length=7, blank=True, null=True)
    g40_4 = models.IntegerField(default=0, blank=True, null=True)
    g41a = models.CharField(max_length=3, blank=True, null=True)
    g42 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    g45 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    g451 = models.CharField(max_length=2, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dcltov2'


class Dcltovar(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    g02_itn = models.CharField(max_length=13, blank=True, null=True)
    g020 = models.CharField(max_length=15, blank=True, null=True)
    g021 = models.CharField(max_length=12, blank=True, null=True)
    g022 = models.CharField(max_length=150, blank=True, null=True)
    g023 = models.CharField(max_length=80, blank=True, null=True)
    g023post = models.CharField(max_length=9, blank=True, null=True)
    g0231 = models.CharField(max_length=2, blank=True, null=True)
    g0231n = models.CharField(max_length=40, blank=True, null=True)
    g023subd = models.CharField(max_length=50, blank=True, null=True)
    g023city = models.CharField(max_length=35, blank=True, null=True)
    g023street = models.CharField(max_length=50, blank=True, null=True)
    g023build = models.CharField(max_length=50, blank=True, null=True)
    g024b = models.CharField(max_length=5, blank=True, null=True)
    g024n = models.CharField(max_length=10, blank=True, null=True)
    g024in = models.CharField(max_length=12, blank=True, null=True)
    g027 = models.CharField(max_length=9, blank=True, null=True)
    g029 = models.CharField(max_length=1, blank=True, null=True)
    g0281 = models.CharField(max_length=7, blank=True, null=True)
    g0281a = models.CharField(max_length=25, blank=True, null=True)
    g02821 = models.CharField(max_length=11, blank=True, null=True)
    g02822 = models.CharField(max_length=25, blank=True, null=True)
    g02823 = models.CharField(max_length=150, blank=True, null=True)
    g0283 = models.DateField(blank=True, null=True)
    g022a = models.CharField(max_length=150, blank=True, null=True)
    g027a = models.CharField(max_length=9, blank=True, null=True)
    g023apost = models.CharField(max_length=9, blank=True, null=True)
    g0231a = models.CharField(max_length=2, blank=True, null=True)
    g0231an = models.CharField(max_length=40, blank=True, null=True)
    g023asubd = models.CharField(max_length=50, blank=True, null=True)
    g023acity = models.CharField(max_length=35, blank=True, null=True)
    g023astree = models.CharField(max_length=50, blank=True, null=True)
    g031 = models.IntegerField(default=0, blank=True, null=True)
    g31_1 = models.CharField(max_length=250, blank=True, null=True)
    g31_10 = models.CharField(max_length=4, blank=True, null=True)
    g31_11 = models.CharField(max_length=50, blank=True, null=True)
    g31_12 = models.CharField(max_length=50, blank=True, null=True)
    g31_13 = models.CharField(max_length=40, blank=True, null=True)
    g31_1_prdt = models.DateField(blank=True, null=True)
    g31_1_oilf = models.CharField(max_length=250, blank=True, null=True)
    g31_2 = models.IntegerField(default=0, blank=True, null=True)
    g31_2part = models.IntegerField(default=0, blank=True, null=True)
    g31_20 = models.CharField(max_length=1, blank=True, null=True)
    g31_21 = models.CharField(max_length=150, blank=True, null=True)
    g31_22 = models.IntegerField(default=0, blank=True, null=True)
    g31_23 = models.CharField(max_length=150, blank=True, null=True)
    g31_3 = models.IntegerField(default=0, blank=True, null=True)
    g31_4 = models.CharField(max_length=12, blank=True, null=True)
    g31_41 = models.IntegerField(default=0, blank=True, null=True)
    g31_401 = models.IntegerField(default=0, blank=True, null=True)
    g31_402 = models.IntegerField(default=0, blank=True, null=True)
    g31_7 = models.DecimalField(default=0.00, max_digits=19, decimal_places=6, blank=True, null=True)
    g31_71 = models.CharField(max_length=13, blank=True, null=True)
    g31_8 = models.DecimalField(default=0.00, max_digits=19, decimal_places=6, blank=True, null=True)
    g31_81 = models.CharField(max_length=13, blank=True, null=True)
    g31_82 = models.CharField(max_length=3, blank=True, null=True)
    g31_9 = models.DecimalField(default=0.00, max_digits=19, decimal_places=6, blank=True, null=True)
    g31_91 = models.CharField(max_length=13, blank=True, null=True)
    g31_92 = models.CharField(max_length=3, blank=True, null=True)
    g31_d1 = models.DateField(blank=True, null=True)
    g31_d2 = models.DateField(blank=True, null=True)
    g31_p1 = models.CharField(max_length=7, blank=True, null=True)
    g31_p2 = models.CharField(max_length=7, blank=True, null=True)
    g31_fact = models.DecimalField(default=0.00, max_digits=19, decimal_places=6, blank=True, null=True)
    g31_fc_1 = models.CharField(max_length=3, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    g32_1 = models.CharField(max_length=3, blank=True, null=True)
    g33 = models.CharField(max_length=10, blank=True, null=True)
    g330 = models.CharField(max_length=1, blank=True, null=True)
    g331 = models.CharField(max_length=1, blank=True, null=True)
    g332 = models.CharField(max_length=1, blank=True, null=True)
    g333 = models.CharField(max_length=4, blank=True, null=True)
    cimsign = models.CharField(max_length=1, blank=True, null=True)
    tcimflag = models.CharField(max_length=2, blank=True, null=True)
    tcimkol = models.IntegerField(default=0, blank=True, null=True)
    g340 = models.CharField(max_length=1, blank=True, null=True)
    g34 = models.CharField(max_length=2, blank=True, null=True)
    g34c = models.CharField(max_length=3, blank=True, null=True)
    g35 = models.DecimalField(default=0.00, max_digits=19, decimal_places=6, blank=True, null=True)
    g35k = models.DecimalField(default=0.00, max_digits=19, decimal_places=6, blank=True, null=True)
    g36 = models.CharField(max_length=7, blank=True, null=True)
    g37 = models.CharField(max_length=7, blank=True, null=True)
    g372 = models.CharField(max_length=1, blank=True, null=True)
    g38 = models.DecimalField(default=0.00, max_digits=19, decimal_places=6, blank=True, null=True)
    g38_1 = models.DecimalField(default=0.00, max_digits=19, decimal_places=6, blank=True, null=True)
    g38k = models.DecimalField(default=0.00, max_digits=19, decimal_places=6, blank=True, null=True)
    g39 = models.DecimalField(default=0.00, max_digits=19, decimal_places=6, blank=True, null=True)
    g3911 = models.CharField(max_length=3, blank=True, null=True)
    g3912 = models.CharField(max_length=3, blank=True, null=True)
    g392 = models.CharField(max_length=70, blank=True, null=True)
    g41a = models.CharField(max_length=3, blank=True, null=True)
    g42 = models.DecimalField(default=0.00, max_digits=17, decimal_places=2, blank=True, null=True)
    g42g221 = models.CharField(max_length=3, blank=True, null=True)
    g42g23 = models.DecimalField(default=0.00, max_digits=11, decimal_places=4, blank=True, null=True)
    g43 = models.CharField(max_length=1, blank=True, null=True)
    g430 = models.CharField(max_length=2, blank=True, null=True)
    g45 = models.DecimalField(default=0.00, max_digits=17, decimal_places=2, blank=True, null=True)
    g451 = models.CharField(max_length=2, blank=True, null=True)
    g46 = models.DecimalField(default=0.00, max_digits=17, decimal_places=2, blank=True, null=True)
    g46k = models.DecimalField(default=0.00, max_digits=17, decimal_places=2, blank=True, null=True)
    g461 = models.CharField(max_length=1, blank=True, null=True)
    nblank = models.CharField(max_length=10, blank=True, null=True)
    invcountr = models.CharField(max_length=2, blank=True, null=True)
    invseqid = models.CharField(max_length=4, blank=True, null=True)
    invyear = models.CharField(max_length=4, blank=True, null=True)
    invkind = models.CharField(max_length=1, blank=True, null=True)
    invgoodid = models.IntegerField(default=0, blank=True, null=True)
    fksign = models.CharField(max_length=1, blank=True, null=True)
    gd0 = models.CharField(max_length=2, blank=True, null=True)
    gd1 = models.DateField(blank=True, null=True)
    gd11 = models.CharField(max_length=8, blank=True, null=True)
    gd2 = models.CharField(max_length=4, blank=True, null=True)
    gd00 = models.CharField(max_length=250, blank=True, null=True)
    gd01 = models.CharField(max_length=250, blank=True, null=True)
    kod_str = models.CharField(max_length=2, blank=True, null=True)
    kod_strc = models.CharField(max_length=3, blank=True, null=True)
    dstat = models.DateField(blank=True, null=True)
    stat = models.CharField(max_length=1, blank=True, null=True)
    recplatr = models.IntegerField(default=0, blank=True, null=True)
    rectechd = models.IntegerField(default=0, blank=True, null=True)
    recpredd = models.IntegerField(default=0, blank=True, null=True)
    recavtmb = models.IntegerField(default=0, blank=True, null=True)
    rectovg = models.IntegerField(default=0, blank=True, null=True)
    recpk = models.IntegerField(default=0, blank=True, null=True)
    recamnum = models.IntegerField(default=0, blank=True, null=True)
    recterms = models.IntegerField(default=0, blank=True, null=True)
    recdog = models.IntegerField(default=0, blank=True, null=True)
    recdoga = models.IntegerField(default=0, blank=True, null=True)
    recdogt = models.IntegerField(default=0, blank=True, null=True)
    reckmp = models.IntegerField(default=0, blank=True, null=True)
    recuslt = models.IntegerField(default=0, blank=True, null=True)
    recsltov = models.IntegerField(default=0, blank=True, null=True)
    rectov2 = models.IntegerField(default=0, blank=True, null=True)
    recplat2 = models.IntegerField(default=0, blank=True, null=True)
    recdinf2 = models.IntegerField(default=0, blank=True, null=True)
    rectovg2 = models.IntegerField(default=0, blank=True, null=True)
    recvrsk = models.IntegerField(default=0, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    npart = models.IntegerField(default=0, blank=True, null=True)
    npartdesc = models.CharField(max_length=80, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dcltovar'


class Dcltovg(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    g32g = models.IntegerField(default=0, blank=True, null=True)
    numrec = models.IntegerField(default=0, blank=True, null=True)
    g31_10 = models.CharField(max_length=4, blank=True, null=True)
    g31_11 = models.CharField(max_length=150, blank=True, null=True)
    g31_12 = models.CharField(max_length=150, blank=True, null=True)
    g31place = models.CharField(max_length=250, blank=True, null=True)
    g31_14 = models.CharField(max_length=50, blank=True, null=True)
    g31_15_mod = models.CharField(max_length=50, blank=True, null=True)
    g31_15 = models.CharField(max_length=50, blank=True, null=True)
    g31_16 = models.CharField(max_length=50, blank=True, null=True)
    compord = models.IntegerField(default=0, blank=True, null=True)
    compnum = models.CharField(max_length=50, blank=True, null=True)
    g31_17 = models.CharField(max_length=50, blank=True, null=True)
    g31_18 = models.CharField(max_length=30, blank=True, null=True)
    g31_19 = models.CharField(max_length=20, blank=True, null=True)
    woodrmin = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    woodrmax = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    woodrcod = models.CharField(max_length=3, blank=True, null=True)
    woodcont = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    woodfact = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    woodfcod = models.CharField(max_length=3, blank=True, null=True)
    g31_20 = models.CharField(max_length=50, blank=True, null=True)
    length = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    clength = models.CharField(max_length=3, blank=True, null=True)
    width = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    cwidth = models.CharField(max_length=3, blank=True, null=True)
    height = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    cheight = models.CharField(max_length=3, blank=True, null=True)
    kolvo = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    code_edi = models.CharField(max_length=3, blank=True, null=True)
    name_edi = models.CharField(max_length=13, blank=True, null=True)
    recordid = models.CharField(max_length=36, blank=True, null=True)
    invoiccost = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    licgrpdoc1 = models.CharField(max_length=50, blank=True, null=True)
    licgrpd1 = models.DateField(blank=True, null=True)
    licrec1 = models.CharField(max_length=36, blank=True, null=True)
    goodnmlic1 = models.IntegerField(default=0, blank=True, null=True)
    licgrpdoc2 = models.CharField(max_length=50, blank=True, null=True)
    licgrpd2 = models.DateField(blank=True, null=True)
    licrec2 = models.CharField(max_length=36, blank=True, null=True)
    goodnmlic2 = models.IntegerField(default=0, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dcltovg'


class Dcltovg2(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    type_info = models.CharField(max_length=1, blank=True, null=True)
    numpredd = models.IntegerField(default=0, blank=True, null=True)
    g32g = models.IntegerField(default=0, blank=True, null=True)
    numrec = models.IntegerField(default=0, blank=True, null=True)
    g31_10 = models.CharField(max_length=4, blank=True, null=True)
    g31_11 = models.CharField(max_length=150, blank=True, null=True)
    g31_12 = models.CharField(max_length=150, blank=True, null=True)
    g31_14 = models.CharField(max_length=50, blank=True, null=True)
    g31_15_mod = models.CharField(max_length=50, blank=True, null=True)
    g31_15 = models.CharField(max_length=50, blank=True, null=True)
    g31_16 = models.CharField(max_length=50, blank=True, null=True)
    g31_17 = models.CharField(max_length=50, blank=True, null=True)
    g31_18 = models.CharField(max_length=30, blank=True, null=True)
    g31_19 = models.CharField(max_length=20, blank=True, null=True)
    g31_20 = models.CharField(max_length=50, blank=True, null=True)
    kolvo = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    code_edi = models.CharField(max_length=3, blank=True, null=True)
    name_edi = models.CharField(max_length=13, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dcltovg2'


class Dcltovs(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    g32g = models.IntegerField(default=0, blank=True, null=True)
    numrec = models.IntegerField(default=0, blank=True, null=True)
    g31_15_sn = models.CharField(max_length=50, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dcltovs'


class Dcltovs2(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    type_info = models.CharField(max_length=1, blank=True, null=True)
    numpredd = models.IntegerField(default=0, blank=True, null=True)
    g32g = models.IntegerField(default=0, blank=True, null=True)
    numrec = models.IntegerField(default=0, blank=True, null=True)
    g31_15_sn = models.CharField(max_length=50, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dcltovs2'


class Dcltrans(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    ngr = models.CharField(max_length=2, blank=True, null=True)
    numrec = models.IntegerField(default=0, blank=True, null=True)
    vidtrans = models.CharField(max_length=2, blank=True, null=True)
    tipts3 = models.CharField(max_length=3, blank=True, null=True)
    mthtrans = models.CharField(max_length=1, blank=True, null=True)
    nametrans = models.CharField(max_length=100, blank=True, null=True)
    ntrans = models.CharField(max_length=40, blank=True, null=True)
    movetrans = models.CharField(max_length=1, blank=True, null=True)
    ntrans1 = models.CharField(max_length=40, blank=True, null=True)
    ntrans2 = models.CharField(max_length=40, blank=True, null=True)
    activeid = models.CharField(max_length=40, blank=True, null=True)
    g19 = models.CharField(max_length=1, blank=True, null=True)
    st_control = models.CharField(max_length=250, blank=True, null=True)
    g212 = models.CharField(max_length=2, blank=True, null=True)
    g29 = models.CharField(max_length=8, blank=True, null=True)
    g291 = models.CharField(max_length=3, blank=True, null=True)
    gc5 = models.DateField(blank=True, null=True)
    gc51 = models.CharField(max_length=8, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dcltrans'


class Dclusl(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    gu01 = models.IntegerField(default=0, blank=True, null=True)
    gu02 = models.IntegerField(default=0, blank=True, null=True)
    gunpp = models.IntegerField(default=0, blank=True, null=True)
    gu10 = models.CharField(max_length=1, blank=True, null=True)
    gu2 = models.CharField(max_length=250, blank=True, null=True)
    gu2d = models.DateField(blank=True, null=True)
    gu3 = models.DateField(blank=True, null=True)
    gu31 = models.DateField(blank=True, null=True)
    gu4 = models.CharField(max_length=8, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dclusl'


class Dcluslt(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    typeinfo = models.CharField(max_length=1, blank=True, null=True)
    gu01 = models.IntegerField(default=0, blank=True, null=True)
    gu02 = models.IntegerField(default=0, blank=True, null=True)
    gu03 = models.CharField(max_length=2, blank=True, null=True)
    gunpp = models.IntegerField(default=0, blank=True, null=True)
    gu1 = models.CharField(max_length=50, blank=True, null=True)
    gu1d = models.DateField(blank=True, null=True)
    gu2 = models.CharField(max_length=250, blank=True, null=True)
    gu3 = models.DateField(blank=True, null=True)
    gudd = models.DateField(blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dcluslt'


class Dclvrsk(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    npart = models.IntegerField(default=0, blank=True, null=True)
    gr010 = models.CharField(max_length=1, blank=True, null=True)
    gr013 = models.CharField(max_length=2, blank=True, null=True)
    gr0131 = models.CharField(max_length=5, blank=True, null=True)
    gr_podr = models.CharField(max_length=4, blank=True, null=True)
    gr014 = models.DateField(blank=True, null=True)
    gr015 = models.CharField(max_length=6, blank=True, null=True)
    gr0151 = models.IntegerField(default=0, blank=True, null=True)
    gr0152 = models.DateField(blank=True, null=True)
    gr0153 = models.DateField(blank=True, null=True)
    gr041 = models.CharField(max_length=4, blank=True, null=True)
    num_dir = models.CharField(max_length=23, blank=True, null=True)
    categobj = models.CharField(max_length=1, blank=True, null=True)
    point_code = models.CharField(max_length=2, blank=True, null=True)
    dpoint = models.DateField(blank=True, null=True)
    tpoint = models.CharField(max_length=8, blank=True, null=True)
    lineid = models.CharField(max_length=36, blank=True, null=True)
    softkind = models.CharField(max_length=1, blank=True, null=True)
    softvrsn = models.CharField(max_length=10, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dclvrsk'


class Dk1(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    k21 = models.IntegerField(default=0, blank=True, null=True)
    k22 = models.IntegerField(default=0, blank=True, null=True)
    k3 = models.DecimalField(default=0.00, max_digits=10, decimal_places=4, blank=True, null=True)
    k4 = models.CharField(max_length=3, blank=True, null=True)
    k5 = models.DecimalField(default=0.00, max_digits=10, decimal_places=4, blank=True, null=True)
    k6 = models.CharField(max_length=12, blank=True, null=True)
    k9 = models.BooleanField(blank=True, null=True)
    k9a = models.CharField(max_length=4, blank=True, null=True)
    k9k = models.IntegerField(default=0, blank=True, null=True)
    k10 = models.BooleanField(blank=True, null=True)
    k10a = models.BooleanField(blank=True, null=True)
    k10c = models.BooleanField(blank=True, null=True)
    k10b = models.CharField(max_length=3, blank=True, null=True)
    k110 = models.BooleanField(blank=True, null=True)
    k111 = models.BooleanField(blank=True, null=True)
    k112 = models.BooleanField(blank=True, null=True)
    k112a = models.DateField(blank=True, null=True)
    k113 = models.BooleanField(blank=True, null=True)
    k114 = models.BooleanField(blank=True, null=True)
    k114a = models.CharField(max_length=23, blank=True, null=True)
    k114b = models.DateField(blank=True, null=True)
    k115 = models.CharField(max_length=20, blank=True, null=True)
    k115a = models.DateField(blank=True, null=True)
    k121 = models.BooleanField(blank=True, null=True)
    k122 = models.CharField(max_length=23, blank=True, null=True)
    k122a = models.DateField(blank=True, null=True)
    k123 = models.CharField(max_length=20, blank=True, null=True)
    k123a = models.DateField(blank=True, null=True)
    k124 = models.CharField(max_length=1, blank=True, null=True)
    k125 = models.CharField(max_length=1, blank=True, null=True)
    k126 = models.DecimalField(default=0.00, max_digits=14, decimal_places=2, blank=True, null=True)
    k130 = models.CharField(max_length=8, blank=True, null=True)
    kpech1 = models.CharField(max_length=4, blank=True, null=True)
    kpech2 = models.CharField(max_length=4, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dk1'


class Dk2(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    prim = models.CharField(max_length=120, blank=True, null=True)
    dateprim = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dk2'


class DkPp(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    okpo = models.CharField(max_length=10, blank=True, null=True)
    inn = models.CharField(max_length=12, blank=True, null=True)
    kpp = models.CharField(max_length=9, blank=True, null=True)
    k92 = models.CharField(max_length=50, blank=True, null=True)
    k93 = models.DateField(blank=True, null=True)
    k94 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    k95 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    k96 = models.DateField(blank=True, null=True)
    k_val = models.CharField(max_length=3, blank=True, null=True)
    priz = models.CharField(max_length=3, blank=True, null=True)
    who = models.CharField(max_length=1, blank=True, null=True)
    sp = models.CharField(max_length=2, blank=True, null=True)
    crypt = models.CharField(max_length=10, blank=True, null=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    bank_id = models.CharField(max_length=20, blank=True, null=True)
    vp = models.CharField(max_length=4, blank=True, null=True)
    iret = models.IntegerField(default=0, blank=True, null=True)
    nblktc1 = models.CharField(max_length=8, blank=True, null=True)
    dsp = models.DateField(blank=True, null=True)
    tsp = models.CharField(max_length=8, blank=True, null=True)
    lnpinsp = models.CharField(max_length=4, blank=True, null=True)
    n_sv = models.CharField(max_length=14, blank=True, null=True)
    d_sv = models.DateField(blank=True, null=True)
    n_cntr = models.CharField(max_length=50, blank=True, null=True)
    d_cntr = models.DateField(blank=True, null=True)
    ntr = models.CharField(max_length=26, blank=True, null=True)
    process_id = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dk_pp'


class Dkisch(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    g470 = models.CharField(max_length=1, blank=True, null=True)
    g471 = models.CharField(max_length=4, blank=True, null=True)
    g471_1 = models.CharField(max_length=1, blank=True, null=True)
    g471npp = models.IntegerField(default=0, blank=True, null=True)
    g472 = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    g4721 = models.CharField(max_length=3, blank=True, null=True)
    g4722 = models.CharField(max_length=50, blank=True, null=True)
    g473 = models.DecimalField(default=0.00, max_digits=12, decimal_places=6, blank=True, null=True)
    g4731 = models.CharField(max_length=1, blank=True, null=True)
    g4732 = models.CharField(max_length=3, blank=True, null=True)
    g4733 = models.CharField(max_length=3, blank=True, null=True)
    g4734 = models.DecimalField(default=0.00, max_digits=8, decimal_places=3, blank=True, null=True)
    g474 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    g4741 = models.CharField(max_length=3, blank=True, null=True)
    g475 = models.CharField(max_length=2, blank=True, null=True)
    g473z1_2 = models.CharField(max_length=1, blank=True, null=True)
    g473_2 = models.DecimalField(default=0.00, max_digits=12, decimal_places=6, blank=True, null=True)
    g4731_2 = models.CharField(max_length=1, blank=True, null=True)
    g4732_2 = models.CharField(max_length=3, blank=True, null=True)
    g4733_2 = models.CharField(max_length=3, blank=True, null=True)
    g4734_2 = models.DecimalField(default=0.00, max_digits=8, decimal_places=3, blank=True, null=True)
    g473z1_3 = models.CharField(max_length=1, blank=True, null=True)
    g473_3 = models.DecimalField(default=0.00, max_digits=12, decimal_places=6, blank=True, null=True)
    g4731_3 = models.CharField(max_length=1, blank=True, null=True)
    g4732_3 = models.CharField(max_length=3, blank=True, null=True)
    g4733_3 = models.CharField(max_length=3, blank=True, null=True)
    g4734_3 = models.DecimalField(default=0.00, max_digits=8, decimal_places=3, blank=True, null=True)
    g473z2_2 = models.IntegerField(default=0, blank=True, null=True)
    g4730 = models.DateField(blank=True, null=True)
    g47_nd = models.IntegerField(default=0, blank=True, null=True)
    g47_ns = models.IntegerField(default=0, blank=True, null=True)
    g47_nm = models.IntegerField(default=0, blank=True, null=True)
    g47_tr = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, blank=True, null=True)
    g47_g40 = models.IntegerField(default=0, blank=True, null=True)
    npp = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dkisch'


class Dkkupl(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    gb0 = models.CharField(max_length=1, blank=True, null=True)
    gb1 = models.CharField(max_length=4, blank=True, null=True)
    gb1_1 = models.CharField(max_length=1, blank=True, null=True)
    gb2 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    gb3 = models.CharField(max_length=3, blank=True, null=True)
    gb4 = models.DecimalField(default=0.00, max_digits=10, decimal_places=4, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dkkupl'


class Dkoprp(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    gb0 = models.CharField(max_length=1, blank=True, null=True)
    gb1 = models.CharField(max_length=4, blank=True, null=True)
    gb1_1 = models.CharField(max_length=1, blank=True, null=True)
    gb2 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    gb3 = models.CharField(max_length=3, blank=True, null=True)
    gb5 = models.CharField(max_length=2, blank=True, null=True)
    ndoc = models.CharField(max_length=15, blank=True, null=True)
    stav = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, blank=True, null=True)
    prcs = models.DecimalField(default=0.00, max_digits=8, decimal_places=2, blank=True, null=True)
    g48 = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dkoprp'


class Dkpeni(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    gb1 = models.CharField(max_length=4, blank=True, null=True)
    gb1_1 = models.CharField(max_length=1, blank=True, null=True)
    gb2 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    gb3 = models.CharField(max_length=3, blank=True, null=True)
    gb4 = models.DecimalField(default=0.00, max_digits=10, decimal_places=4, blank=True, null=True)
    priz = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dkpeni'


class Dtcddtc(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    num_pp = models.IntegerField(default=0, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    npoz = models.CharField(max_length=3, blank=True, null=True)
    addinfcode = models.CharField(max_length=1, blank=True, null=True)
    dt071 = models.CharField(max_length=8, blank=True, null=True)
    dt072 = models.DateField(blank=True, null=True)
    dt073 = models.CharField(max_length=7, blank=True, null=True)
    dtg32 = models.IntegerField(default=0, blank=True, null=True)
    dtsg32 = models.IntegerField(default=0, blank=True, null=True)
    numrec = models.IntegerField(default=0, blank=True, null=True)
    text1 = models.CharField(max_length=250, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dtcddtc'


class Dtcdinfo(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    num_pp = models.IntegerField(default=0, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    npoz = models.CharField(max_length=3, blank=True, null=True)
    numrec = models.IntegerField(default=0, blank=True, null=True)
    dinf01 = models.CharField(max_length=5, blank=True, null=True)
    terms = models.CharField(max_length=3, blank=True, null=True)
    dinf02 = models.CharField(max_length=50, blank=True, null=True)
    dinf03 = models.DateField(blank=True, null=True)
    dt071 = models.CharField(max_length=8, blank=True, null=True)
    dt072 = models.DateField(blank=True, null=True)
    dt073 = models.CharField(max_length=7, blank=True, null=True)
    dtg32 = models.IntegerField(default=0, blank=True, null=True)
    dtsg32 = models.IntegerField(default=0, blank=True, null=True)
    text1 = models.CharField(max_length=250, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dtcdinfo'


class Dtchead(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    num_pp = models.IntegerField(default=0, blank=True, null=True)
    nmet = models.CharField(max_length=2, blank=True, null=True)
    nmet6 = models.CharField(max_length=1, blank=True, null=True)
    formadtc = models.CharField(max_length=1, blank=True, null=True)
    d01_ogrn = models.CharField(max_length=15, blank=True, null=True)
    d01_inn = models.CharField(max_length=12, blank=True, null=True)
    d01_kpp = models.CharField(max_length=9, blank=True, null=True)
    d01_itn = models.CharField(max_length=13, blank=True, null=True)
    d011 = models.CharField(max_length=150, blank=True, null=True)
    d012 = models.CharField(max_length=80, blank=True, null=True)
    d012post = models.CharField(max_length=9, blank=True, null=True)
    d0121 = models.CharField(max_length=2, blank=True, null=True)
    d0121n = models.CharField(max_length=40, blank=True, null=True)
    d012subd = models.CharField(max_length=50, blank=True, null=True)
    d012city = models.CharField(max_length=35, blank=True, null=True)
    d012street = models.CharField(max_length=50, blank=True, null=True)
    d012build = models.CharField(max_length=50, blank=True, null=True)
    d0181 = models.CharField(max_length=7, blank=True, null=True)
    d0181a = models.CharField(max_length=25, blank=True, null=True)
    d01821 = models.CharField(max_length=11, blank=True, null=True)
    d01822 = models.CharField(max_length=25, blank=True, null=True)
    d01823 = models.CharField(max_length=150, blank=True, null=True)
    d0183 = models.DateField(blank=True, null=True)
    d011a = models.CharField(max_length=150, blank=True, null=True)
    d011akpp = models.CharField(max_length=9, blank=True, null=True)
    d011apost = models.CharField(max_length=9, blank=True, null=True)
    d011aalf = models.CharField(max_length=2, blank=True, null=True)
    d011akn = models.CharField(max_length=40, blank=True, null=True)
    d011asubd = models.CharField(max_length=50, blank=True, null=True)
    d011acity = models.CharField(max_length=35, blank=True, null=True)
    d011astree = models.CharField(max_length=50, blank=True, null=True)
    d011abuild = models.CharField(max_length=50, blank=True, null=True)
    d019 = models.CharField(max_length=1, blank=True, null=True)
    d01e14 = models.CharField(max_length=1, blank=True, null=True)
    d02_ogrn = models.CharField(max_length=15, blank=True, null=True)
    d02_inn = models.CharField(max_length=12, blank=True, null=True)
    d02_kpp = models.CharField(max_length=9, blank=True, null=True)
    d02_itn = models.CharField(max_length=13, blank=True, null=True)
    d02a1 = models.CharField(max_length=150, blank=True, null=True)
    d02a2 = models.CharField(max_length=80, blank=True, null=True)
    d02a2post = models.CharField(max_length=9, blank=True, null=True)
    d02a21 = models.CharField(max_length=2, blank=True, null=True)
    d02a21n = models.CharField(max_length=40, blank=True, null=True)
    d02a2subd = models.CharField(max_length=50, blank=True, null=True)
    d02a2city = models.CharField(max_length=35, blank=True, null=True)
    d02a2stree = models.CharField(max_length=50, blank=True, null=True)
    d02a2build = models.CharField(max_length=50, blank=True, null=True)
    d02a81 = models.CharField(max_length=7, blank=True, null=True)
    d02a81a = models.CharField(max_length=25, blank=True, null=True)
    d02a821 = models.CharField(max_length=11, blank=True, null=True)
    d02a822 = models.CharField(max_length=25, blank=True, null=True)
    d02a823 = models.CharField(max_length=150, blank=True, null=True)
    d02a83 = models.DateField(blank=True, null=True)
    d02a1a = models.CharField(max_length=150, blank=True, null=True)
    d02a1akpp = models.CharField(max_length=9, blank=True, null=True)
    d02a1apost = models.CharField(max_length=9, blank=True, null=True)
    d02a1aalf = models.CharField(max_length=2, blank=True, null=True)
    d02a1akn = models.CharField(max_length=40, blank=True, null=True)
    d02a1asubd = models.CharField(max_length=50, blank=True, null=True)
    d02a1acity = models.CharField(max_length=35, blank=True, null=True)
    d02a1astre = models.CharField(max_length=50, blank=True, null=True)
    d02a1build = models.CharField(max_length=50, blank=True, null=True)
    d029 = models.CharField(max_length=1, blank=True, null=True)
    d02e14 = models.CharField(max_length=1, blank=True, null=True)
    d02b_ogrn = models.CharField(max_length=15, blank=True, null=True)
    d02b_inn = models.CharField(max_length=12, blank=True, null=True)
    d02b_kpp = models.CharField(max_length=9, blank=True, null=True)
    d02b_itn = models.CharField(max_length=13, blank=True, null=True)
    d02b1 = models.CharField(max_length=150, blank=True, null=True)
    d02b2 = models.CharField(max_length=80, blank=True, null=True)
    d02b2post = models.CharField(max_length=9, blank=True, null=True)
    d02b21 = models.CharField(max_length=2, blank=True, null=True)
    d02b21n = models.CharField(max_length=40, blank=True, null=True)
    d02b2subd = models.CharField(max_length=50, blank=True, null=True)
    d02b2city = models.CharField(max_length=35, blank=True, null=True)
    d02b2stree = models.CharField(max_length=50, blank=True, null=True)
    d02b2build = models.CharField(max_length=50, blank=True, null=True)
    d02b81 = models.CharField(max_length=7, blank=True, null=True)
    d02b81a = models.CharField(max_length=25, blank=True, null=True)
    d02b821 = models.CharField(max_length=11, blank=True, null=True)
    d02b822 = models.CharField(max_length=25, blank=True, null=True)
    d02b823 = models.CharField(max_length=150, blank=True, null=True)
    d02b83 = models.DateField(blank=True, null=True)
    d02b1a = models.CharField(max_length=150, blank=True, null=True)
    d02b1akpp = models.CharField(max_length=9, blank=True, null=True)
    d02b1apost = models.CharField(max_length=9, blank=True, null=True)
    d02b1aalf = models.CharField(max_length=2, blank=True, null=True)
    d02b1akn = models.CharField(max_length=40, blank=True, null=True)
    d02b1asubd = models.CharField(max_length=50, blank=True, null=True)
    d02b1acity = models.CharField(max_length=35, blank=True, null=True)
    d02b1astre = models.CharField(max_length=50, blank=True, null=True)
    d02b1build = models.CharField(max_length=50, blank=True, null=True)
    aeorowner = models.CharField(max_length=1, blank=True, null=True)
    aeocntry = models.CharField(max_length=2, blank=True, null=True)
    aeonum = models.CharField(max_length=50, blank=True, null=True)
    aeokind = models.CharField(max_length=1, blank=True, null=True)
    aeoregcod = models.CharField(max_length=3, blank=True, null=True)
    d031 = models.CharField(max_length=3, blank=True, null=True)
    d032 = models.CharField(max_length=40, blank=True, null=True)
    d07a = models.CharField(max_length=1, blank=True, null=True)
    d07b = models.CharField(max_length=1, blank=True, null=True)
    d07c = models.CharField(max_length=1, blank=True, null=True)
    d08a = models.CharField(max_length=1, blank=True, null=True)
    d08b = models.CharField(max_length=1, blank=True, null=True)
    d09a = models.CharField(max_length=1, blank=True, null=True)
    d09b = models.CharField(max_length=1, blank=True, null=True)
    koldopl = models.IntegerField(default=0, blank=True, null=True)
    g542 = models.DateField(blank=True, null=True)
    g543 = models.CharField(max_length=4, blank=True, null=True)
    g5441 = models.CharField(max_length=150, blank=True, null=True)
    g5441nm = models.CharField(max_length=150, blank=True, null=True)
    g5441mdnm = models.CharField(max_length=150, blank=True, null=True)
    g5442 = models.CharField(max_length=50, blank=True, null=True)
    g5447 = models.CharField(max_length=50, blank=True, null=True)
    g5451 = models.CharField(max_length=7, blank=True, null=True)
    g5451a = models.CharField(max_length=25, blank=True, null=True)
    g5451b = models.CharField(max_length=11, blank=True, null=True)
    g5452 = models.CharField(max_length=25, blank=True, null=True)
    g5453 = models.DateField(blank=True, null=True)
    g5454 = models.CharField(max_length=150, blank=True, null=True)
    g545aid = models.CharField(max_length=50, blank=True, null=True)
    g545adid = models.CharField(max_length=50, blank=True, null=True)
    g545modid = models.CharField(max_length=10, blank=True, null=True)
    g545doc = models.CharField(max_length=5, blank=True, null=True)
    prprov545 = models.CharField(max_length=1, blank=True, null=True)
    pretype545 = models.CharField(max_length=1, blank=True, null=True)
    prevnum545 = models.CharField(max_length=50, blank=True, null=True)
    valdat = models.DateField(blank=True, null=True)
    tamst_kodv = models.CharField(max_length=3, blank=True, null=True)
    tamst_kurs = models.DecimalField(default=0.00, max_digits=10, decimal_places=4, blank=True, null=True)
    dc10 = models.CharField(max_length=2, blank=True, null=True)
    dc11 = models.DateField(blank=True, null=True)
    dc12 = models.CharField(max_length=4, blank=True, null=True)
    dc12d = models.DateField(blank=True, null=True)
    dc12t = models.CharField(max_length=8, blank=True, null=True)
    dc20 = models.CharField(max_length=2, blank=True, null=True)
    dc22 = models.CharField(max_length=4, blank=True, null=True)
    dc22d = models.DateField(blank=True, null=True)
    dc30 = models.CharField(max_length=2, blank=True, null=True)
    dc32 = models.CharField(max_length=4, blank=True, null=True)
    dc32d = models.DateField(blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)
    ed_idid = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dtchead'


class Dtcslotm(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    num_pp = models.IntegerField(default=0, blank=True, null=True)
    dc_01 = models.CharField(max_length=1, blank=True, null=True)
    nrecc = models.IntegerField(default=0, blank=True, null=True)
    dc_1 = models.CharField(max_length=250, blank=True, null=True)
    dc_2 = models.DateField(blank=True, null=True)
    dc_21 = models.CharField(max_length=8, blank=True, null=True)
    dc_6 = models.CharField(max_length=4, blank=True, null=True)
    dc_7 = models.CharField(max_length=40, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dtcslotm'


class Dtcsscv(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    num_pp = models.IntegerField(default=0, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    npoz = models.CharField(max_length=3, blank=True, null=True)
    valsum = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    valkod = models.CharField(max_length=3, blank=True, null=True)
    valkurs = models.DecimalField(default=0.00, max_digits=10, decimal_places=4, blank=True, null=True)
    valdate = models.DateField(blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dtcsscv'


class Dtcsstc(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    num_pp = models.IntegerField(default=0, blank=True, null=True)
    ch = models.IntegerField(default=0, blank=True, null=True)
    ch1 = models.IntegerField(default=0, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    nmet = models.CharField(max_length=2, blank=True, null=True)
    nmet6 = models.CharField(max_length=1, blank=True, null=True)
    cucostdate = models.DateField(blank=True, null=True)
    d11_v = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    d11_kodv = models.CharField(max_length=3, blank=True, null=True)
    d11_r = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    d11_kurs = models.DecimalField(default=0.00, max_digits=10, decimal_places=4, blank=True, null=True)
    d11_kurd = models.DateField(blank=True, null=True)
    d11b_r = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    d11b_kodv = models.CharField(max_length=3, blank=True, null=True)
    d11b_kurs = models.DecimalField(default=0.00, max_digits=10, decimal_places=4, blank=True, null=True)
    d11b_kurd = models.DateField(blank=True, null=True)
    d11 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    d11a = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    d11b = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    d12 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    d12a = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    d12b = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    d12c = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    d12d = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    d12e = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    d12f = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    d12g = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    d13 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    d13a = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    d13b = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    d13c = models.DecimalField(default=0.00, max_digits=15, decimal_places=2, blank=True, null=True)
    d14 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    d14a = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    d14b = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    d14c = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    d14d = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    d14e = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    d15 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    d16 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    d16a = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    d16b = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    d16c = models.DecimalField(default=0.00, max_digits=15, decimal_places=2, blank=True, null=True)
    d16d = models.DecimalField(default=0.00, max_digits=15, decimal_places=2, blank=True, null=True)
    d17 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    d17mv = models.CharField(max_length=40, blank=True, null=True)
    d17a = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    d17b = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    d17c = models.DecimalField(default=0.00, max_digits=15, decimal_places=2, blank=True, null=True)
    d18 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    d19 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    d20 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    d21 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    d22 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    d23 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    d24 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    d24a = models.DecimalField(default=0.00, max_digits=15, decimal_places=2, blank=True, null=True)
    d24a_ei = models.CharField(max_length=3, blank=True, null=True)
    d24b = models.DecimalField(default=0.00, max_digits=15, decimal_places=2, blank=True, null=True)
    d24b_ei = models.CharField(max_length=3, blank=True, null=True)
    d25 = models.DecimalField(default=0.00, max_digits=15, decimal_places=2, blank=True, null=True)
    d26 = models.DecimalField(default=0.00, max_digits=15, decimal_places=2, blank=True, null=True)
    d_ei = models.CharField(max_length=3, blank=True, null=True)
    d_eiio = models.CharField(max_length=3, blank=True, null=True)
    d_mpmn = models.CharField(max_length=40, blank=True, null=True)
    d_mp = models.CharField(max_length=40, blank=True, null=True)
    d_mpio = models.CharField(max_length=40, blank=True, null=True)
    tamst_r = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    tamst_v = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    valdat = models.DateField(blank=True, null=True)
    tamst_kodv = models.CharField(max_length=3, blank=True, null=True)
    tamst_kurs = models.DecimalField(default=0.00, max_digits=10, decimal_places=4, blank=True, null=True)
    dc10 = models.CharField(max_length=2, blank=True, null=True)
    dc11 = models.DateField(blank=True, null=True)
    dc12 = models.CharField(max_length=4, blank=True, null=True)
    dc12d = models.DateField(blank=True, null=True)
    dc12t = models.CharField(max_length=8, blank=True, null=True)
    dc20 = models.CharField(max_length=2, blank=True, null=True)
    dc22 = models.CharField(max_length=4, blank=True, null=True)
    dc22d = models.DateField(blank=True, null=True)
    dc30 = models.CharField(max_length=2, blank=True, null=True)
    dc32 = models.CharField(max_length=4, blank=True, null=True)
    dc32d = models.DateField(blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'dtcsstc'


class Ktcavtmb(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    k32 = models.IntegerField(default=0, blank=True, null=True)
    nud = models.CharField(max_length=12, blank=True, null=True)
    kodmrk = models.CharField(max_length=3, blank=True, null=True)
    namemrkcar = models.CharField(max_length=20, blank=True, null=True)
    model = models.CharField(max_length=36, blank=True, null=True)
    year = models.IntegerField(default=0, blank=True, null=True)
    price = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    obem = models.IntegerField(default=0, blank=True, null=True)
    id = models.CharField(max_length=20, blank=True, null=True)
    nkuz = models.CharField(max_length=40, blank=True, null=True)
    kabina = models.CharField(max_length=40, blank=True, null=True)
    nsh = models.CharField(max_length=40, blank=True, null=True)
    ndv = models.CharField(max_length=40, blank=True, null=True)
    prim = models.DecimalField(default=0.00, max_digits=8, decimal_places=2, blank=True, null=True)
    probeg = models.IntegerField(default=0, blank=True, null=True)
    nblktc1 = models.CharField(max_length=8, blank=True, null=True)
    nblktc1p = models.CharField(max_length=8, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'ktcavtmb'


class Ktcdinfo(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    k32 = models.IntegerField(default=0, blank=True, null=True)
    ngr = models.CharField(max_length=2, blank=True, null=True)
    typ_ngr = models.CharField(max_length=2, blank=True, null=True)
    k32g = models.IntegerField(default=0, blank=True, null=True)
    numrec = models.IntegerField(default=0, blank=True, null=True)
    text1 = models.CharField(max_length=250, blank=True, null=True)
    ind_text = models.CharField(max_length=3, blank=True, null=True)
    text2 = models.CharField(max_length=50, blank=True, null=True)
    typ_izm = models.CharField(max_length=1, blank=True, null=True)
    kolvo = models.DecimalField(default=0.00, max_digits=16, decimal_places=4, blank=True, null=True)
    code_edi = models.CharField(max_length=3, blank=True, null=True)
    name_edi = models.CharField(max_length=17, blank=True, null=True)
    nblktc1 = models.CharField(max_length=8, blank=True, null=True)
    nblktc1p = models.CharField(max_length=8, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'ktcdinfo'


class Ktcdokiz(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    k32 = models.IntegerField(default=0, blank=True, null=True)
    k4401 = models.IntegerField(default=0, blank=True, null=True)
    k4402 = models.IntegerField(default=0, blank=True, null=True)
    k44020 = models.CharField(max_length=1, blank=True, null=True)
    k44_cust = models.CharField(max_length=8, blank=True, null=True)
    k440 = models.CharField(max_length=4, blank=True, null=True)
    k441 = models.CharField(max_length=5, blank=True, null=True)
    k441a = models.CharField(max_length=2, blank=True, null=True)
    k442 = models.CharField(max_length=50, blank=True, null=True)
    k442lic1 = models.IntegerField(default=0, blank=True, null=True)
    k442lic2 = models.IntegerField(default=0, blank=True, null=True)
    k442r = models.CharField(max_length=28, blank=True, null=True)
    k442simp = models.CharField(max_length=1, blank=True, null=True)
    k44mdp1 = models.IntegerField(default=0, blank=True, null=True)
    k44mdp2 = models.CharField(max_length=18, blank=True, null=True)
    k443 = models.DateField(blank=True, null=True)
    k444 = models.CharField(max_length=250, blank=True, null=True)
    k445 = models.CharField(max_length=150, blank=True, null=True)
    k446 = models.DateField(blank=True, null=True)
    k447 = models.DateField(blank=True, null=True)
    k4480et = models.CharField(max_length=10, blank=True, null=True)
    k4481et = models.DateField(blank=True, null=True)
    k44stper = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    k44sfcntry = models.CharField(max_length=2, blank=True, null=True)
    k44alldoc = models.IntegerField(default=0, blank=True, null=True)
    k4491 = models.DateField(blank=True, null=True)
    k4492 = models.DateField(blank=True, null=True)
    k4493 = models.CharField(max_length=2, blank=True, null=True)
    k44dd = models.DateField(blank=True, null=True)
    nblktc1 = models.CharField(max_length=8, blank=True, null=True)
    nblktc1p = models.CharField(max_length=8, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'ktcdokiz'


class Ktchead(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    k0131 = models.CharField(max_length=2, blank=True, null=True)
    k032 = models.IntegerField(default=0, blank=True, null=True)
    k05 = models.IntegerField(default=0, blank=True, null=True)
    k07 = models.CharField(max_length=3, blank=True, null=True)
    kcurcode = models.CharField(max_length=3, blank=True, null=True)
    k121 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    k122 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    k202 = models.CharField(max_length=3, blank=True, null=True)
    k2021 = models.CharField(max_length=40, blank=True, null=True)
    k203 = models.CharField(max_length=250, blank=True, null=True)
    k221 = models.CharField(max_length=3, blank=True, null=True)
    k221c = models.CharField(max_length=3, blank=True, null=True)
    k222 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    k23 = models.DecimalField(default=0.00, max_digits=10, decimal_places=4, blank=True, null=True)
    k230 = models.DateField(blank=True, null=True)
    k54_itn = models.CharField(max_length=13, blank=True, null=True)
    k5410 = models.CharField(max_length=1, blank=True, null=True)
    k541 = models.CharField(max_length=14, blank=True, null=True)
    k541d = models.DateField(blank=True, null=True)
    k5411 = models.CharField(max_length=50, blank=True, null=True)
    k5411d = models.DateField(blank=True, null=True)
    k541_inn = models.CharField(max_length=12, blank=True, null=True)
    k541_kpp = models.CharField(max_length=9, blank=True, null=True)
    k542 = models.DateField(blank=True, null=True)
    k543 = models.CharField(max_length=4, blank=True, null=True)
    k5441 = models.CharField(max_length=150, blank=True, null=True)
    k5441nm = models.CharField(max_length=150, blank=True, null=True)
    k5441mdnm = models.CharField(max_length=150, blank=True, null=True)
    k5442 = models.CharField(max_length=50, blank=True, null=True)
    k5443 = models.CharField(max_length=250, blank=True, null=True)
    k5444 = models.CharField(max_length=50, blank=True, null=True)
    k5445 = models.DateField(blank=True, null=True)
    k5446 = models.DateField(blank=True, null=True)
    k5447 = models.CharField(max_length=50, blank=True, null=True)
    k5451 = models.CharField(max_length=2, blank=True, null=True)
    k5451a = models.CharField(max_length=15, blank=True, null=True)
    k54521 = models.CharField(max_length=11, blank=True, null=True)
    k54522 = models.CharField(max_length=25, blank=True, null=True)
    k54523 = models.CharField(max_length=150, blank=True, null=True)
    k5453 = models.DateField(blank=True, null=True)
    kb0 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    ka = models.DateField(blank=True, null=True)
    kc30 = models.CharField(max_length=2, blank=True, null=True)
    nblktc1 = models.CharField(max_length=8, blank=True, null=True)
    nblktc1p = models.CharField(max_length=8, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)
    ed_idid = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'ktchead'


class Ktcpk(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    k32 = models.IntegerField(default=0, blank=True, null=True)
    pksign = models.CharField(max_length=1, blank=True, null=True)
    pkvid = models.CharField(max_length=2, blank=True, null=True)
    pkkolvo = models.IntegerField(default=0, blank=True, null=True)
    pkinf = models.CharField(max_length=150, blank=True, null=True)
    nblktc1 = models.CharField(max_length=8, blank=True, null=True)
    nblktc1p = models.CharField(max_length=8, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'ktcpk'


class Ktcplbiz(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    kb0 = models.CharField(max_length=1, blank=True, null=True)
    kb1 = models.CharField(max_length=4, blank=True, null=True)
    kb2 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    kb3 = models.CharField(max_length=3, blank=True, null=True)
    kb6 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    kb61 = models.CharField(max_length=3, blank=True, null=True)
    kb7 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    nblktc1 = models.CharField(max_length=8, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'ktcplbiz'


class Ktcpltiz(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    k32 = models.IntegerField(default=0, blank=True, null=True)
    k470 = models.CharField(max_length=1, blank=True, null=True)
    k471 = models.CharField(max_length=4, blank=True, null=True)
    k471npp = models.IntegerField(default=0, blank=True, null=True)
    k472 = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    k4721 = models.CharField(max_length=3, blank=True, null=True)
    k473 = models.DecimalField(default=0.00, max_digits=12, decimal_places=6, blank=True, null=True)
    k4731 = models.CharField(max_length=1, blank=True, null=True)
    k4732 = models.CharField(max_length=3, blank=True, null=True)
    k4733 = models.CharField(max_length=3, blank=True, null=True)
    k4734 = models.DecimalField(default=0.00, max_digits=8, decimal_places=3, blank=True, null=True)
    kpp = models.IntegerField(default=0, blank=True, null=True)
    k474 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    k4741 = models.CharField(max_length=3, blank=True, null=True)
    k475 = models.CharField(max_length=2, blank=True, null=True)
    k476 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    k4761 = models.CharField(max_length=3, blank=True, null=True)
    k473z1_2 = models.CharField(max_length=1, blank=True, null=True)
    k473_2 = models.DecimalField(default=0.00, max_digits=12, decimal_places=6, blank=True, null=True)
    k4731_2 = models.CharField(max_length=1, blank=True, null=True)
    k4732_2 = models.CharField(max_length=3, blank=True, null=True)
    k4733_2 = models.CharField(max_length=3, blank=True, null=True)
    k4734_2 = models.DecimalField(default=0.00, max_digits=8, decimal_places=3, blank=True, null=True)
    k473z1_3 = models.CharField(max_length=1, blank=True, null=True)
    k473_3 = models.DecimalField(default=0.00, max_digits=12, decimal_places=6, blank=True, null=True)
    k4731_3 = models.CharField(max_length=1, blank=True, null=True)
    k4732_3 = models.CharField(max_length=3, blank=True, null=True)
    k4733_3 = models.CharField(max_length=3, blank=True, null=True)
    k4734_3 = models.DecimalField(default=0.00, max_digits=8, decimal_places=3, blank=True, null=True)
    k473z2_2 = models.IntegerField(default=0, blank=True, null=True)
    k477 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    iret = models.IntegerField(default=0, blank=True, null=True)
    k4730 = models.DateField(blank=True, null=True)
    k4740 = models.DateField(blank=True, null=True)
    k47_nd = models.IntegerField(default=0, blank=True, null=True)
    k47_ns = models.IntegerField(default=0, blank=True, null=True)
    k47_nm = models.IntegerField(default=0, blank=True, null=True)
    k47_tr = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, blank=True, null=True)
    nblktc1 = models.CharField(max_length=8, blank=True, null=True)
    nblktc1p = models.CharField(max_length=8, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'ktcpltiz'


class Ktcslotm(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    kc_01 = models.CharField(max_length=1, blank=True, null=True)
    kc_02 = models.CharField(max_length=2, blank=True, null=True)
    nrecc = models.IntegerField(default=0, blank=True, null=True)
    kc_1 = models.CharField(max_length=150, blank=True, null=True)
    kc_10 = models.CharField(max_length=2, blank=True, null=True)
    kc_11 = models.CharField(max_length=50, blank=True, null=True)
    kc_11d = models.DateField(blank=True, null=True)
    kc_2 = models.DateField(blank=True, null=True)
    kc_21 = models.CharField(max_length=8, blank=True, null=True)
    kc_6 = models.CharField(max_length=4, blank=True, null=True)
    kc_7 = models.CharField(max_length=40, blank=True, null=True)
    nblktc1 = models.CharField(max_length=8, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'ktcslotm'


class Ktcsltov(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    k32 = models.IntegerField(default=0, blank=True, null=True)
    nrecc = models.IntegerField(default=0, blank=True, null=True)
    kc_02 = models.CharField(max_length=2, blank=True, null=True)
    kc_1 = models.CharField(max_length=150, blank=True, null=True)
    kc_10 = models.CharField(max_length=2, blank=True, null=True)
    kc_11 = models.CharField(max_length=50, blank=True, null=True)
    kc_11d = models.DateField(blank=True, null=True)
    kc_2 = models.DateField(blank=True, null=True)
    kc_21 = models.CharField(max_length=8, blank=True, null=True)
    kc_6 = models.CharField(max_length=4, blank=True, null=True)
    kc_7 = models.CharField(max_length=40, blank=True, null=True)
    nblktc1 = models.CharField(max_length=8, blank=True, null=True)
    nblktc1p = models.CharField(max_length=8, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'ktcsltov'


class Ktcsumpp(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    k32 = models.IntegerField(default=0, blank=True, null=True)
    k471 = models.CharField(max_length=4, blank=True, null=True)
    k471npp = models.IntegerField(default=0, blank=True, null=True)
    k4741 = models.CharField(max_length=3, blank=True, null=True)
    k475 = models.CharField(max_length=2, blank=True, null=True)
    iret = models.IntegerField(default=0, blank=True, null=True)
    numpdok = models.CharField(max_length=50, blank=True, null=True)
    datpdok = models.DateField(blank=True, null=True)
    sum_all = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    sumpdok = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    valpdok = models.CharField(max_length=3, blank=True, null=True)
    datpostd = models.DateField(blank=True, null=True)
    datpaymt = models.DateField(blank=True, null=True)
    innplat = models.CharField(max_length=12, blank=True, null=True)
    kppplat = models.CharField(max_length=9, blank=True, null=True)
    lnpins = models.CharField(max_length=4, blank=True, null=True)
    fioins = models.CharField(max_length=40, blank=True, null=True)
    datins = models.DateField(blank=True, null=True)
    timins = models.CharField(max_length=8, blank=True, null=True)
    nblktc1 = models.CharField(max_length=8, blank=True, null=True)
    nblktc1p = models.CharField(max_length=8, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'ktcsumpp'


class Ktcterms(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    k32 = models.IntegerField(default=0, blank=True, null=True)
    terms = models.CharField(max_length=3, blank=True, null=True)
    termspoint = models.CharField(max_length=50, blank=True, null=True)
    termspass = models.CharField(max_length=250, blank=True, null=True)
    nblktc1 = models.CharField(max_length=8, blank=True, null=True)
    nblktc1p = models.CharField(max_length=8, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'ktcterms'


class Ktctovg(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    k32 = models.IntegerField(default=0, blank=True, null=True)
    k32g = models.IntegerField(default=0, blank=True, null=True)
    numrec = models.IntegerField(default=0, blank=True, null=True)
    k31_10 = models.CharField(max_length=4, blank=True, null=True)
    k31_11 = models.CharField(max_length=150, blank=True, null=True)
    k31_12 = models.CharField(max_length=150, blank=True, null=True)
    k31_14 = models.CharField(max_length=50, blank=True, null=True)
    k31_15_mod = models.CharField(max_length=50, blank=True, null=True)
    k31_15 = models.CharField(max_length=50, blank=True, null=True)
    k31_16 = models.CharField(max_length=50, blank=True, null=True)
    k31_17 = models.CharField(max_length=50, blank=True, null=True)
    k31_18 = models.CharField(max_length=30, blank=True, null=True)
    k31_19 = models.CharField(max_length=20, blank=True, null=True)
    k31_20 = models.CharField(max_length=50, blank=True, null=True)
    kolvo = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    code_edi = models.CharField(max_length=3, blank=True, null=True)
    name_edi = models.CharField(max_length=13, blank=True, null=True)
    nblktc1 = models.CharField(max_length=8, blank=True, null=True)
    nblktc1p = models.CharField(max_length=8, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'ktctovg'


class Ktctoviz(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    typ_ktc = models.IntegerField(default=0, blank=True, null=True)
    k011 = models.CharField(max_length=1, blank=True, null=True)
    k012 = models.CharField(max_length=4, blank=True, null=True)
    k013 = models.CharField(max_length=1, blank=True, null=True)
    k031 = models.IntegerField(default=0, blank=True, null=True)
    ch = models.IntegerField(default=0, blank=True, null=True)
    k31_1 = models.CharField(max_length=250, blank=True, null=True)
    k31_11 = models.CharField(max_length=50, blank=True, null=True)
    k31_1_prdt = models.DateField(blank=True, null=True)
    k31_1_oilf = models.CharField(max_length=250, blank=True, null=True)
    k31_2 = models.IntegerField(default=0, blank=True, null=True)
    k31_2part = models.IntegerField(default=0, blank=True, null=True)
    k31_20 = models.CharField(max_length=1, blank=True, null=True)
    k31_21 = models.CharField(max_length=150, blank=True, null=True)
    k31_7 = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    k31_8 = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    k31_9 = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    k31_fact = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    k32 = models.IntegerField(default=0, blank=True, null=True)
    k35 = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    k38 = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    k38_1 = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    k42 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    k43 = models.CharField(max_length=2, blank=True, null=True)
    k451 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    k452 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    k46 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    k461 = models.CharField(max_length=1, blank=True, null=True)
    k470 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    nblktc1 = models.CharField(max_length=8, blank=True, null=True)
    nblktc2 = models.CharField(max_length=8, blank=True, null=True)
    nblktc1p = models.CharField(max_length=8, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'ktctoviz'


class Ktctovs(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    k32 = models.IntegerField(default=0, blank=True, null=True)
    k32g = models.IntegerField(default=0, blank=True, null=True)
    numrec = models.IntegerField(default=0, blank=True, null=True)
    k31_15_sn = models.CharField(max_length=50, blank=True, null=True)
    nblktc1 = models.CharField(max_length=8, blank=True, null=True)
    nblktc1p = models.CharField(max_length=8, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'ktctovs'


class Ktdamnum(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    num_pp = models.IntegerField(default=0, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    series = models.CharField(max_length=9, blank=True, null=True)
    numstart = models.IntegerField(default=0, blank=True, null=True)
    numend = models.IntegerField(default=0, blank=True, null=True)
    kolvoam = models.IntegerField(default=0, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'ktdamnum'


class Ktdavtmb(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    num_pp = models.IntegerField(default=0, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    nud = models.CharField(max_length=12, blank=True, null=True)
    kodmrk = models.CharField(max_length=3, blank=True, null=True)
    namemrkcar = models.CharField(max_length=250, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)
    year = models.IntegerField(default=0, blank=True, null=True)
    price = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    pricev = models.CharField(max_length=3, blank=True, null=True)
    obem = models.IntegerField(default=0, blank=True, null=True)
    id = models.CharField(max_length=20, blank=True, null=True)
    nkuz = models.CharField(max_length=40, blank=True, null=True)
    kabina = models.CharField(max_length=40, blank=True, null=True)
    nsh = models.CharField(max_length=40, blank=True, null=True)
    ndv = models.CharField(max_length=40, blank=True, null=True)
    prim = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, blank=True, null=True)
    probeg = models.IntegerField(default=0, blank=True, null=True)
    probeged = models.CharField(max_length=3, blank=True, null=True)
    emergdev = models.CharField(max_length=50, blank=True, null=True)
    maxpower1 = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, blank=True, null=True)
    maxpower2 = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, blank=True, null=True)
    maxpower3 = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'ktdavtmb'


class Ktdcont(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    num_pp = models.IntegerField(default=0, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    container = models.CharField(max_length=17, blank=True, null=True)
    conttype = models.CharField(max_length=2, blank=True, null=True)
    contstat = models.CharField(max_length=1, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'ktdcont'


class Ktddinf2(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    num_pp = models.IntegerField(default=0, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    numpredd = models.IntegerField(default=0, blank=True, null=True)
    ngr = models.CharField(max_length=2, blank=True, null=True)
    typ_ngr = models.CharField(max_length=2, blank=True, null=True)
    g32g = models.IntegerField(default=0, blank=True, null=True)
    numrec = models.IntegerField(default=0, blank=True, null=True)
    text1 = models.CharField(max_length=250, blank=True, null=True)
    text2 = models.CharField(max_length=50, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'ktddinf2'


class Ktddinfo(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    num_pp = models.IntegerField(default=0, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    ngr = models.CharField(max_length=2, blank=True, null=True)
    typ_ngr = models.CharField(max_length=2, blank=True, null=True)
    g32g = models.IntegerField(default=0, blank=True, null=True)
    numrec = models.IntegerField(default=0, blank=True, null=True)
    text1 = models.CharField(max_length=250, blank=True, null=True)
    ind_text = models.CharField(max_length=3, blank=True, null=True)
    text2 = models.CharField(max_length=50, blank=True, null=True)
    typ_izm = models.CharField(max_length=1, blank=True, null=True)
    kolvo = models.DecimalField(default=0.00, max_digits=16, decimal_places=4, blank=True, null=True)
    code_edi = models.CharField(max_length=3, blank=True, null=True)
    name_edi = models.CharField(max_length=17, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'ktddinfo'


class Ktdhead(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    num_pp = models.IntegerField(default=0, blank=True, null=True)
    kstage = models.CharField(max_length=1, blank=True, null=True)
    kedsign = models.CharField(max_length=2, blank=True, null=True)
    g011 = models.CharField(max_length=2, blank=True, null=True)
    g0121 = models.CharField(max_length=2, blank=True, null=True)
    g0131 = models.CharField(max_length=2, blank=True, null=True)
    k0131 = models.CharField(max_length=2, blank=True, null=True)
    kbase = models.CharField(max_length=150, blank=True, null=True)
    kbasenum = models.CharField(max_length=50, blank=True, null=True)
    kbasedate = models.DateField(blank=True, null=True)
    g020 = models.CharField(max_length=15, blank=True, null=True)
    g021 = models.CharField(max_length=12, blank=True, null=True)
    g022 = models.CharField(max_length=150, blank=True, null=True)
    g023post = models.CharField(max_length=9, blank=True, null=True)
    g0231 = models.CharField(max_length=2, blank=True, null=True)
    g0231n = models.CharField(max_length=40, blank=True, null=True)
    g023subd = models.CharField(max_length=50, blank=True, null=True)
    g023city = models.CharField(max_length=35, blank=True, null=True)
    g023street = models.CharField(max_length=50, blank=True, null=True)
    g023build = models.CharField(max_length=50, blank=True, null=True)
    g027 = models.CharField(max_length=9, blank=True, null=True)
    g0281 = models.CharField(max_length=7, blank=True, null=True)
    g0281a = models.CharField(max_length=25, blank=True, null=True)
    g02821 = models.CharField(max_length=11, blank=True, null=True)
    g02822 = models.CharField(max_length=25, blank=True, null=True)
    g02823 = models.CharField(max_length=150, blank=True, null=True)
    g0283 = models.DateField(blank=True, null=True)
    g022a = models.CharField(max_length=150, blank=True, null=True)
    g027a = models.CharField(max_length=9, blank=True, null=True)
    g023apost = models.CharField(max_length=9, blank=True, null=True)
    g0231a = models.CharField(max_length=2, blank=True, null=True)
    g0231an = models.CharField(max_length=40, blank=True, null=True)
    g023asubd = models.CharField(max_length=50, blank=True, null=True)
    g023acity = models.CharField(max_length=35, blank=True, null=True)
    g023astree = models.CharField(max_length=50, blank=True, null=True)
    g023abuild = models.CharField(max_length=50, blank=True, null=True)
    g029 = models.CharField(max_length=1, blank=True, null=True)
    g02e14 = models.CharField(max_length=1, blank=True, null=True)
    k032 = models.IntegerField(default=0, blank=True, null=True)
    g032 = models.IntegerField(default=0, blank=True, null=True)
    g040 = models.IntegerField(default=0, blank=True, null=True)
    g04 = models.IntegerField(default=0, blank=True, null=True)
    k05 = models.IntegerField(default=0, blank=True, null=True)
    g05 = models.IntegerField(default=0, blank=True, null=True)
    g06 = models.IntegerField(default=0, blank=True, null=True)
    g07 = models.CharField(max_length=3, blank=True, null=True)
    g080 = models.CharField(max_length=15, blank=True, null=True)
    g081 = models.CharField(max_length=12, blank=True, null=True)
    g082 = models.CharField(max_length=150, blank=True, null=True)
    g083post = models.CharField(max_length=9, blank=True, null=True)
    g0831 = models.CharField(max_length=2, blank=True, null=True)
    g0831a = models.CharField(max_length=40, blank=True, null=True)
    g083subd = models.CharField(max_length=50, blank=True, null=True)
    g083city = models.CharField(max_length=35, blank=True, null=True)
    g083street = models.CharField(max_length=50, blank=True, null=True)
    g083build = models.CharField(max_length=50, blank=True, null=True)
    g087 = models.CharField(max_length=9, blank=True, null=True)
    g0881 = models.CharField(max_length=7, blank=True, null=True)
    g0881a = models.CharField(max_length=25, blank=True, null=True)
    g08821 = models.CharField(max_length=11, blank=True, null=True)
    g08822 = models.CharField(max_length=25, blank=True, null=True)
    g08823 = models.CharField(max_length=150, blank=True, null=True)
    g0883 = models.DateField(blank=True, null=True)
    g089 = models.CharField(max_length=1, blank=True, null=True)
    g082a = models.CharField(max_length=150, blank=True, null=True)
    g087a = models.CharField(max_length=9, blank=True, null=True)
    g083apost = models.CharField(max_length=9, blank=True, null=True)
    g0831aa = models.CharField(max_length=2, blank=True, null=True)
    g0831an = models.CharField(max_length=40, blank=True, null=True)
    g083asubd = models.CharField(max_length=50, blank=True, null=True)
    g083acity = models.CharField(max_length=35, blank=True, null=True)
    g083astree = models.CharField(max_length=50, blank=True, null=True)
    g083abuild = models.CharField(max_length=50, blank=True, null=True)
    g08e14 = models.CharField(max_length=1, blank=True, null=True)
    g090 = models.CharField(max_length=15, blank=True, null=True)
    g091 = models.CharField(max_length=12, blank=True, null=True)
    g092 = models.CharField(max_length=150, blank=True, null=True)
    g092a = models.CharField(max_length=150, blank=True, null=True)
    g093post = models.CharField(max_length=9, blank=True, null=True)
    g0931 = models.CharField(max_length=2, blank=True, null=True)
    g0931n = models.CharField(max_length=40, blank=True, null=True)
    g093subd = models.CharField(max_length=50, blank=True, null=True)
    g093city = models.CharField(max_length=35, blank=True, null=True)
    g093street = models.CharField(max_length=50, blank=True, null=True)
    g093build = models.CharField(max_length=50, blank=True, null=True)
    g093apost = models.CharField(max_length=9, blank=True, null=True)
    g0931a = models.CharField(max_length=2, blank=True, null=True)
    g0931an = models.CharField(max_length=40, blank=True, null=True)
    g093asubd = models.CharField(max_length=50, blank=True, null=True)
    g093acity = models.CharField(max_length=35, blank=True, null=True)
    g093astree = models.CharField(max_length=50, blank=True, null=True)
    g093abuild = models.CharField(max_length=50, blank=True, null=True)
    g097 = models.CharField(max_length=9, blank=True, null=True)
    g097a = models.CharField(max_length=9, blank=True, null=True)
    g0981 = models.CharField(max_length=7, blank=True, null=True)
    g0981a = models.CharField(max_length=25, blank=True, null=True)
    g09821 = models.CharField(max_length=11, blank=True, null=True)
    g09822 = models.CharField(max_length=25, blank=True, null=True)
    g09823 = models.CharField(max_length=150, blank=True, null=True)
    g0983 = models.DateField(blank=True, null=True)
    g09e14 = models.CharField(max_length=1, blank=True, null=True)
    g11 = models.CharField(max_length=2, blank=True, null=True)
    g12 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    g121 = models.CharField(max_length=3, blank=True, null=True)
    g12k = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    g122 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    g140 = models.CharField(max_length=15, blank=True, null=True)
    g141 = models.CharField(max_length=12, blank=True, null=True)
    g142 = models.CharField(max_length=150, blank=True, null=True)
    g142a = models.CharField(max_length=150, blank=True, null=True)
    g143post = models.CharField(max_length=9, blank=True, null=True)
    g1431 = models.CharField(max_length=2, blank=True, null=True)
    g1431n = models.CharField(max_length=40, blank=True, null=True)
    g143subd = models.CharField(max_length=50, blank=True, null=True)
    g143city = models.CharField(max_length=35, blank=True, null=True)
    g143street = models.CharField(max_length=50, blank=True, null=True)
    g143build = models.CharField(max_length=50, blank=True, null=True)
    aeorowner = models.CharField(max_length=1, blank=True, null=True)
    aeocntry = models.CharField(max_length=2, blank=True, null=True)
    aeonum = models.CharField(max_length=50, blank=True, null=True)
    aeokind = models.CharField(max_length=1, blank=True, null=True)
    aeoregcod = models.CharField(max_length=3, blank=True, null=True)
    g143apost = models.CharField(max_length=9, blank=True, null=True)
    g1431a = models.CharField(max_length=2, blank=True, null=True)
    g1431an = models.CharField(max_length=40, blank=True, null=True)
    g143asubd = models.CharField(max_length=50, blank=True, null=True)
    g143acity = models.CharField(max_length=35, blank=True, null=True)
    g143astree = models.CharField(max_length=50, blank=True, null=True)
    g143abuild = models.CharField(max_length=50, blank=True, null=True)
    g147 = models.CharField(max_length=9, blank=True, null=True)
    g147a = models.CharField(max_length=9, blank=True, null=True)
    g1481 = models.CharField(max_length=7, blank=True, null=True)
    g1481a = models.CharField(max_length=25, blank=True, null=True)
    g14821 = models.CharField(max_length=11, blank=True, null=True)
    g14822 = models.CharField(max_length=25, blank=True, null=True)
    g14823 = models.CharField(max_length=150, blank=True, null=True)
    g1483 = models.DateField(blank=True, null=True)
    g15 = models.CharField(max_length=40, blank=True, null=True)
    g15a = models.CharField(max_length=2, blank=True, null=True)
    g16a = models.CharField(max_length=2, blank=True, null=True)
    g16 = models.CharField(max_length=40, blank=True, null=True)
    g17a = models.CharField(max_length=2, blank=True, null=True)
    g17b = models.CharField(max_length=40, blank=True, null=True)
    g180 = models.IntegerField(default=0, blank=True, null=True)
    g182 = models.CharField(max_length=2, blank=True, null=True)
    g19 = models.CharField(max_length=1, blank=True, null=True)
    g202 = models.CharField(max_length=3, blank=True, null=True)
    g2021 = models.CharField(max_length=50, blank=True, null=True)
    g203 = models.CharField(max_length=250, blank=True, null=True)
    g210 = models.IntegerField(default=0, blank=True, null=True)
    g212 = models.CharField(max_length=2, blank=True, null=True)
    g221 = models.CharField(max_length=3, blank=True, null=True)
    g222 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    g222k = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    g23 = models.DecimalField(default=0.00, max_digits=10, decimal_places=4, blank=True, null=True)
    g230 = models.DateField(blank=True, null=True)
    g270 = models.CharField(max_length=2, blank=True, null=True)
    g2710 = models.CharField(max_length=1, blank=True, null=True)
    g271 = models.CharField(max_length=13, blank=True, null=True)
    g27 = models.CharField(max_length=40, blank=True, null=True)
    g2711 = models.DateField(blank=True, null=True)
    g2712 = models.CharField(max_length=8, blank=True, null=True)
    g28okpo = models.CharField(max_length=10, blank=True, null=True)
    g28inn = models.CharField(max_length=12, blank=True, null=True)
    g281oth = models.CharField(max_length=30, blank=True, null=True)
    g282 = models.CharField(max_length=70, blank=True, null=True)
    g28211 = models.CharField(max_length=1, blank=True, null=True)
    g28212 = models.CharField(max_length=2, blank=True, null=True)
    g28221 = models.CharField(max_length=3, blank=True, null=True)
    g28222 = models.CharField(max_length=1, blank=True, null=True)
    g28230 = models.CharField(max_length=1, blank=True, null=True)
    g2823 = models.DateField(blank=True, null=True)
    g28240 = models.CharField(max_length=1, blank=True, null=True)
    g2824 = models.DateField(blank=True, null=True)
    g2825 = models.CharField(max_length=3, blank=True, null=True)
    g300 = models.CharField(max_length=2, blank=True, null=True)
    g3010 = models.CharField(max_length=1, blank=True, null=True)
    g30aeoown = models.CharField(max_length=1, blank=True, null=True)
    g30aeocntr = models.CharField(max_length=2, blank=True, null=True)
    g301 = models.CharField(max_length=50, blank=True, null=True)
    g30aeokind = models.CharField(max_length=1, blank=True, null=True)
    g30aeorcod = models.CharField(max_length=3, blank=True, null=True)
    g3011 = models.DateField(blank=True, null=True)
    g30 = models.CharField(max_length=50, blank=True, null=True)
    g30d = models.DateField(blank=True, null=True)
    g30post = models.CharField(max_length=9, blank=True, null=True)
    g30a = models.CharField(max_length=2, blank=True, null=True)
    g30an = models.CharField(max_length=40, blank=True, null=True)
    g30subd = models.CharField(max_length=50, blank=True, null=True)
    g30city = models.CharField(max_length=35, blank=True, null=True)
    g30street = models.CharField(max_length=50, blank=True, null=True)
    g30build = models.CharField(max_length=50, blank=True, null=True)
    g30lname = models.CharField(max_length=150, blank=True, null=True)
    g3012 = models.CharField(max_length=8, blank=True, null=True)
    g30121 = models.CharField(max_length=2, blank=True, null=True)
    g30122 = models.CharField(max_length=50, blank=True, null=True)
    g45a1 = models.CharField(max_length=1, blank=True, null=True)
    g45a2 = models.CharField(max_length=1, blank=True, null=True)
    g45a3 = models.CharField(max_length=1, blank=True, null=True)
    g45a4 = models.CharField(max_length=1, blank=True, null=True)
    g45a5 = models.CharField(max_length=1, blank=True, null=True)
    g45a6 = models.CharField(max_length=1, blank=True, null=True)
    g45a7 = models.CharField(max_length=1, blank=True, null=True)
    g45a8 = models.CharField(max_length=1, blank=True, null=True)
    d54_itn = models.CharField(max_length=13, blank=True, null=True)
    d5410 = models.CharField(max_length=1, blank=True, null=True)
    d541 = models.CharField(max_length=14, blank=True, null=True)
    d541d = models.DateField(blank=True, null=True)
    d5411 = models.CharField(max_length=50, blank=True, null=True)
    d5411d = models.DateField(blank=True, null=True)
    d5411aid = models.CharField(max_length=50, blank=True, null=True)
    d5411adid = models.CharField(max_length=50, blank=True, null=True)
    d5411modid = models.CharField(max_length=10, blank=True, null=True)
    d5411doc = models.CharField(max_length=5, blank=True, null=True)
    prprovd541 = models.CharField(max_length=1, blank=True, null=True)
    pretypd541 = models.CharField(max_length=1, blank=True, null=True)
    prvnumd541 = models.CharField(max_length=50, blank=True, null=True)
    d541_inn = models.CharField(max_length=12, blank=True, null=True)
    d541_kpp = models.CharField(max_length=9, blank=True, null=True)
    d542 = models.DateField(blank=True, null=True)
    d542t = models.CharField(max_length=8, blank=True, null=True)
    d5441 = models.CharField(max_length=150, blank=True, null=True)
    d5441nm = models.CharField(max_length=150, blank=True, null=True)
    d5441mdnm = models.CharField(max_length=150, blank=True, null=True)
    d5442 = models.CharField(max_length=50, blank=True, null=True)
    d5443 = models.CharField(max_length=250, blank=True, null=True)
    d5444 = models.CharField(max_length=50, blank=True, null=True)
    d5445 = models.DateField(blank=True, null=True)
    d544aid = models.CharField(max_length=50, blank=True, null=True)
    d544adid = models.CharField(max_length=50, blank=True, null=True)
    d544modid = models.CharField(max_length=10, blank=True, null=True)
    d544doc = models.CharField(max_length=5, blank=True, null=True)
    prprovd544 = models.CharField(max_length=1, blank=True, null=True)
    pretypd544 = models.CharField(max_length=1, blank=True, null=True)
    prvnumd544 = models.CharField(max_length=50, blank=True, null=True)
    d5446 = models.DateField(blank=True, null=True)
    d5447 = models.CharField(max_length=50, blank=True, null=True)
    d5451 = models.CharField(max_length=7, blank=True, null=True)
    d5451a = models.CharField(max_length=25, blank=True, null=True)
    d54521 = models.CharField(max_length=11, blank=True, null=True)
    d54522 = models.CharField(max_length=25, blank=True, null=True)
    d54523 = models.CharField(max_length=150, blank=True, null=True)
    d5453 = models.DateField(blank=True, null=True)
    d545aid = models.CharField(max_length=50, blank=True, null=True)
    d545adid = models.CharField(max_length=50, blank=True, null=True)
    d545modid = models.CharField(max_length=10, blank=True, null=True)
    d545doc = models.CharField(max_length=5, blank=True, null=True)
    prprovd545 = models.CharField(max_length=1, blank=True, null=True)
    pretypd545 = models.CharField(max_length=1, blank=True, null=True)
    prvnumd545 = models.CharField(max_length=50, blank=True, null=True)
    g54_itn = models.CharField(max_length=13, blank=True, null=True)
    g5410 = models.CharField(max_length=1, blank=True, null=True)
    g541 = models.CharField(max_length=14, blank=True, null=True)
    g541d = models.DateField(blank=True, null=True)
    g5411 = models.CharField(max_length=50, blank=True, null=True)
    g5411d = models.DateField(blank=True, null=True)
    g5411aid = models.CharField(max_length=50, blank=True, null=True)
    g5411adid = models.CharField(max_length=50, blank=True, null=True)
    g5411modid = models.CharField(max_length=10, blank=True, null=True)
    g5411doc = models.CharField(max_length=5, blank=True, null=True)
    prprovg541 = models.CharField(max_length=1, blank=True, null=True)
    pretypg541 = models.CharField(max_length=1, blank=True, null=True)
    prvnumg541 = models.CharField(max_length=50, blank=True, null=True)
    g541_inn = models.CharField(max_length=12, blank=True, null=True)
    g541_kpp = models.CharField(max_length=9, blank=True, null=True)
    g542 = models.DateField(blank=True, null=True)
    g542t = models.CharField(max_length=8, blank=True, null=True)
    g543 = models.CharField(max_length=4, blank=True, null=True)
    g542d = models.DateField(blank=True, null=True)
    g5441 = models.CharField(max_length=150, blank=True, null=True)
    g5441nm = models.CharField(max_length=150, blank=True, null=True)
    g5441mdnm = models.CharField(max_length=150, blank=True, null=True)
    g5442 = models.CharField(max_length=50, blank=True, null=True)
    g5443 = models.CharField(max_length=250, blank=True, null=True)
    g5444 = models.CharField(max_length=50, blank=True, null=True)
    g5445 = models.DateField(blank=True, null=True)
    g544aid = models.CharField(max_length=50, blank=True, null=True)
    g544adid = models.CharField(max_length=50, blank=True, null=True)
    g544modid = models.CharField(max_length=10, blank=True, null=True)
    g544doc = models.CharField(max_length=5, blank=True, null=True)
    prprovg544 = models.CharField(max_length=1, blank=True, null=True)
    pretypg544 = models.CharField(max_length=1, blank=True, null=True)
    prvnumg544 = models.CharField(max_length=50, blank=True, null=True)
    g5446 = models.DateField(blank=True, null=True)
    g5447 = models.CharField(max_length=50, blank=True, null=True)
    g5451 = models.CharField(max_length=7, blank=True, null=True)
    g5451a = models.CharField(max_length=25, blank=True, null=True)
    g54521 = models.CharField(max_length=11, blank=True, null=True)
    g54522 = models.CharField(max_length=25, blank=True, null=True)
    g54523 = models.CharField(max_length=150, blank=True, null=True)
    g5453 = models.DateField(blank=True, null=True)
    g545aid = models.CharField(max_length=50, blank=True, null=True)
    g545adid = models.CharField(max_length=50, blank=True, null=True)
    g545modid = models.CharField(max_length=10, blank=True, null=True)
    g545doc = models.CharField(max_length=5, blank=True, null=True)
    prprovg545 = models.CharField(max_length=1, blank=True, null=True)
    pretypg545 = models.CharField(max_length=1, blank=True, null=True)
    prvnumg545 = models.CharField(max_length=50, blank=True, null=True)
    kb0 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)
    ed_idid = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'ktdhead'


class Ktdpasp(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    num_pp = models.IntegerField(default=0, blank=True, null=True)
    g2810 = models.CharField(max_length=1, blank=True, null=True)
    pasp = models.CharField(max_length=25, blank=True, null=True)
    paspdd = models.DateField(blank=True, null=True)
    pasp0 = models.CharField(max_length=1, blank=True, null=True)
    pasp1 = models.CharField(max_length=25, blank=True, null=True)
    pasp1dd = models.DateField(blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'ktdpasp'


class Ktdpk(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    num_pp = models.IntegerField(default=0, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    pksign = models.CharField(max_length=1, blank=True, null=True)
    pkvid = models.CharField(max_length=2, blank=True, null=True)
    pkkolvo = models.IntegerField(default=0, blank=True, null=True)
    pkinf = models.CharField(max_length=150, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'ktdpk'


class Ktdplbiz(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    num_pp = models.IntegerField(default=0, blank=True, null=True)
    kb0 = models.CharField(max_length=1, blank=True, null=True)
    kb1 = models.CharField(max_length=4, blank=True, null=True)
    kb2 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    kb3 = models.CharField(max_length=3, blank=True, null=True)
    kb4 = models.DecimalField(default=0.00, max_digits=10, decimal_places=4, blank=True, null=True)
    kb5 = models.CharField(max_length=2, blank=True, null=True)
    iret = models.IntegerField(default=0, blank=True, null=True)
    kb6 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    kb61 = models.CharField(max_length=3, blank=True, null=True)
    kb7 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    kb8 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'ktdplbiz'


class Ktdpltiz(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    num_pp = models.IntegerField(default=0, blank=True, null=True)
    k32 = models.IntegerField(default=0, blank=True, null=True)
    k470 = models.CharField(max_length=1, blank=True, null=True)
    k471 = models.CharField(max_length=4, blank=True, null=True)
    k471npp = models.IntegerField(default=0, blank=True, null=True)
    k472 = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    k4721 = models.CharField(max_length=3, blank=True, null=True)
    k4723 = models.CharField(max_length=3, blank=True, null=True)
    k4722 = models.CharField(max_length=50, blank=True, null=True)
    k473 = models.DecimalField(default=0.00, max_digits=12, decimal_places=6, blank=True, null=True)
    k4731 = models.CharField(max_length=1, blank=True, null=True)
    k4732 = models.CharField(max_length=3, blank=True, null=True)
    k4733 = models.CharField(max_length=3, blank=True, null=True)
    k4734 = models.DecimalField(default=0.00, max_digits=8, decimal_places=3, blank=True, null=True)
    kpp = models.IntegerField(default=0, blank=True, null=True)
    k474 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    k4741 = models.CharField(max_length=3, blank=True, null=True)
    k475 = models.CharField(max_length=2, blank=True, null=True)
    k476 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    k4761 = models.CharField(max_length=3, blank=True, null=True)
    k473z1_2 = models.CharField(max_length=1, blank=True, null=True)
    k473_2 = models.DecimalField(default=0.00, max_digits=12, decimal_places=6, blank=True, null=True)
    k4731_2 = models.CharField(max_length=1, blank=True, null=True)
    k4732_2 = models.CharField(max_length=3, blank=True, null=True)
    k4733_2 = models.CharField(max_length=3, blank=True, null=True)
    k4734_2 = models.DecimalField(default=0.00, max_digits=8, decimal_places=3, blank=True, null=True)
    k473z1_3 = models.CharField(max_length=1, blank=True, null=True)
    k473_3 = models.DecimalField(default=0.00, max_digits=12, decimal_places=6, blank=True, null=True)
    k4731_3 = models.CharField(max_length=1, blank=True, null=True)
    k4732_3 = models.CharField(max_length=3, blank=True, null=True)
    k4733_3 = models.CharField(max_length=3, blank=True, null=True)
    k4734_3 = models.DecimalField(default=0.00, max_digits=8, decimal_places=3, blank=True, null=True)
    k473z2_2 = models.IntegerField(default=0, blank=True, null=True)
    k4730 = models.DateField(blank=True, null=True)
    k4740 = models.DateField(blank=True, null=True)
    k47_nd = models.IntegerField(default=0, blank=True, null=True)
    k47_ns = models.IntegerField(default=0, blank=True, null=True)
    k47_nm = models.IntegerField(default=0, blank=True, null=True)
    k47_tr = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, blank=True, null=True)
    k47trf = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, blank=True, null=True)
    k47_g40 = models.IntegerField(default=0, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'ktdpltiz'


class Ktdpredd(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    num_pp = models.IntegerField(default=0, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    numrec = models.IntegerField(default=0, blank=True, null=True)
    g40_cntry = models.CharField(max_length=2, blank=True, null=True)
    g40_0 = models.CharField(max_length=2, blank=True, null=True)
    prevnumtyp = models.CharField(max_length=1, blank=True, null=True)
    g40_naim = models.CharField(max_length=250, blank=True, null=True)
    g40_1 = models.CharField(max_length=8, blank=True, null=True)
    g40_2 = models.DateField(blank=True, null=True)
    g40_21 = models.CharField(max_length=2, blank=True, null=True)
    g40_3 = models.CharField(max_length=9, blank=True, null=True)
    g40_31 = models.CharField(max_length=2, blank=True, null=True)
    g40_4 = models.IntegerField(default=0, blank=True, null=True)
    g40_doctyp = models.CharField(max_length=5, blank=True, null=True)
    g40tnved = models.CharField(max_length=10, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'ktdpredd'


class Ktdslotm(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    num_pp = models.IntegerField(default=0, blank=True, null=True)
    ngr = models.CharField(max_length=2, blank=True, null=True)
    gc_01 = models.CharField(max_length=1, blank=True, null=True)
    gc_02 = models.CharField(max_length=2, blank=True, null=True)
    gc_03 = models.CharField(max_length=1, blank=True, null=True)
    nrecc = models.IntegerField(default=0, blank=True, null=True)
    gc_1 = models.CharField(max_length=150, blank=True, null=True)
    gc_nresh = models.CharField(max_length=29, blank=True, null=True)
    gc_doc = models.CharField(max_length=50, blank=True, null=True)
    gc_docd = models.DateField(blank=True, null=True)
    gc_2 = models.DateField(blank=True, null=True)
    gc_21 = models.CharField(max_length=8, blank=True, null=True)
    gc_6 = models.CharField(max_length=4, blank=True, null=True)
    gc_7 = models.CharField(max_length=40, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'ktdslotm'


class Ktdsltov(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    num_pp = models.IntegerField(default=0, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    ngr = models.CharField(max_length=2, blank=True, null=True)
    gc_01 = models.CharField(max_length=1, blank=True, null=True)
    gc_02 = models.CharField(max_length=2, blank=True, null=True)
    nrecc = models.IntegerField(default=0, blank=True, null=True)
    gc_1 = models.CharField(max_length=150, blank=True, null=True)
    gc_nresh = models.CharField(max_length=29, blank=True, null=True)
    gc_doc = models.CharField(max_length=50, blank=True, null=True)
    gc_docd = models.DateField(blank=True, null=True)
    gc_2 = models.DateField(blank=True, null=True)
    gc_21 = models.CharField(max_length=8, blank=True, null=True)
    gc_6 = models.CharField(max_length=4, blank=True, null=True)
    gc_7 = models.CharField(max_length=40, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'ktdsltov'


class Ktdsumpp(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    num_pp = models.IntegerField(default=0, blank=True, null=True)
    gb1 = models.CharField(max_length=4, blank=True, null=True)
    gb3 = models.CharField(max_length=3, blank=True, null=True)
    gb5 = models.CharField(max_length=2, blank=True, null=True)
    iret = models.IntegerField(default=0, blank=True, null=True)
    numpdok = models.CharField(max_length=50, blank=True, null=True)
    datpdok = models.DateField(blank=True, null=True)
    sum_all = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    sumpdok = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    valpdok = models.CharField(max_length=3, blank=True, null=True)
    datpostd = models.DateField(blank=True, null=True)
    datpaymt = models.DateField(blank=True, null=True)
    innplat = models.CharField(max_length=12, blank=True, null=True)
    kppplat = models.CharField(max_length=9, blank=True, null=True)
    lnpins = models.CharField(max_length=4, blank=True, null=True)
    fioins = models.CharField(max_length=40, blank=True, null=True)
    datins = models.DateField(blank=True, null=True)
    timins = models.CharField(max_length=8, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'ktdsumpp'


class Ktdtcim(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    num_pp = models.IntegerField(default=0, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    numrec = models.IntegerField(default=0, blank=True, null=True)
    firstcimid = models.CharField(max_length=20, blank=True, null=True)
    lastcimid = models.CharField(max_length=20, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'ktdtcim'


class Ktdtechd(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    num_pp = models.IntegerField(default=0, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    g4401 = models.IntegerField(default=0, blank=True, null=True)
    g4402 = models.IntegerField(default=0, blank=True, null=True)
    g44020 = models.CharField(max_length=1, blank=True, null=True)
    g44_cust = models.CharField(max_length=8, blank=True, null=True)
    g440 = models.CharField(max_length=4, blank=True, null=True)
    g441 = models.CharField(max_length=5, blank=True, null=True)
    g441a = models.CharField(max_length=2, blank=True, null=True)
    prprovid = models.CharField(max_length=1, blank=True, null=True)
    ed_aid = models.CharField(max_length=50, blank=True, null=True)
    ed_adid = models.CharField(max_length=50, blank=True, null=True)
    prevnumtyp = models.CharField(max_length=1, blank=True, null=True)
    prevnumdoc = models.CharField(max_length=50, blank=True, null=True)
    recordid = models.CharField(max_length=36, blank=True, null=True)
    executbody = models.CharField(max_length=10, blank=True, null=True)
    execname = models.CharField(max_length=250, blank=True, null=True)
    ineturl = models.CharField(max_length=255, blank=True, null=True)
    docmodeid = models.CharField(max_length=10, blank=True, null=True)
    g442 = models.CharField(max_length=50, blank=True, null=True)
    g442lic1 = models.IntegerField(default=0, blank=True, null=True)
    g442lic2 = models.IntegerField(default=0, blank=True, null=True)
    g442r = models.CharField(max_length=28, blank=True, null=True)
    g442simp = models.CharField(max_length=10, blank=True, null=True)
    g44mdp1 = models.IntegerField(default=0, blank=True, null=True)
    g44mdp2 = models.CharField(max_length=18, blank=True, null=True)
    g443 = models.DateField(blank=True, null=True)
    g444 = models.CharField(max_length=250, blank=True, null=True)
    g445 = models.CharField(max_length=150, blank=True, null=True)
    g446 = models.DateField(blank=True, null=True)
    g447 = models.DateField(blank=True, null=True)
    g4480et = models.CharField(max_length=10, blank=True, null=True)
    g4481et = models.DateField(blank=True, null=True)
    g44stper = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    g44sfcntry = models.CharField(max_length=2, blank=True, null=True)
    g44alldoc = models.IntegerField(default=0, blank=True, null=True)
    g4491 = models.DateField(blank=True, null=True)
    g4492 = models.DateField(blank=True, null=True)
    g4493 = models.CharField(max_length=2, blank=True, null=True)
    g44dd = models.DateField(blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'ktdtechd'


class Ktdterms(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    num_pp = models.IntegerField(default=0, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    terms = models.CharField(max_length=3, blank=True, null=True)
    termspoint = models.CharField(max_length=50, blank=True, null=True)
    termspass = models.CharField(max_length=250, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'ktdterms'


class Ktdtois(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    num_pp = models.IntegerField(default=0, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    numrec = models.IntegerField(default=0, blank=True, null=True)
    typeois = models.CharField(max_length=1, blank=True, null=True)
    cntrycode = models.CharField(max_length=2, blank=True, null=True)
    iporegnum = models.CharField(max_length=25, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'ktdtois'


class Ktdtov2(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    num_pp = models.IntegerField(default=0, blank=True, null=True)
    g031 = models.IntegerField(default=0, blank=True, null=True)
    g31_1 = models.CharField(max_length=250, blank=True, null=True)
    g31_7 = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    g31_71 = models.CharField(max_length=13, blank=True, null=True)
    g31_8 = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    g31_81 = models.CharField(max_length=13, blank=True, null=True)
    g31_82 = models.CharField(max_length=3, blank=True, null=True)
    g31_9 = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    g31_91 = models.CharField(max_length=13, blank=True, null=True)
    g31_92 = models.CharField(max_length=3, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    numpredd = models.IntegerField(default=0, blank=True, null=True)
    g33 = models.CharField(max_length=10, blank=True, null=True)
    g330 = models.CharField(max_length=1, blank=True, null=True)
    g331 = models.CharField(max_length=1, blank=True, null=True)
    g332 = models.CharField(max_length=1, blank=True, null=True)
    g333 = models.CharField(max_length=4, blank=True, null=True)
    g340 = models.CharField(max_length=1, blank=True, null=True)
    g34 = models.CharField(max_length=2, blank=True, null=True)
    g35 = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    g36 = models.CharField(max_length=7, blank=True, null=True)
    g37 = models.CharField(max_length=7, blank=True, null=True)
    g38 = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    g38_1 = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    g40_g38 = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    numrec = models.IntegerField(default=0, blank=True, null=True)
    g41a = models.CharField(max_length=3, blank=True, null=True)
    g42 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    g45 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'ktdtov2'


class Ktdtovar(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    num_pp = models.IntegerField(default=0, blank=True, null=True)
    g020 = models.CharField(max_length=15, blank=True, null=True)
    g021 = models.CharField(max_length=12, blank=True, null=True)
    g022 = models.CharField(max_length=150, blank=True, null=True)
    g023post = models.CharField(max_length=9, blank=True, null=True)
    g0231 = models.CharField(max_length=2, blank=True, null=True)
    g0231n = models.CharField(max_length=40, blank=True, null=True)
    g023subd = models.CharField(max_length=50, blank=True, null=True)
    g023city = models.CharField(max_length=35, blank=True, null=True)
    g023street = models.CharField(max_length=50, blank=True, null=True)
    g023build = models.CharField(max_length=50, blank=True, null=True)
    g027 = models.CharField(max_length=9, blank=True, null=True)
    g022a = models.CharField(max_length=150, blank=True, null=True)
    g027a = models.CharField(max_length=9, blank=True, null=True)
    g0281 = models.CharField(max_length=7, blank=True, null=True)
    g0281a = models.CharField(max_length=25, blank=True, null=True)
    g02821 = models.CharField(max_length=11, blank=True, null=True)
    g02822 = models.CharField(max_length=25, blank=True, null=True)
    g02823 = models.CharField(max_length=150, blank=True, null=True)
    g0283 = models.DateField(blank=True, null=True)
    k031 = models.IntegerField(default=0, blank=True, null=True)
    g031 = models.IntegerField(default=0, blank=True, null=True)
    ch = models.IntegerField(default=0, blank=True, null=True)
    g31_1 = models.CharField(max_length=250, blank=True, null=True)
    g31_13 = models.CharField(max_length=40, blank=True, null=True)
    g31_1_prdt = models.DateField(blank=True, null=True)
    g31_1_oilf = models.CharField(max_length=250, blank=True, null=True)
    g31_2 = models.IntegerField(default=0, blank=True, null=True)
    g31_2part = models.IntegerField(default=0, blank=True, null=True)
    g31_20 = models.CharField(max_length=1, blank=True, null=True)
    g31_3 = models.IntegerField(default=0, blank=True, null=True)
    g31_7 = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    g31_71 = models.CharField(max_length=13, blank=True, null=True)
    g31_8 = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    g31_81 = models.CharField(max_length=13, blank=True, null=True)
    g31_82 = models.CharField(max_length=3, blank=True, null=True)
    g31_9 = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    g31_91 = models.CharField(max_length=13, blank=True, null=True)
    g31_92 = models.CharField(max_length=3, blank=True, null=True)
    g31_d1 = models.DateField(blank=True, null=True)
    g31_d2 = models.DateField(blank=True, null=True)
    g31_p1 = models.CharField(max_length=7, blank=True, null=True)
    g31_p2 = models.CharField(max_length=7, blank=True, null=True)
    g31_fact = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    g31_fc_1 = models.CharField(max_length=3, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    g32kdt = models.IntegerField(default=0, blank=True, null=True)
    g32_1 = models.CharField(max_length=3, blank=True, null=True)
    g33 = models.CharField(max_length=10, blank=True, null=True)
    g330 = models.CharField(max_length=1, blank=True, null=True)
    g331 = models.CharField(max_length=1, blank=True, null=True)
    g332 = models.CharField(max_length=1, blank=True, null=True)
    g333 = models.CharField(max_length=4, blank=True, null=True)
    cimsign = models.CharField(max_length=1, blank=True, null=True)
    tcimflag = models.CharField(max_length=2, blank=True, null=True)
    tcimkol = models.IntegerField(default=0, blank=True, null=True)
    g340 = models.CharField(max_length=1, blank=True, null=True)
    g34 = models.CharField(max_length=2, blank=True, null=True)
    g35 = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    g35k = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    g36 = models.CharField(max_length=7, blank=True, null=True)
    g37 = models.CharField(max_length=7, blank=True, null=True)
    g38 = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    g38k = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    g38_1 = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    g39 = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    g3911 = models.CharField(max_length=3, blank=True, null=True)
    g3912 = models.CharField(max_length=3, blank=True, null=True)
    g392 = models.CharField(max_length=70, blank=True, null=True)
    g41a = models.CharField(max_length=3, blank=True, null=True)
    g42 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    g42g221 = models.CharField(max_length=3, blank=True, null=True)
    g42g23 = models.DecimalField(default=0.00, max_digits=10, decimal_places=4, blank=True, null=True)
    g43 = models.CharField(max_length=1, blank=True, null=True)
    g430 = models.CharField(max_length=2, blank=True, null=True)
    g45 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    g451 = models.CharField(max_length=2, blank=True, null=True)
    g452 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    g45a1 = models.CharField(max_length=1, blank=True, null=True)
    g45a2 = models.CharField(max_length=1, blank=True, null=True)
    g45a3 = models.CharField(max_length=1, blank=True, null=True)
    g45a4 = models.CharField(max_length=1, blank=True, null=True)
    g45a5 = models.CharField(max_length=1, blank=True, null=True)
    g45a6 = models.CharField(max_length=1, blank=True, null=True)
    g45a7 = models.CharField(max_length=1, blank=True, null=True)
    g45a8 = models.CharField(max_length=1, blank=True, null=True)
    g46 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    g46k = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    g461 = models.CharField(max_length=1, blank=True, null=True)
    k470 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    invcountr = models.CharField(max_length=2, blank=True, null=True)
    invseqid = models.CharField(max_length=4, blank=True, null=True)
    invyear = models.CharField(max_length=4, blank=True, null=True)
    invkind = models.CharField(max_length=1, blank=True, null=True)
    invgoodid = models.IntegerField(default=0, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'ktdtovar'


class Ktdtovg(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    num_pp = models.IntegerField(default=0, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    g32g = models.IntegerField(default=0, blank=True, null=True)
    numrec = models.IntegerField(default=0, blank=True, null=True)
    g31_10 = models.CharField(max_length=4, blank=True, null=True)
    g31_11 = models.CharField(max_length=150, blank=True, null=True)
    g31_12 = models.CharField(max_length=150, blank=True, null=True)
    g31place = models.CharField(max_length=250, blank=True, null=True)
    g31_14 = models.CharField(max_length=50, blank=True, null=True)
    g31_15_mod = models.CharField(max_length=50, blank=True, null=True)
    g31_15 = models.CharField(max_length=50, blank=True, null=True)
    g31_16 = models.CharField(max_length=50, blank=True, null=True)
    compord = models.IntegerField(default=0, blank=True, null=True)
    compnum = models.CharField(max_length=50, blank=True, null=True)
    g31_17 = models.CharField(max_length=50, blank=True, null=True)
    g31_18 = models.CharField(max_length=30, blank=True, null=True)
    g31_19 = models.CharField(max_length=20, blank=True, null=True)
    woodrmin = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    woodrmax = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    woodrcod = models.CharField(max_length=3, blank=True, null=True)
    woodcont = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    woodfact = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    woodfcod = models.CharField(max_length=3, blank=True, null=True)
    g31_20 = models.CharField(max_length=50, blank=True, null=True)
    length = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    clength = models.CharField(max_length=3, blank=True, null=True)
    width = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    cwidth = models.CharField(max_length=3, blank=True, null=True)
    height = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    cheight = models.CharField(max_length=3, blank=True, null=True)
    kolvo = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    code_edi = models.CharField(max_length=3, blank=True, null=True)
    name_edi = models.CharField(max_length=13, blank=True, null=True)
    recordid = models.CharField(max_length=36, blank=True, null=True)
    invoiccost = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    licgrpdoc1 = models.CharField(max_length=50, blank=True, null=True)
    licgrpd1 = models.DateField(blank=True, null=True)
    licrec1 = models.CharField(max_length=36, blank=True, null=True)
    goodnmlic1 = models.IntegerField(default=0, blank=True, null=True)
    licgrpdoc2 = models.CharField(max_length=50, blank=True, null=True)
    licgrpd2 = models.DateField(blank=True, null=True)
    licrec2 = models.CharField(max_length=36, blank=True, null=True)
    goodnmlic2 = models.IntegerField(default=0, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'ktdtovg'


class Ktdtovg2(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    num_pp = models.IntegerField(default=0, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    numpredd = models.IntegerField(default=0, blank=True, null=True)
    g32g = models.IntegerField(default=0, blank=True, null=True)
    numrec = models.IntegerField(default=0, blank=True, null=True)
    g31_10 = models.CharField(max_length=4, blank=True, null=True)
    g31_11 = models.CharField(max_length=150, blank=True, null=True)
    g31_12 = models.CharField(max_length=150, blank=True, null=True)
    g31_14 = models.CharField(max_length=50, blank=True, null=True)
    g31_15_mod = models.CharField(max_length=50, blank=True, null=True)
    g31_15 = models.CharField(max_length=50, blank=True, null=True)
    g31_16 = models.CharField(max_length=50, blank=True, null=True)
    g31_17 = models.CharField(max_length=50, blank=True, null=True)
    g31_18 = models.CharField(max_length=30, blank=True, null=True)
    g31_19 = models.CharField(max_length=20, blank=True, null=True)
    g31_20 = models.CharField(max_length=50, blank=True, null=True)
    kolvo = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    code_edi = models.CharField(max_length=3, blank=True, null=True)
    name_edi = models.CharField(max_length=13, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'ktdtovg2'


class Ktdtovs(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    num_pp = models.IntegerField(default=0, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    g32g = models.IntegerField(default=0, blank=True, null=True)
    numrec = models.IntegerField(default=0, blank=True, null=True)
    g31_15_sn = models.CharField(max_length=50, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'ktdtovs'


class Ktdtovs2(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    num_pp = models.IntegerField(default=0, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    numpredd = models.IntegerField(default=0, blank=True, null=True)
    g32g = models.IntegerField(default=0, blank=True, null=True)
    numrec = models.IntegerField(default=0, blank=True, null=True)
    g31_15_sn = models.CharField(max_length=50, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'ktdtovs2'


class Ktdtrans(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    num_pp = models.IntegerField(default=0, blank=True, null=True)
    ngr = models.CharField(max_length=2, blank=True, null=True)
    numrec = models.IntegerField(default=0, blank=True, null=True)
    vidtrans = models.CharField(max_length=2, blank=True, null=True)
    tipts3 = models.CharField(max_length=3, blank=True, null=True)
    mthtrans = models.CharField(max_length=1, blank=True, null=True)
    nametrans = models.CharField(max_length=100, blank=True, null=True)
    ntrans = models.CharField(max_length=40, blank=True, null=True)
    movetrans = models.CharField(max_length=1, blank=True, null=True)
    ntrans1 = models.CharField(max_length=40, blank=True, null=True)
    ntrans2 = models.CharField(max_length=40, blank=True, null=True)
    activeid = models.CharField(max_length=40, blank=True, null=True)
    g19 = models.CharField(max_length=1, blank=True, null=True)
    st_control = models.CharField(max_length=250, blank=True, null=True)
    g212 = models.CharField(max_length=2, blank=True, null=True)
    g29 = models.CharField(max_length=8, blank=True, null=True)
    g291 = models.CharField(max_length=3, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'ktdtrans'


class Ktduslt(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    num_pp = models.IntegerField(default=0, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    typeinfo = models.CharField(max_length=1, blank=True, null=True)
    gu01 = models.IntegerField(default=0, blank=True, null=True)
    gu02 = models.IntegerField(default=0, blank=True, null=True)
    gu03 = models.CharField(max_length=2, blank=True, null=True)
    gunpp = models.IntegerField(default=0, blank=True, null=True)
    gu1 = models.CharField(max_length=50, blank=True, null=True)
    gu1d = models.DateField(blank=True, null=True)
    gu2 = models.CharField(max_length=250, blank=True, null=True)
    gu3 = models.DateField(blank=True, null=True)
    gudd = models.DateField(blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'ktduslt'


class Oupavtmb(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    k32 = models.IntegerField(default=0, blank=True, null=True)
    nud = models.CharField(max_length=12, blank=True, null=True)
    kodmrk = models.CharField(max_length=3, blank=True, null=True)
    namemrkcar = models.CharField(max_length=20, blank=True, null=True)
    model = models.CharField(max_length=36, blank=True, null=True)
    year = models.IntegerField(default=0, blank=True, null=True)
    price = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    obem = models.IntegerField(default=0, blank=True, null=True)
    id = models.CharField(max_length=20, blank=True, null=True)
    nkuz = models.CharField(max_length=40, blank=True, null=True)
    kabina = models.CharField(max_length=40, blank=True, null=True)
    nsh = models.CharField(max_length=40, blank=True, null=True)
    ndv = models.CharField(max_length=40, blank=True, null=True)
    prim = models.DecimalField(default=0.00, max_digits=6, decimal_places=2, blank=True, null=True)
    probeg = models.IntegerField(default=0, blank=True, null=True)
    probeged = models.CharField(max_length=3, blank=True, null=True)
    nblktc1 = models.CharField(max_length=8, blank=True, null=True)
    nblktc1p = models.CharField(max_length=8, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'oupavtmb'


class Oupdinfo(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    k32 = models.IntegerField(default=0, blank=True, null=True)
    ngr = models.CharField(max_length=2, blank=True, null=True)
    typ_ngr = models.CharField(max_length=2, blank=True, null=True)
    k32g = models.IntegerField(default=0, blank=True, null=True)
    numrec = models.IntegerField(default=0, blank=True, null=True)
    text1 = models.CharField(max_length=250, blank=True, null=True)
    ind_text = models.CharField(max_length=3, blank=True, null=True)
    text2 = models.CharField(max_length=50, blank=True, null=True)
    typ_izm = models.CharField(max_length=1, blank=True, null=True)
    kolvo = models.DecimalField(default=0.00, max_digits=16, decimal_places=4, blank=True, null=True)
    code_edi = models.CharField(max_length=3, blank=True, null=True)
    name_edi = models.CharField(max_length=17, blank=True, null=True)
    nblktc1 = models.CharField(max_length=8, blank=True, null=True)
    nblktc1p = models.CharField(max_length=8, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'oupdinfo'


class Oupdokiz(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    k32 = models.IntegerField(default=0, blank=True, null=True)
    k4401 = models.IntegerField(default=0, blank=True, null=True)
    k4402 = models.IntegerField(default=0, blank=True, null=True)
    k44020 = models.CharField(max_length=1, blank=True, null=True)
    k44_cust = models.CharField(max_length=8, blank=True, null=True)
    k440 = models.CharField(max_length=4, blank=True, null=True)
    k441 = models.CharField(max_length=5, blank=True, null=True)
    k441a = models.CharField(max_length=2, blank=True, null=True)
    k442 = models.CharField(max_length=50, blank=True, null=True)
    k442r = models.CharField(max_length=28, blank=True, null=True)
    k442simp = models.CharField(max_length=1, blank=True, null=True)
    k44mdp1 = models.IntegerField(default=0, blank=True, null=True)
    k44mdp2 = models.CharField(max_length=18, blank=True, null=True)
    k443 = models.DateField(blank=True, null=True)
    k444 = models.CharField(max_length=250, blank=True, null=True)
    k445 = models.CharField(max_length=150, blank=True, null=True)
    k446 = models.DateField(blank=True, null=True)
    k447 = models.DateField(blank=True, null=True)
    k4480et = models.CharField(max_length=10, blank=True, null=True)
    k4481et = models.DateField(blank=True, null=True)
    k44stper = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    k44sfcntry = models.CharField(max_length=2, blank=True, null=True)
    k44alldoc = models.IntegerField(default=0, blank=True, null=True)
    k4491 = models.DateField(blank=True, null=True)
    k4492 = models.DateField(blank=True, null=True)
    k4493 = models.CharField(max_length=2, blank=True, null=True)
    k44dd = models.DateField(blank=True, null=True)
    nblktc1 = models.CharField(max_length=8, blank=True, null=True)
    nblktc1p = models.CharField(max_length=8, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'oupdokiz'


class Ouphead(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    k032 = models.IntegerField(default=0, blank=True, null=True)
    k05 = models.IntegerField(default=0, blank=True, null=True)
    k121 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    k122 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    k12k = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    k202 = models.CharField(max_length=3, blank=True, null=True)
    k2021 = models.CharField(max_length=40, blank=True, null=True)
    k203 = models.CharField(max_length=250, blank=True, null=True)
    k221 = models.CharField(max_length=3, blank=True, null=True)
    k221c = models.CharField(max_length=3, blank=True, null=True)
    k222 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    k222k = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    k23 = models.DecimalField(default=0.00, max_digits=10, decimal_places=4, blank=True, null=True)
    k230 = models.DateField(blank=True, null=True)
    k54_itn = models.CharField(max_length=13, blank=True, null=True)
    k5410 = models.CharField(max_length=1, blank=True, null=True)
    k541 = models.CharField(max_length=14, blank=True, null=True)
    k541d = models.DateField(blank=True, null=True)
    k5411 = models.CharField(max_length=50, blank=True, null=True)
    k5411d = models.DateField(blank=True, null=True)
    k541_inn = models.CharField(max_length=12, blank=True, null=True)
    k541_kpp = models.CharField(max_length=9, blank=True, null=True)
    k542 = models.DateField(blank=True, null=True)
    k543 = models.CharField(max_length=4, blank=True, null=True)
    k5441 = models.CharField(max_length=150, blank=True, null=True)
    k5441nm = models.CharField(max_length=150, blank=True, null=True)
    k5441mdnm = models.CharField(max_length=150, blank=True, null=True)
    k5442 = models.CharField(max_length=50, blank=True, null=True)
    k5443 = models.CharField(max_length=250, blank=True, null=True)
    k5444 = models.CharField(max_length=50, blank=True, null=True)
    k5445 = models.DateField(blank=True, null=True)
    k5446 = models.DateField(blank=True, null=True)
    k5447 = models.CharField(max_length=50, blank=True, null=True)
    k5451 = models.CharField(max_length=7, blank=True, null=True)
    k5451a = models.CharField(max_length=25, blank=True, null=True)
    k54521 = models.CharField(max_length=11, blank=True, null=True)
    k54522 = models.CharField(max_length=25, blank=True, null=True)
    k54523 = models.CharField(max_length=150, blank=True, null=True)
    k5453 = models.DateField(blank=True, null=True)
    kb0 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    ka = models.DateField(blank=True, null=True)
    kc30 = models.CharField(max_length=2, blank=True, null=True)
    nblktc1 = models.CharField(max_length=8, blank=True, null=True)
    nblktc1p = models.CharField(max_length=8, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)
    ed_idid = models.CharField(max_length=36, blank=True, null=True)
    idou = models.CharField(max_length=36, blank=True, null=True)
    active = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'ouphead'


class Ouppk(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    k32 = models.IntegerField(default=0, blank=True, null=True)
    pksign = models.CharField(max_length=1, blank=True, null=True)
    pkvid = models.CharField(max_length=2, blank=True, null=True)
    pkkolvo = models.IntegerField(default=0, blank=True, null=True)
    pkinf = models.CharField(max_length=150, blank=True, null=True)
    nblktc1 = models.CharField(max_length=8, blank=True, null=True)
    nblktc1p = models.CharField(max_length=8, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'ouppk'


class Oupplbiz(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    kb0 = models.CharField(max_length=1, blank=True, null=True)
    kb1 = models.CharField(max_length=4, blank=True, null=True)
    kb2 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    kb3 = models.CharField(max_length=3, blank=True, null=True)
    kb6 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    kb61 = models.CharField(max_length=3, blank=True, null=True)
    kb7 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    nblktc1 = models.CharField(max_length=8, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'oupplbiz'


class Ouppltiz(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    k32 = models.IntegerField(default=0, blank=True, null=True)
    k470 = models.CharField(max_length=1, blank=True, null=True)
    k471 = models.CharField(max_length=4, blank=True, null=True)
    k471npp = models.IntegerField(default=0, blank=True, null=True)
    k472 = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    k4721 = models.CharField(max_length=3, blank=True, null=True)
    k4723 = models.CharField(max_length=3, blank=True, null=True)
    k473 = models.DecimalField(default=0.00, max_digits=11, decimal_places=5, blank=True, null=True)
    k4731 = models.CharField(max_length=1, blank=True, null=True)
    k4732 = models.CharField(max_length=3, blank=True, null=True)
    k4733 = models.CharField(max_length=3, blank=True, null=True)
    k4734 = models.DecimalField(default=0.00, max_digits=8, decimal_places=3, blank=True, null=True)
    kpp = models.IntegerField(default=0, blank=True, null=True)
    k474 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    k4741 = models.CharField(max_length=3, blank=True, null=True)
    k475 = models.CharField(max_length=2, blank=True, null=True)
    k476 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    k4761 = models.CharField(max_length=3, blank=True, null=True)
    k473z1_2 = models.CharField(max_length=1, blank=True, null=True)
    k473_2 = models.DecimalField(default=0.00, max_digits=11, decimal_places=5, blank=True, null=True)
    k4731_2 = models.CharField(max_length=1, blank=True, null=True)
    k4732_2 = models.CharField(max_length=3, blank=True, null=True)
    k4733_2 = models.CharField(max_length=3, blank=True, null=True)
    k4734_2 = models.DecimalField(default=0.00, max_digits=8, decimal_places=3, blank=True, null=True)
    k473z1_3 = models.CharField(max_length=1, blank=True, null=True)
    k473_3 = models.DecimalField(default=0.00, max_digits=11, decimal_places=5, blank=True, null=True)
    k4731_3 = models.CharField(max_length=1, blank=True, null=True)
    k4732_3 = models.CharField(max_length=3, blank=True, null=True)
    k4733_3 = models.CharField(max_length=3, blank=True, null=True)
    k4734_3 = models.DecimalField(default=0.00, max_digits=8, decimal_places=3, blank=True, null=True)
    k473z2_2 = models.IntegerField(default=0, blank=True, null=True)
    k477 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    iret = models.IntegerField(default=0, blank=True, null=True)
    k4730 = models.DateField(blank=True, null=True)
    k4740 = models.DateField(blank=True, null=True)
    k47_nd = models.IntegerField(default=0, blank=True, null=True)
    k47_ns = models.IntegerField(default=0, blank=True, null=True)
    k47_nm = models.IntegerField(default=0, blank=True, null=True)
    k47_tr = models.DecimalField(default=0.00, max_digits=3, decimal_places=2, blank=True, null=True)
    k47_desc = models.CharField(max_length=250, blank=True, null=True)
    nblktc1 = models.CharField(max_length=8, blank=True, null=True)
    nblktc1p = models.CharField(max_length=8, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'ouppltiz'


class Oupslotm(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    kc_01 = models.CharField(max_length=1, blank=True, null=True)
    kc_02 = models.CharField(max_length=2, blank=True, null=True)
    nrecc = models.IntegerField(default=0, blank=True, null=True)
    kc_1 = models.CharField(max_length=150, blank=True, null=True)
    kc_10 = models.CharField(max_length=2, blank=True, null=True)
    kc_11 = models.CharField(max_length=50, blank=True, null=True)
    kc_11d = models.DateField(blank=True, null=True)
    kc_2 = models.DateField(blank=True, null=True)
    kc_21 = models.CharField(max_length=8, blank=True, null=True)
    kc_6 = models.CharField(max_length=4, blank=True, null=True)
    kc_7 = models.CharField(max_length=40, blank=True, null=True)
    nblktc1 = models.CharField(max_length=8, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'oupslotm'


class Oupsltov(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    k32 = models.IntegerField(default=0, blank=True, null=True)
    nrecc = models.IntegerField(default=0, blank=True, null=True)
    kc_02 = models.CharField(max_length=2, blank=True, null=True)
    kc_1 = models.CharField(max_length=150, blank=True, null=True)
    kc_10 = models.CharField(max_length=2, blank=True, null=True)
    kc_11 = models.CharField(max_length=50, blank=True, null=True)
    kc_11d = models.DateField(blank=True, null=True)
    kc_2 = models.DateField(blank=True, null=True)
    kc_21 = models.CharField(max_length=8, blank=True, null=True)
    kc_6 = models.CharField(max_length=4, blank=True, null=True)
    kc_7 = models.CharField(max_length=40, blank=True, null=True)
    nblktc1 = models.CharField(max_length=8, blank=True, null=True)
    nblktc1p = models.CharField(max_length=8, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'oupsltov'


class Oupsumpp(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    k32 = models.IntegerField(default=0, blank=True, null=True)
    k471 = models.CharField(max_length=4, blank=True, null=True)
    k471npp = models.IntegerField(default=0, blank=True, null=True)
    k4741 = models.CharField(max_length=3, blank=True, null=True)
    k475 = models.CharField(max_length=2, blank=True, null=True)
    iret = models.IntegerField(default=0, blank=True, null=True)
    numpdok = models.CharField(max_length=50, blank=True, null=True)
    datpdok = models.DateField(blank=True, null=True)
    sum_all = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    sumpdok = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    valpdok = models.CharField(max_length=3, blank=True, null=True)
    datpostd = models.DateField(blank=True, null=True)
    datpaymt = models.DateField(blank=True, null=True)
    innplat = models.CharField(max_length=12, blank=True, null=True)
    kppplat = models.CharField(max_length=9, blank=True, null=True)
    lnpins = models.CharField(max_length=4, blank=True, null=True)
    fioins = models.CharField(max_length=40, blank=True, null=True)
    datins = models.DateField(blank=True, null=True)
    timins = models.CharField(max_length=8, blank=True, null=True)
    nblktc1 = models.CharField(max_length=8, blank=True, null=True)
    nblktc1p = models.CharField(max_length=8, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'oupsumpp'


class Oupterms(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    k32 = models.IntegerField(default=0, blank=True, null=True)
    terms = models.CharField(max_length=3, blank=True, null=True)
    termspoint = models.CharField(max_length=50, blank=True, null=True)
    termspass = models.CharField(max_length=250, blank=True, null=True)
    nblktc1 = models.CharField(max_length=8, blank=True, null=True)
    nblktc1p = models.CharField(max_length=8, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'oupterms'


class Ouptovg(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    k32 = models.IntegerField(default=0, blank=True, null=True)
    k32g = models.IntegerField(default=0, blank=True, null=True)
    numrec = models.IntegerField(default=0, blank=True, null=True)
    k31_10 = models.CharField(max_length=4, blank=True, null=True)
    k31_11 = models.CharField(max_length=150, blank=True, null=True)
    k31_12 = models.CharField(max_length=150, blank=True, null=True)
    k31_14 = models.CharField(max_length=50, blank=True, null=True)
    k31_15_mod = models.CharField(max_length=50, blank=True, null=True)
    k31_15 = models.CharField(max_length=50, blank=True, null=True)
    k31_16 = models.CharField(max_length=50, blank=True, null=True)
    compord = models.IntegerField(default=0, blank=True, null=True)
    compnum = models.CharField(max_length=50, blank=True, null=True)
    k31_17 = models.CharField(max_length=50, blank=True, null=True)
    k31_18 = models.CharField(max_length=30, blank=True, null=True)
    k31_19 = models.CharField(max_length=20, blank=True, null=True)
    k31_20 = models.CharField(max_length=50, blank=True, null=True)
    kolvo = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    code_edi = models.CharField(max_length=3, blank=True, null=True)
    name_edi = models.CharField(max_length=13, blank=True, null=True)
    nblktc1 = models.CharField(max_length=8, blank=True, null=True)
    nblktc1p = models.CharField(max_length=8, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'ouptovg'


class Ouptoviz(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    typ_ktc = models.IntegerField(default=0, blank=True, null=True)
    k011 = models.CharField(max_length=1, blank=True, null=True)
    k012 = models.CharField(max_length=4, blank=True, null=True)
    k013 = models.CharField(max_length=1, blank=True, null=True)
    k031 = models.IntegerField(default=0, blank=True, null=True)
    ch = models.IntegerField(default=0, blank=True, null=True)
    k31_1 = models.CharField(max_length=250, blank=True, null=True)
    k31_1_prdt = models.DateField(blank=True, null=True)
    k31_1_oilf = models.CharField(max_length=250, blank=True, null=True)
    k31_2 = models.IntegerField(default=0, blank=True, null=True)
    k31_2part = models.IntegerField(default=0, blank=True, null=True)
    k31_20 = models.CharField(max_length=1, blank=True, null=True)
    k31_7 = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    k31_71 = models.CharField(max_length=13, blank=True, null=True)
    k31_8 = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    k31_81 = models.CharField(max_length=13, blank=True, null=True)
    k31_82 = models.CharField(max_length=3, blank=True, null=True)
    k31_9 = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    k31_91 = models.CharField(max_length=13, blank=True, null=True)
    k31_92 = models.CharField(max_length=3, blank=True, null=True)
    k31_fact = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    k32 = models.IntegerField(default=0, blank=True, null=True)
    k33 = models.CharField(max_length=10, blank=True, null=True)
    k333 = models.CharField(max_length=4, blank=True, null=True)
    k34 = models.CharField(max_length=2, blank=True, null=True)
    k35 = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    k35k = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    k36 = models.CharField(max_length=7, blank=True, null=True)
    k38 = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    k38_1 = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    k38k = models.DecimalField(default=0.00, max_digits=18, decimal_places=6, blank=True, null=True)
    k41a = models.CharField(max_length=3, blank=True, null=True)
    k42 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    k42g221 = models.CharField(max_length=3, blank=True, null=True)
    k42g23 = models.DecimalField(default=0.00, max_digits=10, decimal_places=4, blank=True, null=True)
    k43 = models.CharField(max_length=2, blank=True, null=True)
    k451 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    k452 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    k46 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    k461 = models.CharField(max_length=1, blank=True, null=True)
    k46k = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    k45_price = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    k45_pval = models.CharField(max_length=3, blank=True, null=True)
    k45_ped = models.CharField(max_length=3, blank=True, null=True)
    k45_pist = models.CharField(max_length=250, blank=True, null=True)
    k47_tobcs1 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    k47_tobcs2 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    k470 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    k4701 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    ou_code = models.CharField(max_length=6, blank=True, null=True)
    cccd1 = models.CharField(max_length=1, blank=True, null=True)
    cccd2 = models.CharField(max_length=1, blank=True, null=True)
    cccd3 = models.CharField(max_length=1, blank=True, null=True)
    cccd4 = models.CharField(max_length=1, blank=True, null=True)
    cccd5 = models.CharField(max_length=1, blank=True, null=True)
    cccd6 = models.CharField(max_length=1, blank=True, null=True)
    nblktc1 = models.CharField(max_length=8, blank=True, null=True)
    nblktc2 = models.CharField(max_length=8, blank=True, null=True)
    nblktc1p = models.CharField(max_length=8, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'ouptoviz'


class Ouptovs(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    k32 = models.IntegerField(default=0, blank=True, null=True)
    k32g = models.IntegerField(default=0, blank=True, null=True)
    numrec = models.IntegerField(default=0, blank=True, null=True)
    k31_15_sn = models.CharField(max_length=50, blank=True, null=True)
    nblktc1 = models.CharField(max_length=8, blank=True, null=True)
    nblktc1p = models.CharField(max_length=8, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'ouptovs'


class Proterr(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    marked = models.CharField(max_length=1, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    rec = models.IntegerField(default=0, blank=True, null=True)
    recdob = models.IntegerField(default=0, blank=True, null=True)
    kod = models.CharField(max_length=40, blank=True, null=True)
    tovar = models.IntegerField(default=0, blank=True, null=True)
    field = models.CharField(max_length=10, blank=True, null=True)
    grafa = models.CharField(max_length=9, blank=True, null=True)
    dclrntid = models.CharField(max_length=15, blank=True, null=True)
    verno = models.CharField(max_length=255, blank=True, null=True)
    rejim = models.CharField(max_length=2, blank=True, null=True)
    tip = models.CharField(max_length=2, blank=True, null=True)
    dtip = models.CharField(max_length=3, blank=True, null=True)
    stroka = models.IntegerField(default=0, blank=True, null=True)
    err_code = models.CharField(max_length=10, blank=True, null=True)
    err_level = models.IntegerField(default=0, blank=True, null=True)
    ktr = models.CharField(max_length=1, blank=True, null=True)
    ind = models.IntegerField(default=0, blank=True, null=True)
    lnpech = models.CharField(max_length=59, blank=True, null=True)
    msg_id = models.CharField(max_length=10, blank=True, null=True)
    alias = models.CharField(max_length=10, blank=True, null=True)
    errstep = models.CharField(max_length=10, blank=True, null=True)
    args = models.CharField(max_length=70, blank=True, null=True)
    recno = models.IntegerField(default=0, blank=True, null=True)
    noborot = models.IntegerField(default=0, blank=True, null=True)
    npp = models.CharField(max_length=5, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    code = models.IntegerField(default=0, blank=True, null=True)
    nprik = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'proterr'


class Protprim(BaseModel):
    plat = models.IntegerField(default=0, blank=True, null=True)
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    ntov = models.IntegerField(default=0, blank=True, null=True)
    txt = models.CharField(max_length=100, blank=True, null=True)
    exclus = models.CharField(max_length=1, blank=True, null=True)
    txt1 = models.CharField(max_length=80, blank=True, null=True)
    fld = models.CharField(max_length=30, blank=True, null=True)
    fldcont = models.CharField(max_length=80, blank=True, null=True)
    txt2 = models.CharField(max_length=150, blank=True, null=True)
    docname = models.CharField(max_length=52, blank=True, null=True)
    docprim = models.CharField(max_length=50, blank=True, null=True)
    continued = models.BooleanField(blank=True, null=True)
    code = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'protprim'


class PzkErr(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    npp = models.CharField(max_length=5, blank=True, null=True)
    g32 = models.IntegerField(default=0, blank=True, null=True)
    name_tbl = models.CharField(max_length=32, blank=True, null=True)
    name_attr = models.CharField(max_length=32, blank=True, null=True)
    nzp = models.IntegerField(default=0, blank=True, null=True)
    kod_err = models.CharField(max_length=16, blank=True, null=True)
    ur_err = models.CharField(max_length=1, blank=True, null=True)
    text_err = models.CharField(max_length=125, blank=True, null=True)
    desc_err = models.CharField(max_length=250, blank=True, null=True)
    true_val = models.CharField(max_length=250, blank=True, null=True)
    ref_typd = models.CharField(max_length=30, blank=True, null=True)
    ref_dptd = models.CharField(max_length=150, blank=True, null=True)
    ref_datd = models.DateField(blank=True, null=True)
    ref_numd = models.CharField(max_length=50, blank=True, null=True)
    ref_dbgd = models.DateField(blank=True, null=True)
    ref_dndd = models.DateField(blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'pzk_err'


class PzkHead(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    type_td = models.CharField(max_length=2, blank=True, null=True)
    id_ps_chck = models.CharField(max_length=80, blank=True, null=True)
    v_ps_chck = models.CharField(max_length=10, blank=True, null=True)
    data_chck = models.DateField(blank=True, null=True)
    time_chck = models.CharField(max_length=8, blank=True, null=True)
    ver_armti = models.CharField(max_length=10, blank=True, null=True)
    c_err = models.IntegerField(default=0, blank=True, null=True)
    kod_rsnrtn = models.CharField(max_length=2, blank=True, null=True)
    primexprsn = models.CharField(max_length=250, blank=True, null=True)
    dataexprsn = models.DateField(blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'pzk_head'


class PzkRsn(BaseModel):
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    npp_err = models.CharField(max_length=5, blank=True, null=True)
    npp_rsn = models.CharField(max_length=3, blank=True, null=True)
    kod_rsn = models.CharField(max_length=3, blank=True, null=True)
    prim_insp = models.CharField(max_length=250, blank=True, null=True)
    ref_typd = models.CharField(max_length=30, blank=True, null=True)
    ref_dptd = models.CharField(max_length=150, blank=True, null=True)
    ref_numd = models.CharField(max_length=50, blank=True, null=True)
    ref_datd = models.DateField(blank=True, null=True)
    lnp_insp = models.CharField(max_length=4, blank=True, null=True)
    data_clsd = models.DateField(blank=True, null=True)
    p_edoc_id = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        abstract = True
        # managed = False
        # db_table = 'pzk_rsn'
