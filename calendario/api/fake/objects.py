class Calendario(object):
	def __init__(self, **kwargs):
		for field in ('id', 'data', 'descricao'):
			setattr(self, field, kwargs.get(field, None))