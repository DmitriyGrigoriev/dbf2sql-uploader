# from django.db import models
from .base.models import (
    DclHead, AktsHead, AktsMess, AktsPath, CntOto,
    Cvc, Dclamnum, Dclavtmb, Dclcont, Dclcrdts,
    Dcldinf2, Dcldinfo, Dcldog, Dcldoga, Dcldogt,
    Dclkmp, Dclkmpk, Dclkmpk, Dcllistd, Dcllisth,
    Dcllistl, Dclpasp, Dclpk, Dclplat2, Dclplatr,
    Dclplatv, Dclpredd, Dclquerd, Dclquerh, Dclquern,
    Dclrinfo, Dclriska, Dclriskb, Dclriskc, Dclriskd,
    Dclriskm, Dclriskp, Dclrsinf, Dclrsk93, Dclrsmpr,
    Dclrsnfi, Dclslotm, Dclsltov, Dclsumpp, Dcltcim,
    Dcltechd, Dclterms, Dcltois, Dcltov2, Dcltovar,
    Dcltovg, Dcltovg2, Dcltovs, Dcltovs2, Dcltrans,
    Dclusl, Dcluslt, Dclvrsk, Dk1, Dk2, DkPp, Dkisch,
    Dkkupl, Dkoprp, Dkpeni, Dtcddtc, Dtcdinfo, Dtchead,
    Dtcslotm, Dtcsscv, Dtcsstc, Ktcavtmb, Ktcdinfo,
    Ktcdokiz, Ktchead, Ktcpk, Ktcplbiz, Ktcpltiz,
    Ktcslotm, Ktcsltov, Ktcsumpp, Ktcterms, Ktctovg,
    Ktctoviz, Ktctovs, Ktdamnum, Ktdavtmb, Ktdcont,
    Ktddinf2, Ktddinfo, Ktdhead, Ktdpasp, Ktdpk,
    Ktdplbiz, Ktdpltiz, Ktdpredd, Ktdslotm, Ktdsltov,
    Ktdsumpp, Ktdtcim, Ktdtechd, Ktdterms, Ktdtois,
    Ktdtov2, Ktdtovar, Ktdtovg, Ktdtovg2, Ktdtovs,
    Ktdtovs2, Ktdtrans, Ktduslt, Oupavtmb, Oupdinfo,
    Oupdokiz, Ouphead, Ouppk, Oupplbiz, Ouppltiz,
    Oupslotm, Oupsltov, Oupsumpp, Oupterms, Ouptovg,
    Ouptoviz, Ouptovs, Proterr, Protprim, PzkErr,
    PzkHead, PzkRsn,
)
from .mixins import ExtBase, ExtBaseG32, ExtBaseK32


class DclHead(ExtBase, DclHead):
    class Meta:
        managed = False
        db_table = 'dclhead'


class AktsHead(ExtBase, AktsHead):
    class Meta:
        managed = False
        db_table = 'aktshead'


class AktsMess(ExtBaseG32, AktsMess):
    class Meta:
        managed = False
        db_table = 'aktsmess'


class AktsPath(ExtBaseG32, AktsPath):
    class Meta:
        managed = False
        db_table = 'aktspath'


class CntOto(ExtBase, CntOto):
    class Meta:
        managed = False
        db_table = 'cnt_oto'


class Cvc(ExtBaseG32, Cvc):
    class Meta:
        managed = False
        db_table = 'cvc'


class Dclamnum(ExtBaseG32, Dclamnum):
    class Meta:
        managed = False
        db_table = 'dclamnum'


class Dclavtmb(ExtBaseG32, Dclavtmb):
    class Meta:
        managed = False
        db_table = 'dclavtmb'


class Dclcont(ExtBaseG32, Dclcont):
    class Meta:
        managed = False
        db_table = 'dclcont'


class Dclcrdts(ExtBaseG32, Dclcrdts):
    class Meta:
        managed = False
        db_table = 'dclcrdts'


