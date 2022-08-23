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
    Kbrtovg, Kbrtoviz, Kbrtovs, Ktdavtmb,
    Ktdcont, Ktdcrdts, Ktddinf2, Ktddinfo, Ktddog,
    Ktddoga, Ktddogt, Ktdhead, Ktdkmp, Ktdkmpk,
    Ktdpasp, Ktdpk, Ktdplatr, Ktdplatv, Ktdpredd,
    Ktdsumpp, Ktdtechd, Ktdterms, Ktdtov2, Ktdtovar,
    Ktdtovg, Ktdtovg2, Ktdtovs, Ktdtrans, Ktduslt,
)
from src.apps.common.mixins import ExtSourceFields


class TDclAmnum(Dbramnum, ExtSourceFields):
    class Meta:
        db_table = 'dclamnum'


class TDclAvtmb(Dbravtmb, ExtSourceFields):
    class Meta:
        db_table = 'dclavtmb'


class TDclCont(Dbrcont, ExtSourceFields):
    class Meta:
        db_table = 'dclcont'


class TDclCrdts(Dbrcrdts, ExtSourceFields):
    class Meta:
        db_table = 'dclcrdts'


class TDclDinf2(Dbrdinf2, ExtSourceFields):
    class Meta:
        db_table = 'dcldinf2'


class TDclDinfo(Dbrdinfo, ExtSourceFields):
    class Meta:
        db_table = 'dcldinfo'


class TDclDog(Dbrdog, ExtSourceFields):
    class Meta:
        db_table = 'dcldog'


class TDclDoga(Dbrdoga, ExtSourceFields):
    class Meta:
        db_table = 'dcldoga'


class TDclDogt(Dbrdogt, ExtSourceFields):
    class Meta:
        db_table = 'dcldogt'


class TDclDop48(Dbrdop48, ExtSourceFields):
    class Meta:
        db_table = 'dcldop48'


class TDclHead(Dbrhead, ExtSourceFields):
    class Meta:
        db_table = 'dclhead'


class TDclKmp(Dbrkmp, ExtSourceFields):
    class Meta:
        db_table = 'dclkmp'


class TDclKmpk(Dbrkmpk, ExtSourceFields):
    class Meta:
        db_table = 'dclkmpk'


class TDclListd(Dcllistd, ExtSourceFields):
    class Meta:
        db_table = 'dcllistd'


class TDclListh(Dcllisth, ExtSourceFields):
    class Meta:
        db_table = 'dcllisth'


class TDclListl(Dcllistl, ExtSourceFields):
    class Meta:
        db_table = 'dcllistl'


class TDclPasp(Dbrpasp, ExtSourceFields):
    class Meta:
        db_table = 'dclpasp'


class TDclPk(Dbrpk, ExtSourceFields):
    class Meta:
        db_table = 'dclpk'


class TDclPlatr(Dbrplatr, ExtSourceFields):
    class Meta:
        db_table = 'dclplatr'


class TDclPlatv(Dbrplatv, ExtSourceFields):
    class Meta:
        db_table = 'dclplatv'


class TDclPredd(Dbrpredd, ExtSourceFields):
    class Meta:
        db_table = 'dclpredd'


class TDclQuerd(Dclquerd, ExtSourceFields):
    class Meta:
        db_table = 'dclquerd'


class TDclQuerh(Dclquerh, ExtSourceFields):
    class Meta:
        db_table = 'dclquerh'


class TDclSumpp(Dbrsumpp, ExtSourceFields):
    class Meta:
        db_table = 'dclsumpp'


class TDclTechd(Dbrtechd, ExtSourceFields):
    class Meta:
        db_table = 'dcltechd'


class TDclTerms(Dbrterms, ExtSourceFields):
    class Meta:
        db_table = 'dclterms'

class TDclTov2(Dbrtov2, ExtSourceFields):
    class Meta:
        db_table = 'dcltov2'


class TDclTovar(Dbrtovar, ExtSourceFields):
    class Meta:
        db_table = 'dcltovar'


class TDclTovg(Dbrtovg, ExtSourceFields):
    class Meta:
        db_table = 'dcltovg'


class TDclTovg2(Dbrtovg2, ExtSourceFields):
    class Meta:
        db_table = 'dcltovg2'


class TDclTovs(Dbrtovs, ExtSourceFields):
    class Meta:
        db_table = 'dcltovs'


class TDclTovs2(Dbrtovs2, ExtSourceFields):
    class Meta:
        db_table = 'dcltovs2'


class TDclTrans(Dbrtrans, ExtSourceFields):
    class Meta:
        db_table = 'dcltrans'


class TDclUslt(Dbruslt, ExtSourceFields):
    class Meta:
        db_table = 'dcluslt'


class TDtcDdtc(Sbrddtc, ExtSourceFields):
    class Meta:
        db_table = 'dtcddtc'


class TDtcDinfo(Sbrdinfo, ExtSourceFields):
    class Meta:
        db_table = 'dtcdinfo'


