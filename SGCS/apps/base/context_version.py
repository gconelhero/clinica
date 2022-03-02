# -*- coding: utf-8 -*-

from SGCS import __version__


def sige_version(request):
    return {'versao': __version__}