class Dcldinf2(ExtBaseG32, Dcldinf2):
    class Meta:
        managed = False
        db_table = 'dcldinf2'


class Dcldinfo(ExtBaseG32, Dcldinfo):
    class Meta:
        managed = False
        db_table = 'dcldinfo'


class Dcldog(ExtBaseG32, Dcldog):
    class Meta:
        managed = False
        db_table = 'dcldog'


class Dcldoga(ExtBaseG32, Dcldoga):
    class Meta:
        managed = False
        db_table = 'dcldoga'


class Dcldogt(ExtBaseG32, Dcldogt):
    class Meta:
        managed = False
        db_table = 'dcldogt'


class Dclkmp(ExtBaseG32, Dclkmp):
    class Meta:
        managed = False
        db_table = 'dclkmp'


class Dclkmpk(ExtBaseG32, Dclkmpk):
    class Meta:
        managed = False
        db_table = 'dclkmpk'


class Dcllistd(ExtBase, Dcllistd):
    class Meta:
        managed = False
        db_table = 'dcllistd'


class Dcllisth(ExtBase, Dcllisth):
    class Meta:
        managed = False
        db_table = 'dcllisth'


class Dcllistl(ExtBase, Dcllistl):
    class Meta:
        managed = False
        db_table = 'dcllistl'


class Dclpasp(ExtBase, Dclpasp):
    class Meta:
        managed = False
        db_table = 'Dclpasp'


class Dclpk(ExtBaseG32, Dclpk):
    class Meta:
        managed = False
        db_table = 'Dclpk'


class Dclplat2(ExtBaseG32, Dclplat2):
    class Meta:
        managed = False
        db_table = 'Dclplat2'


class Dclplatr(ExtBaseG32, Dclplatr):
    class Meta:
        managed = False
        db_table = 'Dclplatr'


class Dclplatv(ExtBase, Dclplatv):
    class Meta:
        managed = False
        db_table = 'Dclplatv'


class Dclpredd(ExtBaseG32, Dclpredd):
    class Meta:
        managed = False
        db_table = 'Dclpredd'


class Dclquerd(ExtBase, Dclquerd):
    class Meta:
        managed = False
        db_table = 'Dclquerd'


class Dclquerh(ExtBase, Dclquerh):
    class Meta:
        managed = False
        db_table = 'Dclquerh'


class Dclquern(ExtBase, Dclquern):
    class Meta:
        managed = False
        db_table = 'Dclquern'


class Dclrinfo(ExtBaseG32, Dclrinfo):
    class Meta:
        managed = False
        db_table = 'Dclrinfo'


class Dclriska(ExtBaseG32, Dclriska):
    class Meta:
        managed = False
        db_table = 'Dclriska'


class Dclriskb(ExtBaseG32, Dclriskb):
    class Meta:
        managed = False
        db_table = 'Dclriskb'


class Dclriskc(ExtBaseG32, Dclriskc):
    class Meta:
        managed = False
        db_table = 'Dclriskc'


class Dclriskd(ExtBaseG32, Dclriskd):
    class Meta:
        managed = False
        db_table = 'Dclriskd'


class Dclriskm(ExtBaseG32, Dclriskm):
    class Meta:
        managed = False
        db_table = 'Dclriskm'


class Dclriskp(ExtBaseG32, Dclriskp):
    class Meta:
        managed = False
        db_table = 'Dclriskp'


class Dclrsinf(ExtBaseG32, Dclrsinf):
    class Meta:
        managed = False
        db_table = 'Dclrsinf'


class Dclrsk93(ExtBaseG32, Dclrsk93):
    class Meta:
        managed = False
        db_table = 'Dclrsk93'


class Dclrsmpr(ExtBaseG32, Dclrsmpr):
    class Meta:
        managed = False
        db_table = 'Dclrsmpr'


class Dclrsnfi(ExtBaseG32, Dclrsnfi):
    class Meta:
        managed = False
        db_table = 'Dclrsnfi'


