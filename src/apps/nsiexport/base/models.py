from django.db import models
from src.apps.common.dataclasses import ETL

class BaseModel(models.Model):
    """Base import model"""
    type = ETL.EXPORT.NSI

    class Meta:
        abstract = True

class AddDoc(BaseModel):
    checkpoint = models.CharField(max_length=6, blank=True, null=True)
    doc_id = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'add_doc'


class Address(BaseModel):
    subject_id = models.DecimalField(default=0.00, max_digits=18, decimal_places=9, blank=True, null=True)
    address1 = models.CharField(max_length=254, blank=True, null=True)
    address2 = models.CharField(max_length=254, blank=True, null=True)
    address3 = models.CharField(max_length=254, blank=True, null=True)
    address4 = models.CharField(max_length=254, blank=True, null=True)
    address5 = models.CharField(max_length=254, blank=True, null=True)
    address6 = models.CharField(max_length=254, blank=True, null=True)
    address7 = models.CharField(max_length=254, blank=True, null=True)
    address8 = models.CharField(max_length=222, blank=True, null=True)
    type = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'address'


class AdpPrim(BaseModel):
    kodt = models.CharField(max_length=10, blank=True, null=True)
    naim = models.CharField(max_length=150, blank=True, null=True)
    st_min = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, blank=True, null=True)
    simvmin = models.CharField(max_length=1, blank=True, null=True)
    edimin = models.CharField(max_length=3, blank=True, null=True)
    oper = models.CharField(max_length=1, blank=True, null=True)
    st_max = models.DecimalField(default=0.00, max_digits=10, decimal_places=3, blank=True, null=True)
    simvmax = models.CharField(max_length=1, blank=True, null=True)
    edimax = models.CharField(max_length=3, blank=True, null=True)
    algvzim = models.CharField(max_length=3, blank=True, null=True)
    zalgvzim = models.CharField(max_length=20, blank=True, null=True)
    falgvzim = models.CharField(max_length=10, blank=True, null=True)
    algusl = models.CharField(max_length=3, blank=True, null=True)
    zalgusl = models.CharField(max_length=20, blank=True, null=True)
    falgusl = models.CharField(max_length=10, blank=True, null=True)
    npric = models.CharField(max_length=20, blank=True, null=True)
    dpric = models.DateField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    data1 = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'adp_prim'


