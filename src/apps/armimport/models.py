from src.apps.armexport.base.models import (
    Dbramnum, Dbravtmb, Dbrcont, Dbrcrdts,
    Dbrdinf2, Dbrdinfo, Dbrdog, Dbrdoga, Dbrdogt,
    Dbrdop48, Dbrhead, Dbrkmp, Dcllistd, Dcllisth,
    Dcllistl, Dbrkmpk, Dbrpasp, Dbrpk, Dbrplatr,
    Dbrplatv, Dbrpredd, Dclquerd, Dclquerh, Dbrsumpp,
    Dbrtechd, Dbrterms, Dbrtov2, Dbrtovar, Dbrtovg,
    Dbrtovg2, Dbrtovs, Dbrtovs2, Dbrtrans, Dbruslt,
    Sbrddtc, Sbrdinfo, Sbrhead, Sbrsscv, Sbrsstc,
    Kbravtmb, Kbrdinfo, Kbrdokiz, Kbrhead,
    Kbrpk, Kbrplbiz, Kbrpltiz, Kbrsumpp, Kbrterms,
    Kbrtovg, Kbrtoviz, Kbrtovs, Ktdavtmb, Ktdamnum,
    Ktdcont, Ktdcrdts, Ktddinf2, Ktddinfo, Ktddog,
    Ktddoga, Ktddogt, Ktdhead, Ktdkmp, Ktdkmpk,
    Ktdpasp, Ktdpk, Ktdplatr, Ktdplatv, Ktdpredd,
    Ktdsumpp, Ktdtechd, Ktdterms, Ktdtov2, Ktdtovar,
    Ktdtovg, Ktdtovg2, Ktdtovs, Ktdtrans, Ktduslt,
)
from src.apps.common.mixins import ExtArmFields


class TDclAmnum(Dbramnum, ExtArmFields):
    class Meta:
        db_table = 'dclamnum'


class TDclAvtmb(Dbravtmb, ExtArmFields):
    class Meta:
        db_table = 'dclavtmb'


class TDclCont(Dbrcont, ExtArmFields):
    class Meta:
        db_table = 'dclcont'


class TDclCrdts(Dbrcrdts, ExtArmFields):
    class Meta:
        db_table = 'dclcrdts'


class TDclDinf2(Dbrdinf2, ExtArmFields):
    class Meta:
        db_table = 'dcldinf2'


class TDclDinfo(Dbrdinfo, ExtArmFields):
    class Meta:
        db_table = 'dcldinfo'


class TDclDog(Dbrdog, ExtArmFields):
    class Meta:
        db_table = 'dcldog'


class TDclDoga(Dbrdoga, ExtArmFields):
    class Meta:
        db_table = 'dcldoga'


class TDclDogt(Dbrdogt, ExtArmFields):
    class Meta:
        db_table = 'dcldogt'


class TDclDop48(Dbrdop48, ExtArmFields):
    class Meta:
        db_table = 'dcldop48'


class TDclHead(Dbrhead, ExtArmFields):
    class Meta:
        db_table = 'dclhead'


class TDclKmp(Dbrkmp, ExtArmFields):
    class Meta:
        db_table = 'dclkmp'


class TDclKmpk(Dbrkmpk, ExtArmFields):
    class Meta:
        db_table = 'dclkmpk'


class TDclListd(Dcllistd, ExtArmFields):
    class Meta:
        db_table = 'dcllistd'


class TDclListh(Dcllisth, ExtArmFields):
    class Meta:
        db_table = 'dcllisth'


class TDclListl(Dcllistl, ExtArmFields):
    class Meta:
        db_table = 'dcllistl'


class TDclPasp(Dbrpasp, ExtArmFields):
    class Meta:
        db_table = 'dclpasp'


class TDclPk(Dbrpk, ExtArmFields):
    class Meta:
        db_table = 'dclpk'


class TDclPlatr(Dbrplatr, ExtArmFields):
    class Meta:
        db_table = 'dclplatr'


class TDclPlatv(Dbrplatv, ExtArmFields):
    class Meta:
        db_table = 'dclplatv'


class TDclPredd(Dbrpredd, ExtArmFields):
    class Meta:
        db_table = 'dclpredd'


class TDclQuerd(Dclquerd, ExtArmFields):
    class Meta:
        db_table = 'dclquerd'


class TDclQuerh(Dclquerh, ExtArmFields):
    class Meta:
        db_table = 'dclquerh'


class TDclSumpp(Dbrsumpp, ExtArmFields):
    class Meta:
        db_table = 'dclsumpp'


class TDbrTechd(Dbrtechd, ExtArmFields):
    class Meta:
        db_table = 'dcltechd'


class TDclTerms(Dbrterms, ExtArmFields):
    class Meta:
        db_table = 'dclterms'

class TDclTov2(Dbrtov2, ExtArmFields):
    class Meta:
        db_table = 'dcltov2'


class TDclTovar(Dbrtovar, ExtArmFields):
    class Meta:
        db_table = 'dcltovar'


class TDclTovg(Dbrtovg, ExtArmFields):
    class Meta:
        db_table = 'dcltovg'


class TDclTovg2(Dbrtovg2, ExtArmFields):
    class Meta:
        db_table = 'dcltovg2'


class TDclTovs(Dbrtovs, ExtArmFields):
    class Meta:
        db_table = 'dcltovs'


class TDclTovs2(Dbrtovs2, ExtArmFields):
    class Meta:
        db_table = 'dcltovs2'


