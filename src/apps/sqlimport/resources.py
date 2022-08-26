from import_export.resources import ModelResource
from src.apps.common import mixins
#####################################################################################
# import models for DBF
#####################################################################################
from .models import (
    TDclHead, TAktsHead, TAktsMess, TAktsPath, TCntOto,
    TCvc, TDclamnum, TDclavtmb, TDclcont, TDclcrdts,
    TDcldinf2, TDcldinfo, TDcldog, TDcldoga, TDcldogt,
    TDclkmp, TDclkmpk, TDcllistd, TDcllisth, TDcllistl,
    TDclpasp, TDclpk, TDclplat2, TDclplatr, TDclplatv,
    TDclpredd, TDclquerd, TDclquerh, TDclquern, TDclrinfo,
    TDclriska, TDclriskb, TDclriskc, TDclriskd, TDclriskm,
    TDclriskp, TDclrsinf, TDclrsk93, TDclrsmpr, TDclrsnfi,
    TDclslotm, TDclsltov, TDclsumpp, TDcltcim, TDcltechd,
    TDclterms, TDcltois, TDcltov2, TDcltovar, TDcltovg,
    TDcltovg2, TDcltovs, TDcltovs2, TDcltrans, TDclusl,
    TDcluslt, TDclvrsk, TDk1, TDk2, TDkPp, TDkisch, TDkkupl,
    TDkoprp, TDkpeni, TDtcddtc, TDtcdinfo, TDtchead,
    TDtcslotm, TDtcsscv, TDtcsstc, TKtcavtmb, TKtcdinfo,
    TKtcdokiz, TKtchead, TKtcpk, TKtcplbiz, TKtcpltiz,
    TKtcslotm, TKtcsltov, TKtcsumpp, TKtcterms, TKtctovg,
    TKtctoviz, TKtctovs, TKtdamnum, TKtdavtmb, TKtdcont,
    TKtddinf2, TKtddinfo, TKtdhead, TKtdpasp, TKtdpk,
    TKtdplbiz, TKtdpltiz, TKtdpredd, TKtdslotm, TKtdsltov,
    TKtdsumpp, TKtdtcim, TKtdtechd, TKtdterms, TKtdtois,
    TKtdtov2, TKtdtovar, TKtdtovg, TKtdtovg2, TKtdtovs,
    TKtdtovs2, TKtdtrans, TKtduslt, TOupavtmb, TOupdinfo,
    TOupdokiz, TOuphead, TOuppk, TOupplbiz, TOuppltiz,
    TOupslotm, TOupsltov, TOupsumpp, TOupterms, TOuptovg,
    TOuptoviz, TOuptovs, TProterr, TProtprim, TPzkErr,
    TPzkHead, TPzkRsn,
)
#####################################################################################
# import models for Doc2SQL
#####################################################################################
from .models import (
    TDclDop48, TKtdCrdts, TKtdDog, TKtdDoga,
    TKtdDogt, TKtdKmp, TKtdKmpk, TKtdPlatr,
    TKtdPlatv,
)

class DclHeadResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclHead


class AktsHeadResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TAktsHead


class AktsMessResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TAktsMess


class AktsPathResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TAktsPath


class CntOtoResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TCntOto


class CvcResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TCvc


class DclamnumResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclamnum


class DclavtmbResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclavtmb


class DclcontResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclcont


class DclcrdtsResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclcrdts


class Dcldinf2Resource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDcldinf2


class DcldinfoResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDcldinfo


class DcldogResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDcldog


class DcldogaResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDcldoga


class DcldogtResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDcldogt


class DclkmpResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclkmp


class DclkmpkResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclkmpk


class DcllistdResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDcllistd


class DcllisthResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDcllisth


class DcllistlResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDcllistl


class DclpaspResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclpasp


class DclpkResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclpk


class Dclplat2Resource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclplat2


class DclplatrResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclplatr


class DclplatvResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclplatv


class DclpreddResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclpredd


class DclquerdResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclquerd


class DclquerhResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclquerh


class DclquernResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclquern


class DclrinfoResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclrinfo


class DclriskaResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclriska


class DclriskbResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclriskb


class DclriskcResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclriskc


class DclriskdResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclriskd


class DclriskmResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclriskm


class DclriskpResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclriskp


class DclrsinfResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclrsinf


class Dclrsk93Resource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclrsk93


class DclrsmprResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclrsmpr


class DclrsnfiResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclrsnfi


class DclslotmResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclslotm


class DclsltovResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclsltov


class DclsumppResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclsumpp


class DcltcimResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDcltcim


class DcltechdResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDcltechd


class DcltermsResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclterms


class DcltoisResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDcltois


class Dcltov2Resource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDcltov2


class DcltovarResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDcltovar


class DcltovgResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDcltovg


class Dcltovg2Resource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDcltovg2


class DcltovsResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDcltovs


class Dcltovs2Resource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDcltovs2


class DcltransResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDcltrans


class DcluslResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclusl


class DclusltResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDcluslt


class DclvrskResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclvrsk


class Dk1Resource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDk1


class Dk2Resource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDk2


class DkPpResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDkPp


class DkischResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDkisch


class DkkuplResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDkkupl


class DkoprpResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDkoprp


class DkpeniResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDkpeni


class DtcddtcResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDtcddtc


class DtcdinfoResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDtcdinfo


class DtcheadResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDtchead


class DtcslotmResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDtcslotm


class DtcsscvResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDtcsscv


class DtcsstcResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDtcsstc


class KtcavtmbResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtcavtmb


class KtcdinfoResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtcdinfo


class KtcdokizResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtcdokiz


class KtcheadResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtchead


class KtcpkResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtcpk


class KtcplbizResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtcplbiz


class KtcpltizResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtcpltiz


class KtcslotmResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtcslotm


class KtcsltovResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtcsltov


class KtcsumppResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtcsumpp


class KtctermsResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtcterms


class KtctovgResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtctovg


class KtctovizResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtctoviz


class KtctovsResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtctovs


class KtdamnumResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdamnum


class KtdavtmbResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdavtmb


class KtdcontResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdcont


class Ktddinf2Resource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtddinf2


class KtddinfoResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtddinfo


class KtdheadResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdhead


class KtdpaspResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdpasp


class KtdpkResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdpk


class KtdplbizResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdplbiz


class KtdpltizResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdpltiz


class KtdpreddResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdpredd


class KtdslotmResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdslotm


class KtdsltovResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdsltov


class KtdsumppResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdsumpp


class KtdtcimResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdtcim


class KtdtechdResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdtechd


class KtdtermsResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdterms


class KtdtoisResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdtois


class Ktdtov2Resource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdtov2


class KtdtovarResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdtovar


class KtdtovgResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdtovg


class Ktdtovg2Resource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdtovg2


class KtdtovsResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdtovs


class Ktdtovs2Resource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdtovs2


class KtdtransResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdtrans


class KtdusltResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtduslt


class OupavtmbResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TOupavtmb


class OupdinfoResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TOupdinfo


class OupdokizResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TOupdokiz


class OupheadResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TOuphead


class OuppkResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TOuppk


class OupplbizResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TOupplbiz


class OuppltizResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TOuppltiz


class OupslotmResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TOupslotm


class OupslotmResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TOupslotm


class OupsltovResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TOupsltov


class OupsumppResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TOupsumpp


class OuptermsResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TOupterms


class OuptovgResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TOuptovg


class OuptovizResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TOuptoviz


class OuptovsResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TOuptovs


class ProterrResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TProterr


class ProtprimResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TProtprim


class PzkErrResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TPzkErr


class PzkHeadResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TPzkHead


class PzkRsnResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TPzkRsn

#####################################################################################
# import models for Doc2SQL
#####################################################################################
class DclDop48Resource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclDop48


class KtdCrdtsResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdCrdts


class KtdDogResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdDog


class KtdDogaResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdDoga


class KtdDogtResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdDogt


class KtdKmpResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdKmp


class KtdKmpkResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdKmpk


class KtdPlatrResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdPlatr


class KtdPlatvResource(mixins.ExtResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdPlatv


# Script for generate resourse classes
# c = (
#     'TDclHead', 'TAktsHead', 'TAktsMess', 'TAktsPath', 'TCntOto',
#     'TCvc', 'TDclamnum', 'TDclavtmb', 'TDclcont', 'TDclcrdts',
#     'TDcldinf2', 'TDcldinfo', 'TDcldog', 'TDcldoga', 'TDcldogt',
#     'TDclkmp', 'TDclkmpk', 'TDcllistd', 'TDcllisth', 'TDcllistl',
#     'TDclpasp', 'TDclpk', 'TDclplat2', 'TDclplatr', 'TDclplatv',
#     'TDclpredd', 'TDclquerd', 'TDclquerh', 'TDclquern', 'TDclrinfo',
#     'TDclriska', 'TDclriskb', 'TDclriskc', 'TDclriskd', 'TDclriskm',
#     'TDclriskp', 'TDclrsinf', 'TDclrsk93', 'TDclrsmpr', 'TDclrsnfi',
#     'TDclslotm', 'TDclsltov', 'TDclsumpp', 'TDcltcim', 'TDcltechd',
#     'TDclterms', 'TDcltois', 'TDcltov2', 'TDcltovar', 'TDcltovg',
#     'TDcltovg2', 'TDcltovs', 'TDcltovs2', 'TDcltrans', 'TDclusl',
#     'TDcluslt', 'TDclvrsk', 'TDk1', 'TDk2', 'TDkPp', 'TDkisch', 'TDkkupl',
#     'TDkoprp', 'TDkpeni', 'TDtcddtc', 'TDtcdinfo', 'TDtchead',
#     'TDtcslotm', 'TDtcsscv', 'TDtcsstc', 'TKtcavtmb', 'TKtcdinfo',
#     'TKtcdokiz', 'TKtchead', 'TKtcpk', 'TKtcplbiz', 'TKtcpltiz',
#     'TKtcslotm', 'TKtcsltov', 'TKtcsumpp', 'TKtcterms', 'TKtctovg',
#     'TKtctoviz', 'TKtctovs', 'TKtdamnum', 'TKtdavtmb', 'TKtdcont',
#     'TKtddinf2', 'TKtddinfo', 'TKtdhead', 'TKtdpasp', 'TKtdpk',
#     'TKtdplbiz', 'TKtdpltiz', 'TKtdpredd', 'TKtdslotm', 'TKtdsltov',
#     'TKtdsumpp', 'TKtdtcim', 'TKtdtechd', 'TKtdterms', 'TKtdtois',
#     'TKtdtov2', 'TKtdtovar', 'TKtdtovg', 'TKtdtovg2', 'TKtdtovs',
#     'TKtdtovs2', 'TKtdtrans', 'TKtduslt', 'TOupavtmb', 'TOupdinfo',
#     'TOupdokiz', 'TOuphead', 'TOuppk', 'TOupplbiz', 'TOuppltiz',
#     'TOupslotm', 'TOupslotm', 'TOupsltov', 'TOupsumpp', 'TOupterms',
#     'TOuptovg', 'TOuptoviz', 'TOuptovs', 'TProterr', 'TProtprim',
#     'TPzkErr', 'TPzkHead', 'TPzkRsn',
# )
#
# for k in c:
#     klass_name = k[1:]
#     out = \
#     f"""
#     class {klass_name}Resource(mixins.ExtResource, ModelResource):
#         class Meta(mixins.ExtResource.Meta):
#             model = {k}
#     """
#     print(out)
