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
from src.apps.common.mixins import BaseSourceFields


class TAddDoc(BaseSourceFields, AddDoc):

    class Meta:
        managed = True
        db_table = 'tadd_doc'


class TAddress(BaseSourceFields, Address):

    class Meta:
        managed = True
        db_table = 'taddress'


class TAdpPrim(BaseSourceFields, AdpPrim):

    class Meta:
        managed = True
        db_table = 'tadp_prim'


class TAkcPrim(BaseSourceFields, AkcPrim):

    class Meta:
        managed = True
        db_table = 'takc_prim'


class TAllIncl(BaseSourceFields, AllIncl):

    class Meta:
        managed = True
        db_table = 'tall_incl'


class TAllOper(BaseSourceFields, AllOper):

    class Meta:
        managed = True
        db_table = 'tall_oper'


class TArxReg(BaseSourceFields, ArxReg):

    class Meta:
        managed = True
        db_table = 'tarx_reg'


class TAtdPos(BaseSourceFields, AtdPos):

    class Meta:
        managed = True
        db_table = 'tatd_pos'


class TAutonz(BaseSourceFields, Autonz):

    class Meta:
        managed = True
        db_table = 'tautonz'


class TBankIzm(BaseSourceFields, BankIzm):

    class Meta:
        managed = True
        db_table = 'tbank_izm'


class TBanklist(BaseSourceFields, Banklist):

    class Meta:
        managed = True
        db_table = 'tbanklist'


class TBartPc(BaseSourceFields, BartPc):

    class Meta:
        managed = True
        db_table = 'tbart_pc'


class TBgDp(BaseSourceFields, BgDp):

    class Meta:
        managed = True
        db_table = 'tbg_dp'


class TBignalog(BaseSourceFields, Bignalog):

    class Meta:
        managed = True
        db_table = 'tbignalog'


class TBignalto(BaseSourceFields, Bignalto):

    class Meta:
        managed = True
        db_table = 'tbignalto'


class TBkbkn(BaseSourceFields, Bkbkn):

    class Meta:
        managed = True
        db_table = 'tbkbkn'


class TBlank(BaseSourceFields, Blank):

    class Meta:
        managed = True
        db_table = 'tblank'


class TBmonth(BaseSourceFields, Bmonth):

    class Meta:
        managed = True
        db_table = 'tbmonth'


class TBnkseek(BaseSourceFields, Bnkseek):

    class Meta:
        managed = True
        db_table = 'tbnkseek'


class TBrok(BaseSourceFields, Brok):

    class Meta:
        managed = True
        db_table = 'tbrok'


class TBx(BaseSourceFields, Bx):

    class Meta:
        managed = True
        db_table = 'tbx'


class TCar(BaseSourceFields, Car):

    class Meta:
        managed = True
        db_table = 'tcar'


class TCarrier(BaseSourceFields, Carrier):

    class Meta:
        managed = True
        db_table = 'tcarrier'


class TCarrierb(BaseSourceFields, Carrierb):

    class Meta:
        managed = True
        db_table = 'tcarrierb'


class TCbContr(BaseSourceFields, CbContr):

    class Meta:
        managed = True
        db_table = 'tcb_contr'


class TChkpoint(BaseSourceFields, Chkpoint):

    class Meta:
        managed = True
        db_table = 'tchkpoint'


class TCntr(BaseSourceFields, Cntr):

    class Meta:
        managed = True
        db_table = 'tcntr'


class TCrV(BaseSourceFields, CrV):

    class Meta:
        managed = True
        db_table = 'tcr_v'


class TCrdts(BaseSourceFields, Crdts):

    class Meta:
        managed = True
        db_table = 'tcrdts'


class TCtovR(BaseSourceFields, CtovR):

    class Meta:
        managed = True
        db_table = 'tctov_r'


class TCtu(BaseSourceFields, Ctu):

    class Meta:
        managed = True
        db_table = 'tctu'


class TCurrency(BaseSourceFields, Currency):

    class Meta:
        managed = True
        db_table = 'tcurrency'


class TCustlist(BaseSourceFields, Custlist):

    class Meta:
        managed = True
        db_table = 'tcustlist'


class TCustoms(BaseSourceFields, Customs):

    class Meta:
        managed = True
        db_table = 'tcustoms'


class TCustpost(BaseSourceFields, Custpost):

    class Meta:
        managed = True
        db_table = 'tcustpost'


class TD44MPr(BaseSourceFields, D44MPr):

    class Meta:
        managed = True
        db_table = 'td44_m_pr'


class TD44MTn(BaseSourceFields, D44MTn):

    class Meta:
        managed = True
        db_table = 'td44_m_tn'


class TD44Mask(BaseSourceFields, D44Mask):

    class Meta:
        managed = True
        db_table = 'td44_mask'


class TD44Sfoiv(BaseSourceFields, D44Sfoiv):

    class Meta:
        managed = True
        db_table = 'td44sfoiv'


class TDeclrnt(BaseSourceFields, Declrnt):

    class Meta:
        managed = True
        db_table = 'tdeclrnt'


class TDelstakc(BaseSourceFields, Delstakc):

    class Meta:
        managed = True
        db_table = 'tdelstakc'


class TDipPrim(BaseSourceFields, DipPrim):

    class Meta:
        managed = True
        db_table = 'tdip_prim'


class TDnbdlist(BaseSourceFields, Dnbdlist):

    class Meta:
        managed = True
        db_table = 'tdnbdlist'


class TDobstakc(BaseSourceFields, Dobstakc):

    class Meta:
        managed = True
        db_table = 'tdobstakc'


class TDocAmts(BaseSourceFields, DocAmts):

    class Meta:
        managed = True
        db_table = 'tdoc_amts'


class TDocPr(BaseSourceFields, DocPr):

    class Meta:
        managed = True
        db_table = 'tdoc_pr'


class TDocTnv(BaseSourceFields, DocTnv):

    class Meta:
        managed = True
        db_table = 'tdoc_tnv'


class TDocg44(BaseSourceFields, Docg44):

    class Meta:
        managed = True
        db_table = 'tdocg44'


class TDocum(BaseSourceFields, Docum):

    class Meta:
        managed = True
        db_table = 'tdocum'


class TDocument(BaseSourceFields, Document):

    class Meta:
        managed = True
        db_table = 'tdocument'


class TDohNepr(BaseSourceFields, DohNepr):

    class Meta:
        managed = True
        db_table = 'tdoh_nepr'


class TDohOsn(BaseSourceFields, DohOsn):

    class Meta:
        managed = True
        db_table = 'tdoh_osn'


class TDolgAll(BaseSourceFields, DolgAll):

    class Meta:
        managed = True
        db_table = 'tdolg_all'


# class TDolgt(BaseSourceFields, Dolgt):
#
#     class Meta:
#         managed = True
#         db_table = 'tdolgt'


