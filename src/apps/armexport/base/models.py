from django.db import models


class BaseModel(models.Model):
    """Base import model"""
    # settings.PIPE_MODULES['ARM']
    type = 'ARM'

    class Meta:
        abstract = True


class Avtomove(BaseModel):
    numcard = models.CharField(db_column='NUMCARD', max_length=23, blank=True, null=True)  # Field name made lowercase.
    vin = models.CharField(db_column='VIN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    model = models.CharField(db_column='MODEL', max_length=36, blank=True, null=True)  # Field name made lowercase.
    tipts = models.CharField(db_column='TIPTS', max_length=2, blank=True, null=True)  # Field name made lowercase.
    kategts = models.CharField(db_column='KATEGTS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    mest = models.SmallIntegerField(db_column='MEST', blank=True, null=True)  # Field name made lowercase.
    god = models.SmallIntegerField(db_column='GOD', blank=True, null=True)  # Field name made lowercase.
    moddvig = models.CharField(db_column='MODDVIG', max_length=15, blank=True, null=True)  # Field name made lowercase.
    numdvig = models.CharField(db_column='NUMDVIG', max_length=40, blank=True, null=True)  # Field name made lowercase.
    shassi = models.CharField(db_column='SHASSI', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kuzov = models.CharField(db_column='KUZOV', max_length=40, blank=True, null=True)  # Field name made lowercase.
    zvet = models.CharField(db_column='ZVET', max_length=3, blank=True, null=True)  # Field name made lowercase.
    powerls = models.FloatField(default=0.00, db_column='POWERLS', blank=True, null=True)  # Field name made lowercase.
    powerkw = models.FloatField(default=0.00, db_column='POWERKW', blank=True, null=True)  # Field name made lowercase.
    obdvig = models.IntegerField(db_column='OBDVIG', blank=True, null=True)  # Field name made lowercase.
    tipdv = models.CharField(db_column='TIPDV', max_length=2, blank=True, null=True)  # Field name made lowercase.
    maxmass = models.IntegerField(db_column='MAXMASS', blank=True, null=True)  # Field name made lowercase.
    minmass = models.IntegerField(db_column='MINMASS', blank=True, null=True)  # Field name made lowercase.
    izgotov = models.CharField(db_column='IZGOTOV', max_length=150, blank=True, null=True)  # Field name made lowercase.
    strizg = models.CharField(db_column='STRIZG', max_length=3, blank=True, null=True)  # Field name made lowercase.
    numodob = models.CharField(db_column='NUMODOB', max_length=21, blank=True, null=True)  # Field name made lowercase.
    datodob = models.DateTimeField(db_column='DATODOB', blank=True, null=True)  # Field name made lowercase.
    orgodob = models.CharField(db_column='ORGODOB', max_length=150, blank=True, null=True)  # Field name made lowercase.
    strvyvoz = models.CharField(db_column='STRVYVOZ', max_length=3, blank=True, null=True)  # Field name made lowercase.
    lic = models.CharField(db_column='LIC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fam = models.CharField(db_column='FAM', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ima = models.CharField(db_column='IMA', max_length=25, blank=True, null=True)  # Field name made lowercase.
    otc = models.CharField(db_column='OTC', max_length=25, blank=True, null=True)  # Field name made lowercase.
    okpo = models.CharField(db_column='OKPO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    namesob = models.CharField(db_column='NAMESOB', max_length=150, blank=True, null=True)  # Field name made lowercase.
    adressob = models.CharField(db_column='ADRESSOB', max_length=105, blank=True, null=True)  # Field name made lowercase.
    udvvoz = models.CharField(db_column='UDVVOZ', max_length=10, blank=True, null=True)  # Field name made lowercase.
    gtd = models.CharField(db_column='GTD', max_length=23, blank=True, null=True)  # Field name made lowercase.
    tamogr = models.CharField(db_column='TAMOGR', max_length=250, blank=True, null=True)  # Field name made lowercase.
    numpts = models.CharField(db_column='NUMPTS', max_length=11, blank=True, null=True)  # Field name made lowercase.
    datpts = models.DateTimeField(db_column='DATPTS', blank=True, null=True)  # Field name made lowercase.
    lnpu = models.CharField(db_column='LNPU', max_length=5, blank=True, null=True)  # Field name made lowercase.
    nomer = models.CharField(db_column='NOMER', max_length=12, blank=True, null=True)  # Field name made lowercase.
    tpo = models.CharField(db_column='TPO', max_length=26, blank=True, null=True)  # Field name made lowercase.
    datud = models.DateTimeField(db_column='DATUD', blank=True, null=True)  # Field name made lowercase.
    inspectu = models.CharField(db_column='INSPECTU', max_length=50, blank=True, null=True)  # Field name made lowercase.
    inspectp = models.CharField(db_column='INSPECTP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lnpp = models.CharField(db_column='LNPP', max_length=5, blank=True, null=True)  # Field name made lowercase.
    p_ts = models.CharField(db_column='P_TS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tnved = models.CharField(db_column='TNVED', max_length=10, blank=True, null=True)  # Field name made lowercase.
    regim = models.CharField(db_column='REGIM', max_length=2, blank=True, null=True)  # Field name made lowercase.
    naprav = models.CharField(db_column='NAPRAV', max_length=2, blank=True, null=True)  # Field name made lowercase.
    p_lgot = models.CharField(db_column='P_LGOT', max_length=1, blank=True, null=True)  # Field name made lowercase.
    datback = models.DateTimeField(db_column='DATBACK', blank=True, null=True)  # Field name made lowercase.
    inn = models.CharField(db_column='INN', max_length=12, blank=True, null=True)  # Field name made lowercase.
    nom_doc = models.CharField(db_column='NOM_DOC', max_length=25, blank=True, null=True)  # Field name made lowercase.
    ser_doc = models.CharField(db_column='SER_DOC', max_length=11, blank=True, null=True)  # Field name made lowercase.
    cod_doc = models.CharField(db_column='COD_DOC', max_length=2, blank=True, null=True)  # Field name made lowercase.
    dat_doc = models.DateTimeField(db_column='DAT_DOC', blank=True, null=True)  # Field name made lowercase.
    strown = models.CharField(db_column='STROWN', max_length=3, blank=True, null=True)  # Field name made lowercase.
    vtt = models.CharField(db_column='VTT', max_length=23, blank=True, null=True)  # Field name made lowercase.
    mdp = models.CharField(db_column='MDP', max_length=23, blank=True, null=True)  # Field name made lowercase.
    probeg = models.IntegerField(db_column='PROBEG', blank=True, null=True)  # Field name made lowercase.
    srok = models.SmallIntegerField(db_column='SROK', blank=True, null=True)  # Field name made lowercase.
    tamgoal = models.CharField(db_column='TAMGOAL', max_length=8, blank=True, null=True)  # Field name made lowercase.
    tamstoim = models.DecimalField(default=0.00, db_column='TAMSTOIM', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tamplat = models.DecimalField(default=0.00, db_column='TAMPLAT', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sumedst = models.DecimalField(default=0.00, db_column='SUMEDST', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sovplat = models.DecimalField(default=0.00, db_column='SOVPLAT', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tamoform = models.DecimalField(default=0.00, db_column='TAMOFORM', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sumnote = models.DecimalField(default=0.00, db_column='SUMNOTE', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    p_plata = models.CharField(db_column='P_PLATA', max_length=1, blank=True, null=True)  # Field name made lowercase.
    p_str = models.CharField(db_column='P_STR', max_length=1, blank=True, null=True)  # Field name made lowercase.
    p_period = models.CharField(db_column='P_PERIOD', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tamu = models.CharField(db_column='TAMU', max_length=8, blank=True, null=True)  # Field name made lowercase.
    tamp = models.CharField(db_column='TAMP', max_length=8, blank=True, null=True)  # Field name made lowercase.
    uvcomm1 = models.CharField(db_column='UVCOMM1', max_length=45, blank=True, null=True)  # Field name made lowercase.
    uvcomm2 = models.CharField(db_column='UVCOMM2', max_length=75, blank=True, null=True)  # Field name made lowercase.
    uvcomm3 = models.CharField(db_column='UVCOMM3', max_length=75, blank=True, null=True)  # Field name made lowercase.
    dockonf = models.CharField(db_column='DOCKONF', max_length=28, blank=True, null=True)  # Field name made lowercase.
    tam_back = models.CharField(db_column='TAM_BACK', max_length=8, blank=True, null=True)  # Field name made lowercase.
    back_dat = models.DateTimeField(db_column='BACK_DAT', blank=True, null=True)  # Field name made lowercase.
    doc_dat = models.DateTimeField(db_column='DOC_DAT', blank=True, null=True)  # Field name made lowercase.
    doc_num = models.CharField(db_column='DOC_NUM', max_length=30, blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(db_column='NOTE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    datsend = models.DateTimeField(db_column='DATSEND', blank=True, null=True)  # Field name made lowercase.
    datrecv = models.DateTimeField(db_column='DATRECV', blank=True, null=True)  # Field name made lowercase.
    post = models.CharField(db_column='POST', max_length=2, blank=True, null=True)  # Field name made lowercase.
    otdel = models.CharField(db_column='OTDEL', max_length=1, blank=True, null=True)  # Field name made lowercase.
    datres = models.DateTimeField(db_column='DATRES', blank=True, null=True)  # Field name made lowercase.
    res = models.CharField(db_column='RES', max_length=10, blank=True, null=True)  # Field name made lowercase.
    texop = models.CharField(db_column='TEXOP', max_length=1, blank=True, null=True)  # Field name made lowercase.
    texdat = models.DateTimeField(db_column='TEXDAT', blank=True, null=True)  # Field name made lowercase.
    give_doc = models.CharField(db_column='GIVE_DOC', max_length=150, blank=True, null=True)  # Field name made lowercase.
    soato = models.CharField(db_column='SOATO', max_length=4, blank=True, null=True)  # Field name made lowercase.
    codt_to = models.CharField(db_column='CODT_TO', max_length=8, blank=True, null=True)  # Field name made lowercase.
    dat_to = models.DateTimeField(db_column='DAT_TO', blank=True, null=True)  # Field name made lowercase.
    num_dkd = models.CharField(db_column='NUM_DKD', max_length=7, blank=True, null=True)  # Field name made lowercase.
    num_ddkd = models.CharField(db_column='NUM_DDKD', max_length=7, blank=True, null=True)  # Field name made lowercase.
    num_ts = models.SmallIntegerField(db_column='NUM_TS', blank=True, null=True)  # Field name made lowercase.
    kol_ntp = models.SmallIntegerField(db_column='KOL_NTP', blank=True, null=True)  # Field name made lowercase.
    dep_tpo = models.CharField(db_column='DEP_TPO', max_length=26, blank=True, null=True)  # Field name made lowercase.
    sum_dep = models.FloatField(default=0.00, db_column='SUM_DEP', blank=True, null=True)  # Field name made lowercase.
    pred_dkd = models.CharField(db_column='PRED_DKD', max_length=23, blank=True, null=True)  # Field name made lowercase.
    f_stoim = models.DecimalField(default=0.00, db_column='F_STOIM', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    kod_val = models.CharField(db_column='KOD_VAL', max_length=3, blank=True, null=True)  # Field name made lowercase.
    doc_vl_ts = models.CharField(db_column='DOC_VL_TS', max_length=60, blank=True, null=True)  # Field name made lowercase.
    doc_id_ts = models.CharField(db_column='DOC_ID_TS', max_length=60, blank=True, null=True)  # Field name made lowercase.
    ocenka = models.DecimalField(default=0.00, db_column='OCENKA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dat_post = models.DateTimeField(db_column='DAT_POST', blank=True, null=True)  # Field name made lowercase.
    dat_ndost = models.DateTimeField(db_column='DAT_NDOST', blank=True, null=True)  # Field name made lowercase.
    doc_ndost = models.CharField(db_column='DOC_NDOST', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kod1 = models.CharField(db_column='KOD1', max_length=3, blank=True, null=True)  # Field name made lowercase.
    kod2 = models.CharField(db_column='KOD2', max_length=3, blank=True, null=True)  # Field name made lowercase.
    kod3 = models.CharField(db_column='KOD3', max_length=3, blank=True, null=True)  # Field name made lowercase.
    shablon = models.CharField(db_column='SHABLON', max_length=25, blank=True, null=True)  # Field name made lowercase.
    kodmrk = models.CharField(db_column='KODMRK', max_length=3, blank=True, null=True)  # Field name made lowercase.
    d_state = models.CharField(db_column='D_STATE', max_length=19, blank=True, null=True)  # Field name made lowercase.
    lnp_cust = models.CharField(db_column='LNP_CUST', max_length=8, blank=True, null=True)  # Field name made lowercase.
    d_unloadbl = models.DateTimeField(db_column='D_UNLOADBL', blank=True, null=True)  # Field name made lowercase.
    avtodel = models.CharField(db_column='AVTODEL', max_length=3, blank=True, null=True)  # Field name made lowercase.
    ekoclass = models.CharField(db_column='EKOCLASS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    kabina = models.CharField(db_column='KABINA', max_length=40, blank=True, null=True)  # Field name made lowercase.
    list_col = models.CharField(db_column='LIST_COL', max_length=43, blank=True, null=True)  # Field name made lowercase.
    kpp = models.CharField(db_column='KPP', max_length=9, blank=True, null=True)  # Field name made lowercase.
    z_address = models.CharField(db_column='Z_ADDRESS', max_length=150, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=23, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'AVTOMOVE'


class Dbramnum(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g32 = models.IntegerField(db_column='G32', blank=True, null=True)  # Field name made lowercase.
    series = models.CharField(db_column='SERIES', max_length=9, blank=True, null=True)  # Field name made lowercase.
    numstart = models.IntegerField(db_column='NUMSTART', blank=True, null=True)  # Field name made lowercase.
    numend = models.IntegerField(db_column='NUMEND', blank=True, null=True)  # Field name made lowercase.
    kolvoam = models.IntegerField(db_column='KOLVOAM', blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'DBRAMNUM'


class Dbravtmb(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g32 = models.IntegerField(db_column='G32', blank=True, null=True)  # Field name made lowercase.
    nud = models.CharField(db_column='NUD', max_length=12, blank=True, null=True)  # Field name made lowercase.
    kodmrk = models.CharField(db_column='KODMRK', max_length=3, blank=True, null=True)  # Field name made lowercase.
    namemrkcar = models.CharField(db_column='NAMEMRKCAR', max_length=250, blank=True, null=True)  # Field name made lowercase.
    model = models.CharField(db_column='MODEL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    year = models.SmallIntegerField(db_column='YEAR', blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(default=0.00, db_column='PRICE', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    obem = models.DecimalField(default=0.00, db_column='OBEM', max_digits=17, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(db_column='ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nkuz = models.CharField(db_column='NKUZ', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kabina = models.CharField(db_column='KABINA', max_length=40, blank=True, null=True)  # Field name made lowercase.
    nsh = models.CharField(db_column='NSH', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ndv = models.CharField(db_column='NDV', max_length=40, blank=True, null=True)  # Field name made lowercase.
    emergency = models.CharField(db_column='EMERGENCY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    prim = models.CharField(db_column='PRIM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    probeg = models.DecimalField(default=0.00, db_column='PROBEG', max_digits=17, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.
    pricev = models.CharField(db_column='PRICEV', max_length=3, blank=True, null=True)  # Field name made lowercase.
    maxpower1 = models.DecimalField(default=0.00, db_column='MAXPOWER1', max_digits=17, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    maxpower2 = models.DecimalField(default=0.00, db_column='MAXPOWER2', max_digits=17, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    maxpower3 = models.DecimalField(default=0.00, db_column='MAXPOWER3', max_digits=17, decimal_places=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'DBRAVTMB'


class Dbrcont(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g32 = models.IntegerField(db_column='G32', blank=True, null=True)  # Field name made lowercase.
    container = models.CharField(db_column='CONTAINER', max_length=17, blank=True, null=True)  # Field name made lowercase.
    conttype = models.CharField(db_column='CONTTYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    contstat = models.CharField(db_column='CONTSTAT', max_length=1, blank=True, null=True)  # Field name made lowercase.
    nzp = models.DecimalField(default=0.00, db_column='NZP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dmodify = models.DateTimeField(db_column='DMODIFY', blank=True, null=True)  # Field name made lowercase.
    tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    p_edoc_id = models.DecimalField(default=0.00, db_column='P_EDOC_ID', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'DBRCONT'


class Dbrcrdts(BaseModel):
    numcard = models.CharField(db_column='NUMCARD', max_length=23, blank=True, null=True)  # Field name made lowercase.
    vin = models.CharField(db_column='VIN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kodmrk = models.CharField(db_column='KODMRK', max_length=3, blank=True, null=True)  # Field name made lowercase.
    namemrkcar = models.CharField(db_column='NAMEMRKCAR', max_length=250, blank=True, null=True)  # Field name made lowercase.
    model = models.CharField(db_column='MODEL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tipts = models.CharField(db_column='TIPTS', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tipts3 = models.CharField(db_column='TIPTS3', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tiptsname = models.CharField(db_column='TIPTSNAME', max_length=150, blank=True, null=True)  # Field name made lowercase.
    kategts = models.CharField(db_column='KATEGTS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    mest = models.SmallIntegerField(db_column='MEST', blank=True, null=True)  # Field name made lowercase.
    god = models.SmallIntegerField(db_column='GOD', blank=True, null=True)  # Field name made lowercase.
    moddvig = models.CharField(db_column='MODDVIG', max_length=15, blank=True, null=True)  # Field name made lowercase.
    numdvig = models.CharField(db_column='NUMDVIG', max_length=40, blank=True, null=True)  # Field name made lowercase.
    numkper = models.CharField(db_column='NUMKPER', max_length=40, blank=True, null=True)  # Field name made lowercase.
    nummost = models.CharField(db_column='NUMMOST', max_length=80, blank=True, null=True)  # Field name made lowercase.
    shassi = models.CharField(db_column='SHASSI', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kuzov = models.CharField(db_column='KUZOV', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kabina = models.CharField(db_column='KABINA', max_length=40, blank=True, null=True)  # Field name made lowercase.
    emergency = models.CharField(db_column='EMERGENCY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    zvet = models.CharField(db_column='ZVET', max_length=3, blank=True, null=True)  # Field name made lowercase.
    listcol = models.CharField(db_column='LISTCOL', max_length=43, blank=True, null=True)  # Field name made lowercase.
    powerls = models.FloatField(default=0.00, db_column='POWERLS', blank=True, null=True)  # Field name made lowercase.
    powerkw = models.FloatField(default=0.00, db_column='POWERKW', blank=True, null=True)  # Field name made lowercase.
    obdvig = models.IntegerField(db_column='OBDVIG', blank=True, null=True)  # Field name made lowercase.
    tipdv = models.CharField(db_column='TIPDV', max_length=2, blank=True, null=True)  # Field name made lowercase.
    viddvig = models.CharField(db_column='VIDDVIG', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ekoclass = models.CharField(db_column='EKOCLASS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    maxmass = models.IntegerField(db_column='MAXMASS', blank=True, null=True)  # Field name made lowercase.
    minmass = models.IntegerField(db_column='MINMASS', blank=True, null=True)  # Field name made lowercase.
    maxspeed = models.SmallIntegerField(db_column='MAXSPEED', blank=True, null=True)  # Field name made lowercase.
    width = models.IntegerField(db_column='WIDTH', blank=True, null=True)  # Field name made lowercase.
    height = models.IntegerField(db_column='HEIGHT', blank=True, null=True)  # Field name made lowercase.
    length = models.IntegerField(db_column='LENGTH', blank=True, null=True)  # Field name made lowercase.
    kodizgot = models.CharField(db_column='KODIZGOT', max_length=3, blank=True, null=True)  # Field name made lowercase.
    izgotov = models.CharField(db_column='IZGOTOV', max_length=150, blank=True, null=True)  # Field name made lowercase.
    strizg = models.CharField(db_column='STRIZG', max_length=2, blank=True, null=True)  # Field name made lowercase.
    izgpost = models.CharField(db_column='IZGPOST', max_length=9, blank=True, null=True)  # Field name made lowercase.
    izgstr = models.CharField(db_column='IZGSTR', max_length=2, blank=True, null=True)  # Field name made lowercase.
    izgsubd = models.CharField(db_column='IZGSUBD', max_length=35, blank=True, null=True)  # Field name made lowercase.
    izgcity = models.CharField(db_column='IZGCITY', max_length=35, blank=True, null=True)  # Field name made lowercase.
    izgstreet = models.CharField(db_column='IZGSTREET', max_length=35, blank=True, null=True)  # Field name made lowercase.
    numodob = models.CharField(db_column='NUMODOB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    datodob = models.DateTimeField(db_column='DATODOB', blank=True, null=True)  # Field name made lowercase.
    orgodob = models.CharField(db_column='ORGODOB', max_length=150, blank=True, null=True)  # Field name made lowercase.
    strvyvoz = models.CharField(db_column='STRVYVOZ', max_length=2, blank=True, null=True)  # Field name made lowercase.
    lic = models.CharField(db_column='LIC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fam = models.CharField(db_column='FAM', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ima = models.CharField(db_column='IMA', max_length=25, blank=True, null=True)  # Field name made lowercase.
    otc = models.CharField(db_column='OTC', max_length=25, blank=True, null=True)  # Field name made lowercase.
    okpo = models.CharField(db_column='OKPO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    inn = models.CharField(db_column='INN', max_length=12, blank=True, null=True)  # Field name made lowercase.
    kpp = models.CharField(db_column='KPP', max_length=9, blank=True, null=True)  # Field name made lowercase.
    kod_dul = models.CharField(db_column='KOD_DUL', max_length=7, blank=True, null=True)  # Field name made lowercase.
    abbrev_dul = models.CharField(db_column='ABBREV_DUL', max_length=6, blank=True, null=True)  # Field name made lowercase.
    ser_dul = models.CharField(db_column='SER_DUL', max_length=11, blank=True, null=True)  # Field name made lowercase.
    nom_dul = models.CharField(db_column='NOM_DUL', max_length=25, blank=True, null=True)  # Field name made lowercase.
    org_dul = models.CharField(db_column='ORG_DUL', max_length=150, blank=True, null=True)  # Field name made lowercase.
    dat_dul = models.DateTimeField(db_column='DAT_DUL', blank=True, null=True)  # Field name made lowercase.
    namesob = models.CharField(db_column='NAMESOB', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sobpost = models.CharField(db_column='SOBPOST', max_length=9, blank=True, null=True)  # Field name made lowercase.
    sobstr = models.CharField(db_column='SOBSTR', max_length=2, blank=True, null=True)  # Field name made lowercase.
    sobsubd = models.CharField(db_column='SOBSUBD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sobcity = models.CharField(db_column='SOBCITY', max_length=35, blank=True, null=True)  # Field name made lowercase.
    sobstreet = models.CharField(db_column='SOBSTREET', max_length=50, blank=True, null=True)  # Field name made lowercase.
    udvvoz = models.CharField(db_column='UDVVOZ', max_length=10, blank=True, null=True)  # Field name made lowercase.
    datud = models.DateTimeField(db_column='DATUD', blank=True, null=True)  # Field name made lowercase.
    lnpu = models.CharField(db_column='LNPU', max_length=4, blank=True, null=True)  # Field name made lowercase.
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    tamogr = models.CharField(db_column='TAMOGR', max_length=250, blank=True, null=True)  # Field name made lowercase.
    tamspec = models.CharField(db_column='TAMSPEC', max_length=250, blank=True, null=True)  # Field name made lowercase.
    numpts = models.CharField(db_column='NUMPTS', max_length=15, blank=True, null=True)  # Field name made lowercase.
    datpts = models.DateTimeField(db_column='DATPTS', blank=True, null=True)  # Field name made lowercase.
    timpts = models.CharField(db_column='TIMPTS', max_length=8, blank=True, null=True)  # Field name made lowercase.
    lnp = models.CharField(db_column='LNP', max_length=4, blank=True, null=True)  # Field name made lowercase.
    work = models.IntegerField(db_column='WORK', blank=True, null=True)  # Field name made lowercase.
    p_ts = models.CharField(db_column='P_TS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g32 = models.IntegerField(db_column='G32', blank=True, null=True)  # Field name made lowercase.
    g33 = models.CharField(db_column='G33', max_length=10, blank=True, null=True)  # Field name made lowercase.
    naimtd = models.CharField(db_column='NAIMTD', max_length=250, blank=True, null=True)  # Field name made lowercase.
    numtd = models.CharField(db_column='NUMTD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dattd = models.DateTimeField(db_column='DATTD', blank=True, null=True)  # Field name made lowercase.
    numz = models.CharField(db_column='NUMZ', max_length=23, blank=True, null=True)  # Field name made lowercase.
    datz = models.DateTimeField(db_column='DATZ', blank=True, null=True)  # Field name made lowercase.
    dateout = models.DateTimeField(db_column='DATEOUT', blank=True, null=True)  # Field name made lowercase.
    timeout = models.CharField(db_column='TIMEOUT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    datemodi = models.DateTimeField(db_column='DATEMODI', blank=True, null=True)  # Field name made lowercase.
    tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    imodi = models.CharField(db_column='IMODI', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ind_k = models.CharField(db_column='IND_K', max_length=1, blank=True, null=True)  # Field name made lowercase.
    d_state = models.CharField(db_column='D_STATE', max_length=19, blank=True, null=True)  # Field name made lowercase.
    d_unload = models.CharField(db_column='D_UNLOAD', max_length=19, blank=True, null=True)  # Field name made lowercase.
    nzp = models.DecimalField(default=0.00, db_column='NZP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    p_edoc_id = models.DecimalField(default=0.00, db_column='P_EDOC_ID', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    strizgc = models.CharField(db_column='STRIZGC', max_length=3, blank=True, null=True)  # Field name made lowercase.
    adrizg = models.CharField(db_column='ADRIZG', max_length=50, blank=True, null=True)  # Field name made lowercase.
    strvyvozc = models.CharField(db_column='STRVYVOZC', max_length=3, blank=True, null=True)  # Field name made lowercase.
    adressob = models.CharField(db_column='ADRESSOB', max_length=80, blank=True, null=True)  # Field name made lowercase.
    ed_idid = models.CharField(db_column='ED_IDID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    numptso = models.CharField(db_column='NUMPTSO', max_length=11, blank=True, null=True)  # Field name made lowercase.
    stsptso = models.CharField(db_column='STSPTSO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ub_idid = models.CharField(db_column='UB_IDID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    yc_status = models.CharField(db_column='YC_STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    yc_tpo = models.CharField(db_column='YC_TPO', max_length=26, blank=True, null=True)  # Field name made lowercase.
    yc_matter = models.CharField(db_column='YC_MATTER', max_length=2, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.
    kateg3 = models.CharField(db_column='KATEG3', max_length=3, blank=True, null=True)  # Field name made lowercase.
    epts = models.CharField(db_column='EPTS', max_length=15, blank=True, null=True)  # Field name made lowercase.
    tipdvname = models.CharField(db_column='TIPDVNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fuel = models.CharField(db_column='FUEL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    powerls2 = models.FloatField(default=0.00, db_column='POWERLS2', blank=True, null=True)  # Field name made lowercase.
    powerkw2 = models.FloatField(default=0.00, db_column='POWERKW2', blank=True, null=True)  # Field name made lowercase.
    tipdv2 = models.CharField(db_column='TIPDV2', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tipdvname2 = models.CharField(db_column='TIPDVNAME2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fuel2 = models.CharField(db_column='FUEL2', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'DBRCRDTS'


class Dbrdinf2(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g32 = models.IntegerField(db_column='G32', blank=True, null=True)  # Field name made lowercase.
    type_info = models.CharField(db_column='TYPE_INFO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    numpredd = models.IntegerField(db_column='NUMPREDD', blank=True, null=True)  # Field name made lowercase.
    ngr = models.CharField(db_column='NGR', max_length=2, blank=True, null=True)  # Field name made lowercase.
    typ_ngr = models.CharField(db_column='TYP_NGR', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g32g = models.SmallIntegerField(db_column='G32G', blank=True, null=True)  # Field name made lowercase.
    numrec = models.DecimalField(default=0.00, db_column='NUMREC', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    text1 = models.CharField(db_column='TEXT1', max_length=250, blank=True, null=True)  # Field name made lowercase.
    text2 = models.CharField(db_column='TEXT2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nzp = models.SmallIntegerField(db_column='NZP', blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'DBRDINF2'


class Dbrdinfo(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g32 = models.IntegerField(db_column='G32', blank=True, null=True)  # Field name made lowercase.
    ngr = models.CharField(db_column='NGR', max_length=2, blank=True, null=True)  # Field name made lowercase.
    typ_ngr = models.CharField(db_column='TYP_NGR', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g32g = models.SmallIntegerField(db_column='G32G', blank=True, null=True)  # Field name made lowercase.
    numrec = models.DecimalField(default=0.00, db_column='NUMREC', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    text1 = models.CharField(db_column='TEXT1', max_length=250, blank=True, null=True)  # Field name made lowercase.
    ind_text = models.CharField(db_column='IND_TEXT', max_length=3, blank=True, null=True)  # Field name made lowercase.
    text2 = models.CharField(db_column='TEXT2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    typ_izm = models.CharField(db_column='TYP_IZM', max_length=1, blank=True, null=True)  # Field name made lowercase.
    kolvo = models.DecimalField(default=0.00, db_column='KOLVO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    code_edi = models.CharField(db_column='CODE_EDI', max_length=3, blank=True, null=True)  # Field name made lowercase.
    name_edi = models.CharField(db_column='NAME_EDI', max_length=17, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'DBRDINFO'


class Dbrdog(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g32 = models.IntegerField(db_column='G32', blank=True, null=True)  # Field name made lowercase.
    dogn = models.CharField(db_column='DOGN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dogd = models.DateTimeField(db_column='DOGD', blank=True, null=True)  # Field name made lowercase.
    pasp = models.CharField(db_column='PASP', max_length=25, blank=True, null=True)  # Field name made lowercase.
    paspbank = models.CharField(db_column='PASPBANK', max_length=70, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'DBRDOG'


class Dbrdoga(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g32 = models.IntegerField(db_column='G32', blank=True, null=True)  # Field name made lowercase.
    dogn = models.CharField(db_column='DOGN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dogd = models.DateTimeField(db_column='DOGD', blank=True, null=True)  # Field name made lowercase.
    dogaddn = models.CharField(db_column='DOGADDN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dogaddd = models.DateTimeField(db_column='DOGADDD', blank=True, null=True)  # Field name made lowercase.
    dogaddt = models.CharField(db_column='DOGADDT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'DBRDOGA'


class Dbrdogt(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g32 = models.IntegerField(db_column='G32', blank=True, null=True)  # Field name made lowercase.
    dogn = models.CharField(db_column='DOGN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dogd = models.DateTimeField(db_column='DOGD', blank=True, null=True)  # Field name made lowercase.
    dognpp = models.SmallIntegerField(db_column='DOGNPP', blank=True, null=True)  # Field name made lowercase.
    dogorg = models.CharField(db_column='DOGORG', max_length=150, blank=True, null=True)  # Field name made lowercase.
    dogcountry = models.CharField(db_column='DOGCOUNTRY', max_length=2, blank=True, null=True)  # Field name made lowercase.
    origcountr = models.CharField(db_column='ORIGCOUNTR', max_length=2, blank=True, null=True)  # Field name made lowercase.
    terms = models.CharField(db_column='TERMS', max_length=3, blank=True, null=True)  # Field name made lowercase.
    termspoint = models.CharField(db_column='TERMSPOINT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    termspass = models.CharField(db_column='TERMSPASS', max_length=250, blank=True, null=True)  # Field name made lowercase.
    qmain = models.DecimalField(default=0.00, db_column='QMAIN', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    qadd = models.DecimalField(default=0.00, db_column='QADD', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    qaddmeas = models.CharField(db_column='QADDMEAS', max_length=3, blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(default=0.00, db_column='PRICE', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    prval = models.CharField(db_column='PRVAL', max_length=3, blank=True, null=True)  # Field name made lowercase.
    prmeas = models.CharField(db_column='PRMEAS', max_length=3, blank=True, null=True)  # Field name made lowercase.
    prtot = models.DecimalField(default=0.00, db_column='PRTOT', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    prtotval = models.CharField(db_column='PRTOTVAL', max_length=3, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'DBRDOGT'


class Dbrdop48(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    gb1 = models.CharField(db_column='GB1', max_length=4, blank=True, null=True)  # Field name made lowercase.
    g48 = models.DateTimeField(db_column='G48', blank=True, null=True)  # Field name made lowercase.
    g48period = models.SmallIntegerField(db_column='G48PERIOD', blank=True, null=True)  # Field name made lowercase.
    g48last = models.DateTimeField(db_column='G48LAST', blank=True, null=True)  # Field name made lowercase.
    nzp = models.DecimalField(default=0.00, db_column='NZP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dmodify = models.DateTimeField(db_column='DMODIFY', blank=True, null=True)  # Field name made lowercase.
    tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    p_edoc_id = models.DecimalField(default=0.00, db_column='P_EDOC_ID', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'DBRDOP48'


class Dbrhead(BaseModel):
    num_ver = models.CharField(db_column='NUM_VER', max_length=8, blank=True, null=True)  # Field name made lowercase.
    data_ver = models.DateTimeField(db_column='DATA_VER', blank=True, null=True)  # Field name made lowercase.
    typ_dcl = models.CharField(db_column='TYP_DCL', max_length=2, blank=True, null=True)  # Field name made lowercase.
    gugtk = models.BooleanField(db_column='GUGTK', blank=True, null=True)  # Field name made lowercase.
    copy = models.BooleanField(db_column='COPY', blank=True, null=True)  # Field name made lowercase.
    dcopy = models.DateTimeField(db_column='DCOPY', blank=True, null=True)  # Field name made lowercase.
    q_edit = models.SmallIntegerField(db_column='Q_EDIT', blank=True, null=True)  # Field name made lowercase.
    d_edit = models.DateTimeField(db_column='D_EDIT', blank=True, null=True)  # Field name made lowercase.
    sol = models.SmallIntegerField(db_column='SOL', blank=True, null=True)  # Field name made lowercase.
    max_err = models.SmallIntegerField(db_column='MAX_ERR', blank=True, null=True)  # Field name made lowercase.
    dd = models.DateTimeField(db_column='DD', blank=True, null=True)  # Field name made lowercase.
    tm = models.CharField(db_column='TM', max_length=8, blank=True, null=True)  # Field name made lowercase.
    extrnl = models.CharField(db_column='EXTRNL', max_length=80, blank=True, null=True)  # Field name made lowercase.
    schet = models.CharField(db_column='SCHET', max_length=160, blank=True, null=True)  # Field name made lowercase.
    stepctrl = models.CharField(db_column='STEPCTRL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    typ_dtc = models.CharField(db_column='TYP_DTC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    vid_ktc = models.CharField(db_column='VID_KTC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    stat = models.CharField(db_column='STAT', max_length=1, blank=True, null=True)  # Field name made lowercase.
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    ui_b_1 = models.CharField(db_column='UI_B_1', max_length=8, blank=True, null=True)  # Field name made lowercase.
    ui_b_2 = models.DateTimeField(db_column='UI_B_2', blank=True, null=True)  # Field name made lowercase.
    ui_b_3 = models.CharField(db_column='UI_B_3', max_length=7, blank=True, null=True)  # Field name made lowercase.
    sds_srv = models.CharField(db_column='SDS_SRV', max_length=4, blank=True, null=True)  # Field name made lowercase.
    sds_num = models.DecimalField(default=0.00, db_column='SDS_NUM', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sds_cust = models.CharField(db_column='SDS_CUST', max_length=8, blank=True, null=True)  # Field name made lowercase.
    f_decl = models.CharField(db_column='F_DECL', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rccncode = models.CharField(db_column='RCCNCODE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    dpresent = models.DateTimeField(db_column='DPRESENT', blank=True, null=True)  # Field name made lowercase.
    tpresent = models.CharField(db_column='TPRESENT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    complectbl = models.CharField(db_column='COMPLECTBL', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g011 = models.CharField(db_column='G011', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g0121 = models.CharField(db_column='G0121', max_length=3, blank=True, null=True)  # Field name made lowercase.
    g0131 = models.CharField(db_column='G0131', max_length=3, blank=True, null=True)  # Field name made lowercase.
    k0131 = models.CharField(db_column='K0131', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g020 = models.CharField(db_column='G020', max_length=15, blank=True, null=True)  # Field name made lowercase.
    g02_itn = models.CharField(db_column='G02_ITN', max_length=13, blank=True, null=True)  # Field name made lowercase.
    g021 = models.CharField(db_column='G021', max_length=40, blank=True, null=True)  # Field name made lowercase.
    g022 = models.CharField(db_column='G022', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g023post = models.CharField(db_column='G023POST', max_length=9, blank=True, null=True)  # Field name made lowercase.
    g0231 = models.CharField(db_column='G0231', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g0231n = models.CharField(db_column='G0231N', max_length=40, blank=True, null=True)  # Field name made lowercase.
    g023subd = models.CharField(db_column='G023SUBD', max_length=120, blank=True, null=True)  # Field name made lowercase.
    g023city = models.CharField(db_column='G023CITY', max_length=120, blank=True, null=True)  # Field name made lowercase.
    g023street = models.CharField(db_column='G023STREET', max_length=120, blank=True, null=True)  # Field name made lowercase.
    g024b = models.CharField(db_column='G024B', max_length=5, blank=True, null=True)  # Field name made lowercase.
    g024n = models.CharField(db_column='G024N', max_length=10, blank=True, null=True)  # Field name made lowercase.
    g024in = models.CharField(db_column='G024IN', max_length=12, blank=True, null=True)  # Field name made lowercase.
    g027 = models.CharField(db_column='G027', max_length=12, blank=True, null=True)  # Field name made lowercase.
    g0281 = models.CharField(db_column='G0281', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g0281a = models.CharField(db_column='G0281A', max_length=15, blank=True, null=True)  # Field name made lowercase.
    g02821 = models.CharField(db_column='G02821', max_length=11, blank=True, null=True)  # Field name made lowercase.
    g02822 = models.CharField(db_column='G02822', max_length=25, blank=True, null=True)  # Field name made lowercase.
    g02823 = models.CharField(db_column='G02823', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g0283 = models.DateTimeField(db_column='G0283', blank=True, null=True)  # Field name made lowercase.
    g022a = models.CharField(db_column='G022A', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g027a = models.CharField(db_column='G027A', max_length=12, blank=True, null=True)  # Field name made lowercase.
    g023apost = models.CharField(db_column='G023APOST', max_length=9, blank=True, null=True)  # Field name made lowercase.
    g0231a = models.CharField(db_column='G0231A', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g0231an = models.CharField(db_column='G0231AN', max_length=40, blank=True, null=True)  # Field name made lowercase.
    g023asubd = models.CharField(db_column='G023ASUBD', max_length=120, blank=True, null=True)  # Field name made lowercase.
    g023acity = models.CharField(db_column='G023ACITY', max_length=120, blank=True, null=True)  # Field name made lowercase.
    g023astree = models.CharField(db_column='G023ASTREE', max_length=120, blank=True, null=True)  # Field name made lowercase.
    g029 = models.CharField(db_column='G029', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g02sm14 = models.CharField(db_column='G02SM14', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g032 = models.IntegerField(db_column='G032', blank=True, null=True)  # Field name made lowercase.
    g040 = models.IntegerField(db_column='G040', blank=True, null=True)  # Field name made lowercase.
    g04 = models.IntegerField(db_column='G04', blank=True, null=True)  # Field name made lowercase.
    g05 = models.IntegerField(db_column='G05', blank=True, null=True)  # Field name made lowercase.
    g06 = models.IntegerField(db_column='G06', blank=True, null=True)  # Field name made lowercase.
    g07 = models.CharField(db_column='G07', max_length=3, blank=True, null=True)  # Field name made lowercase.
    g080 = models.CharField(db_column='G080', max_length=15, blank=True, null=True)  # Field name made lowercase.
    g08_itn = models.CharField(db_column='G08_ITN', max_length=13, blank=True, null=True)  # Field name made lowercase.
    g081 = models.CharField(db_column='G081', max_length=40, blank=True, null=True)  # Field name made lowercase.
    g082 = models.CharField(db_column='G082', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g083post = models.CharField(db_column='G083POST', max_length=9, blank=True, null=True)  # Field name made lowercase.
    g0831 = models.CharField(db_column='G0831', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g0831a = models.CharField(db_column='G0831A', max_length=40, blank=True, null=True)  # Field name made lowercase.
    g083subd = models.CharField(db_column='G083SUBD', max_length=120, blank=True, null=True)  # Field name made lowercase.
    g083city = models.CharField(db_column='G083CITY', max_length=120, blank=True, null=True)  # Field name made lowercase.
    g083street = models.CharField(db_column='G083STREET', max_length=120, blank=True, null=True)  # Field name made lowercase.
    g084b = models.CharField(db_column='G084B', max_length=5, blank=True, null=True)  # Field name made lowercase.
    g087 = models.CharField(db_column='G087', max_length=12, blank=True, null=True)  # Field name made lowercase.
    g0881 = models.CharField(db_column='G0881', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g0881a = models.CharField(db_column='G0881A', max_length=15, blank=True, null=True)  # Field name made lowercase.
    g08821 = models.CharField(db_column='G08821', max_length=11, blank=True, null=True)  # Field name made lowercase.
    g08822 = models.CharField(db_column='G08822', max_length=25, blank=True, null=True)  # Field name made lowercase.
    g08823 = models.CharField(db_column='G08823', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g0883 = models.DateTimeField(db_column='G0883', blank=True, null=True)  # Field name made lowercase.
    g089 = models.CharField(db_column='G089', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g082a = models.CharField(db_column='G082A', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g087a = models.CharField(db_column='G087A', max_length=12, blank=True, null=True)  # Field name made lowercase.
    g083apost = models.CharField(db_column='G083APOST', max_length=9, blank=True, null=True)  # Field name made lowercase.
    g0831aa = models.CharField(db_column='G0831AA', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g0831an = models.CharField(db_column='G0831AN', max_length=40, blank=True, null=True)  # Field name made lowercase.
    g083asubd = models.CharField(db_column='G083ASUBD', max_length=120, blank=True, null=True)  # Field name made lowercase.
    g083acity = models.CharField(db_column='G083ACITY', max_length=120, blank=True, null=True)  # Field name made lowercase.
    g083astree = models.CharField(db_column='G083ASTREE', max_length=120, blank=True, null=True)  # Field name made lowercase.
    g08sm14 = models.CharField(db_column='G08SM14', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g090 = models.CharField(db_column='G090', max_length=15, blank=True, null=True)  # Field name made lowercase.
    g09_itn = models.CharField(db_column='G09_ITN', max_length=13, blank=True, null=True)  # Field name made lowercase.
    g091 = models.CharField(db_column='G091', max_length=40, blank=True, null=True)  # Field name made lowercase.
    g092 = models.CharField(db_column='G092', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g092a = models.CharField(db_column='G092A', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g093post = models.CharField(db_column='G093POST', max_length=9, blank=True, null=True)  # Field name made lowercase.
    g0931 = models.CharField(db_column='G0931', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g0931n = models.CharField(db_column='G0931N', max_length=40, blank=True, null=True)  # Field name made lowercase.
    g093subd = models.CharField(db_column='G093SUBD', max_length=120, blank=True, null=True)  # Field name made lowercase.
    g093city = models.CharField(db_column='G093CITY', max_length=120, blank=True, null=True)  # Field name made lowercase.
    g093street = models.CharField(db_column='G093STREET', max_length=120, blank=True, null=True)  # Field name made lowercase.
    g093apost = models.CharField(db_column='G093APOST', max_length=9, blank=True, null=True)  # Field name made lowercase.
    g0931a = models.CharField(db_column='G0931A', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g0931an = models.CharField(db_column='G0931AN', max_length=40, blank=True, null=True)  # Field name made lowercase.
    g093asubd = models.CharField(db_column='G093ASUBD', max_length=120, blank=True, null=True)  # Field name made lowercase.
    g093acity = models.CharField(db_column='G093ACITY', max_length=120, blank=True, null=True)  # Field name made lowercase.
    g093astree = models.CharField(db_column='G093ASTREE', max_length=120, blank=True, null=True)  # Field name made lowercase.
    g094b = models.CharField(db_column='G094B', max_length=5, blank=True, null=True)  # Field name made lowercase.
    g097 = models.CharField(db_column='G097', max_length=12, blank=True, null=True)  # Field name made lowercase.
    g097a = models.CharField(db_column='G097A', max_length=12, blank=True, null=True)  # Field name made lowercase.
    g0981 = models.CharField(db_column='G0981', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g0981a = models.CharField(db_column='G0981A', max_length=15, blank=True, null=True)  # Field name made lowercase.
    g09821 = models.CharField(db_column='G09821', max_length=11, blank=True, null=True)  # Field name made lowercase.
    g09822 = models.CharField(db_column='G09822', max_length=25, blank=True, null=True)  # Field name made lowercase.
    g09823 = models.CharField(db_column='G09823', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g0983 = models.DateTimeField(db_column='G0983', blank=True, null=True)  # Field name made lowercase.
    g09sm14 = models.CharField(db_column='G09SM14', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g11 = models.CharField(db_column='G11', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g12 = models.DecimalField(default=0.00, db_column='G12', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    g121 = models.CharField(db_column='G121', max_length=3, blank=True, null=True)  # Field name made lowercase.
    g122 = models.DecimalField(default=0.00, db_column='G122', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    g140 = models.CharField(db_column='G140', max_length=15, blank=True, null=True)  # Field name made lowercase.
    g14_itn = models.CharField(db_column='G14_ITN', max_length=13, blank=True, null=True)  # Field name made lowercase.
    g141 = models.CharField(db_column='G141', max_length=40, blank=True, null=True)  # Field name made lowercase.
    g142 = models.CharField(db_column='G142', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g142a = models.CharField(db_column='G142A', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g143post = models.CharField(db_column='G143POST', max_length=9, blank=True, null=True)  # Field name made lowercase.
    g1431 = models.CharField(db_column='G1431', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g1431n = models.CharField(db_column='G1431N', max_length=40, blank=True, null=True)  # Field name made lowercase.
    g143subd = models.CharField(db_column='G143SUBD', max_length=120, blank=True, null=True)  # Field name made lowercase.
    g143city = models.CharField(db_column='G143CITY', max_length=120, blank=True, null=True)  # Field name made lowercase.
    g143street = models.CharField(db_column='G143STREET', max_length=120, blank=True, null=True)  # Field name made lowercase.
    g143apost = models.CharField(db_column='G143APOST', max_length=9, blank=True, null=True)  # Field name made lowercase.
    g1431a = models.CharField(db_column='G1431A', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g1431an = models.CharField(db_column='G1431AN', max_length=40, blank=True, null=True)  # Field name made lowercase.
    g143asubd = models.CharField(db_column='G143ASUBD', max_length=120, blank=True, null=True)  # Field name made lowercase.
    g143acity = models.CharField(db_column='G143ACITY', max_length=120, blank=True, null=True)  # Field name made lowercase.
    g143astree = models.CharField(db_column='G143ASTREE', max_length=120, blank=True, null=True)  # Field name made lowercase.
    g144b = models.CharField(db_column='G144B', max_length=5, blank=True, null=True)  # Field name made lowercase.
    g147 = models.CharField(db_column='G147', max_length=12, blank=True, null=True)  # Field name made lowercase.
    g147a = models.CharField(db_column='G147A', max_length=12, blank=True, null=True)  # Field name made lowercase.
    g1481 = models.CharField(db_column='G1481', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g1481a = models.CharField(db_column='G1481A', max_length=15, blank=True, null=True)  # Field name made lowercase.
    g14821 = models.CharField(db_column='G14821', max_length=11, blank=True, null=True)  # Field name made lowercase.
    g14822 = models.CharField(db_column='G14822', max_length=25, blank=True, null=True)  # Field name made lowercase.
    g14823 = models.CharField(db_column='G14823', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g1483 = models.DateTimeField(db_column='G1483', blank=True, null=True)  # Field name made lowercase.
    g15 = models.CharField(db_column='G15', max_length=40, blank=True, null=True)  # Field name made lowercase.
    g15a = models.CharField(db_column='G15A', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g16 = models.CharField(db_column='G16', max_length=40, blank=True, null=True)  # Field name made lowercase.
    g17a = models.CharField(db_column='G17A', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g17b = models.CharField(db_column='G17B', max_length=40, blank=True, null=True)  # Field name made lowercase.
    g180 = models.IntegerField(db_column='G180', blank=True, null=True)  # Field name made lowercase.
    g182 = models.CharField(db_column='G182', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g19 = models.CharField(db_column='G19', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g202 = models.CharField(db_column='G202', max_length=3, blank=True, null=True)  # Field name made lowercase.
    g2021 = models.CharField(db_column='G2021', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g203 = models.CharField(db_column='G203', max_length=250, blank=True, null=True)  # Field name made lowercase.
    g210 = models.IntegerField(db_column='G210', blank=True, null=True)  # Field name made lowercase.
    g212 = models.CharField(db_column='G212', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g221 = models.CharField(db_column='G221', max_length=3, blank=True, null=True)  # Field name made lowercase.
    g222 = models.DecimalField(default=0.00, db_column='G222', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    g23 = models.FloatField(default=0.00, db_column='G23', blank=True, null=True)  # Field name made lowercase.
    g230 = models.DateTimeField(db_column='G230', blank=True, null=True)  # Field name made lowercase.
    g270 = models.CharField(db_column='G270', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g27_itn = models.CharField(db_column='G27_ITN', max_length=13, blank=True, null=True)  # Field name made lowercase.
    g2710 = models.CharField(db_column='G2710', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g271 = models.CharField(db_column='G271', max_length=21, blank=True, null=True)  # Field name made lowercase.
    g27 = models.CharField(db_column='G27', max_length=40, blank=True, null=True)  # Field name made lowercase.
    g2711 = models.DateTimeField(db_column='G2711', blank=True, null=True)  # Field name made lowercase.
    g2712 = models.CharField(db_column='G2712', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g28_itn = models.CharField(db_column='G28_ITN', max_length=13, blank=True, null=True)  # Field name made lowercase.
    g28okpo = models.CharField(db_column='G28OKPO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    g28inn = models.CharField(db_column='G28INN', max_length=12, blank=True, null=True)  # Field name made lowercase.
    g281oth = models.CharField(db_column='G281OTH', max_length=30, blank=True, null=True)  # Field name made lowercase.
    g28zajmn = models.CharField(db_column='G28ZAJMN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g282 = models.CharField(db_column='G282', max_length=70, blank=True, null=True)  # Field name made lowercase.
    g28211 = models.CharField(db_column='G28211', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g28212 = models.CharField(db_column='G28212', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g28221 = models.CharField(db_column='G28221', max_length=3, blank=True, null=True)  # Field name made lowercase.
    g28222 = models.CharField(db_column='G28222', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g28230 = models.CharField(db_column='G28230', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g2823 = models.DateTimeField(db_column='G2823', blank=True, null=True)  # Field name made lowercase.
    g28240 = models.CharField(db_column='G28240', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g2824 = models.DateTimeField(db_column='G2824', blank=True, null=True)  # Field name made lowercase.
    g2825 = models.CharField(db_column='G2825', max_length=3, blank=True, null=True)  # Field name made lowercase.
    g30_itn = models.CharField(db_column='G30_ITN', max_length=13, blank=True, null=True)  # Field name made lowercase.
    g300 = models.CharField(db_column='G300', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g3010 = models.CharField(db_column='G3010', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g301 = models.CharField(db_column='G301', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g3011 = models.DateTimeField(db_column='G3011', blank=True, null=True)  # Field name made lowercase.
    g30 = models.CharField(db_column='G30', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g30post = models.CharField(db_column='G30POST', max_length=9, blank=True, null=True)  # Field name made lowercase.
    g30a = models.CharField(db_column='G30A', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g30an = models.CharField(db_column='G30AN', max_length=40, blank=True, null=True)  # Field name made lowercase.
    g30subd = models.CharField(db_column='G30SUBD', max_length=120, blank=True, null=True)  # Field name made lowercase.
    g30city = models.CharField(db_column='G30CITY', max_length=120, blank=True, null=True)  # Field name made lowercase.
    g30street = models.CharField(db_column='G30STREET', max_length=120, blank=True, null=True)  # Field name made lowercase.
    g30lname = models.CharField(db_column='G30LNAME', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g3012 = models.CharField(db_column='G3012', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g30121 = models.CharField(db_column='G30121', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g30122 = models.CharField(db_column='G30122', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g45a1 = models.CharField(db_column='G45A1', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g45a2 = models.CharField(db_column='G45A2', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g45a3 = models.CharField(db_column='G45A3', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g45a4 = models.CharField(db_column='G45A4', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g45a5 = models.CharField(db_column='G45A5', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g45a6 = models.CharField(db_column='G45A6', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g45a7 = models.CharField(db_column='G45A7', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g45a8 = models.CharField(db_column='G45A8', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g53_ztk = models.CharField(db_column='G53_ZTK', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g53_dt = models.CharField(db_column='G53_DT', max_length=250, blank=True, null=True)  # Field name made lowercase.
    g53_dn = models.CharField(db_column='G53_DN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g53_dd = models.DateTimeField(db_column='G53_DD', blank=True, null=True)  # Field name made lowercase.
    g53_pos = models.CharField(db_column='G53_POS', max_length=9, blank=True, null=True)  # Field name made lowercase.
    g53_cc = models.CharField(db_column='G53_CC', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g53_cn = models.CharField(db_column='G53_CN', max_length=40, blank=True, null=True)  # Field name made lowercase.
    g53_sub = models.CharField(db_column='G53_SUB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g53_cit = models.CharField(db_column='G53_CIT', max_length=35, blank=True, null=True)  # Field name made lowercase.
    g53_str = models.CharField(db_column='G53_STR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    d54_itn = models.CharField(db_column='D54_ITN', max_length=13, blank=True, null=True)  # Field name made lowercase.
    d5410 = models.CharField(db_column='D5410', max_length=1, blank=True, null=True)  # Field name made lowercase.
    d541 = models.CharField(db_column='D541', max_length=14, blank=True, null=True)  # Field name made lowercase.
    d541d = models.DateTimeField(db_column='D541D', blank=True, null=True)  # Field name made lowercase.
    d5411 = models.CharField(db_column='D5411', max_length=50, blank=True, null=True)  # Field name made lowercase.
    d5411d = models.DateTimeField(db_column='D5411D', blank=True, null=True)  # Field name made lowercase.
    d541_inn = models.CharField(db_column='D541_INN', max_length=12, blank=True, null=True)  # Field name made lowercase.
    d541_kpp = models.CharField(db_column='D541_KPP', max_length=9, blank=True, null=True)  # Field name made lowercase.
    d542 = models.DateTimeField(db_column='D542', blank=True, null=True)  # Field name made lowercase.
    d5441 = models.CharField(db_column='D5441', max_length=150, blank=True, null=True)  # Field name made lowercase.
    d5441nm = models.CharField(db_column='D5441NM', max_length=150, blank=True, null=True)  # Field name made lowercase.
    d5441mdnm = models.CharField(db_column='D5441MDNM', max_length=150, blank=True, null=True)  # Field name made lowercase.
    d5442 = models.CharField(db_column='D5442', max_length=50, blank=True, null=True)  # Field name made lowercase.
    d5443 = models.CharField(db_column='D5443', max_length=250, blank=True, null=True)  # Field name made lowercase.
    d5444 = models.CharField(db_column='D5444', max_length=50, blank=True, null=True)  # Field name made lowercase.
    d5445 = models.DateTimeField(db_column='D5445', blank=True, null=True)  # Field name made lowercase.
    d5446 = models.DateTimeField(db_column='D5446', blank=True, null=True)  # Field name made lowercase.
    d5447 = models.CharField(db_column='D5447', max_length=50, blank=True, null=True)  # Field name made lowercase.
    d5451 = models.CharField(db_column='D5451', max_length=2, blank=True, null=True)  # Field name made lowercase.
    d5451a = models.CharField(db_column='D5451A', max_length=15, blank=True, null=True)  # Field name made lowercase.
    d54521 = models.CharField(db_column='D54521', max_length=11, blank=True, null=True)  # Field name made lowercase.
    d54522 = models.CharField(db_column='D54522', max_length=25, blank=True, null=True)  # Field name made lowercase.
    d54523 = models.CharField(db_column='D54523', max_length=150, blank=True, null=True)  # Field name made lowercase.
    d5453 = models.DateTimeField(db_column='D5453', blank=True, null=True)  # Field name made lowercase.
    g54_itn = models.CharField(db_column='G54_ITN', max_length=13, blank=True, null=True)  # Field name made lowercase.
    g5410 = models.CharField(db_column='G5410', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g541 = models.CharField(db_column='G541', max_length=14, blank=True, null=True)  # Field name made lowercase.
    g541d = models.DateTimeField(db_column='G541D', blank=True, null=True)  # Field name made lowercase.
    g5411 = models.CharField(db_column='G5411', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g5411d = models.DateTimeField(db_column='G5411D', blank=True, null=True)  # Field name made lowercase.
    g541_inn = models.CharField(db_column='G541_INN', max_length=12, blank=True, null=True)  # Field name made lowercase.
    g541_kpp = models.CharField(db_column='G541_KPP', max_length=9, blank=True, null=True)  # Field name made lowercase.
    g542 = models.DateTimeField(db_column='G542', blank=True, null=True)  # Field name made lowercase.
    g5441 = models.CharField(db_column='G5441', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g5441nm = models.CharField(db_column='G5441NM', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g5441mdnm = models.CharField(db_column='G5441MDNM', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g5442 = models.CharField(db_column='G5442', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g5443 = models.CharField(db_column='G5443', max_length=250, blank=True, null=True)  # Field name made lowercase.
    g5444 = models.CharField(db_column='G5444', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g5445 = models.DateTimeField(db_column='G5445', blank=True, null=True)  # Field name made lowercase.
    g5446 = models.DateTimeField(db_column='G5446', blank=True, null=True)  # Field name made lowercase.
    g5447 = models.CharField(db_column='G5447', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g5451 = models.CharField(db_column='G5451', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g5451a = models.CharField(db_column='G5451A', max_length=15, blank=True, null=True)  # Field name made lowercase.
    g54521 = models.CharField(db_column='G54521', max_length=11, blank=True, null=True)  # Field name made lowercase.
    g54522 = models.CharField(db_column='G54522', max_length=25, blank=True, null=True)  # Field name made lowercase.
    g54523 = models.CharField(db_column='G54523', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g5453 = models.DateTimeField(db_column='G5453', blank=True, null=True)  # Field name made lowercase.
    gd0 = models.CharField(db_column='GD0', max_length=2, blank=True, null=True)  # Field name made lowercase.
    gd1 = models.DateTimeField(db_column='GD1', blank=True, null=True)  # Field name made lowercase.
    gd11 = models.CharField(db_column='GD11', max_length=8, blank=True, null=True)  # Field name made lowercase.
    gd2 = models.CharField(db_column='GD2', max_length=4, blank=True, null=True)  # Field name made lowercase.
    gd2fio = models.CharField(db_column='GD2FIO', max_length=150, blank=True, null=True)  # Field name made lowercase.
    gd00 = models.CharField(db_column='GD00', max_length=250, blank=True, null=True)  # Field name made lowercase.
    gddf = models.DateTimeField(db_column='GDDF', blank=True, null=True)  # Field name made lowercase.
    recplatv = models.IntegerField(db_column='RECPLATV', blank=True, null=True)  # Field name made lowercase.
    recslotm = models.IntegerField(db_column='RECSLOTM', blank=True, null=True)  # Field name made lowercase.
    rectrans = models.IntegerField(db_column='RECTRANS', blank=True, null=True)  # Field name made lowercase.
    recsumpp = models.IntegerField(db_column='RECSUMPP', blank=True, null=True)  # Field name made lowercase.
    recpasp = models.IntegerField(db_column='RECPASP', blank=True, null=True)  # Field name made lowercase.
    dmodify = models.DateTimeField(db_column='DMODIFY', blank=True, null=True)  # Field name made lowercase.
    tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    edoc_guid = models.CharField(db_column='EDOC_GUID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    edoc_id = models.DecimalField(default=0.00, db_column='EDOC_ID', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    p_status1 = models.SmallIntegerField(db_column='P_STATUS1', blank=True, null=True)  # Field name made lowercase.
    p_status2 = models.SmallIntegerField(db_column='P_STATUS2', blank=True, null=True)  # Field name made lowercase.
    docid = models.CharField(db_column='DOCID', max_length=38, blank=True, null=True)  # Field name made lowercase.
    num_pp = models.SmallIntegerField(db_column='NUM_PP', blank=True, null=True)  # Field name made lowercase.
    g541dn = models.CharField(db_column='G541DN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g54place = models.CharField(db_column='G54PLACE', max_length=35, blank=True, null=True)  # Field name made lowercase.
    g50rw = models.CharField(db_column='G50RW', max_length=5, blank=True, null=True)  # Field name made lowercase.
    drv41 = models.CharField(db_column='DRV41', max_length=150, blank=True, null=True)  # Field name made lowercase.
    drv41nm = models.CharField(db_column='DRV41NM', max_length=150, blank=True, null=True)  # Field name made lowercase.
    drv41mdnm = models.CharField(db_column='DRV41MDNM', max_length=150, blank=True, null=True)  # Field name made lowercase.
    drv47 = models.CharField(db_column='DRV47', max_length=50, blank=True, null=True)  # Field name made lowercase.
    drv4cc = models.CharField(db_column='DRV4CC', max_length=2, blank=True, null=True)  # Field name made lowercase.
    drv51 = models.CharField(db_column='DRV51', max_length=7, blank=True, null=True)  # Field name made lowercase.
    drv51a = models.CharField(db_column='DRV51A', max_length=15, blank=True, null=True)  # Field name made lowercase.
    drv521 = models.CharField(db_column='DRV521', max_length=11, blank=True, null=True)  # Field name made lowercase.
    drv522 = models.CharField(db_column='DRV522', max_length=25, blank=True, null=True)  # Field name made lowercase.
    drv523 = models.CharField(db_column='DRV523', max_length=150, blank=True, null=True)  # Field name made lowercase.
    drv53 = models.DateTimeField(db_column='DRV53', blank=True, null=True)  # Field name made lowercase.
    act_tp = models.CharField(db_column='ACT_TP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.
    g023build = models.CharField(db_column='G023BUILD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g023abuild = models.CharField(db_column='G023ABUILD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g083build = models.CharField(db_column='G083BUILD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g083abuild = models.CharField(db_column='G083ABUILD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g093build = models.CharField(db_column='G093BUILD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g093abuild = models.CharField(db_column='G093ABUILD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g143build = models.CharField(db_column='G143BUILD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    aeorowner = models.CharField(db_column='AEOROWNER', max_length=1, blank=True, null=True)  # Field name made lowercase.
    aeocntry = models.CharField(db_column='AEOCNTRY', max_length=2, blank=True, null=True)  # Field name made lowercase.
    aeonum = models.CharField(db_column='AEONUM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    aeokind = models.CharField(db_column='AEOKIND', max_length=1, blank=True, null=True)  # Field name made lowercase.
    aeoregcod = models.CharField(db_column='AEOREGCOD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    g143abuild = models.CharField(db_column='G143ABUILD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g16a = models.CharField(db_column='G16A', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g30aeoown = models.CharField(db_column='G30AEOOWN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g30aeocntr = models.CharField(db_column='G30AEOCNTR', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g30aeokind = models.CharField(db_column='G30AEOKIND', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g30aeorcod = models.CharField(db_column='G30AEORCOD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    g30d = models.DateTimeField(db_column='G30D', blank=True, null=True)  # Field name made lowercase.
    g30dd = models.DateTimeField(db_column='G30DD', blank=True, null=True)  # Field name made lowercase.
    g30build = models.CharField(db_column='G30BUILD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g542t = models.CharField(db_column='G542T', max_length=8, blank=True, null=True)  # Field name made lowercase.
    drv241 = models.CharField(db_column='DRV241', max_length=150, blank=True, null=True)  # Field name made lowercase.
    drv241nm = models.CharField(db_column='DRV241NM', max_length=150, blank=True, null=True)  # Field name made lowercase.
    drv241mdnm = models.CharField(db_column='DRV241MDNM', max_length=150, blank=True, null=True)  # Field name made lowercase.
    drv247 = models.CharField(db_column='DRV247', max_length=50, blank=True, null=True)  # Field name made lowercase.
    drv24cc = models.CharField(db_column='DRV24CC', max_length=2, blank=True, null=True)  # Field name made lowercase.
    drv251 = models.CharField(db_column='DRV251', max_length=7, blank=True, null=True)  # Field name made lowercase.
    drv251a = models.CharField(db_column='DRV251A', max_length=15, blank=True, null=True)  # Field name made lowercase.
    drv2521 = models.CharField(db_column='DRV2521', max_length=11, blank=True, null=True)  # Field name made lowercase.
    drv2522 = models.CharField(db_column='DRV2522', max_length=25, blank=True, null=True)  # Field name made lowercase.
    drv2523 = models.CharField(db_column='DRV2523', max_length=150, blank=True, null=True)  # Field name made lowercase.
    drv253 = models.DateTimeField(db_column='DRV253', blank=True, null=True)  # Field name made lowercase.
    g12zpk = models.DecimalField(default=0.00, db_column='G12ZPK', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    g22zpk = models.DecimalField(default=0.00, db_column='G22ZPK', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    g542time = models.CharField(db_column='G542TIME', max_length=14, blank=True, null=True)  # Field name made lowercase.
    g02phone = models.CharField(db_column='G02PHONE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g02email = models.CharField(db_column='G02EMAIL', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g08phone = models.CharField(db_column='G08PHONE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g08email = models.CharField(db_column='G08EMAIL', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g09phone = models.CharField(db_column='G09PHONE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g09email = models.CharField(db_column='G09EMAIL', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g14phone = models.CharField(db_column='G14PHONE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g14email = models.CharField(db_column='G14EMAIL', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g54532 = models.DateTimeField(db_column='G54532', blank=True, null=True)  # Field name made lowercase.
    g54email = models.CharField(db_column='G54EMAIL', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g0132 = models.CharField(db_column='G0132', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g023room = models.CharField(db_column='G023ROOM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    g023typ = models.CharField(db_column='G023TYP', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g023aroom = models.CharField(db_column='G023AROOM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    g023atyp = models.CharField(db_column='G023ATYP', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g083room = models.CharField(db_column='G083ROOM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    g083typ = models.CharField(db_column='G083TYP', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g083aroom = models.CharField(db_column='G083AROOM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    g083atyp = models.CharField(db_column='G083ATYP', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g093room = models.CharField(db_column='G093ROOM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    g093typ = models.CharField(db_column='G093TYP', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g093aroom = models.CharField(db_column='G093AROOM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    g093atyp = models.CharField(db_column='G093ATYP', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g143room = models.CharField(db_column='G143ROOM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    g143typ = models.CharField(db_column='G143TYP', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g143aroom = models.CharField(db_column='G143AROOM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    g143atyp = models.CharField(db_column='G143ATYP', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g30room = models.CharField(db_column='G30ROOM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    g30typ = models.CharField(db_column='G30TYP', max_length=1, blank=True, null=True)  # Field name made lowercase.
    gd1kdt = models.DateTimeField(db_column='GD1KDT', blank=True, null=True)  # Field name made lowercase.
    gd11kdt = models.CharField(db_column='GD11KDT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    seal_plm = models.CharField(db_column='SEAL_PLM', max_length=250, blank=True, null=True)  # Field name made lowercase.
    seal_qty = models.SmallIntegerField(db_column='SEAL_QTY', blank=True, null=True)  # Field name made lowercase.
    seal_id = models.CharField(db_column='SEAL_ID', max_length=250, blank=True, null=True)  # Field name made lowercase.
    seal_decr = models.CharField(db_column='SEAL_DECR', max_length=250, blank=True, null=True)  # Field name made lowercase.
    kz_cust = models.CharField(db_column='KZ_CUST', max_length=8, blank=True, null=True)  # Field name made lowercase.
    kz_sec = models.CharField(db_column='KZ_SEC', max_length=6, blank=True, null=True)  # Field name made lowercase.
    kz_wto = models.CharField(db_column='KZ_WTO', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'DBRHEAD'


# class _Dbrhead(BaseModel):
#     num_ver = models.CharField(db_column='NUM_VER', max_length=8, blank=True, null=True)  # Field name made lowercase.
#     data_ver = models.DateTimeField(db_column='DATA_VER', blank=True, null=True)  # Field name made lowercase.
#     typ_dcl = models.CharField(db_column='TYP_DCL', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     gugtk = models.BooleanField(db_column='GUGTK', blank=True, null=True)  # Field name made lowercase.
#     copy = models.BooleanField(db_column='COPY', blank=True, null=True)  # Field name made lowercase.
#     dcopy = models.DateTimeField(db_column='DCOPY', blank=True, null=True)  # Field name made lowercase.
#     q_edit = models.SmallIntegerField(db_column='Q_EDIT', blank=True, null=True)  # Field name made lowercase.
#     d_edit = models.DateTimeField(db_column='D_EDIT', blank=True, null=True)  # Field name made lowercase.
#     sol = models.SmallIntegerField(db_column='SOL', blank=True, null=True)  # Field name made lowercase.
#     max_err = models.SmallIntegerField(db_column='MAX_ERR', blank=True, null=True)  # Field name made lowercase.
#     dd = models.DateTimeField(db_column='DD', blank=True, null=True)  # Field name made lowercase.
#     tm = models.CharField(db_column='TM', max_length=8, blank=True, null=True)  # Field name made lowercase.
#     extrnl = models.CharField(db_column='EXTRNL', max_length=80, blank=True, null=True)  # Field name made lowercase.
#     schet = models.CharField(db_column='SCHET', max_length=160, blank=True, null=True)  # Field name made lowercase.
#     stepctrl = models.CharField(db_column='STEPCTRL', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     typ_dtc = models.CharField(db_column='TYP_DTC', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     vid_ktc = models.CharField(db_column='VID_KTC', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     stat = models.CharField(db_column='STAT', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
#     g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
#     g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
#     ui_b_1 = models.CharField(db_column='UI_B_1', max_length=8, blank=True, null=True)  # Field name made lowercase.
#     ui_b_2 = models.DateTimeField(db_column='UI_B_2', blank=True, null=True)  # Field name made lowercase.
#     ui_b_3 = models.CharField(db_column='UI_B_3', max_length=7, blank=True, null=True)  # Field name made lowercase.
#     sds_srv = models.CharField(db_column='SDS_SRV', max_length=4, blank=True, null=True)  # Field name made lowercase.
#     sds_num = models.DecimalField(default=0.00, db_column='SDS_NUM', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
#     sds_cust = models.CharField(db_column='SDS_CUST', max_length=8, blank=True, null=True)  # Field name made lowercase.
#     f_decl = models.CharField(db_column='F_DECL', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     rccncode = models.CharField(db_column='RCCNCODE', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     dpresent = models.DateTimeField(db_column='DPRESENT', blank=True, null=True)  # Field name made lowercase.
#     tpresent = models.CharField(db_column='TPRESENT', max_length=8, blank=True, null=True)  # Field name made lowercase.
#     complectbl = models.CharField(db_column='COMPLECTBL', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     g011 = models.CharField(db_column='G011', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     g0121 = models.CharField(db_column='G0121', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     g0131 = models.CharField(db_column='G0131', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     k0131 = models.CharField(db_column='K0131', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     g020 = models.CharField(db_column='G020', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     g02_itn = models.CharField(db_column='G02_ITN', max_length=13, blank=True, null=True)  # Field name made lowercase.
#     g021 = models.CharField(db_column='G021', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     g022 = models.CharField(db_column='G022', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     g023post = models.CharField(db_column='G023POST', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     g0231 = models.CharField(db_column='G0231', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     g0231n = models.CharField(db_column='G0231N', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     g023subd = models.CharField(db_column='G023SUBD', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g023city = models.CharField(db_column='G023CITY', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     g023street = models.CharField(db_column='G023STREET', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g024b = models.CharField(db_column='G024B', max_length=5, blank=True, null=True)  # Field name made lowercase.
#     g024n = models.CharField(db_column='G024N', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     g024in = models.CharField(db_column='G024IN', max_length=12, blank=True, null=True)  # Field name made lowercase.
#     g027 = models.CharField(db_column='G027', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     g0281 = models.CharField(db_column='G0281', max_length=7, blank=True, null=True)  # Field name made lowercase.
#     g0281a = models.CharField(db_column='G0281A', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     g02821 = models.CharField(db_column='G02821', max_length=11, blank=True, null=True)  # Field name made lowercase.
#     g02822 = models.CharField(db_column='G02822', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     g02823 = models.CharField(db_column='G02823', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     g0283 = models.DateTimeField(db_column='G0283', blank=True, null=True)  # Field name made lowercase.
#     g022a = models.CharField(db_column='G022A', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     g027a = models.CharField(db_column='G027A', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     g023apost = models.CharField(db_column='G023APOST', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     g0231a = models.CharField(db_column='G0231A', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     g0231an = models.CharField(db_column='G0231AN', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     g023asubd = models.CharField(db_column='G023ASUBD', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g023acity = models.CharField(db_column='G023ACITY', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     g023astree = models.CharField(db_column='G023ASTREE', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g029 = models.CharField(db_column='G029', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     g02sm14 = models.CharField(db_column='G02SM14', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     g032 = models.IntegerField(db_column='G032', blank=True, null=True)  # Field name made lowercase.
#     g040 = models.IntegerField(db_column='G040', blank=True, null=True)  # Field name made lowercase.
#     g04 = models.IntegerField(db_column='G04', blank=True, null=True)  # Field name made lowercase.
#     g05 = models.IntegerField(db_column='G05', blank=True, null=True)  # Field name made lowercase.
#     g06 = models.IntegerField(db_column='G06', blank=True, null=True)  # Field name made lowercase.
#     g07 = models.CharField(db_column='G07', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     g080 = models.CharField(db_column='G080', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     g08_itn = models.CharField(db_column='G08_ITN', max_length=13, blank=True, null=True)  # Field name made lowercase.
#     g081 = models.CharField(db_column='G081', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     g082 = models.CharField(db_column='G082', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     g083post = models.CharField(db_column='G083POST', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     g0831 = models.CharField(db_column='G0831', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     g0831a = models.CharField(db_column='G0831A', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     g083subd = models.CharField(db_column='G083SUBD', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g083city = models.CharField(db_column='G083CITY', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     g083street = models.CharField(db_column='G083STREET', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g084b = models.CharField(db_column='G084B', max_length=5, blank=True, null=True)  # Field name made lowercase.
#     g087 = models.CharField(db_column='G087', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     g0881 = models.CharField(db_column='G0881', max_length=7, blank=True, null=True)  # Field name made lowercase.
#     g0881a = models.CharField(db_column='G0881A', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     g08821 = models.CharField(db_column='G08821', max_length=11, blank=True, null=True)  # Field name made lowercase.
#     g08822 = models.CharField(db_column='G08822', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     g08823 = models.CharField(db_column='G08823', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     g0883 = models.DateTimeField(db_column='G0883', blank=True, null=True)  # Field name made lowercase.
#     g089 = models.CharField(db_column='G089', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     g082a = models.CharField(db_column='G082A', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     g087a = models.CharField(db_column='G087A', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     g083apost = models.CharField(db_column='G083APOST', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     g0831aa = models.CharField(db_column='G0831AA', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     g0831an = models.CharField(db_column='G0831AN', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     g083asubd = models.CharField(db_column='G083ASUBD', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g083acity = models.CharField(db_column='G083ACITY', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     g083astree = models.CharField(db_column='G083ASTREE', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g08sm14 = models.CharField(db_column='G08SM14', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     g090 = models.CharField(db_column='G090', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     g09_itn = models.CharField(db_column='G09_ITN', max_length=13, blank=True, null=True)  # Field name made lowercase.
#     g091 = models.CharField(db_column='G091', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     g092 = models.CharField(db_column='G092', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     g092a = models.CharField(db_column='G092A', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     g093post = models.CharField(db_column='G093POST', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     g0931 = models.CharField(db_column='G0931', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     g0931n = models.CharField(db_column='G0931N', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     g093subd = models.CharField(db_column='G093SUBD', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g093city = models.CharField(db_column='G093CITY', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     g093street = models.CharField(db_column='G093STREET', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g093apost = models.CharField(db_column='G093APOST', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     g0931a = models.CharField(db_column='G0931A', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     g0931an = models.CharField(db_column='G0931AN', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     g093asubd = models.CharField(db_column='G093ASUBD', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g093acity = models.CharField(db_column='G093ACITY', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     g093astree = models.CharField(db_column='G093ASTREE', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g094b = models.CharField(db_column='G094B', max_length=5, blank=True, null=True)  # Field name made lowercase.
#     g097 = models.CharField(db_column='G097', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     g097a = models.CharField(db_column='G097A', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     g0981 = models.CharField(db_column='G0981', max_length=7, blank=True, null=True)  # Field name made lowercase.
#     g0981a = models.CharField(db_column='G0981A', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     g09821 = models.CharField(db_column='G09821', max_length=11, blank=True, null=True)  # Field name made lowercase.
#     g09822 = models.CharField(db_column='G09822', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     g09823 = models.CharField(db_column='G09823', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     g0983 = models.DateTimeField(db_column='G0983', blank=True, null=True)  # Field name made lowercase.
#     g09sm14 = models.CharField(db_column='G09SM14', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     g11 = models.CharField(db_column='G11', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     g12 = models.DecimalField(default=0.00, db_column='G12', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
#     g121 = models.CharField(db_column='G121', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     g122 = models.DecimalField(default=0.00, db_column='G122', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
#     g140 = models.CharField(db_column='G140', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     g14_itn = models.CharField(db_column='G14_ITN', max_length=13, blank=True, null=True)  # Field name made lowercase.
#     g141 = models.CharField(db_column='G141', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     g142 = models.CharField(db_column='G142', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     g142a = models.CharField(db_column='G142A', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     g143post = models.CharField(db_column='G143POST', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     g1431 = models.CharField(db_column='G1431', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     g1431n = models.CharField(db_column='G1431N', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     g143subd = models.CharField(db_column='G143SUBD', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g143city = models.CharField(db_column='G143CITY', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     g143street = models.CharField(db_column='G143STREET', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g143apost = models.CharField(db_column='G143APOST', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     g1431a = models.CharField(db_column='G1431A', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     g1431an = models.CharField(db_column='G1431AN', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     g143asubd = models.CharField(db_column='G143ASUBD', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g143acity = models.CharField(db_column='G143ACITY', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     g143astree = models.CharField(db_column='G143ASTREE', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g144b = models.CharField(db_column='G144B', max_length=5, blank=True, null=True)  # Field name made lowercase.
#     g147 = models.CharField(db_column='G147', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     g147a = models.CharField(db_column='G147A', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     g1481 = models.CharField(db_column='G1481', max_length=7, blank=True, null=True)  # Field name made lowercase.
#     g1481a = models.CharField(db_column='G1481A', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     g14821 = models.CharField(db_column='G14821', max_length=11, blank=True, null=True)  # Field name made lowercase.
#     g14822 = models.CharField(db_column='G14822', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     g14823 = models.CharField(db_column='G14823', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     g1483 = models.DateTimeField(db_column='G1483', blank=True, null=True)  # Field name made lowercase.
#     g15 = models.CharField(db_column='G15', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     g15a = models.CharField(db_column='G15A', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     g16 = models.CharField(db_column='G16', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     g17a = models.CharField(db_column='G17A', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     g17b = models.CharField(db_column='G17B', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     g180 = models.IntegerField(db_column='G180', blank=True, null=True)  # Field name made lowercase.
#     g182 = models.CharField(db_column='G182', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     g19 = models.CharField(db_column='G19', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     g202 = models.CharField(db_column='G202', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     g2021 = models.CharField(db_column='G2021', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     g203 = models.CharField(db_column='G203', max_length=250, blank=True, null=True)  # Field name made lowercase.
#     g210 = models.IntegerField(db_column='G210', blank=True, null=True)  # Field name made lowercase.
#     g212 = models.CharField(db_column='G212', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     g221 = models.CharField(db_column='G221', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     g222 = models.DecimalField(default=0.00, db_column='G222', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
#     g23 = models.FloatField(default=0.00, db_column='G23', blank=True, null=True)  # Field name made lowercase.
#     g230 = models.DateTimeField(db_column='G230', blank=True, null=True)  # Field name made lowercase.
#     g270 = models.CharField(db_column='G270', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     g27_itn = models.CharField(db_column='G27_ITN', max_length=13, blank=True, null=True)  # Field name made lowercase.
#     g2710 = models.CharField(db_column='G2710', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     g271 = models.CharField(db_column='G271', max_length=21, blank=True, null=True)  # Field name made lowercase.
#     g27 = models.CharField(db_column='G27', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     g2711 = models.DateTimeField(db_column='G2711', blank=True, null=True)  # Field name made lowercase.
#     g2712 = models.CharField(db_column='G2712', max_length=8, blank=True, null=True)  # Field name made lowercase.
#     g28_itn = models.CharField(db_column='G28_ITN', max_length=13, blank=True, null=True)  # Field name made lowercase.
#     g28okpo = models.CharField(db_column='G28OKPO', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     g28inn = models.CharField(db_column='G28INN', max_length=12, blank=True, null=True)  # Field name made lowercase.
#     g281oth = models.CharField(db_column='G281OTH', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     g28zajmn = models.CharField(db_column='G28ZAJMN', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g282 = models.CharField(db_column='G282', max_length=70, blank=True, null=True)  # Field name made lowercase.
#     g28211 = models.CharField(db_column='G28211', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     g28212 = models.CharField(db_column='G28212', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     g28221 = models.CharField(db_column='G28221', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     g28222 = models.CharField(db_column='G28222', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     g28230 = models.CharField(db_column='G28230', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     g2823 = models.DateTimeField(db_column='G2823', blank=True, null=True)  # Field name made lowercase.
#     g28240 = models.CharField(db_column='G28240', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     g2824 = models.DateTimeField(db_column='G2824', blank=True, null=True)  # Field name made lowercase.
#     g2825 = models.CharField(db_column='G2825', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     g30_itn = models.CharField(db_column='G30_ITN', max_length=13, blank=True, null=True)  # Field name made lowercase.
#     g300 = models.CharField(db_column='G300', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     g3010 = models.CharField(db_column='G3010', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     g301 = models.CharField(db_column='G301', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g3011 = models.DateTimeField(db_column='G3011', blank=True, null=True)  # Field name made lowercase.
#     g30 = models.CharField(db_column='G30', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g30post = models.CharField(db_column='G30POST', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     g30a = models.CharField(db_column='G30A', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     g30an = models.CharField(db_column='G30AN', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     g30subd = models.CharField(db_column='G30SUBD', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g30city = models.CharField(db_column='G30CITY', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     g30street = models.CharField(db_column='G30STREET', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g30lname = models.CharField(db_column='G30LNAME', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     g3012 = models.CharField(db_column='G3012', max_length=8, blank=True, null=True)  # Field name made lowercase.
#     g30121 = models.CharField(db_column='G30121', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     g30122 = models.CharField(db_column='G30122', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g45a1 = models.CharField(db_column='G45A1', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     g45a2 = models.CharField(db_column='G45A2', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     g45a3 = models.CharField(db_column='G45A3', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     g45a4 = models.CharField(db_column='G45A4', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     g45a5 = models.CharField(db_column='G45A5', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     g45a6 = models.CharField(db_column='G45A6', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     g45a7 = models.CharField(db_column='G45A7', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     g45a8 = models.CharField(db_column='G45A8', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     g53_ztk = models.CharField(db_column='G53_ZTK', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g53_dt = models.CharField(db_column='G53_DT', max_length=250, blank=True, null=True)  # Field name made lowercase.
#     g53_dn = models.CharField(db_column='G53_DN', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g53_dd = models.DateTimeField(db_column='G53_DD', blank=True, null=True)  # Field name made lowercase.
#     g53_pos = models.CharField(db_column='G53_POS', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     g53_cc = models.CharField(db_column='G53_CC', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     g53_cn = models.CharField(db_column='G53_CN', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     g53_sub = models.CharField(db_column='G53_SUB', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g53_cit = models.CharField(db_column='G53_CIT', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     g53_str = models.CharField(db_column='G53_STR', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     d54_itn = models.CharField(db_column='D54_ITN', max_length=13, blank=True, null=True)  # Field name made lowercase.
#     d5410 = models.CharField(db_column='D5410', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     d541 = models.CharField(db_column='D541', max_length=14, blank=True, null=True)  # Field name made lowercase.
#     d541d = models.DateTimeField(db_column='D541D', blank=True, null=True)  # Field name made lowercase.
#     d5411 = models.CharField(db_column='D5411', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     d5411d = models.DateTimeField(db_column='D5411D', blank=True, null=True)  # Field name made lowercase.
#     d541_inn = models.CharField(db_column='D541_INN', max_length=12, blank=True, null=True)  # Field name made lowercase.
#     d541_kpp = models.CharField(db_column='D541_KPP', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     d542 = models.DateTimeField(db_column='D542', blank=True, null=True)  # Field name made lowercase.
#     d5441 = models.CharField(db_column='D5441', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     d5441nm = models.CharField(db_column='D5441NM', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     d5441mdnm = models.CharField(db_column='D5441MDNM', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     d5442 = models.CharField(db_column='D5442', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     d5443 = models.CharField(db_column='D5443', max_length=250, blank=True, null=True)  # Field name made lowercase.
#     d5444 = models.CharField(db_column='D5444', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     d5445 = models.DateTimeField(db_column='D5445', blank=True, null=True)  # Field name made lowercase.
#     d5446 = models.DateTimeField(db_column='D5446', blank=True, null=True)  # Field name made lowercase.
#     d5447 = models.CharField(db_column='D5447', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     d5451 = models.CharField(db_column='D5451', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     d5451a = models.CharField(db_column='D5451A', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     d54521 = models.CharField(db_column='D54521', max_length=11, blank=True, null=True)  # Field name made lowercase.
#     d54522 = models.CharField(db_column='D54522', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     d54523 = models.CharField(db_column='D54523', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     d5453 = models.DateTimeField(db_column='D5453', blank=True, null=True)  # Field name made lowercase.
#     g54_itn = models.CharField(db_column='G54_ITN', max_length=13, blank=True, null=True)  # Field name made lowercase.
#     g5410 = models.CharField(db_column='G5410', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     g541 = models.CharField(db_column='G541', max_length=14, blank=True, null=True)  # Field name made lowercase.
#     g541d = models.DateTimeField(db_column='G541D', blank=True, null=True)  # Field name made lowercase.
#     g5411 = models.CharField(db_column='G5411', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g5411d = models.DateTimeField(db_column='G5411D', blank=True, null=True)  # Field name made lowercase.
#     g541_inn = models.CharField(db_column='G541_INN', max_length=12, blank=True, null=True)  # Field name made lowercase.
#     g541_kpp = models.CharField(db_column='G541_KPP', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     g542 = models.DateTimeField(db_column='G542', blank=True, null=True)  # Field name made lowercase.
#     g5441 = models.CharField(db_column='G5441', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     g5441nm = models.CharField(db_column='G5441NM', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     g5441mdnm = models.CharField(db_column='G5441MDNM', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     g5442 = models.CharField(db_column='G5442', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g5443 = models.CharField(db_column='G5443', max_length=250, blank=True, null=True)  # Field name made lowercase.
#     g5444 = models.CharField(db_column='G5444', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g5445 = models.DateTimeField(db_column='G5445', blank=True, null=True)  # Field name made lowercase.
#     g5446 = models.DateTimeField(db_column='G5446', blank=True, null=True)  # Field name made lowercase.
#     g5447 = models.CharField(db_column='G5447', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g5451 = models.CharField(db_column='G5451', max_length=7, blank=True, null=True)  # Field name made lowercase.
#     g5451a = models.CharField(db_column='G5451A', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     g54521 = models.CharField(db_column='G54521', max_length=11, blank=True, null=True)  # Field name made lowercase.
#     g54522 = models.CharField(db_column='G54522', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     g54523 = models.CharField(db_column='G54523', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     g5453 = models.DateTimeField(db_column='G5453', blank=True, null=True)  # Field name made lowercase.
#     gd0 = models.CharField(db_column='GD0', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     gd1 = models.DateTimeField(db_column='GD1', blank=True, null=True)  # Field name made lowercase.
#     gd11 = models.CharField(db_column='GD11', max_length=8, blank=True, null=True)  # Field name made lowercase.
#     gd2 = models.CharField(db_column='GD2', max_length=4, blank=True, null=True)  # Field name made lowercase.
#     gd2fio = models.CharField(db_column='GD2FIO', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     gd00 = models.CharField(db_column='GD00', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     gddf = models.DateTimeField(db_column='GDDF', blank=True, null=True)  # Field name made lowercase.
#     recplatv = models.IntegerField(db_column='RECPLATV', blank=True, null=True)  # Field name made lowercase.
#     recslotm = models.IntegerField(db_column='RECSLOTM', blank=True, null=True)  # Field name made lowercase.
#     rectrans = models.IntegerField(db_column='RECTRANS', blank=True, null=True)  # Field name made lowercase.
#     recsumpp = models.IntegerField(db_column='RECSUMPP', blank=True, null=True)  # Field name made lowercase.
#     recpasp = models.IntegerField(db_column='RECPASP', blank=True, null=True)  # Field name made lowercase.
#     dmodify = models.DateTimeField(db_column='DMODIFY', blank=True, null=True)  # Field name made lowercase.
#     tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
#     edoc_guid = models.CharField(db_column='EDOC_GUID', max_length=32, blank=True, null=True)  # Field name made lowercase.
#     edoc_id = models.DecimalField(default=0.00, db_column='EDOC_ID', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     p_status1 = models.SmallIntegerField(db_column='P_STATUS1', blank=True, null=True)  # Field name made lowercase.
#     p_status2 = models.SmallIntegerField(db_column='P_STATUS2', blank=True, null=True)  # Field name made lowercase.
#     docid = models.CharField(db_column='DOCID', max_length=38, blank=True, null=True)  # Field name made lowercase.
#     num_pp = models.SmallIntegerField(db_column='NUM_PP', blank=True, null=True)  # Field name made lowercase.
#     g541dn = models.CharField(db_column='G541DN', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g54place = models.CharField(db_column='G54PLACE', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     g50rw = models.CharField(db_column='G50RW', max_length=5, blank=True, null=True)  # Field name made lowercase.
#     drv41 = models.CharField(db_column='DRV41', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     drv41nm = models.CharField(db_column='DRV41NM', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     drv41mdnm = models.CharField(db_column='DRV41MDNM', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     drv47 = models.CharField(db_column='DRV47', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     drv4cc = models.CharField(db_column='DRV4CC', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     drv51 = models.CharField(db_column='DRV51', max_length=7, blank=True, null=True)  # Field name made lowercase.
#     drv51a = models.CharField(db_column='DRV51A', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     drv521 = models.CharField(db_column='DRV521', max_length=11, blank=True, null=True)  # Field name made lowercase.
#     drv522 = models.CharField(db_column='DRV522', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     drv523 = models.CharField(db_column='DRV523', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     drv53 = models.DateTimeField(db_column='DRV53', blank=True, null=True)  # Field name made lowercase.
#     act_tp = models.CharField(db_column='ACT_TP', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     g023build = models.CharField(db_column='G023BUILD', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g023abuild = models.CharField(db_column='G023ABUILD', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g083build = models.CharField(db_column='G083BUILD', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g083abuild = models.CharField(db_column='G083ABUILD', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g093build = models.CharField(db_column='G093BUILD', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g093abuild = models.CharField(db_column='G093ABUILD', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g143build = models.CharField(db_column='G143BUILD', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aeorowner = models.CharField(db_column='AEOROWNER', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     aeocntry = models.CharField(db_column='AEOCNTRY', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     aeonum = models.CharField(db_column='AEONUM', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aeokind = models.CharField(db_column='AEOKIND', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     aeoregcod = models.CharField(db_column='AEOREGCOD', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     g143abuild = models.CharField(db_column='G143ABUILD', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g16a = models.CharField(db_column='G16A', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     g30aeoown = models.CharField(db_column='G30AEOOWN', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     g30aeocntr = models.CharField(db_column='G30AEOCNTR', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     g30aeokind = models.CharField(db_column='G30AEOKIND', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     g30aeorcod = models.CharField(db_column='G30AEORCOD', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     g30d = models.DateTimeField(db_column='G30D', blank=True, null=True)  # Field name made lowercase.
#     g30dd = models.DateTimeField(db_column='G30DD', blank=True, null=True)  # Field name made lowercase.
#     g30build = models.CharField(db_column='G30BUILD', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g542t = models.CharField(db_column='G542T', max_length=8, blank=True, null=True)  # Field name made lowercase.
#     drv241 = models.CharField(db_column='DRV241', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     drv241nm = models.CharField(db_column='DRV241NM', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     drv241mdnm = models.CharField(db_column='DRV241MDNM', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     drv247 = models.CharField(db_column='DRV247', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     drv24cc = models.CharField(db_column='DRV24CC', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     drv251 = models.CharField(db_column='DRV251', max_length=7, blank=True, null=True)  # Field name made lowercase.
#     drv251a = models.CharField(db_column='DRV251A', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     drv2521 = models.CharField(db_column='DRV2521', max_length=11, blank=True, null=True)  # Field name made lowercase.
#     drv2522 = models.CharField(db_column='DRV2522', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     drv2523 = models.CharField(db_column='DRV2523', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     drv253 = models.DateTimeField(db_column='DRV253', blank=True, null=True)  # Field name made lowercase.
#     g12zpk = models.DecimalField(default=0.00, db_column='G12ZPK', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
#     g22zpk = models.DecimalField(default=0.00, db_column='G22ZPK', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
#     g542time = models.CharField(db_column='G542TIME', max_length=14, blank=True, null=True)  # Field name made lowercase.
#     g02phone = models.CharField(db_column='G02PHONE', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g02email = models.CharField(db_column='G02EMAIL', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     g08phone = models.CharField(db_column='G08PHONE', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g08email = models.CharField(db_column='G08EMAIL', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     g09phone = models.CharField(db_column='G09PHONE', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g09email = models.CharField(db_column='G09EMAIL', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     g14phone = models.CharField(db_column='G14PHONE', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g14email = models.CharField(db_column='G14EMAIL', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     g54532 = models.DateTimeField(db_column='G54532', blank=True, null=True)  # Field name made lowercase.
#     g54email = models.CharField(db_column='G54EMAIL', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     g0132 = models.CharField(db_column='G0132', max_length=2, blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         abstract = True
#         # db_table = 'DBRHEAD'


class Dbrkmp(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g32 = models.IntegerField(db_column='G32', blank=True, null=True)  # Field name made lowercase.
    kmpfb = models.IntegerField(db_column='KMPFB', blank=True, null=True)  # Field name made lowercase.
    kmpnm = models.CharField(db_column='KMPNM', max_length=250, blank=True, null=True)  # Field name made lowercase.
    kmpkod = models.CharField(db_column='KMPKOD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    kmpadd = models.CharField(db_column='KMPADD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    kmpqadd = models.DecimalField(default=0.00, db_column='KMPQADD', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    kmpqmain = models.DecimalField(default=0.00, db_column='KMPQMAIN', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    kmppr = models.DecimalField(default=0.00, db_column='KMPPR', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    kmpprval = models.CharField(db_column='KMPPRVAL', max_length=3, blank=True, null=True)  # Field name made lowercase.
    kmpqk = models.IntegerField(db_column='KMPQK', blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'DBRKMP'


class Dbrkmpk(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g32 = models.IntegerField(db_column='G32', blank=True, null=True)  # Field name made lowercase.
    kmpfb = models.IntegerField(db_column='KMPFB', blank=True, null=True)  # Field name made lowercase.
    kmpk = models.IntegerField(db_column='KMPK', blank=True, null=True)  # Field name made lowercase.
    kmpkid = models.DecimalField(default=0.00, db_column='KMPKID', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    kmpknum = models.CharField(db_column='KMPKNUM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kmpnm = models.CharField(db_column='KMPNM', max_length=250, blank=True, null=True)  # Field name made lowercase.
    kmpkod = models.CharField(db_column='KMPKOD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    kmpadd = models.CharField(db_column='KMPADD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    kmpqadd = models.DecimalField(default=0.00, db_column='KMPQADD', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    kmpqmain = models.DecimalField(default=0.00, db_column='KMPQMAIN', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    kmppr = models.DecimalField(default=0.00, db_column='KMPPR', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    kmpprval = models.CharField(db_column='KMPPRVAL', max_length=3, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'DBRKMPK'


class Dbrpasp(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g2810 = models.CharField(db_column='G2810', max_length=1, blank=True, null=True)  # Field name made lowercase.
    pasp = models.CharField(db_column='PASP', max_length=25, blank=True, null=True)  # Field name made lowercase.
    paspdd = models.DateTimeField(db_column='PASPDD', blank=True, null=True)  # Field name made lowercase.
    pasp0 = models.CharField(db_column='PASP0', max_length=1, blank=True, null=True)  # Field name made lowercase.
    pasp1 = models.CharField(db_column='PASP1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    pasp1dd = models.DateTimeField(db_column='PASP1DD', blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'DBRPASP'


class Dbrpk(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g32 = models.IntegerField(db_column='G32', blank=True, null=True)  # Field name made lowercase.
    pksign = models.CharField(db_column='PKSIGN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    pkvid = models.CharField(db_column='PKVID', max_length=2, blank=True, null=True)  # Field name made lowercase.
    pkkolvo = models.IntegerField(db_column='PKKOLVO', blank=True, null=True)  # Field name made lowercase.
    pkinf = models.CharField(db_column='PKINF', max_length=150, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'DBRPK'


class Dbrplatr(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g32 = models.IntegerField(db_column='G32', blank=True, null=True)  # Field name made lowercase.
    g470 = models.CharField(db_column='G470', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g471 = models.CharField(db_column='G471', max_length=4, blank=True, null=True)  # Field name made lowercase.
    g471npp = models.SmallIntegerField(db_column='G471NPP', blank=True, null=True)  # Field name made lowercase.
    g472 = models.DecimalField(default=0.00, db_column='G472', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    g4721 = models.CharField(db_column='G4721', max_length=3, blank=True, null=True)  # Field name made lowercase.
    g473 = models.FloatField(default=0.00, db_column='G473', blank=True, null=True)  # Field name made lowercase.
    g4731 = models.CharField(db_column='G4731', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g4732 = models.CharField(db_column='G4732', max_length=3, blank=True, null=True)  # Field name made lowercase.
    g4733 = models.CharField(db_column='G4733', max_length=3, blank=True, null=True)  # Field name made lowercase.
    g4734 = models.FloatField(default=0.00, db_column='G4734', blank=True, null=True)  # Field name made lowercase.
    npp = models.SmallIntegerField(db_column='NPP', blank=True, null=True)  # Field name made lowercase.
    g474 = models.DecimalField(default=0.00, db_column='G474', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    g4741 = models.CharField(db_column='G4741', max_length=3, blank=True, null=True)  # Field name made lowercase.
    g475 = models.CharField(db_column='G475', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g473z1_2 = models.CharField(db_column='G473Z1_2', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g473_2 = models.FloatField(default=0.00, db_column='G473_2', blank=True, null=True)  # Field name made lowercase.
    g4731_2 = models.CharField(db_column='G4731_2', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g4732_2 = models.CharField(db_column='G4732_2', max_length=3, blank=True, null=True)  # Field name made lowercase.
    g4733_2 = models.CharField(db_column='G4733_2', max_length=3, blank=True, null=True)  # Field name made lowercase.
    g4734_2 = models.FloatField(default=0.00, db_column='G4734_2', blank=True, null=True)  # Field name made lowercase.
    g473z1_3 = models.CharField(db_column='G473Z1_3', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g473_3 = models.FloatField(default=0.00, db_column='G473_3', blank=True, null=True)  # Field name made lowercase.
    g4731_3 = models.CharField(db_column='G4731_3', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g4732_3 = models.CharField(db_column='G4732_3', max_length=3, blank=True, null=True)  # Field name made lowercase.
    g4733_3 = models.CharField(db_column='G4733_3', max_length=3, blank=True, null=True)  # Field name made lowercase.
    g4734_3 = models.FloatField(default=0.00, db_column='G4734_3', blank=True, null=True)  # Field name made lowercase.
    g473z2_2 = models.SmallIntegerField(db_column='G473Z2_2', blank=True, null=True)  # Field name made lowercase.
    g4730 = models.DateTimeField(db_column='G4730', blank=True, null=True)  # Field name made lowercase.
    g4740 = models.DateTimeField(db_column='G4740', blank=True, null=True)  # Field name made lowercase.
    g47_nd = models.SmallIntegerField(db_column='G47_ND', blank=True, null=True)  # Field name made lowercase.
    g47_ns = models.SmallIntegerField(db_column='G47_NS', blank=True, null=True)  # Field name made lowercase.
    g47_nm = models.SmallIntegerField(db_column='G47_NM', blank=True, null=True)  # Field name made lowercase.
    g47_tr = models.FloatField(default=0.00, db_column='G47_TR', blank=True, null=True)  # Field name made lowercase.
    g47_g40 = models.IntegerField(db_column='G47_G40', blank=True, null=True)  # Field name made lowercase.
    nzp = models.DecimalField(default=0.00, db_column='NZP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dmodify = models.DateTimeField(db_column='DMODIFY', blank=True, null=True)  # Field name made lowercase.
    tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    p_edoc_id = models.DecimalField(default=0.00, db_column='P_EDOC_ID', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    g476 = models.DecimalField(default=0.00, db_column='G476', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    g4761 = models.CharField(db_column='G4761', max_length=3, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.
    g4723 = models.CharField(db_column='G4723', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'DBRPLATR'


class Dbrplatv(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    gb0 = models.CharField(db_column='GB0', max_length=1, blank=True, null=True)  # Field name made lowercase.
    gb1 = models.CharField(db_column='GB1', max_length=4, blank=True, null=True)  # Field name made lowercase.
    gb2 = models.DecimalField(default=0.00, db_column='GB2', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    gb3 = models.CharField(db_column='GB3', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gb4 = models.FloatField(default=0.00, db_column='GB4', blank=True, null=True)  # Field name made lowercase.
    gb5 = models.CharField(db_column='GB5', max_length=2, blank=True, null=True)  # Field name made lowercase.
    iret = models.SmallIntegerField(db_column='IRET', blank=True, null=True)  # Field name made lowercase.
    g48 = models.DateTimeField(db_column='G48', blank=True, null=True)  # Field name made lowercase.
    g481 = models.CharField(db_column='G481', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g482 = models.CharField(db_column='G482', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g482d = models.DateTimeField(db_column='G482D', blank=True, null=True)  # Field name made lowercase.
    nzp = models.DecimalField(default=0.00, db_column='NZP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dmodify = models.DateTimeField(db_column='DMODIFY', blank=True, null=True)  # Field name made lowercase.
    tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    p_edoc_id = models.DecimalField(default=0.00, db_column='P_EDOC_ID', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    gb6 = models.DecimalField(default=0.00, db_column='GB6', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    gb61 = models.CharField(db_column='GB61', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gb7 = models.DecimalField(default=0.00, db_column='GB7', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.
    g48doccode = models.CharField(db_column='G48DOCCODE', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'DBRPLATV'


class Dbrpredd(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g32 = models.IntegerField(db_column='G32', blank=True, null=True)  # Field name made lowercase.
    numrec = models.IntegerField(db_column='NUMREC', blank=True, null=True)  # Field name made lowercase.
    g40_cntry = models.CharField(db_column='G40_CNTRY', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g40_0 = models.CharField(db_column='G40_0', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g40_naim = models.CharField(db_column='G40_NAIM', max_length=250, blank=True, null=True)  # Field name made lowercase.
    g40_1 = models.CharField(db_column='G40_1', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g40_2 = models.DateTimeField(db_column='G40_2', blank=True, null=True)  # Field name made lowercase.
    g40_21 = models.CharField(db_column='G40_21', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g40_3 = models.CharField(db_column='G40_3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g40_4 = models.IntegerField(db_column='G40_4', blank=True, null=True)  # Field name made lowercase.
    g40_doctyp = models.CharField(db_column='G40_DOCTYP', max_length=5, blank=True, null=True)  # Field name made lowercase.
    nzp = models.DecimalField(default=0.00, db_column='NZP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dmodify = models.DateTimeField(db_column='DMODIFY', blank=True, null=True)  # Field name made lowercase.
    tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    p_edoc_id = models.DecimalField(default=0.00, db_column='P_EDOC_ID', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.
    g33 = models.CharField(db_column='G33', max_length=10, blank=True, null=True)  # Field name made lowercase.
    prevnumtyp = models.CharField(db_column='PREVNUMTYP', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g40_31 = models.CharField(db_column='G40_31', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'DBRPREDD'


class Dbrsumpp(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    gb1 = models.CharField(db_column='GB1', max_length=4, blank=True, null=True)  # Field name made lowercase.
    gb3 = models.CharField(db_column='GB3', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gb5 = models.CharField(db_column='GB5', max_length=2, blank=True, null=True)  # Field name made lowercase.
    iret = models.SmallIntegerField(db_column='IRET', blank=True, null=True)  # Field name made lowercase.
    numpdok = models.CharField(db_column='NUMPDOK', max_length=50, blank=True, null=True)  # Field name made lowercase.
    datpdok = models.DateTimeField(db_column='DATPDOK', blank=True, null=True)  # Field name made lowercase.
    sum_all = models.DecimalField(default=0.00, db_column='SUM_ALL', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sumpdok = models.DecimalField(default=0.00, db_column='SUMPDOK', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valpdok = models.CharField(db_column='VALPDOK', max_length=3, blank=True, null=True)  # Field name made lowercase.
    datpostd = models.DateTimeField(db_column='DATPOSTD', blank=True, null=True)  # Field name made lowercase.
    datpaymt = models.DateTimeField(db_column='DATPAYMT', blank=True, null=True)  # Field name made lowercase.
    innplat = models.CharField(db_column='INNPLAT', max_length=30, blank=True, null=True)  # Field name made lowercase.
    kppplat = models.CharField(db_column='KPPPLAT', max_length=9, blank=True, null=True)  # Field name made lowercase.
    lnpins = models.CharField(db_column='LNPINS', max_length=4, blank=True, null=True)  # Field name made lowercase.
    fioins = models.CharField(db_column='FIOINS', max_length=40, blank=True, null=True)  # Field name made lowercase.
    datins = models.DateTimeField(db_column='DATINS', blank=True, null=True)  # Field name made lowercase.
    timins = models.CharField(db_column='TIMINS', max_length=8, blank=True, null=True)  # Field name made lowercase.
    nzp = models.DecimalField(default=0.00, db_column='NZP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dmodify = models.DateTimeField(db_column='DMODIFY', blank=True, null=True)  # Field name made lowercase.
    tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    p_edoc_id = models.DecimalField(default=0.00, db_column='P_EDOC_ID', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'DBRSUMPP'


class Dbrtechd(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g32 = models.IntegerField(db_column='G32', blank=True, null=True)  # Field name made lowercase.
    g4401 = models.SmallIntegerField(db_column='G4401', blank=True, null=True)  # Field name made lowercase.
    g4402 = models.SmallIntegerField(db_column='G4402', blank=True, null=True)  # Field name made lowercase.
    g4403 = models.CharField(db_column='G4403', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g44020 = models.CharField(db_column='G44020', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g44_cust = models.CharField(db_column='G44_CUST', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g440 = models.CharField(db_column='G440', max_length=4, blank=True, null=True)  # Field name made lowercase.
    g441 = models.CharField(db_column='G441', max_length=5, blank=True, null=True)  # Field name made lowercase.
    g441a = models.CharField(db_column='G441A', max_length=2, blank=True, null=True)  # Field name made lowercase.
    id_bdrd = models.CharField(db_column='ID_BDRD', max_length=32, blank=True, null=True)  # Field name made lowercase.
    prsbdrd = models.CharField(db_column='PRSBDRD', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g442 = models.CharField(db_column='G442', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g442lic1 = models.SmallIntegerField(db_column='G442LIC1', blank=True, null=True)  # Field name made lowercase.
    g442lic2 = models.IntegerField(db_column='G442LIC2', blank=True, null=True)  # Field name made lowercase.
    g442r = models.CharField(db_column='G442R', max_length=28, blank=True, null=True)  # Field name made lowercase.
    g442simp = models.CharField(db_column='G442SIMP', max_length=10, blank=True, null=True)  # Field name made lowercase.
    g44mdp1 = models.IntegerField(db_column='G44MDP1', blank=True, null=True)  # Field name made lowercase.
    g44mdp2 = models.CharField(db_column='G44MDP2', max_length=18, blank=True, null=True)  # Field name made lowercase.
    g443 = models.DateTimeField(db_column='G443', blank=True, null=True)  # Field name made lowercase.
    g444 = models.CharField(db_column='G444', max_length=250, blank=True, null=True)  # Field name made lowercase.
    g445 = models.CharField(db_column='G445', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g446 = models.DateTimeField(db_column='G446', blank=True, null=True)  # Field name made lowercase.
    g447 = models.DateTimeField(db_column='G447', blank=True, null=True)  # Field name made lowercase.
    g4480et = models.CharField(db_column='G4480ET', max_length=10, blank=True, null=True)  # Field name made lowercase.
    g4481et = models.DateTimeField(db_column='G4481ET', blank=True, null=True)  # Field name made lowercase.
    g44stper = models.DecimalField(default=0.00, db_column='G44STPER', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    g44sfcntry = models.CharField(db_column='G44SFCNTRY', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g44alldoc = models.SmallIntegerField(db_column='G44ALLDOC', blank=True, null=True)  # Field name made lowercase.
    g4491 = models.DateTimeField(db_column='G4491', blank=True, null=True)  # Field name made lowercase.
    g4492 = models.DateTimeField(db_column='G4492', blank=True, null=True)  # Field name made lowercase.
    g4493 = models.CharField(db_column='G4493', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g44dd = models.DateTimeField(db_column='G44DD', blank=True, null=True)  # Field name made lowercase.
    nzp = models.DecimalField(default=0.00, db_column='NZP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dmodify = models.DateTimeField(db_column='DMODIFY', blank=True, null=True)  # Field name made lowercase.
    tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    ed_id = models.CharField(db_column='ED_ID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.
    prevnumtyp = models.CharField(db_column='PREVNUMTYP', max_length=1, blank=True, null=True)  # Field name made lowercase.
    prevnumdoc = models.CharField(db_column='PREVNUMDOC', max_length=50, blank=True, null=True)  # Field name made lowercase.
    recordid = models.CharField(db_column='RECORDID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    executbody = models.CharField(db_column='EXECUTBODY', max_length=10, blank=True, null=True)  # Field name made lowercase.
    execname = models.CharField(db_column='EXECNAME', max_length=250, blank=True, null=True)  # Field name made lowercase.
    ineturl = models.CharField(db_column='INETURL', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'DBRTECHD'


class Dbrterms(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g32 = models.IntegerField(db_column='G32', blank=True, null=True)  # Field name made lowercase.
    terms = models.CharField(db_column='TERMS', max_length=3, blank=True, null=True)  # Field name made lowercase.
    termspoint = models.CharField(db_column='TERMSPOINT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    termspass = models.CharField(db_column='TERMSPASS', max_length=250, blank=True, null=True)  # Field name made lowercase.
    nzp = models.DecimalField(default=0.00, db_column='NZP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dmodify = models.DateTimeField(db_column='DMODIFY', blank=True, null=True)  # Field name made lowercase.
    tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    p_edoc_id = models.DecimalField(default=0.00, db_column='P_EDOC_ID', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'DBRTERMS'


class Dbrtov2(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    type_info = models.CharField(db_column='TYPE_INFO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g031 = models.IntegerField(db_column='G031', blank=True, null=True)  # Field name made lowercase.
    g31_1 = models.CharField(db_column='G31_1', max_length=250, blank=True, null=True)  # Field name made lowercase.
    g31_7 = models.DecimalField(default=0.00, db_column='G31_7', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    g31_71 = models.CharField(db_column='G31_71', max_length=13, blank=True, null=True)  # Field name made lowercase.
    g31_8 = models.DecimalField(default=0.00, db_column='G31_8', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    g31_81 = models.CharField(db_column='G31_81', max_length=13, blank=True, null=True)  # Field name made lowercase.
    g31_82 = models.CharField(db_column='G31_82', max_length=3, blank=True, null=True)  # Field name made lowercase.
    g31_9 = models.DecimalField(default=0.00, db_column='G31_9', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    g31_91 = models.CharField(db_column='G31_91', max_length=13, blank=True, null=True)  # Field name made lowercase.
    g31_92 = models.CharField(db_column='G31_92', max_length=3, blank=True, null=True)  # Field name made lowercase.
    g31_d1 = models.DateTimeField(db_column='G31_D1', blank=True, null=True)  # Field name made lowercase.
    g31_d2 = models.DateTimeField(db_column='G31_D2', blank=True, null=True)  # Field name made lowercase.
    g32 = models.IntegerField(db_column='G32', blank=True, null=True)  # Field name made lowercase.
    numpredd = models.IntegerField(db_column='NUMPREDD', blank=True, null=True)  # Field name made lowercase.
    g33 = models.CharField(db_column='G33', max_length=10, blank=True, null=True)  # Field name made lowercase.
    g330 = models.CharField(db_column='G330', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g331 = models.CharField(db_column='G331', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g332 = models.CharField(db_column='G332', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g333 = models.CharField(db_column='G333', max_length=4, blank=True, null=True)  # Field name made lowercase.
    g340 = models.CharField(db_column='G340', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g34 = models.CharField(db_column='G34', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g35 = models.DecimalField(default=0.00, db_column='G35', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    g36 = models.CharField(db_column='G36', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g37 = models.CharField(db_column='G37', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g38 = models.DecimalField(default=0.00, db_column='G38', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    g38_1 = models.DecimalField(default=0.00, db_column='G38_1', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    g40_g38 = models.DecimalField(default=0.00, db_column='G40_G38', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    g40_g31_7 = models.DecimalField(default=0.00, db_column='G40_G31_7', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    numrec = models.IntegerField(db_column='NUMREC', blank=True, null=True)  # Field name made lowercase.
    g40_0 = models.CharField(db_column='G40_0', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g40_1 = models.CharField(db_column='G40_1', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g40_2 = models.DateTimeField(db_column='G40_2', blank=True, null=True)  # Field name made lowercase.
    g40_21 = models.CharField(db_column='G40_21', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g40_3 = models.CharField(db_column='G40_3', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g40_4 = models.IntegerField(db_column='G40_4', blank=True, null=True)  # Field name made lowercase.
    g41a = models.CharField(db_column='G41A', max_length=3, blank=True, null=True)  # Field name made lowercase.
    g40_naim = models.CharField(db_column='G40_NAIM', max_length=30, blank=True, null=True)  # Field name made lowercase.
    g42 = models.DecimalField(default=0.00, db_column='G42', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    g45 = models.DecimalField(default=0.00, db_column='G45', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    g451 = models.CharField(db_column='G451', max_length=2, blank=True, null=True)  # Field name made lowercase.
    nzp = models.DecimalField(default=0.00, db_column='NZP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dmodify = models.DateTimeField(db_column='DMODIFY', blank=True, null=True)  # Field name made lowercase.
    tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    p_edoc_id = models.DecimalField(default=0.00, db_column='P_EDOC_ID', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'DBRTOV2'


class Dbrtovar(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g02_itn = models.CharField(db_column='G02_ITN', max_length=13, blank=True, null=True)  # Field name made lowercase.
    g021 = models.CharField(db_column='G021', max_length=40, blank=True, null=True)  # Field name made lowercase.
    g022 = models.CharField(db_column='G022', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g023post = models.CharField(db_column='G023POST', max_length=9, blank=True, null=True)  # Field name made lowercase.
    g0231 = models.CharField(db_column='G0231', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g0231n = models.CharField(db_column='G0231N', max_length=40, blank=True, null=True)  # Field name made lowercase.
    g023subd = models.CharField(db_column='G023SUBD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g023city = models.CharField(db_column='G023CITY', max_length=35, blank=True, null=True)  # Field name made lowercase.
    g023street = models.CharField(db_column='G023STREET', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g024b = models.CharField(db_column='G024B', max_length=5, blank=True, null=True)  # Field name made lowercase.
    g024n = models.CharField(db_column='G024N', max_length=10, blank=True, null=True)  # Field name made lowercase.
    g024in = models.CharField(db_column='G024IN', max_length=12, blank=True, null=True)  # Field name made lowercase.
    g027 = models.CharField(db_column='G027', max_length=9, blank=True, null=True)  # Field name made lowercase.
    g0281 = models.CharField(db_column='G0281', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g0281a = models.CharField(db_column='G0281A', max_length=15, blank=True, null=True)  # Field name made lowercase.
    g02821 = models.CharField(db_column='G02821', max_length=11, blank=True, null=True)  # Field name made lowercase.
    g02822 = models.CharField(db_column='G02822', max_length=25, blank=True, null=True)  # Field name made lowercase.
    g02823 = models.CharField(db_column='G02823', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g0283 = models.DateTimeField(db_column='G0283', blank=True, null=True)  # Field name made lowercase.
    g022a = models.CharField(db_column='G022A', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g027a = models.CharField(db_column='G027A', max_length=9, blank=True, null=True)  # Field name made lowercase.
    g023apost = models.CharField(db_column='G023APOST', max_length=9, blank=True, null=True)  # Field name made lowercase.
    g0231a = models.CharField(db_column='G0231A', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g0231an = models.CharField(db_column='G0231AN', max_length=40, blank=True, null=True)  # Field name made lowercase.
    g023asubd = models.CharField(db_column='G023ASUBD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g023acity = models.CharField(db_column='G023ACITY', max_length=35, blank=True, null=True)  # Field name made lowercase.
    g023astree = models.CharField(db_column='G023ASTREE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g031 = models.IntegerField(db_column='G031', blank=True, null=True)  # Field name made lowercase.
    g31_1 = models.CharField(db_column='G31_1', max_length=250, blank=True, null=True)  # Field name made lowercase.
    g31_13 = models.CharField(db_column='G31_13', max_length=40, blank=True, null=True)  # Field name made lowercase.
    g31_1_prdt = models.DateTimeField(db_column='G31_1_PRDT', blank=True, null=True)  # Field name made lowercase.
    g31_1_oilf = models.CharField(db_column='G31_1_OILF', max_length=250, blank=True, null=True)  # Field name made lowercase.
    g31_2 = models.IntegerField(db_column='G31_2', blank=True, null=True)  # Field name made lowercase.
    g31_2part = models.IntegerField(db_column='G31_2PART', blank=True, null=True)  # Field name made lowercase.
    g31_20 = models.CharField(db_column='G31_20', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g31_3 = models.IntegerField(db_column='G31_3', blank=True, null=True)  # Field name made lowercase.
    g31_7 = models.DecimalField(default=0.00, db_column='G31_7', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    g31_71 = models.CharField(db_column='G31_71', max_length=30, blank=True, null=True)  # Field name made lowercase.
    g31_8 = models.DecimalField(default=0.00, db_column='G31_8', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    g31_81 = models.CharField(db_column='G31_81', max_length=30, blank=True, null=True)  # Field name made lowercase.
    g31_82 = models.CharField(db_column='G31_82', max_length=4, blank=True, null=True)  # Field name made lowercase.
    g31_9 = models.DecimalField(default=0.00, db_column='G31_9', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    g31_91 = models.CharField(db_column='G31_91', max_length=30, blank=True, null=True)  # Field name made lowercase.
    g31_92 = models.CharField(db_column='G31_92', max_length=4, blank=True, null=True)  # Field name made lowercase.
    g31_10 = models.IntegerField(db_column='G31_10', blank=True, null=True)  # Field name made lowercase.
    g31_101 = models.CharField(db_column='G31_101', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g31_d1 = models.DateTimeField(db_column='G31_D1', blank=True, null=True)  # Field name made lowercase.
    g31_d2 = models.DateTimeField(db_column='G31_D2', blank=True, null=True)  # Field name made lowercase.
    g31_p1 = models.CharField(db_column='G31_P1', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g31_p2 = models.CharField(db_column='G31_P2', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g31_fact = models.DecimalField(default=0.00, db_column='G31_FACT', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    g31_fc_1 = models.CharField(db_column='G31_FC_1', max_length=3, blank=True, null=True)  # Field name made lowercase.
    g32 = models.IntegerField(db_column='G32', blank=True, null=True)  # Field name made lowercase.
    g32kdt = models.IntegerField(db_column='G32KDT', blank=True, null=True)  # Field name made lowercase.
    g32_1 = models.CharField(db_column='G32_1', max_length=3, blank=True, null=True)  # Field name made lowercase.
    g33 = models.CharField(db_column='G33', max_length=10, blank=True, null=True)  # Field name made lowercase.
    g330 = models.CharField(db_column='G330', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g331 = models.CharField(db_column='G331', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g332 = models.CharField(db_column='G332', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g333 = models.CharField(db_column='G333', max_length=4, blank=True, null=True)  # Field name made lowercase.
    g334 = models.CharField(db_column='G334', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g340 = models.CharField(db_column='G340', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g34 = models.CharField(db_column='G34', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g35 = models.DecimalField(default=0.00, db_column='G35', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    g36 = models.CharField(db_column='G36', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g37 = models.CharField(db_column='G37', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g38 = models.DecimalField(default=0.00, db_column='G38', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    g38_1 = models.DecimalField(default=0.00, db_column='G38_1', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    g39 = models.DecimalField(default=0.00, db_column='G39', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    g3911 = models.CharField(db_column='G3911', max_length=3, blank=True, null=True)  # Field name made lowercase.
    g3912 = models.CharField(db_column='G3912', max_length=3, blank=True, null=True)  # Field name made lowercase.
    g392 = models.CharField(db_column='G392', max_length=70, blank=True, null=True)  # Field name made lowercase.
    g41a = models.CharField(db_column='G41A', max_length=4, blank=True, null=True)  # Field name made lowercase.
    g42 = models.DecimalField(default=0.00, db_column='G42', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    g43 = models.CharField(db_column='G43', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g430 = models.CharField(db_column='G430', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g45 = models.DecimalField(default=0.00, db_column='G45', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    g451 = models.CharField(db_column='G451', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g452 = models.DecimalField(default=0.00, db_column='G452', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    g45a1 = models.CharField(db_column='G45A1', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g45a2 = models.CharField(db_column='G45A2', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g45a3 = models.CharField(db_column='G45A3', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g45a4 = models.CharField(db_column='G45A4', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g45a5 = models.CharField(db_column='G45A5', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g45a6 = models.CharField(db_column='G45A6', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g45a7 = models.CharField(db_column='G45A7', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g45a8 = models.CharField(db_column='G45A8', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g46 = models.DecimalField(default=0.00, db_column='G46', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    g461 = models.CharField(db_column='G461', max_length=1, blank=True, null=True)  # Field name made lowercase.
    nblank = models.CharField(db_column='NBLANK', max_length=10, blank=True, null=True)  # Field name made lowercase.
    fksign = models.CharField(db_column='FKSIGN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    gd0 = models.CharField(db_column='GD0', max_length=2, blank=True, null=True)  # Field name made lowercase.
    gd1 = models.DateTimeField(db_column='GD1', blank=True, null=True)  # Field name made lowercase.
    gd11 = models.CharField(db_column='GD11', max_length=8, blank=True, null=True)  # Field name made lowercase.
    gd2 = models.CharField(db_column='GD2', max_length=4, blank=True, null=True)  # Field name made lowercase.
    gd00 = models.CharField(db_column='GD00', max_length=150, blank=True, null=True)  # Field name made lowercase.
    kod_str = models.CharField(db_column='KOD_STR', max_length=2, blank=True, null=True)  # Field name made lowercase.
    dstat = models.DateTimeField(db_column='DSTAT', blank=True, null=True)  # Field name made lowercase.
    stat = models.CharField(db_column='STAT', max_length=1, blank=True, null=True)  # Field name made lowercase.
    recplatr = models.IntegerField(db_column='RECPLATR', blank=True, null=True)  # Field name made lowercase.
    rectechd = models.IntegerField(db_column='RECTECHD', blank=True, null=True)  # Field name made lowercase.
    recpredd = models.IntegerField(db_column='RECPREDD', blank=True, null=True)  # Field name made lowercase.
    recavtmb = models.IntegerField(db_column='RECAVTMB', blank=True, null=True)  # Field name made lowercase.
    rectovg = models.IntegerField(db_column='RECTOVG', blank=True, null=True)  # Field name made lowercase.
    recpk = models.IntegerField(db_column='RECPK', blank=True, null=True)  # Field name made lowercase.
    recamnum = models.IntegerField(db_column='RECAMNUM', blank=True, null=True)  # Field name made lowercase.
    recterms = models.IntegerField(db_column='RECTERMS', blank=True, null=True)  # Field name made lowercase.
    recdog = models.IntegerField(db_column='RECDOG', blank=True, null=True)  # Field name made lowercase.
    recdoga = models.IntegerField(db_column='RECDOGA', blank=True, null=True)  # Field name made lowercase.
    recdogt = models.IntegerField(db_column='RECDOGT', blank=True, null=True)  # Field name made lowercase.
    reckmp = models.IntegerField(db_column='RECKMP', blank=True, null=True)  # Field name made lowercase.
    recuslt = models.IntegerField(db_column='RECUSLT', blank=True, null=True)  # Field name made lowercase.
    recsltov = models.IntegerField(db_column='RECSLTOV', blank=True, null=True)  # Field name made lowercase.
    rectov2 = models.IntegerField(db_column='RECTOV2', blank=True, null=True)  # Field name made lowercase.
    recplat2 = models.IntegerField(db_column='RECPLAT2', blank=True, null=True)  # Field name made lowercase.
    recdinf2 = models.IntegerField(db_column='RECDINF2', blank=True, null=True)  # Field name made lowercase.
    rectovg2 = models.IntegerField(db_column='RECTOVG2', blank=True, null=True)  # Field name made lowercase.
    recvrsk = models.IntegerField(db_column='RECVRSK', blank=True, null=True)  # Field name made lowercase.
    nzp = models.DecimalField(default=0.00, db_column='NZP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dmodify = models.DateTimeField(db_column='DMODIFY', blank=True, null=True)  # Field name made lowercase.
    tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    p_edoc_id = models.DecimalField(default=0.00, db_column='P_EDOC_ID', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    g020 = models.CharField(db_column='G020', max_length=15, blank=True, null=True)  # Field name made lowercase.
    g42c = models.CharField(db_column='G42C', max_length=3, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.
    g023build = models.CharField(db_column='G023BUILD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g35zpk = models.DecimalField(default=0.00, db_column='G35ZPK', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    g38zpk = models.DecimalField(default=0.00, db_column='G38ZPK', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    g42curr = models.CharField(db_column='G42CURR', max_length=3, blank=True, null=True)  # Field name made lowercase.
    g42rate = models.FloatField(default=0.00, db_column='G42RATE', blank=True, null=True)  # Field name made lowercase.
    g46zpk = models.DecimalField(default=0.00, db_column='G46ZPK', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    g31_dti = models.DecimalField(default=0.00, db_column='G31_DTI', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    g34_2c = models.CharField(db_column='G34_2C', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g34_2n = models.CharField(db_column='G34_2N', max_length=40, blank=True, null=True)  # Field name made lowercase.
    g31_trc = models.DecimalField(default=0.00, db_column='G31_TRC', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    g31_trc1 = models.CharField(db_column='G31_TRC1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    g31_trc2 = models.CharField(db_column='G31_TRC2', max_length=4, blank=True, null=True)  # Field name made lowercase.
    g335 = models.CharField(db_column='G335', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g462 = models.DecimalField(default=0.00, db_column='G462', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    g462curr = models.CharField(db_column='G462CURR', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'DBRTOVAR'


class Dbrtovg(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g32 = models.IntegerField(db_column='G32', blank=True, null=True)  # Field name made lowercase.
    g32g = models.SmallIntegerField(db_column='G32G', blank=True, null=True)  # Field name made lowercase.
    numrec = models.SmallIntegerField(db_column='NUMREC', blank=True, null=True)  # Field name made lowercase.
    g31_10 = models.CharField(db_column='G31_10', max_length=4, blank=True, null=True)  # Field name made lowercase.
    g31_11 = models.CharField(db_column='G31_11', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g31_12 = models.CharField(db_column='G31_12', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g31_14 = models.CharField(db_column='G31_14', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g31_15_mod = models.CharField(db_column='G31_15_MOD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g31_15 = models.CharField(db_column='G31_15', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g31_16 = models.CharField(db_column='G31_16', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g31_17 = models.CharField(db_column='G31_17', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g31_18 = models.CharField(db_column='G31_18', max_length=30, blank=True, null=True)  # Field name made lowercase.
    g31_19 = models.CharField(db_column='G31_19', max_length=20, blank=True, null=True)  # Field name made lowercase.
    g31_20 = models.CharField(db_column='G31_20', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kolvo = models.DecimalField(default=0.00, db_column='KOLVO', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    code_edi = models.CharField(db_column='CODE_EDI', max_length=3, blank=True, null=True)  # Field name made lowercase.
    name_edi = models.CharField(db_column='NAME_EDI', max_length=13, blank=True, null=True)  # Field name made lowercase.
    rois_num = models.CharField(db_column='ROIS_NUM', max_length=250, blank=True, null=True)  # Field name made lowercase.
    rois_cc = models.CharField(db_column='ROIS_CC', max_length=2, blank=True, null=True)  # Field name made lowercase.
    nzp = models.DecimalField(default=0.00, db_column='NZP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dmodify = models.DateTimeField(db_column='DMODIFY', blank=True, null=True)  # Field name made lowercase.
    tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    p_edoc_id = models.DecimalField(default=0.00, db_column='P_EDOC_ID', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.
    g31place = models.CharField(db_column='G31PLACE', max_length=250, blank=True, null=True)  # Field name made lowercase.
    length = models.DecimalField(default=0.00, db_column='LENGTH', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    width = models.DecimalField(default=0.00, db_column='WIDTH', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    height = models.DecimalField(default=0.00, db_column='HEIGHT', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    recordid = models.CharField(db_column='RECORDID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    invoiccost = models.DecimalField(default=0.00, db_column='INVOICCOST', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    licgrpdoc1 = models.CharField(db_column='LICGRPDOC1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    licgrpd1 = models.DateTimeField(db_column='LICGRPD1', blank=True, null=True)  # Field name made lowercase.
    licrec1 = models.CharField(db_column='LICREC1', max_length=36, blank=True, null=True)  # Field name made lowercase.
    goodnmlic1 = models.IntegerField(db_column='GOODNMLIC1', blank=True, null=True)  # Field name made lowercase.
    licgrpdoc2 = models.CharField(db_column='LICGRPDOC2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    licgrpd2 = models.DateTimeField(db_column='LICGRPD2', blank=True, null=True)  # Field name made lowercase.
    licrec2 = models.CharField(db_column='LICREC2', max_length=36, blank=True, null=True)  # Field name made lowercase.
    goodnmlic2 = models.IntegerField(db_column='GOODNMLIC2', blank=True, null=True)  # Field name made lowercase.
    compord = models.SmallIntegerField(db_column='COMPORD', blank=True, null=True)  # Field name made lowercase.
    compnum = models.CharField(db_column='COMPNUM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g31_inn = models.CharField(db_column='G31_INN', max_length=12, blank=True, null=True)  # Field name made lowercase.
    g31_okato = models.CharField(db_column='G31_OKATO', max_length=11, blank=True, null=True)  # Field name made lowercase.
    g31_kpp = models.CharField(db_column='G31_KPP', max_length=9, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'DBRTOVG'


class Dbrtovg2(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g32 = models.IntegerField(db_column='G32', blank=True, null=True)  # Field name made lowercase.
    type_info = models.CharField(db_column='TYPE_INFO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    numpredd = models.IntegerField(db_column='NUMPREDD', blank=True, null=True)  # Field name made lowercase.
    g32g = models.SmallIntegerField(db_column='G32G', blank=True, null=True)  # Field name made lowercase.
    numrec = models.SmallIntegerField(db_column='NUMREC', blank=True, null=True)  # Field name made lowercase.
    g31_10 = models.CharField(db_column='G31_10', max_length=4, blank=True, null=True)  # Field name made lowercase.
    g31_11 = models.CharField(db_column='G31_11', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g31_12 = models.CharField(db_column='G31_12', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g31_14 = models.CharField(db_column='G31_14', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g31_15_mod = models.CharField(db_column='G31_15_MOD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g31_15 = models.CharField(db_column='G31_15', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g31_16 = models.CharField(db_column='G31_16', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g31_17 = models.CharField(db_column='G31_17', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g31_18 = models.CharField(db_column='G31_18', max_length=30, blank=True, null=True)  # Field name made lowercase.
    g31_19 = models.CharField(db_column='G31_19', max_length=20, blank=True, null=True)  # Field name made lowercase.
    g31_20 = models.CharField(db_column='G31_20', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kolvo = models.DecimalField(default=0.00, db_column='KOLVO', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    code_edi = models.CharField(db_column='CODE_EDI', max_length=3, blank=True, null=True)  # Field name made lowercase.
    name_edi = models.CharField(db_column='NAME_EDI', max_length=13, blank=True, null=True)  # Field name made lowercase.
    nzp = models.DecimalField(default=0.00, db_column='NZP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dmodify = models.DateTimeField(db_column='DMODIFY', blank=True, null=True)  # Field name made lowercase.
    tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    p_edoc_id = models.DecimalField(default=0.00, db_column='P_EDOC_ID', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'DBRTOVG2'


class Dbrtovs(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g32 = models.IntegerField(db_column='G32', blank=True, null=True)  # Field name made lowercase.
    g32g = models.SmallIntegerField(db_column='G32G', blank=True, null=True)  # Field name made lowercase.
    numrec = models.IntegerField(db_column='NUMREC', blank=True, null=True)  # Field name made lowercase.
    g31_15_sn = models.CharField(db_column='G31_15_SN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nzp = models.DecimalField(default=0.00, db_column='NZP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dmodify = models.DateTimeField(db_column='DMODIFY', blank=True, null=True)  # Field name made lowercase.
    tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    p_edoc_id = models.DecimalField(default=0.00, db_column='P_EDOC_ID', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'DBRTOVS'


class Dbrtovs2(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g32 = models.IntegerField(db_column='G32', blank=True, null=True)  # Field name made lowercase.
    type_info = models.CharField(db_column='TYPE_INFO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    numpredd = models.IntegerField(db_column='NUMPREDD', blank=True, null=True)  # Field name made lowercase.
    g32g = models.SmallIntegerField(db_column='G32G', blank=True, null=True)  # Field name made lowercase.
    numrec = models.SmallIntegerField(db_column='NUMREC', blank=True, null=True)  # Field name made lowercase.
    g31_15_sn = models.CharField(db_column='G31_15_SN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nzp = models.DecimalField(default=0.00, db_column='NZP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dmodify = models.DateTimeField(db_column='DMODIFY', blank=True, null=True)  # Field name made lowercase.
    tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    p_edoc_id = models.DecimalField(default=0.00, db_column='P_EDOC_ID', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'DBRTOVS2'


class Dbrtrans(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    ngr = models.CharField(db_column='NGR', max_length=2, blank=True, null=True)  # Field name made lowercase.
    numrec = models.IntegerField(db_column='NUMREC', blank=True, null=True)  # Field name made lowercase.
    vidtrans = models.CharField(db_column='VIDTRANS', max_length=2, blank=True, null=True)  # Field name made lowercase.
    mthtrans = models.CharField(db_column='MTHTRANS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    nametrans = models.CharField(db_column='NAMETRANS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ntrans = models.CharField(db_column='NTRANS', max_length=40, blank=True, null=True)  # Field name made lowercase.
    movetrans = models.CharField(db_column='MOVETRANS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ntrans1 = models.CharField(db_column='NTRANS1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ntrans2 = models.CharField(db_column='NTRANS2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    activeid = models.CharField(db_column='ACTIVEID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    g19 = models.CharField(db_column='G19', max_length=1, blank=True, null=True)  # Field name made lowercase.
    st_control = models.CharField(db_column='ST_CONTROL', max_length=250, blank=True, null=True)  # Field name made lowercase.
    g212 = models.CharField(db_column='G212', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g29 = models.CharField(db_column='G29', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g291 = models.CharField(db_column='G291', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gc5 = models.DateTimeField(db_column='GC5', blank=True, null=True)  # Field name made lowercase.
    gc51 = models.CharField(db_column='GC51', max_length=8, blank=True, null=True)  # Field name made lowercase.
    nzp = models.DecimalField(default=0.00, db_column='NZP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dmodify = models.DateTimeField(db_column='DMODIFY', blank=True, null=True)  # Field name made lowercase.
    tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    p_edoc_id = models.DecimalField(default=0.00, db_column='P_EDOC_ID', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.
    tipts3 = models.CharField(db_column='TIPTS3', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'DBRTRANS'


class Dbruslt(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g32 = models.IntegerField(db_column='G32', blank=True, null=True)  # Field name made lowercase.
    typeinfo = models.CharField(db_column='TYPEINFO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    gu01 = models.SmallIntegerField(db_column='GU01', blank=True, null=True)  # Field name made lowercase.
    gu02 = models.SmallIntegerField(db_column='GU02', blank=True, null=True)  # Field name made lowercase.
    gu03 = models.CharField(db_column='GU03', max_length=2, blank=True, null=True)  # Field name made lowercase.
    gunpp = models.IntegerField(db_column='GUNPP', blank=True, null=True)  # Field name made lowercase.
    gu1 = models.CharField(db_column='GU1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gu1d = models.DateTimeField(db_column='GU1D', blank=True, null=True)  # Field name made lowercase.
    gu2 = models.CharField(db_column='GU2', max_length=250, blank=True, null=True)  # Field name made lowercase.
    gu3 = models.DateTimeField(db_column='GU3', blank=True, null=True)  # Field name made lowercase.
    gudd = models.DateTimeField(db_column='GUDD', blank=True, null=True)  # Field name made lowercase.
    nzp = models.DecimalField(default=0.00, db_column='NZP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dmodify = models.DateTimeField(db_column='DMODIFY', blank=True, null=True)  # Field name made lowercase.
    tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    p_edoc_id = models.DecimalField(default=0.00, db_column='P_EDOC_ID', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'DBRUSLT'


class Dcllistd(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    tlist = models.SmallIntegerField(db_column='TLIST', blank=True, null=True)  # Field name made lowercase.
    lrazdel = models.SmallIntegerField(db_column='LRAZDEL', blank=True, null=True)  # Field name made lowercase.
    lrec = models.IntegerField(db_column='LREC', blank=True, null=True)  # Field name made lowercase.
    quer = models.SmallIntegerField(db_column='QUER', blank=True, null=True)  # Field name made lowercase.
    querd = models.DateTimeField(db_column='QUERD', blank=True, null=True)  # Field name made lowercase.
    g441 = models.CharField(db_column='G441', max_length=5, blank=True, null=True)  # Field name made lowercase.
    g444 = models.CharField(db_column='G444', max_length=250, blank=True, null=True)  # Field name made lowercase.
    g442 = models.CharField(db_column='G442', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g443 = models.DateTimeField(db_column='G443', blank=True, null=True)  # Field name made lowercase.
    lstatdoc = models.CharField(db_column='LSTATDOC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    llist = models.IntegerField(db_column='LLIST', blank=True, null=True)  # Field name made lowercase.
    lkol = models.SmallIntegerField(db_column='LKOL', blank=True, null=True)  # Field name made lowercase.
    l071 = models.CharField(db_column='L071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    l072 = models.DateTimeField(db_column='L072', blank=True, null=True)  # Field name made lowercase.
    l073 = models.CharField(db_column='L073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    lprim = models.CharField(db_column='LPRIM', max_length=128, blank=True, null=True)  # Field name made lowercase.
    nzp = models.DecimalField(default=0.00, db_column='NZP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dmodify = models.DateTimeField(db_column='DMODIFY', blank=True, null=True)  # Field name made lowercase.
    tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    p_edoc_id = models.DecimalField(default=0.00, db_column='P_EDOC_ID', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    filename = models.CharField(db_column='FILENAME', max_length=250, blank=True, null=True)  # Field name made lowercase.
    lineid = models.CharField(db_column='LINEID', max_length=38, blank=True, null=True)  # Field name made lowercase.
    sernum = models.CharField(db_column='SERNUM', max_length=3, blank=True, null=True)  # Field name made lowercase.
    sersign = models.CharField(db_column='SERSIGN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'DCLLISTD'


class Dcllisth(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    hlist = models.SmallIntegerField(db_column='HLIST', blank=True, null=True)  # Field name made lowercase.
    g141 = models.CharField(db_column='G141', max_length=12, blank=True, null=True)  # Field name made lowercase.
    g142 = models.CharField(db_column='G142', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g142a = models.CharField(db_column='G142A', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g147 = models.CharField(db_column='G147', max_length=9, blank=True, null=True)  # Field name made lowercase.
    g541 = models.CharField(db_column='G541', max_length=14, blank=True, null=True)  # Field name made lowercase.
    g541d = models.DateTimeField(db_column='G541D', blank=True, null=True)  # Field name made lowercase.
    tpriem = models.CharField(db_column='TPRIEM', max_length=8, blank=True, null=True)  # Field name made lowercase.
    dbegctrl = models.DateTimeField(db_column='DBEGCTRL', blank=True, null=True)  # Field name made lowercase.
    tbegctrl = models.CharField(db_column='TBEGCTRL', max_length=8, blank=True, null=True)  # Field name made lowercase.
    lnpbegctrl = models.CharField(db_column='LNPBEGCTRL', max_length=4, blank=True, null=True)  # Field name made lowercase.
    gd0 = models.CharField(db_column='GD0', max_length=2, blank=True, null=True)  # Field name made lowercase.
    gd1 = models.DateTimeField(db_column='GD1', blank=True, null=True)  # Field name made lowercase.
    gd11 = models.CharField(db_column='GD11', max_length=8, blank=True, null=True)  # Field name made lowercase.
    gd00 = models.CharField(db_column='GD00', max_length=128, blank=True, null=True)  # Field name made lowercase.
    dmodify = models.DateTimeField(db_column='DMODIFY', blank=True, null=True)  # Field name made lowercase.
    tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    p_edoc_id = models.DecimalField(default=0.00, db_column='P_EDOC_ID', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    g140 = models.CharField(db_column='G140', max_length=15, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'DCLLISTH'


class Dcllistl(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    tlist = models.SmallIntegerField(db_column='TLIST', blank=True, null=True)  # Field name made lowercase.
    dlist = models.DateTimeField(db_column='DLIST', blank=True, null=True)  # Field name made lowercase.
    lnplist = models.CharField(db_column='LNPLIST', max_length=4, blank=True, null=True)  # Field name made lowercase.
    l41 = models.CharField(db_column='L41', max_length=150, blank=True, null=True)  # Field name made lowercase.
    l41nm = models.CharField(db_column='L41NM', max_length=150, blank=True, null=True)  # Field name made lowercase.
    l41mdnm = models.CharField(db_column='L41MDNM', max_length=150, blank=True, null=True)  # Field name made lowercase.
    l43 = models.CharField(db_column='L43', max_length=250, blank=True, null=True)  # Field name made lowercase.
    l44 = models.CharField(db_column='L44', max_length=50, blank=True, null=True)  # Field name made lowercase.
    l45 = models.DateTimeField(db_column='L45', blank=True, null=True)  # Field name made lowercase.
    l51 = models.CharField(db_column='L51', max_length=7, blank=True, null=True)  # Field name made lowercase.
    l51a = models.CharField(db_column='L51A', max_length=15, blank=True, null=True)  # Field name made lowercase.
    l521 = models.CharField(db_column='L521', max_length=11, blank=True, null=True)  # Field name made lowercase.
    l52 = models.CharField(db_column='L52', max_length=25, blank=True, null=True)  # Field name made lowercase.
    l523 = models.CharField(db_column='L523', max_length=150, blank=True, null=True)  # Field name made lowercase.
    l53 = models.DateTimeField(db_column='L53', blank=True, null=True)  # Field name made lowercase.
    nzp = models.DecimalField(default=0.00, db_column='NZP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dmodify = models.DateTimeField(db_column='DMODIFY', blank=True, null=True)  # Field name made lowercase.
    tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    p_edoc_id = models.DecimalField(default=0.00, db_column='P_EDOC_ID', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    l42 = models.CharField(db_column='L42', max_length=50, blank=True, null=True)  # Field name made lowercase.
    l46 = models.DateTimeField(db_column='L46', blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'DCLLISTL'


class Dclquerd(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    quer = models.SmallIntegerField(db_column='QUER', blank=True, null=True)  # Field name made lowercase.
    querd = models.DateTimeField(db_column='QUERD', blank=True, null=True)  # Field name made lowercase.
    qrec = models.IntegerField(db_column='QREC', blank=True, null=True)  # Field name made lowercase.
    g441 = models.CharField(db_column='G441', max_length=4, blank=True, null=True)  # Field name made lowercase.
    g444 = models.CharField(db_column='G444', max_length=250, blank=True, null=True)  # Field name made lowercase.
    qpurpose = models.CharField(db_column='QPURPOSE', max_length=128, blank=True, null=True)  # Field name made lowercase.
    qprim = models.CharField(db_column='QPRIM', max_length=128, blank=True, null=True)  # Field name made lowercase.
    qtam = models.CharField(db_column='QTAM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    nzp = models.DecimalField(default=0.00, db_column='NZP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dmodify = models.DateTimeField(db_column='DMODIFY', blank=True, null=True)  # Field name made lowercase.
    tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    p_edoc_id = models.DecimalField(default=0.00, db_column='P_EDOC_ID', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'DCLQUERD'


class Dclquerh(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    quer = models.SmallIntegerField(db_column='QUER', blank=True, null=True)  # Field name made lowercase.
    querd = models.DateTimeField(db_column='QUERD', blank=True, null=True)  # Field name made lowercase.
    qktam = models.CharField(db_column='QKTAM', max_length=8, blank=True, null=True)  # Field name made lowercase.
    qdocd = models.DateTimeField(db_column='QDOCD', blank=True, null=True)  # Field name made lowercase.
    qlnp = models.CharField(db_column='QLNP', max_length=4, blank=True, null=True)  # Field name made lowercase.
    qcomm = models.CharField(db_column='QCOMM', max_length=1, blank=True, null=True)  # Field name made lowercase.
    qsend = models.CharField(db_column='QSEND', max_length=50, blank=True, null=True)  # Field name made lowercase.
    qsendpost = models.CharField(db_column='QSENDPOST', max_length=9, blank=True, null=True)  # Field name made lowercase.
    qsendcount = models.CharField(db_column='QSENDCOUNT', max_length=2, blank=True, null=True)  # Field name made lowercase.
    qsendsubd = models.CharField(db_column='QSENDSUBD', max_length=35, blank=True, null=True)  # Field name made lowercase.
    qsendcity = models.CharField(db_column='QSENDCITY', max_length=35, blank=True, null=True)  # Field name made lowercase.
    qsendstree = models.CharField(db_column='QSENDSTREE', max_length=35, blank=True, null=True)  # Field name made lowercase.
    qsendd = models.DateTimeField(db_column='QSENDD', blank=True, null=True)  # Field name made lowercase.
    qsendtam = models.CharField(db_column='QSENDTAM', max_length=40, blank=True, null=True)  # Field name made lowercase.
    qrecv = models.CharField(db_column='QRECV', max_length=40, blank=True, null=True)  # Field name made lowercase.
    qrecvd = models.DateTimeField(db_column='QRECVD', blank=True, null=True)  # Field name made lowercase.
    nzp = models.DecimalField(default=0.00, db_column='NZP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dmodify = models.DateTimeField(db_column='DMODIFY', blank=True, null=True)  # Field name made lowercase.
    tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    p_edoc_id = models.DecimalField(default=0.00, db_column='P_EDOC_ID', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'DCLQUERH'


class Docsfiles(BaseModel):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=255)  # Field name made lowercase.
    filename = models.CharField(db_column='FileName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    blob = models.BinaryField(db_column='Blob', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'DocsFiles'


class Kbravtmb(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    k32 = models.IntegerField(db_column='K32', blank=True, null=True)  # Field name made lowercase.
    nud = models.CharField(db_column='NUD', max_length=12, blank=True, null=True)  # Field name made lowercase.
    kodmrk = models.CharField(db_column='KODMRK', max_length=3, blank=True, null=True)  # Field name made lowercase.
    namemrkcar = models.CharField(db_column='NAMEMRKCAR', max_length=20, blank=True, null=True)  # Field name made lowercase.
    model = models.CharField(db_column='MODEL', max_length=36, blank=True, null=True)  # Field name made lowercase.
    year = models.SmallIntegerField(db_column='YEAR', blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(default=0.00, db_column='PRICE', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    obem = models.IntegerField(db_column='OBEM', blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(db_column='ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nkuz = models.CharField(db_column='NKUZ', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kabina = models.CharField(db_column='KABINA', max_length=40, blank=True, null=True)  # Field name made lowercase.
    nsh = models.CharField(db_column='NSH', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ndv = models.CharField(db_column='NDV', max_length=40, blank=True, null=True)  # Field name made lowercase.
    prim = models.FloatField(default=0.00, db_column='PRIM', blank=True, null=True)  # Field name made lowercase.
    probeg = models.IntegerField(db_column='PROBEG', blank=True, null=True)  # Field name made lowercase.
    nblktc1 = models.CharField(db_column='NBLKTC1', max_length=8, blank=True, null=True)  # Field name made lowercase.
    nblktc1p = models.CharField(db_column='NBLKTC1P', max_length=8, blank=True, null=True)  # Field name made lowercase.
    nzp = models.DecimalField(default=0.00, db_column='NZP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dmodify = models.DateTimeField(db_column='DMODIFY', blank=True, null=True)  # Field name made lowercase.
    tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    p_edoc_id = models.DecimalField(default=0.00, db_column='P_EDOC_ID', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=34, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'KBRAVTMB'


class Kbrdinfo(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    k32 = models.IntegerField(db_column='K32', blank=True, null=True)  # Field name made lowercase.
    ngr = models.CharField(db_column='NGR', max_length=2, blank=True, null=True)  # Field name made lowercase.
    typ_ngr = models.CharField(db_column='TYP_NGR', max_length=2, blank=True, null=True)  # Field name made lowercase.
    k32g = models.SmallIntegerField(db_column='K32G', blank=True, null=True)  # Field name made lowercase.
    numrec = models.DecimalField(default=0.00, db_column='NUMREC', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    text1 = models.CharField(db_column='TEXT1', max_length=250, blank=True, null=True)  # Field name made lowercase.
    ind_text = models.CharField(db_column='IND_TEXT', max_length=3, blank=True, null=True)  # Field name made lowercase.
    text2 = models.CharField(db_column='TEXT2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    typ_izm = models.CharField(db_column='TYP_IZM', max_length=1, blank=True, null=True)  # Field name made lowercase.
    kolvo = models.DecimalField(default=0.00, db_column='KOLVO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    code_edi = models.CharField(db_column='CODE_EDI', max_length=3, blank=True, null=True)  # Field name made lowercase.
    name_edi = models.CharField(db_column='NAME_EDI', max_length=17, blank=True, null=True)  # Field name made lowercase.
    nblktc1 = models.CharField(db_column='NBLKTC1', max_length=32, blank=True, null=True)  # Field name made lowercase.
    nblktc1p = models.CharField(db_column='NBLKTC1P', max_length=32, blank=True, null=True)  # Field name made lowercase.
    nzp = models.DecimalField(default=0.00, db_column='NZP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dmodify = models.DateTimeField(db_column='DMODIFY', blank=True, null=True)  # Field name made lowercase.
    tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    p_edoc_id = models.DecimalField(default=0.00, db_column='P_EDOC_ID', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=58, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'KBRDINFO'


class Kbrdokiz(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    k32 = models.IntegerField(db_column='K32', blank=True, null=True)  # Field name made lowercase.
    k4401 = models.SmallIntegerField(db_column='K4401', blank=True, null=True)  # Field name made lowercase.
    k4402 = models.SmallIntegerField(db_column='K4402', blank=True, null=True)  # Field name made lowercase.
    k44020 = models.CharField(db_column='K44020', max_length=1, blank=True, null=True)  # Field name made lowercase.
    k44_cust = models.CharField(db_column='K44_CUST', max_length=8, blank=True, null=True)  # Field name made lowercase.
    k440 = models.CharField(db_column='K440', max_length=4, blank=True, null=True)  # Field name made lowercase.
    k441 = models.CharField(db_column='K441', max_length=5, blank=True, null=True)  # Field name made lowercase.
    k441a = models.CharField(db_column='K441A', max_length=2, blank=True, null=True)  # Field name made lowercase.
    k442 = models.CharField(db_column='K442', max_length=50, blank=True, null=True)  # Field name made lowercase.
    k442lic1 = models.SmallIntegerField(db_column='K442LIC1', blank=True, null=True)  # Field name made lowercase.
    k442lic2 = models.IntegerField(db_column='K442LIC2', blank=True, null=True)  # Field name made lowercase.
    k442r = models.CharField(db_column='K442R', max_length=28, blank=True, null=True)  # Field name made lowercase.
    k442simp = models.CharField(db_column='K442SIMP', max_length=1, blank=True, null=True)  # Field name made lowercase.
    k44mdp1 = models.IntegerField(db_column='K44MDP1', blank=True, null=True)  # Field name made lowercase.
    k44mdp2 = models.CharField(db_column='K44MDP2', max_length=18, blank=True, null=True)  # Field name made lowercase.
    k443 = models.DateTimeField(db_column='K443', blank=True, null=True)  # Field name made lowercase.
    k444 = models.CharField(db_column='K444', max_length=250, blank=True, null=True)  # Field name made lowercase.
    k445 = models.CharField(db_column='K445', max_length=150, blank=True, null=True)  # Field name made lowercase.
    k446 = models.DateTimeField(db_column='K446', blank=True, null=True)  # Field name made lowercase.
    k447 = models.DateTimeField(db_column='K447', blank=True, null=True)  # Field name made lowercase.
    k4480et = models.CharField(db_column='K4480ET', max_length=10, blank=True, null=True)  # Field name made lowercase.
    k4481et = models.DateTimeField(db_column='K4481ET', blank=True, null=True)  # Field name made lowercase.
    k44stper = models.DecimalField(default=0.00, db_column='K44STPER', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    k44sfcntry = models.CharField(db_column='K44SFCNTRY', max_length=2, blank=True, null=True)  # Field name made lowercase.
    k44alldoc = models.SmallIntegerField(db_column='K44ALLDOC', blank=True, null=True)  # Field name made lowercase.
    k4491 = models.DateTimeField(db_column='K4491', blank=True, null=True)  # Field name made lowercase.
    k4492 = models.DateTimeField(db_column='K4492', blank=True, null=True)  # Field name made lowercase.
    k4493 = models.CharField(db_column='K4493', max_length=2, blank=True, null=True)  # Field name made lowercase.
    k44dd = models.DateTimeField(db_column='K44DD', blank=True, null=True)  # Field name made lowercase.
    nblktc1 = models.CharField(db_column='NBLKTC1', max_length=32, blank=True, null=True)  # Field name made lowercase.
    nblktc1p = models.CharField(db_column='NBLKTC1P', max_length=32, blank=True, null=True)  # Field name made lowercase.
    nzp = models.DecimalField(default=0.00, db_column='NZP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dmodify = models.DateTimeField(db_column='DMODIFY', blank=True, null=True)  # Field name made lowercase.
    tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    p_edoc_id = models.DecimalField(default=0.00, db_column='P_EDOC_ID', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=58, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'KBRDOKIZ'


class Kbrhead(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    k032 = models.IntegerField(db_column='K032', blank=True, null=True)  # Field name made lowercase.
    k05 = models.IntegerField(db_column='K05', blank=True, null=True)  # Field name made lowercase.
    k121 = models.DecimalField(default=0.00, db_column='K121', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    k122 = models.DecimalField(default=0.00, db_column='K122', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    k202 = models.CharField(db_column='K202', max_length=3, blank=True, null=True)  # Field name made lowercase.
    k2021 = models.CharField(db_column='K2021', max_length=40, blank=True, null=True)  # Field name made lowercase.
    k203 = models.CharField(db_column='K203', max_length=250, blank=True, null=True)  # Field name made lowercase.
    k221 = models.CharField(db_column='K221', max_length=3, blank=True, null=True)  # Field name made lowercase.
    k222 = models.DecimalField(default=0.00, db_column='K222', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    k23 = models.FloatField(default=0.00, db_column='K23', blank=True, null=True)  # Field name made lowercase.
    k230 = models.DateTimeField(db_column='K230', blank=True, null=True)  # Field name made lowercase.
    k54_itn = models.CharField(db_column='K54_ITN', max_length=13, blank=True, null=True)  # Field name made lowercase.
    k5410 = models.CharField(db_column='K5410', max_length=1, blank=True, null=True)  # Field name made lowercase.
    k541 = models.CharField(db_column='K541', max_length=14, blank=True, null=True)  # Field name made lowercase.
    k541d = models.DateTimeField(db_column='K541D', blank=True, null=True)  # Field name made lowercase.
    k5411 = models.CharField(db_column='K5411', max_length=50, blank=True, null=True)  # Field name made lowercase.
    k5411d = models.DateTimeField(db_column='K5411D', blank=True, null=True)  # Field name made lowercase.
    k541_inn = models.CharField(db_column='K541_INN', max_length=12, blank=True, null=True)  # Field name made lowercase.
    k541_kpp = models.CharField(db_column='K541_KPP', max_length=9, blank=True, null=True)  # Field name made lowercase.
    k542 = models.DateTimeField(db_column='K542', blank=True, null=True)  # Field name made lowercase.
    k543 = models.CharField(db_column='K543', max_length=4, blank=True, null=True)  # Field name made lowercase.
    k5441 = models.CharField(db_column='K5441', max_length=150, blank=True, null=True)  # Field name made lowercase.
    k5441nm = models.CharField(db_column='K5441NM', max_length=150, blank=True, null=True)  # Field name made lowercase.
    k5441mdnm = models.CharField(db_column='K5441MDNM', max_length=150, blank=True, null=True)  # Field name made lowercase.
    k5442 = models.CharField(db_column='K5442', max_length=50, blank=True, null=True)  # Field name made lowercase.
    k5443 = models.CharField(db_column='K5443', max_length=250, blank=True, null=True)  # Field name made lowercase.
    k5444 = models.CharField(db_column='K5444', max_length=50, blank=True, null=True)  # Field name made lowercase.
    k5445 = models.DateTimeField(db_column='K5445', blank=True, null=True)  # Field name made lowercase.
    k5446 = models.DateTimeField(db_column='K5446', blank=True, null=True)  # Field name made lowercase.
    k5447 = models.CharField(db_column='K5447', max_length=50, blank=True, null=True)  # Field name made lowercase.
    k5451 = models.CharField(db_column='K5451', max_length=2, blank=True, null=True)  # Field name made lowercase.
    k5451a = models.CharField(db_column='K5451A', max_length=15, blank=True, null=True)  # Field name made lowercase.
    k54521 = models.CharField(db_column='K54521', max_length=11, blank=True, null=True)  # Field name made lowercase.
    k54522 = models.CharField(db_column='K54522', max_length=25, blank=True, null=True)  # Field name made lowercase.
    k54523 = models.CharField(db_column='K54523', max_length=150, blank=True, null=True)  # Field name made lowercase.
    k5453 = models.DateTimeField(db_column='K5453', blank=True, null=True)  # Field name made lowercase.
    kb0 = models.DecimalField(default=0.00, db_column='KB0', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ka = models.DateTimeField(db_column='KA', blank=True, null=True)  # Field name made lowercase.
    kc30 = models.CharField(db_column='KC30', max_length=2, blank=True, null=True)  # Field name made lowercase.
    nblktc1 = models.CharField(db_column='NBLKTC1', max_length=32, blank=True, null=True)  # Field name made lowercase.
    nblktc1p = models.CharField(db_column='NBLKTC1P', max_length=32, blank=True, null=True)  # Field name made lowercase.
    nzp = models.DecimalField(default=0.00, db_column='NZP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dmodify = models.DateTimeField(db_column='DMODIFY', blank=True, null=True)  # Field name made lowercase.
    tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    p_edoc_id = models.DecimalField(default=0.00, db_column='P_EDOC_ID', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=58, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'KBRHEAD'


class Kbrpk(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    k32 = models.IntegerField(db_column='K32', blank=True, null=True)  # Field name made lowercase.
    pksign = models.CharField(db_column='PKSIGN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    pkvid = models.CharField(db_column='PKVID', max_length=2, blank=True, null=True)  # Field name made lowercase.
    pkkolvo = models.IntegerField(db_column='PKKOLVO', blank=True, null=True)  # Field name made lowercase.
    pkinf = models.CharField(db_column='PKINF', max_length=150, blank=True, null=True)  # Field name made lowercase.
    nblktc1 = models.CharField(db_column='NBLKTC1', max_length=32, blank=True, null=True)  # Field name made lowercase.
    nblktc1p = models.CharField(db_column='NBLKTC1P', max_length=32, blank=True, null=True)  # Field name made lowercase.
    nzp = models.DecimalField(default=0.00, db_column='NZP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dmodify = models.DateTimeField(db_column='DMODIFY', blank=True, null=True)  # Field name made lowercase.
    tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    p_edoc_id = models.DecimalField(default=0.00, db_column='P_EDOC_ID', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=58, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'KBRPK'


class Kbrplbiz(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    kb0 = models.CharField(db_column='KB0', max_length=1, blank=True, null=True)  # Field name made lowercase.
    kb1 = models.CharField(db_column='KB1', max_length=4, blank=True, null=True)  # Field name made lowercase.
    kb2 = models.DecimalField(default=0.00, db_column='KB2', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    kb3 = models.CharField(db_column='KB3', max_length=3, blank=True, null=True)  # Field name made lowercase.
    kb6 = models.DecimalField(default=0.00, db_column='KB6', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    kb61 = models.CharField(db_column='KB61', max_length=3, blank=True, null=True)  # Field name made lowercase.
    kb7 = models.DecimalField(default=0.00, db_column='KB7', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    nblktc1 = models.CharField(db_column='NBLKTC1', max_length=32, blank=True, null=True)  # Field name made lowercase.
    nzp = models.DecimalField(default=0.00, db_column='NZP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dmodify = models.DateTimeField(db_column='DMODIFY', blank=True, null=True)  # Field name made lowercase.
    tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    p_edoc_id = models.DecimalField(default=0.00, db_column='P_EDOC_ID', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=58, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'KBRPLBIZ'


class Kbrpltiz(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    k32 = models.IntegerField(db_column='K32', blank=True, null=True)  # Field name made lowercase.
    k470 = models.CharField(db_column='K470', max_length=1, blank=True, null=True)  # Field name made lowercase.
    k471 = models.CharField(db_column='K471', max_length=4, blank=True, null=True)  # Field name made lowercase.
    k471npp = models.SmallIntegerField(db_column='K471NPP', blank=True, null=True)  # Field name made lowercase.
    k472 = models.DecimalField(default=0.00, db_column='K472', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    k4721 = models.CharField(db_column='K4721', max_length=3, blank=True, null=True)  # Field name made lowercase.
    k473 = models.FloatField(default=0.00, db_column='K473', blank=True, null=True)  # Field name made lowercase.
    k4731 = models.CharField(db_column='K4731', max_length=1, blank=True, null=True)  # Field name made lowercase.
    k4732 = models.CharField(db_column='K4732', max_length=3, blank=True, null=True)  # Field name made lowercase.
    k4733 = models.CharField(db_column='K4733', max_length=3, blank=True, null=True)  # Field name made lowercase.
    k4734 = models.FloatField(default=0.00, db_column='K4734', blank=True, null=True)  # Field name made lowercase.
    kpp = models.SmallIntegerField(db_column='KPP', blank=True, null=True)  # Field name made lowercase.
    k474 = models.DecimalField(default=0.00, db_column='K474', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    k4741 = models.CharField(db_column='K4741', max_length=3, blank=True, null=True)  # Field name made lowercase.
    k475 = models.CharField(db_column='K475', max_length=2, blank=True, null=True)  # Field name made lowercase.
    k476 = models.DecimalField(default=0.00, db_column='K476', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    k4761 = models.CharField(db_column='K4761', max_length=3, blank=True, null=True)  # Field name made lowercase.
    k473z1_2 = models.CharField(db_column='K473Z1_2', max_length=1, blank=True, null=True)  # Field name made lowercase.
    k473_2 = models.FloatField(default=0.00, db_column='K473_2', blank=True, null=True)  # Field name made lowercase.
    k4731_2 = models.CharField(db_column='K4731_2', max_length=1, blank=True, null=True)  # Field name made lowercase.
    k4732_2 = models.CharField(db_column='K4732_2', max_length=3, blank=True, null=True)  # Field name made lowercase.
    k4733_2 = models.CharField(db_column='K4733_2', max_length=3, blank=True, null=True)  # Field name made lowercase.
    k4734_2 = models.FloatField(default=0.00, db_column='K4734_2', blank=True, null=True)  # Field name made lowercase.
    k473z1_3 = models.CharField(db_column='K473Z1_3', max_length=1, blank=True, null=True)  # Field name made lowercase.
    k473_3 = models.FloatField(default=0.00, db_column='K473_3', blank=True, null=True)  # Field name made lowercase.
    k4731_3 = models.CharField(db_column='K4731_3', max_length=1, blank=True, null=True)  # Field name made lowercase.
    k4732_3 = models.CharField(db_column='K4732_3', max_length=3, blank=True, null=True)  # Field name made lowercase.
    k4733_3 = models.CharField(db_column='K4733_3', max_length=3, blank=True, null=True)  # Field name made lowercase.
    k4734_3 = models.FloatField(default=0.00, db_column='K4734_3', blank=True, null=True)  # Field name made lowercase.
    k473z2_2 = models.SmallIntegerField(db_column='K473Z2_2', blank=True, null=True)  # Field name made lowercase.
    k477 = models.DecimalField(default=0.00, db_column='K477', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    k4730 = models.DateTimeField(db_column='K4730', blank=True, null=True)  # Field name made lowercase.
    k4740 = models.DateTimeField(db_column='K4740', blank=True, null=True)  # Field name made lowercase.
    k47_nd = models.SmallIntegerField(db_column='K47_ND', blank=True, null=True)  # Field name made lowercase.
    k47_ns = models.SmallIntegerField(db_column='K47_NS', blank=True, null=True)  # Field name made lowercase.
    k47_nm = models.SmallIntegerField(db_column='K47_NM', blank=True, null=True)  # Field name made lowercase.
    k47_tr = models.FloatField(default=0.00, db_column='K47_TR', blank=True, null=True)  # Field name made lowercase.
    nblktc1 = models.CharField(db_column='NBLKTC1', max_length=32, blank=True, null=True)  # Field name made lowercase.
    nblktc1p = models.CharField(db_column='NBLKTC1P', max_length=32, blank=True, null=True)  # Field name made lowercase.
    nzp = models.DecimalField(default=0.00, db_column='NZP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dmodify = models.DateTimeField(db_column='DMODIFY', blank=True, null=True)  # Field name made lowercase.
    tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    p_edoc_id = models.DecimalField(default=0.00, db_column='P_EDOC_ID', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    pdoc = models.CharField(db_column='PDOC', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pdate = models.DateTimeField(db_column='PDATE', blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=58, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'KBRPLTIZ'


class Kbrsumpp(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    k32 = models.IntegerField(db_column='K32', blank=True, null=True)  # Field name made lowercase.
    k471 = models.CharField(db_column='K471', max_length=4, blank=True, null=True)  # Field name made lowercase.
    k471npp = models.SmallIntegerField(db_column='K471NPP', blank=True, null=True)  # Field name made lowercase.
    k4741 = models.CharField(db_column='K4741', max_length=3, blank=True, null=True)  # Field name made lowercase.
    iret = models.SmallIntegerField(db_column='IRET', blank=True, null=True)  # Field name made lowercase.
    numpdok = models.CharField(db_column='NUMPDOK', max_length=50, blank=True, null=True)  # Field name made lowercase.
    datpdok = models.DateTimeField(db_column='DATPDOK', blank=True, null=True)  # Field name made lowercase.
    sum_all = models.DecimalField(default=0.00, db_column='SUM_ALL', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sumpdok = models.DecimalField(default=0.00, db_column='SUMPDOK', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valpdok = models.CharField(db_column='VALPDOK', max_length=3, blank=True, null=True)  # Field name made lowercase.
    datpostd = models.DateTimeField(db_column='DATPOSTD', blank=True, null=True)  # Field name made lowercase.
    datpaymt = models.DateTimeField(db_column='DATPAYMT', blank=True, null=True)  # Field name made lowercase.
    innplat = models.CharField(db_column='INNPLAT', max_length=12, blank=True, null=True)  # Field name made lowercase.
    kppplat = models.CharField(db_column='KPPPLAT', max_length=9, blank=True, null=True)  # Field name made lowercase.
    lnpins = models.CharField(db_column='LNPINS', max_length=4, blank=True, null=True)  # Field name made lowercase.
    fioins = models.CharField(db_column='FIOINS', max_length=40, blank=True, null=True)  # Field name made lowercase.
    datins = models.DateTimeField(db_column='DATINS', blank=True, null=True)  # Field name made lowercase.
    timins = models.CharField(db_column='TIMINS', max_length=8, blank=True, null=True)  # Field name made lowercase.
    nblktc1 = models.CharField(db_column='NBLKTC1', max_length=8, blank=True, null=True)  # Field name made lowercase.
    nblktc1p = models.CharField(db_column='NBLKTC1P', max_length=8, blank=True, null=True)  # Field name made lowercase.
    nzp = models.DecimalField(default=0.00, db_column='NZP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dmodify = models.DateTimeField(db_column='DMODIFY', blank=True, null=True)  # Field name made lowercase.
    tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    p_edoc_id = models.DecimalField(default=0.00, db_column='P_EDOC_ID', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=34, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'KBRSUMPP'


class Kbrterms(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    k32 = models.IntegerField(db_column='K32', blank=True, null=True)  # Field name made lowercase.
    terms = models.CharField(db_column='TERMS', max_length=3, blank=True, null=True)  # Field name made lowercase.
    termspoint = models.CharField(db_column='TERMSPOINT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    termspass = models.CharField(db_column='TERMSPASS', max_length=250, blank=True, null=True)  # Field name made lowercase.
    nblktc1 = models.CharField(db_column='NBLKTC1', max_length=32, blank=True, null=True)  # Field name made lowercase.
    nblktc1p = models.CharField(db_column='NBLKTC1P', max_length=32, blank=True, null=True)  # Field name made lowercase.
    nzp = models.DecimalField(default=0.00, db_column='NZP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dmodify = models.DateTimeField(db_column='DMODIFY', blank=True, null=True)  # Field name made lowercase.
    tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    p_edoc_id = models.DecimalField(default=0.00, db_column='P_EDOC_ID', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=58, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'KBRTERMS'


class Kbrtovg(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    k32 = models.IntegerField(db_column='K32', blank=True, null=True)  # Field name made lowercase.
    k32g = models.SmallIntegerField(db_column='K32G', blank=True, null=True)  # Field name made lowercase.
    numrec = models.SmallIntegerField(db_column='NUMREC', blank=True, null=True)  # Field name made lowercase.
    k31_10 = models.CharField(db_column='K31_10', max_length=4, blank=True, null=True)  # Field name made lowercase.
    k31_11 = models.CharField(db_column='K31_11', max_length=150, blank=True, null=True)  # Field name made lowercase.
    k31_12 = models.CharField(db_column='K31_12', max_length=150, blank=True, null=True)  # Field name made lowercase.
    k31_14 = models.CharField(db_column='K31_14', max_length=50, blank=True, null=True)  # Field name made lowercase.
    k31_15_mod = models.CharField(db_column='K31_15_MOD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    k31_15 = models.CharField(db_column='K31_15', max_length=50, blank=True, null=True)  # Field name made lowercase.
    k31_16 = models.CharField(db_column='K31_16', max_length=50, blank=True, null=True)  # Field name made lowercase.
    k31_17 = models.CharField(db_column='K31_17', max_length=50, blank=True, null=True)  # Field name made lowercase.
    k31_18 = models.CharField(db_column='K31_18', max_length=30, blank=True, null=True)  # Field name made lowercase.
    k31_19 = models.CharField(db_column='K31_19', max_length=20, blank=True, null=True)  # Field name made lowercase.
    k31_20 = models.CharField(db_column='K31_20', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kolvo = models.DecimalField(default=0.00, db_column='KOLVO', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    code_edi = models.CharField(db_column='CODE_EDI', max_length=3, blank=True, null=True)  # Field name made lowercase.
    name_edi = models.CharField(db_column='NAME_EDI', max_length=13, blank=True, null=True)  # Field name made lowercase.
    nblktc1 = models.CharField(db_column='NBLKTC1', max_length=32, blank=True, null=True)  # Field name made lowercase.
    nblktc1p = models.CharField(db_column='NBLKTC1P', max_length=32, blank=True, null=True)  # Field name made lowercase.
    nzp = models.DecimalField(default=0.00, db_column='NZP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dmodify = models.DateTimeField(db_column='DMODIFY', blank=True, null=True)  # Field name made lowercase.
    tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    p_edoc_id = models.DecimalField(default=0.00, db_column='P_EDOC_ID', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=58, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'KBRTOVG'


class Kbrtoviz(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    typ_ktc = models.SmallIntegerField(db_column='TYP_KTC', blank=True, null=True)  # Field name made lowercase.
    k011 = models.CharField(db_column='K011', max_length=1, blank=True, null=True)  # Field name made lowercase.
    k012 = models.CharField(db_column='K012', max_length=4, blank=True, null=True)  # Field name made lowercase.
    k013 = models.CharField(db_column='K013', max_length=1, blank=True, null=True)  # Field name made lowercase.
    k031 = models.IntegerField(db_column='K031', blank=True, null=True)  # Field name made lowercase.
    ch = models.SmallIntegerField(db_column='CH', blank=True, null=True)  # Field name made lowercase.
    k31_1 = models.CharField(db_column='K31_1', max_length=250, blank=True, null=True)  # Field name made lowercase.
    k31_1_prdt = models.DateTimeField(db_column='K31_1_PRDT', blank=True, null=True)  # Field name made lowercase.
    k31_1_oilf = models.CharField(db_column='K31_1_OILF', max_length=250, blank=True, null=True)  # Field name made lowercase.
    k31_2 = models.IntegerField(db_column='K31_2', blank=True, null=True)  # Field name made lowercase.
    k31_2part = models.IntegerField(db_column='K31_2PART', blank=True, null=True)  # Field name made lowercase.
    k31_20 = models.CharField(db_column='K31_20', max_length=1, blank=True, null=True)  # Field name made lowercase.
    k31_7 = models.DecimalField(default=0.00, db_column='K31_7', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    k31_71 = models.CharField(db_column='K31_71', max_length=13, blank=True, null=True)  # Field name made lowercase.
    k41a = models.CharField(db_column='K41A', max_length=3, blank=True, null=True)  # Field name made lowercase.
    k31_8 = models.DecimalField(default=0.00, db_column='K31_8', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    k31_81 = models.CharField(db_column='K31_81', max_length=13, blank=True, null=True)  # Field name made lowercase.
    k31_82 = models.CharField(db_column='K31_82', max_length=3, blank=True, null=True)  # Field name made lowercase.
    k31_9 = models.DecimalField(default=0.00, db_column='K31_9', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    k31_fact = models.DecimalField(default=0.00, db_column='K31_FACT', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    k31_91 = models.CharField(db_column='K31_91', max_length=13, blank=True, null=True)  # Field name made lowercase.
    k31_92 = models.CharField(db_column='K31_92', max_length=3, blank=True, null=True)  # Field name made lowercase.
    k32 = models.IntegerField(db_column='K32', blank=True, null=True)  # Field name made lowercase.
    k33 = models.CharField(db_column='K33', max_length=10, blank=True, null=True)  # Field name made lowercase.
    k330 = models.CharField(db_column='K330', max_length=1, blank=True, null=True)  # Field name made lowercase.
    k331 = models.CharField(db_column='K331', max_length=1, blank=True, null=True)  # Field name made lowercase.
    k332 = models.CharField(db_column='K332', max_length=1, blank=True, null=True)  # Field name made lowercase.
    k333 = models.CharField(db_column='K333', max_length=4, blank=True, null=True)  # Field name made lowercase.
    k35 = models.DecimalField(default=0.00, db_column='K35', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    k38 = models.DecimalField(default=0.00, db_column='K38', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    k38_1 = models.DecimalField(default=0.00, db_column='K38_1', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    k42 = models.DecimalField(default=0.00, db_column='K42', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    k43 = models.CharField(db_column='K43', max_length=2, blank=True, null=True)  # Field name made lowercase.
    k451 = models.DecimalField(default=0.00, db_column='K451', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    k452 = models.DecimalField(default=0.00, db_column='K452', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    k46 = models.DecimalField(default=0.00, db_column='K46', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    k461 = models.CharField(db_column='K461', max_length=1, blank=True, null=True)  # Field name made lowercase.
    k470 = models.DecimalField(default=0.00, db_column='K470', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    nblktc1 = models.CharField(db_column='NBLKTC1', max_length=32, blank=True, null=True)  # Field name made lowercase.
    nblktc2 = models.CharField(db_column='NBLKTC2', max_length=8, blank=True, null=True)  # Field name made lowercase.
    nblktc1p = models.CharField(db_column='NBLKTC1P', max_length=32, blank=True, null=True)  # Field name made lowercase.
    nzp = models.DecimalField(default=0.00, db_column='NZP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dmodify = models.DateTimeField(db_column='DMODIFY', blank=True, null=True)  # Field name made lowercase.
    tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    p_edoc_id = models.DecimalField(default=0.00, db_column='P_EDOC_ID', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=58, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'KBRTOVIZ'


class Kbrtovs(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    k32 = models.IntegerField(db_column='K32', blank=True, null=True)  # Field name made lowercase.
    k32g = models.SmallIntegerField(db_column='K32G', blank=True, null=True)  # Field name made lowercase.
    numrec = models.SmallIntegerField(db_column='NUMREC', blank=True, null=True)  # Field name made lowercase.
    k31_15_sn = models.CharField(db_column='K31_15_SN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nblktc1 = models.CharField(db_column='NBLKTC1', max_length=8, blank=True, null=True)  # Field name made lowercase.
    nblktc1p = models.CharField(db_column='NBLKTC1P', max_length=8, blank=True, null=True)  # Field name made lowercase.
    nzp = models.DecimalField(default=0.00, db_column='NZP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dmodify = models.DateTimeField(db_column='DMODIFY', blank=True, null=True)  # Field name made lowercase.
    tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    p_edoc_id = models.DecimalField(default=0.00, db_column='P_EDOC_ID', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=34, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'KBRTOVS'


class Ktdamnum(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g32 = models.IntegerField(db_column='G32', blank=True, null=True)  # Field name made lowercase.
    series = models.CharField(db_column='SERIES', max_length=9, blank=True, null=True)  # Field name made lowercase.
    numstart = models.IntegerField(db_column='NUMSTART', blank=True, null=True)  # Field name made lowercase.
    numend = models.IntegerField(db_column='NUMEND', blank=True, null=True)  # Field name made lowercase.
    kolvoam = models.IntegerField(db_column='KOLVOAM', blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'KTDAMNUM'


class Ktdavtmb(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g32 = models.IntegerField(db_column='G32', blank=True, null=True)  # Field name made lowercase.
    nud = models.CharField(db_column='NUD', max_length=12, blank=True, null=True)  # Field name made lowercase.
    kodmrk = models.CharField(db_column='KODMRK', max_length=3, blank=True, null=True)  # Field name made lowercase.
    namemrkcar = models.CharField(db_column='NAMEMRKCAR', max_length=250, blank=True, null=True)  # Field name made lowercase.
    model = models.CharField(db_column='MODEL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    year = models.SmallIntegerField(db_column='YEAR', blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(default=0.00, db_column='PRICE', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    obem = models.DecimalField(default=0.00, db_column='OBEM', max_digits=17, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    id = models.CharField(db_column='ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nkuz = models.CharField(db_column='NKUZ', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kabina = models.CharField(db_column='KABINA', max_length=40, blank=True, null=True)  # Field name made lowercase.
    nsh = models.CharField(db_column='NSH', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ndv = models.CharField(db_column='NDV', max_length=40, blank=True, null=True)  # Field name made lowercase.
    emergency = models.CharField(db_column='EMERGENCY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    prim = models.CharField(db_column='PRIM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    probeg = models.DecimalField(default=0.00, db_column='PROBEG', max_digits=17, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.
    pricev = models.CharField(db_column='PRICEV', max_length=3, blank=True, null=True)  # Field name made lowercase.
    maxpower1 = models.DecimalField(default=0.00, db_column='MAXPOWER1', max_digits=17, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    maxpower2 = models.DecimalField(default=0.00, db_column='MAXPOWER2', max_digits=17, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    maxpower3 = models.DecimalField(default=0.00, db_column='MAXPOWER3', max_digits=17, decimal_places=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'KTDAVTMB'


class Ktdcont(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g32 = models.IntegerField(db_column='G32', blank=True, null=True)  # Field name made lowercase.
    container = models.CharField(db_column='CONTAINER', max_length=17, blank=True, null=True)  # Field name made lowercase.
    conttype = models.CharField(db_column='CONTTYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    contstat = models.CharField(db_column='CONTSTAT', max_length=1, blank=True, null=True)  # Field name made lowercase.
    nzp = models.DecimalField(default=0.00, db_column='NZP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dmodify = models.DateTimeField(db_column='DMODIFY', blank=True, null=True)  # Field name made lowercase.
    tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    p_edoc_id = models.DecimalField(default=0.00, db_column='P_EDOC_ID', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'KTDCONT'


class Ktdcrdts(BaseModel):
    numcard = models.CharField(db_column='NUMCARD', max_length=23, blank=True, null=True)  # Field name made lowercase.
    vin = models.CharField(db_column='VIN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kodmrk = models.CharField(db_column='KODMRK', max_length=3, blank=True, null=True)  # Field name made lowercase.
    namemrkcar = models.CharField(db_column='NAMEMRKCAR', max_length=250, blank=True, null=True)  # Field name made lowercase.
    model = models.CharField(db_column='MODEL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tipts = models.CharField(db_column='TIPTS', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tipts3 = models.CharField(db_column='TIPTS3', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tiptsname = models.CharField(db_column='TIPTSNAME', max_length=150, blank=True, null=True)  # Field name made lowercase.
    kategts = models.CharField(db_column='KATEGTS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    mest = models.SmallIntegerField(db_column='MEST', blank=True, null=True)  # Field name made lowercase.
    god = models.SmallIntegerField(db_column='GOD', blank=True, null=True)  # Field name made lowercase.
    moddvig = models.CharField(db_column='MODDVIG', max_length=15, blank=True, null=True)  # Field name made lowercase.
    numdvig = models.CharField(db_column='NUMDVIG', max_length=40, blank=True, null=True)  # Field name made lowercase.
    numkper = models.CharField(db_column='NUMKPER', max_length=40, blank=True, null=True)  # Field name made lowercase.
    nummost = models.CharField(db_column='NUMMOST', max_length=80, blank=True, null=True)  # Field name made lowercase.
    shassi = models.CharField(db_column='SHASSI', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kuzov = models.CharField(db_column='KUZOV', max_length=40, blank=True, null=True)  # Field name made lowercase.
    kabina = models.CharField(db_column='KABINA', max_length=40, blank=True, null=True)  # Field name made lowercase.
    emergency = models.CharField(db_column='EMERGENCY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    zvet = models.CharField(db_column='ZVET', max_length=3, blank=True, null=True)  # Field name made lowercase.
    listcol = models.CharField(db_column='LISTCOL', max_length=43, blank=True, null=True)  # Field name made lowercase.
    powerls = models.FloatField(default=0.00, db_column='POWERLS', blank=True, null=True)  # Field name made lowercase.
    powerkw = models.FloatField(default=0.00, db_column='POWERKW', blank=True, null=True)  # Field name made lowercase.
    obdvig = models.IntegerField(db_column='OBDVIG', blank=True, null=True)  # Field name made lowercase.
    tipdv = models.CharField(db_column='TIPDV', max_length=2, blank=True, null=True)  # Field name made lowercase.
    viddvig = models.CharField(db_column='VIDDVIG', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ekoclass = models.CharField(db_column='EKOCLASS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    maxmass = models.IntegerField(db_column='MAXMASS', blank=True, null=True)  # Field name made lowercase.
    minmass = models.IntegerField(db_column='MINMASS', blank=True, null=True)  # Field name made lowercase.
    maxspeed = models.SmallIntegerField(db_column='MAXSPEED', blank=True, null=True)  # Field name made lowercase.
    width = models.IntegerField(db_column='WIDTH', blank=True, null=True)  # Field name made lowercase.
    height = models.IntegerField(db_column='HEIGHT', blank=True, null=True)  # Field name made lowercase.
    length = models.IntegerField(db_column='LENGTH', blank=True, null=True)  # Field name made lowercase.
    kodizgot = models.CharField(db_column='KODIZGOT', max_length=3, blank=True, null=True)  # Field name made lowercase.
    izgotov = models.CharField(db_column='IZGOTOV', max_length=150, blank=True, null=True)  # Field name made lowercase.
    strizg = models.CharField(db_column='STRIZG', max_length=2, blank=True, null=True)  # Field name made lowercase.
    izgpost = models.CharField(db_column='IZGPOST', max_length=9, blank=True, null=True)  # Field name made lowercase.
    izgstr = models.CharField(db_column='IZGSTR', max_length=2, blank=True, null=True)  # Field name made lowercase.
    izgsubd = models.CharField(db_column='IZGSUBD', max_length=35, blank=True, null=True)  # Field name made lowercase.
    izgcity = models.CharField(db_column='IZGCITY', max_length=35, blank=True, null=True)  # Field name made lowercase.
    izgstreet = models.CharField(db_column='IZGSTREET', max_length=35, blank=True, null=True)  # Field name made lowercase.
    numodob = models.CharField(db_column='NUMODOB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    datodob = models.DateTimeField(db_column='DATODOB', blank=True, null=True)  # Field name made lowercase.
    orgodob = models.CharField(db_column='ORGODOB', max_length=150, blank=True, null=True)  # Field name made lowercase.
    strvyvoz = models.CharField(db_column='STRVYVOZ', max_length=2, blank=True, null=True)  # Field name made lowercase.
    lic = models.CharField(db_column='LIC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fam = models.CharField(db_column='FAM', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ima = models.CharField(db_column='IMA', max_length=25, blank=True, null=True)  # Field name made lowercase.
    otc = models.CharField(db_column='OTC', max_length=25, blank=True, null=True)  # Field name made lowercase.
    okpo = models.CharField(db_column='OKPO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    inn = models.CharField(db_column='INN', max_length=12, blank=True, null=True)  # Field name made lowercase.
    kpp = models.CharField(db_column='KPP', max_length=9, blank=True, null=True)  # Field name made lowercase.
    kod_dul = models.CharField(db_column='KOD_DUL', max_length=7, blank=True, null=True)  # Field name made lowercase.
    abbrev_dul = models.CharField(db_column='ABBREV_DUL', max_length=6, blank=True, null=True)  # Field name made lowercase.
    ser_dul = models.CharField(db_column='SER_DUL', max_length=11, blank=True, null=True)  # Field name made lowercase.
    nom_dul = models.CharField(db_column='NOM_DUL', max_length=25, blank=True, null=True)  # Field name made lowercase.
    org_dul = models.CharField(db_column='ORG_DUL', max_length=150, blank=True, null=True)  # Field name made lowercase.
    dat_dul = models.DateTimeField(db_column='DAT_DUL', blank=True, null=True)  # Field name made lowercase.
    namesob = models.CharField(db_column='NAMESOB', max_length=150, blank=True, null=True)  # Field name made lowercase.
    sobpost = models.CharField(db_column='SOBPOST', max_length=9, blank=True, null=True)  # Field name made lowercase.
    sobstr = models.CharField(db_column='SOBSTR', max_length=2, blank=True, null=True)  # Field name made lowercase.
    sobsubd = models.CharField(db_column='SOBSUBD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sobcity = models.CharField(db_column='SOBCITY', max_length=35, blank=True, null=True)  # Field name made lowercase.
    sobstreet = models.CharField(db_column='SOBSTREET', max_length=50, blank=True, null=True)  # Field name made lowercase.
    udvvoz = models.CharField(db_column='UDVVOZ', max_length=10, blank=True, null=True)  # Field name made lowercase.
    datud = models.DateTimeField(db_column='DATUD', blank=True, null=True)  # Field name made lowercase.
    lnpu = models.CharField(db_column='LNPU', max_length=4, blank=True, null=True)  # Field name made lowercase.
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    tamogr = models.CharField(db_column='TAMOGR', max_length=250, blank=True, null=True)  # Field name made lowercase.
    tamspec = models.CharField(db_column='TAMSPEC', max_length=250, blank=True, null=True)  # Field name made lowercase.
    numpts = models.CharField(db_column='NUMPTS', max_length=15, blank=True, null=True)  # Field name made lowercase.
    datpts = models.DateTimeField(db_column='DATPTS', blank=True, null=True)  # Field name made lowercase.
    timpts = models.CharField(db_column='TIMPTS', max_length=8, blank=True, null=True)  # Field name made lowercase.
    lnp = models.CharField(db_column='LNP', max_length=4, blank=True, null=True)  # Field name made lowercase.
    work = models.IntegerField(db_column='WORK', blank=True, null=True)  # Field name made lowercase.
    p_ts = models.CharField(db_column='P_TS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g32 = models.IntegerField(db_column='G32', blank=True, null=True)  # Field name made lowercase.
    g33 = models.CharField(db_column='G33', max_length=10, blank=True, null=True)  # Field name made lowercase.
    naimtd = models.CharField(db_column='NAIMTD', max_length=250, blank=True, null=True)  # Field name made lowercase.
    numtd = models.CharField(db_column='NUMTD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dattd = models.DateTimeField(db_column='DATTD', blank=True, null=True)  # Field name made lowercase.
    numz = models.CharField(db_column='NUMZ', max_length=23, blank=True, null=True)  # Field name made lowercase.
    datz = models.DateTimeField(db_column='DATZ', blank=True, null=True)  # Field name made lowercase.
    dateout = models.DateTimeField(db_column='DATEOUT', blank=True, null=True)  # Field name made lowercase.
    timeout = models.CharField(db_column='TIMEOUT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    datemodi = models.DateTimeField(db_column='DATEMODI', blank=True, null=True)  # Field name made lowercase.
    tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    imodi = models.CharField(db_column='IMODI', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ind_k = models.CharField(db_column='IND_K', max_length=1, blank=True, null=True)  # Field name made lowercase.
    d_state = models.CharField(db_column='D_STATE', max_length=19, blank=True, null=True)  # Field name made lowercase.
    d_unload = models.CharField(db_column='D_UNLOAD', max_length=19, blank=True, null=True)  # Field name made lowercase.
    nzp = models.DecimalField(default=0.00, db_column='NZP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    p_edoc_id = models.DecimalField(default=0.00, db_column='P_EDOC_ID', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    strizgc = models.CharField(db_column='STRIZGC', max_length=3, blank=True, null=True)  # Field name made lowercase.
    adrizg = models.CharField(db_column='ADRIZG', max_length=50, blank=True, null=True)  # Field name made lowercase.
    strvyvozc = models.CharField(db_column='STRVYVOZC', max_length=3, blank=True, null=True)  # Field name made lowercase.
    adressob = models.CharField(db_column='ADRESSOB', max_length=80, blank=True, null=True)  # Field name made lowercase.
    ed_idid = models.CharField(db_column='ED_IDID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    numptso = models.CharField(db_column='NUMPTSO', max_length=11, blank=True, null=True)  # Field name made lowercase.
    stsptso = models.CharField(db_column='STSPTSO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ub_idid = models.CharField(db_column='UB_IDID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    yc_status = models.CharField(db_column='YC_STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    yc_tpo = models.CharField(db_column='YC_TPO', max_length=26, blank=True, null=True)  # Field name made lowercase.
    yc_matter = models.CharField(db_column='YC_MATTER', max_length=2, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.
    kateg3 = models.CharField(db_column='KATEG3', max_length=3, blank=True, null=True)  # Field name made lowercase.
    epts = models.CharField(db_column='EPTS', max_length=15, blank=True, null=True)  # Field name made lowercase.
    tipdvname = models.CharField(db_column='TIPDVNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fuel = models.CharField(db_column='FUEL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    powerls2 = models.FloatField(default=0.00, db_column='POWERLS2', blank=True, null=True)  # Field name made lowercase.
    powerkw2 = models.FloatField(default=0.00, db_column='POWERKW2', blank=True, null=True)  # Field name made lowercase.
    tipdv2 = models.CharField(db_column='TIPDV2', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tipdvname2 = models.CharField(db_column='TIPDVNAME2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fuel2 = models.CharField(db_column='FUEL2', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'KTDCRDTS'


class Ktddinf2(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g32 = models.IntegerField(db_column='G32', blank=True, null=True)  # Field name made lowercase.
    type_info = models.CharField(db_column='TYPE_INFO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    numpredd = models.IntegerField(db_column='NUMPREDD', blank=True, null=True)  # Field name made lowercase.
    ngr = models.CharField(db_column='NGR', max_length=2, blank=True, null=True)  # Field name made lowercase.
    typ_ngr = models.CharField(db_column='TYP_NGR', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g32g = models.SmallIntegerField(db_column='G32G', blank=True, null=True)  # Field name made lowercase.
    numrec = models.DecimalField(default=0.00, db_column='NUMREC', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    text1 = models.CharField(db_column='TEXT1', max_length=250, blank=True, null=True)  # Field name made lowercase.
    text2 = models.CharField(db_column='TEXT2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nzp = models.SmallIntegerField(db_column='NZP', blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'KTDDINF2'


class Ktddinfo(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g32 = models.IntegerField(db_column='G32', blank=True, null=True)  # Field name made lowercase.
    ngr = models.CharField(db_column='NGR', max_length=2, blank=True, null=True)  # Field name made lowercase.
    typ_ngr = models.CharField(db_column='TYP_NGR', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g32g = models.SmallIntegerField(db_column='G32G', blank=True, null=True)  # Field name made lowercase.
    numrec = models.DecimalField(default=0.00, db_column='NUMREC', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    text1 = models.CharField(db_column='TEXT1', max_length=250, blank=True, null=True)  # Field name made lowercase.
    ind_text = models.CharField(db_column='IND_TEXT', max_length=3, blank=True, null=True)  # Field name made lowercase.
    text2 = models.CharField(db_column='TEXT2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    typ_izm = models.CharField(db_column='TYP_IZM', max_length=1, blank=True, null=True)  # Field name made lowercase.
    kolvo = models.DecimalField(default=0.00, db_column='KOLVO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    code_edi = models.CharField(db_column='CODE_EDI', max_length=3, blank=True, null=True)  # Field name made lowercase.
    name_edi = models.CharField(db_column='NAME_EDI', max_length=17, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'KTDDINFO'


class Ktddog(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g32 = models.IntegerField(db_column='G32', blank=True, null=True)  # Field name made lowercase.
    dogn = models.CharField(db_column='DOGN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dogd = models.DateTimeField(db_column='DOGD', blank=True, null=True)  # Field name made lowercase.
    pasp = models.CharField(db_column='PASP', max_length=25, blank=True, null=True)  # Field name made lowercase.
    paspbank = models.CharField(db_column='PASPBANK', max_length=70, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'KTDDOG'


class Ktddoga(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g32 = models.IntegerField(db_column='G32', blank=True, null=True)  # Field name made lowercase.
    dogn = models.CharField(db_column='DOGN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dogd = models.DateTimeField(db_column='DOGD', blank=True, null=True)  # Field name made lowercase.
    dogaddn = models.CharField(db_column='DOGADDN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dogaddd = models.DateTimeField(db_column='DOGADDD', blank=True, null=True)  # Field name made lowercase.
    dogaddt = models.CharField(db_column='DOGADDT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'KTDDOGA'


class Ktddogt(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g32 = models.IntegerField(db_column='G32', blank=True, null=True)  # Field name made lowercase.
    dogn = models.CharField(db_column='DOGN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dogd = models.DateTimeField(db_column='DOGD', blank=True, null=True)  # Field name made lowercase.
    dognpp = models.SmallIntegerField(db_column='DOGNPP', blank=True, null=True)  # Field name made lowercase.
    dogorg = models.CharField(db_column='DOGORG', max_length=150, blank=True, null=True)  # Field name made lowercase.
    dogcountry = models.CharField(db_column='DOGCOUNTRY', max_length=2, blank=True, null=True)  # Field name made lowercase.
    origcountr = models.CharField(db_column='ORIGCOUNTR', max_length=2, blank=True, null=True)  # Field name made lowercase.
    terms = models.CharField(db_column='TERMS', max_length=3, blank=True, null=True)  # Field name made lowercase.
    termspoint = models.CharField(db_column='TERMSPOINT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    termspass = models.CharField(db_column='TERMSPASS', max_length=250, blank=True, null=True)  # Field name made lowercase.
    qmain = models.DecimalField(default=0.00, db_column='QMAIN', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    qadd = models.DecimalField(default=0.00, db_column='QADD', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    qaddmeas = models.CharField(db_column='QADDMEAS', max_length=3, blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(default=0.00, db_column='PRICE', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    prval = models.CharField(db_column='PRVAL', max_length=3, blank=True, null=True)  # Field name made lowercase.
    prmeas = models.CharField(db_column='PRMEAS', max_length=3, blank=True, null=True)  # Field name made lowercase.
    prtot = models.DecimalField(default=0.00, db_column='PRTOT', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    prtotval = models.CharField(db_column='PRTOTVAL', max_length=3, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'KTDDOGT'


class Ktdhead(BaseModel):
    num_ver = models.CharField(db_column='NUM_VER', max_length=8, blank=True, null=True)  # Field name made lowercase.
    data_ver = models.DateTimeField(db_column='DATA_VER', blank=True, null=True)  # Field name made lowercase.
    typ_dcl = models.CharField(db_column='TYP_DCL', max_length=2, blank=True, null=True)  # Field name made lowercase.
    gugtk = models.BooleanField(db_column='GUGTK', blank=True, null=True)  # Field name made lowercase.
    copy = models.BooleanField(db_column='COPY', blank=True, null=True)  # Field name made lowercase.
    dcopy = models.DateTimeField(db_column='DCOPY', blank=True, null=True)  # Field name made lowercase.
    q_edit = models.SmallIntegerField(db_column='Q_EDIT', blank=True, null=True)  # Field name made lowercase.
    d_edit = models.DateTimeField(db_column='D_EDIT', blank=True, null=True)  # Field name made lowercase.
    sol = models.SmallIntegerField(db_column='SOL', blank=True, null=True)  # Field name made lowercase.
    max_err = models.SmallIntegerField(db_column='MAX_ERR', blank=True, null=True)  # Field name made lowercase.
    dd = models.DateTimeField(db_column='DD', blank=True, null=True)  # Field name made lowercase.
    tm = models.CharField(db_column='TM', max_length=8, blank=True, null=True)  # Field name made lowercase.
    extrnl = models.CharField(db_column='EXTRNL', max_length=80, blank=True, null=True)  # Field name made lowercase.
    schet = models.CharField(db_column='SCHET', max_length=160, blank=True, null=True)  # Field name made lowercase.
    stepctrl = models.CharField(db_column='STEPCTRL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    typ_dtc = models.CharField(db_column='TYP_DTC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    vid_ktc = models.CharField(db_column='VID_KTC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    stat = models.CharField(db_column='STAT', max_length=1, blank=True, null=True)  # Field name made lowercase.
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    ui_b_1 = models.CharField(db_column='UI_B_1', max_length=8, blank=True, null=True)  # Field name made lowercase.
    ui_b_2 = models.DateTimeField(db_column='UI_B_2', blank=True, null=True)  # Field name made lowercase.
    ui_b_3 = models.CharField(db_column='UI_B_3', max_length=7, blank=True, null=True)  # Field name made lowercase.
    sds_srv = models.CharField(db_column='SDS_SRV', max_length=4, blank=True, null=True)  # Field name made lowercase.
    sds_num = models.DecimalField(default=0.00, db_column='SDS_NUM', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sds_cust = models.CharField(db_column='SDS_CUST', max_length=8, blank=True, null=True)  # Field name made lowercase.
    f_decl = models.CharField(db_column='F_DECL', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rccncode = models.CharField(db_column='RCCNCODE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    dpresent = models.DateTimeField(db_column='DPRESENT', blank=True, null=True)  # Field name made lowercase.
    tpresent = models.CharField(db_column='TPRESENT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    complectbl = models.CharField(db_column='COMPLECTBL', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g011 = models.CharField(db_column='G011', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g0121 = models.CharField(db_column='G0121', max_length=3, blank=True, null=True)  # Field name made lowercase.
    g0131 = models.CharField(db_column='G0131', max_length=3, blank=True, null=True)  # Field name made lowercase.
    k0131 = models.CharField(db_column='K0131', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g020 = models.CharField(db_column='G020', max_length=15, blank=True, null=True)  # Field name made lowercase.
    g02_itn = models.CharField(db_column='G02_ITN', max_length=13, blank=True, null=True)  # Field name made lowercase.
    g021 = models.CharField(db_column='G021', max_length=40, blank=True, null=True)  # Field name made lowercase.
    g022 = models.CharField(db_column='G022', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g023post = models.CharField(db_column='G023POST', max_length=9, blank=True, null=True)  # Field name made lowercase.
    g0231 = models.CharField(db_column='G0231', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g0231n = models.CharField(db_column='G0231N', max_length=40, blank=True, null=True)  # Field name made lowercase.
    g023subd = models.CharField(db_column='G023SUBD', max_length=120, blank=True, null=True)  # Field name made lowercase.
    g023city = models.CharField(db_column='G023CITY', max_length=120, blank=True, null=True)  # Field name made lowercase.
    g023street = models.CharField(db_column='G023STREET', max_length=120, blank=True, null=True)  # Field name made lowercase.
    g024b = models.CharField(db_column='G024B', max_length=5, blank=True, null=True)  # Field name made lowercase.
    g024n = models.CharField(db_column='G024N', max_length=10, blank=True, null=True)  # Field name made lowercase.
    g024in = models.CharField(db_column='G024IN', max_length=12, blank=True, null=True)  # Field name made lowercase.
    g027 = models.CharField(db_column='G027', max_length=12, blank=True, null=True)  # Field name made lowercase.
    g0281 = models.CharField(db_column='G0281', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g0281a = models.CharField(db_column='G0281A', max_length=15, blank=True, null=True)  # Field name made lowercase.
    g02821 = models.CharField(db_column='G02821', max_length=11, blank=True, null=True)  # Field name made lowercase.
    g02822 = models.CharField(db_column='G02822', max_length=25, blank=True, null=True)  # Field name made lowercase.
    g02823 = models.CharField(db_column='G02823', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g0283 = models.DateTimeField(db_column='G0283', blank=True, null=True)  # Field name made lowercase.
    g022a = models.CharField(db_column='G022A', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g027a = models.CharField(db_column='G027A', max_length=12, blank=True, null=True)  # Field name made lowercase.
    g023apost = models.CharField(db_column='G023APOST', max_length=9, blank=True, null=True)  # Field name made lowercase.
    g0231a = models.CharField(db_column='G0231A', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g0231an = models.CharField(db_column='G0231AN', max_length=40, blank=True, null=True)  # Field name made lowercase.
    g023asubd = models.CharField(db_column='G023ASUBD', max_length=120, blank=True, null=True)  # Field name made lowercase.
    g023acity = models.CharField(db_column='G023ACITY', max_length=120, blank=True, null=True)  # Field name made lowercase.
    g023astree = models.CharField(db_column='G023ASTREE', max_length=120, blank=True, null=True)  # Field name made lowercase.
    g029 = models.CharField(db_column='G029', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g02sm14 = models.CharField(db_column='G02SM14', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g032 = models.IntegerField(db_column='G032', blank=True, null=True)  # Field name made lowercase.
    g040 = models.IntegerField(db_column='G040', blank=True, null=True)  # Field name made lowercase.
    g04 = models.IntegerField(db_column='G04', blank=True, null=True)  # Field name made lowercase.
    g05 = models.IntegerField(db_column='G05', blank=True, null=True)  # Field name made lowercase.
    g06 = models.IntegerField(db_column='G06', blank=True, null=True)  # Field name made lowercase.
    g07 = models.CharField(db_column='G07', max_length=3, blank=True, null=True)  # Field name made lowercase.
    g080 = models.CharField(db_column='G080', max_length=15, blank=True, null=True)  # Field name made lowercase.
    g08_itn = models.CharField(db_column='G08_ITN', max_length=13, blank=True, null=True)  # Field name made lowercase.
    g081 = models.CharField(db_column='G081', max_length=40, blank=True, null=True)  # Field name made lowercase.
    g082 = models.CharField(db_column='G082', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g083post = models.CharField(db_column='G083POST', max_length=9, blank=True, null=True)  # Field name made lowercase.
    g0831 = models.CharField(db_column='G0831', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g0831a = models.CharField(db_column='G0831A', max_length=40, blank=True, null=True)  # Field name made lowercase.
    g083subd = models.CharField(db_column='G083SUBD', max_length=120, blank=True, null=True)  # Field name made lowercase.
    g083city = models.CharField(db_column='G083CITY', max_length=120, blank=True, null=True)  # Field name made lowercase.
    g083street = models.CharField(db_column='G083STREET', max_length=120, blank=True, null=True)  # Field name made lowercase.
    g084b = models.CharField(db_column='G084B', max_length=5, blank=True, null=True)  # Field name made lowercase.
    g087 = models.CharField(db_column='G087', max_length=12, blank=True, null=True)  # Field name made lowercase.
    g0881 = models.CharField(db_column='G0881', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g0881a = models.CharField(db_column='G0881A', max_length=15, blank=True, null=True)  # Field name made lowercase.
    g08821 = models.CharField(db_column='G08821', max_length=11, blank=True, null=True)  # Field name made lowercase.
    g08822 = models.CharField(db_column='G08822', max_length=25, blank=True, null=True)  # Field name made lowercase.
    g08823 = models.CharField(db_column='G08823', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g0883 = models.DateTimeField(db_column='G0883', blank=True, null=True)  # Field name made lowercase.
    g089 = models.CharField(db_column='G089', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g082a = models.CharField(db_column='G082A', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g087a = models.CharField(db_column='G087A', max_length=12, blank=True, null=True)  # Field name made lowercase.
    g083apost = models.CharField(db_column='G083APOST', max_length=9, blank=True, null=True)  # Field name made lowercase.
    g0831aa = models.CharField(db_column='G0831AA', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g0831an = models.CharField(db_column='G0831AN', max_length=40, blank=True, null=True)  # Field name made lowercase.
    g083asubd = models.CharField(db_column='G083ASUBD', max_length=120, blank=True, null=True)  # Field name made lowercase.
    g083acity = models.CharField(db_column='G083ACITY', max_length=120, blank=True, null=True)  # Field name made lowercase.
    g083astree = models.CharField(db_column='G083ASTREE', max_length=120, blank=True, null=True)  # Field name made lowercase.
    g08sm14 = models.CharField(db_column='G08SM14', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g090 = models.CharField(db_column='G090', max_length=15, blank=True, null=True)  # Field name made lowercase.
    g09_itn = models.CharField(db_column='G09_ITN', max_length=13, blank=True, null=True)  # Field name made lowercase.
    g091 = models.CharField(db_column='G091', max_length=40, blank=True, null=True)  # Field name made lowercase.
    g092 = models.CharField(db_column='G092', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g092a = models.CharField(db_column='G092A', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g093post = models.CharField(db_column='G093POST', max_length=9, blank=True, null=True)  # Field name made lowercase.
    g0931 = models.CharField(db_column='G0931', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g0931n = models.CharField(db_column='G0931N', max_length=40, blank=True, null=True)  # Field name made lowercase.
    g093subd = models.CharField(db_column='G093SUBD', max_length=120, blank=True, null=True)  # Field name made lowercase.
    g093city = models.CharField(db_column='G093CITY', max_length=120, blank=True, null=True)  # Field name made lowercase.
    g093street = models.CharField(db_column='G093STREET', max_length=120, blank=True, null=True)  # Field name made lowercase.
    g093apost = models.CharField(db_column='G093APOST', max_length=9, blank=True, null=True)  # Field name made lowercase.
    g0931a = models.CharField(db_column='G0931A', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g0931an = models.CharField(db_column='G0931AN', max_length=40, blank=True, null=True)  # Field name made lowercase.
    g093asubd = models.CharField(db_column='G093ASUBD', max_length=120, blank=True, null=True)  # Field name made lowercase.
    g093acity = models.CharField(db_column='G093ACITY', max_length=120, blank=True, null=True)  # Field name made lowercase.
    g093astree = models.CharField(db_column='G093ASTREE', max_length=120, blank=True, null=True)  # Field name made lowercase.
    g094b = models.CharField(db_column='G094B', max_length=5, blank=True, null=True)  # Field name made lowercase.
    g097 = models.CharField(db_column='G097', max_length=12, blank=True, null=True)  # Field name made lowercase.
    g097a = models.CharField(db_column='G097A', max_length=12, blank=True, null=True)  # Field name made lowercase.
    g0981 = models.CharField(db_column='G0981', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g0981a = models.CharField(db_column='G0981A', max_length=15, blank=True, null=True)  # Field name made lowercase.
    g09821 = models.CharField(db_column='G09821', max_length=11, blank=True, null=True)  # Field name made lowercase.
    g09822 = models.CharField(db_column='G09822', max_length=25, blank=True, null=True)  # Field name made lowercase.
    g09823 = models.CharField(db_column='G09823', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g0983 = models.DateTimeField(db_column='G0983', blank=True, null=True)  # Field name made lowercase.
    g09sm14 = models.CharField(db_column='G09SM14', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g11 = models.CharField(db_column='G11', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g12 = models.DecimalField(default=0.00, db_column='G12', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    g121 = models.CharField(db_column='G121', max_length=3, blank=True, null=True)  # Field name made lowercase.
    g122 = models.DecimalField(default=0.00, db_column='G122', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    g140 = models.CharField(db_column='G140', max_length=15, blank=True, null=True)  # Field name made lowercase.
    g14_itn = models.CharField(db_column='G14_ITN', max_length=13, blank=True, null=True)  # Field name made lowercase.
    g141 = models.CharField(db_column='G141', max_length=40, blank=True, null=True)  # Field name made lowercase.
    g142 = models.CharField(db_column='G142', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g142a = models.CharField(db_column='G142A', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g143post = models.CharField(db_column='G143POST', max_length=9, blank=True, null=True)  # Field name made lowercase.
    g1431 = models.CharField(db_column='G1431', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g1431n = models.CharField(db_column='G1431N', max_length=40, blank=True, null=True)  # Field name made lowercase.
    g143subd = models.CharField(db_column='G143SUBD', max_length=120, blank=True, null=True)  # Field name made lowercase.
    g143city = models.CharField(db_column='G143CITY', max_length=120, blank=True, null=True)  # Field name made lowercase.
    g143street = models.CharField(db_column='G143STREET', max_length=120, blank=True, null=True)  # Field name made lowercase.
    g143apost = models.CharField(db_column='G143APOST', max_length=9, blank=True, null=True)  # Field name made lowercase.
    g1431a = models.CharField(db_column='G1431A', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g1431an = models.CharField(db_column='G1431AN', max_length=40, blank=True, null=True)  # Field name made lowercase.
    g143asubd = models.CharField(db_column='G143ASUBD', max_length=120, blank=True, null=True)  # Field name made lowercase.
    g143acity = models.CharField(db_column='G143ACITY', max_length=120, blank=True, null=True)  # Field name made lowercase.
    g143astree = models.CharField(db_column='G143ASTREE', max_length=120, blank=True, null=True)  # Field name made lowercase.
    g144b = models.CharField(db_column='G144B', max_length=5, blank=True, null=True)  # Field name made lowercase.
    g147 = models.CharField(db_column='G147', max_length=12, blank=True, null=True)  # Field name made lowercase.
    g147a = models.CharField(db_column='G147A', max_length=12, blank=True, null=True)  # Field name made lowercase.
    g1481 = models.CharField(db_column='G1481', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g1481a = models.CharField(db_column='G1481A', max_length=15, blank=True, null=True)  # Field name made lowercase.
    g14821 = models.CharField(db_column='G14821', max_length=11, blank=True, null=True)  # Field name made lowercase.
    g14822 = models.CharField(db_column='G14822', max_length=25, blank=True, null=True)  # Field name made lowercase.
    g14823 = models.CharField(db_column='G14823', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g1483 = models.DateTimeField(db_column='G1483', blank=True, null=True)  # Field name made lowercase.
    g15 = models.CharField(db_column='G15', max_length=40, blank=True, null=True)  # Field name made lowercase.
    g15a = models.CharField(db_column='G15A', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g16 = models.CharField(db_column='G16', max_length=40, blank=True, null=True)  # Field name made lowercase.
    g17a = models.CharField(db_column='G17A', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g17b = models.CharField(db_column='G17B', max_length=40, blank=True, null=True)  # Field name made lowercase.
    g180 = models.IntegerField(db_column='G180', blank=True, null=True)  # Field name made lowercase.
    g182 = models.CharField(db_column='G182', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g19 = models.CharField(db_column='G19', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g202 = models.CharField(db_column='G202', max_length=3, blank=True, null=True)  # Field name made lowercase.
    g2021 = models.CharField(db_column='G2021', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g203 = models.CharField(db_column='G203', max_length=250, blank=True, null=True)  # Field name made lowercase.
    g210 = models.IntegerField(db_column='G210', blank=True, null=True)  # Field name made lowercase.
    g212 = models.CharField(db_column='G212', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g221 = models.CharField(db_column='G221', max_length=3, blank=True, null=True)  # Field name made lowercase.
    g222 = models.DecimalField(default=0.00, db_column='G222', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    g23 = models.FloatField(default=0.00, db_column='G23', blank=True, null=True)  # Field name made lowercase.
    g230 = models.DateTimeField(db_column='G230', blank=True, null=True)  # Field name made lowercase.
    g270 = models.CharField(db_column='G270', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g27_itn = models.CharField(db_column='G27_ITN', max_length=13, blank=True, null=True)  # Field name made lowercase.
    g2710 = models.CharField(db_column='G2710', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g271 = models.CharField(db_column='G271', max_length=21, blank=True, null=True)  # Field name made lowercase.
    g27 = models.CharField(db_column='G27', max_length=40, blank=True, null=True)  # Field name made lowercase.
    g2711 = models.DateTimeField(db_column='G2711', blank=True, null=True)  # Field name made lowercase.
    g2712 = models.CharField(db_column='G2712', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g28_itn = models.CharField(db_column='G28_ITN', max_length=13, blank=True, null=True)  # Field name made lowercase.
    g28okpo = models.CharField(db_column='G28OKPO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    g28inn = models.CharField(db_column='G28INN', max_length=12, blank=True, null=True)  # Field name made lowercase.
    g281oth = models.CharField(db_column='G281OTH', max_length=30, blank=True, null=True)  # Field name made lowercase.
    g28zajmn = models.CharField(db_column='G28ZAJMN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g282 = models.CharField(db_column='G282', max_length=70, blank=True, null=True)  # Field name made lowercase.
    g28211 = models.CharField(db_column='G28211', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g28212 = models.CharField(db_column='G28212', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g28221 = models.CharField(db_column='G28221', max_length=3, blank=True, null=True)  # Field name made lowercase.
    g28222 = models.CharField(db_column='G28222', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g28230 = models.CharField(db_column='G28230', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g2823 = models.DateTimeField(db_column='G2823', blank=True, null=True)  # Field name made lowercase.
    g28240 = models.CharField(db_column='G28240', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g2824 = models.DateTimeField(db_column='G2824', blank=True, null=True)  # Field name made lowercase.
    g2825 = models.CharField(db_column='G2825', max_length=3, blank=True, null=True)  # Field name made lowercase.
    g30_itn = models.CharField(db_column='G30_ITN', max_length=13, blank=True, null=True)  # Field name made lowercase.
    g300 = models.CharField(db_column='G300', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g3010 = models.CharField(db_column='G3010', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g301 = models.CharField(db_column='G301', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g3011 = models.DateTimeField(db_column='G3011', blank=True, null=True)  # Field name made lowercase.
    g30 = models.CharField(db_column='G30', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g30post = models.CharField(db_column='G30POST', max_length=9, blank=True, null=True)  # Field name made lowercase.
    g30a = models.CharField(db_column='G30A', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g30an = models.CharField(db_column='G30AN', max_length=40, blank=True, null=True)  # Field name made lowercase.
    g30subd = models.CharField(db_column='G30SUBD', max_length=120, blank=True, null=True)  # Field name made lowercase.
    g30city = models.CharField(db_column='G30CITY', max_length=120, blank=True, null=True)  # Field name made lowercase.
    g30street = models.CharField(db_column='G30STREET', max_length=120, blank=True, null=True)  # Field name made lowercase.
    g30lname = models.CharField(db_column='G30LNAME', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g3012 = models.CharField(db_column='G3012', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g30121 = models.CharField(db_column='G30121', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g30122 = models.CharField(db_column='G30122', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g45a1 = models.CharField(db_column='G45A1', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g45a2 = models.CharField(db_column='G45A2', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g45a3 = models.CharField(db_column='G45A3', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g45a4 = models.CharField(db_column='G45A4', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g45a5 = models.CharField(db_column='G45A5', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g45a6 = models.CharField(db_column='G45A6', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g45a7 = models.CharField(db_column='G45A7', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g45a8 = models.CharField(db_column='G45A8', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g53_ztk = models.CharField(db_column='G53_ZTK', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g53_dt = models.CharField(db_column='G53_DT', max_length=250, blank=True, null=True)  # Field name made lowercase.
    g53_dn = models.CharField(db_column='G53_DN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g53_dd = models.DateTimeField(db_column='G53_DD', blank=True, null=True)  # Field name made lowercase.
    g53_pos = models.CharField(db_column='G53_POS', max_length=9, blank=True, null=True)  # Field name made lowercase.
    g53_cc = models.CharField(db_column='G53_CC', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g53_cn = models.CharField(db_column='G53_CN', max_length=40, blank=True, null=True)  # Field name made lowercase.
    g53_sub = models.CharField(db_column='G53_SUB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g53_cit = models.CharField(db_column='G53_CIT', max_length=35, blank=True, null=True)  # Field name made lowercase.
    g53_str = models.CharField(db_column='G53_STR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    d54_itn = models.CharField(db_column='D54_ITN', max_length=13, blank=True, null=True)  # Field name made lowercase.
    d5410 = models.CharField(db_column='D5410', max_length=1, blank=True, null=True)  # Field name made lowercase.
    d541 = models.CharField(db_column='D541', max_length=14, blank=True, null=True)  # Field name made lowercase.
    d541d = models.DateTimeField(db_column='D541D', blank=True, null=True)  # Field name made lowercase.
    d5411 = models.CharField(db_column='D5411', max_length=50, blank=True, null=True)  # Field name made lowercase.
    d5411d = models.DateTimeField(db_column='D5411D', blank=True, null=True)  # Field name made lowercase.
    d541_inn = models.CharField(db_column='D541_INN', max_length=12, blank=True, null=True)  # Field name made lowercase.
    d541_kpp = models.CharField(db_column='D541_KPP', max_length=9, blank=True, null=True)  # Field name made lowercase.
    d542 = models.DateTimeField(db_column='D542', blank=True, null=True)  # Field name made lowercase.
    d5441 = models.CharField(db_column='D5441', max_length=150, blank=True, null=True)  # Field name made lowercase.
    d5441nm = models.CharField(db_column='D5441NM', max_length=150, blank=True, null=True)  # Field name made lowercase.
    d5441mdnm = models.CharField(db_column='D5441MDNM', max_length=150, blank=True, null=True)  # Field name made lowercase.
    d5442 = models.CharField(db_column='D5442', max_length=50, blank=True, null=True)  # Field name made lowercase.
    d5443 = models.CharField(db_column='D5443', max_length=250, blank=True, null=True)  # Field name made lowercase.
    d5444 = models.CharField(db_column='D5444', max_length=50, blank=True, null=True)  # Field name made lowercase.
    d5445 = models.DateTimeField(db_column='D5445', blank=True, null=True)  # Field name made lowercase.
    d5446 = models.DateTimeField(db_column='D5446', blank=True, null=True)  # Field name made lowercase.
    d5447 = models.CharField(db_column='D5447', max_length=50, blank=True, null=True)  # Field name made lowercase.
    d5451 = models.CharField(db_column='D5451', max_length=2, blank=True, null=True)  # Field name made lowercase.
    d5451a = models.CharField(db_column='D5451A', max_length=15, blank=True, null=True)  # Field name made lowercase.
    d54521 = models.CharField(db_column='D54521', max_length=11, blank=True, null=True)  # Field name made lowercase.
    d54522 = models.CharField(db_column='D54522', max_length=25, blank=True, null=True)  # Field name made lowercase.
    d54523 = models.CharField(db_column='D54523', max_length=150, blank=True, null=True)  # Field name made lowercase.
    d5453 = models.DateTimeField(db_column='D5453', blank=True, null=True)  # Field name made lowercase.
    g54_itn = models.CharField(db_column='G54_ITN', max_length=13, blank=True, null=True)  # Field name made lowercase.
    g5410 = models.CharField(db_column='G5410', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g541 = models.CharField(db_column='G541', max_length=14, blank=True, null=True)  # Field name made lowercase.
    g541d = models.DateTimeField(db_column='G541D', blank=True, null=True)  # Field name made lowercase.
    g5411 = models.CharField(db_column='G5411', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g5411d = models.DateTimeField(db_column='G5411D', blank=True, null=True)  # Field name made lowercase.
    g541_inn = models.CharField(db_column='G541_INN', max_length=12, blank=True, null=True)  # Field name made lowercase.
    g541_kpp = models.CharField(db_column='G541_KPP', max_length=9, blank=True, null=True)  # Field name made lowercase.
    g542 = models.DateTimeField(db_column='G542', blank=True, null=True)  # Field name made lowercase.
    g5441 = models.CharField(db_column='G5441', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g5441nm = models.CharField(db_column='G5441NM', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g5441mdnm = models.CharField(db_column='G5441MDNM', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g5442 = models.CharField(db_column='G5442', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g5443 = models.CharField(db_column='G5443', max_length=250, blank=True, null=True)  # Field name made lowercase.
    g5444 = models.CharField(db_column='G5444', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g5445 = models.DateTimeField(db_column='G5445', blank=True, null=True)  # Field name made lowercase.
    g5446 = models.DateTimeField(db_column='G5446', blank=True, null=True)  # Field name made lowercase.
    g5447 = models.CharField(db_column='G5447', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g5451 = models.CharField(db_column='G5451', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g5451a = models.CharField(db_column='G5451A', max_length=15, blank=True, null=True)  # Field name made lowercase.
    g54521 = models.CharField(db_column='G54521', max_length=11, blank=True, null=True)  # Field name made lowercase.
    g54522 = models.CharField(db_column='G54522', max_length=25, blank=True, null=True)  # Field name made lowercase.
    g54523 = models.CharField(db_column='G54523', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g5453 = models.DateTimeField(db_column='G5453', blank=True, null=True)  # Field name made lowercase.
    gd0 = models.CharField(db_column='GD0', max_length=2, blank=True, null=True)  # Field name made lowercase.
    gd1 = models.DateTimeField(db_column='GD1', blank=True, null=True)  # Field name made lowercase.
    gd11 = models.CharField(db_column='GD11', max_length=8, blank=True, null=True)  # Field name made lowercase.
    gd2 = models.CharField(db_column='GD2', max_length=4, blank=True, null=True)  # Field name made lowercase.
    gd2fio = models.CharField(db_column='GD2FIO', max_length=150, blank=True, null=True)  # Field name made lowercase.
    gd00 = models.CharField(db_column='GD00', max_length=250, blank=True, null=True)  # Field name made lowercase.
    gddf = models.DateTimeField(db_column='GDDF', blank=True, null=True)  # Field name made lowercase.
    recplatv = models.IntegerField(db_column='RECPLATV', blank=True, null=True)  # Field name made lowercase.
    recslotm = models.IntegerField(db_column='RECSLOTM', blank=True, null=True)  # Field name made lowercase.
    rectrans = models.IntegerField(db_column='RECTRANS', blank=True, null=True)  # Field name made lowercase.
    recsumpp = models.IntegerField(db_column='RECSUMPP', blank=True, null=True)  # Field name made lowercase.
    recpasp = models.IntegerField(db_column='RECPASP', blank=True, null=True)  # Field name made lowercase.
    dmodify = models.DateTimeField(db_column='DMODIFY', blank=True, null=True)  # Field name made lowercase.
    tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    edoc_guid = models.CharField(db_column='EDOC_GUID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    edoc_id = models.DecimalField(default=0.00, db_column='EDOC_ID', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    p_status1 = models.SmallIntegerField(db_column='P_STATUS1', blank=True, null=True)  # Field name made lowercase.
    p_status2 = models.SmallIntegerField(db_column='P_STATUS2', blank=True, null=True)  # Field name made lowercase.
    docid = models.CharField(db_column='DOCID', max_length=38, blank=True, null=True)  # Field name made lowercase.
    num_pp = models.SmallIntegerField(db_column='NUM_PP', blank=True, null=True)  # Field name made lowercase.
    g541dn = models.CharField(db_column='G541DN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g54place = models.CharField(db_column='G54PLACE', max_length=35, blank=True, null=True)  # Field name made lowercase.
    g50rw = models.CharField(db_column='G50RW', max_length=5, blank=True, null=True)  # Field name made lowercase.
    drv41 = models.CharField(db_column='DRV41', max_length=150, blank=True, null=True)  # Field name made lowercase.
    drv41nm = models.CharField(db_column='DRV41NM', max_length=150, blank=True, null=True)  # Field name made lowercase.
    drv41mdnm = models.CharField(db_column='DRV41MDNM', max_length=150, blank=True, null=True)  # Field name made lowercase.
    drv47 = models.CharField(db_column='DRV47', max_length=50, blank=True, null=True)  # Field name made lowercase.
    drv4cc = models.CharField(db_column='DRV4CC', max_length=2, blank=True, null=True)  # Field name made lowercase.
    drv51 = models.CharField(db_column='DRV51', max_length=7, blank=True, null=True)  # Field name made lowercase.
    drv51a = models.CharField(db_column='DRV51A', max_length=15, blank=True, null=True)  # Field name made lowercase.
    drv521 = models.CharField(db_column='DRV521', max_length=11, blank=True, null=True)  # Field name made lowercase.
    drv522 = models.CharField(db_column='DRV522', max_length=25, blank=True, null=True)  # Field name made lowercase.
    drv523 = models.CharField(db_column='DRV523', max_length=150, blank=True, null=True)  # Field name made lowercase.
    drv53 = models.DateTimeField(db_column='DRV53', blank=True, null=True)  # Field name made lowercase.
    act_tp = models.CharField(db_column='ACT_TP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.
    g023build = models.CharField(db_column='G023BUILD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g023abuild = models.CharField(db_column='G023ABUILD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g083build = models.CharField(db_column='G083BUILD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g083abuild = models.CharField(db_column='G083ABUILD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g093build = models.CharField(db_column='G093BUILD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g093abuild = models.CharField(db_column='G093ABUILD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g143build = models.CharField(db_column='G143BUILD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    aeorowner = models.CharField(db_column='AEOROWNER', max_length=1, blank=True, null=True)  # Field name made lowercase.
    aeocntry = models.CharField(db_column='AEOCNTRY', max_length=2, blank=True, null=True)  # Field name made lowercase.
    aeonum = models.CharField(db_column='AEONUM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    aeokind = models.CharField(db_column='AEOKIND', max_length=1, blank=True, null=True)  # Field name made lowercase.
    aeoregcod = models.CharField(db_column='AEOREGCOD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    g143abuild = models.CharField(db_column='G143ABUILD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g16a = models.CharField(db_column='G16A', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g30aeoown = models.CharField(db_column='G30AEOOWN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g30aeocntr = models.CharField(db_column='G30AEOCNTR', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g30aeokind = models.CharField(db_column='G30AEOKIND', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g30aeorcod = models.CharField(db_column='G30AEORCOD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    g30d = models.DateTimeField(db_column='G30D', blank=True, null=True)  # Field name made lowercase.
    g30dd = models.DateTimeField(db_column='G30DD', blank=True, null=True)  # Field name made lowercase.
    g30build = models.CharField(db_column='G30BUILD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g542t = models.CharField(db_column='G542T', max_length=8, blank=True, null=True)  # Field name made lowercase.
    drv241 = models.CharField(db_column='DRV241', max_length=150, blank=True, null=True)  # Field name made lowercase.
    drv241nm = models.CharField(db_column='DRV241NM', max_length=150, blank=True, null=True)  # Field name made lowercase.
    drv241mdnm = models.CharField(db_column='DRV241MDNM', max_length=150, blank=True, null=True)  # Field name made lowercase.
    drv247 = models.CharField(db_column='DRV247', max_length=50, blank=True, null=True)  # Field name made lowercase.
    drv24cc = models.CharField(db_column='DRV24CC', max_length=2, blank=True, null=True)  # Field name made lowercase.
    drv251 = models.CharField(db_column='DRV251', max_length=7, blank=True, null=True)  # Field name made lowercase.
    drv251a = models.CharField(db_column='DRV251A', max_length=15, blank=True, null=True)  # Field name made lowercase.
    drv2521 = models.CharField(db_column='DRV2521', max_length=11, blank=True, null=True)  # Field name made lowercase.
    drv2522 = models.CharField(db_column='DRV2522', max_length=25, blank=True, null=True)  # Field name made lowercase.
    drv2523 = models.CharField(db_column='DRV2523', max_length=150, blank=True, null=True)  # Field name made lowercase.
    drv253 = models.DateTimeField(db_column='DRV253', blank=True, null=True)  # Field name made lowercase.
    g12zpk = models.DecimalField(default=0.00, db_column='G12ZPK', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    g22zpk = models.DecimalField(default=0.00, db_column='G22ZPK', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    g542time = models.CharField(db_column='G542TIME', max_length=14, blank=True, null=True)  # Field name made lowercase.
    g02phone = models.CharField(db_column='G02PHONE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g02email = models.CharField(db_column='G02EMAIL', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g08phone = models.CharField(db_column='G08PHONE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g08email = models.CharField(db_column='G08EMAIL', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g09phone = models.CharField(db_column='G09PHONE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g09email = models.CharField(db_column='G09EMAIL', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g14phone = models.CharField(db_column='G14PHONE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g14email = models.CharField(db_column='G14EMAIL', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g54532 = models.DateTimeField(db_column='G54532', blank=True, null=True)  # Field name made lowercase.
    g54email = models.CharField(db_column='G54EMAIL', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g0132 = models.CharField(db_column='G0132', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g023room = models.CharField(db_column='G023ROOM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    g023typ = models.CharField(db_column='G023TYP', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g023aroom = models.CharField(db_column='G023AROOM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    g023atyp = models.CharField(db_column='G023ATYP', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g083room = models.CharField(db_column='G083ROOM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    g083typ = models.CharField(db_column='G083TYP', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g083aroom = models.CharField(db_column='G083AROOM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    g083atyp = models.CharField(db_column='G083ATYP', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g093room = models.CharField(db_column='G093ROOM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    g093typ = models.CharField(db_column='G093TYP', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g093aroom = models.CharField(db_column='G093AROOM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    g093atyp = models.CharField(db_column='G093ATYP', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g143room = models.CharField(db_column='G143ROOM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    g143typ = models.CharField(db_column='G143TYP', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g143aroom = models.CharField(db_column='G143AROOM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    g143atyp = models.CharField(db_column='G143ATYP', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g30room = models.CharField(db_column='G30ROOM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    g30typ = models.CharField(db_column='G30TYP', max_length=1, blank=True, null=True)  # Field name made lowercase.
    gd1kdt = models.DateTimeField(db_column='GD1KDT', blank=True, null=True)  # Field name made lowercase.
    gd11kdt = models.CharField(db_column='GD11KDT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    seal_plm = models.CharField(db_column='SEAL_PLM', max_length=250, blank=True, null=True)  # Field name made lowercase.
    seal_qty = models.SmallIntegerField(db_column='SEAL_QTY', blank=True, null=True)  # Field name made lowercase.
    seal_id = models.CharField(db_column='SEAL_ID', max_length=250, blank=True, null=True)  # Field name made lowercase.
    seal_decr = models.CharField(db_column='SEAL_DECR', max_length=250, blank=True, null=True)  # Field name made lowercase.
    kz_cust = models.CharField(db_column='KZ_CUST', max_length=8, blank=True, null=True)  # Field name made lowercase.
    kz_sec = models.CharField(db_column='KZ_SEC', max_length=6, blank=True, null=True)  # Field name made lowercase.
    kz_wto = models.CharField(db_column='KZ_WTO', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'KTDHEAD'


# class _Ktdhead(BaseModel):
#     num_ver = models.CharField(db_column='NUM_VER', max_length=8, blank=True, null=True)  # Field name made lowercase.
#     data_ver = models.DateTimeField(db_column='DATA_VER', blank=True, null=True)  # Field name made lowercase.
#     typ_dcl = models.CharField(db_column='TYP_DCL', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     gugtk = models.BooleanField(db_column='GUGTK', blank=True, null=True)  # Field name made lowercase.
#     copy = models.BooleanField(db_column='COPY', blank=True, null=True)  # Field name made lowercase.
#     dcopy = models.DateTimeField(db_column='DCOPY', blank=True, null=True)  # Field name made lowercase.
#     q_edit = models.SmallIntegerField(db_column='Q_EDIT', blank=True, null=True)  # Field name made lowercase.
#     d_edit = models.DateTimeField(db_column='D_EDIT', blank=True, null=True)  # Field name made lowercase.
#     sol = models.SmallIntegerField(db_column='SOL', blank=True, null=True)  # Field name made lowercase.
#     max_err = models.SmallIntegerField(db_column='MAX_ERR', blank=True, null=True)  # Field name made lowercase.
#     dd = models.DateTimeField(db_column='DD', blank=True, null=True)  # Field name made lowercase.
#     tm = models.CharField(db_column='TM', max_length=8, blank=True, null=True)  # Field name made lowercase.
#     extrnl = models.CharField(db_column='EXTRNL', max_length=80, blank=True, null=True)  # Field name made lowercase.
#     schet = models.CharField(db_column='SCHET', max_length=160, blank=True, null=True)  # Field name made lowercase.
#     stepctrl = models.CharField(db_column='STEPCTRL', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     typ_dtc = models.CharField(db_column='TYP_DTC', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     vid_ktc = models.CharField(db_column='VID_KTC', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     stat = models.CharField(db_column='STAT', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
#     g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
#     g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
#     ui_b_1 = models.CharField(db_column='UI_B_1', max_length=8, blank=True, null=True)  # Field name made lowercase.
#     ui_b_2 = models.DateTimeField(db_column='UI_B_2', blank=True, null=True)  # Field name made lowercase.
#     ui_b_3 = models.CharField(db_column='UI_B_3', max_length=7, blank=True, null=True)  # Field name made lowercase.
#     sds_srv = models.CharField(db_column='SDS_SRV', max_length=4, blank=True, null=True)  # Field name made lowercase.
#     sds_num = models.DecimalField(default=0.00, db_column='SDS_NUM', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
#     sds_cust = models.CharField(db_column='SDS_CUST', max_length=8, blank=True, null=True)  # Field name made lowercase.
#     f_decl = models.CharField(db_column='F_DECL', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     rccncode = models.CharField(db_column='RCCNCODE', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     dpresent = models.DateTimeField(db_column='DPRESENT', blank=True, null=True)  # Field name made lowercase.
#     tpresent = models.CharField(db_column='TPRESENT', max_length=8, blank=True, null=True)  # Field name made lowercase.
#     complectbl = models.CharField(db_column='COMPLECTBL', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     g011 = models.CharField(db_column='G011', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     g0121 = models.CharField(db_column='G0121', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     g0131 = models.CharField(db_column='G0131', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     k0131 = models.CharField(db_column='K0131', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     g020 = models.CharField(db_column='G020', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     g02_itn = models.CharField(db_column='G02_ITN', max_length=13, blank=True, null=True)  # Field name made lowercase.
#     g021 = models.CharField(db_column='G021', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     g022 = models.CharField(db_column='G022', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     g023post = models.CharField(db_column='G023POST', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     g0231 = models.CharField(db_column='G0231', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     g0231n = models.CharField(db_column='G0231N', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     g023subd = models.CharField(db_column='G023SUBD', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g023city = models.CharField(db_column='G023CITY', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     g023street = models.CharField(db_column='G023STREET', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g024b = models.CharField(db_column='G024B', max_length=5, blank=True, null=True)  # Field name made lowercase.
#     g024n = models.CharField(db_column='G024N', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     g024in = models.CharField(db_column='G024IN', max_length=12, blank=True, null=True)  # Field name made lowercase.
#     g027 = models.CharField(db_column='G027', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     g0281 = models.CharField(db_column='G0281', max_length=7, blank=True, null=True)  # Field name made lowercase.
#     g0281a = models.CharField(db_column='G0281A', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     g02821 = models.CharField(db_column='G02821', max_length=11, blank=True, null=True)  # Field name made lowercase.
#     g02822 = models.CharField(db_column='G02822', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     g02823 = models.CharField(db_column='G02823', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     g0283 = models.DateTimeField(db_column='G0283', blank=True, null=True)  # Field name made lowercase.
#     g022a = models.CharField(db_column='G022A', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     g027a = models.CharField(db_column='G027A', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     g023apost = models.CharField(db_column='G023APOST', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     g0231a = models.CharField(db_column='G0231A', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     g0231an = models.CharField(db_column='G0231AN', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     g023asubd = models.CharField(db_column='G023ASUBD', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g023acity = models.CharField(db_column='G023ACITY', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     g023astree = models.CharField(db_column='G023ASTREE', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g029 = models.CharField(db_column='G029', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     g02sm14 = models.CharField(db_column='G02SM14', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     g032 = models.IntegerField(db_column='G032', blank=True, null=True)  # Field name made lowercase.
#     g040 = models.IntegerField(db_column='G040', blank=True, null=True)  # Field name made lowercase.
#     g04 = models.IntegerField(db_column='G04', blank=True, null=True)  # Field name made lowercase.
#     g05 = models.IntegerField(db_column='G05', blank=True, null=True)  # Field name made lowercase.
#     g06 = models.IntegerField(db_column='G06', blank=True, null=True)  # Field name made lowercase.
#     g07 = models.CharField(db_column='G07', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     g080 = models.CharField(db_column='G080', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     g08_itn = models.CharField(db_column='G08_ITN', max_length=13, blank=True, null=True)  # Field name made lowercase.
#     g081 = models.CharField(db_column='G081', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     g082 = models.CharField(db_column='G082', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     g083post = models.CharField(db_column='G083POST', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     g0831 = models.CharField(db_column='G0831', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     g0831a = models.CharField(db_column='G0831A', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     g083subd = models.CharField(db_column='G083SUBD', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g083city = models.CharField(db_column='G083CITY', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     g083street = models.CharField(db_column='G083STREET', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g084b = models.CharField(db_column='G084B', max_length=5, blank=True, null=True)  # Field name made lowercase.
#     g087 = models.CharField(db_column='G087', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     g0881 = models.CharField(db_column='G0881', max_length=7, blank=True, null=True)  # Field name made lowercase.
#     g0881a = models.CharField(db_column='G0881A', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     g08821 = models.CharField(db_column='G08821', max_length=11, blank=True, null=True)  # Field name made lowercase.
#     g08822 = models.CharField(db_column='G08822', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     g08823 = models.CharField(db_column='G08823', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     g0883 = models.DateTimeField(db_column='G0883', blank=True, null=True)  # Field name made lowercase.
#     g089 = models.CharField(db_column='G089', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     g082a = models.CharField(db_column='G082A', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     g087a = models.CharField(db_column='G087A', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     g083apost = models.CharField(db_column='G083APOST', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     g0831aa = models.CharField(db_column='G0831AA', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     g0831an = models.CharField(db_column='G0831AN', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     g083asubd = models.CharField(db_column='G083ASUBD', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g083acity = models.CharField(db_column='G083ACITY', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     g083astree = models.CharField(db_column='G083ASTREE', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g08sm14 = models.CharField(db_column='G08SM14', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     g090 = models.CharField(db_column='G090', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     g09_itn = models.CharField(db_column='G09_ITN', max_length=13, blank=True, null=True)  # Field name made lowercase.
#     g091 = models.CharField(db_column='G091', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     g092 = models.CharField(db_column='G092', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     g092a = models.CharField(db_column='G092A', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     g093post = models.CharField(db_column='G093POST', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     g0931 = models.CharField(db_column='G0931', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     g0931n = models.CharField(db_column='G0931N', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     g093subd = models.CharField(db_column='G093SUBD', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g093city = models.CharField(db_column='G093CITY', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     g093street = models.CharField(db_column='G093STREET', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g093apost = models.CharField(db_column='G093APOST', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     g0931a = models.CharField(db_column='G0931A', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     g0931an = models.CharField(db_column='G0931AN', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     g093asubd = models.CharField(db_column='G093ASUBD', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g093acity = models.CharField(db_column='G093ACITY', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     g093astree = models.CharField(db_column='G093ASTREE', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g094b = models.CharField(db_column='G094B', max_length=5, blank=True, null=True)  # Field name made lowercase.
#     g097 = models.CharField(db_column='G097', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     g097a = models.CharField(db_column='G097A', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     g0981 = models.CharField(db_column='G0981', max_length=7, blank=True, null=True)  # Field name made lowercase.
#     g0981a = models.CharField(db_column='G0981A', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     g09821 = models.CharField(db_column='G09821', max_length=11, blank=True, null=True)  # Field name made lowercase.
#     g09822 = models.CharField(db_column='G09822', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     g09823 = models.CharField(db_column='G09823', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     g0983 = models.DateTimeField(db_column='G0983', blank=True, null=True)  # Field name made lowercase.
#     g09sm14 = models.CharField(db_column='G09SM14', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     g11 = models.CharField(db_column='G11', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     g12 = models.DecimalField(default=0.00, db_column='G12', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
#     g121 = models.CharField(db_column='G121', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     g122 = models.DecimalField(default=0.00, db_column='G122', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
#     g140 = models.CharField(db_column='G140', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     g14_itn = models.CharField(db_column='G14_ITN', max_length=13, blank=True, null=True)  # Field name made lowercase.
#     g141 = models.CharField(db_column='G141', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     g142 = models.CharField(db_column='G142', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     g142a = models.CharField(db_column='G142A', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     g143post = models.CharField(db_column='G143POST', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     g1431 = models.CharField(db_column='G1431', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     g1431n = models.CharField(db_column='G1431N', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     g143subd = models.CharField(db_column='G143SUBD', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g143city = models.CharField(db_column='G143CITY', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     g143street = models.CharField(db_column='G143STREET', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g143apost = models.CharField(db_column='G143APOST', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     g1431a = models.CharField(db_column='G1431A', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     g1431an = models.CharField(db_column='G1431AN', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     g143asubd = models.CharField(db_column='G143ASUBD', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g143acity = models.CharField(db_column='G143ACITY', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     g143astree = models.CharField(db_column='G143ASTREE', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g144b = models.CharField(db_column='G144B', max_length=5, blank=True, null=True)  # Field name made lowercase.
#     g147 = models.CharField(db_column='G147', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     g147a = models.CharField(db_column='G147A', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     g1481 = models.CharField(db_column='G1481', max_length=7, blank=True, null=True)  # Field name made lowercase.
#     g1481a = models.CharField(db_column='G1481A', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     g14821 = models.CharField(db_column='G14821', max_length=11, blank=True, null=True)  # Field name made lowercase.
#     g14822 = models.CharField(db_column='G14822', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     g14823 = models.CharField(db_column='G14823', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     g1483 = models.DateTimeField(db_column='G1483', blank=True, null=True)  # Field name made lowercase.
#     g15 = models.CharField(db_column='G15', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     g15a = models.CharField(db_column='G15A', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     g16 = models.CharField(db_column='G16', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     g17a = models.CharField(db_column='G17A', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     g17b = models.CharField(db_column='G17B', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     g180 = models.IntegerField(db_column='G180', blank=True, null=True)  # Field name made lowercase.
#     g182 = models.CharField(db_column='G182', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     g19 = models.CharField(db_column='G19', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     g202 = models.CharField(db_column='G202', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     g2021 = models.CharField(db_column='G2021', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     g203 = models.CharField(db_column='G203', max_length=250, blank=True, null=True)  # Field name made lowercase.
#     g210 = models.IntegerField(db_column='G210', blank=True, null=True)  # Field name made lowercase.
#     g212 = models.CharField(db_column='G212', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     g221 = models.CharField(db_column='G221', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     g222 = models.DecimalField(default=0.00, db_column='G222', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
#     g23 = models.FloatField(default=0.00, db_column='G23', blank=True, null=True)  # Field name made lowercase.
#     g230 = models.DateTimeField(db_column='G230', blank=True, null=True)  # Field name made lowercase.
#     g270 = models.CharField(db_column='G270', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     g27_itn = models.CharField(db_column='G27_ITN', max_length=13, blank=True, null=True)  # Field name made lowercase.
#     g2710 = models.CharField(db_column='G2710', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     g271 = models.CharField(db_column='G271', max_length=21, blank=True, null=True)  # Field name made lowercase.
#     g27 = models.CharField(db_column='G27', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     g2711 = models.DateTimeField(db_column='G2711', blank=True, null=True)  # Field name made lowercase.
#     g2712 = models.CharField(db_column='G2712', max_length=8, blank=True, null=True)  # Field name made lowercase.
#     g28_itn = models.CharField(db_column='G28_ITN', max_length=13, blank=True, null=True)  # Field name made lowercase.
#     g28okpo = models.CharField(db_column='G28OKPO', max_length=10, blank=True, null=True)  # Field name made lowercase.
#     g28inn = models.CharField(db_column='G28INN', max_length=12, blank=True, null=True)  # Field name made lowercase.
#     g281oth = models.CharField(db_column='G281OTH', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     g28zajmn = models.CharField(db_column='G28ZAJMN', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g282 = models.CharField(db_column='G282', max_length=70, blank=True, null=True)  # Field name made lowercase.
#     g28211 = models.CharField(db_column='G28211', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     g28212 = models.CharField(db_column='G28212', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     g28221 = models.CharField(db_column='G28221', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     g28222 = models.CharField(db_column='G28222', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     g28230 = models.CharField(db_column='G28230', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     g2823 = models.DateTimeField(db_column='G2823', blank=True, null=True)  # Field name made lowercase.
#     g28240 = models.CharField(db_column='G28240', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     g2824 = models.DateTimeField(db_column='G2824', blank=True, null=True)  # Field name made lowercase.
#     g2825 = models.CharField(db_column='G2825', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     g30_itn = models.CharField(db_column='G30_ITN', max_length=13, blank=True, null=True)  # Field name made lowercase.
#     g300 = models.CharField(db_column='G300', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     g3010 = models.CharField(db_column='G3010', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     g301 = models.CharField(db_column='G301', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g3011 = models.DateTimeField(db_column='G3011', blank=True, null=True)  # Field name made lowercase.
#     g30 = models.CharField(db_column='G30', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g30post = models.CharField(db_column='G30POST', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     g30a = models.CharField(db_column='G30A', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     g30an = models.CharField(db_column='G30AN', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     g30subd = models.CharField(db_column='G30SUBD', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g30city = models.CharField(db_column='G30CITY', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     g30street = models.CharField(db_column='G30STREET', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g30lname = models.CharField(db_column='G30LNAME', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     g3012 = models.CharField(db_column='G3012', max_length=8, blank=True, null=True)  # Field name made lowercase.
#     g30121 = models.CharField(db_column='G30121', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     g30122 = models.CharField(db_column='G30122', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g45a1 = models.CharField(db_column='G45A1', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     g45a2 = models.CharField(db_column='G45A2', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     g45a3 = models.CharField(db_column='G45A3', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     g45a4 = models.CharField(db_column='G45A4', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     g45a5 = models.CharField(db_column='G45A5', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     g45a6 = models.CharField(db_column='G45A6', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     g45a7 = models.CharField(db_column='G45A7', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     g45a8 = models.CharField(db_column='G45A8', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     g53_ztk = models.CharField(db_column='G53_ZTK', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g53_dt = models.CharField(db_column='G53_DT', max_length=250, blank=True, null=True)  # Field name made lowercase.
#     g53_dn = models.CharField(db_column='G53_DN', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g53_dd = models.DateTimeField(db_column='G53_DD', blank=True, null=True)  # Field name made lowercase.
#     g53_pos = models.CharField(db_column='G53_POS', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     g53_cc = models.CharField(db_column='G53_CC', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     g53_cn = models.CharField(db_column='G53_CN', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     g53_sub = models.CharField(db_column='G53_SUB', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g53_cit = models.CharField(db_column='G53_CIT', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     g53_str = models.CharField(db_column='G53_STR', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     d54_itn = models.CharField(db_column='D54_ITN', max_length=13, blank=True, null=True)  # Field name made lowercase.
#     d5410 = models.CharField(db_column='D5410', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     d541 = models.CharField(db_column='D541', max_length=14, blank=True, null=True)  # Field name made lowercase.
#     d541d = models.DateTimeField(db_column='D541D', blank=True, null=True)  # Field name made lowercase.
#     d5411 = models.CharField(db_column='D5411', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     d5411d = models.DateTimeField(db_column='D5411D', blank=True, null=True)  # Field name made lowercase.
#     d541_inn = models.CharField(db_column='D541_INN', max_length=12, blank=True, null=True)  # Field name made lowercase.
#     d541_kpp = models.CharField(db_column='D541_KPP', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     d542 = models.DateTimeField(db_column='D542', blank=True, null=True)  # Field name made lowercase.
#     d5441 = models.CharField(db_column='D5441', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     d5441nm = models.CharField(db_column='D5441NM', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     d5441mdnm = models.CharField(db_column='D5441MDNM', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     d5442 = models.CharField(db_column='D5442', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     d5443 = models.CharField(db_column='D5443', max_length=250, blank=True, null=True)  # Field name made lowercase.
#     d5444 = models.CharField(db_column='D5444', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     d5445 = models.DateTimeField(db_column='D5445', blank=True, null=True)  # Field name made lowercase.
#     d5446 = models.DateTimeField(db_column='D5446', blank=True, null=True)  # Field name made lowercase.
#     d5447 = models.CharField(db_column='D5447', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     d5451 = models.CharField(db_column='D5451', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     d5451a = models.CharField(db_column='D5451A', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     d54521 = models.CharField(db_column='D54521', max_length=11, blank=True, null=True)  # Field name made lowercase.
#     d54522 = models.CharField(db_column='D54522', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     d54523 = models.CharField(db_column='D54523', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     d5453 = models.DateTimeField(db_column='D5453', blank=True, null=True)  # Field name made lowercase.
#     g54_itn = models.CharField(db_column='G54_ITN', max_length=13, blank=True, null=True)  # Field name made lowercase.
#     g5410 = models.CharField(db_column='G5410', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     g541 = models.CharField(db_column='G541', max_length=14, blank=True, null=True)  # Field name made lowercase.
#     g541d = models.DateTimeField(db_column='G541D', blank=True, null=True)  # Field name made lowercase.
#     g5411 = models.CharField(db_column='G5411', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g5411d = models.DateTimeField(db_column='G5411D', blank=True, null=True)  # Field name made lowercase.
#     g541_inn = models.CharField(db_column='G541_INN', max_length=12, blank=True, null=True)  # Field name made lowercase.
#     g541_kpp = models.CharField(db_column='G541_KPP', max_length=9, blank=True, null=True)  # Field name made lowercase.
#     g542 = models.DateTimeField(db_column='G542', blank=True, null=True)  # Field name made lowercase.
#     g5441 = models.CharField(db_column='G5441', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     g5441nm = models.CharField(db_column='G5441NM', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     g5441mdnm = models.CharField(db_column='G5441MDNM', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     g5442 = models.CharField(db_column='G5442', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g5443 = models.CharField(db_column='G5443', max_length=250, blank=True, null=True)  # Field name made lowercase.
#     g5444 = models.CharField(db_column='G5444', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g5445 = models.DateTimeField(db_column='G5445', blank=True, null=True)  # Field name made lowercase.
#     g5446 = models.DateTimeField(db_column='G5446', blank=True, null=True)  # Field name made lowercase.
#     g5447 = models.CharField(db_column='G5447', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g5451 = models.CharField(db_column='G5451', max_length=7, blank=True, null=True)  # Field name made lowercase.
#     g5451a = models.CharField(db_column='G5451A', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     g54521 = models.CharField(db_column='G54521', max_length=11, blank=True, null=True)  # Field name made lowercase.
#     g54522 = models.CharField(db_column='G54522', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     g54523 = models.CharField(db_column='G54523', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     g5453 = models.DateTimeField(db_column='G5453', blank=True, null=True)  # Field name made lowercase.
#     gd0 = models.CharField(db_column='GD0', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     gd1 = models.DateTimeField(db_column='GD1', blank=True, null=True)  # Field name made lowercase.
#     gd11 = models.CharField(db_column='GD11', max_length=8, blank=True, null=True)  # Field name made lowercase.
#     gd2 = models.CharField(db_column='GD2', max_length=4, blank=True, null=True)  # Field name made lowercase.
#     gd2fio = models.CharField(db_column='GD2FIO', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     gd00 = models.CharField(db_column='GD00', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     gddf = models.DateTimeField(db_column='GDDF', blank=True, null=True)  # Field name made lowercase.
#     recplatv = models.IntegerField(db_column='RECPLATV', blank=True, null=True)  # Field name made lowercase.
#     recslotm = models.IntegerField(db_column='RECSLOTM', blank=True, null=True)  # Field name made lowercase.
#     rectrans = models.IntegerField(db_column='RECTRANS', blank=True, null=True)  # Field name made lowercase.
#     recsumpp = models.IntegerField(db_column='RECSUMPP', blank=True, null=True)  # Field name made lowercase.
#     recpasp = models.IntegerField(db_column='RECPASP', blank=True, null=True)  # Field name made lowercase.
#     dmodify = models.DateTimeField(db_column='DMODIFY', blank=True, null=True)  # Field name made lowercase.
#     tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
#     edoc_guid = models.CharField(db_column='EDOC_GUID', max_length=32, blank=True, null=True)  # Field name made lowercase.
#     edoc_id = models.DecimalField(default=0.00, db_column='EDOC_ID', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
#     p_status1 = models.SmallIntegerField(db_column='P_STATUS1', blank=True, null=True)  # Field name made lowercase.
#     p_status2 = models.SmallIntegerField(db_column='P_STATUS2', blank=True, null=True)  # Field name made lowercase.
#     docid = models.CharField(db_column='DOCID', max_length=38, blank=True, null=True)  # Field name made lowercase.
#     num_pp = models.SmallIntegerField(db_column='NUM_PP', blank=True, null=True)  # Field name made lowercase.
#     g541dn = models.CharField(db_column='G541DN', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g54place = models.CharField(db_column='G54PLACE', max_length=35, blank=True, null=True)  # Field name made lowercase.
#     g50rw = models.CharField(db_column='G50RW', max_length=5, blank=True, null=True)  # Field name made lowercase.
#     drv41 = models.CharField(db_column='DRV41', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     drv41nm = models.CharField(db_column='DRV41NM', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     drv41mdnm = models.CharField(db_column='DRV41MDNM', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     drv47 = models.CharField(db_column='DRV47', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     drv4cc = models.CharField(db_column='DRV4CC', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     drv51 = models.CharField(db_column='DRV51', max_length=7, blank=True, null=True)  # Field name made lowercase.
#     drv51a = models.CharField(db_column='DRV51A', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     drv521 = models.CharField(db_column='DRV521', max_length=11, blank=True, null=True)  # Field name made lowercase.
#     drv522 = models.CharField(db_column='DRV522', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     drv523 = models.CharField(db_column='DRV523', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     drv53 = models.DateTimeField(db_column='DRV53', blank=True, null=True)  # Field name made lowercase.
#     act_tp = models.CharField(db_column='ACT_TP', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     g023build = models.CharField(db_column='G023BUILD', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g023abuild = models.CharField(db_column='G023ABUILD', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g083build = models.CharField(db_column='G083BUILD', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g083abuild = models.CharField(db_column='G083ABUILD', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g093build = models.CharField(db_column='G093BUILD', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g093abuild = models.CharField(db_column='G093ABUILD', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g143build = models.CharField(db_column='G143BUILD', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aeorowner = models.CharField(db_column='AEOROWNER', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     aeocntry = models.CharField(db_column='AEOCNTRY', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     aeonum = models.CharField(db_column='AEONUM', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     aeokind = models.CharField(db_column='AEOKIND', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     aeoregcod = models.CharField(db_column='AEOREGCOD', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     g143abuild = models.CharField(db_column='G143ABUILD', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g16a = models.CharField(db_column='G16A', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     g30aeoown = models.CharField(db_column='G30AEOOWN', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     g30aeocntr = models.CharField(db_column='G30AEOCNTR', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     g30aeokind = models.CharField(db_column='G30AEOKIND', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     g30aeorcod = models.CharField(db_column='G30AEORCOD', max_length=3, blank=True, null=True)  # Field name made lowercase.
#     g30d = models.DateTimeField(db_column='G30D', blank=True, null=True)  # Field name made lowercase.
#     g30dd = models.DateTimeField(db_column='G30DD', blank=True, null=True)  # Field name made lowercase.
#     g30build = models.CharField(db_column='G30BUILD', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g542t = models.CharField(db_column='G542T', max_length=8, blank=True, null=True)  # Field name made lowercase.
#     drv241 = models.CharField(db_column='DRV241', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     drv241nm = models.CharField(db_column='DRV241NM', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     drv241mdnm = models.CharField(db_column='DRV241MDNM', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     drv247 = models.CharField(db_column='DRV247', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     drv24cc = models.CharField(db_column='DRV24CC', max_length=2, blank=True, null=True)  # Field name made lowercase.
#     drv251 = models.CharField(db_column='DRV251', max_length=7, blank=True, null=True)  # Field name made lowercase.
#     drv251a = models.CharField(db_column='DRV251A', max_length=15, blank=True, null=True)  # Field name made lowercase.
#     drv2521 = models.CharField(db_column='DRV2521', max_length=11, blank=True, null=True)  # Field name made lowercase.
#     drv2522 = models.CharField(db_column='DRV2522', max_length=25, blank=True, null=True)  # Field name made lowercase.
#     drv2523 = models.CharField(db_column='DRV2523', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     drv253 = models.DateTimeField(db_column='DRV253', blank=True, null=True)  # Field name made lowercase.
#     g12zpk = models.DecimalField(default=0.00, db_column='G12ZPK', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
#     g22zpk = models.DecimalField(default=0.00, db_column='G22ZPK', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
#     g542time = models.CharField(db_column='G542TIME', max_length=14, blank=True, null=True)  # Field name made lowercase.
#     g02phone = models.CharField(db_column='G02PHONE', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g02email = models.CharField(db_column='G02EMAIL', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     g08phone = models.CharField(db_column='G08PHONE', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g08email = models.CharField(db_column='G08EMAIL', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     g09phone = models.CharField(db_column='G09PHONE', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g09email = models.CharField(db_column='G09EMAIL', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     g14phone = models.CharField(db_column='G14PHONE', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     g14email = models.CharField(db_column='G14EMAIL', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     g54532 = models.DateTimeField(db_column='G54532', blank=True, null=True)  # Field name made lowercase.
#     g54email = models.CharField(db_column='G54EMAIL', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     g0132 = models.CharField(db_column='G0132', max_length=2, blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         abstract = True
#         # db_table = 'KTDHEAD'


class Ktdkmp(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g32 = models.IntegerField(db_column='G32', blank=True, null=True)  # Field name made lowercase.
    kmpfb = models.IntegerField(db_column='KMPFB', blank=True, null=True)  # Field name made lowercase.
    kmpnm = models.CharField(db_column='KMPNM', max_length=250, blank=True, null=True)  # Field name made lowercase.
    kmpkod = models.CharField(db_column='KMPKOD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    kmpadd = models.CharField(db_column='KMPADD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    kmpqadd = models.DecimalField(default=0.00, db_column='KMPQADD', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    kmpqmain = models.DecimalField(default=0.00, db_column='KMPQMAIN', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    kmppr = models.DecimalField(default=0.00, db_column='KMPPR', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    kmpprval = models.CharField(db_column='KMPPRVAL', max_length=3, blank=True, null=True)  # Field name made lowercase.
    kmpqk = models.IntegerField(db_column='KMPQK', blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'KTDKMP'


class Ktdkmpk(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g32 = models.IntegerField(db_column='G32', blank=True, null=True)  # Field name made lowercase.
    kmpfb = models.IntegerField(db_column='KMPFB', blank=True, null=True)  # Field name made lowercase.
    kmpk = models.IntegerField(db_column='KMPK', blank=True, null=True)  # Field name made lowercase.
    kmpkid = models.DecimalField(default=0.00, db_column='KMPKID', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    kmpknum = models.CharField(db_column='KMPKNUM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kmpnm = models.CharField(db_column='KMPNM', max_length=250, blank=True, null=True)  # Field name made lowercase.
    kmpkod = models.CharField(db_column='KMPKOD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    kmpadd = models.CharField(db_column='KMPADD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    kmpqadd = models.DecimalField(default=0.00, db_column='KMPQADD', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    kmpqmain = models.DecimalField(default=0.00, db_column='KMPQMAIN', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    kmppr = models.DecimalField(default=0.00, db_column='KMPPR', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    kmpprval = models.CharField(db_column='KMPPRVAL', max_length=3, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'KTDKMPK'


class Ktdpasp(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g2810 = models.CharField(db_column='G2810', max_length=1, blank=True, null=True)  # Field name made lowercase.
    pasp = models.CharField(db_column='PASP', max_length=25, blank=True, null=True)  # Field name made lowercase.
    paspdd = models.DateTimeField(db_column='PASPDD', blank=True, null=True)  # Field name made lowercase.
    pasp0 = models.CharField(db_column='PASP0', max_length=1, blank=True, null=True)  # Field name made lowercase.
    pasp1 = models.CharField(db_column='PASP1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    pasp1dd = models.DateTimeField(db_column='PASP1DD', blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'KTDPASP'


class Ktdpk(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g32 = models.IntegerField(db_column='G32', blank=True, null=True)  # Field name made lowercase.
    pksign = models.CharField(db_column='PKSIGN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    pkvid = models.CharField(db_column='PKVID', max_length=2, blank=True, null=True)  # Field name made lowercase.
    pkkolvo = models.IntegerField(db_column='PKKOLVO', blank=True, null=True)  # Field name made lowercase.
    pkinf = models.CharField(db_column='PKINF', max_length=150, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'KTDPK'


class Ktdplatr(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g32 = models.IntegerField(db_column='G32', blank=True, null=True)  # Field name made lowercase.
    g470 = models.CharField(db_column='G470', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g471 = models.CharField(db_column='G471', max_length=4, blank=True, null=True)  # Field name made lowercase.
    g471npp = models.SmallIntegerField(db_column='G471NPP', blank=True, null=True)  # Field name made lowercase.
    g472 = models.DecimalField(default=0.00, db_column='G472', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    g4721 = models.CharField(db_column='G4721', max_length=3, blank=True, null=True)  # Field name made lowercase.
    g473 = models.FloatField(default=0.00, db_column='G473', blank=True, null=True)  # Field name made lowercase.
    g4731 = models.CharField(db_column='G4731', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g4732 = models.CharField(db_column='G4732', max_length=3, blank=True, null=True)  # Field name made lowercase.
    g4733 = models.CharField(db_column='G4733', max_length=3, blank=True, null=True)  # Field name made lowercase.
    g4734 = models.FloatField(default=0.00, db_column='G4734', blank=True, null=True)  # Field name made lowercase.
    npp = models.SmallIntegerField(db_column='NPP', blank=True, null=True)  # Field name made lowercase.
    g474 = models.DecimalField(default=0.00, db_column='G474', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    g4741 = models.CharField(db_column='G4741', max_length=3, blank=True, null=True)  # Field name made lowercase.
    g475 = models.CharField(db_column='G475', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g473z1_2 = models.CharField(db_column='G473Z1_2', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g473_2 = models.FloatField(default=0.00, db_column='G473_2', blank=True, null=True)  # Field name made lowercase.
    g4731_2 = models.CharField(db_column='G4731_2', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g4732_2 = models.CharField(db_column='G4732_2', max_length=3, blank=True, null=True)  # Field name made lowercase.
    g4733_2 = models.CharField(db_column='G4733_2', max_length=3, blank=True, null=True)  # Field name made lowercase.
    g4734_2 = models.FloatField(default=0.00, db_column='G4734_2', blank=True, null=True)  # Field name made lowercase.
    g473z1_3 = models.CharField(db_column='G473Z1_3', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g473_3 = models.FloatField(default=0.00, db_column='G473_3', blank=True, null=True)  # Field name made lowercase.
    g4731_3 = models.CharField(db_column='G4731_3', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g4732_3 = models.CharField(db_column='G4732_3', max_length=3, blank=True, null=True)  # Field name made lowercase.
    g4733_3 = models.CharField(db_column='G4733_3', max_length=3, blank=True, null=True)  # Field name made lowercase.
    g4734_3 = models.FloatField(default=0.00, db_column='G4734_3', blank=True, null=True)  # Field name made lowercase.
    g473z2_2 = models.SmallIntegerField(db_column='G473Z2_2', blank=True, null=True)  # Field name made lowercase.
    g4730 = models.DateTimeField(db_column='G4730', blank=True, null=True)  # Field name made lowercase.
    g4740 = models.DateTimeField(db_column='G4740', blank=True, null=True)  # Field name made lowercase.
    g47_nd = models.SmallIntegerField(db_column='G47_ND', blank=True, null=True)  # Field name made lowercase.
    g47_ns = models.SmallIntegerField(db_column='G47_NS', blank=True, null=True)  # Field name made lowercase.
    g47_nm = models.SmallIntegerField(db_column='G47_NM', blank=True, null=True)  # Field name made lowercase.
    g47_tr = models.FloatField(default=0.00, db_column='G47_TR', blank=True, null=True)  # Field name made lowercase.
    g47_g40 = models.IntegerField(db_column='G47_G40', blank=True, null=True)  # Field name made lowercase.
    nzp = models.DecimalField(default=0.00, db_column='NZP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dmodify = models.DateTimeField(db_column='DMODIFY', blank=True, null=True)  # Field name made lowercase.
    tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    p_edoc_id = models.DecimalField(default=0.00, db_column='P_EDOC_ID', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    g476 = models.DecimalField(default=0.00, db_column='G476', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    g4761 = models.CharField(db_column='G4761', max_length=3, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.
    g4723 = models.CharField(db_column='G4723', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'KTDPLATR'


class Ktdplatv(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    gb0 = models.CharField(db_column='GB0', max_length=1, blank=True, null=True)  # Field name made lowercase.
    gb1 = models.CharField(db_column='GB1', max_length=4, blank=True, null=True)  # Field name made lowercase.
    gb2 = models.DecimalField(default=0.00, db_column='GB2', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    gb3 = models.CharField(db_column='GB3', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gb4 = models.FloatField(default=0.00, db_column='GB4', blank=True, null=True)  # Field name made lowercase.
    gb5 = models.CharField(db_column='GB5', max_length=2, blank=True, null=True)  # Field name made lowercase.
    iret = models.SmallIntegerField(db_column='IRET', blank=True, null=True)  # Field name made lowercase.
    g48 = models.DateTimeField(db_column='G48', blank=True, null=True)  # Field name made lowercase.
    g481 = models.CharField(db_column='G481', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g482 = models.CharField(db_column='G482', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g482d = models.DateTimeField(db_column='G482D', blank=True, null=True)  # Field name made lowercase.
    nzp = models.DecimalField(default=0.00, db_column='NZP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dmodify = models.DateTimeField(db_column='DMODIFY', blank=True, null=True)  # Field name made lowercase.
    tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    p_edoc_id = models.DecimalField(default=0.00, db_column='P_EDOC_ID', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    gb6 = models.DecimalField(default=0.00, db_column='GB6', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    gb61 = models.CharField(db_column='GB61', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gb7 = models.DecimalField(default=0.00, db_column='GB7', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.
    g48doccode = models.CharField(db_column='G48DOCCODE', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'KTDPLATV'


class Ktdpredd(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g32 = models.IntegerField(db_column='G32', blank=True, null=True)  # Field name made lowercase.
    numrec = models.IntegerField(db_column='NUMREC', blank=True, null=True)  # Field name made lowercase.
    g40_cntry = models.CharField(db_column='G40_CNTRY', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g40_0 = models.CharField(db_column='G40_0', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g40_naim = models.CharField(db_column='G40_NAIM', max_length=250, blank=True, null=True)  # Field name made lowercase.
    g40_1 = models.CharField(db_column='G40_1', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g40_2 = models.DateTimeField(db_column='G40_2', blank=True, null=True)  # Field name made lowercase.
    g40_21 = models.CharField(db_column='G40_21', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g40_3 = models.CharField(db_column='G40_3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g40_4 = models.IntegerField(db_column='G40_4', blank=True, null=True)  # Field name made lowercase.
    g40_doctyp = models.CharField(db_column='G40_DOCTYP', max_length=5, blank=True, null=True)  # Field name made lowercase.
    nzp = models.DecimalField(default=0.00, db_column='NZP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dmodify = models.DateTimeField(db_column='DMODIFY', blank=True, null=True)  # Field name made lowercase.
    tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    p_edoc_id = models.DecimalField(default=0.00, db_column='P_EDOC_ID', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.
    g33 = models.CharField(db_column='G33', max_length=10, blank=True, null=True)  # Field name made lowercase.
    prevnumtyp = models.CharField(db_column='PREVNUMTYP', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g40_31 = models.CharField(db_column='G40_31', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'KTDPREDD'


class Ktdsumpp(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    gb1 = models.CharField(db_column='GB1', max_length=4, blank=True, null=True)  # Field name made lowercase.
    gb3 = models.CharField(db_column='GB3', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gb5 = models.CharField(db_column='GB5', max_length=2, blank=True, null=True)  # Field name made lowercase.
    iret = models.SmallIntegerField(db_column='IRET', blank=True, null=True)  # Field name made lowercase.
    numpdok = models.CharField(db_column='NUMPDOK', max_length=50, blank=True, null=True)  # Field name made lowercase.
    datpdok = models.DateTimeField(db_column='DATPDOK', blank=True, null=True)  # Field name made lowercase.
    sum_all = models.DecimalField(default=0.00, db_column='SUM_ALL', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sumpdok = models.DecimalField(default=0.00, db_column='SUMPDOK', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valpdok = models.CharField(db_column='VALPDOK', max_length=3, blank=True, null=True)  # Field name made lowercase.
    datpostd = models.DateTimeField(db_column='DATPOSTD', blank=True, null=True)  # Field name made lowercase.
    datpaymt = models.DateTimeField(db_column='DATPAYMT', blank=True, null=True)  # Field name made lowercase.
    innplat = models.CharField(db_column='INNPLAT', max_length=30, blank=True, null=True)  # Field name made lowercase.
    kppplat = models.CharField(db_column='KPPPLAT', max_length=9, blank=True, null=True)  # Field name made lowercase.
    lnpins = models.CharField(db_column='LNPINS', max_length=4, blank=True, null=True)  # Field name made lowercase.
    fioins = models.CharField(db_column='FIOINS', max_length=40, blank=True, null=True)  # Field name made lowercase.
    datins = models.DateTimeField(db_column='DATINS', blank=True, null=True)  # Field name made lowercase.
    timins = models.CharField(db_column='TIMINS', max_length=8, blank=True, null=True)  # Field name made lowercase.
    nzp = models.DecimalField(default=0.00, db_column='NZP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dmodify = models.DateTimeField(db_column='DMODIFY', blank=True, null=True)  # Field name made lowercase.
    tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    p_edoc_id = models.DecimalField(default=0.00, db_column='P_EDOC_ID', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'KTDSUMPP'


class Ktdtechd(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g32 = models.IntegerField(db_column='G32', blank=True, null=True)  # Field name made lowercase.
    g4401 = models.SmallIntegerField(db_column='G4401', blank=True, null=True)  # Field name made lowercase.
    g4402 = models.SmallIntegerField(db_column='G4402', blank=True, null=True)  # Field name made lowercase.
    g4403 = models.CharField(db_column='G4403', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g44020 = models.CharField(db_column='G44020', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g44_cust = models.CharField(db_column='G44_CUST', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g440 = models.CharField(db_column='G440', max_length=4, blank=True, null=True)  # Field name made lowercase.
    g441 = models.CharField(db_column='G441', max_length=5, blank=True, null=True)  # Field name made lowercase.
    g441a = models.CharField(db_column='G441A', max_length=2, blank=True, null=True)  # Field name made lowercase.
    id_bdrd = models.CharField(db_column='ID_BDRD', max_length=32, blank=True, null=True)  # Field name made lowercase.
    prsbdrd = models.CharField(db_column='PRSBDRD', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g442 = models.CharField(db_column='G442', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g442lic1 = models.SmallIntegerField(db_column='G442LIC1', blank=True, null=True)  # Field name made lowercase.
    g442lic2 = models.IntegerField(db_column='G442LIC2', blank=True, null=True)  # Field name made lowercase.
    g442r = models.CharField(db_column='G442R', max_length=28, blank=True, null=True)  # Field name made lowercase.
    g442simp = models.CharField(db_column='G442SIMP', max_length=10, blank=True, null=True)  # Field name made lowercase.
    g44mdp1 = models.IntegerField(db_column='G44MDP1', blank=True, null=True)  # Field name made lowercase.
    g44mdp2 = models.CharField(db_column='G44MDP2', max_length=18, blank=True, null=True)  # Field name made lowercase.
    g443 = models.DateTimeField(db_column='G443', blank=True, null=True)  # Field name made lowercase.
    g444 = models.CharField(db_column='G444', max_length=250, blank=True, null=True)  # Field name made lowercase.
    g445 = models.CharField(db_column='G445', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g446 = models.DateTimeField(db_column='G446', blank=True, null=True)  # Field name made lowercase.
    g447 = models.DateTimeField(db_column='G447', blank=True, null=True)  # Field name made lowercase.
    g4480et = models.CharField(db_column='G4480ET', max_length=10, blank=True, null=True)  # Field name made lowercase.
    g4481et = models.DateTimeField(db_column='G4481ET', blank=True, null=True)  # Field name made lowercase.
    g44stper = models.DecimalField(default=0.00, db_column='G44STPER', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    g44sfcntry = models.CharField(db_column='G44SFCNTRY', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g44alldoc = models.SmallIntegerField(db_column='G44ALLDOC', blank=True, null=True)  # Field name made lowercase.
    g4491 = models.DateTimeField(db_column='G4491', blank=True, null=True)  # Field name made lowercase.
    g4492 = models.DateTimeField(db_column='G4492', blank=True, null=True)  # Field name made lowercase.
    g4493 = models.CharField(db_column='G4493', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g44dd = models.DateTimeField(db_column='G44DD', blank=True, null=True)  # Field name made lowercase.
    nzp = models.DecimalField(default=0.00, db_column='NZP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dmodify = models.DateTimeField(db_column='DMODIFY', blank=True, null=True)  # Field name made lowercase.
    tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    ed_id = models.CharField(db_column='ED_ID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.
    prevnumtyp = models.CharField(db_column='PREVNUMTYP', max_length=1, blank=True, null=True)  # Field name made lowercase.
    prevnumdoc = models.CharField(db_column='PREVNUMDOC', max_length=50, blank=True, null=True)  # Field name made lowercase.
    recordid = models.CharField(db_column='RECORDID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    executbody = models.CharField(db_column='EXECUTBODY', max_length=10, blank=True, null=True)  # Field name made lowercase.
    execname = models.CharField(db_column='EXECNAME', max_length=250, blank=True, null=True)  # Field name made lowercase.
    ineturl = models.CharField(db_column='INETURL', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'KTDTECHD'


class Ktdterms(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g32 = models.IntegerField(db_column='G32', blank=True, null=True)  # Field name made lowercase.
    terms = models.CharField(db_column='TERMS', max_length=3, blank=True, null=True)  # Field name made lowercase.
    termspoint = models.CharField(db_column='TERMSPOINT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    termspass = models.CharField(db_column='TERMSPASS', max_length=250, blank=True, null=True)  # Field name made lowercase.
    nzp = models.DecimalField(default=0.00, db_column='NZP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dmodify = models.DateTimeField(db_column='DMODIFY', blank=True, null=True)  # Field name made lowercase.
    tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    p_edoc_id = models.DecimalField(default=0.00, db_column='P_EDOC_ID', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'KTDTERMS'


class Ktdtov2(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    type_info = models.CharField(db_column='TYPE_INFO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g031 = models.IntegerField(db_column='G031', blank=True, null=True)  # Field name made lowercase.
    g31_1 = models.CharField(db_column='G31_1', max_length=250, blank=True, null=True)  # Field name made lowercase.
    g31_7 = models.DecimalField(default=0.00, db_column='G31_7', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    g31_71 = models.CharField(db_column='G31_71', max_length=13, blank=True, null=True)  # Field name made lowercase.
    g31_8 = models.DecimalField(default=0.00, db_column='G31_8', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    g31_81 = models.CharField(db_column='G31_81', max_length=13, blank=True, null=True)  # Field name made lowercase.
    g31_82 = models.CharField(db_column='G31_82', max_length=3, blank=True, null=True)  # Field name made lowercase.
    g31_9 = models.DecimalField(default=0.00, db_column='G31_9', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    g31_91 = models.CharField(db_column='G31_91', max_length=13, blank=True, null=True)  # Field name made lowercase.
    g31_92 = models.CharField(db_column='G31_92', max_length=3, blank=True, null=True)  # Field name made lowercase.
    g31_d1 = models.DateTimeField(db_column='G31_D1', blank=True, null=True)  # Field name made lowercase.
    g31_d2 = models.DateTimeField(db_column='G31_D2', blank=True, null=True)  # Field name made lowercase.
    g32 = models.IntegerField(db_column='G32', blank=True, null=True)  # Field name made lowercase.
    numpredd = models.IntegerField(db_column='NUMPREDD', blank=True, null=True)  # Field name made lowercase.
    g33 = models.CharField(db_column='G33', max_length=10, blank=True, null=True)  # Field name made lowercase.
    g330 = models.CharField(db_column='G330', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g331 = models.CharField(db_column='G331', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g332 = models.CharField(db_column='G332', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g333 = models.CharField(db_column='G333', max_length=4, blank=True, null=True)  # Field name made lowercase.
    g340 = models.CharField(db_column='G340', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g34 = models.CharField(db_column='G34', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g35 = models.DecimalField(default=0.00, db_column='G35', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    g36 = models.CharField(db_column='G36', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g37 = models.CharField(db_column='G37', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g38 = models.DecimalField(default=0.00, db_column='G38', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    g38_1 = models.DecimalField(default=0.00, db_column='G38_1', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    g40_g38 = models.DecimalField(default=0.00, db_column='G40_G38', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    g40_g31_7 = models.DecimalField(default=0.00, db_column='G40_G31_7', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    numrec = models.IntegerField(db_column='NUMREC', blank=True, null=True)  # Field name made lowercase.
    g40_0 = models.CharField(db_column='G40_0', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g40_1 = models.CharField(db_column='G40_1', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g40_2 = models.DateTimeField(db_column='G40_2', blank=True, null=True)  # Field name made lowercase.
    g40_21 = models.CharField(db_column='G40_21', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g40_3 = models.CharField(db_column='G40_3', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g40_4 = models.IntegerField(db_column='G40_4', blank=True, null=True)  # Field name made lowercase.
    g41a = models.CharField(db_column='G41A', max_length=3, blank=True, null=True)  # Field name made lowercase.
    g40_naim = models.CharField(db_column='G40_NAIM', max_length=30, blank=True, null=True)  # Field name made lowercase.
    g42 = models.DecimalField(default=0.00, db_column='G42', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    g45 = models.DecimalField(default=0.00, db_column='G45', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    g451 = models.CharField(db_column='G451', max_length=2, blank=True, null=True)  # Field name made lowercase.
    nzp = models.DecimalField(default=0.00, db_column='NZP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dmodify = models.DateTimeField(db_column='DMODIFY', blank=True, null=True)  # Field name made lowercase.
    tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    p_edoc_id = models.DecimalField(default=0.00, db_column='P_EDOC_ID', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'KTDTOV2'


class Ktdtovar(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g02_itn = models.CharField(db_column='G02_ITN', max_length=13, blank=True, null=True)  # Field name made lowercase.
    g021 = models.CharField(db_column='G021', max_length=40, blank=True, null=True)  # Field name made lowercase.
    g022 = models.CharField(db_column='G022', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g023post = models.CharField(db_column='G023POST', max_length=9, blank=True, null=True)  # Field name made lowercase.
    g0231 = models.CharField(db_column='G0231', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g0231n = models.CharField(db_column='G0231N', max_length=40, blank=True, null=True)  # Field name made lowercase.
    g023subd = models.CharField(db_column='G023SUBD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g023city = models.CharField(db_column='G023CITY', max_length=35, blank=True, null=True)  # Field name made lowercase.
    g023street = models.CharField(db_column='G023STREET', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g024b = models.CharField(db_column='G024B', max_length=5, blank=True, null=True)  # Field name made lowercase.
    g024n = models.CharField(db_column='G024N', max_length=10, blank=True, null=True)  # Field name made lowercase.
    g024in = models.CharField(db_column='G024IN', max_length=12, blank=True, null=True)  # Field name made lowercase.
    g027 = models.CharField(db_column='G027', max_length=9, blank=True, null=True)  # Field name made lowercase.
    g0281 = models.CharField(db_column='G0281', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g0281a = models.CharField(db_column='G0281A', max_length=15, blank=True, null=True)  # Field name made lowercase.
    g02821 = models.CharField(db_column='G02821', max_length=11, blank=True, null=True)  # Field name made lowercase.
    g02822 = models.CharField(db_column='G02822', max_length=25, blank=True, null=True)  # Field name made lowercase.
    g02823 = models.CharField(db_column='G02823', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g0283 = models.DateTimeField(db_column='G0283', blank=True, null=True)  # Field name made lowercase.
    g022a = models.CharField(db_column='G022A', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g027a = models.CharField(db_column='G027A', max_length=9, blank=True, null=True)  # Field name made lowercase.
    g023apost = models.CharField(db_column='G023APOST', max_length=9, blank=True, null=True)  # Field name made lowercase.
    g0231a = models.CharField(db_column='G0231A', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g0231an = models.CharField(db_column='G0231AN', max_length=40, blank=True, null=True)  # Field name made lowercase.
    g023asubd = models.CharField(db_column='G023ASUBD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g023acity = models.CharField(db_column='G023ACITY', max_length=35, blank=True, null=True)  # Field name made lowercase.
    g023astree = models.CharField(db_column='G023ASTREE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g031 = models.IntegerField(db_column='G031', blank=True, null=True)  # Field name made lowercase.
    g31_1 = models.CharField(db_column='G31_1', max_length=250, blank=True, null=True)  # Field name made lowercase.
    g31_13 = models.CharField(db_column='G31_13', max_length=40, blank=True, null=True)  # Field name made lowercase.
    g31_1_prdt = models.DateTimeField(db_column='G31_1_PRDT', blank=True, null=True)  # Field name made lowercase.
    g31_1_oilf = models.CharField(db_column='G31_1_OILF', max_length=250, blank=True, null=True)  # Field name made lowercase.
    g31_2 = models.IntegerField(db_column='G31_2', blank=True, null=True)  # Field name made lowercase.
    g31_2part = models.IntegerField(db_column='G31_2PART', blank=True, null=True)  # Field name made lowercase.
    g31_20 = models.CharField(db_column='G31_20', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g31_3 = models.IntegerField(db_column='G31_3', blank=True, null=True)  # Field name made lowercase.
    g31_7 = models.DecimalField(default=0.00, db_column='G31_7', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    g31_71 = models.CharField(db_column='G31_71', max_length=30, blank=True, null=True)  # Field name made lowercase.
    g31_8 = models.DecimalField(default=0.00, db_column='G31_8', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    g31_81 = models.CharField(db_column='G31_81', max_length=30, blank=True, null=True)  # Field name made lowercase.
    g31_82 = models.CharField(db_column='G31_82', max_length=4, blank=True, null=True)  # Field name made lowercase.
    g31_9 = models.DecimalField(default=0.00, db_column='G31_9', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    g31_91 = models.CharField(db_column='G31_91', max_length=30, blank=True, null=True)  # Field name made lowercase.
    g31_92 = models.CharField(db_column='G31_92', max_length=4, blank=True, null=True)  # Field name made lowercase.
    g31_10 = models.IntegerField(db_column='G31_10', blank=True, null=True)  # Field name made lowercase.
    g31_101 = models.CharField(db_column='G31_101', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g31_d1 = models.DateTimeField(db_column='G31_D1', blank=True, null=True)  # Field name made lowercase.
    g31_d2 = models.DateTimeField(db_column='G31_D2', blank=True, null=True)  # Field name made lowercase.
    g31_p1 = models.CharField(db_column='G31_P1', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g31_p2 = models.CharField(db_column='G31_P2', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g31_fact = models.DecimalField(default=0.00, db_column='G31_FACT', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    g31_fc_1 = models.CharField(db_column='G31_FC_1', max_length=3, blank=True, null=True)  # Field name made lowercase.
    g32 = models.IntegerField(db_column='G32', blank=True, null=True)  # Field name made lowercase.
    g32kdt = models.IntegerField(db_column='G32KDT', blank=True, null=True)  # Field name made lowercase.
    g32_1 = models.CharField(db_column='G32_1', max_length=3, blank=True, null=True)  # Field name made lowercase.
    g33 = models.CharField(db_column='G33', max_length=10, blank=True, null=True)  # Field name made lowercase.
    g330 = models.CharField(db_column='G330', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g331 = models.CharField(db_column='G331', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g332 = models.CharField(db_column='G332', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g333 = models.CharField(db_column='G333', max_length=4, blank=True, null=True)  # Field name made lowercase.
    g334 = models.CharField(db_column='G334', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g340 = models.CharField(db_column='G340', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g34 = models.CharField(db_column='G34', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g35 = models.DecimalField(default=0.00, db_column='G35', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    g36 = models.CharField(db_column='G36', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g37 = models.CharField(db_column='G37', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g38 = models.DecimalField(default=0.00, db_column='G38', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    g38_1 = models.DecimalField(default=0.00, db_column='G38_1', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    g39 = models.DecimalField(default=0.00, db_column='G39', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    g3911 = models.CharField(db_column='G3911', max_length=3, blank=True, null=True)  # Field name made lowercase.
    g3912 = models.CharField(db_column='G3912', max_length=3, blank=True, null=True)  # Field name made lowercase.
    g392 = models.CharField(db_column='G392', max_length=70, blank=True, null=True)  # Field name made lowercase.
    g41a = models.CharField(db_column='G41A', max_length=4, blank=True, null=True)  # Field name made lowercase.
    g42 = models.DecimalField(default=0.00, db_column='G42', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    g43 = models.CharField(db_column='G43', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g430 = models.CharField(db_column='G430', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g45 = models.DecimalField(default=0.00, db_column='G45', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    g451 = models.CharField(db_column='G451', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g452 = models.DecimalField(default=0.00, db_column='G452', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    g45a1 = models.CharField(db_column='G45A1', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g45a2 = models.CharField(db_column='G45A2', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g45a3 = models.CharField(db_column='G45A3', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g45a4 = models.CharField(db_column='G45A4', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g45a5 = models.CharField(db_column='G45A5', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g45a6 = models.CharField(db_column='G45A6', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g45a7 = models.CharField(db_column='G45A7', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g45a8 = models.CharField(db_column='G45A8', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g46 = models.DecimalField(default=0.00, db_column='G46', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    g461 = models.CharField(db_column='G461', max_length=1, blank=True, null=True)  # Field name made lowercase.
    nblank = models.CharField(db_column='NBLANK', max_length=10, blank=True, null=True)  # Field name made lowercase.
    fksign = models.CharField(db_column='FKSIGN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    gd0 = models.CharField(db_column='GD0', max_length=2, blank=True, null=True)  # Field name made lowercase.
    gd1 = models.DateTimeField(db_column='GD1', blank=True, null=True)  # Field name made lowercase.
    gd11 = models.CharField(db_column='GD11', max_length=8, blank=True, null=True)  # Field name made lowercase.
    gd2 = models.CharField(db_column='GD2', max_length=4, blank=True, null=True)  # Field name made lowercase.
    gd00 = models.CharField(db_column='GD00', max_length=150, blank=True, null=True)  # Field name made lowercase.
    kod_str = models.CharField(db_column='KOD_STR', max_length=2, blank=True, null=True)  # Field name made lowercase.
    dstat = models.DateTimeField(db_column='DSTAT', blank=True, null=True)  # Field name made lowercase.
    stat = models.CharField(db_column='STAT', max_length=1, blank=True, null=True)  # Field name made lowercase.
    recplatr = models.IntegerField(db_column='RECPLATR', blank=True, null=True)  # Field name made lowercase.
    rectechd = models.IntegerField(db_column='RECTECHD', blank=True, null=True)  # Field name made lowercase.
    recpredd = models.IntegerField(db_column='RECPREDD', blank=True, null=True)  # Field name made lowercase.
    recavtmb = models.IntegerField(db_column='RECAVTMB', blank=True, null=True)  # Field name made lowercase.
    rectovg = models.IntegerField(db_column='RECTOVG', blank=True, null=True)  # Field name made lowercase.
    recpk = models.IntegerField(db_column='RECPK', blank=True, null=True)  # Field name made lowercase.
    recamnum = models.IntegerField(db_column='RECAMNUM', blank=True, null=True)  # Field name made lowercase.
    recterms = models.IntegerField(db_column='RECTERMS', blank=True, null=True)  # Field name made lowercase.
    recdog = models.IntegerField(db_column='RECDOG', blank=True, null=True)  # Field name made lowercase.
    recdoga = models.IntegerField(db_column='RECDOGA', blank=True, null=True)  # Field name made lowercase.
    recdogt = models.IntegerField(db_column='RECDOGT', blank=True, null=True)  # Field name made lowercase.
    reckmp = models.IntegerField(db_column='RECKMP', blank=True, null=True)  # Field name made lowercase.
    recuslt = models.IntegerField(db_column='RECUSLT', blank=True, null=True)  # Field name made lowercase.
    recsltov = models.IntegerField(db_column='RECSLTOV', blank=True, null=True)  # Field name made lowercase.
    rectov2 = models.IntegerField(db_column='RECTOV2', blank=True, null=True)  # Field name made lowercase.
    recplat2 = models.IntegerField(db_column='RECPLAT2', blank=True, null=True)  # Field name made lowercase.
    recdinf2 = models.IntegerField(db_column='RECDINF2', blank=True, null=True)  # Field name made lowercase.
    rectovg2 = models.IntegerField(db_column='RECTOVG2', blank=True, null=True)  # Field name made lowercase.
    recvrsk = models.IntegerField(db_column='RECVRSK', blank=True, null=True)  # Field name made lowercase.
    nzp = models.DecimalField(default=0.00, db_column='NZP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dmodify = models.DateTimeField(db_column='DMODIFY', blank=True, null=True)  # Field name made lowercase.
    tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    p_edoc_id = models.DecimalField(default=0.00, db_column='P_EDOC_ID', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    g020 = models.CharField(db_column='G020', max_length=15, blank=True, null=True)  # Field name made lowercase.
    g42c = models.CharField(db_column='G42C', max_length=3, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.
    g023build = models.CharField(db_column='G023BUILD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g35zpk = models.DecimalField(default=0.00, db_column='G35ZPK', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    g38zpk = models.DecimalField(default=0.00, db_column='G38ZPK', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    g42curr = models.CharField(db_column='G42CURR', max_length=3, blank=True, null=True)  # Field name made lowercase.
    g42rate = models.FloatField(default=0.00, db_column='G42RATE', blank=True, null=True)  # Field name made lowercase.
    g46zpk = models.DecimalField(default=0.00, db_column='G46ZPK', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    g31_dti = models.DecimalField(default=0.00, db_column='G31_DTI', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    g34_2c = models.CharField(db_column='G34_2C', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g34_2n = models.CharField(db_column='G34_2N', max_length=40, blank=True, null=True)  # Field name made lowercase.
    g31_trc = models.DecimalField(default=0.00, db_column='G31_TRC', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    g31_trc1 = models.CharField(db_column='G31_TRC1', max_length=30, blank=True, null=True)  # Field name made lowercase.
    g31_trc2 = models.CharField(db_column='G31_TRC2', max_length=4, blank=True, null=True)  # Field name made lowercase.
    g335 = models.CharField(db_column='G335', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g462 = models.DecimalField(default=0.00, db_column='G462', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    g462curr = models.CharField(db_column='G462CURR', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'KTDTOVAR'


class Ktdtovg(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g32 = models.IntegerField(db_column='G32', blank=True, null=True)  # Field name made lowercase.
    g32g = models.SmallIntegerField(db_column='G32G', blank=True, null=True)  # Field name made lowercase.
    numrec = models.SmallIntegerField(db_column='NUMREC', blank=True, null=True)  # Field name made lowercase.
    g31_10 = models.CharField(db_column='G31_10', max_length=4, blank=True, null=True)  # Field name made lowercase.
    g31_11 = models.CharField(db_column='G31_11', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g31_12 = models.CharField(db_column='G31_12', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g31_14 = models.CharField(db_column='G31_14', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g31_15_mod = models.CharField(db_column='G31_15_MOD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g31_15 = models.CharField(db_column='G31_15', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g31_16 = models.CharField(db_column='G31_16', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g31_17 = models.CharField(db_column='G31_17', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g31_18 = models.CharField(db_column='G31_18', max_length=30, blank=True, null=True)  # Field name made lowercase.
    g31_19 = models.CharField(db_column='G31_19', max_length=20, blank=True, null=True)  # Field name made lowercase.
    g31_20 = models.CharField(db_column='G31_20', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kolvo = models.DecimalField(default=0.00, db_column='KOLVO', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    code_edi = models.CharField(db_column='CODE_EDI', max_length=3, blank=True, null=True)  # Field name made lowercase.
    name_edi = models.CharField(db_column='NAME_EDI', max_length=13, blank=True, null=True)  # Field name made lowercase.
    rois_num = models.CharField(db_column='ROIS_NUM', max_length=250, blank=True, null=True)  # Field name made lowercase.
    rois_cc = models.CharField(db_column='ROIS_CC', max_length=2, blank=True, null=True)  # Field name made lowercase.
    nzp = models.DecimalField(default=0.00, db_column='NZP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dmodify = models.DateTimeField(db_column='DMODIFY', blank=True, null=True)  # Field name made lowercase.
    tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    p_edoc_id = models.DecimalField(default=0.00, db_column='P_EDOC_ID', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.
    g31place = models.CharField(db_column='G31PLACE', max_length=250, blank=True, null=True)  # Field name made lowercase.
    length = models.DecimalField(default=0.00, db_column='LENGTH', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    width = models.DecimalField(default=0.00, db_column='WIDTH', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    height = models.DecimalField(default=0.00, db_column='HEIGHT', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    recordid = models.CharField(db_column='RECORDID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    invoiccost = models.DecimalField(default=0.00, db_column='INVOICCOST', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    licgrpdoc1 = models.CharField(db_column='LICGRPDOC1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    licgrpd1 = models.DateTimeField(db_column='LICGRPD1', blank=True, null=True)  # Field name made lowercase.
    licrec1 = models.CharField(db_column='LICREC1', max_length=36, blank=True, null=True)  # Field name made lowercase.
    goodnmlic1 = models.IntegerField(db_column='GOODNMLIC1', blank=True, null=True)  # Field name made lowercase.
    licgrpdoc2 = models.CharField(db_column='LICGRPDOC2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    licgrpd2 = models.DateTimeField(db_column='LICGRPD2', blank=True, null=True)  # Field name made lowercase.
    licrec2 = models.CharField(db_column='LICREC2', max_length=36, blank=True, null=True)  # Field name made lowercase.
    goodnmlic2 = models.IntegerField(db_column='GOODNMLIC2', blank=True, null=True)  # Field name made lowercase.
    compord = models.SmallIntegerField(db_column='COMPORD', blank=True, null=True)  # Field name made lowercase.
    compnum = models.CharField(db_column='COMPNUM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g31_inn = models.CharField(db_column='G31_INN', max_length=12, blank=True, null=True)  # Field name made lowercase.
    g31_okato = models.CharField(db_column='G31_OKATO', max_length=11, blank=True, null=True)  # Field name made lowercase.
    g31_kpp = models.CharField(db_column='G31_KPP', max_length=9, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'KTDTOVG'


class Ktdtovg2(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g32 = models.IntegerField(db_column='G32', blank=True, null=True)  # Field name made lowercase.
    type_info = models.CharField(db_column='TYPE_INFO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    numpredd = models.IntegerField(db_column='NUMPREDD', blank=True, null=True)  # Field name made lowercase.
    g32g = models.SmallIntegerField(db_column='G32G', blank=True, null=True)  # Field name made lowercase.
    numrec = models.SmallIntegerField(db_column='NUMREC', blank=True, null=True)  # Field name made lowercase.
    g31_10 = models.CharField(db_column='G31_10', max_length=4, blank=True, null=True)  # Field name made lowercase.
    g31_11 = models.CharField(db_column='G31_11', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g31_12 = models.CharField(db_column='G31_12', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g31_14 = models.CharField(db_column='G31_14', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g31_15_mod = models.CharField(db_column='G31_15_MOD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g31_15 = models.CharField(db_column='G31_15', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g31_16 = models.CharField(db_column='G31_16', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g31_17 = models.CharField(db_column='G31_17', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g31_18 = models.CharField(db_column='G31_18', max_length=30, blank=True, null=True)  # Field name made lowercase.
    g31_19 = models.CharField(db_column='G31_19', max_length=20, blank=True, null=True)  # Field name made lowercase.
    g31_20 = models.CharField(db_column='G31_20', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kolvo = models.DecimalField(default=0.00, db_column='KOLVO', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    code_edi = models.CharField(db_column='CODE_EDI', max_length=3, blank=True, null=True)  # Field name made lowercase.
    name_edi = models.CharField(db_column='NAME_EDI', max_length=13, blank=True, null=True)  # Field name made lowercase.
    nzp = models.DecimalField(default=0.00, db_column='NZP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dmodify = models.DateTimeField(db_column='DMODIFY', blank=True, null=True)  # Field name made lowercase.
    tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    p_edoc_id = models.DecimalField(default=0.00, db_column='P_EDOC_ID', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'KTDTOVG2'


class Ktdtovs(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g32 = models.IntegerField(db_column='G32', blank=True, null=True)  # Field name made lowercase.
    g32g = models.SmallIntegerField(db_column='G32G', blank=True, null=True)  # Field name made lowercase.
    numrec = models.IntegerField(db_column='NUMREC', blank=True, null=True)  # Field name made lowercase.
    g31_15_sn = models.CharField(db_column='G31_15_SN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nzp = models.DecimalField(default=0.00, db_column='NZP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dmodify = models.DateTimeField(db_column='DMODIFY', blank=True, null=True)  # Field name made lowercase.
    tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    p_edoc_id = models.DecimalField(default=0.00, db_column='P_EDOC_ID', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'KTDTOVS'


class Ktdtrans(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    ngr = models.CharField(db_column='NGR', max_length=2, blank=True, null=True)  # Field name made lowercase.
    numrec = models.IntegerField(db_column='NUMREC', blank=True, null=True)  # Field name made lowercase.
    vidtrans = models.CharField(db_column='VIDTRANS', max_length=2, blank=True, null=True)  # Field name made lowercase.
    mthtrans = models.CharField(db_column='MTHTRANS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    nametrans = models.CharField(db_column='NAMETRANS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ntrans = models.CharField(db_column='NTRANS', max_length=40, blank=True, null=True)  # Field name made lowercase.
    movetrans = models.CharField(db_column='MOVETRANS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ntrans1 = models.CharField(db_column='NTRANS1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ntrans2 = models.CharField(db_column='NTRANS2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    activeid = models.CharField(db_column='ACTIVEID', max_length=40, blank=True, null=True)  # Field name made lowercase.
    g19 = models.CharField(db_column='G19', max_length=1, blank=True, null=True)  # Field name made lowercase.
    st_control = models.CharField(db_column='ST_CONTROL', max_length=250, blank=True, null=True)  # Field name made lowercase.
    g212 = models.CharField(db_column='G212', max_length=2, blank=True, null=True)  # Field name made lowercase.
    g29 = models.CharField(db_column='G29', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g291 = models.CharField(db_column='G291', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gc5 = models.DateTimeField(db_column='GC5', blank=True, null=True)  # Field name made lowercase.
    gc51 = models.CharField(db_column='GC51', max_length=8, blank=True, null=True)  # Field name made lowercase.
    nzp = models.DecimalField(default=0.00, db_column='NZP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dmodify = models.DateTimeField(db_column='DMODIFY', blank=True, null=True)  # Field name made lowercase.
    tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    p_edoc_id = models.DecimalField(default=0.00, db_column='P_EDOC_ID', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.
    tipts3 = models.CharField(db_column='TIPTS3', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'KTDTRANS'


class Ktduslt(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g32 = models.IntegerField(db_column='G32', blank=True, null=True)  # Field name made lowercase.
    typeinfo = models.CharField(db_column='TYPEINFO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    gu01 = models.SmallIntegerField(db_column='GU01', blank=True, null=True)  # Field name made lowercase.
    gu02 = models.SmallIntegerField(db_column='GU02', blank=True, null=True)  # Field name made lowercase.
    gu03 = models.CharField(db_column='GU03', max_length=2, blank=True, null=True)  # Field name made lowercase.
    gunpp = models.IntegerField(db_column='GUNPP', blank=True, null=True)  # Field name made lowercase.
    gu1 = models.CharField(db_column='GU1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gu1d = models.DateTimeField(db_column='GU1D', blank=True, null=True)  # Field name made lowercase.
    gu2 = models.CharField(db_column='GU2', max_length=250, blank=True, null=True)  # Field name made lowercase.
    gu3 = models.DateTimeField(db_column='GU3', blank=True, null=True)  # Field name made lowercase.
    gudd = models.DateTimeField(db_column='GUDD', blank=True, null=True)  # Field name made lowercase.
    nzp = models.DecimalField(default=0.00, db_column='NZP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dmodify = models.DateTimeField(db_column='DMODIFY', blank=True, null=True)  # Field name made lowercase.
    tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    p_edoc_id = models.DecimalField(default=0.00, db_column='P_EDOC_ID', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'KTDUSLT'


class Psm(BaseModel):
    numcard = models.CharField(db_column='NUMCARD', max_length=23, blank=True, null=True)  # Field name made lowercase.
    model = models.CharField(db_column='MODEL', max_length=36, blank=True, null=True)  # Field name made lowercase.
    tipts = models.CharField(db_column='TIPTS', max_length=2, blank=True, null=True)  # Field name made lowercase.
    god = models.SmallIntegerField(db_column='GOD', blank=True, null=True)  # Field name made lowercase.
    numdvig = models.CharField(db_column='NUMDVIG', max_length=40, blank=True, null=True)  # Field name made lowercase.
    numkper = models.CharField(db_column='NUMKPER', max_length=40, blank=True, null=True)  # Field name made lowercase.
    nummost = models.CharField(db_column='NUMMOST', max_length=80, blank=True, null=True)  # Field name made lowercase.
    shassi = models.CharField(db_column='SHASSI', max_length=40, blank=True, null=True)  # Field name made lowercase.
    zvet = models.CharField(db_column='ZVET', max_length=3, blank=True, null=True)  # Field name made lowercase.
    powerls = models.FloatField(default=0.00, db_column='POWERLS', blank=True, null=True)  # Field name made lowercase.
    powerkw = models.FloatField(default=0.00, db_column='POWERKW', blank=True, null=True)  # Field name made lowercase.
    viddvig = models.CharField(db_column='VIDDVIG', max_length=2, blank=True, null=True)  # Field name made lowercase.
    maxmass = models.IntegerField(db_column='MAXMASS', blank=True, null=True)  # Field name made lowercase.
    maxspeed = models.SmallIntegerField(db_column='MAXSPEED', blank=True, null=True)  # Field name made lowercase.
    width = models.IntegerField(db_column='WIDTH', blank=True, null=True)  # Field name made lowercase.
    height = models.IntegerField(db_column='HEIGHT', blank=True, null=True)  # Field name made lowercase.
    length = models.IntegerField(db_column='LENGTH', blank=True, null=True)  # Field name made lowercase.
    work = models.IntegerField(db_column='WORK', blank=True, null=True)  # Field name made lowercase.
    izgotov = models.CharField(db_column='IZGOTOV', max_length=150, blank=True, null=True)  # Field name made lowercase.
    strizg = models.CharField(db_column='STRIZG', max_length=3, blank=True, null=True)  # Field name made lowercase.
    adrizg = models.CharField(db_column='ADRIZG', max_length=105, blank=True, null=True)  # Field name made lowercase.
    numodob = models.CharField(db_column='NUMODOB', max_length=21, blank=True, null=True)  # Field name made lowercase.
    datodob = models.DateTimeField(db_column='DATODOB', blank=True, null=True)  # Field name made lowercase.
    orgodob = models.CharField(db_column='ORGODOB', max_length=150, blank=True, null=True)  # Field name made lowercase.
    strvyvoz = models.CharField(db_column='STRVYVOZ', max_length=3, blank=True, null=True)  # Field name made lowercase.
    lic = models.CharField(db_column='LIC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fam = models.CharField(db_column='FAM', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ima = models.CharField(db_column='IMA', max_length=25, blank=True, null=True)  # Field name made lowercase.
    otc = models.CharField(db_column='OTC', max_length=25, blank=True, null=True)  # Field name made lowercase.
    nom_doc = models.CharField(db_column='NOM_DOC', max_length=25, blank=True, null=True)  # Field name made lowercase.
    ser_doc = models.CharField(db_column='SER_DOC', max_length=11, blank=True, null=True)  # Field name made lowercase.
    cod_doc = models.CharField(db_column='COD_DOC', max_length=2, blank=True, null=True)  # Field name made lowercase.
    dat_doc = models.DateTimeField(db_column='DAT_DOC', blank=True, null=True)  # Field name made lowercase.
    give_doc = models.CharField(db_column='GIVE_DOC', max_length=150, blank=True, null=True)  # Field name made lowercase.
    strown = models.CharField(db_column='STROWN', max_length=3, blank=True, null=True)  # Field name made lowercase.
    soato = models.CharField(db_column='SOATO', max_length=4, blank=True, null=True)  # Field name made lowercase.
    inn = models.CharField(db_column='INN', max_length=12, blank=True, null=True)  # Field name made lowercase.
    okpo = models.CharField(db_column='OKPO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    namesob = models.CharField(db_column='NAMESOB', max_length=150, blank=True, null=True)  # Field name made lowercase.
    adressob = models.CharField(db_column='ADRESSOB', max_length=105, blank=True, null=True)  # Field name made lowercase.
    gtd = models.CharField(db_column='GTD', max_length=23, blank=True, null=True)  # Field name made lowercase.
    tamogr = models.CharField(db_column='TAMOGR', max_length=250, blank=True, null=True)  # Field name made lowercase.
    numpts = models.CharField(db_column='NUMPTS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    datpts = models.DateTimeField(db_column='DATPTS', blank=True, null=True)  # Field name made lowercase.
    lnpp = models.CharField(db_column='LNPP', max_length=5, blank=True, null=True)  # Field name made lowercase.
    inspectp = models.CharField(db_column='INSPECTP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tamp = models.CharField(db_column='TAMP', max_length=8, blank=True, null=True)  # Field name made lowercase.
    tpo = models.CharField(db_column='TPO', max_length=26, blank=True, null=True)  # Field name made lowercase.
    tnved = models.CharField(db_column='TNVED', max_length=10, blank=True, null=True)  # Field name made lowercase.
    numtd = models.CharField(db_column='NUMTD', max_length=23, blank=True, null=True)  # Field name made lowercase.
    dattd = models.DateTimeField(db_column='DATTD', blank=True, null=True)  # Field name made lowercase.
    numz = models.CharField(db_column='NUMZ', max_length=23, blank=True, null=True)  # Field name made lowercase.
    datz = models.DateTimeField(db_column='DATZ', blank=True, null=True)  # Field name made lowercase.
    datrecv = models.DateTimeField(db_column='DATRECV', blank=True, null=True)  # Field name made lowercase.
    datsend = models.DateTimeField(db_column='DATSEND', blank=True, null=True)  # Field name made lowercase.
    timesend = models.CharField(db_column='TIMESEND', max_length=8, blank=True, null=True)  # Field name made lowercase.
    datemodi = models.DateTimeField(db_column='DATEMODI', blank=True, null=True)  # Field name made lowercase.
    imodi = models.CharField(db_column='IMODI', max_length=1, blank=True, null=True)  # Field name made lowercase.
    kod1 = models.CharField(db_column='KOD1', max_length=3, blank=True, null=True)  # Field name made lowercase.
    kod2 = models.CharField(db_column='KOD2', max_length=3, blank=True, null=True)  # Field name made lowercase.
    kod3 = models.CharField(db_column='KOD3', max_length=3, blank=True, null=True)  # Field name made lowercase.
    shablon = models.CharField(db_column='SHABLON', max_length=25, blank=True, null=True)  # Field name made lowercase.
    avtodel = models.CharField(db_column='AVTODEL', max_length=3, blank=True, null=True)  # Field name made lowercase.
    kabina = models.CharField(db_column='KABINA', max_length=40, blank=True, null=True)  # Field name made lowercase.
    list_col = models.CharField(db_column='LIST_COL', max_length=43, blank=True, null=True)  # Field name made lowercase.
    kpp = models.CharField(db_column='KPP', max_length=9, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=23, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'PSM'


class RegTi(BaseModel):
    adress = models.CharField(db_column='ADRESS', max_length=150, blank=True, null=True)  # Field name made lowercase.
    telefon = models.CharField(db_column='TELEFON', max_length=12, blank=True, null=True)  # Field name made lowercase.
    telegraf = models.CharField(db_column='TELEGRAF', max_length=50, blank=True, null=True)  # Field name made lowercase.
    telefax = models.CharField(db_column='TELEFAX', max_length=12, blank=True, null=True)  # Field name made lowercase.
    telex = models.CharField(db_column='TELEX', max_length=20, blank=True, null=True)  # Field name made lowercase.
    zayv = models.CharField(db_column='ZAYV', max_length=80, blank=True, null=True)  # Field name made lowercase.
    nomr1 = models.CharField(db_column='NOMR1', max_length=2, blank=True, null=True)  # Field name made lowercase.
    nomr2 = models.CharField(db_column='NOMR2', max_length=4, blank=True, null=True)  # Field name made lowercase.
    nomr3 = models.CharField(db_column='NOMR3', max_length=10, blank=True, null=True)  # Field name made lowercase.
    psu = models.CharField(db_column='PSU', max_length=1, blank=True, null=True)  # Field name made lowercase.
    okato = models.CharField(db_column='OKATO', max_length=11, blank=True, null=True)  # Field name made lowercase.
    okpobr = models.CharField(db_column='OKPOBR', max_length=10, blank=True, null=True)  # Field name made lowercase.
    schet1 = models.CharField(db_column='SCHET1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    korschr = models.CharField(db_column='KORSCHR', max_length=20, blank=True, null=True)  # Field name made lowercase.
    okpobv = models.CharField(db_column='OKPOBV', max_length=10, blank=True, null=True)  # Field name made lowercase.
    schet2 = models.CharField(db_column='SCHET2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    korschv = models.CharField(db_column='KORSCHV', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kodtam = models.CharField(db_column='KODTAM', max_length=8, blank=True, null=True)  # Field name made lowercase.
    datr = models.DateTimeField(db_column='DATR', blank=True, null=True)  # Field name made lowercase.
    ogrn = models.CharField(db_column='OGRN', max_length=15, blank=True, null=True)  # Field name made lowercase.
    inn = models.CharField(db_column='INN', max_length=12, blank=True, null=True)  # Field name made lowercase.
    kpp = models.CharField(db_column='KPP', max_length=9, blank=True, null=True)  # Field name made lowercase.
    datn = models.DateTimeField(db_column='DATN', blank=True, null=True)  # Field name made lowercase.
    datm = models.DateTimeField(db_column='DATM', blank=True, null=True)  # Field name made lowercase.
    alfa2 = models.CharField(db_column='ALFA2', max_length=2, blank=True, null=True)  # Field name made lowercase.
    post9 = models.CharField(db_column='POST9', max_length=9, blank=True, null=True)  # Field name made lowercase.
    subcntry = models.CharField(db_column='SUBCNTRY', max_length=35, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='CITY', max_length=35, blank=True, null=True)  # Field name made lowercase.
    street = models.CharField(db_column='STREET', max_length=50, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'REG_TI'


class Sbrddtc(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    num_pp = models.SmallIntegerField(db_column='NUM_PP', blank=True, null=True)  # Field name made lowercase.
    g32 = models.IntegerField(db_column='G32', blank=True, null=True)  # Field name made lowercase.
    npoz = models.CharField(db_column='NPOZ', max_length=3, blank=True, null=True)  # Field name made lowercase.
    numrec = models.SmallIntegerField(db_column='NUMREC', blank=True, null=True)  # Field name made lowercase.
    text1 = models.CharField(db_column='TEXT1', max_length=250, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=28, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'SBRDDTC'


class Sbrdinfo(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    num_pp = models.SmallIntegerField(db_column='NUM_PP', blank=True, null=True)  # Field name made lowercase.
    g32 = models.IntegerField(db_column='G32', blank=True, null=True)  # Field name made lowercase.
    npoz = models.CharField(db_column='NPOZ', max_length=3, blank=True, null=True)  # Field name made lowercase.
    numrec = models.SmallIntegerField(db_column='NUMREC', blank=True, null=True)  # Field name made lowercase.
    dinf01 = models.CharField(db_column='DINF01', max_length=5, blank=True, null=True)  # Field name made lowercase.
    terms = models.CharField(db_column='TERMS', max_length=3, blank=True, null=True)  # Field name made lowercase.
    dinf02 = models.CharField(db_column='DINF02', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dinf03 = models.DateTimeField(db_column='DINF03', blank=True, null=True)  # Field name made lowercase.
    text1 = models.CharField(db_column='TEXT1', max_length=250, blank=True, null=True)  # Field name made lowercase.
    nzp = models.DecimalField(default=0.00, db_column='NZP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dmodify = models.DateTimeField(db_column='DMODIFY', blank=True, null=True)  # Field name made lowercase.
    tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    p_edoc_id = models.DecimalField(default=0.00, db_column='P_EDOC_ID', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=28, blank=True, null=True)  # Field name made lowercase.
    addinfcode = models.CharField(db_column='ADDINFCODE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dt071 = models.CharField(db_column='DT071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    dt072 = models.DateTimeField(db_column='DT072', blank=True, null=True)  # Field name made lowercase.
    dt073 = models.CharField(db_column='DT073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    dtg32 = models.SmallIntegerField(db_column='DTG32', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'SBRDINFO'


class Sbrhead(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    num_pp = models.SmallIntegerField(db_column='NUM_PP', blank=True, null=True)  # Field name made lowercase.
    nmet = models.CharField(db_column='NMET', max_length=2, blank=True, null=True)  # Field name made lowercase.
    nmet6 = models.CharField(db_column='NMET6', max_length=1, blank=True, null=True)  # Field name made lowercase.
    formadtc = models.CharField(db_column='FORMADTC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    d01_ogrn = models.CharField(db_column='D01_OGRN', max_length=15, blank=True, null=True)  # Field name made lowercase.
    d01_inn = models.CharField(db_column='D01_INN', max_length=12, blank=True, null=True)  # Field name made lowercase.
    d01_kpp = models.CharField(db_column='D01_KPP', max_length=9, blank=True, null=True)  # Field name made lowercase.
    d01_itn = models.CharField(db_column='D01_ITN', max_length=13, blank=True, null=True)  # Field name made lowercase.
    d011 = models.CharField(db_column='D011', max_length=150, blank=True, null=True)  # Field name made lowercase.
    d012post = models.CharField(db_column='D012POST', max_length=9, blank=True, null=True)  # Field name made lowercase.
    d0121 = models.CharField(db_column='D0121', max_length=2, blank=True, null=True)  # Field name made lowercase.
    d0121n = models.CharField(db_column='D0121N', max_length=40, blank=True, null=True)  # Field name made lowercase.
    d012subd = models.CharField(db_column='D012SUBD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    d012city = models.CharField(db_column='D012CITY', max_length=35, blank=True, null=True)  # Field name made lowercase.
    d012street = models.CharField(db_column='D012STREET', max_length=50, blank=True, null=True)  # Field name made lowercase.
    d0181 = models.CharField(db_column='D0181', max_length=7, blank=True, null=True)  # Field name made lowercase.
    d0181a = models.CharField(db_column='D0181A', max_length=15, blank=True, null=True)  # Field name made lowercase.
    d01821 = models.CharField(db_column='D01821', max_length=11, blank=True, null=True)  # Field name made lowercase.
    d01822 = models.CharField(db_column='D01822', max_length=25, blank=True, null=True)  # Field name made lowercase.
    d01823 = models.CharField(db_column='D01823', max_length=150, blank=True, null=True)  # Field name made lowercase.
    d0183 = models.DateTimeField(db_column='D0183', blank=True, null=True)  # Field name made lowercase.
    d011a = models.CharField(db_column='D011A', max_length=150, blank=True, null=True)  # Field name made lowercase.
    d011akpp = models.CharField(db_column='D011AKPP', max_length=9, blank=True, null=True)  # Field name made lowercase.
    d011apost = models.CharField(db_column='D011APOST', max_length=9, blank=True, null=True)  # Field name made lowercase.
    d011aalf = models.CharField(db_column='D011AALF', max_length=2, blank=True, null=True)  # Field name made lowercase.
    d011akn = models.CharField(db_column='D011AKN', max_length=40, blank=True, null=True)  # Field name made lowercase.
    d011asubd = models.CharField(db_column='D011ASUBD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    d011acity = models.CharField(db_column='D011ACITY', max_length=35, blank=True, null=True)  # Field name made lowercase.
    d011astree = models.CharField(db_column='D011ASTREE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    d02_ogrn = models.CharField(db_column='D02_OGRN', max_length=15, blank=True, null=True)  # Field name made lowercase.
    d02_inn = models.CharField(db_column='D02_INN', max_length=12, blank=True, null=True)  # Field name made lowercase.
    d02_kpp = models.CharField(db_column='D02_KPP', max_length=9, blank=True, null=True)  # Field name made lowercase.
    d02_itn = models.CharField(db_column='D02_ITN', max_length=13, blank=True, null=True)  # Field name made lowercase.
    d02a1 = models.CharField(db_column='D02A1', max_length=150, blank=True, null=True)  # Field name made lowercase.
    d02a2post = models.CharField(db_column='D02A2POST', max_length=9, blank=True, null=True)  # Field name made lowercase.
    d02a21 = models.CharField(db_column='D02A21', max_length=2, blank=True, null=True)  # Field name made lowercase.
    d02a21n = models.CharField(db_column='D02A21N', max_length=40, blank=True, null=True)  # Field name made lowercase.
    d02a2subd = models.CharField(db_column='D02A2SUBD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    d02a2city = models.CharField(db_column='D02A2CITY', max_length=35, blank=True, null=True)  # Field name made lowercase.
    d02a2stree = models.CharField(db_column='D02A2STREE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    d02a81 = models.CharField(db_column='D02A81', max_length=7, blank=True, null=True)  # Field name made lowercase.
    d02a81a = models.CharField(db_column='D02A81A', max_length=15, blank=True, null=True)  # Field name made lowercase.
    d02a821 = models.CharField(db_column='D02A821', max_length=11, blank=True, null=True)  # Field name made lowercase.
    d02a822 = models.CharField(db_column='D02A822', max_length=25, blank=True, null=True)  # Field name made lowercase.
    d02a823 = models.CharField(db_column='D02A823', max_length=150, blank=True, null=True)  # Field name made lowercase.
    d02a83 = models.DateTimeField(db_column='D02A83', blank=True, null=True)  # Field name made lowercase.
    d02a1a = models.CharField(db_column='D02A1A', max_length=150, blank=True, null=True)  # Field name made lowercase.
    d02a1akpp = models.CharField(db_column='D02A1AKPP', max_length=9, blank=True, null=True)  # Field name made lowercase.
    d02a1apost = models.CharField(db_column='D02A1APOST', max_length=9, blank=True, null=True)  # Field name made lowercase.
    d02a1aalf = models.CharField(db_column='D02A1AALF', max_length=2, blank=True, null=True)  # Field name made lowercase.
    d02a1akn = models.CharField(db_column='D02A1AKN', max_length=40, blank=True, null=True)  # Field name made lowercase.
    d02a1asubd = models.CharField(db_column='D02A1ASUBD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    d02a1acity = models.CharField(db_column='D02A1ACITY', max_length=35, blank=True, null=True)  # Field name made lowercase.
    d02a1astre = models.CharField(db_column='D02A1ASTRE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    d02b_ogrn = models.CharField(db_column='D02B_OGRN', max_length=15, blank=True, null=True)  # Field name made lowercase.
    d02b_inn = models.CharField(db_column='D02B_INN', max_length=12, blank=True, null=True)  # Field name made lowercase.
    d02b_kpp = models.CharField(db_column='D02B_KPP', max_length=9, blank=True, null=True)  # Field name made lowercase.
    d02b_itn = models.CharField(db_column='D02B_ITN', max_length=13, blank=True, null=True)  # Field name made lowercase.
    d02b1 = models.CharField(db_column='D02B1', max_length=150, blank=True, null=True)  # Field name made lowercase.
    d02b2post = models.CharField(db_column='D02B2POST', max_length=9, blank=True, null=True)  # Field name made lowercase.
    d02b21 = models.CharField(db_column='D02B21', max_length=2, blank=True, null=True)  # Field name made lowercase.
    d02b21n = models.CharField(db_column='D02B21N', max_length=40, blank=True, null=True)  # Field name made lowercase.
    d02b2subd = models.CharField(db_column='D02B2SUBD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    d02b2city = models.CharField(db_column='D02B2CITY', max_length=35, blank=True, null=True)  # Field name made lowercase.
    d02b2stree = models.CharField(db_column='D02B2STREE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    d02b81 = models.CharField(db_column='D02B81', max_length=7, blank=True, null=True)  # Field name made lowercase.
    d02b81a = models.CharField(db_column='D02B81A', max_length=15, blank=True, null=True)  # Field name made lowercase.
    d02b821 = models.CharField(db_column='D02B821', max_length=11, blank=True, null=True)  # Field name made lowercase.
    d02b822 = models.CharField(db_column='D02B822', max_length=25, blank=True, null=True)  # Field name made lowercase.
    d02b823 = models.CharField(db_column='D02B823', max_length=150, blank=True, null=True)  # Field name made lowercase.
    d02b83 = models.DateTimeField(db_column='D02B83', blank=True, null=True)  # Field name made lowercase.
    d02b1a = models.CharField(db_column='D02B1A', max_length=150, blank=True, null=True)  # Field name made lowercase.
    d02b1akpp = models.CharField(db_column='D02B1AKPP', max_length=9, blank=True, null=True)  # Field name made lowercase.
    d02b1apost = models.CharField(db_column='D02B1APOST', max_length=9, blank=True, null=True)  # Field name made lowercase.
    d02b1aalf = models.CharField(db_column='D02B1AALF', max_length=2, blank=True, null=True)  # Field name made lowercase.
    d02b1akn = models.CharField(db_column='D02B1AKN', max_length=40, blank=True, null=True)  # Field name made lowercase.
    d02b1asubd = models.CharField(db_column='D02B1ASUBD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    d02b1acity = models.CharField(db_column='D02B1ACITY', max_length=35, blank=True, null=True)  # Field name made lowercase.
    d02b1astre = models.CharField(db_column='D02B1ASTRE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    d07a = models.CharField(db_column='D07A', max_length=1, blank=True, null=True)  # Field name made lowercase.
    d07b = models.CharField(db_column='D07B', max_length=1, blank=True, null=True)  # Field name made lowercase.
    d07c = models.CharField(db_column='D07C', max_length=1, blank=True, null=True)  # Field name made lowercase.
    d08a = models.CharField(db_column='D08A', max_length=1, blank=True, null=True)  # Field name made lowercase.
    d08b = models.CharField(db_column='D08B', max_length=1, blank=True, null=True)  # Field name made lowercase.
    d09a = models.CharField(db_column='D09A', max_length=1, blank=True, null=True)  # Field name made lowercase.
    d09b = models.CharField(db_column='D09B', max_length=1, blank=True, null=True)  # Field name made lowercase.
    koldopl = models.IntegerField(db_column='KOLDOPL', blank=True, null=True)  # Field name made lowercase.
    g542 = models.DateTimeField(db_column='G542', blank=True, null=True)  # Field name made lowercase.
    g543 = models.CharField(db_column='G543', max_length=4, blank=True, null=True)  # Field name made lowercase.
    g5441 = models.CharField(db_column='G5441', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g5441nm = models.CharField(db_column='G5441NM', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g5441mdnm = models.CharField(db_column='G5441MDNM', max_length=150, blank=True, null=True)  # Field name made lowercase.
    g5442 = models.CharField(db_column='G5442', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g5447 = models.CharField(db_column='G5447', max_length=50, blank=True, null=True)  # Field name made lowercase.
    g5451 = models.CharField(db_column='G5451', max_length=7, blank=True, null=True)  # Field name made lowercase.
    g5451a = models.CharField(db_column='G5451A', max_length=15, blank=True, null=True)  # Field name made lowercase.
    g5451b = models.CharField(db_column='G5451B', max_length=11, blank=True, null=True)  # Field name made lowercase.
    g5452 = models.CharField(db_column='G5452', max_length=25, blank=True, null=True)  # Field name made lowercase.
    g5453 = models.DateTimeField(db_column='G5453', blank=True, null=True)  # Field name made lowercase.
    g5454 = models.CharField(db_column='G5454', max_length=150, blank=True, null=True)  # Field name made lowercase.
    valdat = models.DateTimeField(db_column='VALDAT', blank=True, null=True)  # Field name made lowercase.
    tamst_kodv = models.CharField(db_column='TAMST_KODV', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tamst_kurs = models.FloatField(default=0.00, db_column='TAMST_KURS', blank=True, null=True)  # Field name made lowercase.
    dc10 = models.CharField(db_column='DC10', max_length=2, blank=True, null=True)  # Field name made lowercase.
    dc11 = models.DateTimeField(db_column='DC11', blank=True, null=True)  # Field name made lowercase.
    dc12 = models.CharField(db_column='DC12', max_length=4, blank=True, null=True)  # Field name made lowercase.
    dc12d = models.DateTimeField(db_column='DC12D', blank=True, null=True)  # Field name made lowercase.
    dc20 = models.CharField(db_column='DC20', max_length=2, blank=True, null=True)  # Field name made lowercase.
    dc22 = models.CharField(db_column='DC22', max_length=4, blank=True, null=True)  # Field name made lowercase.
    dc22d = models.DateTimeField(db_column='DC22D', blank=True, null=True)  # Field name made lowercase.
    dc30 = models.CharField(db_column='DC30', max_length=2, blank=True, null=True)  # Field name made lowercase.
    dc32 = models.CharField(db_column='DC32', max_length=4, blank=True, null=True)  # Field name made lowercase.
    dc32d = models.DateTimeField(db_column='DC32D', blank=True, null=True)  # Field name made lowercase.
    nzp = models.DecimalField(default=0.00, db_column='NZP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dmodify = models.DateTimeField(db_column='DMODIFY', blank=True, null=True)  # Field name made lowercase.
    tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    p_edoc_id = models.DecimalField(default=0.00, db_column='P_EDOC_ID', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    guid = models.CharField(db_column='GUID', max_length=38, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=28, blank=True, null=True)  # Field name made lowercase.
    d012build = models.CharField(db_column='D012BUILD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    d011abuild = models.CharField(db_column='D011ABUILD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    d02a2build = models.CharField(db_column='D02A2BUILD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    d02a1build = models.CharField(db_column='D02A1BUILD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    d02b2build = models.CharField(db_column='D02B2BUILD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    d02b1build = models.CharField(db_column='D02B1BUILD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    d0184 = models.DateTimeField(db_column='D0184', blank=True, null=True)  # Field name made lowercase.
    d02a84 = models.DateTimeField(db_column='D02A84', blank=True, null=True)  # Field name made lowercase.
    d02b84 = models.DateTimeField(db_column='D02B84', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'SBRHEAD'


class Sbrsscv(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    num_pp = models.SmallIntegerField(db_column='NUM_PP', blank=True, null=True)  # Field name made lowercase.
    g32 = models.IntegerField(db_column='G32', blank=True, null=True)  # Field name made lowercase.
    npoz = models.CharField(db_column='NPOZ', max_length=3, blank=True, null=True)  # Field name made lowercase.
    valsum = models.DecimalField(default=0.00, db_column='VALSUM', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valkod = models.CharField(db_column='VALKOD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    valkurs = models.FloatField(default=0.00, db_column='VALKURS', blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=28, blank=True, null=True)  # Field name made lowercase.
    valdate = models.DateTimeField(db_column='VALDATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'SBRSSCV'


class Sbrsstc(BaseModel):
    # g071 = models.CharField(db_column='G071', max_length=8, blank=True, null=True)  # Field name made lowercase.
    g072 = models.DateTimeField(db_column='G072', blank=True, null=True)  # Field name made lowercase.
    g073 = models.CharField(db_column='G073', max_length=7, blank=True, null=True)  # Field name made lowercase.
    num_pp = models.SmallIntegerField(db_column='NUM_PP', blank=True, null=True)  # Field name made lowercase.
    ch = models.IntegerField(db_column='CH', blank=True, null=True)  # Field name made lowercase.
    ch1 = models.SmallIntegerField(db_column='CH1', blank=True, null=True)  # Field name made lowercase.
    g32 = models.IntegerField(db_column='G32', blank=True, null=True)  # Field name made lowercase.
    nmet = models.CharField(db_column='NMET', max_length=2, blank=True, null=True)  # Field name made lowercase.
    nmet6 = models.CharField(db_column='NMET6', max_length=1, blank=True, null=True)  # Field name made lowercase.
    d11_v = models.DecimalField(default=0.00, db_column='D11_V', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    d11_kodv = models.CharField(db_column='D11_KODV', max_length=3, blank=True, null=True)  # Field name made lowercase.
    d11_r = models.DecimalField(default=0.00, db_column='D11_R', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    d11_kurs = models.FloatField(default=0.00, db_column='D11_KURS', blank=True, null=True)  # Field name made lowercase.
    d11b_r = models.DecimalField(default=0.00, db_column='D11B_R', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    d11b_kodv = models.CharField(db_column='D11B_KODV', max_length=3, blank=True, null=True)  # Field name made lowercase.
    d11b_kurs = models.FloatField(default=0.00, db_column='D11B_KURS', blank=True, null=True)  # Field name made lowercase.
    d11 = models.DecimalField(default=0.00, db_column='D11', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    d12 = models.DecimalField(default=0.00, db_column='D12', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    d12a = models.DecimalField(default=0.00, db_column='D12A', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    d12b = models.DecimalField(default=0.00, db_column='D12B', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    d12c = models.DecimalField(default=0.00, db_column='D12C', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    d12d = models.DecimalField(default=0.00, db_column='D12D', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    d12e = models.DecimalField(default=0.00, db_column='D12E', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    d12f = models.DecimalField(default=0.00, db_column='D12F', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    d13 = models.DecimalField(default=0.00, db_column='D13', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    d13a = models.DecimalField(default=0.00, db_column='D13A', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    d13b = models.DecimalField(default=0.00, db_column='D13B', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    d14 = models.DecimalField(default=0.00, db_column='D14', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    d14a = models.DecimalField(default=0.00, db_column='D14A', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    d14b = models.DecimalField(default=0.00, db_column='D14B', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    d14c = models.DecimalField(default=0.00, db_column='D14C', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    d14d = models.DecimalField(default=0.00, db_column='D14D', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    d14e = models.DecimalField(default=0.00, db_column='D14E', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    d15 = models.DecimalField(default=0.00, db_column='D15', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    d16 = models.DecimalField(default=0.00, db_column='D16', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    d16a = models.DecimalField(default=0.00, db_column='D16A', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    d16b = models.DecimalField(default=0.00, db_column='D16B', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    d17 = models.DecimalField(default=0.00, db_column='D17', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    d17a = models.DecimalField(default=0.00, db_column='D17A', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    d17b = models.DecimalField(default=0.00, db_column='D17B', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    d18 = models.DecimalField(default=0.00, db_column='D18', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    d19 = models.DecimalField(default=0.00, db_column='D19', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    d20 = models.DecimalField(default=0.00, db_column='D20', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    d21 = models.DecimalField(default=0.00, db_column='D21', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    d22 = models.DecimalField(default=0.00, db_column='D22', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    d23 = models.DecimalField(default=0.00, db_column='D23', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    d24 = models.DecimalField(default=0.00, db_column='D24', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    d_ei = models.CharField(db_column='D_EI', max_length=3, blank=True, null=True)  # Field name made lowercase.
    d_eiio = models.CharField(db_column='D_EIIO', max_length=3, blank=True, null=True)  # Field name made lowercase.
    d_mpmn = models.CharField(db_column='D_MPMN', max_length=40, blank=True, null=True)  # Field name made lowercase.
    d_mp = models.CharField(db_column='D_MP', max_length=40, blank=True, null=True)  # Field name made lowercase.
    d_mpio = models.CharField(db_column='D_MPIO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    d_mp2 = models.CharField(db_column='D_MP2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    d_mpio2 = models.CharField(db_column='D_MPIO2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tamst_r = models.DecimalField(default=0.00, db_column='TAMST_R', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tamst_v = models.DecimalField(default=0.00, db_column='TAMST_V', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dc10 = models.CharField(db_column='DC10', max_length=2, blank=True, null=True)  # Field name made lowercase.
    dc11 = models.DateTimeField(db_column='DC11', blank=True, null=True)  # Field name made lowercase.
    dc12 = models.CharField(db_column='DC12', max_length=4, blank=True, null=True)  # Field name made lowercase.
    dc12d = models.DateTimeField(db_column='DC12D', blank=True, null=True)  # Field name made lowercase.
    dc20 = models.CharField(db_column='DC20', max_length=2, blank=True, null=True)  # Field name made lowercase.
    dc22 = models.CharField(db_column='DC22', max_length=4, blank=True, null=True)  # Field name made lowercase.
    dc22d = models.DateTimeField(db_column='DC22D', blank=True, null=True)  # Field name made lowercase.
    dc30 = models.CharField(db_column='DC30', max_length=2, blank=True, null=True)  # Field name made lowercase.
    dc32 = models.CharField(db_column='DC32', max_length=4, blank=True, null=True)  # Field name made lowercase.
    dc32d = models.DateTimeField(db_column='DC32D', blank=True, null=True)  # Field name made lowercase.
    nzp = models.DecimalField(default=0.00, db_column='NZP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dmodify = models.DateTimeField(db_column='DMODIFY', blank=True, null=True)  # Field name made lowercase.
    tmodify = models.CharField(db_column='TMODIFY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    p_edoc_id = models.DecimalField(default=0.00, db_column='P_EDOC_ID', max_digits=19, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    d_tnved = models.CharField(db_column='D_TNVED', max_length=10, blank=True, null=True)  # Field name made lowercase.
    d_cod4 = models.CharField(db_column='D_COD4', max_length=4, blank=True, null=True)  # Field name made lowercase.
    d_brutto = models.DecimalField(default=0.00, db_column='D_BRUTTO', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    d_netto = models.DecimalField(default=0.00, db_column='D_NETTO', max_digits=19, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    # docnum = models.CharField(db_column='DocNum', max_length=28, blank=True, null=True)  # Field name made lowercase.
    valdat = models.DateTimeField(db_column='VALDAT', blank=True, null=True)  # Field name made lowercase.
    tamst_kodv = models.CharField(db_column='TAMST_KODV', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tamst_kurs = models.FloatField(default=0.00, db_column='TAMST_KURS', blank=True, null=True)  # Field name made lowercase.
    d11_kurd = models.DateTimeField(db_column='D11_KURD', blank=True, null=True)  # Field name made lowercase.
    d11b_kurd = models.DateTimeField(db_column='D11B_KURD', blank=True, null=True)  # Field name made lowercase.
    cucostdate = models.DateTimeField(db_column='CUCOSTDATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'SBRSSTC'


class Version(BaseModel):
    program = models.CharField(db_column='Program', primary_key=True, max_length=255)  # Field name made lowercase.
    dbver = models.CharField(db_column='DBVer', max_length=50)  # Field name made lowercase.
    exever = models.CharField(db_column='ExeVer', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        abstract = True
        # db_table = 'Version'