class Dclslotm(ExtBase, Dclslotm):
    class Meta:
        managed = False
        db_table = 'Dclslotm'


class Dclsltov(ExtBase, Dclsltov):
    class Meta:
        managed = False
        db_table = 'Dclsltov'


class Dclsumpp(ExtBase, Dclsumpp):
    class Meta:
        managed = False
        db_table = 'Dclsumpp'


class Dcltcim(ExtBaseG32, Dcltcim):
    class Meta:
        managed = False
        db_table = 'Dcltcim'


class Dcltechd(ExtBaseG32, Dcltechd):
    class Meta:
        managed = False
        db_table = 'Dcltechd'


class Dclterms(ExtBaseG32, Dclterms):
    class Meta:
        managed = False
        db_table = 'Dclterms'


class Dcltois(ExtBaseG32, Dcltois):
    class Meta:
        managed = False
        db_table = 'Dcltois'


class Dcltov2(ExtBaseG32, Dcltov2):
    class Meta:
        managed = False
        db_table = 'Dcltov2'


class Dcltovar(ExtBaseG32, Dcltovar):
    class Meta:
        managed = False
        db_table = 'Dcltovar'


class Dcltovg(ExtBaseG32, Dcltovg):
    class Meta:
        managed = False
        db_table = 'Dcltovg'


class Dcltovg2(ExtBaseG32, Dcltovg2):
    class Meta:
        managed = False
        db_table = 'Dcltovg2'


class Dcltovs(ExtBaseG32, Dcltovs):
    class Meta:
        managed = False
        db_table = 'Dcltovs'


class Dcltovs2(ExtBaseG32, Dcltovs2):
    class Meta:
        managed = False
        db_table = 'Dcltovs2'


class Dcltrans(ExtBase, Dcltrans):
    class Meta:
        managed = False
        db_table = 'Dcltrans'


class Dclusl(ExtBase, Dclusl):
    class Meta:
        managed = False
        db_table = 'Dclusl'


class Dcluslt(ExtBaseG32, Dcluslt):
    class Meta:
        managed = False
        db_table = 'Dcluslt'


class Dclvrsk(ExtBaseG32, Dclvrsk):
    class Meta:
        managed = False
        db_table = 'Dclvrsk'


class Dk1(ExtBase, Dk1):
    class Meta:
        managed = False
        db_table = 'Dk1'


class Dk2(ExtBaseG32, Dk2):
    class Meta:
        managed = False
        db_table = 'Dk2'


class DkPp(ExtBase, DkPp):
    class Meta:
        managed = False
        db_table = 'Dk_pp'


class Dkisch(ExtBaseG32, Dkisch):
    class Meta:
        managed = False
        db_table = 'Dkisch'


class Dkkupl(ExtBase, Dkkupl):
    class Meta:
        managed = False
        db_table = 'Dkkupl'


class Dkoprp(ExtBase, Dkoprp):
    class Meta:
        managed = False
        db_table = 'Dkoprp'


class Dkpeni(ExtBase, Dkpeni):
    class Meta:
        managed = False
        db_table = 'Dkpeni'


class Dtcddtc(ExtBaseG32, Dtcddtc):
    class Meta:
        managed = False
        db_table = 'Dtcddtc'


class Dtcdinfo(ExtBaseG32, Dtcdinfo):
    class Meta:
        managed = False
        db_table = 'Dtcdinfo'


class Dtchead(ExtBase, Dtchead):
    class Meta:
        managed = False
        db_table = 'Dtchead'


class Dtcslotm(ExtBase, Dtcslotm):
    class Meta:
        managed = False
        db_table = 'Dtcslotm'


class Dtcsscv(ExtBaseG32, Dtcsscv):
    class Meta:
        managed = False
        db_table = 'Dtcsscv'


class Dtcsstc(ExtBaseG32, Dtcsstc):
    class Meta:
        managed = False
        db_table = 'Dtcsstc'


class Ktcavtmb(ExtBaseK32, Ktcavtmb):
    class Meta:
        managed = False
        db_table = 'Ktcavtmb'