class TDov(BaseSourceFields, Dov):

    class Meta:
        managed = True
        db_table = 'tdov'


class TDtamreg(BaseSourceFields, Dtamreg):

    class Meta:
        managed = True
        db_table = 'tdtamreg'


class TEcop(BaseSourceFields, Ecop):

    class Meta:
        managed = True
        db_table = 'tecop'


class TEcop1(BaseSourceFields, Ecop1):

    class Meta:
        managed = True
        db_table = 'tecop1'


class TEcop2(BaseSourceFields, Ecop2):

    class Meta:
        managed = True
        db_table = 'tecop2'


class TEcop3(BaseSourceFields, Ecop3):

    class Meta:
        managed = True
        db_table = 'tecop3'


class TEcop4(BaseSourceFields, Ecop4):

    class Meta:
        managed = True
        db_table = 'tecop4'


class TEcop5(BaseSourceFields, Ecop5):

    class Meta:
        managed = True
        db_table = 'tecop5'


class TEdizm(BaseSourceFields, Edizm):

    class Meta:
        managed = True
        db_table = 'tedizm'


class TEdizmDp(BaseSourceFields, EdizmDp):

    class Meta:
        managed = True
        db_table = 'tedizm_dp'


class TEkAr(BaseSourceFields, EkAr):

    class Meta:
        managed = True
        db_table = 'tek_ar'


class TEkEu(BaseSourceFields, EkEu):

    class Meta:
        managed = True
        db_table = 'tek_eu'


class TExpPrim(BaseSourceFields, ExpPrim):

    class Meta:
        managed = True
        db_table = 'texp_prim'


class TExperimt(BaseSourceFields, Experimt):

    class Meta:
        managed = True
        db_table = 'texperimt'


class TExpstakc(BaseSourceFields, Expstakc):

    class Meta:
        managed = True
        db_table = 'texpstakc'


class TExtremM(BaseSourceFields, ExtremM):

    class Meta:
        managed = True
        db_table = 'textrem_m'


class TFaItemc(BaseSourceFields, FaItemc):

    class Meta:
        managed = True
        db_table = 'tfa_itemc'


class TFaPredm(BaseSourceFields, FaPredm):

    class Meta:
        managed = True
        db_table = 'tfa_predm'


class TFinbg(BaseSourceFields, Finbg):

    class Meta:
        managed = True
        db_table = 'tfinbg'


class TFinbg0(BaseSourceFields, Finbg0):

    class Meta:
        managed = True
        db_table = 'tfinbg_'


class TFmtk(BaseSourceFields, Fmtk):

    class Meta:
        managed = True
        db_table = 'tfmtk'


class TFormras(BaseSourceFields, Formras):

    class Meta:
        managed = True
        db_table = 'tformras'


class TFstRaz(BaseSourceFields, FstRaz):

    class Meta:
        managed = True
        db_table = 'tfst_raz'


class TFstZakl(BaseSourceFields, FstZakl):

    class Meta:
        managed = True
        db_table = 'tfst_zakl'


class TGarant(BaseSourceFields, Garant):

    class Meta:
        managed = True
        db_table = 'tgarant'


class TGdOtd(BaseSourceFields, GdOtd):

    class Meta:
        managed = True
        db_table = 'tgd_otd'


class TGdStan(BaseSourceFields, GdStan):

    class Meta:
        managed = True
        db_table = 'tgd_stan'


class TGeoAr(BaseSourceFields, GeoAr):

    class Meta:
        managed = True
        db_table = 'tgeo_ar'


class TGrp(BaseSourceFields, Grp):

    class Meta:
        managed = True
        db_table = 'tgrp'


class THold(BaseSourceFields, Hold):

    class Meta:
        managed = True
        db_table = 'thold'


class TImpPrim(BaseSourceFields, ImpPrim):

    class Meta:
        managed = True
        db_table = 'timp_prim'


class TInFirm(BaseSourceFields, InFirm):

    class Meta:
        managed = True
        db_table = 'tin_firm'


class TIndicEf(BaseSourceFields, IndicEf):

    class Meta:
        managed = True
        db_table = 'tindic_ef'


class TIndnsi(BaseSourceFields, Indnsi):

    class Meta:
        managed = True
        db_table = 'tindnsi'


class TInf1Td(BaseSourceFields, Inf1Td):

    class Meta:
        managed = True
        db_table = 'tinf1td'


class TInfEais(BaseSourceFields, InfEais):

    class Meta:
        managed = True
        db_table = 'tinf_eais'


class TInfram(BaseSourceFields, Infram):

    class Meta:
        managed = True
        db_table = 'tinfram'


class TIzgot(BaseSourceFields, Izgot):

    class Meta:
        managed = True
        db_table = 'tizgot'


class TKat(BaseSourceFields, Kat):

    class Meta:
        managed = True
        db_table = 'tkat'


class TKateg(BaseSourceFields, Kateg):

    class Meta:
        managed = True
        db_table = 'tkateg'


class TKategwar(BaseSourceFields, Kategwar):

    class Meta:
        managed = True
        db_table = 'tkategwar'


class TKatt(BaseSourceFields, Katt):

    class Meta:
        managed = True
        db_table = 'tkatt'


class TKkk(BaseSourceFields, Kkk):

    class Meta:
        managed = True
        db_table = 'tkkk'


class TKl203B(BaseSourceFields, Kl203B):

    class Meta:
        managed = True
        db_table = 'tkl203b'


class TKl203E(BaseSourceFields, Kl203E):

    class Meta:
        managed = True
        db_table = 'tkl203e'


class TKl203I(BaseSourceFields, Kl203I):

    class Meta:
        managed = True
        db_table = 'tkl203i'


class TKl204(BaseSourceFields, Kl204):

    class Meta:
        managed = True
        db_table = 'tkl204'


class TKl204B(BaseSourceFields, Kl204B):

    class Meta:
        managed = True
        db_table = 'tkl204b'


class TKl204Ing(BaseSourceFields, Kl204Ing):

    class Meta:
        managed = True
        db_table = 'tkl204ing'


class TKlStav(BaseSourceFields, KlStav):

    class Meta:
        managed = True
        db_table = 'tkl_stav'


class TKlass203(BaseSourceFields, Klass203):

    class Meta:
        managed = True
        db_table = 'tklass203'


class TKlass204(BaseSourceFields, Klass204):

    class Meta:
        managed = True
        db_table = 'tklass204'


class TKlass205(BaseSourceFields, Klass205):

    class Meta:
        managed = True
        db_table = 'tklass205'


class TKlirVal(BaseSourceFields, KlirVal):

    class Meta:
        managed = True
        db_table = 'tklir_val'


class TKliring(BaseSourceFields, Kliring):

    class Meta:
        managed = True
        db_table = 'tkliring'


