from django.db import models
import uuid

class Sessao(models.Modal):

        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        usuario.models.ForeignKey(Usuario,on_delete=models.CASCADE)

        class Meta:
            db_table = 'Sessao';
