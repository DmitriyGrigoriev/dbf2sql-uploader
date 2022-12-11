#from django.utils.translation import gettext_lazy as _
#####################################################################################
# add models from DBF
#####################################################################################
from src.apps.dbfexport.base.models import (
    DclHead, AktsHead, AktsMess, AktsPath, CntOto,
    Cvc, Dclamnum, Dclavtmb, Dclcont, Dclcrdts,
    Dcldinf2, Dcldinfo, Dcldog, Dcldoga, Dcldogt,
    Dclkmp, Dclkmpk, Dcllistd, Dcllisth, Dcllistl,
    Dclpasp, Dclpk, Dclplat2, Dclplatr, Dclplatv,
    Dclpredd, Dclquerd, Dclquerh, Dclquern, Dclrinfo,
    Dclriska, Dclriskb, Dclriskc, Dclriskd, Dclriskm,
    Dclriskp, Dclrsinf, Dclrsk93, Dclrsmpr, Dclrsnfi,
    Dclslotm, Dclsltov, Dclsumpp, Dcltcim, Dcltechd,
    Dclterms, Dcltois, Dcltov2, Dcltovar, Dcltovg,
    Dcltovg2, Dcltovs, Dcltovs2, Dcltrans, Dclusl,
    Dcluslt, Dclvrsk, Dk1, Dk2, DkPp, Dkisch, Dkkupl,
    Dkoprp, Dkpeni, Dtcddtc, Dtcdinfo, Dtchead,
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
    Oupslotm, Oupslotm, Oupsltov, Oupsumpp, Oupterms,
    Ouptovg, Ouptoviz, Ouptovs, Proterr, Protprim,
    PzkErr, PzkHead, PzkRsn
)
#####################################################################################
# add models from ARM Doc2SQL
#####################################################################################
from src.apps.armexport.base.models import (
    Dbrdop48, Ktdcrdts, Ktddog, Ktddoga, Ktddogt,
    Ktdkmp, Ktdkmpk, Ktdplatr, Ktdplatv,
)
from src.apps.common.mixins import ExtSourceFields, ExtSourceNoHashUniqueIndex


#####################################################################################
# Models: import from DBF
#####################################################################################
class TDclHead(DclHead, ExtSourceFields):
    class Meta:
        db_table = 'tdclhead'


class TAktsHead(AktsHead, ExtSourceFields):
    class Meta:
        db_table = 'taktshead'


class TAktsMess(AktsMess, ExtSourceFields):
    class Meta:
        db_table = 'taktsmess'


class TAktsPath(AktsPath, ExtSourceFields):
    class Meta:
        db_table = 'taktspath'


class TCntOto(CntOto, ExtSourceFields):
    class Meta:
        db_table = 'tcnt_oto'


class TCvc(Cvc, ExtSourceFields):
    class Meta:
        db_table = 'tcvc'


class TDclamnum(Dclamnum, ExtSourceFields):
    class Meta:
        db_table = 'tdclamnum'


class TDclavtmb(Dclavtmb, ExtSourceFields):
    class Meta:
        db_table = 'tdclavtmb'


class TDclcont(Dclcont, ExtSourceFields):
    class Meta:
        db_table = 'tdclcont'


class TDclcrdts(Dclcrdts, ExtSourceFields):
    class Meta:
        db_table = 'tdclcrdts'


class TDcldinf2(Dcldinf2, ExtSourceFields):
    class Meta:
        db_table = 'tdcldinf2'


class TDcldinfo(Dcldinfo, ExtSourceNoHashUniqueIndex):
    class Meta:
        db_table = 'tdcldinfo'


class TDcldog(Dcldog, ExtSourceFields):
    class Meta:
        db_table = 'tdcldog'


class TDcldoga(Dcldoga, ExtSourceFields):
    class Meta:
        db_table = 'tdcldoga'


class TDcldogt(Dcldogt, ExtSourceFields):
    class Meta:
        db_table = 'tdcldogt'


class TDclkmp(Dclkmp, ExtSourceFields):
    class Meta:
        db_table = 'tdclkmp'


class TDclkmpk(Dclkmpk, ExtSourceFields):
    class Meta:
        db_table = 'tdclkmpk'


class TDcllistd(Dcllistd, ExtSourceFields):
    class Meta:
        db_table = 'tdcllistd'