class TDtcHead(Sbrhead, ExtSourceFields):
    class Meta:
        db_table = 'dtchead'


class TDtcSscv(Sbrsscv, ExtSourceFields):
    class Meta:
        db_table = 'dtcsscv'


class TDtcSstc(Sbrsstc, ExtSourceFields):
    class Meta:
        db_table = 'dtcsstc'


class TKtcAvtmb(Kbravtmb, ExtSourceFields):
    class Meta:
        db_table = 'ktcavtmb'


class TKtcDinfo(Kbrdinfo, ExtSourceFields):
    class Meta:
        db_table = 'ktcdinfo'


class TKtcDokiz(Kbrdokiz, ExtSourceFields):
    class Meta:
        db_table = 'ktcdokiz'


class TKtcHead(Kbrhead, ExtSourceFields):
    class Meta:
        db_table = 'ktchead'


class TKtcPk(Kbrpk, ExtSourceFields):
    class Meta:
        db_table = 'ktcpk'


class TKtcPlbiz(Kbrplbiz, ExtSourceFields):
    class Meta:
        db_table = 'ktcplbiz'


class TKtcPltiz(Kbrpltiz, ExtSourceFields):
    class Meta:
        db_table = 'ktcpltiz'


class TKtcSumpp(Kbrsumpp, ExtSourceFields):
    class Meta:
        db_table = 'ktcsumpp'


class TKtcTerms(Kbrterms, ExtSourceFields):
    class Meta:
        db_table = 'ktcterms'


class TKtcTovg(Kbrtovg, ExtSourceFields):
    class Meta:
        db_table = 'ktctovg'


class TKtcToviz(Kbrtoviz, ExtSourceFields):
    class Meta:
        db_table = 'ktctoviz'


class TKtcTovs(Kbrtovs, ExtSourceFields):
    class Meta:
        db_table = 'ktctovs'


class TKtdAvtmb(Ktdavtmb, ExtSourceFields):
    class Meta:
        db_table = 'ktdavtmb'


class TKtdCont(Ktdcont, ExtSourceFields):
    class Meta:
        db_table = 'ktdcont'


class TKtdCrdts(Ktdcrdts, ExtSourceFields):
    class Meta:
        db_table = 'ktdcrdts'


class TKtdDinf2(Ktddinf2, ExtSourceFields):
    class Meta:
        db_table = 'ktddinf2'


class TKtdDinfo(Ktddinfo, ExtSourceFields):
    class Meta:
        db_table = 'ktddinfo'

class TKtdDog(Ktddog, ExtSourceFields):
    class Meta:
        db_table = 'ktddog'


class TKtdDoga(Ktddoga, ExtSourceFields):
    class Meta:
        db_table = 'ktddoga'


class TKtdDogt(Ktddogt, ExtSourceFields):
    class Meta:
        db_table = 'ktddogt'


class TKtdHead(Ktdhead, ExtSourceFields):
    class Meta:
        db_table = 'ktdhead'


class TKtdKmp(Ktdkmp, ExtSourceFields):
    class Meta:
        db_table = 'ktdkmp'


class TKtdKmpk(Ktdkmpk, ExtSourceFields):
    class Meta:
        db_table = 'ktdkmpk'


class TKtdPasp(Ktdpasp, ExtSourceFields):
    class Meta:
        db_table = 'ktdpasp'


class TKtdPk(Ktdpk, ExtSourceFields):
    class Meta:
        db_table = 'ktdpk'


class TKtdPlatr(Ktdplatr, ExtSourceFields):
    class Meta:
        db_table = 'ktdplatr'


class TKtdPlatv(Ktdplatv, ExtSourceFields):
    class Meta:
        db_table = 'ktdplatv'


class TKtdPredd(Ktdpredd, ExtSourceFields):
    class Meta:
        db_table = 'ktdpredd'


class TKtdSumpp(Ktdsumpp, ExtSourceFields):
    class Meta:
        db_table = 'ktdsumpp'


class TKtdTechd(Ktdtechd, ExtSourceFields):
    class Meta:
        db_table = 'ktdtechd'


class TKtdTerms(Ktdterms, ExtSourceFields):
    class Meta:
        db_table = 'ktdterms'


class TKtdTov2(Ktdtov2, ExtSourceFields):
    class Meta:
        db_table = 'ktdtov2'


class TKtdTovar(Ktdtovar, ExtSourceFields):
    class Meta:
        db_table = 'ktdtovar'


class TKtdTovg(Ktdtovg, ExtSourceFields):
    class Meta:
        db_table = 'ktdtovg'


class TKtdTovg2(Ktdtovg2, ExtSourceFields):
    class Meta:
        db_table = 'ktdtovg2'


class TKtdTovs(Ktdtovs, ExtSourceFields):
    class Meta:
        db_table = 'ktdtovs'


class TKtdTrans(Ktdtrans, ExtSourceFields):
    class Meta:
        db_table = 'ktdtrans'


class TKtdUslt(Ktduslt, ExtSourceFields):
    class Meta:
        db_table = 'ktduslt'
