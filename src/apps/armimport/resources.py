from import_export.resources import ModelResource
from .models import (
    TDclAmnum, TDclAvtmb, TDclCont, TDclCrdts,
    TDclDinf2, TDclDinfo, TDclDog, TDclDoga, TDclDogt,
    TDclDop48, TDclHead, TDclKmp, TDclKmpk, TDclListd,
    TDclListh, TDclListl, TDclPasp, TDclPk, TDclPlatr,
    TDclPlatv, TDclPredd, TDclQuerd, TDclQuerh,
    TDclSumpp, TDclTechd, TDclTerms, TDclTov2, TDclTovar,
    TDclTovg, TDclTovg2, TDclTovs, TDclTovs2, TDclTrans,
    TDclUslt, TDtcDdtc, TDtcDinfo, TDtcHead, TDtcSscv,
    TDtcSstc, TKtcAvtmb, TKtcDinfo, TKtcDokiz, TKtcHead,
    TKtcPk, TKtcPlbiz, TKtcPltiz, TKtcSumpp, TKtcTerms,
    TKtcTovg, TKtcToviz, TKtcTovs, TKtdAvtmb, TKtdCont,
    TKtdCrdts, TKtdDinf2, TKtdDinfo, TKtdDog, TKtdDoga,
    TKtdDogt, TKtdHead, TKtdKmp, TKtdKmpk, TKtdPasp,
    TKtdPk, TKtdPlatr, TKtdPlatv, TKtdPredd, TKtdSumpp,
    TKtdTechd, TKtdTerms, TKtdTov2, TKtdTovar, TKtdTovg,
    TKtdTovg2, TKtdTovs, TKtdTrans, TKtdUslt,
)
from src.apps.common import mixins


class DclmnumResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclAmnum


class DclavtmbResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclAvtmb


class DclcontResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclCont


class DclcrdtsResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclCrdts


class Dcldinf2Resource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclDinf2


class DcldinfoResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclDinfo


class DcldogResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclDog


class DcldogaResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclDoga


class DcldogtResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclDogt


class Dcldop48Resource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclDop48


class DclheadResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclHead


class DclkmpResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclKmp


class DclkmpkResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclKmpk


class DcllistdResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclListd


class DcllisthResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclListh


class DcllistlResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclListl


class DclpaspResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclPasp


class DclpkResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclPk


class DclplatrResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclPlatr


class DclplatvResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclPlatv


class DclpreddResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclPredd


class DclquerdResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclQuerd


class DclquerhResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclQuerh


class DclsumppResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclSumpp


class DcltechdResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclTechd


class DcltermsResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclTerms


class Dcltov2Resource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclTov2


class DcltovarResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclTovar


class DcltovgResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclTovg


class Dcltovg2Resource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclTovg2


class DcltovsResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclTovs


class Dcltovs2Resource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclTovs2


class DcltransResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclTrans


class DclusltResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDclUslt


class DtcddtcResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDtcDdtc


class DtcdinfoResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDtcDinfo


class DtcheadResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDtcHead


class DtcsscvResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDtcSscv


class DtcsstcResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TDtcSstc


class KtcavtmbResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtcAvtmb


class KtcdinfoResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtcDinfo


class KtcdokizResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtcDokiz


class KtcheadResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtcHead


class KtcPkResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtcPk


class KtcplbizResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtcPlbiz


class KtcpltizResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtcPltiz


class KtcsumppResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtcSumpp


class KtctermsResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtcTerms


class KtctovgResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtcTovg


class KtctovizResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtcToviz


class KtctovsResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtcTovs


class KtdavtmbResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdAvtmb


class KtdcontResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdCont


class KtdcrdtsResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdCrdts


class Ktddinf2Resource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdDinf2


class KtddinfoResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdDinfo


class KtddogResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdDog


class KtddogaResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdDoga


class KtddogtResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdDogt


class KtdheadResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdHead


class KtdkmpResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdKmp


class KtdkmpkResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdKmpk


class KtdpaspResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdPasp


class KtdpkResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdPk


class KtdplatrResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdPlatr


class KtdplatvResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdPlatv


class KtdpreddResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdPredd


class KtdsumppResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdSumpp


class KtdtechdResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdTechd


class KtdtermsResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdTerms


class Ktdtov2Resource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdTov2


class KtdtovarResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdTovar


class KtdtovgResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdTovg


class Ktdtovg2Resource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdTovg2


class KtdtovsResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdTovs


class KtdtransResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdTrans


class KtdusltResource(mixins.ArmResource, ModelResource):
    class Meta(mixins.ExtResource.Meta):
        model = TKtdUslt


# Script for generate resourse classes
# c = (
#     'Dbramnum', 'Dbravtmb', 'Dbrcont', 'Dbrcrdts',
#     'Dbrdinf2', 'Dbrdinfo', 'Dbrdog', 'Dbrdoga', 'Dbrdogt',
#     'Dbrdop48', 'Dbrhead', 'Dbrkmp', 'Dcllistd', 'Dcllisth',
#     'Dcllistl', 'Dbrkmpk', 'Dbrpasp', 'Dbrpk', 'Dbrplatr',
#     'Dbrplatv', 'Dbrpredd', 'Dclquerd', 'Dclquerh', 'Dbrsumpp',
#     'Dbrtechd', 'Dbrterms', 'Dbrtov2', 'Dbrtovar', 'Dbrtovg',
#     'Dbrtovg2', 'Dbrtovs', 'Dbrtovs2', 'Dbrtrans', 'Dbruslt',
#     'Sbrddtc', 'Sbrdinfo', 'Sbrhead', 'Sbrsscv', 'Sbrsstc',
#     'Kbravtmb', 'Kbrdinfo', 'Kbrdokiz', 'Kbrhead',
#     'Kbrpk', 'Kbrplbiz', 'Kbrpltiz', 'Kbrsumpp', 'Kbrterms',
#     'Kbrtovg', 'Kbrtoviz', 'Kbrtovs', 'Ktdavtmb',
#     'Ktdcont', 'Ktdcrdts', 'Ktddinf2', 'Ktddinfo', 'Ktddog',
#     'Ktddoga', 'Ktddogt', 'Ktdhead', 'Ktdkmp', 'Ktdkmpk',
#     'Ktdpasp', 'Ktdpk', 'Ktdplatr', 'Ktdplatv', 'Ktdpredd',
#     'Ktdsumpp', 'Ktdtechd', 'Ktdterms', 'Ktdtov2', 'Ktdtovar',
#     'Ktdtovg', 'Ktdtovg2', 'Ktdtovs', 'Ktdtrans', 'Ktduslt',
# )
#
# for k in c:
#     klass_name = k
#     out = \
#     f"""
#     class {klass_name}Resource(mixins.ArmResource, ModelResource):
#         class Meta(mixins.ExtResource.Meta):
#             model = T{k}
#     """
#     print(out)