class TKodG300(BaseSourceFields, KodG300):

    class Meta:
        managed = True
        db_table = 'tkod_g300'


class TKodkdt(BaseSourceFields, Kodkdt):

    class Meta:
        managed = True
        db_table = 'tkodkdt'


class TKodktc(BaseSourceFields, Kodktc):

    class Meta:
        managed = True
        db_table = 'tkodktc'


class TKomop(BaseSourceFields, Komop):

    class Meta:
        managed = True
        db_table = 'tkomop'


class TKray(BaseSourceFields, Kray):

    class Meta:
        managed = True
        db_table = 'tkray'


class TKtam(BaseSourceFields, Ktam):

    class Meta:
        managed = True
        db_table = 'tktam'


class TKtam1(BaseSourceFields, Ktam1):

    class Meta:
        managed = True
        db_table = 'tktam1'


class TKtam2(BaseSourceFields, Ktam2):

    class Meta:
        managed = True
        db_table = 'tktam2'


class TKtamatr(BaseSourceFields, Ktamatr):

    class Meta:
        managed = True
        db_table = 'tktamatr'


class TKtamolap(BaseSourceFields, Ktamolap):

    class Meta:
        managed = True
        db_table = 'tktamolap'


class TKtamold(BaseSourceFields, Ktamold):

    class Meta:
        managed = True
        db_table = 'tktamold'


class TKtddl(BaseSourceFields, Ktddl):

    class Meta:
        managed = True
        db_table = 'tktddl'


class TKvota(BaseSourceFields, Kvota):

    class Meta:
        managed = True
        db_table = 'tkvota'


class TKvz(BaseSourceFields, Kvz):

    class Meta:
        managed = True
        db_table = 'tkvz'


class TLgotUv(BaseSourceFields, LgotUv):

    class Meta:
        managed = True
        db_table = 'tlgot_uv'


class TLicTi(BaseSourceFields, LicTi):

    class Meta:
        managed = True
        db_table = 'tlic_ti'


class TLicTov(BaseSourceFields, LicTov):

    class Meta:
        managed = True
        db_table = 'tlic_tov'


class TLicTv(BaseSourceFields, LicTv):

    class Meta:
        managed = True
        db_table = 'tlic_tv'


class TLocKntr(BaseSourceFields, LocKntr):

    class Meta:
        managed = True
        db_table = 'tloc_kntr'


class TLostTir(BaseSourceFields, LostTir):

    class Meta:
        managed = True
        db_table = 'tlost_tir'


class TMarAkc(BaseSourceFields, MarAkc):

    class Meta:
        managed = True
        db_table = 'tmar_akc'


class TMaxstakc(BaseSourceFields, Maxstakc):

    class Meta:
        managed = True
        db_table = 'tmaxstakc'


class TMdpAdr(BaseSourceFields, MdpAdr):

    class Meta:
        managed = True
        db_table = 'tmdp_adr'


class TMdpD(BaseSourceFields, MdpD):

    class Meta:
        managed = True
        db_table = 'tmdp_d'


class TMdpKont(BaseSourceFields, MdpKont):

    class Meta:
        managed = True
        db_table = 'tmdp_kont'


class TMeasures(BaseSourceFields, Measures):

    class Meta:
        managed = True
        db_table = 'tmeasures'


class TMintnv(BaseSourceFields, Mintnv):

    class Meta:
        managed = True
        db_table = 'tmintnv'


class TMnt(BaseSourceFields, Mnt):

    class Meta:
        managed = True
        db_table = 'tmnt'


class TMosKtam(BaseSourceFields, MosKtam):

    class Meta:
        managed = True
        db_table = 'tmos_ktam'


class TMotc(BaseSourceFields, Motc):

    class Meta:
        managed = True
        db_table = 'tmotc'


class TMotsfl(BaseSourceFields, Motsfl):

    class Meta:
        managed = True
        db_table = 'tmotsfl'


class TMps(BaseSourceFields, Mps):

    class Meta:
        managed = True
        db_table = 'tmps'


class TMpsreg(BaseSourceFields, Mpsreg):

    class Meta:
        managed = True
        db_table = 'tmpsreg'


class TMrkCar(BaseSourceFields, MrkCar):

    class Meta:
        managed = True
        db_table = 'tmrk_car'


class TMrkCars(BaseSourceFields, MrkCars):

    class Meta:
        managed = True
        db_table = 'tmrk_cars'


class TNamefirm(BaseSourceFields, Namefirm):

    class Meta:
        managed = True
        db_table = 'tnamefirm'


class TNar(BaseSourceFields, Nar):

    class Meta:
        managed = True
        db_table = 'tnar'


class TNarVtt(BaseSourceFields, NarVtt):

    class Meta:
        managed = True
        db_table = 'tnar_vtt'


class TNewTi(BaseSourceFields, NewTi):

    class Meta:
        managed = True
        db_table = 'tnew_ti'


class TNlstmpr(BaseSourceFields, Nlstmpr):

    class Meta:
        managed = True
        db_table = 'tnlstmpr'


class TNpech(BaseSourceFields, Npech):

    class Meta:
        managed = True
        db_table = 'tnpech'


class TNprsSbj(BaseSourceFields, NprsSbj):

    class Meta:
        managed = True
        db_table = 'tnprs_sbj'


class TNsDolgn(BaseSourceFields, NsDolgn):

    class Meta:
        managed = True
        db_table = 'tns_dolgn'


class TNsDul(BaseSourceFields, NsDul):

    class Meta:
        managed = True
        db_table = 'tns_dul'


class TNsDulT(BaseSourceFields, NsDulT):

    class Meta:
        managed = True
        db_table = 'tns_dul_t'


class TNsDulV(BaseSourceFields, NsDulV):

    class Meta:
        managed = True
        db_table = 'tns_dul_v'


class TNsGr31(BaseSourceFields, NsGr31):

    class Meta:
        managed = True
        db_table = 'tns_gr31'


class TNsMpo(BaseSourceFields, NsMpo):

    class Meta:
        managed = True
        db_table = 'tns_mpo'


class TNsOd31(BaseSourceFields, NsOd31):

    class Meta:
        managed = True
        db_table = 'tns_od31'


class TNsTsfl(BaseSourceFields, NsTsfl):

    class Meta:
        managed = True
        db_table = 'tns_tsfl'


class TNsiKbk(BaseSourceFields, NsiKbk):

    class Meta:
        managed = True
        db_table = 'tnsi_kbk'


class TNullstB(BaseSourceFields, NullstB):

    class Meta:
        managed = True
        db_table = 'tnullst_b'


class TO803(BaseSourceFields, O803):

    class Meta:
        managed = True
        db_table = 'to803'


class TObject0(BaseSourceFields, Object0):

    class Meta:
        managed = True
        db_table = 'tobject'


