#####################################################################################
# import models for NSI
#####################################################################################
from .models import (
    TAddDoc, TAddress, TAdpPrim, TAkcPrim, TAllIncl, TAllOper,
    TArxReg, TAtdPos, TAutonz, TBankIzm, TBanklist, TBartPc,
    TBgDp, TBignalog, TBignalto, TBkbkn, TBlank, TBmonth,
    TBnkseek, TBrok, TBx, TCar, TCarrier, TCarrierb, TCbContr,
    TChkpoint, TCntr, TCrV, TCrdts, TCtovR, TCtu, TCurrency,
    TCustlist, TCustoms, TCustpost, TD44MPr, TD44MTn, TD44Mask,
    TD44Sfoiv, TDeclrnt, TDelstakc, TDipPrim, TDnbdlist,
    TDobstakc, TDoc, TDocAmts, TDocPr, TDocTnv, TDocg44, TDocum,
    TDocument, TDohNepr, TDohOsn, TDolgAll, TDov, TDtamreg,
    TEcop, TEcop1, TEcop2, TEcop3, TEcop4, TEcop5, TEdizm,
    TEdizmDp, TEkAr, TEkEu, TExpPrim, TExperimt, TExpstakc,
    TExtremM, TFaItemc, TFaPredm, TFinbg, TFinbg0, TFmtk,
    TFormras, TFstRaz, TFstZakl, TGarant, TGdOtd, TGdStan,
    TGeoAr, TGrp, THold, TImpPrim, TInFirm, TIndicEf, TIndnsi,
    TInf1Td, TInfEais, TInfram, TIzgot, TKat, TKateg, TKategwar,
    TKatt, TKkk, TKl203B, TKl203E, TKl203I, TKl204,
    TKl204B, TKl204Ing, TKlStav, TKlass203, TKlass204, TKlass205,
    TKlirVal, TKliring, TKodG300, TKodkdt, TKodktc,
    TKomop, TKray, TKtam, TKtam1, TKtam2, TKtamatr, TKtamolap,
    TKtamold, TKtddl, TKvota, TKvz, TLgotUv, TLicTi, TLicTov,
    TLicTv, TLocKntr, TLostTir, TMarAkc, TMaxstakc, TMdpAdr,
    TMdpD, TMdpKont, TMeasures, TMintnv, TMnt, TMosKtam, TMotc,
    TMotsfl, TMps, TMpsreg, TMrkCar, TMrkCars, TNamefirm, TNar,
    TNarVtt, TNewTi, TNlstmpr, TNpech, TNprsSbj, TNsDolgn,
    TNsDul, TNsDulT, TNsDulV, TNsGr31, TNsMpo, TNsOd31, TNsTsfl,
    TNsiKbk, TNullstB, TO803, TObject0, TOfdoc, TOgovorka,
    TOkaPk38, TOkaPk44, TOkaPk48, TOkaPk65, TOkaPk66, TOkaPk72,
    TOkaPk75, TOkaPk76, TOkaPk79, TOkaPk82, TOkaPk83,
    TOkaPk84, TOkaPk85, TOkaPk86, TOkaPk87, TOkaPk88, TOkaPk89,
    TOkato, TOkatosrf, TOksmt, TOprMeas, TOrgNpr, TOrtov,
    TOsdelka, TOsf, TOstamplt, TOstamplu, TOtamreg, TOtr, TOutp,
    TOzvet, TPasport, TPech, TPechDel, TPechKpv, TPechvid,
    TPedhDel, TPermSch, TPermit, TPlbase, TPlomDel, TPlombir,
    TPointDa, TPointIn, TPointNe, TPointOp, TPointRe, TPoluch,
    TPravo, TPredresh, TPrice, TPrice10, TPriceg, TPrimAdp, TPrimBg,
    TPrimBzp, TPrimKod, TPrimLec, TPrimLic, TPrimMrk,
    TPrimNdc, TPrimPr0, TPrimPrf, TPrimPry, TPrimSpr, TPrimSt1,
    TPrmCont, TPrstate, TPzkOrd, TRam, TRdBg872, TRe12Tm,
    TReAct, TReArhiv, TReDeist, TReDelo, TReDopps, TReDoprv, TReLi,
    TReLsoi, TReLsov, TReLv, TReMist, TRePost, TRePrich,
    TReRvto, TReSttk, TReTmist, TReZalob, TRecom, TReg, TRegK,
    TRegMvs, TRegS, TRegTi, TRegTi1, TRegTit, TRegiK,
    TRegpltls, TRegtiTe, TReshdel, TRezultto, TRezultto1, TRmbt,
    TRmd, TRmdG, TRmtotok, TRole, TRpsi, TRskCrit,
    TRskFinp, TRskMera, TRskNdpd, TRskNinf, TRskNmb, TRskNpm,
    TRskPrim, TRskRsmr, TRskRsnd, TRskRspr, TRskSpdr0,
    TRskTprc, TRskrmera, TRskrsdsm, TRskrsprc, TRskspdr, TRsksppri,
    TRsktmera, TRskxdosm, TRskzdosm, TRsnBpos, TRsnBuss,
    TRsnCntr, TRsnEntf, TRsnEntr, TRsnFlab, TRsnOrg, TRsnOrgt,
    TRsnProd, TRsnSpro, TRsnTarg, TRsnTdep, TRsnTsto,
    TRsnUnit, TRsnVlab, TRstrH, TRstrKat, TRstrLic, TRstrN, TRstrOis,
    TRstrTov, TRstrTz, TRstrpath, TSExhib, TSExhid,
    TSObutp, TSbj, TSbjCst, TSbjExt, TSbjRole, TSbxDel, TSdelka,
    TSelfnsi1, TSertS, TSertif, TSertif4, TSezPrim,
    TSklStt, TSklad, TSkladbx, TSkladtB, TSkladtm, TSkladvB,
    TSkrecc, TSoato, TSokr, TSono, TSoun1, TSource, TSpTovW,
    TSpcPrim, TSpcproc, TSpzkRsn, TSrsnRtn, TStack, TStmDel,
    TStrana, TStt, TSubject, TSubject0, TSutp, TSysKtpt, TTDoc,
    TTab47B, TTabnar, TTam, TTamplat, TTamplat0, TTampred,
    TTampred1, TTampred2, TTampred3, TTampred4, TTamst,
    TTamstavt, TTbrok, TTbrok1, TTbrok2, TTbrok3, TTbrok4,
    TTbrok5, TTbrok6, TTbrok7, TTbrok8, TTipdv, TTipts, TTiptsS,
    TTk, TTk1, TTndti14, TTnvLtd, TTnvStav, TTnved, TTnved1,
    TTnved2, TTnved3, TTnved4, TTnved6, TTnved8, TTnved9,
    TTovW, TTovsign, TTpoPlt, TTrans, TTs, TTsk, TTskat, TUpravl,
    TUslpost, TUtilsbor, TV2, TVObup, TVal, TValCen,
    TValname, TValuta, TVidAmts, TVidDoc, TViddvig, TVidtrans,
    TVidupak, TVkortd, TVkvot, TVpertr, TVspupr, TVtsTov,
    TVtsZakl, TWaybill, TYear, TZan, TZvet, Tab47B, Tabnar, Tam,
    Tamplat, Tamplat0, Tampred, Tampred1, Tampred2,
    Tampred3, Tampred4, Tamst, Tamstavt, Tbrok, Tbrok1, Tbrok2,
    Tbrok3, Tbrok4, Tbrok5, Tbrok6, Tbrok7, Tbrok8, Tipdv,
    Tipts, TiptsS, Tk, Tk1, Tndti14, TnvLtd, TnvStav, Tnved,
    Tnved1, Tnved2, Tnved3, Tnved4, Tnved6, Tnved8, Tnved9,
    TovW, Tovsign, TpoPlt, Trans, Ts, Tsk, Tskat,
)
from src.apps.common import mixins


class TAddDocResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TAddDoc


class TAddressResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TAddress


class TAdpPrimResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TAdpPrim


class TAkcPrimResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TAkcPrim


class TAllInclResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TAllIncl


class TAllOperResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TAllOper


class TArxRegResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TArxReg


class TAtdPosResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TAtdPos


class TAutonzResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TAutonz


class TBankIzmResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TBankIzm


class TBanklistResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TBanklist


class TBartPcResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TBartPc


class TBgDpResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TBgDp


class TBignalogResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TBignalog


class TBignaltoResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TBignalto


class TBkbknResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TBkbkn


class TBlankResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TBlank


class TBmonthResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TBmonth


class TBnkseekResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TBnkseek


class TBrokResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TBrok


class TBxResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TBx


class TCarResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TCar


class TCarrierResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TCarrier


class TCarrierbResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TCarrierb


class TCbContrResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TCbContr


class TChkpointResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TChkpoint


class TCntrResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TCntr


class TCrVResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TCrV


class TCrdtsResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TCrdts


class TCtovRResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TCtovR


class TCtuResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TCtu


class TCurrencyResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TCurrency


class TCustlistResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TCustlist


class TCustomsResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TCustoms


class TCustpostResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TCustpost


class TD44MPrResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TD44MPr


class TD44MTnResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TD44MTn


class TD44MaskResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TD44Mask


class TD44SfoivResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TD44Sfoiv


class TDeclrntResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDeclrnt


class TDelstakcResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDelstakc


class TDipPrimResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDipPrim


class TDnbdlistResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDnbdlist


class TDobstakcResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDobstakc


class TDocResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDoc


class TDocAmtsResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDocAmts


class TDocPrResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDocPr


class TDocTnvResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDocTnv


class TDocg44Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDocg44


class TDocumResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDocum


class TDocumentResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDocument


class TDohNeprResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDohNepr


class TDohOsnResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDohOsn


class TDolgAllResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDolgAll


class TDovResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDov


class TDtamregResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDtamreg


class TEcopResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TEcop


class TEcop1Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TEcop1


class TEcop2Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TEcop2


class TEcop3Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TEcop3


class TEcop4Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TEcop4


class TEcop5Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TEcop5


class TEdizmResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TEdizm


class TEdizmDpResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TEdizmDp


class TEkArResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TEkAr


class TEkEuResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TEkEu


class TExpPrimResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TExpPrim


class TExperimtResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TExperimt


class TExpstakcResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TExpstakc


class TExtremMResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TExtremM


class TFaItemcResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TFaItemc


class TFaPredmResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TFaPredm


class TFinbgResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TFinbg


class TFinbg0Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TFinbg0


class TFmtkResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TFmtk


class TFormrasResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TFormras


class TFstRazResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TFstRaz


class TFstZaklResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TFstZakl


class TGarantResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TGarant


class TGdOtdResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TGdOtd


class TGdStanResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TGdStan


class TGeoArResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TGeoAr


class TGrpResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TGrp


class THoldResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = THold


class TImpPrimResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TImpPrim


class TInFirmResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TInFirm


class TIndicEfResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TIndicEf


class TIndnsiResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TIndnsi


class TInf1TdResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TInf1Td


class TInfEaisResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TInfEais


class TInframResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TInfram


class TIzgotResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TIzgot


class TKatResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKat


class TKategResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKateg


class TKategwarResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKategwar


class TKattResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKatt


class TKkkResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKkk


class TKl203BResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKl203B


class TKl203EResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKl203E


class TKl203IResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKl203I


class TKl204Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKl204


class TKl204BResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKl204B


class TKl204IngResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKl204Ing


class TKlStavResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKlStav


class TKlass203Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKlass203


class TKlass204Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKlass204


class TKlass205Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKlass205


class TKlirValResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKlirVal


class TKliringResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKliring


class TKodG300Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKodG300


class TKodkdtResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKodkdt


class TKodktcResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKodktc


class TKomopResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKomop


class TKrayResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKray


class TKtamResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtam


class TKtam1Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtam1


class TKtam2Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtam2


class TKtamatrResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtamatr


class TKtamolapResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtamolap


class TKtamoldResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtamold


class TKtddlResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtddl


class TKvotaResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKvota


class TKvzResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKvz


class TLgotUvResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TLgotUv


class TLicTiResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TLicTi


class TLicTovResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TLicTov


class TLicTvResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TLicTv


class TLocKntrResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TLocKntr


class TLostTirResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TLostTir


class TMarAkcResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TMarAkc


class TMaxstakcResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TMaxstakc


class TMdpAdrResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TMdpAdr


class TMdpDResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TMdpD


class TMdpKontResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TMdpKont


class TMeasuresResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TMeasures


class TMintnvResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TMintnv


class TMntResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TMnt


class TMosKtamResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TMosKtam


class TMotcResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TMotc


class TMotsflResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TMotsfl


class TMpsResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TMps


class TMpsregResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TMpsreg


class TMrkCarResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TMrkCar


class TMrkCarsResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TMrkCars


class TNamefirmResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TNamefirm


class TNarResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TNar


class TNarVttResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TNarVtt


class TNewTiResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TNewTi


class TNlstmprResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TNlstmpr


class TNpechResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TNpech


class TNprsSbjResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TNprsSbj


class TNsDolgnResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TNsDolgn


class TNsDulResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TNsDul


class TNsDulTResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TNsDulT


class TNsDulVResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TNsDulV


class TNsGr31Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TNsGr31


class TNsMpoResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TNsMpo


class TNsOd31Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TNsOd31


class TNsTsflResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TNsTsfl


class TNsiKbkResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TNsiKbk


class TNullstBResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TNullstB


class TO803Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TO803


class TObject0Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TObject0


class TOfdocResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TOfdoc


class TOgovorkaResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TOgovorka


class TOkaPk38Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TOkaPk38


class TOkaPk44Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TOkaPk44


class TOkaPk48Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TOkaPk48


class TOkaPk65Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TOkaPk65


class TOkaPk66Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TOkaPk66


class TOkaPk72Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TOkaPk72


class TOkaPk75Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TOkaPk75


class TOkaPk76Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TOkaPk76


class TOkaPk79Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TOkaPk79


class TOkaPk82Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TOkaPk82


class TOkaPk83Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TOkaPk83


class TOkaPk84Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TOkaPk84


class TOkaPk85Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TOkaPk85


class TOkaPk86Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TOkaPk86


class TOkaPk87Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TOkaPk87


class TOkaPk88Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TOkaPk88


class TOkaPk89Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TOkaPk89


class TOkatoResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TOkato


class TOkatosrfResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TOkatosrf


class TOksmtResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TOksmt


class TOprMeasResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TOprMeas


class TOrgNprResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TOrgNpr


class TOrtovResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TOrtov


class TOsdelkaResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TOsdelka


class TOsfResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TOsf


class TOstampltResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TOstamplt


class TOstampluResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TOstamplu


class TOtamregResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TOtamreg


class TOtrResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TOtr


class TOutpResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TOutp


class TOzvetResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TOzvet


class TPasportResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TPasport


class TPechResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TPech


class TPechDelResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TPechDel


class TPechKpvResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TPechKpv


class TPechvidResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TPechvid


class TPedhDelResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TPedhDel


class TPermSchResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TPermSch


class TPermitResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TPermit


class TPlbaseResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TPlbase


class TPlomDelResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TPlomDel


class TPlombirResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TPlombir


class TPointDaResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TPointDa


class TPointInResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TPointIn


class TPointNeResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TPointNe


class TPointOpResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TPointOp


class TPointReResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TPointRe


class TPoluchResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TPoluch


class TPravoResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TPravo


class TPredreshResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TPredresh


class TPriceResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TPrice


class TPrice10Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TPrice10


class TPricegResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TPriceg


class TPrimAdpResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TPrimAdp


class TPrimBgResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TPrimBg


class TPrimBzpResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TPrimBzp


class TPrimKodResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TPrimKod


class TPrimLecResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TPrimLec


class TPrimLicResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TPrimLic


class TPrimMrkResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TPrimMrk


class TPrimNdcResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TPrimNdc


class TPrimPr0Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TPrimPr0


class TPrimPrfResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TPrimPrf


class TPrimPryResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TPrimPry


class TPrimSprResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TPrimSpr


class TPrimSt1Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TPrimSt1


class TPrmContResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TPrmCont


class TPrstateResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TPrstate


class TPzkOrdResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TPzkOrd


class TRamResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRam


class TRdBg872Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRdBg872


class TRe12TmResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRe12Tm


class TReActResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TReAct


class TReArhivResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TReArhiv


class TReDeistResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TReDeist


class TReDeloResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TReDelo


class TReDoppsResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TReDopps


class TReDoprvResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TReDoprv


class TReLiResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TReLi


class TReLsoiResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TReLsoi


class TReLsovResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TReLsov


class TReLvResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TReLv


class TReMistResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TReMist


class TRePostResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRePost


class TRePrichResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRePrich


class TReRvtoResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TReRvto


class TReSttkResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TReSttk


class TReTmistResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TReTmist


class TReZalobResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TReZalob


class TRecomResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRecom


class TRegResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TReg


class TRegKResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRegK


class TRegMvsResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRegMvs


class TRegSResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRegS


class TRegTiResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRegTi


class TRegTi1Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRegTi1


class TRegTitResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRegTit


class TRegiKResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRegiK


class TRegpltlsResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRegpltls


class TRegtiTeResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRegtiTe


class TReshdelResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TReshdel


class TRezulttoResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRezultto


class TRezultto1Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRezultto1


class TRmbtResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRmbt


class TRmdResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRmd


class TRmdGResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRmdG


class TRmtotokResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRmtotok


class TRoleResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRole


class TRpsiResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRpsi


class TRskCritResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRskCrit


class TRskFinpResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRskFinp


class TRskMeraResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRskMera


class TRskNdpdResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRskNdpd


class TRskNinfResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRskNinf


class TRskNmbResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRskNmb


class TRskNpmResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRskNpm


class TRskPrimResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRskPrim


class TRskRsmrResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRskRsmr


class TRskRsndResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRskRsnd


class TRskRsprResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRskRspr


class TRskSpdr0Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRskSpdr0


class TRskTprcResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRskTprc


class TRskrmeraResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRskrmera


class TRskrsdsmResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRskrsdsm


class TRskrsprcResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRskrsprc


class TRskspdrResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRskspdr


class TRsksppriResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRsksppri


class TRsktmeraResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRsktmera


class TRskxdosmResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRskxdosm


class TRskzdosmResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRskzdosm


class TRsnBposResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRsnBpos


class TRsnBussResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRsnBuss


class TRsnCntrResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRsnCntr


class TRsnEntfResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRsnEntf


class TRsnEntrResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRsnEntr


class TRsnFlabResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRsnFlab


class TRsnOrgResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRsnOrg


class TRsnOrgtResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRsnOrgt


class TRsnProdResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRsnProd


class TRsnSproResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRsnSpro


class TRsnTargResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRsnTarg


class TRsnTdepResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRsnTdep


class TRsnTstoResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRsnTsto


class TRsnUnitResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRsnUnit


class TRsnVlabResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRsnVlab


class TRstrHResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRstrH


class TRstrKatResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRstrKat


class TRstrLicResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRstrLic


class TRstrNResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRstrN


class TRstrOisResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRstrOis


class TRstrTovResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRstrTov


class TRstrTzResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRstrTz


class TRstrpathResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TRstrpath


class TSExhibResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TSExhib


class TSExhidResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TSExhid


class TSObutpResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TSObutp


class TSbjResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TSbj


class TSbjCstResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TSbjCst


class TSbjExtResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TSbjExt


class TSbjRoleResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TSbjRole


class TSbxDelResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TSbxDel


class TSdelkaResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TSdelka


class TSelfnsi1Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TSelfnsi1


class TSertSResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TSertS


class TSertifResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TSertif


class TSertif4Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TSertif4


class TSezPrimResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TSezPrim


class TSklSttResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TSklStt


class TSkladResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TSklad


class TSkladbxResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TSkladbx


class TSkladtBResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TSkladtB


class TSkladtmResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TSkladtm


class TSkladvBResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TSkladvB


class TSkreccResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TSkrecc


class TSoatoResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TSoato


class TSokrResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TSokr


class TSonoResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TSono


class TSoun1Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TSoun1


class TSourceResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TSource


class TSpTovWResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TSpTovW


class TSpcPrimResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TSpcPrim


class TSpcprocResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TSpcproc


class TSpzkRsnResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TSpzkRsn


class TSrsnRtnResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TSrsnRtn


class TStackResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TStack


class TStmDelResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TStmDel


class TStranaResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TStrana


class TSttResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TStt


class TSubjectResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TSubject


class TSubject0Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TSubject0


class TSutpResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TSutp


class TSysKtptResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TSysKtpt


class TTDocResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TTDoc


class TTab47BResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TTab47B


class TTabnarResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TTabnar


class TTamResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TTam


class TTamplatResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TTamplat


class TTamplat0Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TTamplat0


class TTampredResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TTampred


class TTampred1Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TTampred1


class TTampred2Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TTampred2


class TTampred3Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TTampred3


class TTampred4Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TTampred4


class TTamstResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TTamst


class TTamstavtResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TTamstavt


class TTbrokResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TTbrok


class TTbrok1Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TTbrok1


class TTbrok2Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TTbrok2


class TTbrok3Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TTbrok3


class TTbrok4Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TTbrok4


class TTbrok5Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TTbrok5


class TTbrok6Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TTbrok6


class TTbrok7Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TTbrok7


class TTbrok8Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TTbrok8


class TTipdvResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TTipdv


class TTiptsResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TTipts


class TTiptsSResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TTiptsS


class TTkResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TTk


class TTk1Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TTk1


class TTndti14Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TTndti14


class TTnvLtdResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TTnvLtd


class TTnvStavResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TTnvStav


class TTnvedResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TTnved


class TTnved1Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TTnved1


class TTnved2Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TTnved2


class TTnved3Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TTnved3


class TTnved4Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TTnved4


class TTnved6Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TTnved6


class TTnved8Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TTnved8


class TTnved9Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TTnved9


class TTovWResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TTovW


class TTovsignResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TTovsign


class TTpoPltResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TTpoPlt


class TTransResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TTrans


class TTsResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TTs


class TTskResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TTsk


class TTskatResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TTskat


class TUpravlResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TUpravl


class TUslpostResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TUslpost


class TUtilsborResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TUtilsbor


class TV2Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TV2


class TVObupResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TVObup


class TValResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TVal


class TValCenResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TValCen


class TValnameResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TValname


class TValutaResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TValuta


class TVidAmtsResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TVidAmts


class TVidDocResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TVidDoc


class TViddvigResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TViddvig


class TVidtransResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TVidtrans


class TVidupakResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TVidupak


class TVkortdResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TVkortd


class TVkvotResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TVkvot


class TVpertrResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TVpertr


class TVspuprResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TVspupr


class TVtsTovResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TVtsTov


class TVtsZaklResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TVtsZakl


class TWaybillResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TWaybill


class TYearResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TYear


class TZanResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TZan


class TZvetResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TZvet


class Tab47BResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = Tab47B


class TabnarResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = Tabnar


class TamResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = Tam


class TamplatResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = Tamplat


class Tamplat0Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = Tamplat0


class TampredResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = Tampred


class Tampred1Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = Tampred1


class Tampred2Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = Tampred2


class Tampred3Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = Tampred3


class Tampred4Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = Tampred4


class TamstResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = Tamst


class TamstavtResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = Tamstavt


class TbrokResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = Tbrok


class Tbrok1Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = Tbrok1


class Tbrok2Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = Tbrok2


class Tbrok3Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = Tbrok3


class Tbrok4Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = Tbrok4


class Tbrok5Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = Tbrok5


class Tbrok6Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = Tbrok6


class Tbrok7Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = Tbrok7


class Tbrok8Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = Tbrok8


class TipdvResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = Tipdv


class TiptsResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = Tipts


class TiptsSResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TiptsS


class TkResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = Tk


class Tk1Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = Tk1


class Tndti14Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = Tndti14


class TnvLtdResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TnvLtd


class TnvStavResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TnvStav


class TnvedResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = Tnved


class Tnved1Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = Tnved1


class Tnved2Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = Tnved2


class Tnved3Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = Tnved3


class Tnved4Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = Tnved4


class Tnved6Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = Tnved6


class Tnved8Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = Tnved8


class Tnved9Resource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = Tnved9


class TovWResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TovW


class TovsignResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = Tovsign


class TpoPltResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = TpoPlt


class TransResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = Trans


class TsResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = Ts


class TskResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = Tsk


class TskatResource(mixins.ExtResource):
    class Meta(mixins.ExtResource.Meta):
        model = Tskat