class AkcPrim(BaseModel):
    st = models.CharField(max_length=2, blank=True, null=True)
    kodt = models.CharField(max_length=10, blank=True, null=True)
    naim = models.TextField(blank=True, null=True)
    st_akc = models.DecimalField(default=0.00, max_digits=15, decimal_places=6, blank=True, null=True)
    simv1 = models.CharField(max_length=3, blank=True, null=True)
    edi1 = models.CharField(max_length=3, blank=True, null=True)
    koefedi1 = models.DecimalField(default=0.00, max_digits=9, decimal_places=3, blank=True, null=True)
    operd = models.CharField(max_length=1, blank=True, null=True)
    st_akcd = models.DecimalField(default=0.00, max_digits=15, decimal_places=6, blank=True, null=True)
    simvd = models.CharField(max_length=3, blank=True, null=True)
    edid = models.CharField(max_length=3, blank=True, null=True)
    koefedid = models.DecimalField(default=0.00, max_digits=9, decimal_places=3, blank=True, null=True)
    oper = models.CharField(max_length=1, blank=True, null=True)
    st_akc2 = models.DecimalField(default=0.00, max_digits=15, decimal_places=6, blank=True, null=True)
    simv2 = models.CharField(max_length=3, blank=True, null=True)
    edi2 = models.CharField(max_length=3, blank=True, null=True)
    koefedi2 = models.DecimalField(default=0.00, max_digits=9, decimal_places=3, blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    data1 = models.DateField(blank=True, null=True)
    npric = models.CharField(max_length=20, blank=True, null=True)
    dpric = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'akc_prim'


class AllIncl(BaseModel):
    inclusioni = models.CharField(max_length=2, blank=True, null=True)
    inclusionn = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'all_incl'


class AllOper(BaseModel):
    operationi = models.CharField(max_length=2, blank=True, null=True)
    operationn = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'all_oper'


class ArxReg(BaseModel):
    adress = models.CharField(max_length=150, blank=True, null=True)
    telefon = models.CharField(max_length=12, blank=True, null=True)
    telegraf = models.CharField(max_length=50, blank=True, null=True)
    telefax = models.CharField(max_length=12, blank=True, null=True)
    telex = models.CharField(max_length=20, blank=True, null=True)
    zayv = models.CharField(max_length=80, blank=True, null=True)
    nomr1 = models.CharField(max_length=2, blank=True, null=True)
    nomr2 = models.CharField(max_length=4, blank=True, null=True)
    nomr3 = models.CharField(max_length=10, blank=True, null=True)
    psu = models.CharField(max_length=1, blank=True, null=True)
    okato = models.CharField(max_length=11, blank=True, null=True)
    okpobr = models.CharField(max_length=10, blank=True, null=True)
    schet1 = models.CharField(max_length=20, blank=True, null=True)
    korschr = models.CharField(max_length=20, blank=True, null=True)
    okpobv = models.CharField(max_length=10, blank=True, null=True)
    schet2 = models.CharField(max_length=20, blank=True, null=True)
    korschv = models.CharField(max_length=20, blank=True, null=True)
    kodtam = models.CharField(max_length=8, blank=True, null=True)
    datr = models.DateField(blank=True, null=True)
    ogrn = models.CharField(max_length=15, blank=True, null=True)
    inn = models.CharField(max_length=12, blank=True, null=True)
    kpp = models.CharField(max_length=9, blank=True, null=True)
    datn = models.DateField(blank=True, null=True)
    datm = models.DateField(blank=True, null=True)
    alfa2 = models.CharField(max_length=2, blank=True, null=True)
    post9 = models.CharField(max_length=9, blank=True, null=True)
    subcntry = models.CharField(max_length=35, blank=True, null=True)
    city = models.CharField(max_length=35, blank=True, null=True)
    street = models.CharField(max_length=35, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'arx_reg'


class AtdPos(BaseModel):
    code = models.CharField(max_length=4, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'atd_pos'


class Autonz(BaseModel):
    reg_number = models.CharField(max_length=26, blank=True, null=True)
    n_trailer = models.CharField(max_length=17, blank=True, null=True)
    n_trailr2 = models.CharField(max_length=17, blank=True, null=True)
    drivername = models.CharField(max_length=40, blank=True, null=True)
    drpassport = models.CharField(max_length=26, blank=True, null=True)
    ncertif = models.CharField(max_length=12, blank=True, null=True)
    dcertif = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'autonz'


class BankIzm(BaseModel):
    kod_izm = models.CharField(max_length=2, blank=True, null=True)
    name_izm = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'bank_izm'


class Banklist(BaseModel):
    num = models.DecimalField(default=0.00, max_digits=2, decimal_places=0, blank=True, null=True)
    status = models.CharField(max_length=4, blank=True, null=True)
    tip = models.CharField(max_length=1, blank=True, null=True)
    namemax = models.CharField(max_length=250, blank=True, null=True)
    name = models.CharField(max_length=60, blank=True, null=True)
    regn = models.DecimalField(default=0.00, max_digits=4, decimal_places=0, blank=True, null=True)
    rnfl = models.DecimalField(default=0.00, max_digits=4, decimal_places=0, blank=True, null=True)
    lic_rub = models.DateField(blank=True, null=True)
    lic_val = models.DateField(blank=True, null=True)
    vv = models.CharField(max_length=1, blank=True, null=True)
    rei = models.CharField(max_length=1, blank=True, null=True)
    opp = models.CharField(max_length=1, blank=True, null=True)
    ko = models.CharField(max_length=1, blank=True, null=True)
    no = models.CharField(max_length=1, blank=True, null=True)
    adres = models.CharField(max_length=200, blank=True, null=True)
    kors = models.CharField(max_length=20, blank=True, null=True)
    kod = models.CharField(max_length=7, blank=True, null=True)
    okato = models.CharField(max_length=11, blank=True, null=True)
    telefon = models.CharField(max_length=250, blank=True, null=True)
    fax = models.CharField(max_length=100, blank=True, null=True)
    telex = models.CharField(max_length=28, blank=True, null=True)
    teletap = models.CharField(max_length=24, blank=True, null=True)
    fio_pr_pr = models.CharField(max_length=50, blank=True, null=True)
    fio_gl_b = models.CharField(max_length=50, blank=True, null=True)
    okpo = models.CharField(max_length=10, blank=True, null=True)
    okpo_gb = models.CharField(max_length=10, blank=True, null=True)
    time = models.DateField(blank=True, null=True)
    sovam = models.CharField(max_length=8, blank=True, null=True)
    packet = models.CharField(max_length=4, blank=True, null=True)
    type_co = models.CharField(max_length=1, blank=True, null=True)
    mfo = models.CharField(max_length=8, blank=True, null=True)
    uch = models.CharField(max_length=2, blank=True, null=True)
    kod_izm = models.CharField(max_length=2, blank=True, null=True)
    mfon = models.CharField(max_length=9, blank=True, null=True)
    sovam_i = models.CharField(max_length=8, blank=True, null=True)
    ogrn = models.CharField(max_length=15, blank=True, null=True)
    inn = models.CharField(max_length=12, blank=True, null=True)
    kpp = models.CharField(max_length=9, blank=True, null=True)
    igarant = models.CharField(max_length=1, blank=True, null=True)
    datan = models.DateField(blank=True, null=True)
    datao = models.DateField(blank=True, null=True)
    lic_met = models.DateField(blank=True, null=True)
    uer = models.CharField(max_length=1, blank=True, null=True)
    lic_gold = models.DateField(blank=True, null=True)
    lic_gold1 = models.DateField(blank=True, null=True)
    pric_otz = models.CharField(max_length=20, blank=True, null=True)
    data_fiz = models.DateField(blank=True, null=True)
    kp = models.CharField(max_length=1, blank=True, null=True)
    ust_f = models.DecimalField(default=0.00, max_digits=17, decimal_places=5, blank=True, null=True)
    cp = models.DecimalField(default=0.00, max_digits=2, decimal_places=0, blank=True, null=True)
    cp_f = models.DecimalField(default=0.00, max_digits=2, decimal_places=0, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'banklist'


class BartPc(BaseModel):
    pb_priz_b = models.CharField(max_length=1, blank=True, null=True)
    pb_innu = models.CharField(max_length=10, blank=True, null=True)
    pb_n_dl = models.CharField(max_length=3, blank=True, null=True)
    pb_n_pc = models.CharField(max_length=10, blank=True, null=True)
    pb_d_pc = models.DateField(blank=True, null=True)
    pb_upr = models.CharField(max_length=50, blank=True, null=True)
    pb_adru = models.CharField(max_length=85, blank=True, null=True)
    pb_okpor = models.CharField(max_length=10, blank=True, null=True)
    ogrn = models.CharField(max_length=15, blank=True, null=True)
    pb_innr = models.CharField(max_length=12, blank=True, null=True)
    pb_kpp = models.CharField(max_length=9, blank=True, null=True)
    pb_namer = models.CharField(max_length=120, blank=True, null=True)
    pb_adrr = models.CharField(max_length=85, blank=True, null=True)
    pb_namep = models.CharField(max_length=120, blank=True, null=True)
    pb_kstrp = models.CharField(max_length=3, blank=True, null=True)
    pb_nstrp = models.CharField(max_length=17, blank=True, null=True)
    pb_adrp = models.CharField(max_length=85, blank=True, null=True)
    pb_nkont = models.CharField(max_length=50, blank=True, null=True)
    pb_dkont = models.DateField(blank=True, null=True)
    pb_forma = models.CharField(max_length=2, blank=True, null=True)
    pb_crok = models.CharField(max_length=2, blank=True, null=True)
    pb_d_end = models.DateField(blank=True, null=True)
    pb_kwalk = models.CharField(max_length=3, blank=True, null=True)
    pb_nwalk = models.CharField(max_length=20, blank=True, null=True)
    pb_osumk = models.DecimalField(default=0.00, max_digits=13, decimal_places=3, blank=True, null=True)
    pb_n_liz = models.CharField(max_length=50, blank=True, null=True)
    pb_d_liz = models.DateField(blank=True, null=True)
    pb_k_otcr = models.CharField(max_length=2, blank=True, null=True)
    pb_otcrok = models.CharField(max_length=70, blank=True, null=True)
    pb_priz_v = models.CharField(max_length=1, blank=True, null=True)
    pb_okpob = models.CharField(max_length=10, blank=True, null=True)
    pb_n_dlv = models.CharField(max_length=3, blank=True, null=True)
    pb_n_pcv = models.CharField(max_length=10, blank=True, null=True)
    pb_d_pcv = models.DateField(blank=True, null=True)
    pby1 = models.CharField(max_length=50, blank=True, null=True)
    pby2 = models.CharField(max_length=30, blank=True, null=True)
    pby3 = models.DateField(blank=True, null=True)
    pby4 = models.CharField(max_length=50, blank=True, null=True)
    pby5 = models.CharField(max_length=30, blank=True, null=True)
    pby6 = models.DateField(blank=True, null=True)
    pb_prim = models.CharField(max_length=100, blank=True, null=True)
    pb_exp = models.DecimalField(default=0.00, max_digits=13, decimal_places=3, blank=True, null=True)
    pb_imp = models.DecimalField(default=0.00, max_digits=13, decimal_places=3, blank=True, null=True)
    pbzak = models.CharField(max_length=1, blank=True, null=True)
    pbdzak = models.DateField(blank=True, null=True)
    pdel = models.CharField(max_length=1, blank=True, null=True)
    pbzam = models.CharField(max_length=1, blank=True, null=True)
    pb_b_gtk = models.DateField(blank=True, null=True)
    pb_iz_gtk = models.DateField(blank=True, null=True)
    pb_b_gtkp = models.DateField(blank=True, null=True)
    pb_b_im = models.DateField(blank=True, null=True)
    pb_iz_im = models.DateField(blank=True, null=True)
    pbkor = models.DateField(blank=True, null=True)
    pbnop = models.CharField(max_length=2, blank=True, null=True)
    pbstat = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'bart_pc'


class BgDp(BaseModel):
    n_go = models.CharField(max_length=24, blank=True, null=True)
    type_go = models.CharField(max_length=2, blank=True, null=True)
    reg_date = models.DateField(blank=True, null=True)
    payment = models.DecimalField(default=0.00, max_digits=12, decimal_places=2, blank=True, null=True)
    g501 = models.CharField(max_length=52, blank=True, null=True)
    g502 = models.CharField(max_length=52, blank=True, null=True)
    cntrydrive = models.CharField(max_length=3, blank=True, null=True)
    inn_driver = models.CharField(max_length=20, blank=True, null=True)
    g531 = models.CharField(max_length=8, blank=True, null=True)
    ga3 = models.CharField(max_length=8, blank=True, null=True)
    ga1 = models.CharField(max_length=100, blank=True, null=True)
    standuntil = models.DateField(blank=True, null=True)
    stopdate = models.DateField(blank=True, null=True)
    docno = models.CharField(max_length=19, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'bg_dp'


class Bignalog(BaseModel):
    plt_inn = models.CharField(max_length=12, blank=True, null=True)
    plt_kpp = models.CharField(max_length=9, blank=True, null=True)
    plt_name = models.CharField(max_length=80, blank=True, null=True)
    br_inn = models.CharField(max_length=12, blank=True, null=True)
    br_kpp = models.CharField(max_length=9, blank=True, null=True)
    br_name = models.CharField(max_length=80, blank=True, null=True)
    rasp_no = models.CharField(max_length=20, blank=True, null=True)
    rasp_dat = models.DateField(blank=True, null=True)
    rasp_beg = models.DateField(blank=True, null=True)
    rasp_end = models.DateField(blank=True, null=True)
    sogl_no = models.CharField(max_length=20, blank=True, null=True)
    sogl_dat = models.DateField(blank=True, null=True)
    sogl_beg = models.DateField(blank=True, null=True)
    sogl_end = models.DateField(blank=True, null=True)
    ind_so = models.CharField(max_length=1, blank=True, null=True)
    nump = models.CharField(max_length=20, blank=True, null=True)
    datep = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'bignalog'


class Bignalto(BaseModel):
    plt_inn = models.CharField(max_length=12, blank=True, null=True)
    plt_kpp = models.CharField(max_length=9, blank=True, null=True)
    plt_ogrn = models.CharField(max_length=13, blank=True, null=True)
    plt_name = models.CharField(max_length=80, blank=True, null=True)
    adress = models.CharField(max_length=255, blank=True, null=True)
    kpp_adr = models.CharField(max_length=9, blank=True, null=True)
    okato5 = models.CharField(max_length=5, blank=True, null=True)
    prim = models.CharField(max_length=255, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'bignalto'


class Bkbkn(BaseModel):
    nom = models.DecimalField(default=0.00, max_digits=2, decimal_places=0, blank=True, null=True)
    imn = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'bkbkn'


class Blank(BaseModel):
    numblank = models.CharField(max_length=11, blank=True, null=True)
    p_ts = models.CharField(max_length=1, blank=True, null=True)
    prblank = models.CharField(max_length=1, blank=True, null=True)
    tam = models.CharField(max_length=8, blank=True, null=True)
    dateut = models.DateField(blank=True, null=True)
    datepos = models.DateField(blank=True, null=True)
    p_up = models.CharField(max_length=1, blank=True, null=True)
    res = models.CharField(max_length=11, blank=True, null=True)
    datres = models.DateField(blank=True, null=True)
    d_state = models.CharField(max_length=19, blank=True, null=True)
    d_unloadbl = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'blank'


class Bmonth(BaseModel):
    kod = models.CharField(max_length=2, blank=True, null=True)
    mes = models.CharField(max_length=9, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'bmonth'


class Bnkseek(BaseModel):
    vkey = models.CharField(max_length=8, blank=True, null=True)
    real = models.CharField(max_length=4, blank=True, null=True)
    pzn = models.CharField(max_length=2, blank=True, null=True)
    uer = models.CharField(max_length=1, blank=True, null=True)
    rgn = models.CharField(max_length=2, blank=True, null=True)
    ind = models.CharField(max_length=6, blank=True, null=True)
    tnp = models.CharField(max_length=1, blank=True, null=True)
    nnp = models.CharField(max_length=25, blank=True, null=True)
    adr = models.CharField(max_length=30, blank=True, null=True)
    rkc = models.CharField(max_length=9, blank=True, null=True)
    namep = models.CharField(max_length=45, blank=True, null=True)
    namen = models.CharField(max_length=30, blank=True, null=True)
    newnum = models.CharField(max_length=9, blank=True, null=True)
    newks = models.CharField(max_length=9, blank=True, null=True)
    permfo = models.CharField(max_length=6, blank=True, null=True)
    srok = models.CharField(max_length=2, blank=True, null=True)
    at1 = models.CharField(max_length=7, blank=True, null=True)
    at2 = models.CharField(max_length=7, blank=True, null=True)
    telef = models.CharField(max_length=25, blank=True, null=True)
    regn = models.CharField(max_length=9, blank=True, null=True)
    okpo = models.CharField(max_length=8, blank=True, null=True)
    dt_izm = models.DateField(blank=True, null=True)
    cks = models.CharField(max_length=6, blank=True, null=True)
    ksnp = models.CharField(max_length=20, blank=True, null=True)
    date_in = models.DateField(blank=True, null=True)
    date_ch = models.DateField(blank=True, null=True)
    vkeydel = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'bnkseek'


class Brok(BaseModel):
    sbj_id = models.DecimalField(default=0.00, max_digits=15, decimal_places=0, blank=True, null=True)
    br_lic_id = models.DecimalField(default=0.00, max_digits=15, decimal_places=0, blank=True, null=True)
    doctype = models.CharField(max_length=1, blank=True, null=True)
    docnumber = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'brok'


class Bx(BaseModel):
    sbj_id = models.DecimalField(default=0.00, max_digits=15, decimal_places=0, blank=True, null=True)
    bx_lic_id = models.DecimalField(default=0.00, max_digits=15, decimal_places=0, blank=True, null=True)
    doctype = models.CharField(max_length=1, blank=True, null=True)
    docnumber = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'bx'


class Car(BaseModel):
    sbj_id = models.DecimalField(default=0.00, max_digits=15, decimal_places=0, blank=True, null=True)
    car_lic_id = models.DecimalField(default=0.00, max_digits=15, decimal_places=0, blank=True, null=True)
    doctype = models.CharField(max_length=1, blank=True, null=True)
    docnumber = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'car'


class Carrier(BaseModel):
    st = models.CharField(max_length=2, blank=True, null=True)
    typ_doc = models.CharField(max_length=1, blank=True, null=True)
    nlic = models.CharField(max_length=25, blank=True, null=True)
    pr_per = models.CharField(max_length=1, blank=True, null=True)
    n_blank = models.CharField(max_length=10, blank=True, null=True)
    dbegin = models.DateField(blank=True, null=True)
    dend = models.DateField(blank=True, null=True)
    kodt = models.CharField(max_length=55, blank=True, null=True)
    idel = models.CharField(max_length=1, blank=True, null=True)
    typep = models.CharField(max_length=1, blank=True, null=True)
    owner = models.CharField(max_length=255, blank=True, null=True)
    adrrown = models.TextField(blank=True, null=True)
    adrpocht = models.TextField(blank=True, null=True)
    telefp = models.CharField(max_length=50, blank=True, null=True)
    teletype = models.CharField(max_length=30, blank=True, null=True)
    telefax = models.CharField(max_length=30, blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    ogrn = models.CharField(max_length=15, blank=True, null=True)
    inn = models.CharField(max_length=20, blank=True, null=True)
    kpp = models.CharField(max_length=9, blank=True, null=True)
    okpo = models.CharField(max_length=10, blank=True, null=True)
    iakciz = models.CharField(max_length=1, blank=True, null=True)
    asovam = models.CharField(max_length=8, blank=True, null=True)
    vidtrans = models.CharField(max_length=20, blank=True, null=True)
    date_mod = models.DateField(blank=True, null=True)
    opf_vl = models.CharField(max_length=2, blank=True, null=True)
    rf_outp = models.CharField(max_length=9, blank=True, null=True)
    doc_tp = models.CharField(max_length=100, blank=True, null=True)
    dend_tp = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'carrier'


class Carrierb(BaseModel):
    country = models.CharField(max_length=3, blank=True, null=True)
    customs = models.CharField(max_length=2, blank=True, null=True)
    custpost = models.CharField(max_length=3, blank=True, null=True)
    nlic = models.CharField(max_length=15, blank=True, null=True)
    pr_per = models.CharField(max_length=1, blank=True, null=True)
    inn = models.CharField(max_length=12, blank=True, null=True)
    okpo = models.CharField(max_length=8, blank=True, null=True)
    datereg = models.DateField(blank=True, null=True)
    dbegin = models.DateField(blank=True, null=True)
    dend = models.DateField(blank=True, null=True)
    idel = models.CharField(max_length=1, blank=True, null=True)
    didel = models.DateField(blank=True, null=True)
    typep = models.CharField(max_length=1, blank=True, null=True)
    owner = models.CharField(max_length=50, blank=True, null=True)
    adrrown = models.CharField(max_length=150, blank=True, null=True)
    telefp = models.CharField(max_length=31, blank=True, null=True)
    asovan = models.CharField(max_length=9, blank=True, null=True)
    vidtrans = models.CharField(max_length=21, blank=True, null=True)
    iakciz = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'carrierb'


class CbContr(BaseModel):
    codcontr = models.CharField(max_length=1, blank=True, null=True)
    vidcontr = models.CharField(max_length=250, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=50, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=50, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'cb_contr'


class Chkpoint(BaseModel):
    checkpoint = models.CharField(max_length=6, blank=True, null=True)
    code = models.CharField(max_length=8, blank=True, null=True)
    dbegin = models.DateField(blank=True, null=True)
    dend = models.DateField(blank=True, null=True)
    kod_tr = models.CharField(max_length=2, blank=True, null=True)
    name_pp = models.CharField(max_length=80, blank=True, null=True)
    sopred_exi = models.CharField(max_length=1, blank=True, null=True)
    uprosh = models.CharField(max_length=1, blank=True, null=True)
    initial_do = models.CharField(max_length=4, blank=True, null=True)
    opening_do = models.CharField(max_length=4, blank=True, null=True)
    fun = models.CharField(max_length=1, blank=True, null=True)
    character = models.CharField(max_length=2, blank=True, null=True)
    regim = models.CharField(max_length=1, blank=True, null=True)
    kategor = models.CharField(max_length=1, blank=True, null=True)
    sovam = models.CharField(max_length=8, blank=True, null=True)
    rsovam = models.CharField(max_length=8, blank=True, null=True)
    dat_beg = models.DateField(blank=True, null=True)
    pric_beg = models.CharField(max_length=50, blank=True, null=True)
    dat_beg_r = models.DateField(blank=True, null=True)
    status_r = models.CharField(max_length=1, blank=True, null=True)
    dat_end = models.DateField(blank=True, null=True)
    pric_end = models.CharField(max_length=50, blank=True, null=True)
    dat_del_r = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'chkpoint'


class Cntr(BaseModel):
    ncntr = models.DecimalField(default=0.00, max_digits=3, decimal_places=0, blank=True, null=True)
    cntr = models.CharField(max_length=20, blank=True, null=True)
    alfa3 = models.CharField(max_length=3, blank=True, null=True)
    dimp = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'cntr'


class CrV(BaseModel):
    d_reason = models.CharField(max_length=150, blank=True, null=True)
    full_d = models.CharField(max_length=250, blank=True, null=True)
    code = models.CharField(max_length=3, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'cr_v'


class Crdts(BaseModel):
    numcard = models.CharField(max_length=20, blank=True, null=True)
    vin = models.CharField(max_length=20, blank=True, null=True)
    model = models.CharField(max_length=36, blank=True, null=True)
    tipts = models.CharField(max_length=2, blank=True, null=True)
    kategts = models.CharField(max_length=1, blank=True, null=True)
    mest = models.DecimalField(default=0.00, max_digits=4, decimal_places=0, blank=True, null=True)
    god = models.DecimalField(default=0.00, max_digits=4, decimal_places=0, blank=True, null=True)
    moddvig = models.CharField(max_length=15, blank=True, null=True)
    numdvig = models.CharField(max_length=20, blank=True, null=True)
    numkper = models.CharField(max_length=20, blank=True, null=True)
    nummost = models.CharField(max_length=80, blank=True, null=True)
    shassi = models.CharField(max_length=20, blank=True, null=True)
    kuzov = models.CharField(max_length=20, blank=True, null=True)
    zvet = models.CharField(max_length=3, blank=True, null=True)
    powerls = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    powerkw = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    obdvig = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    tipdv = models.CharField(max_length=2, blank=True, null=True)
    viddvig = models.CharField(max_length=2, blank=True, null=True)
    maxmass = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    minmass = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    maxspeed = models.DecimalField(default=0.00, max_digits=3, decimal_places=0, blank=True, null=True)
    width = models.DecimalField(default=0.00, max_digits=5, decimal_places=0, blank=True, null=True)
    height = models.DecimalField(default=0.00, max_digits=5, decimal_places=0, blank=True, null=True)
    length = models.DecimalField(default=0.00, max_digits=5, decimal_places=0, blank=True, null=True)
    kodizgot = models.CharField(max_length=3, blank=True, null=True)
    izgotov = models.CharField(max_length=50, blank=True, null=True)
    strizg = models.CharField(max_length=3, blank=True, null=True)
    adrizg = models.CharField(max_length=50, blank=True, null=True)
    numodob = models.CharField(max_length=19, blank=True, null=True)
    datodob = models.DateField(blank=True, null=True)
    orgodob = models.CharField(max_length=128, blank=True, null=True)
    strvyvoz = models.CharField(max_length=3, blank=True, null=True)
    lic = models.CharField(max_length=1, blank=True, null=True)
    fam = models.CharField(max_length=30, blank=True, null=True)
    ima = models.CharField(max_length=25, blank=True, null=True)
    otc = models.CharField(max_length=25, blank=True, null=True)
    okpo = models.CharField(max_length=8, blank=True, null=True)
    namesob = models.CharField(max_length=80, blank=True, null=True)
    adressob = models.CharField(max_length=80, blank=True, null=True)
    udvvoz = models.CharField(max_length=10, blank=True, null=True)
    datud = models.DateField(blank=True, null=True)
    lnpu = models.CharField(max_length=4, blank=True, null=True)
    g071 = models.CharField(max_length=5, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)
    tamogr = models.CharField(max_length=150, blank=True, null=True)
    numpts = models.CharField(max_length=10, blank=True, null=True)
    datpts = models.DateField(blank=True, null=True)
    lnp = models.CharField(max_length=4, blank=True, null=True)
    work = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    p_ts = models.CharField(max_length=1, blank=True, null=True)
    g32 = models.DecimalField(default=0.00, max_digits=3, decimal_places=0, blank=True, null=True)
    g33 = models.CharField(max_length=10, blank=True, null=True)
    numtd = models.CharField(max_length=20, blank=True, null=True)
    dattd = models.DateField(blank=True, null=True)
    numz = models.CharField(max_length=20, blank=True, null=True)
    datz = models.DateField(blank=True, null=True)
    dateout = models.DateField(blank=True, null=True)
    timeout = models.CharField(max_length=8, blank=True, null=True)
    datemodi = models.DateField(blank=True, null=True)
    imodi = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'crdts'


class CtovR(BaseModel):
    code = models.CharField(max_length=3, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'ctov_r'


class Ctu(BaseModel):
    kodstan = models.CharField(max_length=5, blank=True, null=True)
    naimstan = models.CharField(max_length=24, blank=True, null=True)
    dats_s = models.DateField(blank=True, null=True)
    koddor = models.CharField(max_length=2, blank=True, null=True)
    naimdor = models.CharField(max_length=21, blank=True, null=True)
    kodotd = models.CharField(max_length=4, blank=True, null=True)
    kodtam = models.CharField(max_length=5, blank=True, null=True)
    code = models.CharField(max_length=8, blank=True, null=True)
    dats_t = models.DateField(blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    komop1 = models.CharField(max_length=2, blank=True, null=True)
    komop2 = models.CharField(max_length=2, blank=True, null=True)
    komop3 = models.CharField(max_length=2, blank=True, null=True)
    komop4 = models.CharField(max_length=2, blank=True, null=True)
    komop5 = models.CharField(max_length=2, blank=True, null=True)
    komop6 = models.CharField(max_length=2, blank=True, null=True)
    komop7 = models.CharField(max_length=2, blank=True, null=True)
    komop8 = models.CharField(max_length=2, blank=True, null=True)
    komop9 = models.CharField(max_length=2, blank=True, null=True)
    komop10 = models.CharField(max_length=2, blank=True, null=True)
    komop11 = models.CharField(max_length=2, blank=True, null=True)
    komop12 = models.CharField(max_length=2, blank=True, null=True)
    komop13 = models.CharField(max_length=2, blank=True, null=True)
    komop14 = models.CharField(max_length=2, blank=True, null=True)
    komop15 = models.CharField(max_length=2, blank=True, null=True)
    datp = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'ctu'


class Currency(BaseModel):
    kod = models.DecimalField(default=0.00, max_digits=3, decimal_places=0, blank=True, null=True)
    bukkod = models.CharField(max_length=3, blank=True, null=True)
    krnaim = models.CharField(max_length=20, blank=True, null=True)
    ncntr = models.DecimalField(default=0.00, max_digits=3, decimal_places=0, blank=True, null=True)
    kolv = models.DecimalField(default=0.00, max_digits=5, decimal_places=0, blank=True, null=True)
    kursv = models.DecimalField(default=0.00, max_digits=6, decimal_places=2, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'currency'


class Custlist(BaseModel):
    code = models.CharField(max_length=8, blank=True, null=True)
    prright = models.BooleanField(blank=True, null=True)
    rprright = models.BooleanField(blank=True, null=True)
    sprright = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    tprright = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'custlist'


class Customs(BaseModel):
    customs = models.CharField(max_length=2, blank=True, null=True)
    name = models.CharField(max_length=40, blank=True, null=True)
    address = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'customs'


class Custpost(BaseModel):
    custom = models.CharField(max_length=2, blank=True, null=True)
    custpost = models.CharField(max_length=3, blank=True, null=True)
    name = models.CharField(max_length=40, blank=True, null=True)
    address = models.CharField(max_length=65, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'custpost'


class D44MPr(BaseModel):
    kod = models.CharField(max_length=5, blank=True, null=True)
    n_msk = models.DecimalField(default=0.00, max_digits=5, decimal_places=0, blank=True, null=True)
    sid_smev = models.CharField(max_length=55, blank=True, null=True)
    kod_foiv = models.CharField(max_length=10, blank=True, null=True)
    kodpr = models.CharField(max_length=2, blank=True, null=True)
    razdel_1 = models.CharField(max_length=1, blank=True, null=True)
    razdel_2 = models.CharField(max_length=1, blank=True, null=True)
    pr_plt = models.CharField(max_length=4, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'd44_m_pr'


class D44MTn(BaseModel):
    kod = models.CharField(max_length=5, blank=True, null=True)
    n_msk = models.DecimalField(default=0.00, max_digits=5, decimal_places=0, blank=True, null=True)
    sid_smev = models.CharField(max_length=55, blank=True, null=True)
    foiv = models.CharField(max_length=255, blank=True, null=True)
    kodt = models.CharField(max_length=10, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'd44_m_tn'


class D44Mask(BaseModel):
    sid_smev = models.CharField(max_length=55, blank=True, null=True)
    kod = models.CharField(max_length=5, blank=True, null=True)
    n_msk = models.DecimalField(default=0.00, max_digits=5, decimal_places=0, blank=True, null=True)
    name_msk = models.CharField(max_length=255, blank=True, null=True)
    k_maska = models.CharField(max_length=255, blank=True, null=True)
    dscr_msk = models.CharField(max_length=255, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)
    priznak = models.CharField(max_length=1, blank=True, null=True)
    p_dop = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'd44_mask'


class D44Sfoiv(BaseModel):
    kod_foiv = models.CharField(max_length=10, blank=True, null=True)
    kod = models.CharField(max_length=5, blank=True, null=True)
    mode_id = models.CharField(max_length=8, blank=True, null=True)
    docname = models.CharField(max_length=255, blank=True, null=True)
    sid_smev = models.CharField(max_length=10, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'd44sfoiv'


class Declrnt(BaseModel):
    okpo = models.CharField(max_length=8, blank=True, null=True)
    nlic = models.CharField(max_length=15, blank=True, null=True)
    datr = models.DateField(blank=True, null=True)
    ndecl = models.CharField(max_length=80, blank=True, null=True)
    adr = models.CharField(max_length=80, blank=True, null=True)
    schet1 = models.CharField(max_length=20, blank=True, null=True)
    bank1 = models.CharField(max_length=100, blank=True, null=True)
    schet2 = models.CharField(max_length=20, blank=True, null=True)
    bank2 = models.CharField(max_length=100, blank=True, null=True)
    telefon = models.CharField(max_length=12, blank=True, null=True)
    telefaks = models.CharField(max_length=12, blank=True, null=True)
    teleks = models.CharField(max_length=20, blank=True, null=True)
    telegraf = models.CharField(max_length=50, blank=True, null=True)
    inn = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'declrnt'


class Delstakc(BaseModel):
    kodstr = models.CharField(max_length=3, blank=True, null=True)
    kodtov = models.CharField(max_length=10, blank=True, null=True)
    st_l = models.DecimalField(default=0.00, max_digits=10, decimal_places=3, blank=True, null=True)
    simvl = models.CharField(max_length=3, blank=True, null=True)
    edil = models.CharField(max_length=3, blank=True, null=True)
    oper = models.CharField(max_length=1, blank=True, null=True)
    st_r = models.DecimalField(default=0.00, max_digits=10, decimal_places=3, blank=True, null=True)
    simvr = models.CharField(max_length=3, blank=True, null=True)
    edir = models.CharField(max_length=3, blank=True, null=True)
    prim = models.CharField(max_length=140, blank=True, null=True)
    npric = models.CharField(max_length=20, blank=True, null=True)
    dpric = models.DateField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    data1 = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'delstakc'


class DipPrim(BaseModel):
    kodt = models.CharField(max_length=10, blank=True, null=True)
    naim = models.CharField(max_length=150, blank=True, null=True)
    st_dip = models.DecimalField(default=0.00, max_digits=10, decimal_places=3, blank=True, null=True)
    npric = models.CharField(max_length=20, blank=True, null=True)
    dpric = models.DateField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    data1 = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'dip_prim'


class Dnbdlist(BaseModel):
    id_num = models.CharField(max_length=18, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    adres = models.CharField(max_length=80, blank=True, null=True)
    ogrn = models.CharField(max_length=15, blank=True, null=True)
    inn = models.CharField(max_length=12, blank=True, null=True)
    kpp = models.CharField(max_length=9, blank=True, null=True)
    country = models.CharField(max_length=3, blank=True, null=True)
    appl_no = models.CharField(max_length=1, blank=True, null=True)
    prikaz = models.CharField(max_length=50, blank=True, null=True)
    data_b = models.DateField(blank=True, null=True)
    data_o = models.DateField(blank=True, null=True)
    country_pr = models.CharField(max_length=3, blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'dnbdlist'


class Dobstakc(BaseModel):
    dst_ak = models.DecimalField(default=0.00, max_digits=10, decimal_places=3, blank=True, null=True)
    npric = models.CharField(max_length=20, blank=True, null=True)
    dpric = models.DateField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    data1 = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'dobstakc'


class DocAmts(BaseModel):
    kod = models.CharField(max_length=2, blank=True, null=True)
    name = models.CharField(max_length=240, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'doc_amts'


class DocPr(BaseModel):
    kod = models.DecimalField(default=0.00, max_digits=2, decimal_places=0, blank=True, null=True)
    vid = models.CharField(max_length=128, blank=True, null=True)
    i44 = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'doc_pr'


class DocTnv(BaseModel):
    priznac = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    code1 = models.CharField(max_length=10, blank=True, null=True)
    code2 = models.CharField(max_length=10, blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    inform = models.TextField(blank=True, null=True)
    recomm = models.TextField(blank=True, null=True)
    prim = models.CharField(max_length=255, blank=True, null=True)
    dbegin = models.DateField(blank=True, null=True)
    dend = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'doc_tnv'


class Docg44(BaseModel):
    kod = models.CharField(max_length=5, blank=True, null=True)
    gr_doc = models.CharField(max_length=2, blank=True, null=True)
    naim = models.TextField(blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)
    pr_rb = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    pr_rk = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    pr_rf = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    pr_am = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    pr_kg = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'docg44'


class Docum(BaseModel):
    cod = models.CharField(max_length=2, blank=True, null=True)
    name = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'docum'


class Document(BaseModel):
    doc_id = models.CharField(max_length=4, blank=True, null=True)
    doc_type_i = models.CharField(max_length=2, blank=True, null=True)
    vid_doc = models.CharField(max_length=2, blank=True, null=True)
    comment = models.CharField(max_length=200, blank=True, null=True)
    num_doc = models.CharField(max_length=10, blank=True, null=True)
    dat_doc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'document'


class DohNepr(BaseModel):
    kod = models.CharField(max_length=3, blank=True, null=True)
    naim = models.CharField(max_length=250, blank=True, null=True)
    tip = models.CharField(max_length=250, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'doh_nepr'


class DohOsn(BaseModel):
    kod = models.CharField(max_length=3, blank=True, null=True)
    naim = models.CharField(max_length=250, blank=True, null=True)
    docum = models.CharField(max_length=20, blank=True, null=True)
    stat = models.CharField(max_length=20, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'doh_osn'


class DolgAll(BaseModel):
    kod = models.CharField(max_length=8, blank=True, null=True)
    nomr3 = models.CharField(max_length=10, blank=True, null=True)
    ogrn = models.CharField(max_length=15, blank=True, null=True)
    inn = models.CharField(max_length=12, blank=True, null=True)
    kpp = models.CharField(max_length=9, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'dolg_all'


# class Dolgt(BaseModel):
#     kod = models.CharField(db_column='KOD', max_length=8, blank=True, null=True)  # Field name made lowercase.
#     customs = models.CharField(db_column='ТАМОЖНЯ', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     kodzon = models.CharField(db_column='KODZON', max_length=8, blank=True, null=True)  # Field name made lowercase.
#     naim = models.CharField(db_column='NAIM', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     nomr1 = models.CharField(db_column='NOMR1', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     nomr3 = models.CharField(db_column='NOMR3', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     inn = models.CharField(db_column='INN', max_length=12, blank=True, null=True)  # Field name made lowercase.
#     kpp = models.CharField(db_column='KPP', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     series = models.CharField(db_column='SERIES', max_length=8, blank=True, null=True)  # Field name made lowercase.
#     nompas = models.CharField(db_column='NOMPAS', max_length=12, blank=True, null=True)  # Field name made lowercase.
#     krnaim = models.CharField(db_column='KRNAIM', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     kodd = models.CharField(db_column='KODD', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     drepot = models.DateTimeField(db_column='DREPOT', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         abstract = True
#         # db_table = 'dolgt'


class Dov(BaseModel):
    naim = models.CharField(max_length=52, blank=True, null=True)
    adres = models.CharField(max_length=52, blank=True, null=True)
    fio = models.CharField(max_length=30, blank=True, null=True)
    countrycod = models.CharField(max_length=3, blank=True, null=True)
    inn = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    telex = models.CharField(max_length=20, blank=True, null=True)
    fax = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'dov'


class Dtamreg(BaseModel):
    kod = models.CharField(max_length=3, blank=True, null=True)
    naim = models.TextField(blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)
    pr_rb = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    pr_rk = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    pr_rf = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    pr_am = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    pr_kg = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'dtamreg'


class Ecop(BaseModel):
    st = models.CharField(max_length=2, blank=True, null=True)
    nlic = models.CharField(max_length=25, blank=True, null=True)
    pr_per = models.CharField(max_length=1, blank=True, null=True)
    n_blank = models.CharField(max_length=10, blank=True, null=True)
    dbegin = models.DateField(blank=True, null=True)
    dend = models.DateField(blank=True, null=True)
    owner = models.CharField(max_length=255, blank=True, null=True)
    opf_vl = models.CharField(max_length=2, blank=True, null=True)
    post = models.CharField(max_length=9, blank=True, null=True)
    subd = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=35, blank=True, null=True)
    street = models.CharField(max_length=50, blank=True, null=True)
    telephon = models.CharField(max_length=100, blank=True, null=True)
    teletype = models.CharField(max_length=100, blank=True, null=True)
    telefax = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    ogrn = models.CharField(max_length=15, blank=True, null=True)
    inn = models.CharField(max_length=20, blank=True, null=True)
    kpp = models.CharField(max_length=9, blank=True, null=True)
    okpo = models.CharField(max_length=10, blank=True, null=True)
    osp = models.CharField(max_length=1, blank=True, null=True)
    date_mod = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)
    numsusdoc = models.CharField(max_length=20, blank=True, null=True)
    datsusdoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'ecop'


class Ecop1(BaseModel):
    st = models.CharField(max_length=2, blank=True, null=True)
    nlic = models.CharField(max_length=25, blank=True, null=True)
    pr_per = models.CharField(max_length=1, blank=True, null=True)
    dbegin = models.DateField(blank=True, null=True)
    owner = models.CharField(max_length=255, blank=True, null=True)
    inn = models.CharField(max_length=20, blank=True, null=True)
    kpp = models.CharField(max_length=9, blank=True, null=True)
    post = models.CharField(max_length=9, blank=True, null=True)
    subd = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=35, blank=True, null=True)
    street = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'ecop1'


class Ecop2(BaseModel):
    st = models.CharField(max_length=2, blank=True, null=True)
    nlic = models.CharField(max_length=25, blank=True, null=True)
    pr_per = models.CharField(max_length=1, blank=True, null=True)
    dbegin = models.DateField(blank=True, null=True)
    kod_tam = models.CharField(max_length=8, blank=True, null=True)
    sp_simpl = models.CharField(max_length=1, blank=True, null=True)
    time_resh = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'ecop2'


class Ecop3(BaseModel):
    st = models.CharField(max_length=2, blank=True, null=True)
    nlic = models.CharField(max_length=25, blank=True, null=True)
    pr_per = models.CharField(max_length=1, blank=True, null=True)
    dbegin = models.DateField(blank=True, null=True)
    sp_simpl = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'ecop3'


class Ecop4(BaseModel):
    st = models.CharField(max_length=2, blank=True, null=True)
    nlic = models.CharField(max_length=25, blank=True, null=True)
    pr_per = models.CharField(max_length=1, blank=True, null=True)
    dbegin = models.DateField(blank=True, null=True)
    guarkind = models.CharField(max_length=2, blank=True, null=True)
    numbdoctp = models.CharField(max_length=25, blank=True, null=True)
    datbdoctp = models.DateField(blank=True, null=True)
    begdoctp = models.DateField(blank=True, null=True)
    enddoctp = models.DateField(blank=True, null=True)
    amount = models.DecimalField(default=0.00, max_digits=20, decimal_places=2, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'ecop4'


class Ecop5(BaseModel):
    st = models.CharField(max_length=2, blank=True, null=True)
    nlic = models.CharField(max_length=25, blank=True, null=True)
    pr_per = models.CharField(max_length=1, blank=True, null=True)
    dbegin = models.DateField(blank=True, null=True)
    p_locat = models.CharField(max_length=255, blank=True, null=True)
    tam_loc = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'ecop5'


class Edizm(BaseModel):
    kod = models.CharField(max_length=3, blank=True, null=True)
    krnaim = models.CharField(max_length=100, blank=True, null=True)
    fnaim = models.CharField(max_length=255, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'edizm'


class EdizmDp(BaseModel):
    kod = models.CharField(max_length=3, blank=True, null=True)
    krnaim = models.CharField(max_length=100, blank=True, null=True)
    fnaim = models.CharField(max_length=255, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'edizm_dp'


class EkAr(BaseModel):
    kod_ar = models.CharField(max_length=2, blank=True, null=True)
    naim = models.CharField(max_length=50, blank=True, null=True)
    krnaim = models.CharField(max_length=7, blank=True, null=True)
    akrnaim = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'ek_ar'


class EkEu(BaseModel):
    krnaim = models.CharField(max_length=5, blank=True, null=True)
    naim = models.CharField(max_length=50, blank=True, null=True)
    abc2 = models.CharField(max_length=2, blank=True, null=True)
    abc3 = models.CharField(max_length=3, blank=True, null=True)
    pr_str = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    pr_regio = models.CharField(max_length=2, blank=True, null=True)
    kod_ar = models.CharField(max_length=14, blank=True, null=True)
    reserv = models.CharField(max_length=10, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'ek_eu'


class ExpPrim(BaseModel):
    kodt = models.CharField(max_length=10, blank=True, null=True)
    naim = models.CharField(max_length=150, blank=True, null=True)
    st_min = models.DecimalField(default=0.00, max_digits=9, decimal_places=3, blank=True, null=True)
    simvmin = models.CharField(max_length=1, blank=True, null=True)
    edimin = models.CharField(max_length=3, blank=True, null=True)
    st_dop = models.DecimalField(default=0.00, max_digits=9, decimal_places=3, blank=True, null=True)
    simvdop = models.CharField(max_length=1, blank=True, null=True)
    edidop = models.CharField(max_length=3, blank=True, null=True)
    oper = models.CharField(max_length=1, blank=True, null=True)
    st_max = models.DecimalField(default=0.00, max_digits=10, decimal_places=3, blank=True, null=True)
    simvmax = models.CharField(max_length=1, blank=True, null=True)
    edimax = models.CharField(max_length=3, blank=True, null=True)
    ivzmtams = models.CharField(max_length=1, blank=True, null=True)
    ivzmsng = models.CharField(max_length=1, blank=True, null=True)
    ivzmdalz = models.CharField(max_length=1, blank=True, null=True)
    npric = models.CharField(max_length=20, blank=True, null=True)
    dpric = models.DateField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    data1 = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'exp_prim'


class Experimt(BaseModel):
    kodt = models.CharField(max_length=8, blank=True, null=True)
    experiment = models.CharField(max_length=100, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'experimt'


class Expstakc(BaseModel):
    okpo = models.CharField(max_length=10, blank=True, null=True)
    ogrn = models.CharField(max_length=15, blank=True, null=True)
    inn = models.CharField(max_length=12, blank=True, null=True)
    kpp = models.CharField(max_length=9, blank=True, null=True)
    naim = models.CharField(max_length=80, blank=True, null=True)
    st_ak = models.DecimalField(default=0.00, max_digits=10, decimal_places=3, blank=True, null=True)
    npric = models.CharField(max_length=20, blank=True, null=True)
    dpric = models.DateField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    data1 = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'expstakc'


class ExtremM(BaseModel):
    reg_num = models.DecimalField(default=0.00, max_digits=16, decimal_places=0, blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    priznak = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'extrem_m'


class FaItemc(BaseModel):
    ntam = models.DecimalField(default=0.00, max_digits=5, decimal_places=0, blank=True, null=True)
    delnum = models.DecimalField(default=0.00, max_digits=4, decimal_places=0, blank=True, null=True)
    datprt = models.DateField(blank=True, null=True)
    kod = models.CharField(max_length=8, blank=True, null=True)
    kol = models.DecimalField(default=0.00, max_digits=8, decimal_places=0, blank=True, null=True)
    ves = models.DecimalField(default=0.00, max_digits=8, decimal_places=3, blank=True, null=True)
    sum = models.DecimalField(default=0.00, max_digits=10, decimal_places=0, blank=True, null=True)
    ntsk = models.DecimalField(default=0.00, max_digits=2, decimal_places=0, blank=True, null=True)
    nsokr = models.DecimalField(default=0.00, max_digits=3, decimal_places=0, blank=True, null=True)
    prvozv = models.BooleanField(blank=True, null=True)
    dscr1 = models.CharField(max_length=60, blank=True, null=True)
    dscr2 = models.CharField(max_length=60, blank=True, null=True)
    dscr3 = models.CharField(max_length=60, blank=True, null=True)
    daterec = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'fa_itemc'


class FaPredm(BaseModel):
    ident = models.CharField(max_length=8, blank=True, null=True)
    predm = models.CharField(max_length=75, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'fa_predm'


class Finbg(BaseModel):
    kod = models.CharField(max_length=20, blank=True, null=True)
    shifr = models.CharField(max_length=4, blank=True, null=True)
    naim = models.CharField(max_length=180, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'finbg'


class Finbg0(BaseModel):
    kod = models.CharField(max_length=7, blank=True, null=True)
    shifr = models.CharField(max_length=2, blank=True, null=True)
    naim = models.CharField(max_length=180, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'finbg_'


class Fmtk(BaseModel):
    kod_rec = models.CharField(max_length=6, blank=True, null=True)
    text_rec = models.CharField(max_length=250, blank=True, null=True)
    data_beg = models.DateField(blank=True, null=True)
    data_mod = models.DateField(blank=True, null=True)
    data_end = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'fmtk'


class Formras(BaseModel):
    kod = models.CharField(max_length=1, blank=True, null=True)
    naim = models.CharField(max_length=200, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'formras'


class FstRaz(BaseModel):
    typ_doc = models.CharField(max_length=1, blank=True, null=True)
    n_razr = models.CharField(max_length=20, blank=True, null=True)
    d_razr = models.DateField(blank=True, null=True)
    n_kontr = models.CharField(max_length=255, blank=True, null=True)
    d_kontr = models.DateField(blank=True, null=True)
    naim_rus = models.TextField(blank=True, null=True)
    strana = models.CharField(max_length=30, blank=True, null=True)
    n_obj_ek = models.TextField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    datemod = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'fst_raz'


class FstZakl(BaseModel):
    typ_doc = models.CharField(max_length=1, blank=True, null=True)
    n_zakl = models.CharField(max_length=20, blank=True, null=True)
    d_zakl = models.DateField(blank=True, null=True)
    n_kontr = models.CharField(max_length=255, blank=True, null=True)
    d_kontr = models.DateField(blank=True, null=True)
    naim_rus = models.TextField(blank=True, null=True)
    inn = models.CharField(max_length=12, blank=True, null=True)
    naim_frn = models.CharField(max_length=255, blank=True, null=True)
    naim_plz = models.CharField(max_length=255, blank=True, null=True)
    strana = models.CharField(max_length=30, blank=True, null=True)
    n_obj_ek = models.TextField(blank=True, null=True)
    kodtnv = models.CharField(max_length=255, blank=True, null=True)
    kr_opis = models.TextField(blank=True, null=True)
    zakl_obj = models.CharField(max_length=20, blank=True, null=True)
    n_poz_k = models.TextField(blank=True, null=True)
    kontr_sp = models.CharField(max_length=15, blank=True, null=True)
    resume = models.CharField(max_length=255, blank=True, null=True)
    d_status = models.DateField(blank=True, null=True)
    datemod = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'fst_zakl'


class Garant(BaseModel):
    codegar = models.CharField(max_length=2, blank=True, null=True)
    namegar = models.CharField(max_length=55, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'garant'


class GdOtd(BaseModel):
    kodotd = models.CharField(max_length=4, blank=True, null=True)
    naim = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'gd_otd'


class GdStan(BaseModel):
    kodstan = models.CharField(max_length=10, blank=True, null=True)
    naimstan = models.CharField(max_length=100, blank=True, null=True)
    dats_s = models.DateField(blank=True, null=True)
    koddor = models.CharField(max_length=2, blank=True, null=True)
    naimdor = models.CharField(max_length=50, blank=True, null=True)
    kodotd = models.CharField(max_length=4, blank=True, null=True)
    kodtam = models.CharField(max_length=5, blank=True, null=True)
    code = models.CharField(max_length=8, blank=True, null=True)
    dats_t = models.DateField(blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    komop1 = models.CharField(max_length=2, blank=True, null=True)
    komop2 = models.CharField(max_length=2, blank=True, null=True)
    komop3 = models.CharField(max_length=2, blank=True, null=True)
    komop4 = models.CharField(max_length=2, blank=True, null=True)
    komop5 = models.CharField(max_length=2, blank=True, null=True)
    komop6 = models.CharField(max_length=2, blank=True, null=True)
    komop7 = models.CharField(max_length=2, blank=True, null=True)
    komop8 = models.CharField(max_length=2, blank=True, null=True)
    komop9 = models.CharField(max_length=2, blank=True, null=True)
    komop10 = models.CharField(max_length=2, blank=True, null=True)
    komop11 = models.CharField(max_length=2, blank=True, null=True)
    komop12 = models.CharField(max_length=2, blank=True, null=True)
    komop13 = models.CharField(max_length=2, blank=True, null=True)
    komop14 = models.CharField(max_length=2, blank=True, null=True)
    komop15 = models.CharField(max_length=2, blank=True, null=True)
    datp = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'gd_stan'


class GeoAr(BaseModel):
    pr_reg = models.CharField(max_length=2, blank=True, null=True)
    naim = models.CharField(max_length=30, blank=True, null=True)
    anaim = models.CharField(max_length=22, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'geo_ar'


class Grp(BaseModel):
    id = models.CharField(max_length=2, blank=True, null=True)
    name = models.CharField(max_length=24, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'grp'


class Hold(BaseModel):
    kod = models.DecimalField(default=0.00, max_digits=2, decimal_places=0, blank=True, null=True)
    naim = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'hold'


class ImpPrim(BaseModel):
    kodt = models.CharField(max_length=10, blank=True, null=True)
    country2 = models.CharField(max_length=2, blank=True, null=True)
    naim = models.CharField(max_length=150, blank=True, null=True)
    st_min = models.DecimalField(default=0.00, max_digits=9, decimal_places=3, blank=True, null=True)
    simvmin = models.CharField(max_length=1, blank=True, null=True)
    edimin = models.CharField(max_length=3, blank=True, null=True)
    oper = models.CharField(max_length=1, blank=True, null=True)
    st_max = models.DecimalField(default=0.00, max_digits=10, decimal_places=3, blank=True, null=True)
    simvmax = models.CharField(max_length=1, blank=True, null=True)
    edimax = models.CharField(max_length=3, blank=True, null=True)
    npric = models.CharField(max_length=20, blank=True, null=True)
    dpric = models.DateField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    data1 = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'imp_prim'


class InFirm(BaseModel):
    country = models.CharField(max_length=3, blank=True, null=True)
    naim = models.CharField(max_length=76, blank=True, null=True)
    adress = models.CharField(max_length=76, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'in_firm'


class IndicEf(BaseModel):
    kodt = models.CharField(max_length=10, blank=True, null=True)
    ktam = models.CharField(max_length=8, blank=True, null=True)
    category = models.CharField(max_length=2, blank=True, null=True)
    gr013 = models.CharField(max_length=2, blank=True, null=True)
    gr0131 = models.CharField(max_length=5, blank=True, null=True)
    gr014 = models.DateField(blank=True, null=True)
    gr015 = models.CharField(max_length=5, blank=True, null=True)
    g340 = models.CharField(max_length=1, blank=True, null=True)
    g34 = models.CharField(max_length=2, blank=True, null=True)
    dbegin = models.DateField(blank=True, null=True)
    dend = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'indic_ef'


class Indnsi(BaseModel):
    lib = models.CharField(max_length=4, blank=True, null=True)
    namnsi = models.CharField(max_length=12, blank=True, null=True)
    datar = models.DateField(blank=True, null=True)
    datai = models.DateField(blank=True, null=True)
    mark = models.CharField(max_length=1, blank=True, null=True)
    datart = models.CharField(max_length=8, blank=True, null=True)
    datait = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'indnsi'


class Inf1Td(BaseModel):
    kod = models.CharField(max_length=3, blank=True, null=True)
    naim = models.CharField(max_length=255, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)
    pr_rb = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    pr_rk = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    pr_rf = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    pr_am = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    pr_kg = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'inf1td'


class InfEais(BaseModel):
    num_inf = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    name_inf = models.CharField(max_length=250, blank=True, null=True)
    acc_inf = models.CharField(max_length=250, blank=True, null=True)
    cust_code = models.CharField(max_length=8, blank=True, null=True)
    annotat = models.CharField(max_length=250, blank=True, null=True)
    date_beg = models.DateField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)
    date_crt = models.DateField(blank=True, null=True)
    oper_crt = models.CharField(max_length=13, blank=True, null=True)
    hps_crt = models.CharField(max_length=20, blank=True, null=True)
    date_mod = models.DateField(blank=True, null=True)
    oper_mod = models.CharField(max_length=13, blank=True, null=True)
    hps_mod = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'inf_eais'


class Infram(BaseModel):
    kodram = models.CharField(max_length=2, blank=True, null=True)
    kod = models.CharField(max_length=9, blank=True, null=True)
    naim = models.CharField(max_length=250, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'infram'


class Izgot(BaseModel):
    mki = models.CharField(max_length=3, blank=True, null=True)
    ski = models.CharField(max_length=3, blank=True, null=True)
    name = models.CharField(max_length=24, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'izgot'


class Kat(BaseModel):
    nomr3 = models.CharField(max_length=8, blank=True, null=True)
    nomr1 = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'kat'


class Kateg(BaseModel):
    kod = models.CharField(max_length=2, blank=True, null=True)
    naim = models.CharField(max_length=250, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'kateg'


class Kategwar(BaseModel):
    kateg = models.CharField(max_length=4, blank=True, null=True)
    name = models.CharField(max_length=390, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'kategwar'


class Katt(BaseModel):
    kod = models.CharField(max_length=2, blank=True, null=True)
    naim = models.CharField(max_length=40, blank=True, null=True)
    pr_s = models.DecimalField(default=0.00, max_digits=3, decimal_places=0, blank=True, null=True)
    vid_x = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'katt'


class Kkk(BaseModel):
    kodt = models.CharField(max_length=5, blank=True, null=True)
    namt = models.CharField(max_length=50, blank=True, null=True)
    kodzon = models.CharField(max_length=5, blank=True, null=True)
    adrtam = models.CharField(max_length=75, blank=True, null=True)
    gorod = models.CharField(max_length=30, blank=True, null=True)
    fax = models.CharField(max_length=20, blank=True, null=True)
    teleks = models.CharField(max_length=20, blank=True, null=True)
    telefon = models.CharField(max_length=20, blank=True, null=True)
    datas = models.DateField(blank=True, null=True)
    kodtn = models.CharField(max_length=5, blank=True, null=True)
    rpsi = models.CharField(max_length=5, blank=True, null=True)
    adr_okdt = models.CharField(max_length=100, blank=True, null=True)
    tel_okdt = models.CharField(max_length=20, blank=True, null=True)
    fax_okdt = models.CharField(max_length=20, blank=True, null=True)
    tx_okdt = models.CharField(max_length=20, blank=True, null=True)
    ruk_okdt = models.CharField(max_length=50, blank=True, null=True)
    adr_dost = models.CharField(max_length=100, blank=True, null=True)
    reg_dost = models.CharField(max_length=150, blank=True, null=True)
    trn_dost = models.CharField(max_length=25, blank=True, null=True)
    tel_dost = models.CharField(max_length=20, blank=True, null=True)
    fax_dost = models.CharField(max_length=20, blank=True, null=True)
    tx_dost = models.CharField(max_length=20, blank=True, null=True)
    sovam = models.CharField(max_length=8, blank=True, null=True)
    owner = models.CharField(max_length=5, blank=True, null=True)
    sign = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'kkk'


class Kl203B(BaseModel):
    kod = models.CharField(max_length=2, blank=True, null=True)
    naim = models.CharField(max_length=100, blank=True, null=True)
    srok = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'kl203b'


class Kl203E(BaseModel):
    kod = models.CharField(max_length=2, blank=True, null=True)
    naim = models.CharField(max_length=100, blank=True, null=True)
    srok = models.CharField(max_length=4, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'kl203e'


class Kl203I(BaseModel):
    kod = models.CharField(max_length=2, blank=True, null=True)
    naim = models.CharField(max_length=100, blank=True, null=True)
    srok = models.CharField(max_length=4, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'kl203i'


class Kl204(BaseModel):
    kod = models.CharField(max_length=2, blank=True, null=True)
    naim_r = models.CharField(max_length=250, blank=True, null=True)
    naim_f = models.CharField(max_length=250, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'kl204'


class Kl204B(BaseModel):
    kod = models.CharField(max_length=2, blank=True, null=True)
    naim = models.CharField(max_length=50, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'kl204b'


class Kl204Ing(BaseModel):
    kod = models.CharField(max_length=2, blank=True, null=True)
    naim = models.CharField(max_length=50, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'kl204ing'


class KlStav(BaseModel):
    stav = models.DecimalField(default=0.00, max_digits=7, decimal_places=4, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    datemod = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'kl_stav'


class Klass203(BaseModel):
    kod = models.CharField(max_length=2, blank=True, null=True)
    naim = models.CharField(max_length=50, blank=True, null=True)
    srok = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'klass203'


class Klass204(BaseModel):
    kod = models.CharField(max_length=2, blank=True, null=True)
    naim = models.CharField(max_length=50, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'klass204'


class Klass205(BaseModel):
    kod = models.CharField(max_length=2, blank=True, null=True)
    srok = models.CharField(max_length=4, blank=True, null=True)
    naim = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'klass205'


class KlirVal(BaseModel):
    kod_kl = models.CharField(max_length=3, blank=True, null=True)
    naim_kl = models.CharField(max_length=100, blank=True, null=True)
    kod = models.CharField(max_length=3, blank=True, null=True)
    buk = models.CharField(max_length=3, blank=True, null=True)
    pr_kod = models.CharField(max_length=20, blank=True, null=True)
    numdoc = models.CharField(max_length=20, blank=True, null=True)
    datdoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'klir_val'


class Kliring(BaseModel):
    kod_kl = models.CharField(max_length=3, blank=True, null=True)
    naim_kl = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'kliring'


class KodG300(BaseModel):
    kod = models.CharField(max_length=2, blank=True, null=True)
    naimk = models.CharField(max_length=40, blank=True, null=True)
    naimp = models.CharField(max_length=240, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'kod_g300'


class Kodkdt(BaseModel):
    kod = models.CharField(max_length=2, blank=True, null=True)
    naim = models.CharField(max_length=255, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'kodkdt'


class Kodktc(BaseModel):
    kod = models.CharField(max_length=1, blank=True, null=True)
    naim = models.CharField(max_length=255, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'kodktc'


class Komop(BaseModel):
    kod = models.CharField(max_length=2, blank=True, null=True)
    naimp = models.CharField(max_length=80, blank=True, null=True)
    naimk = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'komop'


class Kray(BaseModel):
    pole1 = models.CharField(max_length=3, blank=True, null=True)
    pole2 = models.CharField(max_length=2, blank=True, null=True)
    pole5 = models.CharField(max_length=50, blank=True, null=True)
    pole7 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'kray'


class Ktam(BaseModel):
    code = models.CharField(max_length=8, blank=True, null=True)
    strana2 = models.CharField(max_length=2, blank=True, null=True)
    dbegin = models.DateField(blank=True, null=True)
    nprcreate = models.CharField(max_length=40, blank=True, null=True)
    dprcreate = models.DateField(blank=True, null=True)
    atrchange = models.CharField(max_length=1, blank=True, null=True)
    dend = models.DateField(blank=True, null=True)
    dendcust = models.DateField(blank=True, null=True)
    nprend = models.CharField(max_length=40, blank=True, null=True)
    dprend = models.DateField(blank=True, null=True)
    newcode = models.CharField(max_length=8, blank=True, null=True)
    kodt = models.CharField(max_length=5, blank=True, null=True)
    ttt = models.CharField(max_length=3, blank=True, null=True)
    owner = models.CharField(max_length=5, blank=True, null=True)
    kodzon = models.CharField(max_length=5, blank=True, null=True)
    kodtn = models.CharField(max_length=5, blank=True, null=True)
    datas = models.DateField(blank=True, null=True)
    oldcode = models.CharField(max_length=8, blank=True, null=True)
    soato = models.CharField(max_length=30, blank=True, null=True)
    okpo = models.CharField(max_length=10, blank=True, null=True)
    ogrn = models.CharField(max_length=15, blank=True, null=True)
    inn = models.CharField(max_length=12, blank=True, null=True)
    kpp = models.CharField(max_length=9, blank=True, null=True)
    namt = models.CharField(max_length=50, blank=True, null=True)
    name_all = models.CharField(max_length=255, blank=True, null=True)
    pstindex = models.CharField(max_length=6, blank=True, null=True)
    okato = models.CharField(max_length=5, blank=True, null=True)
    gorod = models.CharField(max_length=30, blank=True, null=True)
    adrtam = models.CharField(max_length=255, blank=True, null=True)
    prosf = models.CharField(max_length=2, blank=True, null=True)
    sign = models.CharField(max_length=10, blank=True, null=True)
    telefon = models.CharField(max_length=20, blank=True, null=True)
    fax = models.CharField(max_length=20, blank=True, null=True)
    teleks = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    rpsi = models.CharField(max_length=8, blank=True, null=True)
    sovam = models.CharField(max_length=8, blank=True, null=True)
    rsovam = models.CharField(max_length=8, blank=True, null=True)
    ustp = models.CharField(max_length=64, blank=True, null=True)
    adr_okdt = models.CharField(max_length=100, blank=True, null=True)
    ruk_okdt = models.CharField(max_length=50, blank=True, null=True)
    tel_okdt = models.CharField(max_length=20, blank=True, null=True)
    fax_okdt = models.CharField(max_length=20, blank=True, null=True)
    tx_okdt = models.CharField(max_length=20, blank=True, null=True)
    adr_dost = models.CharField(max_length=100, blank=True, null=True)
    tel_dost = models.CharField(max_length=20, blank=True, null=True)
    fax_dost = models.CharField(max_length=20, blank=True, null=True)
    tx_dost = models.CharField(max_length=20, blank=True, null=True)
    reg_dost = models.CharField(max_length=150, blank=True, null=True)
    trn_dost = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'ktam'


class Ktam1(BaseModel):
    code = models.CharField(max_length=8, blank=True, null=True)
    strana2 = models.CharField(max_length=2, blank=True, null=True)
    dbegin = models.DateField(blank=True, null=True)
    nprcreate = models.CharField(max_length=40, blank=True, null=True)
    dprcreate = models.DateField(blank=True, null=True)
    atrchange = models.CharField(max_length=1, blank=True, null=True)
    dend = models.DateField(blank=True, null=True)
    dendcust = models.DateField(blank=True, null=True)
    nprend = models.CharField(max_length=40, blank=True, null=True)
    dprend = models.DateField(blank=True, null=True)
    newcode = models.CharField(max_length=8, blank=True, null=True)
    kodt = models.CharField(max_length=5, blank=True, null=True)
    ttt = models.CharField(max_length=3, blank=True, null=True)
    owner = models.CharField(max_length=5, blank=True, null=True)
    kodzon = models.CharField(max_length=5, blank=True, null=True)
    kodtn = models.CharField(max_length=5, blank=True, null=True)
    datas = models.DateField(blank=True, null=True)
    oldcode = models.CharField(max_length=8, blank=True, null=True)
    soato = models.CharField(max_length=30, blank=True, null=True)
    okpo = models.CharField(max_length=10, blank=True, null=True)
    ogrn = models.CharField(max_length=15, blank=True, null=True)
    inn = models.CharField(max_length=12, blank=True, null=True)
    kpp = models.CharField(max_length=9, blank=True, null=True)
    namt = models.CharField(max_length=50, blank=True, null=True)
    name_all = models.CharField(max_length=255, blank=True, null=True)
    pstindex = models.CharField(max_length=6, blank=True, null=True)
    okato = models.CharField(max_length=5, blank=True, null=True)
    gorod = models.CharField(max_length=30, blank=True, null=True)
    adrtam = models.CharField(max_length=255, blank=True, null=True)
    prosf = models.CharField(max_length=2, blank=True, null=True)
    sign = models.CharField(max_length=10, blank=True, null=True)
    telefon = models.CharField(max_length=20, blank=True, null=True)
    fax = models.CharField(max_length=20, blank=True, null=True)
    teleks = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    rpsi = models.CharField(max_length=8, blank=True, null=True)
    sovam = models.CharField(max_length=8, blank=True, null=True)
    rsovam = models.CharField(max_length=8, blank=True, null=True)
    ustp = models.CharField(max_length=64, blank=True, null=True)
    adr_okdt = models.CharField(max_length=100, blank=True, null=True)
    ruk_okdt = models.CharField(max_length=50, blank=True, null=True)
    tel_okdt = models.CharField(max_length=20, blank=True, null=True)
    fax_okdt = models.CharField(max_length=20, blank=True, null=True)
    tx_okdt = models.CharField(max_length=20, blank=True, null=True)
    adr_dost = models.CharField(max_length=100, blank=True, null=True)
    tel_dost = models.CharField(max_length=20, blank=True, null=True)
    fax_dost = models.CharField(max_length=20, blank=True, null=True)
    tx_dost = models.CharField(max_length=20, blank=True, null=True)
    reg_dost = models.CharField(max_length=150, blank=True, null=True)
    trn_dost = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'ktam1'


class Ktam2(BaseModel):
    code = models.CharField(max_length=8, blank=True, null=True)
    dbegin = models.DateField(blank=True, null=True)
    nprcreate = models.CharField(max_length=40, blank=True, null=True)
    dprcreate = models.DateField(blank=True, null=True)
    atrchange = models.CharField(max_length=1, blank=True, null=True)
    dend = models.DateField(blank=True, null=True)
    dendcust = models.DateField(blank=True, null=True)
    nprend = models.CharField(max_length=40, blank=True, null=True)
    dprend = models.DateField(blank=True, null=True)
    newcode = models.CharField(max_length=8, blank=True, null=True)
    kodt = models.CharField(max_length=5, blank=True, null=True)
    ttt = models.CharField(max_length=3, blank=True, null=True)
    owner = models.CharField(max_length=5, blank=True, null=True)
    kodzon = models.CharField(max_length=5, blank=True, null=True)
    kodtn = models.CharField(max_length=5, blank=True, null=True)
    datas = models.DateField(blank=True, null=True)
    oldcode = models.CharField(max_length=8, blank=True, null=True)
    soato = models.CharField(max_length=30, blank=True, null=True)
    okpo = models.CharField(max_length=10, blank=True, null=True)
    ogrn = models.CharField(max_length=15, blank=True, null=True)
    inn = models.CharField(max_length=12, blank=True, null=True)
    kpp = models.CharField(max_length=9, blank=True, null=True)
    namt = models.CharField(max_length=50, blank=True, null=True)
    name_all = models.CharField(max_length=250, blank=True, null=True)
    pstindex = models.CharField(max_length=6, blank=True, null=True)
    okato = models.CharField(max_length=5, blank=True, null=True)
    gorod = models.CharField(max_length=30, blank=True, null=True)
    adrtam = models.CharField(max_length=75, blank=True, null=True)
    prosf = models.CharField(max_length=2, blank=True, null=True)
    sign = models.CharField(max_length=10, blank=True, null=True)
    telefon = models.CharField(max_length=20, blank=True, null=True)
    fax = models.CharField(max_length=20, blank=True, null=True)
    teleks = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    rpsi = models.CharField(max_length=8, blank=True, null=True)
    sovam = models.CharField(max_length=8, blank=True, null=True)
    rsovam = models.CharField(max_length=8, blank=True, null=True)
    adr_okdt = models.CharField(max_length=100, blank=True, null=True)
    ruk_okdt = models.CharField(max_length=50, blank=True, null=True)
    tel_okdt = models.CharField(max_length=20, blank=True, null=True)
    fax_okdt = models.CharField(max_length=20, blank=True, null=True)
    tx_okdt = models.CharField(max_length=20, blank=True, null=True)
    adr_dost = models.CharField(max_length=100, blank=True, null=True)
    tel_dost = models.CharField(max_length=20, blank=True, null=True)
    fax_dost = models.CharField(max_length=20, blank=True, null=True)
    tx_dost = models.CharField(max_length=20, blank=True, null=True)
    reg_dost = models.CharField(max_length=150, blank=True, null=True)
    trn_dost = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'ktam2'


class Ktamatr(BaseModel):
    code = models.CharField(max_length=1, blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'ktamatr'


class Ktamolap(BaseModel):
    child = models.CharField(max_length=8, blank=True, null=True)
    parent = models.CharField(max_length=8, blank=True, null=True)
    post_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'ktamolap'


class Ktamold(BaseModel):
    code = models.CharField(max_length=8, blank=True, null=True)
    strana2 = models.CharField(max_length=2, blank=True, null=True)
    dbegin = models.DateField(blank=True, null=True)
    nprcreate = models.CharField(max_length=40, blank=True, null=True)
    dprcreate = models.DateField(blank=True, null=True)
    atrchange = models.CharField(max_length=1, blank=True, null=True)
    dend = models.DateField(blank=True, null=True)
    dendcust = models.DateField(blank=True, null=True)
    nprend = models.CharField(max_length=40, blank=True, null=True)
    dprend = models.DateField(blank=True, null=True)
    newcode = models.CharField(max_length=8, blank=True, null=True)
    kodt = models.CharField(max_length=5, blank=True, null=True)
    ttt = models.CharField(max_length=3, blank=True, null=True)
    owner = models.CharField(max_length=5, blank=True, null=True)
    kodzon = models.CharField(max_length=5, blank=True, null=True)
    kodtn = models.CharField(max_length=5, blank=True, null=True)
    datas = models.DateField(blank=True, null=True)
    oldcode = models.CharField(max_length=8, blank=True, null=True)
    soato = models.CharField(max_length=30, blank=True, null=True)
    okpo = models.CharField(max_length=10, blank=True, null=True)
    ogrn = models.CharField(max_length=15, blank=True, null=True)
    inn = models.CharField(max_length=12, blank=True, null=True)
    kpp = models.CharField(max_length=9, blank=True, null=True)
    namt = models.CharField(max_length=50, blank=True, null=True)
    name_all = models.CharField(max_length=255, blank=True, null=True)
    pstindex = models.CharField(max_length=6, blank=True, null=True)
    okato = models.CharField(max_length=5, blank=True, null=True)
    gorod = models.CharField(max_length=30, blank=True, null=True)
    adrtam = models.CharField(max_length=255, blank=True, null=True)
    prosf = models.CharField(max_length=2, blank=True, null=True)
    sign = models.CharField(max_length=10, blank=True, null=True)
    telefon = models.CharField(max_length=20, blank=True, null=True)
    fax = models.CharField(max_length=20, blank=True, null=True)
    teleks = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    rpsi = models.CharField(max_length=8, blank=True, null=True)
    sovam = models.CharField(max_length=8, blank=True, null=True)
    rsovam = models.CharField(max_length=8, blank=True, null=True)
    ustp = models.CharField(max_length=64, blank=True, null=True)
    adr_okdt = models.CharField(max_length=100, blank=True, null=True)
    ruk_okdt = models.CharField(max_length=50, blank=True, null=True)
    tel_okdt = models.CharField(max_length=20, blank=True, null=True)
    fax_okdt = models.CharField(max_length=20, blank=True, null=True)
    tx_okdt = models.CharField(max_length=20, blank=True, null=True)
    adr_dost = models.CharField(max_length=100, blank=True, null=True)
    tel_dost = models.CharField(max_length=20, blank=True, null=True)
    fax_dost = models.CharField(max_length=20, blank=True, null=True)
    tx_dost = models.CharField(max_length=20, blank=True, null=True)
    reg_dost = models.CharField(max_length=150, blank=True, null=True)
    trn_dost = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'ktamold'


class Ktddl(BaseModel):
    lnpdl = models.CharField(max_length=4, blank=True, null=True)
    doldl = models.CharField(max_length=50, blank=True, null=True)
    fiodl = models.CharField(max_length=50, blank=True, null=True)
    teldl = models.CharField(max_length=20, blank=True, null=True)
    form = models.BooleanField(blank=True, null=True)
    sogl = models.BooleanField(blank=True, null=True)
    in_field = models.BooleanField(db_column='in', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    izm = models.BooleanField(blank=True, null=True)
    out = models.BooleanField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'ktddl'


class Kvota(BaseModel):
    okpo = models.CharField(max_length=10, blank=True, null=True)
    nomlic = models.CharField(max_length=17, blank=True, null=True)
    kod_tnved = models.CharField(max_length=10, blank=True, null=True)
    kol = models.DecimalField(default=0.00, max_digits=19, decimal_places=6, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'kvota'


class Kvz(BaseModel):
    v_vz = models.CharField(max_length=3, blank=True, null=True)
    n_vz = models.CharField(max_length=190, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'kvz'


class LgotUv(BaseModel):
    kod = models.CharField(max_length=1, blank=True, null=True)
    name = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'lgot_uv'


class LicTi(BaseModel):
    nomr3 = models.CharField(max_length=10, blank=True, null=True)
    nomlic = models.CharField(max_length=17, blank=True, null=True)
    ei = models.CharField(max_length=1, blank=True, null=True)
    prlic = models.CharField(max_length=1, blank=True, null=True)
    datr = models.DateField(blank=True, null=True)
    kodstrn = models.CharField(max_length=3, blank=True, null=True)
    kodstrp = models.CharField(max_length=3, blank=True, null=True)
    kodtam = models.CharField(max_length=62, blank=True, null=True)
    datlic = models.DateField(blank=True, null=True)
    datdol = models.DateField(blank=True, null=True)
    kodsdel = models.CharField(max_length=2, blank=True, null=True)
    kodval = models.CharField(max_length=3, blank=True, null=True)
    dopname = models.CharField(max_length=150, blank=True, null=True)
    datd = models.DateField(blank=True, null=True)
    sim = models.CharField(max_length=8, blank=True, null=True)
    tov = models.CharField(max_length=10, blank=True, null=True)
    kol = models.DecimalField(default=0.00, max_digits=19, decimal_places=6, blank=True, null=True)
    edi = models.CharField(max_length=3, blank=True, null=True)
    stoim = models.DecimalField(default=0.00, max_digits=15, decimal_places=3, blank=True, null=True)
    statst = models.DecimalField(default=0.00, max_digits=15, decimal_places=3, blank=True, null=True)
    kodvalpl = models.CharField(max_length=3, blank=True, null=True)
    ogrn = models.CharField(max_length=15, blank=True, null=True)
    inn = models.CharField(max_length=12, blank=True, null=True)
    kpp = models.CharField(max_length=9, blank=True, null=True)
    kontr = models.CharField(max_length=70, blank=True, null=True)
    koddoc = models.CharField(max_length=5, blank=True, null=True)
    kod_ktov = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'lic_ti'


class LicTov(BaseModel):
    code = models.CharField(max_length=3, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'lic_tov'


class LicTv(BaseModel):
    okpo = models.CharField(max_length=8, blank=True, null=True)
    nomlic = models.CharField(max_length=17, blank=True, null=True)
    tov = models.CharField(max_length=9, blank=True, null=True)
    kol = models.DecimalField(default=0.00, max_digits=19, decimal_places=6, blank=True, null=True)
    edi = models.CharField(max_length=3, blank=True, null=True)
    stoim = models.DecimalField(default=0.00, max_digits=15, decimal_places=3, blank=True, null=True)
    kodvalpl = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'lic_tv'


class LocKntr(BaseModel):
    caption = models.CharField(max_length=100, blank=True, null=True)
    usl_pr = models.CharField(max_length=850, blank=True, null=True)
    nmfile = models.CharField(max_length=70, blank=True, null=True)
    nmind = models.CharField(max_length=70, blank=True, null=True)
    kluch = models.CharField(max_length=250, blank=True, null=True)
    alias = models.CharField(max_length=10, blank=True, null=True)
    formula = models.CharField(max_length=850, blank=True, null=True)
    fwhile = models.CharField(max_length=850, blank=True, null=True)
    txt_osh = models.CharField(max_length=850, blank=True, null=True)
    koderr = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    ltstdobl = models.BooleanField(blank=True, null=True)
    grafa = models.CharField(max_length=250, blank=True, null=True)
    fldname = models.CharField(max_length=250, blank=True, null=True)
    verno = models.CharField(max_length=250, blank=True, null=True)
    driver = models.CharField(max_length=10, blank=True, null=True)
    tag = models.CharField(max_length=10, blank=True, null=True)
    err_step = models.CharField(max_length=10, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    tmodify = models.CharField(max_length=8, blank=True, null=True)
    mode = models.CharField(max_length=2, blank=True, null=True)
    preblock = models.CharField(max_length=250, blank=True, null=True)
    postblock = models.CharField(max_length=250, blank=True, null=True)
    lsp = models.BooleanField(blank=True, null=True)
    def_lvl = models.BooleanField(blank=True, null=True)
    code = models.CharField(max_length=250, blank=True, null=True)
    disable = models.BooleanField(blank=True, null=True)
    msgid = models.CharField(max_length=850, blank=True, null=True)
    gtdalias = models.CharField(max_length=15, blank=True, null=True)
    gtdobj = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'loc_kntr'


class LostTir(BaseModel):
    n_mdp = models.CharField(max_length=10, blank=True, null=True)
    d_mdp = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'lost_tir'


class MarAkc(BaseModel):
    kod = models.CharField(max_length=1, blank=True, null=True)
    naim = models.CharField(max_length=210, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'mar_akc'


class Maxstakc(BaseModel):
    mst_ak = models.DecimalField(default=0.00, max_digits=10, decimal_places=3, blank=True, null=True)
    npric = models.CharField(max_length=20, blank=True, null=True)
    dpric = models.DateField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    data1 = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'maxstakc'


class MdpAdr(BaseModel):
    checkcod = models.CharField(max_length=18, blank=True, null=True)
    kod_dmdp = models.CharField(max_length=6, blank=True, null=True)
    tip_adr = models.CharField(max_length=1, blank=True, null=True)
    kod_post = models.CharField(max_length=15, blank=True, null=True)
    ind_post = models.CharField(max_length=15, blank=True, null=True)
    town = models.CharField(max_length=50, blank=True, null=True)
    street = models.CharField(max_length=50, blank=True, null=True)
    nom_hous = models.CharField(max_length=15, blank=True, null=True)
    postbox = models.CharField(max_length=15, blank=True, null=True)
    nom_off = models.CharField(max_length=15, blank=True, null=True)
    datmod = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'mdp_adr'


class MdpD(BaseModel):
    checkcod = models.CharField(max_length=18, blank=True, null=True)
    kod_dmdp = models.CharField(max_length=6, blank=True, null=True)
    kod = models.CharField(max_length=3, blank=True, null=True)
    kodassoc = models.CharField(max_length=4, blank=True, null=True)
    namassoc = models.CharField(max_length=100, blank=True, null=True)
    nam_carr = models.CharField(max_length=80, blank=True, null=True)
    inn = models.CharField(max_length=30, blank=True, null=True)
    dat_dop = models.DateField(blank=True, null=True)
    dat_iz = models.DateField(blank=True, null=True)
    pr_nac = models.CharField(max_length=1, blank=True, null=True)
    pr_ins = models.CharField(max_length=1, blank=True, null=True)
    pr_dop = models.CharField(max_length=1, blank=True, null=True)
    kol_tss = models.DecimalField(default=0.00, max_digits=3, decimal_places=0, blank=True, null=True)
    kol_tsa = models.DecimalField(default=0.00, max_digits=3, decimal_places=0, blank=True, null=True)
    datmod = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'mdp_d'


class MdpKont(BaseModel):
    checkcod = models.CharField(max_length=18, blank=True, null=True)
    kod_dmdp = models.CharField(max_length=6, blank=True, null=True)
    vid_lic = models.CharField(max_length=1, blank=True, null=True)
    l_name = models.CharField(max_length=20, blank=True, null=True)
    f_name = models.CharField(max_length=15, blank=True, null=True)
    m_name = models.CharField(max_length=15, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    kodphone = models.CharField(max_length=5, blank=True, null=True)
    fax = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=20, blank=True, null=True)
    datmod = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'mdp_kont'


class Measures(BaseModel):
    code = models.CharField(max_length=2, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    sign = models.CharField(max_length=1, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)
    pr_rb = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    pr_rk = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    pr_rf = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    pr_am = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    pr_kg = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'measures'


class Mintnv(BaseModel):
    kodg = models.CharField(max_length=4, blank=True, null=True)
    st_poshl = models.DecimalField(default=0.00, max_digits=10, decimal_places=3, blank=True, null=True)
    tstposhl = models.CharField(max_length=1, blank=True, null=True)
    ediposhl = models.CharField(max_length=3, blank=True, null=True)
    st_ndc = models.DecimalField(default=0.00, max_digits=10, decimal_places=3, blank=True, null=True)
    tstndc = models.CharField(max_length=1, blank=True, null=True)
    edindc = models.CharField(max_length=3, blank=True, null=True)
    st_akciz = models.DecimalField(default=0.00, max_digits=10, decimal_places=3, blank=True, null=True)
    tstakciz = models.CharField(max_length=1, blank=True, null=True)
    ediakciz = models.CharField(max_length=3, blank=True, null=True)
    st_spnal = models.DecimalField(default=0.00, max_digits=10, decimal_places=3, blank=True, null=True)
    tstspnal = models.CharField(max_length=1, blank=True, null=True)
    edispnal = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'mintnv'


class Mnt(BaseModel):
    kod = models.CharField(max_length=2, blank=True, null=True)
    naim = models.TextField(blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)
    pr_rb = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    pr_rk = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    pr_rf = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    pr_am = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    pr_kg = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'mnt'


class MosKtam(BaseModel):
    kodt = models.CharField(max_length=5, blank=True, null=True)
    namt = models.CharField(max_length=50, blank=True, null=True)
    kodzon = models.CharField(max_length=5, blank=True, null=True)
    adrtam = models.CharField(max_length=75, blank=True, null=True)
    gorod = models.CharField(max_length=30, blank=True, null=True)
    fax = models.CharField(max_length=20, blank=True, null=True)
    teleks = models.CharField(max_length=20, blank=True, null=True)
    telefon = models.CharField(max_length=20, blank=True, null=True)
    datas = models.DateField(blank=True, null=True)
    kodtn = models.CharField(max_length=5, blank=True, null=True)
    rpsi = models.CharField(max_length=5, blank=True, null=True)
    adr_okdt = models.CharField(max_length=100, blank=True, null=True)
    tel_okdt = models.CharField(max_length=20, blank=True, null=True)
    fax_okdt = models.CharField(max_length=20, blank=True, null=True)
    tx_okdt = models.CharField(max_length=20, blank=True, null=True)
    ruk_okdt = models.CharField(max_length=50, blank=True, null=True)
    adr_dost = models.CharField(max_length=100, blank=True, null=True)
    reg_dost = models.CharField(max_length=150, blank=True, null=True)
    trn_dost = models.CharField(max_length=25, blank=True, null=True)
    tel_dost = models.CharField(max_length=20, blank=True, null=True)
    fax_dost = models.CharField(max_length=20, blank=True, null=True)
    tx_dost = models.CharField(max_length=20, blank=True, null=True)
    sovam = models.CharField(max_length=8, blank=True, null=True)
    owner = models.CharField(max_length=5, blank=True, null=True)
    sign = models.CharField(max_length=10, blank=True, null=True)
    soato = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'mos_ktam'


class Motc(BaseModel):
    code = models.CharField(max_length=2, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'motc'


class Motsfl(BaseModel):
    kodt = models.CharField(max_length=8, blank=True, null=True)
    dat_vvod = models.DateField(blank=True, null=True)
    dat_otmn = models.DateField(blank=True, null=True)
    doc_vvod = models.CharField(max_length=50, blank=True, null=True)
    doc_otmn = models.CharField(max_length=50, blank=True, null=True)
    e_adres = models.CharField(max_length=10, blank=True, null=True)
    reserv = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'motsfl'


class Mps(BaseModel):
    kodstan = models.CharField(max_length=5, blank=True, null=True)
    naimstan = models.CharField(max_length=24, blank=True, null=True)
    koddor = models.CharField(max_length=2, blank=True, null=True)
    naimdor = models.CharField(max_length=21, blank=True, null=True)
    kodtam = models.CharField(max_length=8, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'mps'


class Mpsreg(BaseModel):
    kodstan = models.CharField(max_length=5, blank=True, null=True)
    kodtam = models.CharField(max_length=8, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    datp = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'mpsreg'


class MrkCar(BaseModel):
    kodmrk = models.CharField(max_length=3, blank=True, null=True)
    namemrkcar = models.CharField(max_length=20, blank=True, null=True)
    namemrkrus = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)
    reserv = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'mrk_car'


class MrkCars(BaseModel):
    kodmrk = models.CharField(max_length=3, blank=True, null=True)
    namemrkcar = models.CharField(max_length=100, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'mrk_cars'


class Namefirm(BaseModel):
    regn = models.CharField(max_length=3, blank=True, null=True)
    regnold = models.CharField(max_length=2, blank=True, null=True)
    naim = models.CharField(max_length=99, blank=True, null=True)
    dated = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'namefirm'


class Nar(BaseModel):
    prnar = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    nar = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'nar'


class NarVtt(BaseModel):
    nomr1 = models.CharField(max_length=2, blank=True, null=True)
    nomr2 = models.CharField(max_length=4, blank=True, null=True)
    nomr3 = models.CharField(max_length=10, blank=True, null=True)
    psu = models.CharField(max_length=1, blank=True, null=True)
    okato = models.CharField(max_length=5, blank=True, null=True)
    ogrn = models.CharField(max_length=15, blank=True, null=True)
    inn = models.CharField(max_length=12, blank=True, null=True)
    kpp = models.CharField(max_length=9, blank=True, null=True)
    zayv = models.CharField(max_length=80, blank=True, null=True)
    adress = models.CharField(max_length=80, blank=True, null=True)
    telefon = models.CharField(max_length=12, blank=True, null=True)
    telefax = models.CharField(max_length=12, blank=True, null=True)
    telex = models.CharField(max_length=20, blank=True, null=True)
    datr = models.DateField(blank=True, null=True)
    kodtam = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'nar_vtt'


class NewTi(BaseModel):
    nomr3 = models.CharField(max_length=8, blank=True, null=True)
    nomlic = models.CharField(max_length=17, blank=True, null=True)
    ei = models.CharField(max_length=1, blank=True, null=True)
    prlic = models.CharField(max_length=1, blank=True, null=True)
    datr = models.DateField(blank=True, null=True)
    kodstrn = models.CharField(max_length=3, blank=True, null=True)
    kodstrp = models.CharField(max_length=3, blank=True, null=True)
    kodtam = models.CharField(max_length=41, blank=True, null=True)
    datlic = models.DateField(blank=True, null=True)
    datdol = models.DateField(blank=True, null=True)
    kodsdel = models.CharField(max_length=2, blank=True, null=True)
    kodval = models.CharField(max_length=3, blank=True, null=True)
    dopname = models.CharField(max_length=150, blank=True, null=True)
    datd = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'new_ti'


class Nlstmpr(BaseModel):
    reason = models.CharField(max_length=2, blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'nlstmpr'


class Npech(BaseModel):
    ktam = models.CharField(max_length=8, blank=True, null=True)
    num_lnp = models.CharField(max_length=4, blank=True, null=True)
    ktam_pch = models.CharField(max_length=8, blank=True, null=True)
    namt = models.CharField(max_length=50, blank=True, null=True)
    fio = models.CharField(max_length=40, blank=True, null=True)
    data_iz = models.DateField(blank=True, null=True)
    date_mod = models.DateField(blank=True, null=True)
    pr_izjat = models.CharField(max_length=20, blank=True, null=True)
    data_vv = models.DateField(blank=True, null=True)
    pr_vvod = models.CharField(max_length=25, blank=True, null=True)
    pr_vivod = models.CharField(max_length=25, blank=True, null=True)
    prikaz48 = models.CharField(max_length=1, blank=True, null=True)
    s1 = models.CharField(max_length=8, blank=True, null=True)
    s2 = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'npech'


class NprsSbj(BaseModel):
    sbj_id = models.DecimalField(default=0.00, max_digits=15, decimal_places=0, blank=True, null=True)
    kod_spdr = models.CharField(max_length=2, blank=True, null=True)
    kod_ndpd = models.CharField(max_length=2, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'nprs_sbj'


class NsDolgn(BaseModel):
    ogrn = models.CharField(max_length=15, blank=True, null=True)
    inn = models.CharField(max_length=12, blank=True, null=True)
    kpp = models.CharField(max_length=9, blank=True, null=True)
    okpo = models.CharField(max_length=10, blank=True, null=True)
    naim = models.TextField(blank=True, null=True)
    adr = models.CharField(max_length=255, blank=True, null=True)
    periodotch = models.CharField(max_length=1, blank=True, null=True)
    dateotch = models.CharField(max_length=8, blank=True, null=True)
    priznakotc = models.CharField(max_length=23, blank=True, null=True)
    datnalotch = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'ns_dolgn'


class NsDul(BaseModel):
    strana = models.CharField(max_length=2, blank=True, null=True)
    kod = models.CharField(max_length=2, blank=True, null=True)
    kod_v = models.CharField(max_length=3, blank=True, null=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    abbrev = models.CharField(max_length=6, blank=True, null=True)
    series = models.CharField(max_length=11, blank=True, null=True)
    number1 = models.CharField(max_length=25, blank=True, null=True)
    comment1 = models.CharField(max_length=120, blank=True, null=True)
    priznak = models.CharField(max_length=10, blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'ns_dul'


class NsDulT(BaseModel):
    kod = models.CharField(max_length=2, blank=True, null=True)
    name = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'ns_dul_t'


class NsDulV(BaseModel):
    kod_v = models.CharField(max_length=3, blank=True, null=True)
    name = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'ns_dul_v'


class NsGr31(BaseModel):
    kodt1 = models.CharField(max_length=10, blank=True, null=True)
    kodt2 = models.CharField(max_length=10, blank=True, null=True)
    kodtiskl = models.CharField(max_length=10, blank=True, null=True)
    nametov = models.TextField(blank=True, null=True)
    ntov_g31 = models.TextField(blank=True, null=True)
    regim = models.CharField(max_length=2, blank=True, null=True)
    doc_vvod = models.CharField(max_length=50, blank=True, null=True)
    dat_vvod = models.DateField(blank=True, null=True)
    doc_viv = models.CharField(max_length=50, blank=True, null=True)
    dat_viv = models.DateField(blank=True, null=True)
    dbegin = models.DateField(blank=True, null=True)
    dend = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'ns_gr31'


class NsMpo(BaseModel):
    code1 = models.CharField(max_length=8, blank=True, null=True)
    naimt1 = models.CharField(max_length=100, blank=True, null=True)
    code2 = models.CharField(max_length=8, blank=True, null=True)
    naimt2 = models.CharField(max_length=100, blank=True, null=True)
    naim_po = models.CharField(max_length=100, blank=True, null=True)
    priznak = models.CharField(max_length=2, blank=True, null=True)
    adr = models.CharField(max_length=100, blank=True, null=True)
    telefon = models.CharField(max_length=30, blank=True, null=True)
    npric = models.CharField(max_length=20, blank=True, null=True)
    dpric = models.DateField(blank=True, null=True)
    dbegin = models.DateField(blank=True, null=True)
    dend = models.DateField(blank=True, null=True)
    reserv1 = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'ns_mpo'


class NsOd31(BaseModel):
    kodt = models.CharField(max_length=10, blank=True, null=True)
    kodiskl = models.CharField(max_length=250, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'ns_od31'


class NsTsfl(BaseModel):
    naim_reg = models.TextField(blank=True, null=True)
    naimto = models.CharField(max_length=250, blank=True, null=True)
    code = models.CharField(max_length=8, blank=True, null=True)
    adr = models.CharField(max_length=100, blank=True, null=True)
    doc_vvod = models.CharField(max_length=50, blank=True, null=True)
    dat_vvod = models.DateField(blank=True, null=True)
    doc_viv = models.CharField(max_length=50, blank=True, null=True)
    dat_viv = models.DateField(blank=True, null=True)
    dbegin = models.DateField(blank=True, null=True)
    dend = models.DateField(blank=True, null=True)
    priznak = models.CharField(max_length=1, blank=True, null=True)
    reserv1 = models.CharField(max_length=10, blank=True, null=True)
    reserv2 = models.CharField(max_length=10, blank=True, null=True)
    reserv3 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'ns_tsfl'


class NsiKbk(BaseModel):
    kbk = models.CharField(max_length=20, blank=True, null=True)
    advance = models.CharField(max_length=1, blank=True, null=True)
    pay_code = models.CharField(max_length=6, blank=True, null=True)
    begin_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    b_doc_num = models.CharField(max_length=30, blank=True, null=True)
    b_doc_date = models.DateField(blank=True, null=True)
    e_doc_num = models.CharField(max_length=30, blank=True, null=True)
    e_doc_date = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'nsi_kbk'


class NullstB(BaseModel):
    custom = models.CharField(max_length=2, blank=True, null=True)
    pechvid = models.CharField(max_length=1, blank=True, null=True)
    pechtype = models.CharField(max_length=2, blank=True, null=True)
    pechnumber = models.CharField(max_length=4, blank=True, null=True)
    litera = models.CharField(max_length=2, blank=True, null=True)
    datereg = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    dateannul = models.DateField(blank=True, null=True)
    reasonann = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'nullst_b'


class O803(BaseModel):
    name = models.CharField(max_length=200, blank=True, null=True)
    kodt = models.CharField(max_length=8, blank=True, null=True)
    address = models.CharField(max_length=120, blank=True, null=True)
    name_cbx = models.CharField(max_length=120, blank=True, null=True)
    nlic = models.CharField(max_length=12, blank=True, null=True)
    pr_per = models.CharField(max_length=1, blank=True, null=True)
    dend = models.DateField(blank=True, null=True)
    basekodt = models.CharField(max_length=8, blank=True, null=True)
    outkodt = models.CharField(max_length=8, blank=True, null=True)
    drecenter = models.DateField(blank=True, null=True)
    drecend = models.DateField(blank=True, null=True)
    sign = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'o803'


class Object0(BaseModel):
    kodt = models.CharField(max_length=8, blank=True, null=True)
    namt = models.CharField(max_length=50, blank=True, null=True)
    sam = models.CharField(max_length=1, blank=True, null=True)
    kod_sam = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'object'


class Ofdoc(BaseModel):
    kod = models.CharField(max_length=2, blank=True, null=True)
    naim = models.CharField(max_length=240, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'ofdoc'


class Ogovorka(BaseModel):
    code = models.CharField(max_length=2, blank=True, null=True)
    meaning = models.CharField(max_length=60, blank=True, null=True)
    meaning1 = models.CharField(max_length=90, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'ogovorka'


class OkaPk38(BaseModel):
    ter = models.CharField(max_length=3, blank=True, null=True)
    kod1 = models.CharField(max_length=3, blank=True, null=True)
    kod2 = models.CharField(max_length=3, blank=True, null=True)
    kod3 = models.CharField(max_length=3, blank=True, null=True)
    razdel = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    name1 = models.CharField(max_length=150, blank=True, null=True)
    centrum = models.CharField(max_length=80, blank=True, null=True)
    oldkod = models.CharField(max_length=11, blank=True, null=True)
    oldname1 = models.CharField(max_length=150, blank=True, null=True)
    oldcentrum = models.CharField(max_length=80, blank=True, null=True)
    nomakt = models.DecimalField(default=0.00, max_digits=3, decimal_places=0, blank=True, null=True)
    typeakt = models.CharField(max_length=2, blank=True, null=True)
    datakt = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'oka-pk38'


class OkaPk44(BaseModel):
    ter = models.CharField(max_length=3, blank=True, null=True)
    kod1 = models.CharField(max_length=3, blank=True, null=True)
    kod2 = models.CharField(max_length=3, blank=True, null=True)
    kod3 = models.CharField(max_length=3, blank=True, null=True)
    razdel = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    name1 = models.CharField(max_length=150, blank=True, null=True)
    centrum = models.CharField(max_length=80, blank=True, null=True)
    oldkod = models.CharField(max_length=11, blank=True, null=True)
    oldname1 = models.CharField(max_length=150, blank=True, null=True)
    oldcentrum = models.CharField(max_length=80, blank=True, null=True)
    nomakt = models.DecimalField(default=0.00, max_digits=3, decimal_places=0, blank=True, null=True)
    typeakt = models.CharField(max_length=2, blank=True, null=True)
    datakt = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'oka-pk44'


class OkaPk48(BaseModel):
    ter = models.CharField(max_length=3, blank=True, null=True)
    kod1 = models.CharField(max_length=3, blank=True, null=True)
    kod2 = models.CharField(max_length=3, blank=True, null=True)
    kod3 = models.CharField(max_length=3, blank=True, null=True)
    razdel = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    name1 = models.CharField(max_length=150, blank=True, null=True)
    centrum = models.CharField(max_length=80, blank=True, null=True)
    oldkod = models.CharField(max_length=11, blank=True, null=True)
    oldname1 = models.CharField(max_length=150, blank=True, null=True)
    oldcentrum = models.CharField(max_length=80, blank=True, null=True)
    nomakt = models.DecimalField(default=0.00, max_digits=3, decimal_places=0, blank=True, null=True)
    typeakt = models.CharField(max_length=2, blank=True, null=True)
    datakt = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'oka-pk48'


class OkaPk65(BaseModel):
    ter = models.CharField(max_length=3, blank=True, null=True)
    kod1 = models.CharField(max_length=3, blank=True, null=True)
    kod2 = models.CharField(max_length=3, blank=True, null=True)
    kod3 = models.CharField(max_length=3, blank=True, null=True)
    razdel = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    name1 = models.CharField(max_length=200, blank=True, null=True)
    centrum = models.CharField(max_length=80, blank=True, null=True)
    nomakt = models.DecimalField(default=0.00, max_digits=3, decimal_places=0, blank=True, null=True)
    typeakt = models.CharField(max_length=2, blank=True, null=True)
    datakt = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'oka-pk65'


class OkaPk66(BaseModel):
    ter = models.CharField(max_length=3, blank=True, null=True)
    kod1 = models.CharField(max_length=3, blank=True, null=True)
    kod2 = models.CharField(max_length=3, blank=True, null=True)
    kod3 = models.CharField(max_length=3, blank=True, null=True)
    razdel = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    name1 = models.CharField(max_length=200, blank=True, null=True)
    centrum = models.CharField(max_length=80, blank=True, null=True)
    nomakt = models.DecimalField(default=0.00, max_digits=3, decimal_places=0, blank=True, null=True)
    typeakt = models.CharField(max_length=2, blank=True, null=True)
    datakt = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'oka-pk66'


class OkaPk72(BaseModel):
    ter = models.CharField(max_length=3, blank=True, null=True)
    kod1 = models.CharField(max_length=3, blank=True, null=True)
    kod2 = models.CharField(max_length=3, blank=True, null=True)
    kod3 = models.CharField(max_length=3, blank=True, null=True)
    razdel = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    name1 = models.CharField(max_length=200, blank=True, null=True)
    centrum = models.CharField(max_length=80, blank=True, null=True)
    nomakt = models.DecimalField(default=0.00, max_digits=3, decimal_places=0, blank=True, null=True)
    typeakt = models.CharField(max_length=2, blank=True, null=True)
    datakt = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'oka-pk72'


class OkaPk75(BaseModel):
    ter = models.CharField(max_length=3, blank=True, null=True)
    kod1 = models.CharField(max_length=3, blank=True, null=True)
    kod2 = models.CharField(max_length=3, blank=True, null=True)
    kod3 = models.CharField(max_length=3, blank=True, null=True)
    razdel = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    name1 = models.CharField(max_length=200, blank=True, null=True)
    centrum = models.CharField(max_length=80, blank=True, null=True)
    nomakt = models.DecimalField(default=0.00, max_digits=3, decimal_places=0, blank=True, null=True)
    typeakt = models.CharField(max_length=2, blank=True, null=True)
    datakt = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'oka-pk75'


class OkaPk76(BaseModel):
    ter = models.CharField(max_length=3, blank=True, null=True)
    kod1 = models.CharField(max_length=3, blank=True, null=True)
    kod2 = models.CharField(max_length=3, blank=True, null=True)
    kod3 = models.CharField(max_length=3, blank=True, null=True)
    razdel = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    name1 = models.CharField(max_length=200, blank=True, null=True)
    centrum = models.CharField(max_length=80, blank=True, null=True)
    nomakt = models.DecimalField(default=0.00, max_digits=3, decimal_places=0, blank=True, null=True)
    typeakt = models.CharField(max_length=2, blank=True, null=True)
    datakt = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'oka-pk76'


class OkaPk79(BaseModel):
    ter = models.CharField(max_length=3, blank=True, null=True)
    kod1 = models.CharField(max_length=3, blank=True, null=True)
    kod2 = models.CharField(max_length=3, blank=True, null=True)
    kod3 = models.CharField(max_length=3, blank=True, null=True)
    razdel = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    name1 = models.CharField(max_length=200, blank=True, null=True)
    centrum = models.CharField(max_length=80, blank=True, null=True)
    nomakt = models.DecimalField(default=0.00, max_digits=3, decimal_places=0, blank=True, null=True)
    typeakt = models.CharField(max_length=2, blank=True, null=True)
    datakt = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'oka-pk79'


class OkaPk82(BaseModel):
    ter = models.CharField(max_length=2, blank=True, null=True)
    kod1 = models.CharField(max_length=3, blank=True, null=True)
    kod2 = models.CharField(max_length=3, blank=True, null=True)
    kod3 = models.CharField(max_length=3, blank=True, null=True)
    razdel = models.CharField(max_length=1, blank=True, null=True)
    name1 = models.CharField(max_length=150, blank=True, null=True)
    centrum = models.CharField(max_length=80, blank=True, null=True)
    nomdescr = models.CharField(max_length=250, blank=True, null=True)
    nomakt = models.CharField(max_length=3, blank=True, null=True)
    status = models.DecimalField(default=0.00, max_digits=20, decimal_places=5, blank=True, null=True)
    data_upd = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'oka_pk82'


class OkaPk83(BaseModel):
    ter = models.CharField(max_length=2, blank=True, null=True)
    kod1 = models.CharField(max_length=3, blank=True, null=True)
    kod2 = models.CharField(max_length=3, blank=True, null=True)
    kod3 = models.CharField(max_length=3, blank=True, null=True)
    razdel = models.CharField(max_length=1, blank=True, null=True)
    name1 = models.CharField(max_length=150, blank=True, null=True)
    centrum = models.CharField(max_length=80, blank=True, null=True)
    nomdescr = models.CharField(max_length=250, blank=True, null=True)
    nomakt = models.CharField(max_length=3, blank=True, null=True)
    status = models.DecimalField(default=0.00, max_digits=20, decimal_places=5, blank=True, null=True)
    data_upd = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'oka_pk83'


class OkaPk84(BaseModel):
    ter = models.CharField(max_length=2, blank=True, null=True)
    kod1 = models.CharField(max_length=3, blank=True, null=True)
    kod2 = models.CharField(max_length=3, blank=True, null=True)
    kod3 = models.CharField(max_length=3, blank=True, null=True)
    razdel = models.CharField(max_length=1, blank=True, null=True)
    name1 = models.CharField(max_length=150, blank=True, null=True)
    centrum = models.CharField(max_length=80, blank=True, null=True)
    nomdescr = models.CharField(max_length=250, blank=True, null=True)
    nomakt = models.CharField(max_length=3, blank=True, null=True)
    status = models.DecimalField(default=0.00, max_digits=20, decimal_places=5, blank=True, null=True)
    data_upd = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'oka_pk84'


class OkaPk85(BaseModel):
    ter = models.CharField(max_length=2, blank=True, null=True)
    kod1 = models.CharField(max_length=3, blank=True, null=True)
    kod2 = models.CharField(max_length=3, blank=True, null=True)
    kod3 = models.CharField(max_length=3, blank=True, null=True)
    razdel = models.CharField(max_length=1, blank=True, null=True)
    name1 = models.CharField(max_length=150, blank=True, null=True)
    centrum = models.CharField(max_length=80, blank=True, null=True)
    nomdescr = models.CharField(max_length=250, blank=True, null=True)
    nomakt = models.CharField(max_length=3, blank=True, null=True)
    status = models.DecimalField(default=0.00, max_digits=20, decimal_places=5, blank=True, null=True)
    data_upd = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'oka_pk85'


class OkaPk86(BaseModel):
    ter = models.CharField(max_length=2, blank=True, null=True)
    kod1 = models.CharField(max_length=3, blank=True, null=True)
    kod2 = models.CharField(max_length=3, blank=True, null=True)
    kod3 = models.CharField(max_length=3, blank=True, null=True)
    razdel = models.CharField(max_length=1, blank=True, null=True)
    name1 = models.CharField(max_length=150, blank=True, null=True)
    centrum = models.CharField(max_length=80, blank=True, null=True)
    nomdescr = models.CharField(max_length=250, blank=True, null=True)
    nomakt = models.CharField(max_length=3, blank=True, null=True)
    status = models.DecimalField(default=0.00, max_digits=20, decimal_places=5, blank=True, null=True)
    data_upd = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'oka_pk86'


class OkaPk87(BaseModel):
    ter = models.CharField(max_length=2, blank=True, null=True)
    kod1 = models.CharField(max_length=3, blank=True, null=True)
    kod2 = models.CharField(max_length=3, blank=True, null=True)
    kod3 = models.CharField(max_length=3, blank=True, null=True)
    razdel = models.CharField(max_length=1, blank=True, null=True)
    name1 = models.CharField(max_length=150, blank=True, null=True)
    centrum = models.CharField(max_length=80, blank=True, null=True)
    nomdescr = models.CharField(max_length=250, blank=True, null=True)
    nomakt = models.CharField(max_length=3, blank=True, null=True)
    status = models.DecimalField(default=0.00, max_digits=20, decimal_places=5, blank=True, null=True)
    data_upd = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'oka_pk87'


class OkaPk88(BaseModel):
    ter = models.CharField(max_length=2, blank=True, null=True)
    kod1 = models.CharField(max_length=3, blank=True, null=True)
    kod2 = models.CharField(max_length=3, blank=True, null=True)
    kod3 = models.CharField(max_length=3, blank=True, null=True)
    razdel = models.CharField(max_length=1, blank=True, null=True)
    name1 = models.CharField(max_length=150, blank=True, null=True)
    centrum = models.CharField(max_length=80, blank=True, null=True)
    nomdescr = models.CharField(max_length=250, blank=True, null=True)
    nomakt = models.CharField(max_length=3, blank=True, null=True)
    status = models.DecimalField(default=0.00, max_digits=20, decimal_places=5, blank=True, null=True)
    data_upd = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'oka_pk88'


class OkaPk89(BaseModel):
    ter = models.CharField(max_length=2, blank=True, null=True)
    kod1 = models.CharField(max_length=3, blank=True, null=True)
    kod2 = models.CharField(max_length=3, blank=True, null=True)
    kod3 = models.CharField(max_length=3, blank=True, null=True)
    razdel = models.CharField(max_length=1, blank=True, null=True)
    name1 = models.CharField(max_length=150, blank=True, null=True)
    centrum = models.CharField(max_length=80, blank=True, null=True)
    nomdescr = models.CharField(max_length=250, blank=True, null=True)
    nomakt = models.CharField(max_length=3, blank=True, null=True)
    status = models.DecimalField(default=0.00, max_digits=20, decimal_places=5, blank=True, null=True)
    data_upd = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'oka_pk89'


class Okato(BaseModel):
    ter = models.CharField(max_length=2, blank=True, null=True)
    kod1 = models.CharField(max_length=3, blank=True, null=True)
    kod2 = models.CharField(max_length=3, blank=True, null=True)
    kod3 = models.CharField(max_length=3, blank=True, null=True)
    razdel = models.CharField(max_length=1, blank=True, null=True)
    name1 = models.CharField(max_length=250, blank=True, null=True)
    centrum = models.CharField(max_length=80, blank=True, null=True)
    nomdescr = models.CharField(max_length=250, blank=True, null=True)
    nomakt = models.DecimalField(default=0.00, max_digits=20, decimal_places=5, blank=True, null=True)
    status = models.DecimalField(default=0.00, max_digits=20, decimal_places=5, blank=True, null=True)
    dateutv = models.DateField(blank=True, null=True)
    datevved = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'okato'


class Okatosrf(BaseModel):
    kodsrf = models.CharField(max_length=2, blank=True, null=True)
    ter_okato = models.CharField(max_length=5, blank=True, null=True)
    name_ter = models.CharField(max_length=250, blank=True, null=True)
    dbegin = models.DateField(blank=True, null=True)
    doc_vvod = models.CharField(max_length=20, blank=True, null=True)
    dat_vvod = models.DateField(blank=True, null=True)
    dend = models.DateField(blank=True, null=True)
    doc_viv = models.CharField(max_length=20, blank=True, null=True)
    dat_viv = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'okatosrf'


class Oksmt(BaseModel):
    kod = models.CharField(max_length=3, blank=True, null=True)
    abc2 = models.CharField(max_length=2, blank=True, null=True)
    abc3 = models.CharField(max_length=3, blank=True, null=True)
    anaim = models.CharField(max_length=100, blank=True, null=True)
    krnaim = models.CharField(max_length=40, blank=True, null=True)
    naim = models.CharField(max_length=250, blank=True, null=True)
    pr_str = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    pr_lic = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    pr_regio = models.CharField(max_length=2, blank=True, null=True)
    kod_ar = models.CharField(max_length=50, blank=True, null=True)
    reserv = models.CharField(max_length=10, blank=True, null=True)
    date_mod = models.DateField(blank=True, null=True)
    date_nil = models.DateField(blank=True, null=True)
    ata = models.CharField(max_length=1, blank=True, null=True)
    tpp = models.CharField(max_length=250, blank=True, null=True)
    b1 = models.CharField(max_length=1, blank=True, null=True)
    b2 = models.CharField(max_length=1, blank=True, null=True)
    b3 = models.CharField(max_length=1, blank=True, null=True)
    b5 = models.CharField(max_length=1, blank=True, null=True)
    numbegdoc = models.CharField(max_length=50, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'oksmt'


class OprMeas(BaseModel):
    code = models.CharField(max_length=6, blank=True, null=True)
    naim = models.CharField(max_length=255, blank=True, null=True)
    mera = models.CharField(max_length=2, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'opr_meas'


class OrgNpr(BaseModel):
    code = models.CharField(max_length=8, blank=True, null=True)
    ntam = models.CharField(max_length=255, blank=True, null=True)
    inn = models.CharField(max_length=12, blank=True, null=True)
    kpp = models.CharField(max_length=9, blank=True, null=True)
    nved = models.CharField(max_length=255, blank=True, null=True)
    dbegin_t = models.DateField(blank=True, null=True)
    nresh = models.CharField(max_length=55, blank=True, null=True)
    osnov1 = models.CharField(max_length=1, blank=True, null=True)
    osnov2 = models.CharField(max_length=1, blank=True, null=True)
    osnov3 = models.CharField(max_length=1, blank=True, null=True)
    doprisn = models.CharField(max_length=1, blank=True, null=True)
    ustranp = models.CharField(max_length=1, blank=True, null=True)
    dustranp = models.DateField(blank=True, null=True)
    uslov = models.CharField(max_length=1, blank=True, null=True)
    dbegin_f = models.DateField(blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'org_npr'


class Ortov(BaseModel):
    kod = models.CharField(max_length=1, blank=True, null=True)
    naim = models.CharField(max_length=150, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'ortov'


class Osdelka(BaseModel):
    kod = models.CharField(max_length=2, blank=True, null=True)
    naim = models.CharField(max_length=200, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'osdelka'


class Osf(BaseModel):
    code = models.CharField(max_length=2, blank=True, null=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    dbegin = models.DateField(blank=True, null=True)
    dend = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'osf'


class Ostamplt(BaseModel):
    kod = models.CharField(max_length=2, blank=True, null=True)
    razdel_1 = models.CharField(max_length=1, blank=True, null=True)
    razdel_2 = models.CharField(max_length=1, blank=True, null=True)
    pr_plt = models.CharField(max_length=1, blank=True, null=True)
    naim = models.TextField(blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)
    pr_rb = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    pr_rk = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    pr_rf = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    pr_am = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    pr_kg = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'ostamplt'


class Ostamplu(BaseModel):
    kod = models.CharField(max_length=2, blank=True, null=True)
    pr_plt = models.CharField(max_length=1, blank=True, null=True)
    pr_kod = models.CharField(max_length=6, blank=True, null=True)
    doc_kod = models.CharField(max_length=4, blank=True, null=True)
    gr_doc = models.CharField(max_length=10, blank=True, null=True)
    vid_doc = models.CharField(max_length=2, blank=True, null=True)
    doc_no = models.CharField(max_length=50, blank=True, null=True)
    doc_date = models.DateField(blank=True, null=True)
    regul_acts = models.CharField(max_length=250, blank=True, null=True)
    oform_docs = models.CharField(max_length=250, blank=True, null=True)
    norm_docs = models.CharField(max_length=250, blank=True, null=True)
    cust_code = models.CharField(max_length=8, blank=True, null=True)
    tnved_code = models.CharField(max_length=14, blank=True, null=True)
    is_no_obl = models.CharField(max_length=1, blank=True, null=True)
    is_quota = models.CharField(max_length=1, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'ostamplu'


class Otamreg(BaseModel):
    kod = models.CharField(max_length=2, blank=True, null=True)
    gr_tr = models.CharField(max_length=2, blank=True, null=True)
    naim = models.CharField(max_length=255, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'otamreg'


class Otr(BaseModel):
    notr = models.DecimalField(default=0.00, max_digits=3, decimal_places=0, blank=True, null=True)
    otr = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'otr'


class Outp(BaseModel):
    kod = models.CharField(max_length=2, blank=True, null=True)
    naim = models.CharField(max_length=255, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)
    pr_rb = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    pr_rk = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    pr_rf = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    pr_am = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    pr_kg = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'outp'


class Ozvet(BaseModel):
    kod = models.CharField(max_length=1, blank=True, null=True)
    kodzv = models.CharField(max_length=3, blank=True, null=True)
    ncv = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'ozvet'


class Pasport(BaseModel):
    p0 = models.CharField(max_length=25, blank=True, null=True)
    p01 = models.DateField(blank=True, null=True)
    p2 = models.CharField(max_length=134, blank=True, null=True)
    p02 = models.CharField(max_length=134, blank=True, null=True)
    p3 = models.CharField(max_length=70, blank=True, null=True)
    p4 = models.CharField(max_length=10, blank=True, null=True)
    p5 = models.CharField(max_length=40, blank=True, null=True)
    p6 = models.CharField(max_length=100, blank=True, null=True)
    p7 = models.CharField(max_length=25, blank=True, null=True)
    p8 = models.CharField(max_length=40, blank=True, null=True)
    ksp = models.CharField(max_length=3, blank=True, null=True)
    p9 = models.CharField(max_length=17, blank=True, null=True)
    p10 = models.CharField(max_length=100, blank=True, null=True)
    p11 = models.CharField(max_length=50, blank=True, null=True)
    p12 = models.DateField(blank=True, null=True)
    p13 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    p14 = models.CharField(max_length=3, blank=True, null=True)
    p15 = models.CharField(max_length=20, blank=True, null=True)
    p16 = models.DateField(blank=True, null=True)
    p17 = models.CharField(max_length=3, blank=True, null=True)
    p18 = models.CharField(max_length=20, blank=True, null=True)
    p19 = models.CharField(max_length=2, blank=True, null=True)
    p20 = models.CharField(max_length=2, blank=True, null=True)
    p21 = models.CharField(max_length=20, blank=True, null=True)
    p22 = models.CharField(max_length=20, blank=True, null=True)
    p23 = models.DateField(blank=True, null=True)
    p24 = models.CharField(max_length=20, blank=True, null=True)
    p25 = models.CharField(max_length=20, blank=True, null=True)
    p26 = models.DateField(blank=True, null=True)
    p27 = models.CharField(max_length=100, blank=True, null=True)
    p28 = models.CharField(max_length=20, blank=True, null=True)
    p29 = models.CharField(max_length=20, blank=True, null=True)
    p30 = models.DateField(blank=True, null=True)
    p31 = models.DateField(blank=True, null=True)
    p_vo = models.CharField(max_length=100, blank=True, null=True)
    p_nl = models.CharField(max_length=20, blank=True, null=True)
    p_dl = models.DateField(blank=True, null=True)
    p_ot = models.CharField(max_length=70, blank=True, null=True)
    p32 = models.DateField(blank=True, null=True)
    psz = models.CharField(max_length=1, blank=True, null=True)
    ogrn = models.CharField(max_length=15, blank=True, null=True)
    p_inn = models.CharField(max_length=12, blank=True, null=True)
    p_kpp = models.CharField(max_length=9, blank=True, null=True)
    p_dlk = models.DateField(blank=True, null=True)
    p_sum_op = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    p_dat_reg = models.DateField(blank=True, null=True)
    p_regn = models.CharField(max_length=9, blank=True, null=True)
    p_kem = models.CharField(max_length=70, blank=True, null=True)
    p_32 = models.CharField(max_length=3, blank=True, null=True)
    p_33 = models.CharField(max_length=1, blank=True, null=True)
    p_okpo = models.CharField(max_length=10, blank=True, null=True)
    p_adrf = models.CharField(max_length=70, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'pasport'


class Pech(BaseModel):
    ktam = models.CharField(max_length=8, blank=True, null=True)
    num_lnp = models.CharField(max_length=4, blank=True, null=True)
    ktam_pch = models.CharField(max_length=8, blank=True, null=True)
    namt = models.CharField(max_length=50, blank=True, null=True)
    fio = models.CharField(max_length=40, blank=True, null=True)
    data_iz = models.DateField(blank=True, null=True)
    date_mod = models.DateField(blank=True, null=True)
    pr_izjat = models.CharField(max_length=20, blank=True, null=True)
    data_vv = models.DateField(blank=True, null=True)
    pr_vvod = models.CharField(max_length=25, blank=True, null=True)
    pr_vivod = models.CharField(max_length=25, blank=True, null=True)
    prikaz48 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'pech'


class PechDel(BaseModel):
    ktam = models.CharField(max_length=8, blank=True, null=True)
    num_lnp = models.CharField(max_length=4, blank=True, null=True)
    ktam_pch = models.CharField(max_length=8, blank=True, null=True)
    namt = models.CharField(max_length=50, blank=True, null=True)
    fio = models.CharField(max_length=40, blank=True, null=True)
    data_iz = models.DateField(blank=True, null=True)
    date_mod = models.DateField(blank=True, null=True)
    pr_izjat = models.CharField(max_length=20, blank=True, null=True)
    data_vv = models.DateField(blank=True, null=True)
    pr_vvod = models.CharField(max_length=25, blank=True, null=True)
    pr_vivod = models.CharField(max_length=25, blank=True, null=True)
    prikaz48 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'pech_del'


class PechKpv(BaseModel):
    ktam = models.CharField(max_length=8, blank=True, null=True)
    num_lnp = models.CharField(max_length=4, blank=True, null=True)
    ktam_pch = models.CharField(max_length=8, blank=True, null=True)
    namt = models.CharField(max_length=50, blank=True, null=True)
    fio = models.CharField(max_length=40, blank=True, null=True)
    data_iz = models.DateField(blank=True, null=True)
    date_mod = models.DateField(blank=True, null=True)
    pr_izjat = models.CharField(max_length=50, blank=True, null=True)
    data_vv = models.DateField(blank=True, null=True)
    pr_vvod = models.CharField(max_length=25, blank=True, null=True)
    pr_vivod = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'pech_kpv'


class Pechvid(BaseModel):
    pechvid = models.CharField(max_length=1, blank=True, null=True)
    name = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'pechvid'


class PedhDel(BaseModel):
    ktam = models.CharField(max_length=8, blank=True, null=True)
    num_lnp = models.CharField(max_length=4, blank=True, null=True)
    ktam_pch = models.CharField(max_length=8, blank=True, null=True)
    namt = models.CharField(max_length=50, blank=True, null=True)
    fio = models.CharField(max_length=40, blank=True, null=True)
    data_iz = models.DateField(blank=True, null=True)
    date_mod = models.DateField(blank=True, null=True)
    pr_izjat = models.CharField(max_length=20, blank=True, null=True)
    data_vv = models.DateField(blank=True, null=True)
    pr_vvod = models.CharField(max_length=25, blank=True, null=True)
    pr_vivod = models.CharField(max_length=25, blank=True, null=True)
    prikaz48 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'pedh_del'


class PermSch(BaseModel):
    p_rnum = models.CharField(max_length=18, blank=True, null=True)
    p_bokpo = models.CharField(max_length=10, blank=True, null=True)
    p_binn = models.CharField(max_length=12, blank=True, null=True)
    p_sch = models.CharField(max_length=20, blank=True, null=True)
    p_endsch = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'perm_sch'


class Permit(BaseModel):
    p_rnum = models.CharField(max_length=18, blank=True, null=True)
    p_dend = models.DateField(blank=True, null=True)
    p_okpo = models.CharField(max_length=10, blank=True, null=True)
    p_inn = models.CharField(max_length=12, blank=True, null=True)
    p_name = models.CharField(max_length=80, blank=True, null=True)
    p_adru = models.CharField(max_length=80, blank=True, null=True)
    p_adrf = models.CharField(max_length=80, blank=True, null=True)
    p_gks_num = models.CharField(max_length=13, blank=True, null=True)
    p_tlic = models.CharField(max_length=5, blank=True, null=True)
    p_nlic = models.DecimalField(default=0.00, max_digits=4, decimal_places=0, blank=True, null=True)
    p_dlic = models.DateField(blank=True, null=True)
    p_ndog = models.CharField(max_length=10, blank=True, null=True)
    p_ddog = models.DateField(blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'permit'


class Plbase(BaseModel):
    inn = models.CharField(max_length=12, blank=True, null=True)
    kpp = models.CharField(max_length=9, blank=True, null=True)
    okpo = models.CharField(max_length=10, blank=True, null=True)
    k92 = models.CharField(max_length=19, blank=True, null=True)
    k93 = models.DateField(blank=True, null=True)
    k_val = models.CharField(max_length=3, blank=True, null=True)
    k94 = models.DecimalField(default=0.00, max_digits=17, decimal_places=2, blank=True, null=True)
    k95 = models.DecimalField(default=0.00, max_digits=17, decimal_places=2, blank=True, null=True)
    k96 = models.DateField(blank=True, null=True)
    kbk = models.CharField(max_length=20, blank=True, null=True)
    sp = models.CharField(max_length=2, blank=True, null=True)
    ntr = models.CharField(max_length=26, blank=True, null=True)
    process_id = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'plbase'


class PlomDel(BaseModel):
    ktam = models.CharField(max_length=8, blank=True, null=True)
    num_plom = models.CharField(max_length=7, blank=True, null=True)
    fio = models.CharField(max_length=40, blank=True, null=True)
    data_iz = models.DateField(blank=True, null=True)
    date_mod = models.DateField(blank=True, null=True)
    pr_izjat = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'plom_del'


class Plombir(BaseModel):
    ktam = models.CharField(max_length=8, blank=True, null=True)
    num_plom = models.CharField(max_length=7, blank=True, null=True)
    fio = models.CharField(max_length=40, blank=True, null=True)
    data_iz = models.DateField(blank=True, null=True)
    date_mod = models.DateField(blank=True, null=True)
    pr_izjat = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'plombir'


class PointDa(BaseModel):
    checkpoint = models.CharField(max_length=6, blank=True, null=True)
    state_pp = models.DecimalField(default=0.00, max_digits=3, decimal_places=0, blank=True, null=True)
    work_day = models.CharField(max_length=2, blank=True, null=True)
    work_hour1 = models.CharField(max_length=5, blank=True, null=True)
    work_end1 = models.CharField(max_length=5, blank=True, null=True)
    work_hour2 = models.CharField(max_length=5, blank=True, null=True)
    work_end2 = models.CharField(max_length=5, blank=True, null=True)
    work_hour3 = models.CharField(max_length=5, blank=True, null=True)
    work_end3 = models.CharField(max_length=5, blank=True, null=True)
    work_hour4 = models.CharField(max_length=5, blank=True, null=True)
    work_end4 = models.CharField(max_length=5, blank=True, null=True)
    work_hour5 = models.CharField(max_length=5, blank=True, null=True)
    work_end5 = models.CharField(max_length=5, blank=True, null=True)
    work_hour6 = models.CharField(max_length=5, blank=True, null=True)
    work_end6 = models.CharField(max_length=5, blank=True, null=True)
    work_hour7 = models.CharField(max_length=5, blank=True, null=True)
    work_end7 = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'point_da'


class PointIn(BaseModel):
    checkpoint = models.CharField(max_length=6, blank=True, null=True)
    inclusioni = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'point_in'


class PointNe(BaseModel):
    checkpoint = models.CharField(max_length=6, blank=True, null=True)
    kod = models.CharField(max_length=3, blank=True, null=True)
    point_n = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'point_ne'


class PointOp(BaseModel):
    checkpoint = models.CharField(max_length=6, blank=True, null=True)
    operationi = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'point_op'


class PointRe(BaseModel):
    checkpoint = models.CharField(max_length=6, blank=True, null=True)
    adress = models.CharField(max_length=100, blank=True, null=True)
    telefon = models.CharField(max_length=15, blank=True, null=True)
    telefon_v = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'point_re'


class Poluch(BaseModel):
    zayv = models.CharField(max_length=60, blank=True, null=True)
    adress = models.CharField(max_length=60, blank=True, null=True)
    telefax = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'poluch'


class Pravo(BaseModel):
    n_dela = models.CharField(max_length=18, blank=True, null=True)
    datzd = models.DateField(blank=True, null=True)
    kategp = models.CharField(max_length=2, blank=True, null=True)
    nomr1 = models.CharField(max_length=2, blank=True, null=True)
    nomr2 = models.CharField(max_length=4, blank=True, null=True)
    okpo = models.CharField(max_length=10, blank=True, null=True)
    psu = models.CharField(max_length=1, blank=True, null=True)
    okato = models.CharField(max_length=5, blank=True, null=True)
    namp = models.CharField(max_length=80, blank=True, null=True)
    strp = models.CharField(max_length=3, blank=True, null=True)
    adrp = models.CharField(max_length=80, blank=True, null=True)
    ogrn = models.CharField(max_length=15, blank=True, null=True)
    inn = models.CharField(max_length=12, blank=True, null=True)
    kpp = models.CharField(max_length=9, blank=True, null=True)
    sttko = models.CharField(max_length=3, blank=True, null=True)
    sttk1 = models.CharField(max_length=3, blank=True, null=True)
    sttk2 = models.CharField(max_length=3, blank=True, null=True)
    sttk3 = models.CharField(max_length=3, blank=True, null=True)
    kodresh = models.CharField(max_length=2, blank=True, null=True)
    dresh = models.DateField(blank=True, null=True)
    sumrh = models.DecimalField(default=0.00, max_digits=16, decimal_places=0, blank=True, null=True)
    sumrh_v = models.CharField(max_length=1, blank=True, null=True)
    sumkonf = models.DecimalField(default=0.00, max_digits=16, decimal_places=0, blank=True, null=True)
    sumvzs = models.DecimalField(default=0.00, max_digits=16, decimal_places=0, blank=True, null=True)
    sumvzs_u = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'pravo'


class Predresh(BaseModel):
    kodt = models.CharField(max_length=13, blank=True, null=True)
    npp = models.DecimalField(default=0.00, max_digits=5, decimal_places=0, blank=True, null=True)
    nam_tov = models.TextField(blank=True, null=True)
    prim = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'predresh'


class Price(BaseModel):
    cod = models.CharField(max_length=10, blank=True, null=True)
    edi = models.CharField(max_length=3, blank=True, null=True)
    kodstr = models.CharField(max_length=3, blank=True, null=True)
    kodop = models.CharField(max_length=3, blank=True, null=True)
    erprice1 = models.DecimalField(default=0.00, max_digits=16, decimal_places=4, blank=True, null=True)
    erpdev1 = models.DecimalField(default=0.00, max_digits=16, decimal_places=4, blank=True, null=True)
    erprice2 = models.DecimalField(default=0.00, max_digits=16, decimal_places=4, blank=True, null=True)
    erpdev2 = models.DecimalField(default=0.00, max_digits=16, decimal_places=4, blank=True, null=True)
    arprice1 = models.DecimalField(default=0.00, max_digits=16, decimal_places=4, blank=True, null=True)
    ardev1 = models.DecimalField(default=0.00, max_digits=16, decimal_places=4, blank=True, null=True)
    arprice2 = models.DecimalField(default=0.00, max_digits=16, decimal_places=4, blank=True, null=True)
    ardev2 = models.DecimalField(default=0.00, max_digits=16, decimal_places=4, blank=True, null=True)
    n10 = models.DecimalField(default=0.00, max_digits=16, decimal_places=4, blank=True, null=True)
    n10b = models.DecimalField(default=0.00, max_digits=16, decimal_places=4, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'price'


class Price10(BaseModel):
    cod = models.CharField(max_length=10, blank=True, null=True)
    edi = models.CharField(max_length=3, blank=True, null=True)
    kodstr = models.CharField(max_length=3, blank=True, null=True)
    kodop = models.CharField(max_length=3, blank=True, null=True)
    erprice1 = models.DecimalField(default=0.00, max_digits=16, decimal_places=4, blank=True, null=True)
    erpdev1 = models.DecimalField(default=0.00, max_digits=16, decimal_places=4, blank=True, null=True)
    erprice2 = models.DecimalField(default=0.00, max_digits=16, decimal_places=4, blank=True, null=True)
    erpdev2 = models.DecimalField(default=0.00, max_digits=16, decimal_places=4, blank=True, null=True)
    arprice1 = models.DecimalField(default=0.00, max_digits=16, decimal_places=4, blank=True, null=True)
    ardev1 = models.DecimalField(default=0.00, max_digits=16, decimal_places=4, blank=True, null=True)
    arprice2 = models.DecimalField(default=0.00, max_digits=16, decimal_places=4, blank=True, null=True)
    ardev2 = models.DecimalField(default=0.00, max_digits=16, decimal_places=4, blank=True, null=True)
    n10 = models.DecimalField(default=0.00, max_digits=16, decimal_places=4, blank=True, null=True)
    n10b = models.DecimalField(default=0.00, max_digits=16, decimal_places=4, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'price10'


class Priceg(BaseModel):
    nd = models.CharField(max_length=23, blank=True, null=True)
    g33 = models.CharField(max_length=10, blank=True, null=True)
    kodop = models.CharField(max_length=2, blank=True, null=True)
    g37 = models.CharField(max_length=6, blank=True, null=True)
    g24 = models.CharField(max_length=2, blank=True, null=True)
    kodstr = models.CharField(max_length=3, blank=True, null=True)
    g34 = models.CharField(max_length=3, blank=True, null=True)
    arprice1 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    arprice2 = models.DecimalField(default=0.00, max_digits=16, decimal_places=2, blank=True, null=True)
    g41a = models.CharField(max_length=3, blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'priceg'


class PrimAdp(BaseModel):
    kodt = models.CharField(max_length=10, blank=True, null=True)
    naim = models.CharField(max_length=250, blank=True, null=True)
    stavka = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, blank=True, null=True)
    simv = models.CharField(max_length=1, blank=True, null=True)
    edi = models.CharField(max_length=3, blank=True, null=True)
    country3 = models.CharField(max_length=3, blank=True, null=True)
    country2 = models.CharField(max_length=2, blank=True, null=True)
    npric = models.CharField(max_length=20, blank=True, null=True)
    dpric = models.DateField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    data1 = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'prim_adp'


class PrimBg(BaseModel):
    kodt = models.CharField(max_length=10, blank=True, null=True)
    prim = models.CharField(max_length=140, blank=True, null=True)
    naim = models.CharField(max_length=140, blank=True, null=True)
    kodbg = models.CharField(max_length=20, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'prim_bg'


class PrimBzp(BaseModel):
    kodt = models.CharField(max_length=10, blank=True, null=True)
    prim = models.CharField(max_length=140, blank=True, null=True)
    prbzp = models.CharField(max_length=1, blank=True, null=True)
    npric = models.CharField(max_length=20, blank=True, null=True)
    dpric = models.DateField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    data1 = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'prim_bzp'


class PrimKod(BaseModel):
    kod = models.CharField(max_length=10, blank=True, null=True)
    naim = models.CharField(max_length=140, blank=True, null=True)
    pr = models.CharField(max_length=1, blank=True, null=True)
    pr_f = models.CharField(max_length=1, blank=True, null=True)
    npric = models.CharField(max_length=20, blank=True, null=True)
    dpric = models.DateField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    data1 = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'prim_kod'


class PrimLec(BaseModel):
    kodt = models.CharField(max_length=10, blank=True, null=True)
    prim = models.CharField(max_length=140, blank=True, null=True)
    prlic = models.CharField(max_length=1, blank=True, null=True)
    npric = models.CharField(max_length=20, blank=True, null=True)
    dpric = models.DateField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    data1 = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'prim_lec'


class PrimLic(BaseModel):
    kodt = models.CharField(max_length=10, blank=True, null=True)
    prim = models.CharField(max_length=140, blank=True, null=True)
    prlic = models.CharField(max_length=1, blank=True, null=True)
    npric = models.CharField(max_length=20, blank=True, null=True)
    dpric = models.DateField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    data1 = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'prim_lic'


class PrimMrk(BaseModel):
    kodt = models.CharField(max_length=10, blank=True, null=True)
    prim = models.CharField(max_length=140, blank=True, null=True)
    npric = models.CharField(max_length=20, blank=True, null=True)
    dpric = models.DateField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    data1 = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'prim_mrk'


class PrimNdc(BaseModel):
    st = models.CharField(max_length=2, blank=True, null=True)
    okproduct = models.CharField(max_length=6, blank=True, null=True)
    kodt = models.CharField(max_length=10, blank=True, null=True)
    naim = models.TextField(blank=True, null=True)
    st_ndc = models.DecimalField(default=0.00, max_digits=15, decimal_places=6, blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    data1 = models.DateField(blank=True, null=True)
    npric = models.CharField(max_length=20, blank=True, null=True)
    dpric = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'prim_ndc'


class PrimPr0(BaseModel):
    kodt = models.CharField(max_length=10, blank=True, null=True)
    prim = models.CharField(max_length=140, blank=True, null=True)
    npric = models.CharField(max_length=20, blank=True, null=True)
    dpric = models.DateField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    data1 = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'prim_pr0'


class PrimPrf(BaseModel):
    kod = models.CharField(max_length=10, blank=True, null=True)
    naim = models.CharField(max_length=140, blank=True, null=True)
    npric = models.CharField(max_length=20, blank=True, null=True)
    dpric = models.DateField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    data1 = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'prim_prf'


class PrimPry(BaseModel):
    kod = models.CharField(max_length=10, blank=True, null=True)
    prim = models.CharField(max_length=140, blank=True, null=True)
    prprf = models.CharField(max_length=1, blank=True, null=True)
    npric = models.CharField(max_length=20, blank=True, null=True)
    dpric = models.DateField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    data1 = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'prim_pry'


class PrimSpr(BaseModel):
    kod = models.CharField(max_length=10, blank=True, null=True)
    naim = models.CharField(max_length=140, blank=True, null=True)
    pr = models.CharField(max_length=1, blank=True, null=True)
    pr_str = models.CharField(max_length=1, blank=True, null=True)
    pr_f = models.CharField(max_length=1, blank=True, null=True)
    npric = models.CharField(max_length=20, blank=True, null=True)
    dpric = models.DateField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    data1 = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'prim_spr'


class PrimSt1(BaseModel):
    kod = models.CharField(max_length=10, blank=True, null=True)
    prim = models.CharField(max_length=140, blank=True, null=True)
    npric = models.CharField(max_length=20, blank=True, null=True)
    dpric = models.DateField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    data1 = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'prim_st1'


class PrmCont(BaseModel):
    kodt = models.CharField(max_length=10, blank=True, null=True)
    prim = models.CharField(max_length=140, blank=True, null=True)
    npric = models.CharField(max_length=20, blank=True, null=True)
    dpric = models.DateField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    data1 = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'prm_cont'


class Prstate(BaseModel):
    code = models.CharField(max_length=1, blank=True, null=True)
    name = models.CharField(max_length=85, blank=True, null=True)
    codeoksmt = models.CharField(max_length=3, blank=True, null=True)
    dbegin = models.DateField(blank=True, null=True)
    dend = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'prstate'


class PzkOrd(BaseModel):
    ref_numd = models.CharField(max_length=20, blank=True, null=True)
    ref_datd = models.DateField(blank=True, null=True)
    ref_typd = models.CharField(max_length=30, blank=True, null=True)
    ref_dptd = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'pzk_ord'


# class R32Tov(BaseModel):
#
#     class Meta:
#         abstract = True
#         # db_table = 'r32_tov'


class Ram(BaseModel):
    kod = models.CharField(max_length=2, blank=True, null=True)
    naim = models.CharField(max_length=60, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'ram'


class RdBg872(BaseModel):
    kodt = models.CharField(max_length=8, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=75, blank=True, null=True)
    nlic = models.CharField(max_length=12, blank=True, null=True)
    fax = models.CharField(max_length=20, blank=True, null=True)
    teleks = models.CharField(max_length=20, blank=True, null=True)
    telefon = models.CharField(max_length=20, blank=True, null=True)
    owner = models.CharField(max_length=8, blank=True, null=True)
    kodtn = models.CharField(max_length=8, blank=True, null=True)
    kodtold = models.CharField(max_length=8, blank=True, null=True)
    dbegin = models.DateField(blank=True, null=True)
    dend = models.DateField(blank=True, null=True)
    pr_per = models.CharField(max_length=1, blank=True, null=True)
    sovam = models.CharField(max_length=9, blank=True, null=True)
    vidtrans = models.CharField(max_length=30, blank=True, null=True)
    sign_ord = models.CharField(max_length=30, blank=True, null=True)
    n_order = models.CharField(max_length=20, blank=True, null=True)
    d_order = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'rd_bg872'


class Re12Tm(BaseModel):
    r1 = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    r2 = models.DecimalField(default=0.00, max_digits=2, decimal_places=0, blank=True, null=True)
    r3 = models.DecimalField(default=0.00, max_digits=5, decimal_places=0, blank=True, null=True)
    r4 = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    r5 = models.DecimalField(default=0.00, max_digits=9, decimal_places=0, blank=True, null=True)
    r6 = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    r7 = models.DecimalField(default=0.00, max_digits=9, decimal_places=0, blank=True, null=True)
    r8 = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    r9 = models.DecimalField(default=0.00, max_digits=9, decimal_places=0, blank=True, null=True)
    r10 = models.DecimalField(default=0.00, max_digits=9, decimal_places=0, blank=True, null=True)
    r11 = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    r12 = models.DecimalField(default=0.00, max_digits=9, decimal_places=0, blank=True, null=True)
    r13 = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    r14 = models.DecimalField(default=0.00, max_digits=9, decimal_places=0, blank=True, null=True)
    r15 = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    r16 = models.DecimalField(default=0.00, max_digits=9, decimal_places=0, blank=True, null=True)
    r17 = models.DecimalField(default=0.00, max_digits=9, decimal_places=0, blank=True, null=True)
    r18 = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    r19 = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    r20 = models.DecimalField(default=0.00, max_digits=8, decimal_places=0, blank=True, null=True)
    r21 = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    r22 = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    r23 = models.DecimalField(default=0.00, max_digits=8, decimal_places=0, blank=True, null=True)
    r24 = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    r25 = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    r26 = models.DecimalField(default=0.00, max_digits=8, decimal_places=0, blank=True, null=True)
    r27 = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    r28 = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    r29 = models.DecimalField(default=0.00, max_digits=8, decimal_places=0, blank=True, null=True)
    r30 = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    r31 = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    r32 = models.DecimalField(default=0.00, max_digits=8, decimal_places=0, blank=True, null=True)
    r33 = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    r34 = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    r35 = models.DecimalField(default=0.00, max_digits=8, decimal_places=0, blank=True, null=True)
    r36 = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    r37 = models.DecimalField(default=0.00, max_digits=10, decimal_places=0, blank=True, null=True)
    r38 = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    r39 = models.DecimalField(default=0.00, max_digits=10, decimal_places=0, blank=True, null=True)
    r40 = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    r41 = models.DecimalField(default=0.00, max_digits=10, decimal_places=0, blank=True, null=True)
    r42 = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    r43 = models.DecimalField(default=0.00, max_digits=10, decimal_places=0, blank=True, null=True)
    r44 = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    r45 = models.DecimalField(default=0.00, max_digits=10, decimal_places=0, blank=True, null=True)
    r46 = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    r47 = models.DecimalField(default=0.00, max_digits=10, decimal_places=0, blank=True, null=True)
    r48 = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    r49 = models.DecimalField(default=0.00, max_digits=10, decimal_places=0, blank=True, null=True)
    r50 = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    r51 = models.DecimalField(default=0.00, max_digits=10, decimal_places=0, blank=True, null=True)
    r52 = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    r53 = models.DecimalField(default=0.00, max_digits=10, decimal_places=0, blank=True, null=True)
    r54 = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    r55 = models.DecimalField(default=0.00, max_digits=7, decimal_places=0, blank=True, null=True)
    r56 = models.DecimalField(default=0.00, max_digits=8, decimal_places=0, blank=True, null=True)
    r57 = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    r58 = models.DecimalField(default=0.00, max_digits=7, decimal_places=0, blank=True, null=True)
    r59 = models.DecimalField(default=0.00, max_digits=8, decimal_places=0, blank=True, null=True)
    r60 = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    r61 = models.DecimalField(default=0.00, max_digits=7, decimal_places=0, blank=True, null=True)
    r62 = models.DecimalField(default=0.00, max_digits=8, decimal_places=0, blank=True, null=True)
    r63 = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    r64 = models.DecimalField(default=0.00, max_digits=7, decimal_places=0, blank=True, null=True)
    r65 = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    r66 = models.DecimalField(default=0.00, max_digits=7, decimal_places=0, blank=True, null=True)
    r67 = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    r68 = models.DecimalField(default=0.00, max_digits=7, decimal_places=0, blank=True, null=True)
    r69 = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    r70 = models.DecimalField(default=0.00, max_digits=7, decimal_places=0, blank=True, null=True)
    r71 = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    r72 = models.DecimalField(default=0.00, max_digits=7, decimal_places=0, blank=True, null=True)
    r73 = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    r74 = models.DecimalField(default=0.00, max_digits=7, decimal_places=0, blank=True, null=True)
    r75 = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    r76 = models.DecimalField(default=0.00, max_digits=7, decimal_places=0, blank=True, null=True)
    r77 = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    r78 = models.DecimalField(default=0.00, max_digits=7, decimal_places=0, blank=True, null=True)
    r79 = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    r80 = models.DecimalField(default=0.00, max_digits=7, decimal_places=0, blank=True, null=True)
    r81 = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    r82 = models.DecimalField(default=0.00, max_digits=7, decimal_places=0, blank=True, null=True)
    r83 = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    r84 = models.DecimalField(default=0.00, max_digits=7, decimal_places=0, blank=True, null=True)
    r85 = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    r86 = models.DecimalField(default=0.00, max_digits=7, decimal_places=0, blank=True, null=True)
    r87 = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    r88 = models.DecimalField(default=0.00, max_digits=7, decimal_places=0, blank=True, null=True)
    r89 = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    r90 = models.DecimalField(default=0.00, max_digits=7, decimal_places=0, blank=True, null=True)
    r91 = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    r92 = models.DecimalField(default=0.00, max_digits=7, decimal_places=0, blank=True, null=True)
    r93 = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    r94 = models.DecimalField(default=0.00, max_digits=7, decimal_places=0, blank=True, null=True)
    r95 = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    r96 = models.DecimalField(default=0.00, max_digits=7, decimal_places=0, blank=True, null=True)
    r97 = models.DecimalField(default=0.00, max_digits=6, decimal_places=0, blank=True, null=True)
    r98 = models.DecimalField(default=0.00, max_digits=7, decimal_places=0, blank=True, null=True)
    r99 = models.DecimalField(default=0.00, max_digits=11, decimal_places=0, blank=True, null=True)
    r100 = models.DecimalField(default=0.00, max_digits=11, decimal_places=0, blank=True, null=True)
    daterec = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 're_12tm'


class ReAct(BaseModel):
    kod = models.DecimalField(default=0.00, max_digits=2, decimal_places=0, blank=True, null=True)
    deistv = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 're_act'


class ReArhiv(BaseModel):
    god = models.DecimalField(default=0.00, max_digits=4, decimal_places=0, blank=True, null=True)
    activ = models.BooleanField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 're_arhiv'


class ReDeist(BaseModel):
    ntam = models.DecimalField(default=0.00, max_digits=5, decimal_places=0, blank=True, null=True)
    delnum = models.DecimalField(default=0.00, max_digits=4, decimal_places=0, blank=True, null=True)
    datprt = models.DateField(blank=True, null=True)
    ndeistv = models.DecimalField(default=0.00, max_digits=2, decimal_places=0, blank=True, null=True)
    datedeistv = models.DateField(blank=True, null=True)
    prim = models.CharField(max_length=75, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 're_deist'


class ReDelo(BaseModel):
    ntam = models.DecimalField(default=0.00, max_digits=5, decimal_places=0, blank=True, null=True)
    delnum = models.DecimalField(default=0.00, max_digits=4, decimal_places=0, blank=True, null=True)
    datprt = models.DateField(blank=True, null=True)
    famrus = models.CharField(max_length=16, blank=True, null=True)
    namerus = models.CharField(max_length=12, blank=True, null=True)
    otrus = models.CharField(max_length=16, blank=True, null=True)
    famlat = models.CharField(max_length=16, blank=True, null=True)
    namelat = models.CharField(max_length=12, blank=True, null=True)
    polnar = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    ncntr = models.DecimalField(default=0.00, max_digits=3, decimal_places=0, blank=True, null=True)
    nkat = models.DecimalField(default=0.00, max_digits=2, decimal_places=0, blank=True, null=True)
    rodzan = models.DecimalField(default=0.00, max_digits=3, decimal_places=0, blank=True, null=True)
    notr = models.DecimalField(default=0.00, max_digits=3, decimal_places=0, blank=True, null=True)
    pass_field = models.CharField(db_column='pass', max_length=20, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    bday = models.DecimalField(default=0.00, max_digits=4, decimal_places=0, blank=True, null=True)
    rab = models.CharField(max_length=60, blank=True, null=True)
    live = models.CharField(max_length=60, blank=True, null=True)
    oblast = models.DecimalField(default=0.00, max_digits=4, decimal_places=0, blank=True, null=True)
    prnar = models.DecimalField(default=0.00, max_digits=2, decimal_places=0, blank=True, null=True)
    ndep = models.DecimalField(default=0.00, max_digits=3, decimal_places=0, blank=True, null=True)
    ndes = models.DecimalField(default=0.00, max_digits=3, decimal_places=0, blank=True, null=True)
    prinout = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    way = models.CharField(max_length=60, blank=True, null=True)
    ntrans = models.DecimalField(default=0.00, max_digits=3, decimal_places=0, blank=True, null=True)
    placenar = models.CharField(max_length=55, blank=True, null=True)
    datnar = models.DateField(blank=True, null=True)
    nar = models.CharField(max_length=60, blank=True, null=True)
    expl = models.CharField(max_length=60, blank=True, null=True)
    npost = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    datpost = models.DateField(blank=True, null=True)
    st1 = models.CharField(max_length=8, blank=True, null=True)
    st2 = models.CharField(max_length=8, blank=True, null=True)
    st3 = models.CharField(max_length=8, blank=True, null=True)
    st4 = models.CharField(max_length=8, blank=True, null=True)
    ishpost1 = models.CharField(max_length=6, blank=True, null=True)
    ishpost2 = models.CharField(max_length=4, blank=True, null=True)
    prichrvto = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    nrvto = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    datrvto = models.DateField(blank=True, null=True)
    vhrvto1 = models.CharField(max_length=6, blank=True, null=True)
    vhrvto2 = models.CharField(max_length=4, blank=True, null=True)
    shtrafnal = models.DecimalField(default=0.00, max_digits=9, decimal_places=0, blank=True, null=True)
    shtrafvz = models.DecimalField(default=0.00, max_digits=11, decimal_places=0, blank=True, null=True)
    kshtrafvz = models.DecimalField(default=0.00, max_digits=3, decimal_places=0, blank=True, null=True)
    vzshtrrub = models.DecimalField(default=0.00, max_digits=11, decimal_places=0, blank=True, null=True)
    nordshtraf = models.CharField(max_length=6, blank=True, null=True)
    stoim = models.DecimalField(default=0.00, max_digits=13, decimal_places=2, blank=True, null=True)
    stoimvz = models.DecimalField(default=0.00, max_digits=14, decimal_places=2, blank=True, null=True)
    kstoimvz = models.DecimalField(default=0.00, max_digits=3, decimal_places=0, blank=True, null=True)
    nordstoim = models.CharField(max_length=6, blank=True, null=True)
    probshtr = models.BooleanField(blank=True, null=True)
    obshtr = models.CharField(max_length=120, blank=True, null=True)
    pradm = models.BooleanField(blank=True, null=True)
    razradm = models.CharField(max_length=20, blank=True, null=True)
    prldosm = models.BooleanField(blank=True, null=True)
    razrldosm = models.CharField(max_length=20, blank=True, null=True)
    provldosm = models.CharField(max_length=20, blank=True, null=True)
    dobrov = models.BooleanField(blank=True, null=True)
    specldosm = models.BooleanField(blank=True, null=True)
    rezldosm = models.BooleanField(blank=True, null=True)
    daterec = models.DateField(blank=True, null=True)
    inspkod = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 're_delo'


class ReDopps(BaseModel):
    ntam = models.DecimalField(default=0.00, max_digits=5, decimal_places=0, blank=True, null=True)
    delnum = models.DecimalField(default=0.00, max_digits=4, decimal_places=0, blank=True, null=True)
    datprt = models.DateField(blank=True, null=True)
    datpost = models.DateField(blank=True, null=True)
    ishod1 = models.CharField(max_length=6, blank=True, null=True)
    ishod2 = models.CharField(max_length=4, blank=True, null=True)
    post = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    st1 = models.CharField(max_length=8, blank=True, null=True)
    st2 = models.CharField(max_length=8, blank=True, null=True)
    st3 = models.CharField(max_length=8, blank=True, null=True)
    st4 = models.CharField(max_length=8, blank=True, null=True)
    akt = models.BooleanField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 're_dopps'


class ReDoprv(BaseModel):
    ntam = models.DecimalField(default=0.00, max_digits=5, decimal_places=0, blank=True, null=True)
    delnum = models.DecimalField(default=0.00, max_digits=4, decimal_places=0, blank=True, null=True)
    datprt = models.DateField(blank=True, null=True)
    vhod1 = models.CharField(max_length=6, blank=True, null=True)
    vhod2 = models.CharField(max_length=4, blank=True, null=True)
    datrvto = models.DateField(blank=True, null=True)
    prich = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    rvto = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    akt = models.BooleanField(blank=True, null=True)
    izmvz = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 're_doprv'


class ReLi(BaseModel):
    ntam = models.DecimalField(default=0.00, max_digits=5, decimal_places=0, blank=True, null=True)
    delnum = models.DecimalField(default=0.00, max_digits=4, decimal_places=0, blank=True, null=True)
    datprt = models.DateField(blank=True, null=True)
    ishod1 = models.CharField(max_length=6, blank=True, null=True)
    ishod2 = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 're_li'


class ReLsoi(BaseModel):
    ntam = models.DecimalField(default=0.00, max_digits=5, decimal_places=0, blank=True, null=True)
    delnum = models.DecimalField(default=0.00, max_digits=4, decimal_places=0, blank=True, null=True)
    datprt = models.DateField(blank=True, null=True)
    ishod1 = models.CharField(max_length=6, blank=True, null=True)
    ishod2 = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 're_lsoi'


class ReLsov(BaseModel):
    ntam = models.DecimalField(default=0.00, max_digits=5, decimal_places=0, blank=True, null=True)
    delnum = models.DecimalField(default=0.00, max_digits=4, decimal_places=0, blank=True, null=True)
    datprt = models.DateField(blank=True, null=True)
    vhod1 = models.CharField(max_length=6, blank=True, null=True)
    vhod2 = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 're_lsov'


class ReLv(BaseModel):
    ntam = models.DecimalField(default=0.00, max_digits=5, decimal_places=0, blank=True, null=True)
    delnum = models.DecimalField(default=0.00, max_digits=4, decimal_places=0, blank=True, null=True)
    datprt = models.DateField(blank=True, null=True)
    vhod1 = models.CharField(max_length=6, blank=True, null=True)
    vhod2 = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 're_lv'


class ReMist(BaseModel):
    ntam = models.DecimalField(default=0.00, max_digits=5, decimal_places=0, blank=True, null=True)
    delnum = models.DecimalField(default=0.00, max_digits=4, decimal_places=0, blank=True, null=True)
    datprt = models.DateField(blank=True, null=True)
    datemist = models.DateField(blank=True, null=True)
    nmistake = models.DecimalField(default=0.00, max_digits=2, decimal_places=0, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 're_mist'


class RePost(BaseModel):
    npost = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    post = models.CharField(max_length=55, blank=True, null=True)
    krpost = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 're_post'


class RePrich(BaseModel):
    nprich = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    krprich = models.CharField(max_length=7, blank=True, null=True)
    prich = models.CharField(max_length=55, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 're_prich'


class ReRvto(BaseModel):
    nrvto = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    rvto = models.CharField(max_length=55, blank=True, null=True)
    krrvto = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 're_rvto'


class ReSttk(BaseModel):
    kodst = models.CharField(max_length=8, blank=True, null=True)
    st = models.CharField(max_length=65, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 're_sttk'


class ReTmist(BaseModel):
    kod = models.DecimalField(default=0.00, max_digits=2, decimal_places=0, blank=True, null=True)
    mistake = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 're_tmist'


class ReZalob(BaseModel):
    ntam = models.DecimalField(default=0.00, max_digits=5, decimal_places=0, blank=True, null=True)
    delnum = models.DecimalField(default=0.00, max_digits=4, decimal_places=0, blank=True, null=True)
    datprt = models.DateField(blank=True, null=True)
    nvhod1 = models.CharField(max_length=6, blank=True, null=True)
    nvhod2 = models.CharField(max_length=4, blank=True, null=True)
    nish1 = models.CharField(max_length=6, blank=True, null=True)
    nish2 = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 're_zalob'


class Recom(BaseModel):
    itn = models.CharField(max_length=15, blank=True, null=True)
    num_id = models.DecimalField(default=0.00, max_digits=3, decimal_places=0, blank=True, null=True)
    kod_rec = models.CharField(max_length=6, blank=True, null=True)
    kodtam = models.CharField(max_length=8, blank=True, null=True)
    osnov = models.CharField(max_length=50, blank=True, null=True)
    data_begin = models.DateField(blank=True, null=True)
    data_end = models.DateField(blank=True, null=True)
    crc = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'recom'


class Reg(BaseModel):
    adress = models.CharField(max_length=80, blank=True, null=True)
    telefon = models.CharField(max_length=12, blank=True, null=True)
    telegraf = models.CharField(max_length=50, blank=True, null=True)
    telefax = models.CharField(max_length=12, blank=True, null=True)
    telex = models.CharField(max_length=20, blank=True, null=True)
    zayv = models.CharField(max_length=80, blank=True, null=True)
    nomr1 = models.CharField(max_length=2, blank=True, null=True)
    nomr2 = models.CharField(max_length=4, blank=True, null=True)
    nomr3 = models.CharField(max_length=8, blank=True, null=True)
    okpobr = models.CharField(max_length=8, blank=True, null=True)
    schet1 = models.CharField(max_length=20, blank=True, null=True)
    korschr = models.CharField(max_length=20, blank=True, null=True)
    okpobv = models.CharField(max_length=8, blank=True, null=True)
    schet2 = models.CharField(max_length=20, blank=True, null=True)
    korschv = models.CharField(max_length=20, blank=True, null=True)
    kodtam = models.CharField(max_length=5, blank=True, null=True)
    datr = models.DateField(blank=True, null=True)
    inn = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'reg'


class RegK(BaseModel):
    itn = models.CharField(max_length=15, blank=True, null=True)
    data_uk = models.DateField(blank=True, null=True)
    name_ubed = models.CharField(max_length=100, blank=True, null=True)
    reg_nom = models.CharField(max_length=20, blank=True, null=True)
    ogrn = models.CharField(max_length=15, blank=True, null=True)
    inn = models.CharField(max_length=12, blank=True, null=True)
    kpp = models.CharField(max_length=9, blank=True, null=True)
    okato = models.CharField(max_length=11, blank=True, null=True)
    adres = models.CharField(max_length=100, blank=True, null=True)
    kodtam = models.CharField(max_length=8, blank=True, null=True)
    st_uk = models.CharField(max_length=25, blank=True, null=True)
    data_st_uk = models.DateField(blank=True, null=True)
    prim = models.CharField(max_length=250, blank=True, null=True)
    data_beg = models.DateField(blank=True, null=True)
    data_mod = models.DateField(blank=True, null=True)
    data_end = models.DateField(blank=True, null=True)
    crc = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'reg_k'


class RegMvs(BaseModel):
    okpo = models.CharField(max_length=10, blank=True, null=True)
    kodmin = models.CharField(max_length=10, blank=True, null=True)
    kodmax = models.CharField(max_length=10, blank=True, null=True)
    sng = models.CharField(max_length=1, blank=True, null=True)
    predel = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'reg_mvs'


class RegS(BaseModel):
    nomr3 = models.CharField(max_length=10, blank=True, null=True)
    okpob = models.CharField(max_length=10, blank=True, null=True)
    schet = models.CharField(max_length=20, blank=True, null=True)
    tsh = models.CharField(max_length=2, blank=True, null=True)
    ksh = models.CharField(max_length=20, blank=True, null=True)
    inn = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'reg_s'


class RegTi(BaseModel):
    adress = models.CharField(max_length=150, blank=True, null=True)
    telefon = models.CharField(max_length=12, blank=True, null=True)
    telegraf = models.CharField(max_length=50, blank=True, null=True)
    telefax = models.CharField(max_length=12, blank=True, null=True)
    telex = models.CharField(max_length=20, blank=True, null=True)
    zayv = models.CharField(max_length=80, blank=True, null=True)
    nomr1 = models.CharField(max_length=2, blank=True, null=True)
    nomr2 = models.CharField(max_length=4, blank=True, null=True)
    nomr3 = models.CharField(max_length=10, blank=True, null=True)
    psu = models.CharField(max_length=1, blank=True, null=True)
    okato = models.CharField(max_length=11, blank=True, null=True)
    okpobr = models.CharField(max_length=10, blank=True, null=True)
    schet1 = models.CharField(max_length=20, blank=True, null=True)
    korschr = models.CharField(max_length=20, blank=True, null=True)
    okpobv = models.CharField(max_length=10, blank=True, null=True)
    schet2 = models.CharField(max_length=20, blank=True, null=True)
    korschv = models.CharField(max_length=20, blank=True, null=True)
    kodtam = models.CharField(max_length=8, blank=True, null=True)
    datr = models.DateField(blank=True, null=True)
    ogrn = models.CharField(max_length=15, blank=True, null=True)
    inn = models.CharField(max_length=12, blank=True, null=True)
    kpp = models.CharField(max_length=9, blank=True, null=True)
    datn = models.DateField(blank=True, null=True)
    datm = models.DateField(blank=True, null=True)
    alfa2 = models.CharField(max_length=2, blank=True, null=True)
    post9 = models.CharField(max_length=9, blank=True, null=True)
    subcntry = models.CharField(max_length=35, blank=True, null=True)
    city = models.CharField(max_length=35, blank=True, null=True)
    street = models.CharField(max_length=35, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'reg_ti'


class RegTit(BaseModel):
    adress = models.CharField(max_length=150, blank=True, null=True)
    telefon = models.CharField(max_length=12, blank=True, null=True)
    telegraf = models.CharField(max_length=50, blank=True, null=True)
    telefax = models.CharField(max_length=12, blank=True, null=True)
    telex = models.CharField(max_length=20, blank=True, null=True)
    zayv = models.CharField(max_length=80, blank=True, null=True)
    nomr1 = models.CharField(max_length=2, blank=True, null=True)
    nomr2 = models.CharField(max_length=4, blank=True, null=True)
    nomr3 = models.CharField(max_length=10, blank=True, null=True)
    okpobr = models.CharField(max_length=10, blank=True, null=True)
    schet1 = models.CharField(max_length=20, blank=True, null=True)
    korschr = models.CharField(max_length=20, blank=True, null=True)
    okpobv = models.CharField(max_length=10, blank=True, null=True)
    schet2 = models.CharField(max_length=20, blank=True, null=True)
    korschv = models.CharField(max_length=20, blank=True, null=True)
    kodtam = models.CharField(max_length=8, blank=True, null=True)
    datr = models.DateField(blank=True, null=True)
    ogrn = models.CharField(max_length=15, blank=True, null=True)
    inn = models.CharField(max_length=12, blank=True, null=True)
    datn = models.DateField(blank=True, null=True)
    datm = models.DateField(blank=True, null=True)
    okato = models.CharField(max_length=11, blank=True, null=True)
    kpp = models.CharField(max_length=9, blank=True, null=True)
    alfa2 = models.CharField(max_length=2, blank=True, null=True)
    post9 = models.CharField(max_length=9, blank=True, null=True)
    subcntry = models.CharField(max_length=35, blank=True, null=True)
    city = models.CharField(max_length=35, blank=True, null=True)
    street = models.CharField(max_length=35, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'reg_tit'


class RegTi1(BaseModel):
    adress = models.CharField(max_length=150, blank=True, null=True)
    telefon = models.CharField(max_length=12, blank=True, null=True)
    telegraf = models.CharField(max_length=50, blank=True, null=True)
    telefax = models.CharField(max_length=12, blank=True, null=True)
    telex = models.CharField(max_length=20, blank=True, null=True)
    zayv = models.CharField(max_length=80, blank=True, null=True)
    nomr1 = models.CharField(max_length=2, blank=True, null=True)
    nomr2 = models.CharField(max_length=4, blank=True, null=True)
    nomr3 = models.CharField(max_length=10, blank=True, null=True)
    psu = models.CharField(max_length=1, blank=True, null=True)
    okato = models.CharField(max_length=11, blank=True, null=True)
    okpobr = models.CharField(max_length=10, blank=True, null=True)
    schet1 = models.CharField(max_length=20, blank=True, null=True)
    korschr = models.CharField(max_length=20, blank=True, null=True)
    okpobv = models.CharField(max_length=10, blank=True, null=True)
    schet2 = models.CharField(max_length=20, blank=True, null=True)
    korschv = models.CharField(max_length=20, blank=True, null=True)
    kodtam = models.CharField(max_length=8, blank=True, null=True)
    datr = models.DateField(blank=True, null=True)
    ogrn = models.CharField(max_length=15, blank=True, null=True)
    inn = models.CharField(max_length=12, blank=True, null=True)
    kpp = models.CharField(max_length=9, blank=True, null=True)
    datn = models.DateField(blank=True, null=True)
    datm = models.DateField(blank=True, null=True)
    alfa2 = models.CharField(max_length=2, blank=True, null=True)
    post9 = models.CharField(max_length=9, blank=True, null=True)
    subcntry = models.CharField(max_length=35, blank=True, null=True)
    city = models.CharField(max_length=35, blank=True, null=True)
    street = models.CharField(max_length=35, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'reg_ti~1'


class RegiK(BaseModel):
    itn = models.CharField(max_length=15, blank=True, null=True)
    data_uk = models.DateField(blank=True, null=True)
    name_ubed = models.CharField(max_length=100, blank=True, null=True)
    reg_nom = models.CharField(max_length=20, blank=True, null=True)
    ogrn = models.CharField(max_length=13, blank=True, null=True)
    inn = models.CharField(max_length=12, blank=True, null=True)
    kpp = models.CharField(max_length=9, blank=True, null=True)
    okato = models.CharField(max_length=11, blank=True, null=True)
    adres = models.CharField(max_length=100, blank=True, null=True)
    kodtam = models.CharField(max_length=8, blank=True, null=True)
    prim = models.CharField(max_length=250, blank=True, null=True)
    st_uk = models.CharField(max_length=25, blank=True, null=True)
    data_st_uk = models.DateField(blank=True, null=True)
    data_beg = models.DateField(blank=True, null=True)
    data_mod = models.DateField(blank=True, null=True)
    data_end = models.DateField(blank=True, null=True)
    crc = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'regi_k'


class Regpltls(BaseModel):
    inn = models.CharField(max_length=12, blank=True, null=True)
    naim = models.CharField(max_length=255, blank=True, null=True)
    datbegz = models.DateField(blank=True, null=True)
    datendz = models.DateField(blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'regpltls'


class RegtiTe(BaseModel):
    inn = models.CharField(max_length=12, blank=True, null=True)
    last_telef = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'regti_te'


class Reshdel(BaseModel):
    kresh = models.CharField(max_length=2, blank=True, null=True)
    nresh = models.CharField(max_length=70, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'reshdel'


class Rezultto(BaseModel):
    code = models.CharField(max_length=2, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'rezultto'


class Rezultto1(BaseModel):
    code = models.CharField(max_length=2, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'rezultto1'


class Rmbt(BaseModel):
    code = models.CharField(max_length=8, blank=True, null=True)
    nsvid = models.CharField(max_length=9, blank=True, null=True)
    pr_per = models.CharField(max_length=1, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)
    idel = models.CharField(max_length=1, blank=True, null=True)
    opf = models.CharField(max_length=8, blank=True, null=True)
    owner = models.CharField(max_length=255, blank=True, null=True)
    adr_own = models.CharField(max_length=255, blank=True, null=True)
    adrpocht = models.CharField(max_length=255, blank=True, null=True)
    ind_adr = models.CharField(max_length=6, blank=True, null=True)
    telef = models.CharField(max_length=50, blank=True, null=True)
    telefax = models.CharField(max_length=50, blank=True, null=True)
    website = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=25, blank=True, null=True)
    ogrn = models.CharField(max_length=15, blank=True, null=True)
    inn = models.CharField(max_length=12, blank=True, null=True)
    kpp = models.CharField(max_length=9, blank=True, null=True)
    adr_mbt = models.CharField(max_length=255, blank=True, null=True)
    ind_mbt = models.CharField(max_length=6, blank=True, null=True)
    adr_skl = models.CharField(max_length=255, blank=True, null=True)
    ind_skl = models.CharField(max_length=6, blank=True, null=True)
    s_mbt = models.DecimalField(default=0.00, max_digits=9, decimal_places=3, blank=True, null=True)
    s_tz = models.DecimalField(default=0.00, max_digits=9, decimal_places=3, blank=True, null=True)
    s_skl = models.CharField(max_length=255, blank=True, null=True)
    rf_outp = models.CharField(max_length=9, blank=True, null=True)
    doc_tp = models.CharField(max_length=100, blank=True, null=True)
    date_mod = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'rmbt'


class Rmd(BaseModel):
    kodt = models.CharField(max_length=8, blank=True, null=True)
    nlic = models.CharField(max_length=12, blank=True, null=True)
    dbegin = models.DateField(blank=True, null=True)
    dend = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=75, blank=True, null=True)
    owner = models.CharField(max_length=8, blank=True, null=True)
    kodtn = models.CharField(max_length=8, blank=True, null=True)
    kodtold = models.CharField(max_length=8, blank=True, null=True)
    sovam = models.CharField(max_length=9, blank=True, null=True)
    vidtrans = models.CharField(max_length=30, blank=True, null=True)
    fax = models.CharField(max_length=20, blank=True, null=True)
    teleks = models.CharField(max_length=20, blank=True, null=True)
    telefon = models.CharField(max_length=20, blank=True, null=True)
    pr_per = models.CharField(max_length=1, blank=True, null=True)
    sign_ord = models.CharField(max_length=30, blank=True, null=True)
    n_order = models.CharField(max_length=20, blank=True, null=True)
    d_order = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'rmd'


class RmdG(BaseModel):
    kontr = models.CharField(max_length=1, blank=True, null=True)
    kodt = models.CharField(max_length=8, blank=True, null=True)
    nlic = models.CharField(max_length=12, blank=True, null=True)
    dbegin = models.DateField(blank=True, null=True)
    dend = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=75, blank=True, null=True)
    owner = models.CharField(max_length=8, blank=True, null=True)
    kodtn = models.CharField(max_length=8, blank=True, null=True)
    kodtold = models.CharField(max_length=8, blank=True, null=True)
    sovam = models.CharField(max_length=9, blank=True, null=True)
    fax = models.CharField(max_length=20, blank=True, null=True)
    teleks = models.CharField(max_length=20, blank=True, null=True)
    telefon = models.CharField(max_length=20, blank=True, null=True)
    pr_per = models.CharField(max_length=1, blank=True, null=True)
    vidtrans = models.CharField(max_length=30, blank=True, null=True)
    sign_ord = models.CharField(max_length=30, blank=True, null=True)
    n_order = models.CharField(max_length=20, blank=True, null=True)
    d_order = models.DateField(blank=True, null=True)
    fname = models.CharField(max_length=12, blank=True, null=True)
    fdate = models.DateField(blank=True, null=True)
    dload = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'rmd_g'


class Rmtotok(BaseModel):
    kindoford = models.CharField(max_length=2, blank=True, null=True)
    n_order = models.CharField(max_length=12, blank=True, null=True)
    d_order = models.DateField(blank=True, null=True)
    partno = models.CharField(max_length=1, blank=True, null=True)
    dbegin = models.DateField(blank=True, null=True)
    dend = models.DateField(blank=True, null=True)
    tnvedcode = models.CharField(max_length=10, blank=True, null=True)
    tnvedexcep = models.CharField(max_length=10, blank=True, null=True)
    custcode = models.CharField(max_length=8, blank=True, null=True)
    n_lic = models.CharField(max_length=25, blank=True, null=True)
    transcode = models.CharField(max_length=2, blank=True, null=True)
    okato = models.CharField(max_length=5, blank=True, null=True)
    country = models.CharField(max_length=3, blank=True, null=True)
    tnvedoksmt = models.CharField(max_length=3, blank=True, null=True)
    kindbase = models.CharField(max_length=20, blank=True, null=True)
    prim = models.CharField(max_length=250, blank=True, null=True)
    dcustoms = models.DateField(blank=True, null=True)
    tnvedbegin = models.DateField(blank=True, null=True)
    dcustomend = models.DateField(blank=True, null=True)
    tnvedend = models.DateField(blank=True, null=True)
    tnvexbegin = models.DateField(blank=True, null=True)
    tnvexend = models.DateField(blank=True, null=True)
    transbegin = models.DateField(blank=True, null=True)
    transend = models.DateField(blank=True, null=True)
    okatobegin = models.DateField(blank=True, null=True)
    okatoend = models.DateField(blank=True, null=True)
    cntrybegin = models.DateField(blank=True, null=True)
    cntryend = models.DateField(blank=True, null=True)
    cntrtbegin = models.DateField(blank=True, null=True)
    cntrtend = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'rmtotok'


class Role(BaseModel):
    code = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    datn = models.DateField(blank=True, null=True)
    dats = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'role'


class Rpsi(BaseModel):
    cod = models.CharField(max_length=8, blank=True, null=True)
    naim = models.CharField(max_length=40, blank=True, null=True)
    fio = models.CharField(max_length=20, blank=True, null=True)
    direk = models.CharField(max_length=8, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'rpsi'


class RskCrit(BaseModel):
    kod = models.CharField(max_length=4, blank=True, null=True)
    naim = models.CharField(max_length=255, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'rsk_crit'


class RskFinp(BaseModel):
    gr013 = models.CharField(max_length=2, blank=True, null=True)
    gr014 = models.DateField(blank=True, null=True)
    gr015 = models.CharField(max_length=5, blank=True, null=True)
    gr0151 = models.DecimalField(default=0.00, max_digits=3, decimal_places=0, blank=True, null=True)
    kod_inf = models.CharField(max_length=1, blank=True, null=True)
    npp_str = models.DecimalField(default=0.00, max_digits=10, decimal_places=0, blank=True, null=True)
    text_inf = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'rsk_finp'


class RskMera(BaseModel):
    kod = models.CharField(max_length=2, blank=True, null=True)
    naim = models.CharField(max_length=255, blank=True, null=True)
    priznak = models.BooleanField(blank=True, null=True)
    ratio = models.BooleanField(blank=True, null=True)
    rtuspror = models.BooleanField(blank=True, null=True)
    rtupr = models.BooleanField(blank=True, null=True)
    sprsign = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'rsk_mera'


class RskNdpd(BaseModel):
    kod_spdr = models.CharField(max_length=2, blank=True, null=True)
    kod = models.CharField(max_length=4, blank=True, null=True)
    naim = models.CharField(max_length=250, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'rsk_ndpd'


class RskNinf(BaseModel):
    kod = models.CharField(max_length=4, blank=True, null=True)
    naim = models.CharField(max_length=150, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'rsk_ninf'


class RskNmb(BaseModel):
    gr013 = models.CharField(max_length=2, blank=True, null=True)
    gr014 = models.DateField(blank=True, null=True)
    gr015 = models.CharField(max_length=5, blank=True, null=True)
    name = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'rsk_nmb'


class RskNpm(BaseModel):
    kod = models.CharField(max_length=2, blank=True, null=True)
    naim = models.CharField(max_length=250, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'rsk_npm'


class RskPrim(BaseModel):
    kod = models.CharField(max_length=3, blank=True, null=True)
    typepr = models.CharField(max_length=1, blank=True, null=True)
    naim = models.TextField(blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'rsk_prim'


class RskRsmr(BaseModel):
    gr013 = models.CharField(max_length=2, blank=True, null=True)
    gr0131 = models.CharField(max_length=5, blank=True, null=True)
    gr014 = models.DateField(blank=True, null=True)
    gr015 = models.CharField(max_length=5, blank=True, null=True)
    gr0151 = models.DecimalField(default=0.00, max_digits=3, decimal_places=0, blank=True, null=True)
    gr051 = models.CharField(max_length=3, blank=True, null=True)
    gr0511 = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    gr0512 = models.DecimalField(default=0.00, max_digits=2, decimal_places=0, blank=True, null=True)
    gr0513 = models.CharField(max_length=3, blank=True, null=True)
    usesign = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'rsk_rsmr'


class RskRsnd(BaseModel):
    gr013 = models.CharField(max_length=2, blank=True, null=True)
    gr0131 = models.CharField(max_length=5, blank=True, null=True)
    gr014 = models.DateField(blank=True, null=True)
    gr015 = models.CharField(max_length=5, blank=True, null=True)
    gr0151 = models.DecimalField(default=0.00, max_digits=3, decimal_places=0, blank=True, null=True)
    gr_podr = models.CharField(max_length=2, blank=True, null=True)
    gr_nd = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'rsk_rsnd'


class RskRspr(BaseModel):
    gr013 = models.CharField(max_length=2, blank=True, null=True)
    gr0131 = models.CharField(max_length=5, blank=True, null=True)
    gr014 = models.DateField(blank=True, null=True)
    gr015 = models.CharField(max_length=5, blank=True, null=True)
    gr0151 = models.DecimalField(default=0.00, max_digits=3, decimal_places=0, blank=True, null=True)
    gr041 = models.CharField(max_length=4, blank=True, null=True)
    gr_podr = models.CharField(max_length=2, blank=True, null=True)
    kod_proc = models.CharField(max_length=2, blank=True, null=True)
    gr_dbeg = models.DateField(blank=True, null=True)
    gr_dend = models.DateField(blank=True, null=True)
    ver_dend = models.DateField(blank=True, null=True)
    gr_prf = models.CharField(max_length=1, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'rsk_rspr'


class RskSpdr0(BaseModel):
    kod = models.CharField(max_length=2, blank=True, null=True)
    code = models.CharField(max_length=8, blank=True, null=True)
    kr_naim = models.CharField(max_length=10, blank=True, null=True)
    naim = models.CharField(max_length=100, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'rsk_spdr'


class RskTprc(BaseModel):
    kod = models.CharField(max_length=2, blank=True, null=True)
    naim = models.CharField(max_length=100, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'rsk_tprc'


class Rskrmera(BaseModel):
    kod_pr = models.CharField(max_length=2, blank=True, null=True)
    kod = models.CharField(max_length=2, blank=True, null=True)
    naim = models.CharField(max_length=255, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'rskrmera'


class Rskrsdsm(BaseModel):
    gr013 = models.CharField(max_length=2, blank=True, null=True)
    gr0131 = models.CharField(max_length=5, blank=True, null=True)
    gr014 = models.DateField(blank=True, null=True)
    gr015 = models.CharField(max_length=5, blank=True, null=True)
    gr0151 = models.DecimalField(default=0.00, max_digits=3, decimal_places=0, blank=True, null=True)
    gr051 = models.CharField(max_length=3, blank=True, null=True)
    kodatr = models.CharField(max_length=2, blank=True, null=True)
    textatr = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'rskrsdsm'


class Rskrsprc(BaseModel):
    gr013 = models.CharField(max_length=2, blank=True, null=True)
    gr014 = models.DateField(blank=True, null=True)
    gr015 = models.CharField(max_length=5, blank=True, null=True)
    gr0151 = models.DecimalField(default=0.00, max_digits=3, decimal_places=0, blank=True, null=True)
    kod_proc = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'rskrsprc'


class Rskspdr(BaseModel):
    kod_srdr = models.CharField(max_length=2, blank=True, null=True)
    naimspdr = models.CharField(max_length=255, blank=True, null=True)
    krnmcstm = models.CharField(max_length=50, blank=True, null=True)
    krnmrtu = models.CharField(max_length=50, blank=True, null=True)
    krnmfts = models.CharField(max_length=10, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'rskspdr'


class Rsksppri(BaseModel):
    kod_spdr = models.CharField(max_length=2, blank=True, null=True)
    kod_prim = models.CharField(max_length=3, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'rsksppri'


class Rsktmera(BaseModel):
    kod = models.CharField(max_length=2, blank=True, null=True)
    naim = models.CharField(max_length=255, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'rsktmera'


class Rskxdosm(BaseModel):
    kod = models.CharField(max_length=2, blank=True, null=True)
    naim = models.CharField(max_length=30, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'rskxdosm'


class Rskzdosm(BaseModel):
    kodxdosm = models.CharField(max_length=2, blank=True, null=True)
    kod = models.CharField(max_length=6, blank=True, null=True)
    naim = models.CharField(max_length=255, blank=True, null=True)
    spec = models.DecimalField(default=0.00, max_digits=9, decimal_places=3, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'rskzdosm'


class RsnBpos(BaseModel):
    buuid = models.CharField(max_length=36, blank=True, null=True)
    bguid = models.CharField(max_length=36, blank=True, null=True)
    bactive = models.BooleanField(blank=True, null=True)
    blast = models.BooleanField(blank=True, null=True)
    bstatus = models.CharField(max_length=3, blank=True, null=True)
    bcreatedat = models.DateField(blank=True, null=True)
    bupdatedat = models.DateField(blank=True, null=True)
    bprevious = models.CharField(max_length=36, blank=True, null=True)
    bnext = models.CharField(max_length=36, blank=True, null=True)
    fullname = models.CharField(max_length=254, blank=True, null=True)
    shortname = models.CharField(max_length=254, blank=True, null=True)
    engname = models.CharField(max_length=254, blank=True, null=True)
    typ = models.CharField(max_length=36, blank=True, null=True)
    orgcode = models.CharField(max_length=50, blank=True, null=True)
    juraddcnt = models.CharField(max_length=36, blank=True, null=True)
    juraddress = models.CharField(max_length=254, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    fax = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'rsn_bpos'


class RsnBuss(BaseModel):
    buuid = models.CharField(max_length=36, blank=True, null=True)
    bguid = models.CharField(max_length=36, blank=True, null=True)
    bactive = models.BooleanField(blank=True, null=True)
    blast = models.BooleanField(blank=True, null=True)
    bstatus = models.CharField(max_length=3, blank=True, null=True)
    bcreatedat = models.DateField(blank=True, null=True)
    bupdatedat = models.DateField(blank=True, null=True)
    bprevious = models.CharField(max_length=36, blank=True, null=True)
    bnext = models.CharField(max_length=36, blank=True, null=True)
    firmname = models.CharField(max_length=254, blank=True, null=True)
    fio = models.CharField(max_length=254, blank=True, null=True)
    passport = models.CharField(max_length=100, blank=True, null=True)
    inn = models.CharField(max_length=20, blank=True, null=True)
    kpp = models.CharField(max_length=20, blank=True, null=True)
    countryuui = models.CharField(max_length=36, blank=True, null=True)
    countrygui = models.CharField(max_length=36, blank=True, null=True)
    regionuuid = models.CharField(max_length=36, blank=True, null=True)
    regionguid = models.CharField(max_length=36, blank=True, null=True)
    actreguuid = models.CharField(max_length=36, blank=True, null=True)
    actregguid = models.CharField(max_length=36, blank=True, null=True)
    juraddress = models.CharField(max_length=254, blank=True, null=True)
    actaddress = models.CharField(max_length=254, blank=True, null=True)
    typ = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'rsn_buss'


class RsnCntr(BaseModel):
    buuid = models.CharField(max_length=36, blank=True, null=True)
    bguid = models.CharField(max_length=36, blank=True, null=True)
    bactive = models.BooleanField(blank=True, null=True)
    blast = models.BooleanField(blank=True, null=True)
    bstatus = models.CharField(max_length=3, blank=True, null=True)
    bcreatedat = models.DateField(blank=True, null=True)
    bupdatedat = models.DateField(blank=True, null=True)
    bprevious = models.CharField(max_length=36, blank=True, null=True)
    bnext = models.CharField(max_length=36, blank=True, null=True)
    naim = models.CharField(max_length=100, blank=True, null=True)
    fullname = models.CharField(max_length=100, blank=True, null=True)
    engname = models.CharField(max_length=100, blank=True, null=True)
    cod = models.CharField(max_length=2, blank=True, null=True)
    code3 = models.CharField(max_length=3, blank=True, null=True)
    iscu = models.BooleanField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'rsn_cntr'


class RsnEntf(BaseModel):
    buuid = models.CharField(max_length=36, blank=True, null=True)
    bguid = models.CharField(max_length=36, blank=True, null=True)
    bactive = models.BooleanField(blank=True, null=True)
    blast = models.BooleanField(blank=True, null=True)
    bstatus = models.CharField(max_length=3, blank=True, null=True)
    bcreatedat = models.DateField(blank=True, null=True)
    bupdatedat = models.DateField(blank=True, null=True)
    bprevious = models.CharField(max_length=36, blank=True, null=True)
    bnext = models.CharField(max_length=36, blank=True, null=True)
    naim = models.CharField(max_length=254, blank=True, null=True)
    engname = models.CharField(max_length=254, blank=True, null=True)
    activity = models.CharField(max_length=254, blank=True, null=True)
    engactiv = models.CharField(max_length=254, blank=True, null=True)
    adres = models.CharField(max_length=254, blank=True, null=True)
    countryuui = models.CharField(max_length=36, blank=True, null=True)
    countrygui = models.CharField(max_length=36, blank=True, null=True)
    regionuuid = models.CharField(max_length=36, blank=True, null=True)
    regionguid = models.CharField(max_length=36, blank=True, null=True)
    numberlist = models.CharField(max_length=36, blank=True, null=True)
    typ = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'rsn_entf'


class RsnEntr(BaseModel):
    buuid = models.CharField(max_length=36, blank=True, null=True)
    bguid = models.CharField(max_length=36, blank=True, null=True)
    bactive = models.BooleanField(blank=True, null=True)
    blast = models.BooleanField(blank=True, null=True)
    bstatus = models.CharField(max_length=3, blank=True, null=True)
    bcreatedat = models.DateField(blank=True, null=True)
    bupdatedat = models.DateField(blank=True, null=True)
    bprevious = models.CharField(max_length=36, blank=True, null=True)
    bnext = models.CharField(max_length=36, blank=True, null=True)
    naim = models.CharField(max_length=254, blank=True, null=True)
    engname = models.CharField(max_length=254, blank=True, null=True)
    activity = models.CharField(max_length=254, blank=True, null=True)
    engactiv = models.CharField(max_length=254, blank=True, null=True)
    adres = models.CharField(max_length=254, blank=True, null=True)
    countryuui = models.CharField(max_length=36, blank=True, null=True)
    countrygui = models.CharField(max_length=36, blank=True, null=True)
    regionuuid = models.CharField(max_length=36, blank=True, null=True)
    regionguid = models.CharField(max_length=36, blank=True, null=True)
    numberlist = models.CharField(max_length=36, blank=True, null=True)
    typ = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'rsn_entr'


class RsnFlab(BaseModel):
    buuid = models.CharField(max_length=36, blank=True, null=True)
    bguid = models.CharField(max_length=36, blank=True, null=True)
    bactive = models.BooleanField(blank=True, null=True)
    blast = models.BooleanField(blank=True, null=True)
    bstatus = models.CharField(max_length=3, blank=True, null=True)
    bcreatedat = models.DateField(blank=True, null=True)
    bupdatedat = models.DateField(blank=True, null=True)
    bprevious = models.CharField(max_length=36, blank=True, null=True)
    bnext = models.CharField(max_length=36, blank=True, null=True)
    fullname = models.CharField(max_length=254, blank=True, null=True)
    shortname = models.CharField(max_length=254, blank=True, null=True)
    engname = models.CharField(max_length=254, blank=True, null=True)
    typ = models.CharField(max_length=36, blank=True, null=True)
    orgcode = models.CharField(max_length=50, blank=True, null=True)
    juraddcnt = models.CharField(max_length=36, blank=True, null=True)
    juraddress = models.CharField(max_length=254, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    fax = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'rsn_flab'


class RsnOrg(BaseModel):
    buuid = models.CharField(max_length=36, blank=True, null=True)
    bguid = models.CharField(max_length=36, blank=True, null=True)
    bactive = models.BooleanField(blank=True, null=True)
    blast = models.BooleanField(blank=True, null=True)
    bstatus = models.CharField(max_length=3, blank=True, null=True)
    bcreatedat = models.DateField(blank=True, null=True)
    bupdatedat = models.DateField(blank=True, null=True)
    bprevious = models.CharField(max_length=36, blank=True, null=True)
    bnext = models.CharField(max_length=36, blank=True, null=True)
    fullname = models.CharField(max_length=254, blank=True, null=True)
    shortname = models.CharField(max_length=254, blank=True, null=True)
    engname = models.CharField(max_length=254, blank=True, null=True)
    typ = models.CharField(max_length=36, blank=True, null=True)
    orgcode = models.CharField(max_length=50, blank=True, null=True)
    juraddcnt = models.CharField(max_length=36, blank=True, null=True)
    juraddress = models.CharField(max_length=254, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    fax = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'rsn_org'


class RsnOrgt(BaseModel):
    uuid = models.CharField(max_length=36, blank=True, null=True)
    fullname = models.CharField(max_length=100, blank=True, null=True)
    shortname = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'rsn_orgt'


class RsnProd(BaseModel):
    buuid = models.CharField(max_length=36, blank=True, null=True)
    bguid = models.CharField(max_length=36, blank=True, null=True)
    bactive = models.BooleanField(blank=True, null=True)
    blast = models.BooleanField(blank=True, null=True)
    bstatus = models.CharField(max_length=3, blank=True, null=True)
    bcreatedat = models.DateField(blank=True, null=True)
    bupdatedat = models.DateField(blank=True, null=True)
    bprevious = models.CharField(max_length=36, blank=True, null=True)
    bnext = models.CharField(max_length=36, blank=True, null=True)
    naim = models.CharField(max_length=254, blank=True, null=True)
    cod = models.CharField(max_length=100, blank=True, null=True)
    engname = models.CharField(max_length=254, blank=True, null=True)
    prodtype = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'rsn_prod'


class RsnSpro(BaseModel):
    buuid = models.CharField(max_length=36, blank=True, null=True)
    bguid = models.CharField(max_length=36, blank=True, null=True)
    bactive = models.BooleanField(blank=True, null=True)
    blast = models.BooleanField(blank=True, null=True)
    bstatus = models.CharField(max_length=3, blank=True, null=True)
    bcreatedat = models.DateField(blank=True, null=True)
    bupdatedat = models.DateField(blank=True, null=True)
    bprevious = models.CharField(max_length=36, blank=True, null=True)
    bnext = models.CharField(max_length=36, blank=True, null=True)
    naim = models.CharField(max_length=254, blank=True, null=True)
    cod = models.CharField(max_length=100, blank=True, null=True)
    prodguid = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'rsn_spro'


class RsnTarg(BaseModel):
    buuid = models.CharField(max_length=36, blank=True, null=True)
    bguid = models.CharField(max_length=36, blank=True, null=True)
    bactive = models.BooleanField(blank=True, null=True)
    blast = models.BooleanField(blank=True, null=True)
    bstatus = models.CharField(max_length=3, blank=True, null=True)
    bcreatedat = models.DateField(blank=True, null=True)
    bupdatedat = models.DateField(blank=True, null=True)
    bprevious = models.CharField(max_length=36, blank=True, null=True)
    bnext = models.CharField(max_length=36, blank=True, null=True)
    naim = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'rsn_targ'


class RsnTdep(BaseModel):
    buuid = models.CharField(max_length=36, blank=True, null=True)
    bguid = models.CharField(max_length=36, blank=True, null=True)
    bactive = models.BooleanField(blank=True, null=True)
    blast = models.BooleanField(blank=True, null=True)
    bstatus = models.CharField(max_length=3, blank=True, null=True)
    bcreatedat = models.DateField(blank=True, null=True)
    bupdatedat = models.DateField(blank=True, null=True)
    bprevious = models.CharField(max_length=36, blank=True, null=True)
    bnext = models.CharField(max_length=36, blank=True, null=True)
    fullname = models.CharField(max_length=254, blank=True, null=True)
    shortname = models.CharField(max_length=254, blank=True, null=True)
    engname = models.CharField(max_length=254, blank=True, null=True)
    typ = models.CharField(max_length=36, blank=True, null=True)
    orgcode = models.CharField(max_length=50, blank=True, null=True)
    juraddcnt = models.CharField(max_length=36, blank=True, null=True)
    juraddress = models.CharField(max_length=254, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    fax = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'rsn_tdep'


class RsnTsto(BaseModel):
    buuid = models.CharField(max_length=36, blank=True, null=True)
    bguid = models.CharField(max_length=36, blank=True, null=True)
    bactive = models.BooleanField(blank=True, null=True)
    blast = models.BooleanField(blank=True, null=True)
    bstatus = models.CharField(max_length=3, blank=True, null=True)
    bcreatedat = models.DateField(blank=True, null=True)
    bupdatedat = models.DateField(blank=True, null=True)
    bprevious = models.CharField(max_length=36, blank=True, null=True)
    bnext = models.CharField(max_length=36, blank=True, null=True)
    naim = models.CharField(max_length=254, blank=True, null=True)
    shortname = models.CharField(max_length=254, blank=True, null=True)
    typ = models.CharField(max_length=1, blank=True, null=True)
    countrygui = models.CharField(max_length=36, blank=True, null=True)
    regionuuid = models.CharField(max_length=36, blank=True, null=True)
    regionguid = models.CharField(max_length=36, blank=True, null=True)
    actaddress = models.CharField(max_length=254, blank=True, null=True)
    chiefpost = models.CharField(max_length=254, blank=True, null=True)
    chieffio = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'rsn_tsto'


class RsnUnit(BaseModel):
    buuid = models.CharField(max_length=36, blank=True, null=True)
    bguid = models.CharField(max_length=36, blank=True, null=True)
    bactive = models.BooleanField(blank=True, null=True)
    blast = models.BooleanField(blank=True, null=True)
    bstatus = models.CharField(max_length=3, blank=True, null=True)
    bcreatedat = models.DateField(blank=True, null=True)
    bupdatedat = models.DateField(blank=True, null=True)
    bprevious = models.CharField(max_length=36, blank=True, null=True)
    bnext = models.CharField(max_length=36, blank=True, null=True)
    naim = models.CharField(max_length=25, blank=True, null=True)
    fullname = models.CharField(max_length=50, blank=True, null=True)
    commonunit = models.CharField(max_length=36, blank=True, null=True)
    factor = models.DecimalField(default=0.00, max_digits=20, decimal_places=5, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'rsn_unit'


class RsnVlab(BaseModel):
    buuid = models.CharField(max_length=36, blank=True, null=True)
    bguid = models.CharField(max_length=36, blank=True, null=True)
    bactive = models.BooleanField(blank=True, null=True)
    blast = models.BooleanField(blank=True, null=True)
    bstatus = models.CharField(max_length=3, blank=True, null=True)
    bcreatedat = models.DateField(blank=True, null=True)
    bupdatedat = models.DateField(blank=True, null=True)
    bprevious = models.CharField(max_length=36, blank=True, null=True)
    bnext = models.CharField(max_length=36, blank=True, null=True)
    fullname = models.CharField(max_length=254, blank=True, null=True)
    shortname = models.CharField(max_length=254, blank=True, null=True)
    engname = models.CharField(max_length=254, blank=True, null=True)
    typ = models.CharField(max_length=36, blank=True, null=True)
    orgcode = models.CharField(max_length=50, blank=True, null=True)
    juraddcnt = models.CharField(max_length=36, blank=True, null=True)
    juraddress = models.CharField(max_length=254, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    fax = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'rsn_vlab'


# class RstrGrf(BaseModel):
#
#     class Meta:
#         abstract = True
#         # db_table = 'rstr_grf'


class RstrH(BaseModel):
    regnom = models.CharField(max_length=25, blank=True, null=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    namecont = models.CharField(max_length=50, blank=True, null=True)
    dolgcont = models.CharField(max_length=20, blank=True, null=True)
    phoncont = models.CharField(max_length=50, blank=True, null=True)
    inn = models.CharField(max_length=12, blank=True, null=True)
    kpp = models.CharField(max_length=9, blank=True, null=True)
    tip_dov = models.CharField(max_length=2, blank=True, null=True)
    participid = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'rstr_h'


class RstrKat(BaseModel):
    tip_dov = models.CharField(max_length=2, blank=True, null=True)
    desc_dov = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'rstr_kat'


class RstrLic(BaseModel):
    g31_12 = models.CharField(max_length=50, blank=True, null=True)
    nld = models.CharField(max_length=50, blank=True, null=True)
    dld = models.DateField(blank=True, null=True)
    naim = models.CharField(max_length=80, blank=True, null=True)
    adr = models.CharField(max_length=80, blank=True, null=True)
    telefon = models.CharField(max_length=12, blank=True, null=True)
    fax = models.CharField(max_length=12, blank=True, null=True)
    e_mail = models.CharField(max_length=50, blank=True, null=True)
    fio = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'rstr_lic'


class RstrN(BaseModel):
    regnom = models.CharField(max_length=25, blank=True, null=True)
    nletter = models.CharField(max_length=25, blank=True, null=True)
    dletter = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'rstr_n'


class RstrOis(BaseModel):
    regnom = models.CharField(max_length=25, blank=True, null=True)
    g31_12 = models.CharField(max_length=50, blank=True, null=True)
    note = models.CharField(max_length=100, blank=True, null=True)
    npravo = models.CharField(max_length=10, blank=True, null=True)
    dpravo = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=254, blank=True, null=True)
    inn = models.CharField(max_length=12, blank=True, null=True)
    kpp = models.CharField(max_length=9, blank=True, null=True)
    namel = models.CharField(max_length=254, blank=True, null=True)
    address = models.CharField(max_length=254, blank=True, null=True)
    addressl = models.CharField(max_length=254, blank=True, null=True)
    addressu = models.CharField(max_length=254, blank=True, null=True)
    mktu = models.CharField(max_length=254, blank=True, null=True)
    namet = models.TextField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)
    comm = models.TextField(blank=True, null=True)
    participid = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'rstr_ois'


class RstrTov(BaseModel):
    regnom = models.CharField(max_length=25, blank=True, null=True)
    g33 = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'rstr_tov'


class RstrTz(BaseModel):
    g31_12 = models.CharField(max_length=50, blank=True, null=True)
    regnom = models.CharField(max_length=20, blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)
    normdok = models.CharField(max_length=30, blank=True, null=True)
    normdate = models.DateField(blank=True, null=True)
    kodmkty = models.CharField(max_length=2, blank=True, null=True)
    nametov = models.CharField(max_length=80, blank=True, null=True)
    naim = models.CharField(max_length=80, blank=True, null=True)
    adr = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'rstr_tz'


class Rstrpath(BaseModel):
    g31_12 = models.CharField(max_length=50, blank=True, null=True)
    nld = models.CharField(max_length=50, blank=True, null=True)
    dld = models.DateField(blank=True, null=True)
    g33 = models.CharField(max_length=10, blank=True, null=True)
    npp = models.CharField(max_length=10, blank=True, null=True)
    strn = models.CharField(max_length=3, blank=True, null=True)
    soato = models.CharField(max_length=4, blank=True, null=True)
    okato = models.CharField(max_length=5, blank=True, null=True)
    ktam = models.CharField(max_length=8, blank=True, null=True)
    vid_tr = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'rstrpath'


class SExhib(BaseModel):
    ogrn = models.CharField(max_length=15, blank=True, null=True)
    inn = models.CharField(max_length=12, blank=True, null=True)
    kpp = models.CharField(max_length=9, blank=True, null=True)
    okpo = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=80, blank=True, null=True)
    okato_l = models.CharField(max_length=11, blank=True, null=True)
    address_l = models.CharField(max_length=80, blank=True, null=True)
    okato_f = models.CharField(max_length=11, blank=True, null=True)
    address_f = models.CharField(max_length=80, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 's_exhib'


class SExhid(BaseModel):
    inn = models.CharField(max_length=12, blank=True, null=True)
    kpp = models.CharField(max_length=9, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    code = models.CharField(max_length=8, blank=True, null=True)
    bktlic = models.CharField(max_length=5, blank=True, null=True)
    bnpplic = models.DecimalField(default=0.00, max_digits=4, decimal_places=0, blank=True, null=True)
    bdbegin = models.DateField(blank=True, null=True)
    bncoplic = models.DecimalField(default=0.00, max_digits=3, decimal_places=0, blank=True, null=True)
    nlic = models.CharField(max_length=25, blank=True, null=True)
    pr_per = models.CharField(max_length=1, blank=True, null=True)
    dbegin = models.DateField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    data1 = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 's_exhid'


class SObutp(BaseModel):
    code = models.CharField(max_length=6, blank=True, null=True)
    naim = models.TextField(blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 's_obutp'


class Sbj(BaseModel):
    sbj_id = models.DecimalField(default=0.00, max_digits=15, decimal_places=0, blank=True, null=True)
    itn = models.CharField(max_length=13, blank=True, null=True)
    inn = models.CharField(max_length=12, blank=True, null=True)
    kpp = models.CharField(max_length=9, blank=True, null=True)
    ogrn = models.CharField(max_length=15, blank=True, null=True)
    sname = models.CharField(max_length=254, blank=True, null=True)
    inegrul = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    oneday = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'sbj'


class SbjCst(BaseModel):
    inn = models.CharField(max_length=12, blank=True, null=True)
    kod_stat = models.CharField(max_length=2, blank=True, null=True)
    kod_val = models.CharField(max_length=4, blank=True, null=True)
    kod_tam = models.CharField(max_length=8, blank=True, null=True)
    docbeg = models.CharField(max_length=16, blank=True, null=True)
    docbegdt = models.DateField(blank=True, null=True)
    docend = models.CharField(max_length=16, blank=True, null=True)
    docenddt = models.DateField(blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'sbj_cst'


class SbjExt(BaseModel):
    inn = models.CharField(max_length=12, blank=True, null=True)
    zerobal = models.CharField(max_length=1, blank=True, null=True)
    innclosed = models.CharField(max_length=1, blank=True, null=True)
    innvoid = models.CharField(max_length=1, blank=True, null=True)
    egrulst_id = models.DecimalField(default=0.00, max_digits=15, decimal_places=0, blank=True, null=True)
    docbeg = models.CharField(max_length=16, blank=True, null=True)
    docbegdt = models.DateField(blank=True, null=True)
    docend = models.CharField(max_length=16, blank=True, null=True)
    docenddt = models.DateField(blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    kod_kateg = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'sbj_ext'


class SbjRole(BaseModel):
    sbj_id = models.DecimalField(default=0.00, max_digits=15, decimal_places=0, blank=True, null=True)
    scode = models.CharField(max_length=9, blank=True, null=True)
    rcode = models.CharField(max_length=30, blank=True, null=True)
    datn = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'sbj_role'


class SbxDel(BaseModel):
    st = models.CharField(max_length=2, blank=True, null=True)
    kodt = models.CharField(max_length=8, blank=True, null=True)
    namt = models.CharField(max_length=30, blank=True, null=True)
    itam = models.CharField(max_length=1, blank=True, null=True)
    typ_doc = models.CharField(max_length=1, blank=True, null=True)
    nlic = models.CharField(max_length=25, blank=True, null=True)
    pr_per = models.CharField(max_length=1, blank=True, null=True)
    dbegin = models.DateField(blank=True, null=True)
    dend = models.DateField(blank=True, null=True)
    idel = models.CharField(max_length=1, blank=True, null=True)
    types = models.CharField(max_length=1, blank=True, null=True)
    areas = models.DecimalField(default=0.00, max_digits=9, decimal_places=1, blank=True, null=True)
    volume = models.DecimalField(default=0.00, max_digits=9, decimal_places=1, blank=True, null=True)
    owner = models.CharField(max_length=255, blank=True, null=True)
    adrown = models.TextField(blank=True, null=True)
    telefon = models.CharField(max_length=50, blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    adrs = models.TextField(blank=True, null=True)
    telefs = models.CharField(max_length=30, blank=True, null=True)
    iakciz = models.CharField(max_length=1, blank=True, null=True)
    asovam = models.CharField(max_length=8, blank=True, null=True)
    date_mod = models.DateField(blank=True, null=True)
    vidtrans = models.CharField(max_length=30, blank=True, null=True)
    pr441pril3 = models.CharField(max_length=1, blank=True, null=True)
    ata = models.CharField(max_length=1, blank=True, null=True)
    d_isl = models.DateField(blank=True, null=True)
    ogrn = models.CharField(max_length=15, blank=True, null=True)
    inn = models.CharField(max_length=20, blank=True, null=True)
    kpp = models.CharField(max_length=9, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'sbx_del'


class Sdelka(BaseModel):
    kod = models.CharField(max_length=3, blank=True, null=True)
    gr_vd = models.CharField(max_length=2, blank=True, null=True)
    naim = models.CharField(max_length=250, blank=True, null=True)
    pr_sdel = models.CharField(max_length=2, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'sdelka'


class Selfnsi1(BaseModel):
    field1 = models.CharField(max_length=58, blank=True, null=True)
    field2 = models.CharField(max_length=58, blank=True, null=True)
    field3 = models.CharField(max_length=58, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'selfnsi1'


class SertS(BaseModel):
    sert_s = models.CharField(max_length=50, blank=True, null=True)
    blank = models.CharField(max_length=20, blank=True, null=True)
    vidan = models.CharField(max_length=30, blank=True, null=True)
    pol_name = models.CharField(max_length=80, blank=True, null=True)
    pol_okpo = models.CharField(max_length=8, blank=True, null=True)
    pol_soato = models.CharField(max_length=4, blank=True, null=True)
    pol_inn = models.CharField(max_length=12, blank=True, null=True)
    tovar = models.CharField(max_length=150, blank=True, null=True)
    cod_tov = models.CharField(max_length=9, blank=True, null=True)
    contr_we = models.BooleanField(blank=True, null=True)
    weight = models.DecimalField(default=0.00, max_digits=17, decimal_places=6, blank=True, null=True)
    ntrans = models.CharField(max_length=50, blank=True, null=True)
    date_ot = models.DateField(blank=True, null=True)
    date_do = models.DateField(blank=True, null=True)
    priost = models.BooleanField(blank=True, null=True)
    date_pr = models.DateField(blank=True, null=True)
    istek = models.BooleanField(blank=True, null=True)
    date_an = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'sert_s'


class Sertif(BaseModel):
    kod = models.CharField(max_length=5, blank=True, null=True)
    numdocum = models.CharField(max_length=35, blank=True, null=True)
    numblank = models.CharField(max_length=8, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    datestart = models.DateField(blank=True, null=True)
    dateclose = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'sertif'


class Sertif4(BaseModel):
    numdocum = models.CharField(max_length=19, blank=True, null=True)
    numblank = models.CharField(max_length=8, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    datestart = models.DateField(blank=True, null=True)
    dateclose = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'sertif4'


class SezPrim(BaseModel):
    kodt = models.CharField(max_length=10, blank=True, null=True)
    naim = models.CharField(max_length=150, blank=True, null=True)
    st_min = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, blank=True, null=True)
    simvmin = models.CharField(max_length=1, blank=True, null=True)
    edimin = models.CharField(max_length=3, blank=True, null=True)
    oper = models.CharField(max_length=1, blank=True, null=True)
    st_max = models.DecimalField(default=0.00, max_digits=10, decimal_places=3, blank=True, null=True)
    simvmax = models.CharField(max_length=1, blank=True, null=True)
    edimax = models.CharField(max_length=3, blank=True, null=True)
    npric = models.CharField(max_length=20, blank=True, null=True)
    dpric = models.DateField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    data1 = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'sez_prim'


# class Shtraf1(BaseModel):
#
#     class Meta:
#         abstract = True
#         # db_table = 'shtraf1'


class SklStt(BaseModel):
    kod = models.CharField(max_length=2, blank=True, null=True)
    naim = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'skl_stt'


# class SklTm_(BaseModel):
#
#     class Meta:
#         abstract = True
#         # db_table = 'skl_tm'


class Sklad(BaseModel):
    kodt = models.CharField(max_length=5, blank=True, null=True)
    noms = models.CharField(max_length=3, blank=True, null=True)
    okpo_own = models.CharField(max_length=8, blank=True, null=True)
    soatoown = models.CharField(max_length=4, blank=True, null=True)
    innown = models.CharField(max_length=12, blank=True, null=True)
    kategown = models.CharField(max_length=2, blank=True, null=True)
    nlic = models.CharField(max_length=10, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    dateout = models.DateField(blank=True, null=True)
    pr_per = models.CharField(max_length=1, blank=True, null=True)
    adrs = models.CharField(max_length=60, blank=True, null=True)
    date_mod = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'sklad'


class Skladbx(BaseModel):
    st = models.CharField(max_length=2, blank=True, null=True)
    kodt = models.CharField(max_length=8, blank=True, null=True)
    namt = models.CharField(max_length=30, blank=True, null=True)
    itam = models.CharField(max_length=1, blank=True, null=True)
    typ_doc = models.CharField(max_length=1, blank=True, null=True)
    nlic = models.CharField(max_length=25, blank=True, null=True)
    pr_per = models.CharField(max_length=1, blank=True, null=True)
    dbegin = models.DateField(blank=True, null=True)
    dend = models.DateField(blank=True, null=True)
    idel = models.CharField(max_length=1, blank=True, null=True)
    types = models.CharField(max_length=1, blank=True, null=True)
    areas = models.DecimalField(default=0.00, max_digits=9, decimal_places=1, blank=True, null=True)
    volume = models.DecimalField(default=0.00, max_digits=9, decimal_places=1, blank=True, null=True)
    owner = models.CharField(max_length=255, blank=True, null=True)
    adrown = models.TextField(blank=True, null=True)
    telefon = models.CharField(max_length=50, blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    adrs = models.TextField(blank=True, null=True)
    telefs = models.CharField(max_length=30, blank=True, null=True)
    iakciz = models.CharField(max_length=1, blank=True, null=True)
    asovam = models.CharField(max_length=8, blank=True, null=True)
    date_mod = models.DateField(blank=True, null=True)
    vidtrans = models.CharField(max_length=30, blank=True, null=True)
    pr441pril3 = models.CharField(max_length=1, blank=True, null=True)
    ata = models.CharField(max_length=1, blank=True, null=True)
    d_isl = models.DateField(blank=True, null=True)
    ogrn = models.CharField(max_length=15, blank=True, null=True)
    inn = models.CharField(max_length=20, blank=True, null=True)
    kpp = models.CharField(max_length=9, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'skladbx'


class SkladtB(BaseModel):
    country = models.CharField(max_length=3, blank=True, null=True)
    numbskl = models.CharField(max_length=4, blank=True, null=True)
    customs = models.CharField(max_length=2, blank=True, null=True)
    custpost = models.CharField(max_length=3, blank=True, null=True)
    nlic = models.CharField(max_length=15, blank=True, null=True)
    pr_per = models.CharField(max_length=1, blank=True, null=True)
    inn = models.CharField(max_length=12, blank=True, null=True)
    typeowner = models.CharField(max_length=1, blank=True, null=True)
    typskl = models.CharField(max_length=1, blank=True, null=True)
    datereg = models.DateField(blank=True, null=True)
    dategive = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)
    annulcode = models.CharField(max_length=1, blank=True, null=True)
    annuldate = models.DateField(blank=True, null=True)
    owner = models.CharField(max_length=50, blank=True, null=True)
    adrs = models.CharField(max_length=190, blank=True, null=True)
    addrskl = models.CharField(max_length=254, blank=True, null=True)
    telefs = models.CharField(max_length=30, blank=True, null=True)
    iakciz = models.CharField(max_length=1, blank=True, null=True)
    vidtrans = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'skladt_b'


class Skladtm(BaseModel):
    st = models.CharField(max_length=2, blank=True, null=True)
    kodt = models.CharField(max_length=8, blank=True, null=True)
    namt = models.CharField(max_length=30, blank=True, null=True)
    itam = models.CharField(max_length=1, blank=True, null=True)
    typ_doc = models.CharField(max_length=1, blank=True, null=True)
    nlic = models.CharField(max_length=25, blank=True, null=True)
    pr_per = models.CharField(max_length=1, blank=True, null=True)
    dbegin = models.DateField(blank=True, null=True)
    dend = models.DateField(blank=True, null=True)
    idel = models.CharField(max_length=1, blank=True, null=True)
    types = models.CharField(max_length=1, blank=True, null=True)
    areas = models.DecimalField(default=0.00, max_digits=9, decimal_places=1, blank=True, null=True)
    owner = models.CharField(max_length=255, blank=True, null=True)
    adrown = models.TextField(blank=True, null=True)
    telefon = models.CharField(max_length=50, blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    adrs = models.TextField(blank=True, null=True)
    iakciz = models.CharField(max_length=1, blank=True, null=True)
    asovam = models.CharField(max_length=8, blank=True, null=True)
    date_mod = models.DateField(blank=True, null=True)
    vidtrans = models.CharField(max_length=30, blank=True, null=True)
    d_isl = models.DateField(blank=True, null=True)
    d_opdl = models.DateField(blank=True, null=True)
    ogrn = models.CharField(max_length=15, blank=True, null=True)
    inn = models.CharField(max_length=20, blank=True, null=True)
    kpp = models.CharField(max_length=9, blank=True, null=True)
    kodtk = models.CharField(max_length=8, blank=True, null=True)
    namtk = models.CharField(max_length=30, blank=True, null=True)
    volumes = models.DecimalField(default=0.00, max_digits=9, decimal_places=1, blank=True, null=True)
    n_akc = models.CharField(max_length=20, blank=True, null=True)
    d_akc = models.DateField(blank=True, null=True)
    vid_vlad = models.CharField(max_length=30, blank=True, null=True)
    s_upl = models.CharField(max_length=100, blank=True, null=True)
    f_upl = models.CharField(max_length=10, blank=True, null=True)
    nam_bank = models.CharField(max_length=50, blank=True, null=True)
    d_bank = models.DateField(blank=True, null=True)
    n_zalog = models.CharField(max_length=20, blank=True, null=True)
    d_zalog = models.DateField(blank=True, null=True)
    dk_zalog = models.DateField(blank=True, null=True)
    n_por = models.CharField(max_length=20, blank=True, null=True)
    d_por = models.DateField(blank=True, null=True)
    name_por = models.CharField(max_length=80, blank=True, null=True)
    dk_por = models.DateField(blank=True, null=True)
    n_insur = models.CharField(max_length=20, blank=True, null=True)
    d_insur = models.DateField(blank=True, null=True)
    nam_ins = models.CharField(max_length=80, blank=True, null=True)
    dataproc = models.DateField(blank=True, null=True)
    tov = models.TextField(blank=True, null=True)
    prim = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'skladtm'


class SkladvB(BaseModel):
    country = models.CharField(max_length=3, blank=True, null=True)
    numbskl = models.CharField(max_length=4, blank=True, null=True)
    customs = models.CharField(max_length=2, blank=True, null=True)
    custpost = models.CharField(max_length=3, blank=True, null=True)
    nlic = models.CharField(max_length=15, blank=True, null=True)
    pr_per = models.CharField(max_length=1, blank=True, null=True)
    inn = models.CharField(max_length=12, blank=True, null=True)
    typeowner = models.CharField(max_length=1, blank=True, null=True)
    typskl = models.CharField(max_length=1, blank=True, null=True)
    datereg = models.DateField(blank=True, null=True)
    dategive = models.DateField(blank=True, null=True)
    dateend = models.DateField(blank=True, null=True)
    annulcode = models.CharField(max_length=1, blank=True, null=True)
    annuldate = models.DateField(blank=True, null=True)
    owner = models.CharField(max_length=50, blank=True, null=True)
    adrs = models.CharField(max_length=190, blank=True, null=True)
    addrskl = models.CharField(max_length=254, blank=True, null=True)
    telefs = models.CharField(max_length=30, blank=True, null=True)
    iakciz = models.CharField(max_length=1, blank=True, null=True)
    vidtrans = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'skladv_b'


# class Skltm(BaseModel):
#
#     class Meta:
#         abstract = True
#         # db_table = 'skltm'


class Skrecc(BaseModel):
    kod = models.CharField(max_length=2, blank=True, null=True)
    nam = models.CharField(max_length=100, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'skrecc'


class Soato(BaseModel):
    kod = models.CharField(max_length=4, blank=True, null=True)
    naim = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'soato'


class Sokr(BaseModel):
    nsokr = models.DecimalField(default=0.00, max_digits=3, decimal_places=0, blank=True, null=True)
    sokr = models.CharField(max_length=23, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'sokr'


class Sono(BaseModel):
    code = models.CharField(max_length=4, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    data1 = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'sono'


class Soun1(BaseModel):
    kod = models.CharField(max_length=4, blank=True, null=True)
    vid = models.CharField(max_length=2, blank=True, null=True)
    kodp = models.CharField(max_length=30, blank=True, null=True)
    kodv = models.CharField(max_length=4, blank=True, null=True)
    naimk = models.CharField(max_length=120, blank=True, null=True)
    naim = models.CharField(max_length=250, blank=True, null=True)
    psono = models.CharField(max_length=1, blank=True, null=True)
    puch = models.CharField(max_length=1, blank=True, null=True)
    potchdok = models.CharField(max_length=1, blank=True, null=True)
    potch = models.CharField(max_length=1, blank=True, null=True)
    inn = models.CharField(max_length=10, blank=True, null=True)
    kpp = models.CharField(max_length=9, blank=True, null=True)
    adres = models.CharField(max_length=128, blank=True, null=True)
    tel = models.CharField(max_length=64, blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    cite = models.CharField(max_length=64, blank=True, null=True)
    dokum = models.CharField(max_length=100, blank=True, null=True)
    nomdok = models.CharField(max_length=50, blank=True, null=True)
    datadok = models.CharField(max_length=10, blank=True, null=True)
    datan = models.CharField(max_length=10, blank=True, null=True)
    datak = models.CharField(max_length=10, blank=True, null=True)
    coment = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'soun1'


class Source(BaseModel):
    code = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    datn = models.DateField(blank=True, null=True)
    dats = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'source'


class SpTovW(BaseModel):
    isp = models.CharField(max_length=1, blank=True, null=True)
    krnaim = models.CharField(max_length=30, blank=True, null=True)
    naim = models.CharField(max_length=210, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'sp_tov_w'


class SpcPrim(BaseModel):
    kodt = models.CharField(max_length=10, blank=True, null=True)
    naim = models.CharField(max_length=150, blank=True, null=True)
    st_spc = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, blank=True, null=True)
    npric = models.CharField(max_length=20, blank=True, null=True)
    dpric = models.DateField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    data1 = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'spc_prim'


class Spcproc(BaseModel):
    code = models.CharField(max_length=2, blank=True, null=True)
    gr_stp = models.CharField(max_length=2, blank=True, null=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'spcproc'


class SpzkRsn(BaseModel):
    kod = models.CharField(max_length=3, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    prim = models.CharField(max_length=250, blank=True, null=True)
    dbegin = models.DateField(blank=True, null=True)
    dend = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'spzk_rsn'


class SrsnRtn(BaseModel):
    kod = models.CharField(max_length=2, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    prim = models.CharField(max_length=250, blank=True, null=True)
    dbegin = models.DateField(blank=True, null=True)
    dend = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'srsn_rtn'


class Stack(BaseModel):
    rec = models.DecimalField(default=0.00, max_digits=10, decimal_places=0, blank=True, null=True)
    tec_ntx = models.DecimalField(default=0.00, max_digits=2, decimal_places=0, blank=True, null=True)
    kod_sotr = models.CharField(max_length=3, blank=True, null=True)
    arm_schet = models.DecimalField(default=0.00, max_digits=2, decimal_places=0, blank=True, null=True)
    colon = models.DecimalField(default=0.00, max_digits=2, decimal_places=0, blank=True, null=True)
    row = models.DecimalField(default=0.00, max_digits=2, decimal_places=0, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'stack'


# class Stm(BaseModel):
#
#     class Meta:
#         abstract = True
#         # db_table = 'stm'


class StmDel(BaseModel):
    kodt = models.CharField(max_length=8, blank=True, null=True)
    namt = models.CharField(max_length=30, blank=True, null=True)
    itam = models.CharField(max_length=1, blank=True, null=True)
    typ_doc = models.CharField(max_length=1, blank=True, null=True)
    nlic = models.CharField(max_length=11, blank=True, null=True)
    pr_per = models.CharField(max_length=1, blank=True, null=True)
    dbegin = models.DateField(blank=True, null=True)
    dend = models.DateField(blank=True, null=True)
    idel = models.CharField(max_length=1, blank=True, null=True)
    types = models.CharField(max_length=1, blank=True, null=True)
    areas = models.DecimalField(default=0.00, max_digits=9, decimal_places=1, blank=True, null=True)
    owner = models.CharField(max_length=50, blank=True, null=True)
    adrown = models.TextField(blank=True, null=True)
    adrs = models.TextField(blank=True, null=True)
    iakciz = models.CharField(max_length=1, blank=True, null=True)
    asovam = models.CharField(max_length=8, blank=True, null=True)
    date_mod = models.DateField(blank=True, null=True)
    vidtrans = models.CharField(max_length=30, blank=True, null=True)
    d_isl = models.DateField(blank=True, null=True)
    d_opdl = models.DateField(blank=True, null=True)
    ogrn = models.CharField(max_length=15, blank=True, null=True)
    inn = models.CharField(max_length=12, blank=True, null=True)
    kpp = models.CharField(max_length=9, blank=True, null=True)
    kodtk = models.CharField(max_length=8, blank=True, null=True)
    namtk = models.CharField(max_length=30, blank=True, null=True)
    volumes = models.DecimalField(default=0.00, max_digits=9, decimal_places=1, blank=True, null=True)
    n_akc = models.CharField(max_length=20, blank=True, null=True)
    d_akc = models.DateField(blank=True, null=True)
    vid_vlad = models.CharField(max_length=30, blank=True, null=True)
    s_upl = models.CharField(max_length=100, blank=True, null=True)
    f_upl = models.CharField(max_length=10, blank=True, null=True)
    nam_bank = models.CharField(max_length=50, blank=True, null=True)
    d_bank = models.DateField(blank=True, null=True)
    n_zalog = models.CharField(max_length=20, blank=True, null=True)
    d_zalog = models.DateField(blank=True, null=True)
    dk_zalog = models.DateField(blank=True, null=True)
    n_por = models.CharField(max_length=20, blank=True, null=True)
    d_por = models.DateField(blank=True, null=True)
    name_por = models.CharField(max_length=80, blank=True, null=True)
    dk_por = models.DateField(blank=True, null=True)
    n_insur = models.CharField(max_length=20, blank=True, null=True)
    d_insur = models.DateField(blank=True, null=True)
    nam_ins = models.CharField(max_length=80, blank=True, null=True)
    dataproc = models.DateField(blank=True, null=True)
    tov = models.TextField(blank=True, null=True)
    prim = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'stm_del'


class Strana(BaseModel):
    kod = models.CharField(max_length=1, blank=True, null=True)
    kodoksmt = models.CharField(max_length=3, blank=True, null=True)
    name = models.CharField(max_length=35, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'strana'


class Stt(BaseModel):
    nomr3 = models.CharField(max_length=10, blank=True, null=True)
    ogrn = models.CharField(max_length=15, blank=True, null=True)
    inn = models.CharField(max_length=12, blank=True, null=True)
    kpp = models.CharField(max_length=9, blank=True, null=True)
    num_stt = models.CharField(max_length=3, blank=True, null=True)
    num_pnkt = models.CharField(max_length=2, blank=True, null=True)
    datn = models.DateField(blank=True, null=True)
    prim = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'stt'


class Subject(BaseModel):
    id = models.DecimalField(default=0.00, max_digits=18, decimal_places=9, blank=True, null=True)
    itn = models.CharField(max_length=13, blank=True, null=True)
    inn = models.CharField(max_length=12, blank=True, null=True)
    kpp = models.CharField(max_length=9, blank=True, null=True)
    ogrn = models.CharField(max_length=13, blank=True, null=True)
    name_full1 = models.CharField(max_length=254, blank=True, null=True)
    name_full2 = models.CharField(max_length=254, blank=True, null=True)
    name_full3 = models.CharField(max_length=254, blank=True, null=True)
    name_full4 = models.CharField(max_length=254, blank=True, null=True)
    name_full5 = models.CharField(max_length=254, blank=True, null=True)
    name_full6 = models.CharField(max_length=254, blank=True, null=True)
    name_full7 = models.CharField(max_length=254, blank=True, null=True)
    name_full8 = models.CharField(max_length=222, blank=True, null=True)
    name_shor1 = models.CharField(max_length=254, blank=True, null=True)
    name_shor2 = models.CharField(max_length=1, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'subject'


class Subject0(BaseModel):
    subject_id = models.DecimalField(default=0.00, max_digits=18, decimal_places=9, blank=True, null=True)
    date_first = models.CharField(max_length=22, blank=True, null=True)
    date_last = models.CharField(max_length=22, blank=True, null=True)
    role = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'subject_'


class Sutp(BaseModel):
    kod = models.CharField(max_length=2, blank=True, null=True)
    gr_su = models.CharField(max_length=2, blank=True, null=True)
    naim = models.CharField(max_length=255, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)
    pr_rb = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    pr_rk = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    pr_rf = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    pr_am = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    pr_kg = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'sutp'


class SysKtpt(BaseModel):
    dbfname = models.CharField(max_length=8, blank=True, null=True)
    prdbktp = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'sys_ktpt'


class TDoc(BaseModel):
    kod = models.CharField(max_length=2, blank=True, null=True)
    naim = models.CharField(max_length=45, blank=True, null=True)
    kr_naim = models.CharField(max_length=15, blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    data1 = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 't_doc'


class Tab47B(BaseModel):
    nd = models.CharField(max_length=19, blank=True, null=True)
    g011 = models.CharField(max_length=2, blank=True, null=True)
    g012 = models.CharField(max_length=2, blank=True, null=True)
    gb12 = models.DecimalField(default=0.00, max_digits=15, decimal_places=4, blank=True, null=True)
    gb22 = models.DecimalField(default=0.00, max_digits=15, decimal_places=4, blank=True, null=True)
    gb32 = models.DecimalField(default=0.00, max_digits=17, decimal_places=4, blank=True, null=True)
    gb42 = models.DecimalField(default=0.00, max_digits=17, decimal_places=4, blank=True, null=True)
    gb52 = models.DecimalField(default=0.00, max_digits=17, decimal_places=4, blank=True, null=True)
    gb62 = models.DecimalField(default=0.00, max_digits=17, decimal_places=4, blank=True, null=True)
    gb72 = models.DecimalField(default=0.00, max_digits=17, decimal_places=4, blank=True, null=True)
    gb82 = models.DecimalField(default=0.00, max_digits=17, decimal_places=4, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'tab47b'


class Tabnar(BaseModel):
    okpo = models.CharField(max_length=10, blank=True, null=True)
    ogrn = models.CharField(max_length=15, blank=True, null=True)
    inn = models.CharField(max_length=12, blank=True, null=True)
    kpp = models.CharField(max_length=9, blank=True, null=True)
    nom = models.DecimalField(default=0.00, max_digits=2, decimal_places=0, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'tabnar'


class Tam(BaseModel):
    ntam = models.DecimalField(default=0.00, max_digits=5, decimal_places=0, blank=True, null=True)
    tam = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'tam'


class Tamplat(BaseModel):
    shifr = models.CharField(max_length=4, blank=True, null=True)
    razdel_1 = models.CharField(max_length=1, blank=True, null=True)
    pr_plat = models.CharField(max_length=1, blank=True, null=True)
    naim = models.TextField(blank=True, null=True)
    bankrec = models.CharField(max_length=70, blank=True, null=True)
    grp_id = models.CharField(max_length=2, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)
    pr_rb = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    pr_rk = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    pr_rf = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    pr_am = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)
    pr_kg = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'tamplat'


class Tamplat0(BaseModel):
    shifr = models.CharField(max_length=2, blank=True, null=True)
    pr_plat = models.CharField(max_length=1, blank=True, null=True)
    naim = models.CharField(max_length=210, blank=True, null=True)
    bankrec = models.CharField(max_length=70, blank=True, null=True)
    grp_id = models.CharField(max_length=2, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'tamplat_'


class Tampred(BaseModel):
    st = models.CharField(max_length=2, blank=True, null=True)
    typ_doc = models.CharField(max_length=1, blank=True, null=True)
    nlic = models.CharField(max_length=25, blank=True, null=True)
    dbegin = models.DateField(blank=True, null=True)
    prz_prim = models.CharField(max_length=2, blank=True, null=True)
    dbegin_st = models.DateField(blank=True, null=True)
    end_st = models.DateField(blank=True, null=True)
    dend = models.DateField(blank=True, null=True)
    owner = models.CharField(max_length=255, blank=True, null=True)
    adrown = models.CharField(max_length=255, blank=True, null=True)
    adrpocht = models.CharField(max_length=255, blank=True, null=True)
    telefon = models.CharField(max_length=50, blank=True, null=True)
    fax = models.CharField(max_length=50, blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    inn = models.CharField(max_length=20, blank=True, null=True)
    kpp = models.CharField(max_length=9, blank=True, null=True)
    kpp2 = models.CharField(max_length=9, blank=True, null=True)
    priznak = models.CharField(max_length=1, blank=True, null=True)
    cont02 = models.CharField(max_length=255, blank=True, null=True)
    cont03 = models.CharField(max_length=255, blank=True, null=True)
    dopinf = models.CharField(max_length=255, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'tampred'


class Tampred1(BaseModel):
    st = models.CharField(max_length=2, blank=True, null=True)
    typ_doc = models.CharField(max_length=1, blank=True, null=True)
    nlic = models.CharField(max_length=25, blank=True, null=True)
    dbegin = models.DateField(blank=True, null=True)
    prz_prim = models.CharField(max_length=2, blank=True, null=True)
    code_to = models.CharField(max_length=8, blank=True, null=True)
    cont04 = models.CharField(max_length=255, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'tampred1'


class Tampred2(BaseModel):
    st = models.CharField(max_length=2, blank=True, null=True)
    typ_doc = models.CharField(max_length=1, blank=True, null=True)
    nlic = models.CharField(max_length=25, blank=True, null=True)
    dbegin = models.DateField(blank=True, null=True)
    prz_prim = models.CharField(max_length=2, blank=True, null=True)
    kodtmin = models.CharField(max_length=10, blank=True, null=True)
    kodtmax = models.CharField(max_length=10, blank=True, null=True)
    cont01 = models.CharField(max_length=255, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'tampred2'


class Tampred3(BaseModel):
    st = models.CharField(max_length=2, blank=True, null=True)
    typ_doc = models.CharField(max_length=1, blank=True, null=True)
    nlic = models.CharField(max_length=25, blank=True, null=True)
    dbegin = models.DateField(blank=True, null=True)
    prz_prim = models.CharField(max_length=2, blank=True, null=True)
    kod = models.CharField(max_length=2, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'tampred3'


class Tampred4(BaseModel):
    st = models.CharField(max_length=2, blank=True, null=True)
    typ_doc = models.CharField(max_length=1, blank=True, null=True)
    nlic = models.CharField(max_length=25, blank=True, null=True)
    dbegin = models.DateField(blank=True, null=True)
    prz_prim = models.CharField(max_length=2, blank=True, null=True)
    inn_fil = models.CharField(max_length=20, blank=True, null=True)
    kpp_fil = models.CharField(max_length=9, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    cont04 = models.CharField(max_length=255, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'tampred4'


class Tamst(BaseModel):
    npp = models.DecimalField(default=0.00, max_digits=3, decimal_places=0, blank=True, null=True)
    kod = models.CharField(max_length=10, blank=True, null=True)
    cenamin = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, blank=True, null=True)
    cenamax = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, blank=True, null=True)
    edi = models.CharField(max_length=3, blank=True, null=True)
    kodtam = models.CharField(max_length=1, blank=True, null=True)
    uslcena = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, blank=True, null=True)
    priznstr = models.CharField(max_length=1, blank=True, null=True)
    kodiskl = models.CharField(max_length=80, blank=True, null=True)
    striskl = models.CharField(max_length=60, blank=True, null=True)
    pric = models.CharField(max_length=25, blank=True, null=True)
    prim = models.CharField(max_length=150, blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    data1 = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'tamst'


class Tamstavt(BaseModel):
    marka = models.CharField(max_length=20, blank=True, null=True)
    markar = models.CharField(max_length=20, blank=True, null=True)
    strana = models.CharField(max_length=3, blank=True, null=True)
    vdvigmin = models.DecimalField(default=0.00, max_digits=5, decimal_places=0, blank=True, null=True)
    vdvigmax = models.DecimalField(default=0.00, max_digits=5, decimal_places=0, blank=True, null=True)
    market = models.CharField(max_length=1, blank=True, null=True)
    cenamin = models.DecimalField(default=0.00, max_digits=7, decimal_places=0, blank=True, null=True)
    cenamax = models.DecimalField(default=0.00, max_digits=7, decimal_places=0, blank=True, null=True)
    kodtam = models.CharField(max_length=1, blank=True, null=True)
    uslcena = models.DecimalField(default=0.00, max_digits=7, decimal_places=0, blank=True, null=True)
    tipdv = models.CharField(max_length=1, blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    data1 = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'tamstavt'


class Tbrok(BaseModel):
    st = models.CharField(max_length=2, blank=True, null=True)
    typ_doc = models.CharField(max_length=1, blank=True, null=True)
    bktlic = models.CharField(max_length=25, blank=True, null=True)
    bnpplic = models.DecimalField(default=0.00, max_digits=4, decimal_places=0, blank=True, null=True)
    bdbegin = models.DateField(blank=True, null=True)
    prz_prim = models.CharField(max_length=1, blank=True, null=True)
    bdend = models.DateField(blank=True, null=True)
    brokname = models.CharField(max_length=255, blank=True, null=True)
    adrown = models.CharField(max_length=255, blank=True, null=True)
    brokmail = models.CharField(max_length=255, blank=True, null=True)
    brokokpo = models.CharField(max_length=10, blank=True, null=True)
    ogrn = models.CharField(max_length=15, blank=True, null=True)
    brokinn = models.CharField(max_length=20, blank=True, null=True)
    brokkpp = models.CharField(max_length=9, blank=True, null=True)
    bskoltoi = models.DecimalField(default=0.00, max_digits=3, decimal_places=0, blank=True, null=True)
    bskoltoii = models.DecimalField(default=0.00, max_digits=3, decimal_places=0, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'tbrok'


class Tbrok1(BaseModel):
    st = models.CharField(max_length=2, blank=True, null=True)
    typ_doc = models.CharField(max_length=1, blank=True, null=True)
    bktlic = models.CharField(max_length=25, blank=True, null=True)
    bnpplic = models.DecimalField(default=0.00, max_digits=4, decimal_places=0, blank=True, null=True)
    bdbegin = models.DateField(blank=True, null=True)
    prz_prim = models.CharField(max_length=1, blank=True, null=True)
    bvidtran = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'tbrok1'


class Tbrok2(BaseModel):
    st = models.CharField(max_length=2, blank=True, null=True)
    typ_doc = models.CharField(max_length=1, blank=True, null=True)
    bktlic = models.CharField(max_length=25, blank=True, null=True)
    bnpplic = models.DecimalField(default=0.00, max_digits=4, decimal_places=0, blank=True, null=True)
    bdbegin = models.DateField(blank=True, null=True)
    prz_prim = models.CharField(max_length=1, blank=True, null=True)
    bktam = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'tbrok2'


class Tbrok3(BaseModel):
    st = models.CharField(max_length=2, blank=True, null=True)
    typ_doc = models.CharField(max_length=1, blank=True, null=True)
    bktlic = models.CharField(max_length=25, blank=True, null=True)
    bnpplic = models.DecimalField(default=0.00, max_digits=4, decimal_places=0, blank=True, null=True)
    bdbegin = models.DateField(blank=True, null=True)
    prz_prim = models.CharField(max_length=1, blank=True, null=True)
    bkodtmin = models.CharField(max_length=10, blank=True, null=True)
    bkodtmax = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'tbrok3'


class Tbrok4(BaseModel):
    st = models.CharField(max_length=2, blank=True, null=True)
    typ_doc = models.CharField(max_length=1, blank=True, null=True)
    bktlic = models.CharField(max_length=25, blank=True, null=True)
    bnpplic = models.DecimalField(default=0.00, max_digits=4, decimal_places=0, blank=True, null=True)
    bdbegin = models.DateField(blank=True, null=True)
    prz_prim = models.CharField(max_length=1, blank=True, null=True)
    bncoplic = models.DecimalField(default=0.00, max_digits=3, decimal_places=0, blank=True, null=True)
    copdata = models.DateField(blank=True, null=True)
    copdata1 = models.DateField(blank=True, null=True)
    bktam = models.CharField(max_length=8, blank=True, null=True)
    bkoltoi = models.DecimalField(default=0.00, max_digits=3, decimal_places=0, blank=True, null=True)
    bkoltoii = models.DecimalField(default=0.00, max_digits=3, decimal_places=0, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'tbrok4'


class Tbrok5(BaseModel):
    st = models.CharField(max_length=2, blank=True, null=True)
    typ_doc = models.CharField(max_length=1, blank=True, null=True)
    bktlic = models.CharField(max_length=25, blank=True, null=True)
    bnpplic = models.DecimalField(default=0.00, max_digits=4, decimal_places=0, blank=True, null=True)
    bdbegin = models.DateField(blank=True, null=True)
    prz_prim = models.CharField(max_length=1, blank=True, null=True)
    bncoplic = models.DecimalField(default=0.00, max_digits=3, decimal_places=0, blank=True, null=True)
    bkodcom = models.CharField(max_length=1, blank=True, null=True)
    bnumcom = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'tbrok5'


class Tbrok6(BaseModel):
    st = models.CharField(max_length=2, blank=True, null=True)
    typ_doc = models.CharField(max_length=1, blank=True, null=True)
    bktlic = models.CharField(max_length=25, blank=True, null=True)
    bnpplic = models.DecimalField(default=0.00, max_digits=4, decimal_places=0, blank=True, null=True)
    bdbegin = models.DateField(blank=True, null=True)
    prz_prim = models.CharField(max_length=1, blank=True, null=True)
    bncoplic = models.DecimalField(default=0.00, max_digits=3, decimal_places=0, blank=True, null=True)
    bnschet = models.CharField(max_length=20, blank=True, null=True)
    bokpobnk = models.CharField(max_length=10, blank=True, null=True)
    bdendsch = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'tbrok6'


class Tbrok7(BaseModel):
    st = models.CharField(max_length=2, blank=True, null=True)
    typ_doc = models.CharField(max_length=1, blank=True, null=True)
    bktlic = models.CharField(max_length=25, blank=True, null=True)
    bnpplic = models.DecimalField(default=0.00, max_digits=4, decimal_places=0, blank=True, null=True)
    bdbegin = models.DateField(blank=True, null=True)
    prz_prim = models.CharField(max_length=1, blank=True, null=True)
    inn = models.CharField(max_length=20, blank=True, null=True)
    kpp = models.CharField(max_length=9, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'tbrok7'


class Tbrok8(BaseModel):
    st = models.CharField(max_length=2, blank=True, null=True)
    typ_doc = models.CharField(max_length=1, blank=True, null=True)
    bktlic = models.CharField(max_length=25, blank=True, null=True)
    bnpplic = models.DecimalField(default=0.00, max_digits=4, decimal_places=0, blank=True, null=True)
    bdbegin = models.DateField(blank=True, null=True)
    prz_prim = models.CharField(max_length=1, blank=True, null=True)
    bvidtop = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'tbrok8'


class Tipdv(BaseModel):
    kod = models.CharField(max_length=1, blank=True, null=True)
    name = models.CharField(max_length=35, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'tipdv'


class Tipts(BaseModel):
    kod = models.CharField(max_length=2, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'tipts'


class TiptsS(BaseModel):
    kod = models.CharField(max_length=3, blank=True, null=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'tipts_s'


class Tk(BaseModel):
    name = models.CharField(max_length=24, blank=True, null=True)
    fon = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=42, blank=True, null=True)
    inn = models.DecimalField(default=0.00, max_digits=19, decimal_places=0, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'tk'


class Tk1(BaseModel):
    name = models.CharField(max_length=24, blank=True, null=True)
    fon = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=42, blank=True, null=True)
    inn = models.DecimalField(default=0.00, max_digits=19, decimal_places=0, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'tk1'


class Tndti14(BaseModel):
    kod10 = models.CharField(max_length=10, blank=True, null=True)
    kodt11 = models.CharField(max_length=1, blank=True, null=True)
    kodt12 = models.CharField(max_length=1, blank=True, null=True)
    kodt13 = models.CharField(max_length=1, blank=True, null=True)
    kodt14 = models.CharField(max_length=1, blank=True, null=True)
    namt11 = models.CharField(max_length=255, blank=True, null=True)
    namt12 = models.CharField(max_length=255, blank=True, null=True)
    namt13 = models.CharField(max_length=255, blank=True, null=True)
    namt14 = models.CharField(max_length=255, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'tndti14'


class TnvLtd(BaseModel):
    code = models.CharField(max_length=10, blank=True, null=True)
    kodiskl = models.CharField(max_length=10, blank=True, null=True)
    dbegin = models.DateField(blank=True, null=True)
    dend = models.DateField(blank=True, null=True)
    prim = models.CharField(max_length=70, blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)
    levelzn = models.CharField(max_length=1, blank=True, null=True)
    lvl_kod = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'tnv_ltd'


class TnvStav(BaseModel):
    code_tnv = models.CharField(max_length=10, blank=True, null=True)
    stav_imp = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, blank=True, null=True)
    stav_exp = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, blank=True, null=True)
    kod_val = models.CharField(max_length=3, blank=True, null=True)
    prim = models.CharField(max_length=255, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'tnv_stav'


class Tnved(BaseModel):
    gruppa = models.CharField(max_length=2, blank=True, null=True)
    tov_poz = models.CharField(max_length=2, blank=True, null=True)
    sub_poz = models.CharField(max_length=5, blank=True, null=True)
    kr_naim = models.CharField(max_length=200, blank=True, null=True)
    edi1 = models.CharField(max_length=3, blank=True, null=True)
    edi2 = models.CharField(max_length=3, blank=True, null=True)
    i_min = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, blank=True, null=True)
    i_max = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, blank=True, null=True)
    e_baz = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, blank=True, null=True)
    e_val = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, blank=True, null=True)
    e_bval = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, blank=True, null=True)
    pr_lic = models.CharField(max_length=1, blank=True, null=True)
    im_nal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, blank=True, null=True)
    ex_nal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, blank=True, null=True)
    tufta = models.CharField(max_length=10, blank=True, null=True)
    impedi1 = models.CharField(max_length=3, blank=True, null=True)
    impedi2 = models.CharField(max_length=3, blank=True, null=True)
    akcsimv1 = models.CharField(max_length=1, blank=True, null=True)
    akcedi1 = models.CharField(max_length=3, blank=True, null=True)
    akcoper = models.CharField(max_length=1, blank=True, null=True)
    akcstmax = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, blank=True, null=True)
    akcsimv2 = models.CharField(max_length=1, blank=True, null=True)
    akcedi2 = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'tnved'


class Tnved1(BaseModel):
    razdel = models.CharField(max_length=5, blank=True, null=True)
    naim = models.TextField(blank=True, null=True)
    prim = models.TextField(blank=True, null=True)
    npric = models.CharField(max_length=20, blank=True, null=True)
    dpric = models.DateField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    data1 = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'tnved1'


class Tnved2(BaseModel):
    razdel = models.CharField(max_length=5, blank=True, null=True)
    gruppa = models.CharField(max_length=2, blank=True, null=True)
    naim = models.TextField(blank=True, null=True)
    prim = models.TextField(blank=True, null=True)
    npric = models.CharField(max_length=20, blank=True, null=True)
    dpric = models.DateField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    data1 = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'tnved2'


class Tnved3(BaseModel):
    gruppa = models.CharField(max_length=2, blank=True, null=True)
    tov_poz = models.CharField(max_length=2, blank=True, null=True)
    naim = models.TextField(blank=True, null=True)
    npric = models.CharField(max_length=20, blank=True, null=True)
    dpric = models.DateField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    data1 = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'tnved3'


class Tnved4(BaseModel):
    gruppa = models.CharField(max_length=2, blank=True, null=True)
    tov_poz = models.CharField(max_length=2, blank=True, null=True)
    sub_poz = models.CharField(max_length=6, blank=True, null=True)
    kr_naim = models.CharField(max_length=250, blank=True, null=True)
    naimbook = models.TextField(blank=True, null=True)
    prim = models.DecimalField(default=0.00, max_digits=2, decimal_places=0, blank=True, null=True)
    edi1 = models.CharField(max_length=3, blank=True, null=True)
    edi2 = models.CharField(max_length=3, blank=True, null=True)
    edi3 = models.CharField(max_length=3, blank=True, null=True)
    npric = models.CharField(max_length=20, blank=True, null=True)
    dpric = models.DateField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    data1 = models.DateField(blank=True, null=True)
    priznak = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'tnved4'


class Tnved6(BaseModel):
    gruppa = models.CharField(max_length=2, blank=True, null=True)
    tov_poz = models.CharField(max_length=2, blank=True, null=True)
    sub1 = models.CharField(max_length=2, blank=True, null=True)
    naim = models.CharField(max_length=200, blank=True, null=True)
    npric = models.CharField(max_length=20, blank=True, null=True)
    dpric = models.DateField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    data1 = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'tnved6'


class Tnved8(BaseModel):
    gruppa = models.CharField(max_length=2, blank=True, null=True)
    tov_poz = models.CharField(max_length=2, blank=True, null=True)
    sub1 = models.CharField(max_length=4, blank=True, null=True)
    naim = models.CharField(max_length=200, blank=True, null=True)
    npric = models.CharField(max_length=20, blank=True, null=True)
    dpric = models.DateField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    data1 = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'tnved8'


class Tnved9(BaseModel):
    gruppa = models.CharField(max_length=2, blank=True, null=True)
    tov_poz = models.CharField(max_length=2, blank=True, null=True)
    sub1 = models.CharField(max_length=5, blank=True, null=True)
    naim = models.CharField(max_length=200, blank=True, null=True)
    npric = models.CharField(max_length=20, blank=True, null=True)
    dpric = models.DateField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    data1 = models.DateField(blank=True, null=True)
    priznak = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'tnved9'


class TovW(BaseModel):
    kodt = models.CharField(max_length=10, blank=True, null=True)
    npoz = models.CharField(max_length=100, blank=True, null=True)
    naim = models.TextField(blank=True, null=True)
    isp = models.CharField(max_length=2, blank=True, null=True)
    pr_ogr = models.CharField(max_length=1, blank=True, null=True)
    npric = models.CharField(max_length=20, blank=True, null=True)
    dpric = models.DateField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    data1 = models.DateField(blank=True, null=True)
    onpric = models.CharField(max_length=20, blank=True, null=True)
    odpric = models.DateField(blank=True, null=True)
    docnaim = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'tov_w'


class Tovsign(BaseModel):
    gruppa = models.CharField(max_length=2, blank=True, null=True)
    tov_poz = models.CharField(max_length=2, blank=True, null=True)
    sub_poz = models.CharField(max_length=6, blank=True, null=True)
    pr_prod = models.BooleanField(blank=True, null=True)
    edi1 = models.CharField(max_length=3, blank=True, null=True)
    edi2 = models.CharField(max_length=3, blank=True, null=True)
    edi3 = models.CharField(max_length=3, blank=True, null=True)
    i_min = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, blank=True, null=True)
    i_max = models.DecimalField(default=0.00, max_digits=10, decimal_places=3, blank=True, null=True)
    e_baz = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, blank=True, null=True)
    e_val = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, blank=True, null=True)
    e_bval = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, blank=True, null=True)
    pr_lic = models.CharField(max_length=1, blank=True, null=True)
    raw_m = models.BooleanField(blank=True, null=True)
    im_nal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, blank=True, null=True)
    ex_nal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, blank=True, null=True)
    tufta = models.CharField(max_length=10, blank=True, null=True)
    impedi1 = models.CharField(max_length=3, blank=True, null=True)
    impedi2 = models.CharField(max_length=3, blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    akcsimv1 = models.CharField(max_length=1, blank=True, null=True)
    akcedi1 = models.CharField(max_length=3, blank=True, null=True)
    akcoper = models.CharField(max_length=1, blank=True, null=True)
    akcstmax = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, blank=True, null=True)
    akcsimv2 = models.CharField(max_length=1, blank=True, null=True)
    akcedi2 = models.CharField(max_length=3, blank=True, null=True)
    expedi1 = models.CharField(max_length=3, blank=True, null=True)
    expedi2 = models.CharField(max_length=3, blank=True, null=True)
    expoper = models.CharField(max_length=1, blank=True, null=True)
    expsimv2 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'tovsign'


class TpoPlt(BaseModel):
    num_tpo = models.CharField(max_length=10, blank=True, null=True)
    sp = models.CharField(max_length=2, blank=True, null=True)
    inn = models.CharField(max_length=12, blank=True, null=True)
    kpp = models.CharField(max_length=9, blank=True, null=True)
    kpph = models.CharField(max_length=9, blank=True, null=True)
    num_doc = models.CharField(max_length=50, blank=True, null=True)
    date_doc = models.DateField(blank=True, null=True)
    summa = models.DecimalField(default=0.00, max_digits=15, decimal_places=2, blank=True, null=True)
    kodval = models.CharField(max_length=3, blank=True, null=True)
    sum_tpo = models.DecimalField(default=0.00, max_digits=15, decimal_places=2, blank=True, null=True)
    vidnac = models.CharField(max_length=4, blank=True, null=True)
    schr = models.CharField(max_length=20, blank=True, null=True)
    bic = models.CharField(max_length=9, blank=True, null=True)
    kbk = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'tpo_plt'


class Trans(BaseModel):
    kod = models.DecimalField(default=0.00, max_digits=3, decimal_places=0, blank=True, null=True)
    naim = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'trans'


class Ts(BaseModel):
    sbj_id = models.DecimalField(default=0.00, max_digits=15, decimal_places=0, blank=True, null=True)
    ts_lic_id = models.DecimalField(default=0.00, max_digits=15, decimal_places=0, blank=True, null=True)
    doctype = models.CharField(max_length=1, blank=True, null=True)
    docnumber = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'ts'


class Tsk(BaseModel):
    kod = models.DecimalField(default=0.00, max_digits=2, decimal_places=0, blank=True, null=True)
    naim = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'tsk'


class Tskat(BaseModel):
    kod = models.CharField(max_length=1, blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    simb = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'tskat'


class Upravl(BaseModel):
    kod = models.CharField(max_length=8, blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'upravl'


class Uslpost(BaseModel):
    kodz = models.DecimalField(default=0.00, max_digits=2, decimal_places=0, blank=True, null=True)
    kods = models.CharField(max_length=3, blank=True, null=True)
    naim = models.CharField(max_length=100, blank=True, null=True)
    krnaim = models.CharField(max_length=3, blank=True, null=True)
    geonaim = models.CharField(max_length=100, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'uslpost'


class Utilsbor(BaseModel):
    d_reason = models.CharField(max_length=250, blank=True, null=True)
    full_d = models.TextField(blank=True, null=True)
    code = models.CharField(max_length=2, blank=True, null=True)
    ex_code = models.CharField(max_length=2, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)
    nummdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegmdoc = models.DateField(blank=True, null=True)
    datendmdoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'utilsbor'


class V2(BaseModel):
    kod = models.CharField(max_length=3, blank=True, null=True)
    buk = models.CharField(max_length=3, blank=True, null=True)
    kol = models.DecimalField(default=0.00, max_digits=8, decimal_places=0, blank=True, null=True)
    okurs = models.DecimalField(default=0.00, max_digits=11, decimal_places=4, blank=True, null=True)
    kkurs = models.DecimalField(default=0.00, max_digits=11, decimal_places=4, blank=True, null=True)
    data = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'v2'


class VObup(BaseModel):
    kodc = models.CharField(max_length=2, blank=True, null=True)
    kodb = models.CharField(max_length=2, blank=True, null=True)
    naim = models.CharField(max_length=255, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'v_obup'


class Val(BaseModel):
    r_date = models.DateField(blank=True, null=True)
    gb_kd = models.DecimalField(default=0.00, max_digits=19, decimal_places=5, blank=True, null=True)
    kod = models.DecimalField(default=0.00, max_digits=19, decimal_places=5, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'val'


class ValCen(BaseModel):
    kod = models.CharField(max_length=2, blank=True, null=True)
    pr_cen = models.CharField(max_length=1, blank=True, null=True)
    naim = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'val_cen'


class Valname(BaseModel):
    kod = models.CharField(max_length=3, blank=True, null=True)
    buk = models.CharField(max_length=3, blank=True, null=True)
    kod_old = models.CharField(max_length=3, blank=True, null=True)
    krnaim = models.CharField(max_length=17, blank=True, null=True)
    fnaim = models.CharField(max_length=255, blank=True, null=True)
    pr_val = models.CharField(max_length=2, blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    data1 = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'valname'


class Valuta(BaseModel):
    kod = models.CharField(max_length=3, blank=True, null=True)
    buk = models.CharField(max_length=3, blank=True, null=True)
    kol = models.DecimalField(default=0.00, max_digits=8, decimal_places=0, blank=True, null=True)
    okurs = models.DecimalField(default=0.00, max_digits=11, decimal_places=4, blank=True, null=True)
    kkurs = models.DecimalField(default=0.00, max_digits=11, decimal_places=4, blank=True, null=True)
    data = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'valuta'


class VidAmts(BaseModel):
    vid_amts = models.CharField(max_length=3, blank=True, null=True)
    name = models.CharField(max_length=26, blank=True, null=True)
    group = models.CharField(max_length=2, blank=True, null=True)
    subgroup = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'vid_amts'


class VidDoc(BaseModel):
    kod = models.CharField(max_length=2, blank=True, null=True)
    naim = models.CharField(max_length=210, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'vid_doc'


class Viddvig(BaseModel):
    kod = models.CharField(max_length=2, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'viddvig'


class Vidtrans(BaseModel):
    kod = models.CharField(max_length=2, blank=True, null=True)
    gr_vt = models.CharField(max_length=2, blank=True, null=True)
    naim = models.CharField(max_length=255, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'vidtrans'


class Vidupak(BaseModel):
    kod = models.CharField(max_length=2, blank=True, null=True)
    naim_r = models.CharField(max_length=255, blank=True, null=True)
    naim_e = models.CharField(max_length=255, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'vidupak'


class Vkortd(BaseModel):
    kod = models.CharField(max_length=2, blank=True, null=True)
    naim = models.CharField(max_length=255, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'vkortd'


class Vkvot(BaseModel):
    kod = models.CharField(max_length=2, blank=True, null=True)
    naim = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'vkvot'


class Vpertr(BaseModel):
    kod = models.CharField(max_length=2, blank=True, null=True)
    naim = models.CharField(max_length=255, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'vpertr'


class Vspupr(BaseModel):
    kod = models.CharField(max_length=1, blank=True, null=True)
    naim = models.CharField(max_length=255, blank=True, null=True)
    datbeg = models.DateField(blank=True, null=True)
    numbegdoc = models.CharField(max_length=20, blank=True, null=True)
    datbegdoc = models.DateField(blank=True, null=True)
    datend = models.DateField(blank=True, null=True)
    numenddoc = models.CharField(max_length=20, blank=True, null=True)
    datenddoc = models.DateField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'vspupr'


class VtsTov(BaseModel):
    key_specif = models.DecimalField(default=0.00, max_digits=19, decimal_places=5, blank=True, null=True)
    zakl_key = models.DecimalField(default=0.00, max_digits=19, decimal_places=5, blank=True, null=True)
    name_prod = models.CharField(max_length=250, blank=True, null=True)
    obozn_prod = models.CharField(max_length=250, blank=True, null=True)
    sern_prod = models.CharField(max_length=250, blank=True, null=True)
    rekv_prod = models.CharField(max_length=250, blank=True, null=True)
    kol_prod = models.CharField(max_length=250, blank=True, null=True)
    primech = models.CharField(max_length=250, blank=True, null=True)
    prizn_bloc = models.DecimalField(default=0.00, max_digits=19, decimal_places=5, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'vts_tov'


class VtsZakl(BaseModel):
    zakl_key = models.DecimalField(default=0.00, max_digits=19, decimal_places=5, blank=True, null=True)
    numb = models.CharField(max_length=250, blank=True, null=True)
    dt = models.DateField(blank=True, null=True)
    name_org = models.TextField(blank=True, null=True)
    uradr_org = models.TextField(blank=True, null=True)
    post_num = models.CharField(max_length=250, blank=True, null=True)
    post_dt = models.DateField(blank=True, null=True)
    ustanovl = models.TextField(blank=True, null=True)
    srok_dey = models.DateField(blank=True, null=True)
    name_pod = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'vts_zakl'


class Waybill(BaseModel):
    num_nakl = models.CharField(max_length=20, blank=True, null=True)
    napravl = models.CharField(max_length=30, blank=True, null=True)
    g021 = models.CharField(max_length=12, blank=True, null=True)
    g022 = models.CharField(max_length=80, blank=True, null=True)
    g023 = models.CharField(max_length=80, blank=True, null=True)
    g027 = models.CharField(max_length=9, blank=True, null=True)
    g081 = models.CharField(max_length=12, blank=True, null=True)
    g082 = models.CharField(max_length=80, blank=True, null=True)
    g083 = models.CharField(max_length=80, blank=True, null=True)
    g087 = models.CharField(max_length=9, blank=True, null=True)
    inn_driver = models.CharField(max_length=12, blank=True, null=True)
    g501 = models.CharField(max_length=80, blank=True, null=True)
    g502 = models.CharField(max_length=80, blank=True, null=True)
    kpp_driver = models.CharField(max_length=9, blank=True, null=True)
    vs_type = models.CharField(max_length=2, blank=True, null=True)
    vs_mark = models.CharField(max_length=100, blank=True, null=True)
    bort_num = models.CharField(max_length=10, blank=True, null=True)
    reis = models.CharField(max_length=10, blank=True, null=True)
    g15a = models.CharField(max_length=3, blank=True, null=True)
    g15 = models.CharField(max_length=35, blank=True, null=True)
    tranzit = models.BooleanField(blank=True, null=True)
    g17a = models.CharField(max_length=3, blank=True, null=True)
    g17b = models.CharField(max_length=35, blank=True, null=True)
    arr_date = models.DateField(blank=True, null=True)
    arr_time = models.CharField(max_length=5, blank=True, null=True)
    pass_count = models.DecimalField(default=0.00, max_digits=3, decimal_places=0, blank=True, null=True)
    g06 = models.DecimalField(default=0.00, max_digits=7, decimal_places=0, blank=True, null=True)
    g35 = models.DecimalField(default=0.00, max_digits=17, decimal_places=6, blank=True, null=True)
    g30 = models.CharField(max_length=15, blank=True, null=True)
    isclosed = models.CharField(max_length=1, blank=True, null=True)
    dmodify = models.DateField(blank=True, null=True)
    g212 = models.CharField(max_length=3, blank=True, null=True)
    g212b = models.CharField(max_length=35, blank=True, null=True)
    fiooforml = models.CharField(max_length=40, blank=True, null=True)
    lnpoforml = models.CharField(max_length=4, blank=True, null=True)
    g30naim = models.CharField(max_length=50, blank=True, null=True)
    datedosm = models.DateField(blank=True, null=True)
    fiodosm = models.CharField(max_length=40, blank=True, null=True)
    lnpdosm = models.CharField(max_length=4, blank=True, null=True)
    g071 = models.CharField(max_length=8, blank=True, null=True)
    g072 = models.DateField(blank=True, null=True)
    g073 = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'waybill'


class Year(BaseModel):
    kod = models.CharField(max_length=1, blank=True, null=True)
    name = models.DecimalField(default=0.00, max_digits=4, decimal_places=0, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'year'


class Zan(BaseModel):
    nzan = models.DecimalField(default=0.00, max_digits=3, decimal_places=0, blank=True, null=True)
    zan = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'zan'


class Zvet(BaseModel):
    kod = models.CharField(max_length=3, blank=True, null=True)
    ncv = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        abstract = True
        # db_table = 'zvet'