class TOfdoc(BaseSourceFields, Ofdoc):

    class Meta:
        managed = True
        db_table = 'tofdoc'


class TOgovorka(BaseSourceFields, Ogovorka):

    class Meta:
        managed = True
        db_table = 'togovorka'


class TOkaPk38(BaseSourceFields, OkaPk38):

    class Meta:
        managed = True
        db_table = 'toka-pk38'


class TOkaPk44(BaseSourceFields, OkaPk44):

    class Meta:
        managed = True
        db_table = 'toka-pk44'


class TOkaPk48(BaseSourceFields, OkaPk48):

    class Meta:
        managed = True
        db_table = 'toka-pk48'


class TOkaPk65(BaseSourceFields, OkaPk65):

    class Meta:
        managed = True
        db_table = 'toka-pk65'


class TOkaPk66(BaseSourceFields, OkaPk66):

    class Meta:
        managed = True
        db_table = 'toka-pk66'


class TOkaPk72(BaseSourceFields, OkaPk72):

    class Meta:
        managed = True
        db_table = 'toka-pk72'


class TOkaPk75(BaseSourceFields, OkaPk75):

    class Meta:
        managed = True
        db_table = 'toka-pk75'


class TOkaPk76(BaseSourceFields, OkaPk76):

    class Meta:
        managed = True
        db_table = 'toka-pk76'


class TOkaPk79(BaseSourceFields, OkaPk79):

    class Meta:
        managed = True
        db_table = 'toka-pk79'


class TOkaPk82(BaseSourceFields, OkaPk82):

    class Meta:
        managed = True
        db_table = 'toka_pk82'


class TOkaPk83(BaseSourceFields, OkaPk83):

    class Meta:
        managed = True
        db_table = 'toka_pk83'


class TOkaPk84(BaseSourceFields, OkaPk84):

    class Meta:
        managed = True
        db_table = 'toka_pk84'


class TOkaPk85(BaseSourceFields, OkaPk85):

    class Meta:
        managed = True
        db_table = 'toka_pk85'


class TOkaPk86(BaseSourceFields, OkaPk86):

    class Meta:
        managed = True
        db_table = 'toka_pk86'


class TOkaPk87(BaseSourceFields, OkaPk87):

    class Meta:
        managed = True
        db_table = 'toka_pk87'


class TOkaPk88(BaseSourceFields, OkaPk88):

    class Meta:
        managed = True
        db_table = 'toka_pk88'


class TOkaPk89(BaseSourceFields, OkaPk89):

    class Meta:
        managed = True
        db_table = 'toka_pk89'


class TOkato(BaseSourceFields, Okato):

    class Meta:
        managed = True
        db_table = 'tokato'


class TOkatosrf(BaseSourceFields, Okatosrf):

    class Meta:
        managed = True
        db_table = 'tokatosrf'


class TOksmt(BaseSourceFields, Oksmt):

    class Meta:
        managed = True
        db_table = 'toksmt'


class TOprMeas(BaseSourceFields, OprMeas):

    class Meta:
        managed = True
        db_table = 'topr_meas'


class TOrgNpr(BaseSourceFields, OrgNpr):

    class Meta:
        managed = True
        db_table = 'torg_npr'


class TOrtov(BaseSourceFields, Ortov):

    class Meta:
        managed = True
        db_table = 'tortov'


class TOsdelka(BaseSourceFields, Osdelka):

    class Meta:
        managed = True
        db_table = 'tosdelka'


class TOsf(BaseSourceFields, Osf):

    class Meta:
        managed = True
        db_table = 'tosf'


class TOstamplt(BaseSourceFields, Ostamplt):

    class Meta:
        managed = True
        db_table = 'tostamplt'


class TOstamplu(BaseSourceFields, Ostamplu):

    class Meta:
        managed = True
        db_table = 'tostamplu'


class TOtamreg(BaseSourceFields, Otamreg):

    class Meta:
        managed = True
        db_table = 'totamreg'


class TOtr(BaseSourceFields, Otr):

    class Meta:
        managed = True
        db_table = 'totr'


class TOutp(BaseSourceFields, Outp):

    class Meta:
        managed = True
        db_table = 'toutp'


class TOzvet(BaseSourceFields, Ozvet):

    class Meta:
        managed = True
        db_table = 'tozvet'


class TPasport(BaseSourceFields, Pasport):

    class Meta:
        managed = True
        db_table = 'tpasport'


class TPech(BaseSourceFields, Pech):

    class Meta:
        managed = True
        db_table = 'tpech'


class TPechDel(BaseSourceFields, PechDel):

    class Meta:
        managed = True
        db_table = 'tpech_del'


class TPechKpv(BaseSourceFields, PechKpv):

    class Meta:
        managed = True
        db_table = 'tpech_kpv'


class TPechvid(BaseSourceFields, Pechvid):

    class Meta:
        managed = True
        db_table = 'tpechvid'


class TPedhDel(BaseSourceFields, PedhDel):

    class Meta:
        managed = True
        db_table = 'tpedh_del'


class TPermSch(BaseSourceFields, PermSch):

    class Meta:
        managed = True
        db_table = 'tperm_sch'


class TPermit(BaseSourceFields, Permit):

    class Meta:
        managed = True
        db_table = 'tpermit'


class TPlbase(BaseSourceFields, Plbase):

    class Meta:
        managed = True
        db_table = 'tplbase'


class TPlomDel(BaseSourceFields, PlomDel):

    class Meta:
        managed = True
        db_table = 'tplom_del'


class TPlombir(BaseSourceFields, Plombir):

    class Meta:
        managed = True
        db_table = 'tplombir'


class TPointDa(BaseSourceFields, PointDa):

    class Meta:
        managed = True
        db_table = 'tpoint_da'


class TPointIn(BaseSourceFields, PointIn):

    class Meta:
        managed = True
        db_table = 'tpoint_in'


class TPointNe(BaseSourceFields, PointNe):

    class Meta:
        managed = True
        db_table = 'tpoint_ne'


class TPointOp(BaseSourceFields, PointOp):

    class Meta:
        managed = True
        db_table = 'tpoint_op'


class TPointRe(BaseSourceFields, PointRe):

    class Meta:
        managed = True
        db_table = 'tpoint_re'


class TPoluch(BaseSourceFields, Poluch):

    class Meta:
        managed = True
        db_table = 'tpoluch'


class TPravo(BaseSourceFields, Pravo):

    class Meta:
        managed = True
        db_table = 'tpravo'


class TPredresh(BaseSourceFields, Predresh):

    class Meta:
        managed = True
        db_table = 'tpredresh'


class TPrice(BaseSourceFields, Price):

    class Meta:
        managed = True
        db_table = 'tprice'


class TPrice10(BaseSourceFields, Price10):

    class Meta:
        managed = True
        db_table = 'tprice10'


