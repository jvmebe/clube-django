# clube-django

Criar .venv:
`py -m venv .venv`

Instalar requirements.txt:

pip install -r requirements.txt

Gerar uma secret key:

```
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

Criar arquivo auth.py em `./setup` com o seguinte conteúdo:
```secret = '<key>'``` 
<br>

`<key>` é a chave gerada no comando anterior

Criar banco de dados:
`py manage.py migrate`
