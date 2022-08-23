from .base.models import (
    Avtomove, Dbramnum, Dbravtmb, Dbrcont, Dbrcrdts,
    Dbrdinf2, Dbrdinfo, Dbrdog, Dbrdoga, Dbrdogt,
    Dbrdop48, Dbrhead, Dbrkmp, Dbrkmpk, Dbrpasp,
    Dbrpk, Dbrplatr, Dbrplatv, Dbrpredd, Dbrsumpp,
    Dbrtechd, Dbrterms, Dbrtov2, Dbrtovar, Dbrtovg,
    Dbrtovg2, Dbrtovs, Dbrtovs2, Dbrtrans, Dbruslt,
    Dcllistd, Dcllisth, Dcllistl, Dclquerd, Dclquerh,
    Docsfiles, Kbravtmb, Kbrdinfo, Kbrdokiz, Kbrhead,
    Kbrpk, Kbrplbiz, Kbrpltiz, Kbrsumpp, Kbrterms,
    Kbrtovg, Kbrtoviz, Kbrtovs, Ktdamnum, Ktdavtmb,
    Ktdcont, Ktdcrdts, Ktddinf2, Ktddinfo, Ktddog,
    Ktddoga, Ktddogt, Ktdhead, Ktdkmp, Ktdkmpk,
    Ktdpasp, Ktdpk, Ktdplatr, Ktdplatv, Ktdpredd,
    Ktdsumpp, Ktdtechd, Ktdterms, Ktdtov2, Ktdtovar,
    Ktdtovg, Ktdtovg2, Ktdtovs, Ktdtrans, Ktduslt,
    Psm, RegTi, Sbrddtc, Sbrdinfo, Sbrhead, Sbrsscv,
    Sbrsstc, Version
)
from src.apps.common.mixins import ExtBaseDocNum

class Avtomove(ExtBaseDocNum, Avtomove):
    class Meta:
        managed = False
        db_table = 'avtomove'


class Dbramnum(ExtBaseDocNum, Dbramnum):
    class Meta:
        managed = False
        db_table = 'dbramnum'


class Dbravtmb(ExtBaseDocNum, Dbravtmb):
    class Meta:
        managed = False
        db_table = 'dbravtmb'


class Dbrcont(ExtBaseDocNum, Dbrcont):
    class Meta:
        managed = False
        db_table = 'dbrcont'


class Dbrcrdts(ExtBaseDocNum, Dbrcrdts):
    class Meta:
        managed = False
        db_table = 'dbrcrdts'


class Dbrdinf2(ExtBaseDocNum, Dbrdinf2):
    class Meta:
        managed = False
        db_table = 'dbrdinf2'


class Dbrdinfo(ExtBaseDocNum, Dbrdinfo):
    class Meta:
        managed = False
        db_table = 'dbrdinfo'


class Dbrdog(ExtBaseDocNum, Dbrdog):
    class Meta:
        managed = False
        db_table = 'dbrdog'


class Dbrdoga(ExtBaseDocNum, Dbrdoga):
    class Meta:
        managed = False
        db_table = 'dbrdoga'


class Dbrdogt(ExtBaseDocNum, Dbrdogt):
    class Meta:
        managed = False
        db_table = 'dbrdogt'


class Dbrdop48(ExtBaseDocNum, Dbrdop48):
    class Meta:
        managed = False
        db_table = 'dbrdop48'


class Dbrhead(ExtBaseDocNum, Dbrhead):
    class Meta:
        managed = False
        db_table = 'dbrhead'


class Dbrkmp(ExtBaseDocNum, Dbrkmp):
    class Meta:
        managed = False
        db_table = 'dbrkmp'


class Dbrkmpk(ExtBaseDocNum, Dbrkmpk):
    class Meta:
        managed = False
        db_table = 'dbrkmpk'


class Dbrpasp(ExtBaseDocNum, Dbrpasp):
    class Meta:
        managed = False
        db_table = 'dbrpasp'


class Dbrpk(ExtBaseDocNum, Dbrpk):
    class Meta:
        managed = False
        db_table = 'dbrpk'


class Dbrplatr(ExtBaseDocNum, Dbrplatr):
    class Meta:
        managed = False
        db_table = 'dbrplatr'


class Dbrplatv(ExtBaseDocNum, Dbrplatv):
    class Meta:
        managed = False
        db_table = 'dbrplatv'


class Dbrpredd(ExtBaseDocNum, Dbrpredd):
    class Meta:
        managed = False
        db_table = 'dbrpredd'


