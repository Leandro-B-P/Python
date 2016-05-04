#!/usr/bin/python

from datetime import datetime, timedelta, date

def validar_token():

	requisicao = datetime(2016,04,27,00,00,00)
	atual = datetime(2016,04,27,00,00,00)
	if (atual - requisicao).total_seconds() < 3600:
		return True
	else:
		return False

