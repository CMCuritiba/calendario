class Calendario(object):
	def __init__(self, **kwargs):
		for field in ('id', 'start', 'end', 'url', 'title', 'setor', 'pessoa', 'cclass'):
			setattr(self, field, kwargs.get(field, None))