class Dbrsumpp(ExtBaseDocNum, Dbrsumpp):
    class Meta:
        managed = False
        db_table = 'Dbrsumpp'


class Dbrtechd(ExtBaseDocNum, Dbrtechd):
    class Meta:
        managed = False
        db_table = 'dbrtechd'


class Dbrterms(ExtBaseDocNum, Dbrterms):
    class Meta:
        managed = False
        db_table = 'dbrterms'


class Dbrtov2(ExtBaseDocNum, Dbrtov2):
    class Meta:
        managed = False
        db_table = 'dbrtov2'


class Dbrtovar(ExtBaseDocNum, Dbrtovar):
    class Meta:
        managed = False
        db_table = 'dbrtovar'


class Dbrtovg(ExtBaseDocNum, Dbrtovg):
    class Meta:
        managed = False
        db_table = 'dbrtovg'


class Dbrtovg2(ExtBaseDocNum, Dbrtovg2):
    class Meta:
        managed = False
        db_table = 'dbrtovg2'


class Dbrtovs(ExtBaseDocNum, Dbrtovs):
    class Meta:
        managed = False
        db_table = 'dbrtovs'


class Dbrtovs2(ExtBaseDocNum, Dbrtovs2):
    class Meta:
        managed = False
        db_table = 'dbrtovs2'


class Dbrtrans(ExtBaseDocNum, Dbrtrans):
    class Meta:
        managed = False
        db_table = 'dbrtrans'


class Dbruslt(ExtBaseDocNum, Dbruslt):
    class Meta:
        managed = False
        db_table = 'dbruslt'


class Dcllistd(ExtBaseDocNum, Dcllistd):
    class Meta:
        managed = False
        db_table = 'dcllistd'


class Dcllisth(ExtBaseDocNum, Dcllisth):
    class Meta:
        managed = False
        db_table = 'dcllisth'


class Dcllistl(ExtBaseDocNum, Dcllistl):
    class Meta:
        managed = False
        db_table = 'dcllistl'


class Dclquerd(ExtBaseDocNum, Dclquerd):
    class Meta:
        managed = False
        db_table = 'dclquerd'


class Dclquerh(ExtBaseDocNum, Dclquerh):
    class Meta:
        managed = False
        db_table = 'dclquerh'


class Docsfiles(Docsfiles):
    class Meta:
        managed = False
        db_table = 'docsfiles'


class Kbravtmb(ExtBaseDocNum, Kbravtmb):
    class Meta:
        managed = False
        db_table = 'kbravtmb'


class Kbrdinfo(ExtBaseDocNum, Kbrdinfo):
    class Meta:
        managed = False
        db_table = 'kbrdinfo'


class Kbrdokiz(ExtBaseDocNum, Kbrdokiz):
    class Meta:
        managed = False
        db_table = 'kbrdokiz'


class Kbrhead(ExtBaseDocNum, Kbrhead):
    class Meta:
        managed = False
        db_table = 'kbrhead'


class Kbrpk(ExtBaseDocNum, Kbrpk):
    class Meta:
        managed = False
        db_table = 'kbrpk'


class Kbrplbiz(ExtBaseDocNum, Kbrplbiz):
    class Meta:
        managed = False
        db_table = 'kbrplbiz'


class Kbrpltiz(ExtBaseDocNum, Kbrpltiz):
    class Meta:
        managed = False
        db_table = 'kbrpltiz'


class Kbrsumpp(ExtBaseDocNum, Kbrsumpp):
    class Meta:
        managed = False
        db_table = 'kbrsumpp'


class Kbrterms(ExtBaseDocNum, Kbrterms):
    class Meta:
        managed = False
        db_table = 'kbrterms'


class Kbrtovg(ExtBaseDocNum, Kbrtovg):
    class Meta:
        managed = False
        db_table = 'kbrtovg'


class Kbrtoviz(ExtBaseDocNum, Kbrtoviz):
    class Meta:
        managed = False
        db_table = 'kbrtoviz'


class Kbrtovs(ExtBaseDocNum, Kbrtovs):
    class Meta:
        managed = False
        db_table = 'kbrtovs'


class Ktdamnum(ExtBaseDocNum, Ktdamnum):
    class Meta:
        managed = False
        db_table = 'ktdamnum'


class Ktdavtmb(ExtBaseDocNum, Ktdavtmb):
    class Meta:
        managed = False
        db_table = 'ktdavtmb'


class Ktdcont(ExtBaseDocNum, Ktdcont):
    class Meta:
        managed = False
        db_table = 'ktdcont'