class TDcllisth(Dcllisth, ExtSourceFields):
    class Meta:
        db_table = 'tdcllisth'


class TDcllistl(Dcllistl, ExtSourceFields):
    class Meta:
        db_table = 'tdcllistl'


class TDclpasp(Dclpasp, ExtSourceFields):
    class Meta:
        db_table = 'tdclpasp'


class TDclpk(Dclpk, ExtSourceNoHashUniqueIndex):
    class Meta:
        db_table = 'tdclpk'


class TDclplat2(Dclplat2, ExtSourceFields):
    class Meta:
        db_table = 'tdclplat2'


class TDclplatr(Dclplatr, ExtSourceFields):
    class Meta:
        db_table = 'tdclplatr'


class TDclplatv(Dclplatv, ExtSourceFields):
    class Meta:
        db_table = 'tdclplatv'


class TDclpredd(Dclpredd, ExtSourceFields):
    class Meta:
        db_table = 'tdclpredd'


class TDclquerd(Dclquerd, ExtSourceFields):
    class Meta:
        db_table = 'tdclquerd'


class TDclquerh(Dclquerh, ExtSourceFields):
    class Meta:
        db_table = 'tdclquerh'


class TDclquern(Dclquern, ExtSourceFields):
    class Meta:
        db_table = 'tdclquern'


class TDclrinfo(Dclrinfo, ExtSourceFields):
    class Meta:
        db_table = 'tdclrinfo'


class TDclriska(Dclriska, ExtSourceFields):
    class Meta:
        db_table = 'tdclriska'


class TDclriskb(Dclriskb, ExtSourceFields):
    class Meta:
        db_table = 'tdclriskb'


class TDclriskc(Dclriskc, ExtSourceFields):
    class Meta:
        db_table = 'tdclriskc'


class TDclriskd(Dclriskd, ExtSourceFields):
    class Meta:
        db_table = 'tdclriskd'


class TDclriskm(Dclriskm, ExtSourceFields):
    class Meta:
        db_table = 'tdclriskm'


class TDclriskp(Dclriskp, ExtSourceFields):
    class Meta:
        db_table = 'tdclriskp'


class TDclrsinf(Dclrsinf, ExtSourceFields):
    class Meta:
        db_table = 'tdclrsinf'


class TDclrsk93(Dclrsk93, ExtSourceFields):
    class Meta:
        db_table = 'tdclrsk93'


class TDclrsmpr(Dclrsmpr, ExtSourceFields):
    class Meta:
        db_table = 'tdclrsmpr'


class TDclrsnfi(Dclrsnfi, ExtSourceFields):
    class Meta:
        db_table = 'tdclrsnfi'


class TDclslotm(Dclslotm, ExtSourceFields):
    class Meta:
        db_table = 'tdclslotm'


class TDclsltov(Dclsltov, ExtSourceFields):
    class Meta:
        db_table = 'tdclsltov'


class TDclsumpp(Dclsumpp, ExtSourceFields):
    class Meta:
        db_table = 'tdclsumpp'


class TDcltcim(Dcltcim, ExtSourceFields):
    class Meta:
        db_table = 'tdcltcim'


class TDcltechd(Dcltechd, ExtSourceNoHashUniqueIndex):
    class Meta:
        db_table = 'tdcltechd'


class TDclterms(Dclterms, ExtSourceFields):
    class Meta:
        db_table = 'tdclterms'


class TDcltois(Dcltois, ExtSourceFields):
    class Meta:
        db_table = 'tdcltois'


class TDcltov2(Dcltov2, ExtSourceFields):
    class Meta:
        db_table = 'tdcltov2'


class TDcltovar(Dcltovar, ExtSourceFields):
    class Meta:
        db_table = 'tdcltovar'


class TDcltovg(Dcltovg, ExtSourceFields):
    class Meta:
        db_table = 'tdcltovg'


class TDcltovg2(Dcltovg2, ExtSourceFields):
    class Meta:
        db_table = 'tdcltovg2'


class TDcltovs(Dcltovs, ExtSourceFields):
    class Meta:
        db_table = 'tdcltovs'


class TDcltovs2(Dcltovs2, ExtSourceFields):
    class Meta:
        db_table = 'tdcltovs2'


