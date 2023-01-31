from src.apps.nsiexport.base.models import (
    AddDoc, Address, AdpPrim, AkcPrim, AllIncl,
    AllOper, ArxReg, AtdPos, Autonz, BankIzm,
    Banklist, BartPc, BgDp, Bignalog,
    Bignalto, Bkbkn, Blank, Bmonth, Bnkseek, Brok,
    Bx, Car, Carrier, Carrierb, CbContr, Chkpoint,
    Cntr, CrV, Crdts, CtovR, Ctu, Currency, Custlist,
    Customs, Custpost, D44MPr, D44MTn, D44Mask,
    D44Sfoiv, Declrnt, Delstakc,
    DipPrim, Dnbdlist, Dobstakc, DocAmts, DocPr,
    DocTnv, Docg44, Docum, Document, DohNepr, DohOsn,
    DolgAll, Dov, Dtamreg, Ecop, Ecop1, Ecop2,
    Ecop3, Ecop4, Ecop5, Edizm, EdizmDp, EkAr, EkEu,
    ExpPrim, Experimt, Expstakc, ExtremM, FaItemc,
    FaPredm, Finbg, Finbg0, Fmtk, Formras, FstRaz, FstZakl,
    Garant, GdOtd, GdStan, GeoAr, Grp, Hold, ImpPrim,
    InFirm, IndicEf, Indnsi, Inf1Td, InfEais, Infram,
    Izgot, Kat, Kateg, Kategwar, Katt, Kkk, Kl203B,
    Kl203E, Kl203I, Kl204, Kl204B, Kl204Ing, KlStav,
    Klass203, Klass204, Klass205, KlirVal, Kliring,
    KodG300, Kodkdt, Kodktc, Komop, Kray, Ktam, Ktam1,
    Ktam2, Ktamatr, Ktamolap, Ktamold, Ktddl, Kvota,
    Kvz, LgotUv, LicTi, LicTov, LicTv, LocKntr, LostTir,
    MarAkc, Maxstakc, MdpAdr, MdpD, MdpKont, Measures,
    Mintnv, Mnt, MosKtam, Motc, Motsfl, Mps, Mpsreg,
    MrkCar, MrkCars, Namefirm, Nar, NarVtt, NewTi,
    Nlstmpr, Npech, NprsSbj, NsDolgn, NsDul, NsDulT,
    NsDulV, NsGr31, NsMpo, NsOd31, NsTsfl, NsiKbk,
    NullstB, O803, Object0, Ofdoc,
    Ogovorka, OkaPk38, OkaPk44, OkaPk48, OkaPk65,
    OkaPk66, OkaPk72, OkaPk75, OkaPk76, OkaPk79,
    OkaPk82, OkaPk83, OkaPk84, OkaPk85, OkaPk86,
    OkaPk87, OkaPk88, OkaPk89, Okato, Okatosrf, Oksmt,
    OprMeas, OrgNpr, Ortov, Osdelka, Osf, Ostamplt,
    Ostamplu, Otamreg, Otr, Outp, Ozvet, Pasport, Pech,
    PechDel, PechKpv, Pechvid, PedhDel, PermSch, Permit,
    Plbase, PlomDel, Plombir, PointDa, PointIn, PointNe,
    PointOp, PointRe, Poluch, Pravo, Predresh, Price,
    Price10, Priceg, PrimAdp, PrimBg, PrimBzp, PrimKod,
    PrimLec, PrimLic, PrimMrk, PrimNdc, PrimPr0, PrimPrf,
    PrimPry, PrimSpr, PrimSt1, PrmCont, Prstate, PzkOrd, Ram,
    RdBg872, Re12Tm, ReAct, ReArhiv, ReDeist, ReDelo, ReDopps,
    ReDoprv, ReLi, ReLsoi, ReLsov, ReLv, ReMist, RePost,
    RePrich, ReRvto, ReSttk, ReTmist, ReZalob, Recom,
    Reg, RegK, RegMvs, RegS, RegTi, RegTi1, RegTit,
    RegiK, Regpltls, RegtiTe, Reshdel, Rezultto, Rezultto1,
    Rmbt, Rmd, RmdG, Rmtotok, Role, Rpsi, RskCrit, RskFinp,
    RskMera, RskNdpd, RskNinf, RskNmb, RskNpm, RskPrim,
    RskRsmr, RskRsnd, RskRspr, RskSpdr0, RskTprc, Rskrmera,
    Rskrsdsm, Rskrsprc, Rskspdr, Rsksppri, Rsktmera, Rskxdosm,
    Rskzdosm, RsnBpos, RsnBuss, RsnCntr, RsnEntf, RsnEntr,
    RsnFlab, RsnOrg, RsnOrgt, RsnProd, RsnSpro, RsnTarg, RsnTdep,
    RsnTsto, RsnUnit, RsnVlab, RstrH, RstrKat, RstrLic,
    RstrN, RstrOis, RstrTov, RstrTz, Rstrpath, SExhib, SExhid,
    SObutp, Sbj, SbjCst, SbjExt, SbjRole, SbxDel, Sdelka, Selfnsi1,
    SertS, Sertif, Sertif4, SezPrim, SklStt, Sklad,
    Skladbx, SkladtB, Skladtm, SkladvB, Skrecc, Soato, Sokr,
    Sono, Soun1, Source, SpTovW, SpcPrim, Spcproc, SpzkRsn, SrsnRtn,
    Stack, StmDel, Strana, Stt, Subject, Subject0, Sutp, SysKtpt, TDoc,
    Tab47B, Tabnar, Tam, Tamplat, Tamplat0, Tampred, Tampred1, Tampred2,
    Tampred3, Tampred4, Tamst, Tamstavt, Tbrok, Tbrok1, Tbrok2,
    Tbrok3, Tbrok4, Tbrok5, Tbrok6, Tbrok7, Tbrok8, Tipdv, Tipts,
    TiptsS, Tk, Tk1, Tndti14, TnvLtd, TnvStav, Tnved, Tnved1,
    Tnved2, Tnved3, Tnved4, Tnved6, Tnved8, Tnved9, TovW, Tovsign,
    TpoPlt, Trans, Ts, Tsk, Tskat, Upravl, Uslpost, Utilsbor, V2,
    VObup, Val, ValCen, Valname, Valuta, VidAmts, VidDoc, Viddvig,
    Vidtrans, Vidupak, Vkortd, Vkvot, Vpertr, Vspupr, VtsTov, VtsZakl,
    Waybill, Year, Zan, Zvet,
)
from django.db import models
from src.apps.common.mixins import ExtBase