class Ktdcrdts(ExtBaseDocNum, Ktdcrdts):
    class Meta:
        managed = False
        db_table = 'ktdcrdts'


class Ktddinf2(ExtBaseDocNum, Ktddinf2):
    class Meta:
        managed = False
        db_table = 'ktddinf2'


class Ktddinfo(ExtBaseDocNum, Ktddinfo):
    class Meta:
        managed = False
        db_table = 'ktddinfo'


class Ktddog(ExtBaseDocNum, Ktddog):
    class Meta:
        managed = False
        db_table = 'ktddog'


class Ktddoga(ExtBaseDocNum, Ktddoga):
    class Meta:
        managed = False
        db_table = 'ktddoga'


class Ktddogt(ExtBaseDocNum, Ktddogt):
    class Meta:
        managed = False
        db_table = 'ktddogt'


class Ktdhead(ExtBaseDocNum, Ktdhead):
    class Meta:
        managed = False
        db_table = 'ktdhead'


class Ktdkmp(ExtBaseDocNum, Ktdkmp):
    class Meta:
        managed = False
        db_table = 'ktdkmp'


class Ktdkmpk(ExtBaseDocNum, Ktdkmpk):
    class Meta:
        managed = False
        db_table = 'ktdkmpk'


class Ktdpasp(ExtBaseDocNum, Ktdpasp):
    class Meta:
        managed = False
        db_table = 'ktdpasp'


class Ktdpk(ExtBaseDocNum, Ktdpk):
    class Meta:
        managed = False
        db_table = 'ktdpk'


class Ktdplatr(ExtBaseDocNum, Ktdplatr):
    class Meta:
        managed = False
        db_table = 'ktdplatr'


class Ktdplatv(ExtBaseDocNum, Ktdplatv):
    class Meta:
        managed = False
        db_table = 'Ktdplatv'


class Ktdpredd(ExtBaseDocNum, Ktdpredd):
    class Meta:
        managed = False
        db_table = 'ktdpredd'


class Ktdsumpp(ExtBaseDocNum, Ktdsumpp):
    class Meta:
        managed = False
        db_table = 'ktdsumpp'


class Ktdtechd(ExtBaseDocNum, Ktdtechd):
    class Meta:
        managed = False
        db_table = 'ktdtechd'


class Ktdterms(ExtBaseDocNum, Ktdterms):
    class Meta:
        managed = False
        db_table = 'Ktdterms'


class Ktdtov2(ExtBaseDocNum, Ktdtov2):
    class Meta:
        managed = False
        db_table = 'ktdtov2'


class Ktdtovar(ExtBaseDocNum, Ktdtovar):
    class Meta:
        managed = False
        db_table = 'ktdtovar'


class Ktdtovg(ExtBaseDocNum, Ktdtovg):
    class Meta:
        managed = False
        db_table = 'ktdtovg'


class Ktdtovg2(ExtBaseDocNum, Ktdtovg2):
    class Meta:
        managed = False
        db_table = 'ktdtovg2'


class Ktdtovs(ExtBaseDocNum, Ktdtovs):
    class Meta:
        managed = False
        db_table = 'ktdtovs'


class Ktdtrans(ExtBaseDocNum, Ktdtrans):
    class Meta:
        managed = False
        db_table = 'Ktdtrans'


class Ktduslt(ExtBaseDocNum, Ktduslt):
    class Meta:
        managed = False
        db_table = 'Ktduslt'


class Psm(ExtBaseDocNum, Psm):
    class Meta:
        managed = False
        db_table = 'psm'


class RegTi(ExtBaseDocNum, RegTi):
    class Meta:
        managed = False
        db_table = 'regti'


class Sbrddtc(ExtBaseDocNum, Sbrddtc):
    class Meta:
        managed = False
        db_table = 'sbrddtc'


class Sbrdinfo(ExtBaseDocNum, Sbrdinfo):
    class Meta:
        managed = False
        db_table = 'sbrdinfo'


class Sbrhead(ExtBaseDocNum, Sbrhead):
    class Meta:
        managed = False
        db_table = 'sbrhead'


class Sbrsscv(ExtBaseDocNum, Sbrsscv):
    class Meta:
        managed = False
        db_table = 'sbrsscv'


class Sbrsstc(ExtBaseDocNum, Sbrsstc):
    class Meta:
        managed = False
        db_table = 'sbrsstc'


class Version(Version):
    class Meta:
        managed = False
        db_table = 'version'