class TPriceg(BaseSourceFields, Priceg):

    class Meta:
        managed = True
        db_table = 'tpriceg'


class TPrimAdp(BaseSourceFields, PrimAdp):

    class Meta:
        managed = True
        db_table = 'tprim_adp'


class TPrimBg(BaseSourceFields, PrimBg):

    class Meta:
        managed = True
        db_table = 'tprim_bg'


class TPrimBzp(BaseSourceFields, PrimBzp):

    class Meta:
        managed = True
        db_table = 'tprim_bzp'


class TPrimKod(BaseSourceFields, PrimKod):

    class Meta:
        managed = True
        db_table = 'tprim_kod'


class TPrimLec(BaseSourceFields, PrimLec):

    class Meta:
        managed = True
        db_table = 'tprim_lec'


class TPrimLic(BaseSourceFields, PrimLic):

    class Meta:
        managed = True
        db_table = 'tprim_lic'


class TPrimMrk(BaseSourceFields, PrimMrk):

    class Meta:
        managed = True
        db_table = 'tprim_mrk'


class TPrimNdc(BaseSourceFields, PrimNdc):

    class Meta:
        managed = True
        db_table = 'tprim_ndc'


class TPrimPr0(BaseSourceFields, PrimPr0):

    class Meta:
        managed = True
        db_table = 'tprim_pr0'


class TPrimPrf(BaseSourceFields, PrimPrf):

    class Meta:
        managed = True
        db_table = 'tprim_prf'


class TPrimPry(BaseSourceFields, PrimPry):

    class Meta:
        managed = True
        db_table = 'tprim_pry'


class TPrimSpr(BaseSourceFields, PrimSpr):

    class Meta:
        managed = True
        db_table = 'tprim_spr'


class TPrimSt1(BaseSourceFields, PrimSt1):

    class Meta:
        managed = True
        db_table = 'tprim_st1'


class TPrmCont(BaseSourceFields, PrmCont):

    class Meta:
        managed = True
        db_table = 'tprm_cont'


class TPrstate(BaseSourceFields, Prstate):

    class Meta:
        managed = True
        db_table = 'tprstate'


class TPzkOrd(BaseSourceFields, PzkOrd):

    class Meta:
        managed = True
        db_table = 'tpzk_ord'


class TRam(BaseSourceFields, Ram):

    class Meta:
        managed = True
        db_table = 'tram'


class TRdBg872(BaseSourceFields, RdBg872):

    class Meta:
        managed = True
        db_table = 'trd_bg872'


class TRe12Tm(BaseSourceFields, Re12Tm):

    class Meta:
        managed = True
        db_table = 'tre_12tm'


class TReAct(BaseSourceFields, ReAct):

    class Meta:
        managed = True
        db_table = 'tre_act'


class TReArhiv(BaseSourceFields, ReArhiv):

    class Meta:
        managed = True
        db_table = 'tre_arhiv'


class TReDeist(BaseSourceFields, ReDeist):

    class Meta:
        managed = True
        db_table = 'tre_deist'


class TReDelo(BaseSourceFields, ReDelo):

    class Meta:
        managed = True
        db_table = 'tre_delo'


class TReDopps(BaseSourceFields, ReDopps):

    class Meta:
        managed = True
        db_table = 'tre_dopps'


class TReDoprv(BaseSourceFields, ReDoprv):

    class Meta:
        managed = True
        db_table = 'tre_doprv'


class TReLi(BaseSourceFields, ReLi):

    class Meta:
        managed = True
        db_table = 'tre_li'


class TReLsoi(BaseSourceFields, ReLsoi):

    class Meta:
        managed = True
        db_table = 'tre_lsoi'


class TReLsov(BaseSourceFields, ReLsov):

    class Meta:
        managed = True
        db_table = 'tre_lsov'


class TReLv(BaseSourceFields, ReLv):

    class Meta:
        managed = True
        db_table = 'tre_lv'


class TReMist(BaseSourceFields, ReMist):

    class Meta:
        managed = True
        db_table = 'tre_mist'


class TRePost(BaseSourceFields, RePost):

    class Meta:
        managed = True
        db_table = 'tre_post'


class TRePrich(BaseSourceFields, RePrich):

    class Meta:
        managed = True
        db_table = 'tre_prich'


class TReRvto(BaseSourceFields, ReRvto):

    class Meta:
        managed = True
        db_table = 'tre_rvto'


class TReSttk(BaseSourceFields, ReSttk):

    class Meta:
        managed = True
        db_table = 'tre_sttk'


class TReTmist(BaseSourceFields, ReTmist):

    class Meta:
        managed = True
        db_table = 'tre_tmist'


class TReZalob(BaseSourceFields, ReZalob):

    class Meta:
        managed = True
        db_table = 'tre_zalob'


class TRecom(BaseSourceFields, Recom):

    class Meta:
        managed = True
        db_table = 'trecom'


class TReg(BaseSourceFields, Reg):

    class Meta:
        managed = True
        db_table = 'treg'


class TRegK(BaseSourceFields, RegK):

    class Meta:
        managed = True
        db_table = 'treg_k'


class TRegMvs(BaseSourceFields, RegMvs):

    class Meta:
        managed = True
        db_table = 'treg_mvs'


class TRegS(BaseSourceFields, RegS):

    class Meta:
        managed = True
        db_table = 'treg_s'


class TRegTi(BaseSourceFields, RegTi):

    class Meta:
        managed = True
        db_table = 'treg_ti'


class TRegTit(BaseSourceFields, RegTit):

    class Meta:
        managed = True
        db_table = 'treg_tit'


class TRegTi1(BaseSourceFields, RegTi1):

    class Meta:
        managed = True
        db_table = 'treg_ti~1'


class TRegiK(BaseSourceFields, RegiK):

    class Meta:
        managed = True
        db_table = 'tregi_k'


class TRegpltls(BaseSourceFields, Regpltls):

    class Meta:
        managed = True
        db_table = 'tregpltls'


class TRegtiTe(BaseSourceFields, RegtiTe):

    class Meta:
        managed = True
        db_table = 'tregti_te'


class TReshdel(BaseSourceFields, Reshdel):

    class Meta:
        managed = True
        db_table = 'treshdel'


class TRezultto(BaseSourceFields, Rezultto):

    class Meta:
        managed = True
        db_table = 'trezultto'


class TRezultto1(BaseSourceFields, Rezultto1):

    class Meta:
        managed = True
        db_table = 'trezultto1'


class TRmbt(BaseSourceFields, Rmbt):

    class Meta:
        managed = True
        db_table = 'trmbt'


class TRmd(BaseSourceFields, Rmd):

    class Meta:
        managed = True
        db_table = 'trmd'