class TAddDoc(AddDoc):
    doc_id = models.CharField(max_length=4, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'add_doc'


class TAddress(Address):
    subject_id = models.DecimalField(default=0.00, max_digits=18, decimal_places=9, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'address'


class TAdpPrim(AdpPrim):
    kodt = models.CharField(max_length=10, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'adp_prim'


class TAkcPrim(AkcPrim):
    kodt = models.CharField(max_length=10, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'akc_prim'


class TAllIncl(AllIncl):
    inclusionn = models.CharField(max_length=200, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'all_incl'


class TAllOper(AllOper):
    operationn = models.CharField(max_length=100, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'all_oper'


class TArxReg(ArxReg):
    inn = models.CharField(max_length=12, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'arx_reg'


class TAtdPos(AtdPos):
    code = models.CharField(max_length=4, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'atd_pos'


class TAutonz(Autonz):
    reg_number = models.CharField(max_length=26, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'autonz'


class TBankIzm(BankIzm):
    kod_izm = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'bank_izm'


class TBanklist(Banklist):
    kod = models.CharField(max_length=7, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'banklist'


class TBartPc(BartPc):
    pb_innu = models.CharField(max_length=10, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'bart_pc'


class TBgDp(BgDp):
    docno = models.CharField(max_length=19, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'bg_dp'


class TBignalog(Bignalog):
    plt_inn = models.CharField(max_length=12, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'bignalog'


class TBignalto(Bignalto):
    plt_inn = models.CharField(max_length=12, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'bignalto'


class TBkbkn(Bkbkn):
    nom = models.DecimalField(default=0.00, max_digits=2, decimal_places=0, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'bkbkn'


class TBlank(Blank):
    numblank = models.CharField(max_length=11, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'blank'


class TBmonth(Bmonth):
    kod = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'bmonth'


class TBnkseek(Bnkseek):
    nnp = models.CharField(max_length=25, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'bnkseek'


class TBrok(Brok):
    sbj_id = models.DecimalField(default=0.00, max_digits=15, decimal_places=0, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'brok'


class TBx(Bx):
    sbj_id = models.DecimalField(default=0.00, max_digits=15, decimal_places=0, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'bx'


class TCar(Car):
    sbj_id = models.DecimalField(default=0.00, max_digits=15, decimal_places=0, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'car'


class TCarrier(Carrier):
    nlic = models.CharField(max_length=25, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'carrier'


class TCarrierb(Carrierb):
    nlic = models.CharField(max_length=15, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'carrierb'


class TCbContr(CbContr):
    codcontr = models.CharField(max_length=1, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'cb_contr'


class TChkpoint(Chkpoint):
    code = models.CharField(max_length=8, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'chkpoint'


class TCntr(Cntr):
    cntr = models.CharField(max_length=20, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'cntr'


class TCrV(CrV):
    code = models.CharField(max_length=3, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'cr_v'


class TCrdts(Crdts):
    numcard = models.CharField(max_length=20, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'crdts'


class TCtovR(CtovR):
    code = models.CharField(max_length=3, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'ctov_r'


class TCtu(Ctu):
    code = models.CharField(max_length=8, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'ctu'


class TCurrency(Currency):
    kod = models.DecimalField(default=0.00, max_digits=3, decimal_places=0, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'currency'


class TCustlist(Custlist):
    code = models.CharField(max_length=8, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'custlist'


class TCustoms(Customs):
    customs = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'customs'


class TCustpost(Custpost):
    custom = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'custpost'


class TD44MPr(D44MPr):
    kod = models.CharField(max_length=5, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'd44_m_pr'


class TD44MTn(D44MTn):
    kod = models.CharField(max_length=5, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'd44_m_tn'


class TD44Mask(D44Mask):
    kod = models.CharField(max_length=5, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'd44_mask'


class TD44Sfoiv(D44Sfoiv):
    kod = models.CharField(max_length=5, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'd44sfoiv'


class TDeclrnt(Declrnt):
    nlic = models.CharField(max_length=15, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'declrnt'


class TDelstakc(Delstakc):
    kodtov = models.CharField(max_length=10, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'delstakc'


class TDipPrim(DipPrim):
    kodt = models.CharField(max_length=10, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'dip_prim'


class TDnbdlist(Dnbdlist):
    id_num = models.CharField(max_length=18, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'dnbdlist'


class TDobstakc(Dobstakc):
    npric = models.CharField(max_length=20, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'dobstakc'


class TDocAmts(DocAmts):
    kod = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'doc_amts'


class TDocPr(DocPr):
    kod = models.DecimalField(default=0.00, max_digits=2, decimal_places=0, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'doc_pr'


class TDocTnv(DocTnv):
    code1 = models.CharField(max_length=10, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'doc_tnv'


class TDocg44(Docg44):
    kod = models.CharField(max_length=5, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'docg44'


class TDocum(Docum):
    cod = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'docum'


class TDocument(Document):
    doc_id = models.CharField(max_length=4, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'document'


class TDohNepr(DohNepr):
    kod = models.CharField(max_length=3, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'doh_nepr'


class TDohOsn(DohOsn):
    kod = models.CharField(max_length=3, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'doh_osn'


class TDolgAll(DolgAll):
    kod = models.CharField(max_length=8, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'dolg_all'


# class TDolgt(Dolgt):
#     kod = models.CharField(db_column='KOD', max_length=8, blank=True, primary_key=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'dolgt'


class TDov(Dov):
    inn = models.CharField(max_length=20, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'dov'


class TDtamreg(Dtamreg):
    kod = models.CharField(max_length=3, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'dtamreg'


class TEcop(Ecop):
    nlic = models.CharField(max_length=25, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'ecop'


class TEcop1(Ecop1):
    nlic = models.CharField(max_length=25, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'ecop1'


class TEcop2(Ecop2):
    nlic = models.CharField(max_length=25, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'ecop2'


class TEcop3(Ecop3):
    nlic = models.CharField(max_length=25, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'ecop3'


class TEcop4(Ecop4):
    nlic = models.CharField(max_length=25, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'ecop4'


class TEcop5(Ecop5):
    nlic = models.CharField(max_length=25, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'ecop5'


class TEdizm(Edizm):
    kod = models.CharField(max_length=3, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'edizm'


class TEdizmDp(EdizmDp):
    kod = models.CharField(max_length=3, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'edizm_dp'


class TEkAr(EkAr):
    kod_ar = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'ek_ar'


class TEkEu(EkEu):
    kod_ar = models.CharField(max_length=14, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'ek_eu'


class TExpPrim(ExpPrim):
    kodt = models.CharField(max_length=10, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'exp_prim'


class TExperimt(Experimt):
    kodt = models.CharField(max_length=8, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'experimt'


class TExpstakc(Expstakc):
    inn = models.CharField(max_length=12, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'expstakc'


class TExtremM(ExtremM):
    reg_num = models.DecimalField(default=0.00, max_digits=16, decimal_places=0, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'extrem_m'


class TFaItemc(FaItemc):
    kod = models.CharField(max_length=8, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'fa_itemc'


class TFaPredm(FaPredm):
    ident = models.CharField(max_length=8, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'fa_predm'


class TFinbg(Finbg):
    kod = models.CharField(max_length=20, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'finbg'


class TFinbg0(Finbg0):
    kod = models.CharField(max_length=7, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'finbg_'


class TFmtk(Fmtk):
    kod_rec = models.CharField(max_length=6, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'fmtk'


class TFormras(Formras):
    kod = models.CharField(max_length=1, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'formras'


class TFstRaz(FstRaz):
    n_razr = models.CharField(max_length=20, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'fst_raz'


class TFstZakl(FstZakl):
    n_zakl = models.CharField(max_length=20, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'fst_zakl'


class TGarant(Garant):
    codegar = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'garant'


class TGdOtd(GdOtd):
    kodotd = models.CharField(max_length=4, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'gd_otd'


class TGdStan(GdStan):
    code = models.CharField(max_length=8, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'gd_stan'


class TGeoAr(GeoAr):
    pr_reg = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'geo_ar'


class TGrp(Grp):
    id = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'grp'


class THold(Hold):
    kod = models.DecimalField(default=0.00, max_digits=2, decimal_places=0, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'hold'


class TImpPrim(ImpPrim):
    kodt = models.CharField(max_length=10, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'imp_prim'


class TInFirm(InFirm):
    country = models.CharField(max_length=3, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'in_firm'


class TIndicEf(IndicEf):
    kodt = models.CharField(max_length=10, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'indic_ef'


class TIndnsi(Indnsi):
    lib = models.CharField(max_length=4, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'indnsi'


class TInf1Td(Inf1Td):
    kod = models.CharField(max_length=3, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'inf1td'


class TInfEais(InfEais):
    cust_code = models.CharField(max_length=8, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'inf_eais'


class TInfram(Infram):
    kod = models.CharField(max_length=9, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'infram'


class TIzgot(Izgot):
    mki = models.CharField(max_length=3, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'izgot'


class TKat(Kat):
    nomr3 = models.CharField(max_length=8, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'kat'


class TKateg(Kateg):
    kod = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'kateg'


class TKategwar(Kategwar):
    kateg = models.CharField(max_length=4, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'kategwar'


class TKatt(Katt):
    kod = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'katt'


class TKkk(Kkk):
    kodt = models.CharField(max_length=5, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'kkk'


class TKl203B(Kl203B):
    kod = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'kl203b'


class TKl203E(Kl203E):
    kod = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'kl203e'


class TKl203I(Kl203I):
    kod = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'kl203i'


class TKl204(Kl204):
    kod = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'kl204'


class TKl204B(Kl204B):
    kod = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'kl204b'


class TKl204Ing(Kl204Ing):
    kod = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'kl204ing'


class TKlStav(KlStav):
    stav = models.DecimalField(default=0.00, max_digits=7, decimal_places=4, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'kl_stav'


class TKlass203(Klass203):
    kod = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'klass203'


class TKlass204(Klass204):
    kod = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'klass204'


class TKlass205(Klass205):
    kod = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'klass205'


class TKlirVal(KlirVal):
    kod = models.CharField(max_length=3, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'klir_val'


class TKliring(Kliring):
    kod_kl = models.CharField(max_length=3, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'kliring'


class TKodG300(KodG300):
    kod = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'kod_g300'


class TKodkdt(Kodkdt):
    kod = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'kodkdt'


class TKodktc(Kodktc):
    kod = models.CharField(max_length=1, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'kodktc'


class TKomop(Komop):
    kod = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'komop'


class TKray(Kray):
    pole1 = models.CharField(max_length=3, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'kray'


class TKtam(Ktam):
    code = models.CharField(max_length=8, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'ktam'


class TKtam1(Ktam1):
    code = models.CharField(max_length=8, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'ktam1'


class TKtam2(Ktam2):
    code = models.CharField(max_length=8, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'ktam2'


class TKtamatr(Ktamatr):
    code = models.CharField(max_length=1, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'ktamatr'


class TKtamolap(Ktamolap):
    child = models.CharField(max_length=8, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'ktamolap'


class TKtamold(Ktamold):
    code = models.CharField(max_length=8, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'ktamold'


class TKtddl(Ktddl):
    lnpdl = models.CharField(max_length=4, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'ktddl'


class TKvota(Kvota):
    kod_tnved = models.CharField(max_length=10, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'kvota'


class TKvz(Kvz):
    v_vz = models.CharField(max_length=3, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'kvz'


class TLgotUv(LgotUv):
    kod = models.CharField(max_length=1, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'lgot_uv'


class TLicTi(LicTi):
    nomlic = models.CharField(max_length=17, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'lic_ti'


class TLicTov(LicTov):
    code = models.CharField(max_length=3, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'lic_tov'


class TLicTv(LicTv):
    nomlic = models.CharField(max_length=17, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'lic_tv'


class TLocKntr(LocKntr):
    code = models.CharField(max_length=250, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'loc_kntr'


class TLostTir(LostTir):
    n_mdp = models.CharField(max_length=10, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'lost_tir'


class TMarAkc(MarAkc):
    kod = models.CharField(max_length=1, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'mar_akc'


class TMaxstakc(Maxstakc):
    mst_ak = models.DecimalField(default=0.00, max_digits=10, decimal_places=3, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'maxstakc'


class TMdpAdr(MdpAdr):
    checkcod = models.CharField(max_length=18, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'mdp_adr'


class TMdpD(MdpD):
    checkcod = models.CharField(max_length=18, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'mdp_d'


class TMdpKont(MdpKont):
    checkcod = models.CharField(max_length=18, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'mdp_kont'


class TMeasures(Measures):
    code = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'measures'


class TMintnv(Mintnv):
    kodg = models.CharField(max_length=4, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'mintnv'


class TMnt(Mnt):
    kod = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'mnt'


class TMosKtam(MosKtam):
    kodt = models.CharField(max_length=5, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'mos_ktam'


class TMotc(Motc):
    code = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'motc'


class TMotsfl(Motsfl):
    kodt = models.CharField(max_length=8, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'motsfl'


class TMps(Mps):
    kodstan = models.CharField(max_length=5, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'mps'


class TMpsreg(Mpsreg):
    kodstan = models.CharField(max_length=5, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'mpsreg'


class TMrkCar(MrkCar):
    kodmrk = models.CharField(max_length=3, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'mrk_car'


class TMrkCars(MrkCars):
    kodmrk = models.CharField(max_length=3, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'mrk_cars'


class TNamefirm(Namefirm):
    regn = models.CharField(max_length=3, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'namefirm'


class TNar(Nar):
    nar = models.CharField(max_length=12, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'nar'


class TNarVtt(NarVtt):
    inn = models.CharField(max_length=12, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'nar_vtt'


class TNewTi(NewTi):
    nomlic = models.CharField(max_length=17, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'new_ti'


class TNlstmpr(Nlstmpr):
    reason = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'nlstmpr'


class TNpech(Npech):
    ktam = models.CharField(max_length=8, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'npech'


class TNprsSbj(NprsSbj):
    sbj_id = models.DecimalField(default=0.00, max_digits=15, decimal_places=0, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'nprs_sbj'


class TNsDolgn(NsDolgn):
    inn = models.CharField(max_length=12, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'ns_dolgn'


class TNsDul(NsDul):
    kod = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'ns_dul'


class TNsDulT(NsDulT):
    kod = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'ns_dul_t'


class TNsDulV(NsDulV):
    kod_v = models.CharField(max_length=3, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'ns_dul_v'


class TNsGr31(NsGr31):
    kodt1 = models.CharField(max_length=10, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'ns_gr31'


class TNsMpo(NsMpo):
    code1 = models.CharField(max_length=8, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'ns_mpo'


class TNsOd31(NsOd31):
    kodt = models.CharField(max_length=10, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'ns_od31'


class TNsTsfl(NsTsfl):
    code = models.CharField(max_length=8, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'ns_tsfl'


class TNsiKbk(NsiKbk):
    kbk = models.CharField(max_length=20, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'nsi_kbk'


class TNullstB(NullstB):
    custom = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'nullst_b'


class TO803(O803):
    kodt = models.CharField(max_length=8, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'o803'


class TObject0(Object0):
    kodt = models.CharField(max_length=8, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'object'


class TOfdoc(Ofdoc):
    kod = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'ofdoc'


class TOgovorka(Ogovorka):
    code = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'ogovorka'


class TOkaPk38(OkaPk38):
    ter = models.CharField(max_length=3, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'oka-pk38'


class TOkaPk44(OkaPk44):
    ter = models.CharField(max_length=3, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'oka-pk44'


class TOkaPk48(OkaPk48):
    ter = models.CharField(max_length=3, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'oka-pk48'


class TOkaPk65(OkaPk65):
    ter = models.CharField(max_length=3, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'oka-pk65'


class TOkaPk66(OkaPk66):
    ter = models.CharField(max_length=3, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'oka-pk66'


class TOkaPk72(OkaPk72):
    ter = models.CharField(max_length=3, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'oka-pk72'


class TOkaPk75(OkaPk75):
    ter = models.CharField(max_length=3, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'oka-pk75'


class TOkaPk76(OkaPk76):
    ter = models.CharField(max_length=3, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'oka-pk76'


class TOkaPk79(OkaPk79):
    ter = models.CharField(max_length=3, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'oka-pk79'


class TOkaPk82(OkaPk82):
    ter = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'oka_pk82'


class TOkaPk83(OkaPk83):
    ter = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'oka_pk83'


class TOkaPk84(OkaPk84):
    ter = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'oka_pk84'


class TOkaPk85(OkaPk85):
    ter = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'oka_pk85'


class TOkaPk86(OkaPk86):
    ter = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'oka_pk86'


class TOkaPk87(OkaPk87):
    ter = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'oka_pk87'


class TOkaPk88(OkaPk88):
    ter = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'oka_pk88'


class TOkaPk89(OkaPk89):
    ter = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'oka_pk89'


class TOkato(Okato):
    ter = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'okato'


class TOkatosrf(Okatosrf):
    kodsrf = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'okatosrf'


class TOksmt(Oksmt):
    kod = models.CharField(max_length=3, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'oksmt'


class TOprMeas(OprMeas):
    code = models.CharField(max_length=6, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'opr_meas'


class TOrgNpr(OrgNpr):
    code = models.CharField(max_length=8, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'org_npr'


class TOrtov(Ortov):
    kod = models.CharField(max_length=1, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'ortov'


class TOsdelka(Osdelka):
    kod = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'osdelka'


class TOsf(Osf):
    code = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'osf'


class TOstamplt(Ostamplt):
    kod = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'ostamplt'


class TOstamplu(Ostamplu):
    kod = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'ostamplu'


class TOtamreg(Otamreg):
    kod = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'otamreg'


class TOtr(Otr):
    otr = models.CharField(max_length=30, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'otr'


class TOutp(Outp):
    kod = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'outp'


class TOzvet(Ozvet):
    kod = models.CharField(max_length=1, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'ozvet'


class TPasport(Pasport):
    p_inn = models.CharField(max_length=12, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'pasport'


class TPech(Pech):
    ktam = models.CharField(max_length=8, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'pech'


class TPechDel(PechDel):
    ktam = models.CharField(max_length=8, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'pech_del'


class TPechKpv(PechKpv):
    ktam = models.CharField(max_length=8, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'pech_kpv'


class TPechvid(Pechvid):
    pechvid = models.CharField(max_length=1, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'pechvid'


class TPedhDel(PedhDel):
    ktam = models.CharField(max_length=8, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'pedh_del'


class TPermSch(PermSch):
    p_rnum = models.CharField(max_length=18, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'perm_sch'


class TPermit(Permit):
    p_inn = models.CharField(max_length=12, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'permit'


class TPlbase(Plbase):
    p_inn = models.CharField(max_length=12, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'plbase'


class TPlomDel(PlomDel):
    ktam = models.CharField(max_length=8, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'plom_del'


class TPlombir(Plombir):
    ktam = models.CharField(max_length=8, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'plombir'


class TPointDa(PointDa):
    checkpoint = models.CharField(max_length=6, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'point_da'


class TPointIn(PointIn):
    checkpoint = models.CharField(max_length=6, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'point_in'


class TPointNe(PointNe):
    checkpoint = models.CharField(max_length=6, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'point_ne'


class TPointOp(PointOp):
    checkpoint = models.CharField(max_length=6, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'point_op'


class TPointRe(PointRe):
    checkpoint = models.CharField(max_length=6, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'point_re'


class TPoluch(Poluch):
    zayv = models.CharField(max_length=60, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'poluch'


class TPravo(Pravo):
    inn = models.CharField(max_length=12, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'pravo'


class TPredresh(Predresh):
    kodt = models.CharField(max_length=13, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'predresh'


class TPrice(Price):
    cod = models.CharField(max_length=10, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'price'


class TPrice10(Price10):
    cod = models.CharField(max_length=10, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'price10'


class TPriceg(Priceg):
    nd = models.CharField(max_length=23, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'priceg'


class TPrimAdp(PrimAdp):

    class Meta:
        managed = False
        db_table = 'prim_adp'


class TPrimBg(PrimBg):
    kodt = models.CharField(max_length=10, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'prim_bg'


class TPrimBzp(PrimBzp):
    kodt = models.CharField(max_length=10, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'prim_bzp'


class TPrimKod(PrimKod):
    kodt = models.CharField(max_length=10, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'prim_kod'


class TPrimLec(PrimLec):
    kodt = models.CharField(max_length=10, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'prim_lec'


class TPrimLic(PrimLic):
    kodt = models.CharField(max_length=10, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'prim_lic'


class TPrimMrk(PrimMrk):
    kodt = models.CharField(max_length=10, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'prim_mrk'


class TPrimNdc(PrimNdc):
    kodt = models.CharField(max_length=10, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'prim_ndc'


class TPrimPr0(PrimPr0):
    kodt = models.CharField(max_length=10, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'prim_pr0'


class TPrimPrf(PrimPrf):
    kod = models.CharField(max_length=10, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'prim_prf'


class TPrimPry(PrimPry):
    kod = models.CharField(max_length=10, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'prim_pry'


class TPrimSpr(PrimSpr):
    kod = models.CharField(max_length=10, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'prim_spr'


class TPrimSt1(PrimSt1):
    kod = models.CharField(max_length=10, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'prim_st1'


class TPrmCont(PrmCont):
    kodt = models.CharField(max_length=10, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'prm_cont'


class TPrstate(Prstate):
    code = models.CharField(max_length=1, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'prstate'


class TPzkOrd(PzkOrd):
    ref_numd = models.CharField(max_length=20, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'pzk_ord'


class TRam(Ram):
    kod = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'ram'


class TRdBg872(RdBg872):
    kodt = models.CharField(max_length=8, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'rd_bg872'


class TRe12Tm(Re12Tm):
    r1 = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 're_12tm'


class TReAct(ReAct):
    kod = models.DecimalField(default=0.00, max_digits=2, decimal_places=0, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 're_act'


class TReArhiv(ReArhiv):
    god = models.DecimalField(default=0.00, max_digits=4, decimal_places=0, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 're_arhiv'


class TReDeist(ReDeist):
    ntam = models.DecimalField(default=0.00, max_digits=5, decimal_places=0, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 're_deist'


class TReDelo(ReDelo):
    ntam = models.DecimalField(default=0.00, max_digits=5, decimal_places=0, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 're_delo'


class TReDopps(ReDopps):
    ntam = models.DecimalField(default=0.00, max_digits=5, decimal_places=0, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 're_dopps'


class TReDoprv(ReDoprv):
    ntam = models.DecimalField(default=0.00, max_digits=5, decimal_places=0, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 're_doprv'


class TReLi(ReLi):
    ntam = models.DecimalField(default=0.00, max_digits=5, decimal_places=0, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 're_li'


class TReLsoi(ReLsoi):
    ntam = models.DecimalField(default=0.00, max_digits=5, decimal_places=0, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 're_lsoi'


class TReLsov(ReLsov):
    ntam = models.DecimalField(default=0.00, max_digits=5, decimal_places=0, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 're_lsov'


class TReLv(ReLv):
    ntam = models.DecimalField(default=0.00, max_digits=5, decimal_places=0, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 're_lv'


class TReMist(ReMist):
    ntam = models.DecimalField(default=0.00, max_digits=5, decimal_places=0, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 're_mist'


class TRePost(RePost):
    npost = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 're_post'


class TRePrich(RePrich):
    nprich = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 're_prich'


class TReRvto(ReRvto):
    nrvto = models.DecimalField(default=0.00, max_digits=1, decimal_places=0, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 're_rvto'


class TReSttk(ReSttk):
    kodst = models.CharField(max_length=8, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 're_sttk'


class TReTmist(ReTmist):
    kod = models.DecimalField(default=0.00, max_digits=2, decimal_places=0, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 're_tmist'


class TReZalob(ReZalob):
    ntam = models.DecimalField(default=0.00, max_digits=5, decimal_places=0, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 're_zalob'


class TRecom(Recom):
    num_id = models.DecimalField(default=0.00, max_digits=3, decimal_places=0, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'recom'


class TReg(Reg):
    kodtam = models.CharField(max_length=5, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'reg'


class TRegK(RegK):
    reg_nom = models.CharField(max_length=20, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'reg_k'


class TRegMvs(RegMvs):
    okpo = models.CharField(max_length=10, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'reg_mvs'


class TRegS(RegS):
    nomr3 = models.CharField(max_length=10, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'reg_s'


class TRegTi(RegTi):
    kodtam = models.CharField(max_length=8, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'reg_ti'


class TRegTit(RegTit):
    kodtam = models.CharField(max_length=8, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'reg_tit'


class TRegTi1(RegTi1):
    kodtam = models.CharField(max_length=8, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'reg_ti~1'


class TRegiK(RegiK):
    reg_nom = models.CharField(max_length=20, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'regi_k'


class TRegpltls(Regpltls):
    inn = models.CharField(max_length=12, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'regpltls'


class TRegtiTe(RegtiTe):
    inn = models.CharField(max_length=12, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'regti_te'


class TReshdel(Reshdel):
    code = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'reshdel'


class TRezultto(Rezultto):
    code = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'rezultto'


class TRezultto1(Rezultto1):
    code = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'rezultto1'


class TRmbt(Rmbt):
    code = models.CharField(max_length=8, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'rmbt'


class TRmd(Rmd):
    kodt = models.CharField(max_length=8, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'rmd'


class TRmdG(RmdG):
    kodt = models.CharField(max_length=8, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'rmd_g'


class TRmtotok(Rmtotok):
    n_lic = models.CharField(max_length=25, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'rmtotok'


class TRole(Role):
    code = models.CharField(max_length=30, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'role'


class TRpsi(Rpsi):
    cod = models.CharField(max_length=8, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'rpsi'


class TRskCrit(RskCrit):
    kod = models.CharField(max_length=4, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'rsk_crit'


class TRskFinp(RskFinp):
    npp_str = models.DecimalField(default=0.00, max_digits=10, decimal_places=0, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'rsk_finp'


class TRskMera(RskMera):
    kod = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'rsk_mera'


class TRskNdpd(RskNdpd):
    kod = models.CharField(max_length=4, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'rsk_ndpd'


class TRskNinf(RskNinf):
    kod = models.CharField(max_length=4, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'rsk_ninf'


class TRskNmb(RskNmb):
    gr013 = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'rsk_nmb'


class TRskNpm(RskNpm):
    kod = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'rsk_npm'


class TRskPrim(RskPrim):
    kod = models.CharField(max_length=3, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'rsk_prim'


class TRskRsmr(RskRsmr):
    gr013 = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'rsk_rsmr'


class TRskRsnd(RskRsnd):
    gr013 = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'rsk_rsnd'


class TRskRspr(RskRspr):
    gr013 = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'rsk_rspr'


class TRskSpdr0(RskSpdr0):
    kod = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'rsk_spdr'


class TRskTprc(RskTprc):
    kod = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'rsk_tprc'


class TRskrmera(Rskrmera):
    kod = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'rskrmera'


class TRskrsdsm(Rskrsdsm):
    gr013 = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'rskrsdsm'


class TRskrsprc(Rskrsprc):
    gr013 = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'rskrsprc'


class TRskspdr(Rskspdr):
    kod_srdr = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'rskspdr'


class TRsksppri(Rsksppri):
    kod_srdr = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'rsksppri'


class TRsktmera(Rsktmera):
    kod = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'rsktmera'


class TRskxdosm(Rskxdosm):
    kod = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'rskxdosm'


class TRskzdosm(Rskzdosm):
    kod = models.CharField(max_length=6, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'rskzdosm'


class TRsnBpos(RsnBpos):
    buuid = models.CharField(max_length=36, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'rsn_bpos'


class TRsnBuss(RsnBuss):
    buuid = models.CharField(max_length=36, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'rsn_buss'


class TRsnCntr(RsnCntr):
    buuid = models.CharField(max_length=36, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'rsn_cntr'


class TRsnEntf(RsnEntf):
    buuid = models.CharField(max_length=36, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'rsn_entf'


class TRsnEntr(RsnEntr):
    buuid = models.CharField(max_length=36, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'rsn_entr'


class TRsnFlab(RsnFlab):
    buuid = models.CharField(max_length=36, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'rsn_flab'


class TRsnOrg(RsnOrg):
    buuid = models.CharField(max_length=36, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'rsn_org'


class TRsnOrgt(RsnOrgt):
    buuid = models.CharField(max_length=36, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'rsn_orgt'


class TRsnProd(RsnProd):
    buuid = models.CharField(max_length=36, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'rsn_prod'


class TRsnSpro(RsnSpro):
    buuid = models.CharField(max_length=36, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'rsn_spro'


class TRsnTarg(RsnTarg):
    buuid = models.CharField(max_length=36, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'rsn_targ'


class TRsnTdep(RsnTdep):
    buuid = models.CharField(max_length=36, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'rsn_tdep'


class TRsnTsto(RsnTsto):
    buuid = models.CharField(max_length=36, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'rsn_tsto'


class TRsnUnit(RsnUnit):
    buuid = models.CharField(max_length=36, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'rsn_unit'


class TRsnVlab(RsnVlab):
    buuid = models.CharField(max_length=36, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'rsn_vlab'


# class TRstrGrf(RstrGrf):
# 
#     class Meta:
#         managed = False
#         db_table = 'rstr_grf'


class TRstrH(RstrH):
    regnom = models.CharField(max_length=25, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'rstr_h'


class TRstrKat(RstrKat):
    tip_dov = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'rstr_kat'


class TRstrLic(RstrLic):
    g31_12 = models.CharField(max_length=50, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'rstr_lic'


class TRstrN(RstrN):
    regnom = models.CharField(max_length=25, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'rstr_n'


class TRstrOis(RstrOis):
    regnom = models.CharField(max_length=25, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'rstr_ois'


class TRstrTov(RstrTov):
    regnom = models.CharField(max_length=25, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'rstr_tov'


class TRstrTz(RstrTz):
    g31_12 = models.CharField(max_length=50, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'rstr_tz'


class TRstrpath(Rstrpath):
    g31_12 = models.CharField(max_length=50, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'rstrpath'


class TSExhib(SExhib):
    inn = models.CharField(max_length=12, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 's_exhib'


class TSExhid(SExhid):
    inn = models.CharField(max_length=12, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 's_exhid'


class TSObutp(SObutp):
    code = models.CharField(max_length=6, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 's_obutp'


class TSbj(Sbj):
    sbj_id = models.DecimalField(default=0.00, max_digits=15, decimal_places=0, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'sbj'


class TSbjCst(SbjCst):
    inn = models.CharField(max_length=12, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'sbj_cst'


class TSbjExt(SbjExt):
    inn = models.CharField(max_length=12, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'sbj_ext'


class TSbjRole(SbjRole):
    sbj_id = models.DecimalField(default=0.00, max_digits=15, decimal_places=0, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'sbj_role'


class TSbxDel(SbxDel):
    kodt = models.CharField(max_length=8, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'sbx_del'


class TSdelka(Sdelka):
    kod = models.CharField(max_length=3, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'sdelka'


class TSelfnsi1(Selfnsi1):
    field1 = models.CharField(max_length=58, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'selfnsi1'


class TSertS(SertS):
    sert_s = models.CharField(max_length=50, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'sert_s'


class TSertif(Sertif):
    kod = models.CharField(max_length=5, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'sertif'


class TSertif4(Sertif4):
    numdocum = models.CharField(max_length=19, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'sertif4'


class TSezPrim(SezPrim):
    kodt = models.CharField(max_length=10, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'sez_prim'


# class TShtraf1(Shtraf1):
# 
#     class Meta:
#         managed = False
#         db_table = 'shtraf1'


class TSklStt(SklStt):
    kod = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'skl_stt'


# class TSklTm_(SklTm_):
#
#     class Meta:
#         managed = False
#         db_table = 'skl_tm'


class TSklad(Sklad):
    kodt = models.CharField(max_length=5, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'sklad'


class TSkladbx(Skladbx):
    kodt = models.CharField(max_length=8, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'skladbx'


class TSkladtB(SkladtB):
    nlic = models.CharField(max_length=15, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'skladt_b'


class TSkladtm(Skladtm):
    nlic = models.CharField(max_length=15, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'skladtm'


class TSkladvB(SkladvB):
    nlic = models.CharField(max_length=15, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'skladv_b'


# class TSkltm(Skltm):
# 
#     class Meta:
#         managed = False
#         db_table = 'skltm'


class TSkrecc(Skrecc):
    kod = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'skrecc'


class TSoato(Soato):
    kod = models.CharField(max_length=4, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'soato'


class TSokr(Sokr):
    nsokr = models.DecimalField(default=0.00, max_digits=3, decimal_places=0, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'sokr'


class TSono(Sono):
    code = models.CharField(max_length=4, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'sono'


class TSoun1(Soun1):
    kod = models.CharField(max_length=4, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'soun1'


class TSource(Source):
    code = models.CharField(max_length=30, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'source'


class TSpTovW(SpTovW):
    krnaim = models.CharField(max_length=30, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'sp_tov_w'


class TSpcPrim(SpcPrim):
    kodt = models.CharField(max_length=10, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'spc_prim'


class TSpcproc(Spcproc):
    code = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'spcproc'


class TSpzkRsn(SpzkRsn):
    kod = models.CharField(max_length=3, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'spzk_rsn'


class TSrsnRtn(SrsnRtn):
    kod = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'srsn_rtn'


class TStack(Stack):
    rec = models.DecimalField(default=0.00, max_digits=10, decimal_places=0, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'stack'


# class TStm(Stm):
# 
#     class Meta:
#         managed = False
#         db_table = 'stm'


class TStmDel(StmDel):
    kodt = models.CharField(max_length=8, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'stm_del'


class TStrana(Strana):
    kod = models.CharField(max_length=1, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'strana'


class TStt(Stt):
    inn = models.CharField(max_length=12, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'stt'


class TSubject(Subject):
    id = models.DecimalField(default=0.00, max_digits=18, decimal_places=9, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'subject'


class TSubject0(Subject0):
    subject_id = models.DecimalField(default=0.00, max_digits=18, decimal_places=9, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'subject_'


class TSutp(Sutp):
    kod = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'sutp'


class TSysKtpt(SysKtpt):
    dbfname = models.CharField(max_length=8, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'sys_ktpt'


class TTDoc(TDoc):
    kod = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 't_doc'


class TTab47B(Tab47B):
    nd = models.CharField(max_length=19, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'tab47b'


class TTabnar(Tabnar):
    inn = models.CharField(max_length=12, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'tabnar'


class TTam(Tam):
    tam = models.CharField(max_length=16, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'tam'


class TTamplat(Tamplat):
    grp_id = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'tamplat'


class TTamplat0(Tamplat0):
    grp_id = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'tamplat_'


class TTampred(Tampred):
    nlic = models.CharField(max_length=25, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'tampred'


class TTampred1(Tampred1):
    nlic = models.CharField(max_length=25, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'tampred1'


class TTampred2(Tampred2):
    nlic = models.CharField(max_length=25, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'tampred2'


class TTampred3(Tampred3):
    nlic = models.CharField(max_length=25, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'tampred3'


class TTampred4(Tampred4):
    nlic = models.CharField(max_length=25, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'tampred4'


class TTamst(Tamst):
    kod = models.CharField(max_length=10, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'tamst'


class TTamstavt(Tamstavt):
    kodtam = models.CharField(max_length=1, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'tamstavt'


class TTbrok(Tbrok):
    bktlic = models.CharField(max_length=25, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'tbrok'


class TTbrok1(Tbrok1):
    bktlic = models.CharField(max_length=25, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'tbrok1'


class TTbrok2(Tbrok2):
    bktlic = models.CharField(max_length=25, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'tbrok2'


class TTbrok3(Tbrok3):
    bktlic = models.CharField(max_length=25, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'tbrok3'


class TTbrok4(Tbrok4):
    bktlic = models.CharField(max_length=25, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'tbrok4'


class TTbrok5(Tbrok5):
    bktlic = models.CharField(max_length=25, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'tbrok5'


class TTbrok6(Tbrok6):
    bktlic = models.CharField(max_length=25, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'tbrok6'


class TTbrok7(Tbrok7):
    bktlic = models.CharField(max_length=25, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'tbrok7'


class TTbrok8(Tbrok8):
    bktlic = models.CharField(max_length=25, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'tbrok8'


class TTipdv(Tipdv):
    kod = models.CharField(max_length=1, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'tipdv'


class TTipts(Tipts):
    kod = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'tipts'


class TTiptsS(TiptsS):
    kod = models.CharField(max_length=3, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'tipts_s'


class TTk(Tk):
    inn = models.DecimalField(default=0.00, max_digits=19, decimal_places=0, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'tk'


class TTk1(Tk1):
    inn = models.DecimalField(default=0.00, max_digits=19, decimal_places=0, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'tk1'


class TTndti14(Tndti14):
    kod10 = models.CharField(max_length=10, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'tndti14'


class TTnvLtd(TnvLtd):
    code = models.CharField(max_length=10, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'tnv_ltd'


class TTnvStav(TnvStav):
    code_tnv = models.CharField(max_length=10, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'tnv_stav'


class TTnved(Tnved):
    gruppa = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'tnved'


class TTnved1(Tnved1):
    razdel = models.CharField(max_length=5, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'tnved1'


class TTnved2(Tnved2):
    razdel = models.CharField(max_length=5, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'tnved2'


class TTnved3(Tnved3):
    gruppa = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'tnved3'


class TTnved4(Tnved4):
    gruppa = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'tnved4'


class TTnved6(Tnved6):
    gruppa = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'tnved6'


class TTnved8(Tnved8):
    gruppa = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'tnved8'


class TTnved9(Tnved9):
    gruppa = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'tnved9'


class TTovW(TovW):
    kodt = models.CharField(max_length=10, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'tov_w'


class TTovsign(Tovsign):
    gruppa = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'tovsign'


class TTpoPlt(TpoPlt):
    num_tpo = models.CharField(max_length=10, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'tpo_plt'


class TTrans(Trans):
    kod = models.DecimalField(default=0.00, max_digits=3, decimal_places=0, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'trans'


class TTs(Ts):
    sbj_id = models.DecimalField(default=0.00, max_digits=15, decimal_places=0, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'ts'


class TTsk(Tsk):
    kod = models.DecimalField(default=0.00, max_digits=2, decimal_places=0, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'tsk'


class TTskat(Tskat):
    kod = models.CharField(max_length=1, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'tskat'


class TUpravl(Upravl):
    kod = models.CharField(max_length=8, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'upravl'


class TUslpost(Uslpost):
    kodz = models.DecimalField(default=0.00, max_digits=2, decimal_places=0, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'uslpost'


class TUtilsbor(Utilsbor):
    code = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'utilsbor'


class TV2(V2):
    kod = models.CharField(max_length=3, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'v2'


class TVObup(VObup):
    kodc = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'v_obup'


class TVal(Val):
    kod = models.DecimalField(default=0.00, max_digits=19, decimal_places=5, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'val'


class TValCen(ValCen):
    kod = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'val_cen'


class TValname(Valname):
    kod = models.CharField(max_length=3, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'valname'


class TValuta(Valuta):
    kod = models.CharField(max_length=3, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'valuta'


class TVidAmts(VidAmts):
    vid_amts = models.CharField(max_length=3, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'vid_amts'


class TVidDoc(VidDoc):
    kod = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'vid_doc'


class TViddvig(Viddvig):
    kod = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'viddvig'


class TVidtrans(Vidtrans):
    kod = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'vidtrans'


class TVidupak(Vidupak):
    kod = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'vidupak'


class TVkortd(Vkortd):
    kod = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'vkortd'


class TVkvot(Vkvot):
    kod = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'vkvot'


class TVpertr(Vpertr):
    kod = models.CharField(max_length=2, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'vpertr'


class TVspupr(Vspupr):
    kod = models.CharField(max_length=1, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'vspupr'


class TVtsTov(VtsTov):
    key_specif = models.DecimalField(default=0.00, max_digits=19, decimal_places=5, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'vts_tov'


class TVtsZakl(VtsZakl):
    zakl_key = models.DecimalField(default=0.00, max_digits=19, decimal_places=5, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'vts_zakl'


class TWaybill(Waybill):
    num_nakl = models.CharField(max_length=20, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'waybill'


class TYear(Year):
    kod = models.CharField(max_length=1, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'year'


class TZan(Zan):
    nzan = models.DecimalField(default=0.00, max_digits=3, decimal_places=0, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'zan'


class TZvet(Zvet):
    kod = models.CharField(max_length=3, blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'zvet'