class TDcltrans(Dcltrans, ExtSourceFields):
    class Meta:
        db_table = 'tdcltrans'


class TDclusl(Dclusl, ExtSourceFields):
    class Meta:
        db_table = 'tdclusl'


class TDcluslt(Dcluslt, ExtSourceFields):
    class Meta:
        db_table = 'tdcluslt'


class TDclvrsk(Dclvrsk, ExtSourceFields):
    class Meta:
        db_table = 'tdclvrsk'


class TDk1(Dk1, ExtSourceFields):
    class Meta:
        db_table = 'tdk1'


class TDk2(Dk2, ExtSourceFields):
    class Meta:
        db_table = 'tdk2'


class TDkPp(DkPp, ExtSourceFields):
    class Meta:
        db_table = 'tdk_pp'


class TDkisch(Dkisch, ExtSourceFields):
    class Meta:
        db_table = 'tdkisch'


class TDkkupl(Dkkupl, ExtSourceFields):
    class Meta:
        db_table = 'tdkkupl'


class TDkoprp(Dkoprp, ExtSourceFields):
    class Meta:
        db_table = 'tdkoprp'


class TDkpeni(Dkpeni, ExtSourceFields):
    class Meta:
        db_table = 'tdkpeni'


class TDtcddtc(Dtcddtc, ExtSourceFields):
    class Meta:
        db_table = 'tdtcddtc'


class TDtcdinfo(Dtcdinfo, ExtSourceFields):
    class Meta:
        db_table = 'tdtcdinfo'


class TDtchead(Dtchead, ExtSourceFields):
    class Meta:
        db_table = 'tdtchead'


class TDtcslotm(Dtcslotm, ExtSourceFields):
    class Meta:
        db_table = 'tdtcslotm'


class TDtcsscv(Dtcsscv, ExtSourceFields):
    class Meta:
        db_table = 'tdtcsscv'


class TDtcsstc(Dtcsstc, ExtSourceFields):
    class Meta:
        db_table = 'tdtcsstc'


class TKtcavtmb(Ktcavtmb, ExtSourceFields):
    class Meta:
        db_table = 'tktcavtmb'


class TKtcdinfo(Ktcdinfo, ExtSourceFields):
    class Meta:
        db_table = 'tktcdinfo'


class TKtcdokiz(Ktcdokiz, ExtSourceFields):
    class Meta:
        db_table = 'tktcdokiz'


class TKtchead(Ktchead, ExtSourceFields):
    class Meta:
        db_table = 'tktchead'


class TKtcpk(Ktcpk, ExtSourceFields):
    class Meta:
        db_table = 'tktcpk'


class TKtcplbiz(Ktcplbiz, ExtSourceFields):
    class Meta:
        db_table = 'tktcplbiz'


class TKtcpltiz(Ktcpltiz, ExtSourceFields):
    class Meta:
        db_table = 'tktcpltiz'


class TKtcslotm(Ktcslotm, ExtSourceFields):
    class Meta:
        db_table = 'tktcslotm'


class TKtcsltov(Ktcsltov, ExtSourceFields):
    class Meta:
        db_table = 'tktcsltov'


class TKtcsumpp(Ktcsumpp, ExtSourceFields):
    class Meta:
        db_table = 'tktcsumpp'


class TKtcterms(Ktcterms, ExtSourceFields):
    class Meta:
        db_table = 'tktcterms'


class TKtctovg(Ktctovg, ExtSourceFields):
    class Meta:
        db_table = 'tktctovg'


class TKtctoviz(Ktctoviz, ExtSourceFields):
    class Meta:
        db_table = 'tktctoviz'


class TKtctovs(Ktctovs, ExtSourceFields):
    class Meta:
        db_table = 'tktctovs'


class TKtdamnum(Ktdamnum, ExtSourceFields):
    class Meta:
        db_table = 'tktdamnum'


class TKtdavtmb(Ktdavtmb, ExtSourceFields):
    class Meta:
        db_table = 'tktdavtmb'


class TKtdcont(Ktdcont, ExtSourceFields):
    class Meta:
        db_table = 'tktdcont'


class TKtddinf2(Ktddinf2, ExtSourceFields):
    class Meta:
        db_table = 'tktddinf2'


class TKtddinfo(Ktddinfo, ExtSourceFields):
    class Meta:
        db_table = 'tktddinfo'