class Ktcdinfo(ExtBaseK32, Ktcdinfo):
    class Meta:
        managed = False
        db_table = 'Ktcdinfo'


class Ktcdokiz(ExtBaseK32, Ktcdokiz):
    class Meta:
        managed = False
        db_table = 'Ktcdokiz'


class Ktchead(ExtBaseG32, Ktchead):
    class Meta:
        managed = False
        db_table = 'Ktchead'


class Ktcpk(ExtBaseK32, Ktcpk):
    class Meta:
        managed = False
        db_table = 'Ktcpk'


class Ktcplbiz(ExtBase, Ktcplbiz):
    class Meta:
        managed = False
        db_table = 'Ktcplbiz'


class Ktcpltiz(ExtBaseK32, Ktcpltiz):
    class Meta:
        managed = False
        db_table = 'Ktcpltiz'


class Ktcslotm(ExtBase, Ktcslotm):
    class Meta:
        managed = False
        db_table = 'Ktcslotm'


class Ktcsltov(ExtBaseK32, Ktcsltov):
    class Meta:
        managed = False
        db_table = 'Ktcsltov'


class Ktcsumpp(ExtBaseK32, Ktcsumpp):
    class Meta:
        managed = False
        db_table = 'Ktcsumpp'



class Ktcterms(ExtBaseK32, Ktcterms):
    class Meta:
        managed = False
        db_table = 'Ktcterms'


class Ktctovg(ExtBaseK32, Ktctovg):
    class Meta:
        managed = False
        db_table = 'Ktctovg'


class Ktctoviz(ExtBase, Ktctoviz):
    class Meta:
        managed = False
        db_table = 'Ktctoviz'

class Ktctovs(ExtBaseK32, Ktctovs):
    class Meta:
        managed = False
        db_table = 'Ktctovs'


class Ktdamnum(ExtBaseG32, Ktdamnum):
    class Meta:
        managed = False
        db_table = 'Ktdamnum'


class Ktdavtmb(ExtBaseG32, Ktdavtmb):
    class Meta:
        managed = False
        db_table = 'Ktdavtmb'


class Ktdcont(ExtBaseG32, Ktdcont):
    class Meta:
        managed = False
        db_table = 'Ktdcont'


class Ktddinf2(ExtBaseG32, Ktddinf2):
    class Meta:
        managed = False
        db_table = 'Ktddinf2'


class Ktddinfo(ExtBaseG32, Ktddinfo):
    class Meta:
        managed = False
        db_table = 'Ktddinfo'


class Ktdhead(ExtBase, Ktdhead):
    class Meta:
        managed = False
        db_table = 'Ktdhead'


class Ktdpasp(ExtBase, Ktdpasp):
    class Meta:
        managed = False
        db_table = 'Ktdpasp'


class Ktdpk(ExtBaseG32, Ktdpk):
    class Meta:
        managed = False
        db_table = 'Ktdpk'


class Ktdplbiz(ExtBase, Ktdplbiz):
    class Meta:
        managed = False
        db_table = 'Ktdplbiz'


class Ktdpltiz(ExtBaseK32, Ktdpltiz):
    class Meta:
        managed = False
        db_table = 'Ktdpltiz'


class Ktdpredd(ExtBaseG32, Ktdpredd):
    class Meta:
        managed = False
        db_table = 'Ktdpredd'


class Ktdslotm(ExtBase, Ktdslotm):
    class Meta:
        managed = False
        db_table = 'Ktdslotm'


class Ktdsltov(ExtBaseG32, Ktdsltov):
    class Meta:
        managed = False
        db_table = 'Ktdsltov'


class Ktdsumpp(ExtBase, Ktdsumpp):
    class Meta:
        managed = False
        db_table = 'Ktdsumpp'


class Ktdtcim(ExtBaseG32, Ktdtcim):
    class Meta:
        managed = False
        db_table = 'Ktdtcim'