class TDclTrans(Dbrtrans, ExtArmFields):
    class Meta:
        db_table = 'dcltrans'


class TDclUslt(Dbruslt, ExtArmFields):
    class Meta:
        db_table = 'dcluslt'


class TDtcDdtc(Sbrddtc, ExtArmFields):
    class Meta:
        db_table = 'dtcddtc'


class TDtcDinfo(Sbrdinfo, ExtArmFields):
    class Meta:
        db_table = 'dtcdinfo'


class TDtcHead(Sbrhead, ExtArmFields):
    class Meta:
        db_table = 'dtchead'


class TDtcSscv(Sbrsscv, ExtArmFields):
    class Meta:
        db_table = 'dtcsscv'


class TDtcSstc(Sbrsstc, ExtArmFields):
    class Meta:
        db_table = 'dtcsstc'


class TKtcAvtmb(Kbravtmb, ExtArmFields):
    class Meta:
        db_table = 'ktcavtmb'


class TKtcDinfo(Kbrdinfo, ExtArmFields):
    class Meta:
        db_table = 'ktcdinfo'


class TKtcDokiz(Kbrdokiz, ExtArmFields):
    class Meta:
        db_table = 'ktcdokiz'


class TKtcHead(Kbrhead, ExtArmFields):
    class Meta:
        db_table = 'ktchead'


class TKtcPk(Kbrpk, ExtArmFields):
    class Meta:
        db_table = 'ktcpk'


class TKtcPlbiz(Kbrplbiz, ExtArmFields):
    class Meta:
        db_table = 'ktcplbiz'


class TKtcPltiz(Kbrpltiz, ExtArmFields):
    class Meta:
        db_table = 'ktcpltiz'


class TKtcSumpp(Kbrsumpp, ExtArmFields):
    class Meta:
        db_table = 'ktcsumpp'


class TKtcTerms(Kbrterms, ExtArmFields):
    class Meta:
        db_table = 'ktcterms'


class TKtcTovg(Kbrtovg, ExtArmFields):
    class Meta:
        db_table = 'ktctovg'


class TKtcToviz(Kbrtoviz, ExtArmFields):
    class Meta:
        db_table = 'ktctoviz'


class TKtcTovs(Kbrtovs, ExtArmFields):
    class Meta:
        db_table = 'ktctovs'


class TKtdAvtmb(Ktdavtmb, ExtArmFields):
    class Meta:
        db_table = 'ktdavtmb'


class TKtdAmnum(Ktdamnum, ExtArmFields):
    class Meta:
        db_table = 'ktdamnum'


class TKtdCont(Ktdcont, ExtArmFields):
    class Meta:
        db_table = 'ktdcont'


class TKtdCrdts(Ktdcrdts, ExtArmFields):
    class Meta:
        db_table = 'ktdcrdts'


class TKtdDinf2(Ktddinf2, ExtArmFields):
    class Meta:
        db_table = 'ktddinf2'


class TKtdDinfo(Ktddinfo, ExtArmFields):
    class Meta:
        db_table = 'ktddinfo'

class TKtdDog(Ktddog, ExtArmFields):
    class Meta:
        db_table = 'ktddog'


class TKtdDoga(Ktddoga, ExtArmFields):
    class Meta:
        db_table = 'ktddoga'


class TKtdDogt(Ktddogt, ExtArmFields):
    class Meta:
        db_table = 'ktddogt'


class TKtdHead(Ktdhead, ExtArmFields):
    class Meta:
        db_table = 'ktdhead'


class TKtdKmp(Ktdkmp, ExtArmFields):
    class Meta:
        db_table = 'ktdkmp'


class TKtdKmpk(Ktdkmpk, ExtArmFields):
    class Meta:
        db_table = 'ktdkmpk'


class TKtdPasp(Ktdpasp, ExtArmFields):
    class Meta:
        db_table = 'ktdpasp'


class TKtdPk(Ktdpk, ExtArmFields):
    class Meta:
        db_table = 'ktdpk'


class TKtdPlatr(Ktdplatr, ExtArmFields):
    class Meta:
        db_table = 'ktdplatr'


class TKtdPlatv(Ktdplatv, ExtArmFields):
    class Meta:
        db_table = 'ktdplatv'


class TKtdPredd(Ktdpredd, ExtArmFields):
    class Meta:
        db_table = 'ktdpredd'


class TKtdSumpp(Ktdsumpp, ExtArmFields):
    class Meta:
        db_table = 'ktdsumpp'


class TKtdTechd(Ktdtechd, ExtArmFields):
    class Meta:
        db_table = 'ktdtechd'


class TKtdTerms(Ktdterms, ExtArmFields):
    class Meta:
        db_table = 'ktdterms'


class TKtdTov2(Ktdtov2, ExtArmFields):
    class Meta:
        db_table = 'ktdtov2'


class TKtdTovar(Ktdtovar, ExtArmFields):
    class Meta:
        db_table = 'ktdtovar'


class TKtdTovg(Ktdtovg, ExtArmFields):
    class Meta:
        db_table = 'ktdtovg'


class TKtdTovg2(Ktdtovg2, ExtArmFields):
    class Meta:
        db_table = 'ktdtovg2'


class TKtdTovs(Ktdtovs, ExtArmFields):
    class Meta:
        db_table = 'ktdtovs'


class TKtdTrans(Ktdtrans, ExtArmFields):
    class Meta:
        db_table = 'ktdtrans'


class TKtdUslt(Ktduslt, ExtArmFields):
    class Meta:
        db_table = 'ktduslt'