class TKtdhead(Ktdhead, ExtSourceFields):
    class Meta:
        db_table = 'tktdhead'


class TKtdpasp(Ktdpasp, ExtSourceFields):
    class Meta:
        db_table = 'tktdpasp'


class TKtdpk(Ktdpk, ExtSourceFields):
    class Meta:
        db_table = 'tktdpk'


class TKtdplbiz(Ktdplbiz, ExtSourceFields):
    class Meta:
        db_table = 'tktdplbiz'


class TKtdpltiz(Ktdpltiz, ExtSourceFields):
    class Meta:
        db_table = 'tktdpltiz'


class TKtdpredd(Ktdpredd, ExtSourceFields):
    class Meta:
        db_table = 'tktdpredd'


class TKtdslotm(Ktdslotm, ExtSourceFields):
    class Meta:
        db_table = 'tktdslotm'


class TKtdsltov(Ktdsltov, ExtSourceFields):
    class Meta:
        db_table = 'tktdsltov'


class TKtdsumpp(Ktdsumpp, ExtSourceFields):
    class Meta:
        db_table = 'tktdsumpp'


class TKtdtcim(Ktdtcim, ExtSourceFields):
    class Meta:
        db_table = 'tktdtcim'


class TKtdtechd(Ktdtechd, ExtSourceFields):
    class Meta:
        db_table = 'tktdtechd'


class TKtdterms(Ktdterms, ExtSourceFields):
    class Meta:
        db_table = 'tktdterms'


class TKtdtois(Ktdtois, ExtSourceFields):
    class Meta:
        db_table = 'tktdtois'


class TKtdtov2(Ktdtov2, ExtSourceFields):
    class Meta:
        db_table = 'tktdtov2'


class TKtdtovar(Ktdtovar, ExtSourceFields):
    class Meta:
        db_table = 'tktdtovar'


class TKtdtovg(Ktdtovg, ExtSourceFields):
    class Meta:
        db_table = 'tktdtovg'


class TKtdtovg2(Ktdtovg2, ExtSourceFields):
    class Meta:
        db_table = 'tktdtovg2'


class TKtdtovs(Ktdtovs, ExtSourceFields):
    class Meta:
        db_table = 'tktdtovs'


class TKtdtovs2(Ktdtovs2, ExtSourceFields):
    class Meta:
        db_table = 'tktdtovs2'


class TKtdtrans(Ktdtrans, ExtSourceFields):
    class Meta:
        db_table = 'tktdtrans'


class TKtduslt(Ktduslt, ExtSourceFields):
    class Meta:
        db_table = 'tktduslt'


class TOupavtmb(Oupavtmb, ExtSourceFields):
    class Meta:
        db_table = 'toupavtmb'


class TOupdinfo(Oupdinfo, ExtSourceFields):
    class Meta:
        db_table = 'toupdinfo'


class TOupdokiz(Oupdokiz, ExtSourceFields):
    class Meta:
        db_table = 'toupdokiz'


class TOuphead(Ouphead, ExtSourceFields):
    class Meta:
        db_table = 'touphead'


class TOuppk(Ouppk, ExtSourceFields):
    class Meta:
        db_table = 'touppk'


class TOupplbiz(Oupplbiz, ExtSourceFields):
    class Meta:
        db_table = 'toupplbiz'


class TOuppltiz(Ouppltiz, ExtSourceFields):
    class Meta:
        db_table = 'touppltiz'


class TOupslotm(Oupslotm, ExtSourceFields):
    class Meta:
        db_table = 'toupslotm'


class TOupsltov(Oupsltov, ExtSourceFields):
    class Meta:
        db_table = 'toupsltov'


class TOupsumpp(Oupsumpp, ExtSourceFields):
    class Meta:
        db_table = 'toupsumpp'


class TOupterms(Oupterms, ExtSourceFields):
    class Meta:
        db_table = 'toupterms'


class TOuptovg(Ouptovg, ExtSourceFields):
    class Meta:
        db_table = 'touptovg'


class TOuptoviz(Ouptoviz, ExtSourceFields):
    class Meta:
        db_table = 'touptoviz'


class TOuptovs(Ouptovs, ExtSourceFields):
    class Meta:
        db_table = 'touptovs'