class Ktdtechd(ExtBaseG32, Ktdtechd):
    class Meta:
        managed = False
        db_table = 'Ktdtechd'

class Ktdterms(ExtBaseG32, Ktdterms):
    class Meta:
        managed = False
        db_table = 'Ktdterms'


class Ktdtois(ExtBaseG32, Ktdtois):
    class Meta:
        managed = False
        db_table = 'Ktdtois'


class Ktdtov2(ExtBaseG32, Ktdtov2):
    class Meta:
        managed = False
        db_table = 'Ktdtov2'


class Ktdtovar(ExtBaseG32, Ktdtovar):
    class Meta:
        managed = False
        db_table = 'Ktdtovar'


class Ktdtovg(ExtBaseG32, Ktdtovg):
    class Meta:
        managed = False
        db_table = 'Ktdtovg'


class Ktdtovg2(ExtBaseG32, Ktdtovg2):
    class Meta:
        managed = False
        db_table = 'Ktdtovg2'


class Ktdtovs(ExtBaseG32, Ktdtovs):
    class Meta:
        managed = False
        db_table = 'Ktdtovs'


class Ktdtovs2(ExtBaseG32, Ktdtovs2):
    class Meta:
        managed = False
        db_table = 'Ktdtovs2'


class Ktdtrans(ExtBaseG32, Ktdtrans):
    class Meta:
        managed = False
        db_table = 'Ktdtrans'


class Ktduslt(ExtBaseG32, Ktduslt):
    class Meta:
        managed = False
        db_table = 'Ktduslt'


class Oupavtmb(ExtBaseK32, Oupavtmb):
    class Meta:
        managed = False
        db_table = 'Oupavtmb'


class Oupdinfo(ExtBaseK32, Oupdinfo):
    class Meta:
        managed = False
        db_table = 'Oupdinfo'


class Oupdokiz(ExtBaseK32, Oupdokiz):
    class Meta:
        managed = False
        db_table = 'Oupdokiz'


class Ouphead(ExtBaseK32, Ouphead):
    class Meta:
        managed = False
        db_table = 'Ouphead'


class Ouppk(ExtBaseK32, Ouppk):
    class Meta:
        managed = False
        db_table = 'Ouppk'


class Oupplbiz(ExtBase, Oupplbiz):
    class Meta:
        managed = False
        db_table = 'Oupplbiz'


class Ouppltiz(ExtBase, Ouppltiz):
    class Meta:
        managed = False
        db_table = 'Ouppltiz'


class Oupslotm(ExtBase, Oupslotm):
    class Meta:
        managed = False
        db_table = 'Oupslotm'


class Oupsltov(ExtBaseK32, Oupsltov):
    class Meta:
        managed = False
        db_table = 'Oupsltov'


class Oupsumpp(ExtBaseK32, Oupsumpp):
    class Meta:
        managed = False
        db_table = 'Oupsumpp'


class Oupterms(ExtBaseK32, Oupterms):
    class Meta:
        managed = False
        db_table = 'Oupterms'


class Ouptovg(ExtBaseK32, Ouptovg):
    class Meta:
        managed = False
        db_table = 'Ouptovg'


class Ouptoviz(ExtBase, Ouptoviz):
    class Meta:
        managed = False
        db_table = 'Ouptoviz'


class Ouptovs(ExtBaseK32, Ouptovs):
    class Meta:
        managed = False
        db_table = 'Ouptovs'


class Proterr(ExtBase, Proterr):
    class Meta:
        managed = False
        db_table = 'Proterr'


class Protprim(ExtBase, Protprim):
    class Meta:
        managed = False
        db_table = 'Protprim'


class PzkErr(ExtBase, PzkErr):
    class Meta:
        managed = False
        db_table = 'Pzk_err'

class PzkHead(ExtBase, PzkHead):
    class Meta:
        managed = False
        db_table = 'Pzk_head'


class PzkRsn(ExtBase, PzkRsn):
    class Meta:
        managed = False
        db_table = 'Pzk_rsn'
