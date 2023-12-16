# Как развернуть проект

Создайте `.env` файл с ключами:
```
AUTH0_DOMAIN = dev-1h3larboppake67p.eu.auth0.com
AUTH0_API_AUDIENCE = https://codev0.xyz
AUTH0_ISSUER = https://dev-1h3larboppake67p.eu.auth0.com/
AUTH0_ALGORITHMS = RS256
```

Создайте Postgres БД с именем `webdevendterm`

Чтобы получить токен нужно выполнить curl

```
curl --request POST \
  --url https://dev-1h3larboppake67p.eu.auth0.com/oauth/token \
  --header 'content-type: application/json' \
  --data '{"client_id":"","client_secret":"","audience":"https://codev0.xyz","grant_type":"client_credentials"}'
```

client_id, client_secret отдельно передаются

В репозитории есть файл test_main.http чтобы тестировать через REST Client IDE Jetbrains