class TProterr(Proterr, ExtSourceFields):
    class Meta:
        db_table = 'tproterr'


class TProtprim(Protprim, ExtSourceFields):
    class Meta:
        db_table = 'tprotprim'


class TPzkErr(PzkErr, ExtSourceFields):
    class Meta:
        db_table = 'tpzk_err'


class TPzkHead(PzkHead, ExtSourceFields):
    class Meta:
        db_table = 'tpzk_head'


class TPzkRsn(PzkRsn, ExtSourceFields):
    class Meta:
        db_table = 'tpzk_rsn'

#####################################################################################
# Models: import from Doc2SQL
#####################################################################################
class TDclDop48(Dbrdop48, ExtSourceFields):
    class Meta:
        db_table = 'tdcldop48'


class TKtdCrdts(Ktdcrdts, ExtSourceFields):
    class Meta:
        db_table = 'tktdcrdts'


class TKtdDog(Ktddog, ExtSourceFields):
    class Meta:
        db_table = 'tktddog'


class TKtdDoga(Ktddoga, ExtSourceFields):
    class Meta:
        db_table = 'tktddoga'


class TKtdDogt(Ktddogt, ExtSourceFields):
    class Meta:
        db_table = 'tktddogt'


class TKtdKmp(Ktdkmp, ExtSourceFields):
    class Meta:
        db_table = 'tktdkmp'


class TKtdKmpk(Ktdkmpk, ExtSourceFields):
    class Meta:
        db_table = 'tktdkmpk'


class TKtdPlatr(Ktdplatr, ExtSourceFields):
    class Meta:
        db_table = 'tktdplatr'


class TKtdPlatv(Ktdplatv, ExtSourceFields):
    class Meta:
        db_table = 'tktdplatv'



# Create your models here.
# class TDbf(models.Model):
#     int = models.IntegerField(blank=True, null=True)
#     char = models.CharField(max_length=10, blank=True, null=True)
#     charbin = models.CharField(max_length=10, blank=True, null=True)
#     currency = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
#     date = models.DateField(blank=True, null=True)
#     datetime = models.DateTimeField(blank=True, null=True)
#     double = models.FloatField(blank=True, null=True)
#     float = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
#     logical = models.BooleanField(blank=True, null=True)
#     memo = models.TextField(blank=True, null=True)
#     memobin = models.TextField(blank=True, null=True)
#     numeric = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
#     varbinary = models.BinaryField(blank=True, null=True)
#     varchar = models.CharField(max_length=10, blank=True, null=True)
#     vcarcharb = models.CharField(max_length=10, blank=True, null=True)
#     general = models.BinaryField(blank=True, null=True)
#     class Meta:
#         # managed = False
#         db_table = 'T_DBF'

# class DataSourceInfo(models.Model):
#     """Store data source info like as connection string"""
#     CLIPPER_CONNECTOR_CLASS = 'AdvantageClipperConnect'
#     VFP_CONNECTOR_CLASS = 'AdvantageVisualFoxproConnect'
#     DSN_CONNECTOR_CLASS = 'ODBCDataSourceConnect'
#
#     ODBC_CONNECTORS = (
#         (CLIPPER_CONNECTOR_CLASS, _('Connect to the Clipper tables')),
#         (VFP_CONNECTOR_CLASS, _('Connect to the Visual Foxpro free tables')),
#         (DSN_CONNECTOR_CLASS, _('Connect to the Data Sources by DSN')),
#     )
#     name = models.CharField(_('Data Source name'), max_length=128, blank=False, unique=True)
#     slug_name = models.SlugField(max_length=150)
#     connector = models.CharField(_('Choose connector'), max_length=50,
#                                  choices=ODBC_CONNECTORS, default=CLIPPER_CONNECTOR_CLASS, blank=False)
#     description = models.CharField(_('Description of the connector'), max_length=200)
#     settings = models.TextField(_('Json settings for connection'), blank=False)
#
#     def save(
#         self, force_insert=False, force_update=False, using=None, update_fields=None
#     ):
#         self.slug_name = slugify(self.name)
#         super(DataSourceInfo, self).save(force_insert=force_insert, force_update=force_update,
#                                             using=using, update_fields=update_fields
#                                          )
#
#     class Meta:
#         # app_label = 'sqlimport'
#         db_table = 'data_source_info'