class TRmdG(BaseSourceFields, RmdG):

    class Meta:
        managed = True
        db_table = 'trmd_g'


class TRmtotok(BaseSourceFields, Rmtotok):

    class Meta:
        managed = True
        db_table = 'trmtotok'


class TRole(BaseSourceFields, Role):

    class Meta:
        managed = True
        db_table = 'trole'


class TRpsi(BaseSourceFields, Rpsi):

    class Meta:
        managed = True
        db_table = 'trpsi'


class TRskCrit(BaseSourceFields, RskCrit):

    class Meta:
        managed = True
        db_table = 'trsk_crit'


class TRskFinp(BaseSourceFields, RskFinp):

    class Meta:
        managed = True
        db_table = 'trsk_finp'


class TRskMera(BaseSourceFields, RskMera):

    class Meta:
        managed = True
        db_table = 'trsk_mera'


class TRskNdpd(BaseSourceFields, RskNdpd):

    class Meta:
        managed = True
        db_table = 'trsk_ndpd'


class TRskNinf(BaseSourceFields, RskNinf):

    class Meta:
        managed = True
        db_table = 'trsk_ninf'


class TRskNmb(BaseSourceFields, RskNmb):

    class Meta:
        managed = True
        db_table = 'trsk_nmb'


class TRskNpm(BaseSourceFields, RskNpm):

    class Meta:
        managed = True
        db_table = 'trsk_npm'


class TRskPrim(BaseSourceFields, RskPrim):

    class Meta:
        managed = True
        db_table = 'trsk_prim'


class TRskRsmr(BaseSourceFields, RskRsmr):

    class Meta:
        managed = True
        db_table = 'trsk_rsmr'


class TRskRsnd(BaseSourceFields, RskRsnd):

    class Meta:
        managed = True
        db_table = 'trsk_rsnd'


class TRskRspr(BaseSourceFields, RskRspr):

    class Meta:
        managed = True
        db_table = 'trsk_rspr'


class TRskSpdr0(BaseSourceFields, RskSpdr0):

    class Meta:
        managed = True
        db_table = 'trsk_spdr'


class TRskTprc(BaseSourceFields, RskTprc):

    class Meta:
        managed = True
        db_table = 'trsk_tprc'


class TRskrmera(BaseSourceFields, Rskrmera):

    class Meta:
        managed = True
        db_table = 'trskrmera'


class TRskrsdsm(BaseSourceFields, Rskrsdsm):

    class Meta:
        managed = True
        db_table = 'trskrsdsm'


class TRskrsprc(BaseSourceFields, Rskrsprc):

    class Meta:
        managed = True
        db_table = 'trskrsprc'


class TRskspdr(BaseSourceFields, Rskspdr):

    class Meta:
        managed = True
        db_table = 'trskspdr'


class TRsksppri(BaseSourceFields, Rsksppri):

    class Meta:
        managed = True
        db_table = 'trsksppri'


class TRsktmera(BaseSourceFields, Rsktmera):

    class Meta:
        managed = True
        db_table = 'trsktmera'


class TRskxdosm(BaseSourceFields, Rskxdosm):

    class Meta:
        managed = True
        db_table = 'trskxdosm'


class TRskzdosm(BaseSourceFields, Rskzdosm):

    class Meta:
        managed = True
        db_table = 'trskzdosm'


class TRsnBpos(BaseSourceFields, RsnBpos):

    class Meta:
        managed = True
        db_table = 'trsn_bpos'


class TRsnBuss(BaseSourceFields, RsnBuss):

    class Meta:
        managed = True
        db_table = 'trsn_buss'


class TRsnCntr(BaseSourceFields, RsnCntr):

    class Meta:
        managed = True
        db_table = 'trsn_cntr'


class TRsnEntf(BaseSourceFields, RsnEntf):

    class Meta:
        managed = True
        db_table = 'trsn_entf'


class TRsnEntr(BaseSourceFields, RsnEntr):

    class Meta:
        managed = True
        db_table = 'trsn_entr'


class TRsnFlab(BaseSourceFields, RsnFlab):

    class Meta:
        managed = True
        db_table = 'trsn_flab'


class TRsnOrg(BaseSourceFields, RsnOrg):

    class Meta:
        managed = True
        db_table = 'trsn_org'


class TRsnOrgt(BaseSourceFields, RsnOrgt):

    class Meta:
        managed = True
        db_table = 'trsn_orgt'


class TRsnProd(BaseSourceFields, RsnProd):

    class Meta:
        managed = True
        db_table = 'trsn_prod'


class TRsnSpro(BaseSourceFields, RsnSpro):

    class Meta:
        managed = True
        db_table = 'trsn_spro'


class TRsnTarg(BaseSourceFields, RsnTarg):

    class Meta:
        managed = True
        db_table = 'trsn_targ'


class TRsnTdep(BaseSourceFields, RsnTdep):

    class Meta:
        managed = True
        db_table = 'trsn_tdep'


class TRsnTsto(BaseSourceFields, RsnTsto):

    class Meta:
        managed = True
        db_table = 'trsn_tsto'


class TRsnUnit(BaseSourceFields, RsnUnit):

    class Meta:
        managed = True
        db_table = 'trsn_unit'


class TRsnVlab(BaseSourceFields, RsnVlab):

    class Meta:
        managed = True
        db_table = 'trsn_vlab'


# class TRstrGrf(BaseSourceFields, RstrGrf):
#
#     class Meta:
#         managed = True
#         db_table = 'trstr_grf'


class TRstrH(BaseSourceFields, RstrH):

    class Meta:
        managed = True
        db_table = 'trstr_h'


class TRstrKat(BaseSourceFields, RstrKat):

    class Meta:
        managed = True
        db_table = 'trstr_kat'


class TRstrLic(BaseSourceFields, RstrLic):

    class Meta:
        managed = True
        db_table = 'trstr_lic'


class TRstrN(BaseSourceFields, RstrN):

    class Meta:
        managed = True
        db_table = 'trstr_n'


class TRstrOis(BaseSourceFields, RstrOis):

    class Meta:
        managed = True
        db_table = 'trstr_ois'


class TRstrTov(BaseSourceFields, RstrTov):

    class Meta:
        managed = True
        db_table = 'trstr_tov'


class TRstrTz(BaseSourceFields, RstrTz):

    class Meta:
        managed = True
        db_table = 'trstr_tz'


class TRstrpath(BaseSourceFields, Rstrpath):

    class Meta:
        managed = True
        db_table = 'trstrpath'


class TSExhib(BaseSourceFields, SExhib):

    class Meta:
        managed = True
        db_table = 'ts_exhib'


class TSExhid(BaseSourceFields, SExhid):

    class Meta:
        managed = True
        db_table = 'ts_exhid'


class TSObutp(BaseSourceFields, SObutp):

    class Meta:
        managed = True
        db_table = 'ts_obutp'


class TSbj(BaseSourceFields, Sbj):

    class Meta:
        managed = True
        db_table = 'tsbj'


class TSbjCst(BaseSourceFields, SbjCst):

    class Meta:
        managed = True
        db_table = 'tsbj_cst'


class TSbjExt(BaseSourceFields, SbjExt):

    class Meta:
        managed = True
        db_table = 'tsbj_ext'


class TSbjRole(BaseSourceFields, SbjRole):

    class Meta:
        managed = True
        db_table = 'tsbj_role'


class TSbxDel(BaseSourceFields, SbxDel):

    class Meta:
        managed = True
        db_table = 'tsbx_del'


class TSdelka(BaseSourceFields, Sdelka):

    class Meta:
        managed = True
        db_table = 'tsdelka'


class TSelfnsi1(BaseSourceFields, Selfnsi1):

    class Meta:
        managed = True
        db_table = 'tselfnsi1'


class TSertS(BaseSourceFields, SertS):

    class Meta:
        managed = True
        db_table = 'tsert_s'


class TSertif(BaseSourceFields, Sertif):

    class Meta:
        managed = True
        db_table = 'tsertif'


class TSertif4(BaseSourceFields, Sertif4):

    class Meta:
        managed = True
        db_table = 'tsertif4'


class TSezPrim(BaseSourceFields, SezPrim):

    class Meta:
        managed = True
        db_table = 'tsez_prim'


# class TShtraf1(BaseSourceFields, Shtraf1):
#
#     class Meta:
#         managed = True
#         db_table = 'tshtraf1'


class TSklStt(BaseSourceFields, SklStt):

    class Meta:
        managed = True
        db_table = 'tskl_stt'


# class TSklTm(BaseSourceFields, SklTm):
#
#     class Meta:
#         managed = True
#         db_table = 'tskl_tm'


class TSklad(BaseSourceFields, Sklad):

    class Meta:
        managed = True
        db_table = 'tsklad'


class TSkladbx(BaseSourceFields, Skladbx):

    class Meta:
        managed = True
        db_table = 'tskladbx'


class TSkladtB(BaseSourceFields, SkladtB):

    class Meta:
        managed = True
        db_table = 'tskladt_b'


class TSkladtm(BaseSourceFields, Skladtm):

    class Meta:
        managed = True
        db_table = 'tskladtm'


class TSkladvB(BaseSourceFields, SkladvB):

    class Meta:
        managed = True
        db_table = 'tskladv_b'


# class TSkltm(BaseSourceFields, Skltm):
#
#     class Meta:
#         managed = True
#         db_table = 'tskltm'


class TSkrecc(BaseSourceFields, Skrecc):

    class Meta:
        managed = True
        db_table = 'tskrecc'


class TSoato(BaseSourceFields, Soato):

    class Meta:
        managed = True
        db_table = 'tsoato'


class TSokr(BaseSourceFields, Sokr):

    class Meta:
        managed = True
        db_table = 'tsokr'


class TSono(BaseSourceFields, Sono):

    class Meta:
        managed = True
        db_table = 'tsono'


class TSoun1(BaseSourceFields, Soun1):

    class Meta:
        managed = True
        db_table = 'tsoun1'


class TSource(BaseSourceFields, Source):

    class Meta:
        managed = True
        db_table = 'tsource'


class TSpTovW(BaseSourceFields, SpTovW):

    class Meta:
        managed = True
        db_table = 'tsp_tov_w'


class TSpcPrim(BaseSourceFields, SpcPrim):

    class Meta:
        managed = True
        db_table = 'tspc_prim'


class TSpcproc(BaseSourceFields, Spcproc):

    class Meta:
        managed = True
        db_table = 'tspcproc'


class TSpzkRsn(BaseSourceFields, SpzkRsn):

    class Meta:
        managed = True
        db_table = 'tspzk_rsn'


class TSrsnRtn(BaseSourceFields, SrsnRtn):

    class Meta:
        managed = True
        db_table = 'tsrsn_rtn'


class TStack(BaseSourceFields, Stack):

    class Meta:
        managed = True
        db_table = 'tstack'


# class TStm(BaseSourceFields, Stm):
#
#     class Meta:
#         managed = True
#         db_table = 'tstm'


class TStmDel(BaseSourceFields, StmDel):

    class Meta:
        managed = True
        db_table = 'tstm_del'


class TStrana(BaseSourceFields, Strana):

    class Meta:
        managed = True
        db_table = 'tstrana'


class TStt(BaseSourceFields, Stt):

    class Meta:
        managed = True
        db_table = 'tstt'


class TSubject(BaseSourceFields, Subject):

    class Meta:
        managed = True
        db_table = 'tsubject'


class TSubject0(BaseSourceFields, Subject0):

    class Meta:
        managed = True
        db_table = 'tsubject_'


class TSutp(BaseSourceFields, Sutp):

    class Meta:
        managed = True
        db_table = 'tsutp'


class TSysKtpt(BaseSourceFields, SysKtpt):

    class Meta:
        managed = True
        db_table = 'tsys_ktpt'


class TTDoc(BaseSourceFields, TDoc):

    class Meta:
        managed = True
        db_table = 'tt_doc'


class TTab47B(BaseSourceFields, Tab47B):

    class Meta:
        managed = True
        db_table = 'ttab47b'


class TTabnar(BaseSourceFields, Tabnar):

    class Meta:
        managed = True
        db_table = 'ttabnar'


class TTam(BaseSourceFields, Tam):

    class Meta:
        managed = True
        db_table = 'ttam'


class TTamplat(BaseSourceFields, Tamplat):

    class Meta:
        managed = True
        db_table = 'ttamplat'


class TTamplat0(BaseSourceFields, Tamplat0):

    class Meta:
        managed = True
        db_table = 'ttamplat_'


class TTampred(BaseSourceFields, Tampred):

    class Meta:
        managed = True
        db_table = 'ttampred'


class TTampred1(BaseSourceFields, Tampred1):

    class Meta:
        managed = True
        db_table = 'ttampred1'


class TTampred2(BaseSourceFields, Tampred2):

    class Meta:
        managed = True
        db_table = 'ttampred2'


class TTampred3(BaseSourceFields, Tampred3):

    class Meta:
        managed = True
        db_table = 'ttampred3'


class TTampred4(BaseSourceFields, Tampred4):

    class Meta:
        managed = True
        db_table = 'ttampred4'


class TTamst(BaseSourceFields, Tamst):

    class Meta:
        managed = True
        db_table = 'ttamst'


class TTamstavt(BaseSourceFields, Tamstavt):

    class Meta:
        managed = True
        db_table = 'ttamstavt'


class TTbrok(BaseSourceFields, Tbrok):

    class Meta:
        managed = True
        db_table = 'ttbrok'


class TTbrok1(BaseSourceFields, Tbrok1):

    class Meta:
        managed = True
        db_table = 'ttbrok1'


class TTbrok2(BaseSourceFields, Tbrok2):

    class Meta:
        managed = True
        db_table = 'ttbrok2'


class TTbrok3(BaseSourceFields, Tbrok3):

    class Meta:
        managed = True
        db_table = 'ttbrok3'


class TTbrok4(BaseSourceFields, Tbrok4):

    class Meta:
        managed = True
        db_table = 'ttbrok4'


class TTbrok5(BaseSourceFields, Tbrok5):

    class Meta:
        managed = True
        db_table = 'ttbrok5'


class TTbrok6(BaseSourceFields, Tbrok6):

    class Meta:
        managed = True
        db_table = 'ttbrok6'


class TTbrok7(BaseSourceFields, Tbrok7):

    class Meta:
        managed = True
        db_table = 'ttbrok7'


class TTbrok8(BaseSourceFields, Tbrok8):

    class Meta:
        managed = True
        db_table = 'ttbrok8'


class TTipdv(BaseSourceFields, Tipdv):

    class Meta:
        managed = True
        db_table = 'ttipdv'


class TTipts(BaseSourceFields, Tipts):

    class Meta:
        managed = True
        db_table = 'ttipts'


class TTiptsS(BaseSourceFields, TiptsS):

    class Meta:
        managed = True
        db_table = 'ttipts_s'


class TTk(BaseSourceFields, Tk):

    class Meta:
        managed = True
        db_table = 'ttk'


class TTk1(BaseSourceFields, Tk1):

    class Meta:
        managed = True
        db_table = 'ttk1'


class TTndti14(BaseSourceFields, Tndti14):

    class Meta:
        managed = True
        db_table = 'ttndti14'


class TTnvLtd(BaseSourceFields, TnvLtd):

    class Meta:
        managed = True
        db_table = 'ttnv_ltd'


class TTnvStav(BaseSourceFields, TnvStav):

    class Meta:
        managed = True
        db_table = 'ttnv_stav'


class TTnved(BaseSourceFields, Tnved):

    class Meta:
        managed = True
        db_table = 'ttnved'


class TTnved1(BaseSourceFields, Tnved1):

    class Meta:
        managed = True
        db_table = 'ttnved1'


class TTnved2(BaseSourceFields, Tnved2):

    class Meta:
        managed = True
        db_table = 'ttnved2'


class TTnved3(BaseSourceFields, Tnved3):

    class Meta:
        managed = True
        db_table = 'ttnved3'


class TTnved4(BaseSourceFields, Tnved4):

    class Meta:
        managed = True
        db_table = 'ttnved4'


class TTnved6(BaseSourceFields, Tnved6):

    class Meta:
        managed = True
        db_table = 'ttnved6'


class TTnved8(BaseSourceFields, Tnved8):

    class Meta:
        managed = True
        db_table = 'ttnved8'


class TTnved9(BaseSourceFields, Tnved9):

    class Meta:
        managed = True
        db_table = 'ttnved9'


class TTovW(BaseSourceFields, TovW):

    class Meta:
        managed = True
        db_table = 'ttov_w'


class TTovsign(BaseSourceFields, Tovsign):

    class Meta:
        managed = True
        db_table = 'ttovsign'


class TTpoPlt(BaseSourceFields, TpoPlt):

    class Meta:
        managed = True
        db_table = 'ttpo_plt'


class TTrans(BaseSourceFields, Trans):

    class Meta:
        managed = True
        db_table = 'ttrans'


class TTs(BaseSourceFields, Ts):

    class Meta:
        managed = True
        db_table = 'tts'


class TTsk(BaseSourceFields, Tsk):

    class Meta:
        managed = True
        db_table = 'ttsk'


class TTskat(BaseSourceFields, Tskat):

    class Meta:
        managed = True
        db_table = 'ttskat'


class TUpravl(BaseSourceFields, Upravl):

    class Meta:
        managed = True
        db_table = 'tupravl'


class TUslpost(BaseSourceFields, Uslpost):

    class Meta:
        managed = True
        db_table = 'tuslpost'


class TUtilsbor(BaseSourceFields, Utilsbor):

    class Meta:
        managed = True
        db_table = 'tutilsbor'


class TV2(BaseSourceFields, V2):

    class Meta:
        managed = True
        db_table = 'tv2'


class TVObup(BaseSourceFields, VObup):

    class Meta:
        managed = True
        db_table = 'tv_obup'


class TVal(BaseSourceFields, Val):

    class Meta:
        managed = True
        db_table = 'tval'


class TValCen(BaseSourceFields, ValCen):

    class Meta:
        managed = True
        db_table = 'tval_cen'


class TValname(BaseSourceFields, Valname):

    class Meta:
        managed = True
        db_table = 'tvalname'


class TValuta(BaseSourceFields, Valuta):

    class Meta:
        managed = True
        db_table = 'tvaluta'


class TVidAmts(BaseSourceFields, VidAmts):

    class Meta:
        managed = True
        db_table = 'tvid_amts'


class TVidDoc(BaseSourceFields, VidDoc):

    class Meta:
        managed = True
        db_table = 'tvid_doc'


class TViddvig(BaseSourceFields, Viddvig):

    class Meta:
        managed = True
        db_table = 'tviddvig'


class TVidtrans(BaseSourceFields, Vidtrans):

    class Meta:
        managed = True
        db_table = 'tvidtrans'


class TVidupak(BaseSourceFields, Vidupak):

    class Meta:
        managed = True
        db_table = 'tvidupak'


class TVkortd(BaseSourceFields, Vkortd):

    class Meta:
        managed = True
        db_table = 'tvkortd'


class TVkvot(BaseSourceFields, Vkvot):

    class Meta:
        managed = True
        db_table = 'tvkvot'


class TVpertr(BaseSourceFields, Vpertr):

    class Meta:
        managed = True
        db_table = 'tvpertr'


class TVspupr(BaseSourceFields, Vspupr):

    class Meta:
        managed = True
        db_table = 'tvspupr'


class TVtsTov(BaseSourceFields, VtsTov):

    class Meta:
        managed = True
        db_table = 'tvts_tov'


class TVtsZakl(BaseSourceFields, VtsZakl):

    class Meta:
        managed = True
        db_table = 'tvts_zakl'


class TWaybill(BaseSourceFields, Waybill):

    class Meta:
        managed = True
        db_table = 'twaybill'


class TYear(BaseSourceFields, Year):

    class Meta:
        managed = True
        db_table = 'tyear'


class TZan(BaseSourceFields, Zan):

    class Meta:
        managed = True
        db_table = 'tzan'


class TZvet(BaseSourceFields, Zvet):

    class Meta:
        managed = True
        db_table = 'tzvet'
