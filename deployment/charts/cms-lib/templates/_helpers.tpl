{{- define "cms-lib.env" -}}
- name: DJANGO_CONFIGURATION
  value: {{ required "Configuration is required" .Values.configuration | quote }}
- name: DOMAIN_API
  value: {{ required "Api domain is required" .Values.domain.api | quote }}
- name: DOMAIN_ADMIN
  value: {{ required "Admin domain is required" .Values.domain.admin | quote }}
- name: SECRET_KEY
  value: {{ required "SecretKey is required" .Values.secretKey | quote }}
- name: POD_IP
  valueFrom:
    fieldRef:
      fieldPath: status.podIP
- name: RQ_REDIS_HOST
  value: {{ required "Redis host is required"  .Values.redis.rq.host | quote }}
- name: RQ_REDIS_PORT
  value: {{ required "Redis port is required"  .Values.redis.rq.port | quote }}
- name: RQ_REDIS_DB
  value: {{ required "Redis db is required"  .Values.redis.rq.db | quote }}
- name: STORAGE_REDIS_HOST
  value: {{ required "Redis host is required"  .Values.redis.storage.host | quote }}
- name: STORAGE_REDIS_PORT
  value: {{ required "Redis port is required"  .Values.redis.storage.port | quote }}
- name: STORAGE_REDIS_DB
  value: {{ required "Redis db is required"  .Values.redis.storage.db | quote }}
- name: DB_NAME
  value: {{ required "DB name is required" .Values.postgres.dbname | quote }}
- name: DB_USERNAME
  value: {{ required "postgres username is required" .Values.postgres.username | quote }}
- name: DB_PASSWORD
  value: {{ required "Postgres password is required" .Values.postgres.password | quote }}
- name: DB_HOST
  value: {{ required "Postgres host is required" .Values.postgres.host | quote }}
- name: DB_PORT
  value: {{ required "Postgres port is required" .Values.postgres.port | quote }}
- name: ELASTICSEARCH_DSL
  value: {{ required "Elasticsearch url is required" .Values.elasticsearch.url | quote }}
{{- end }}

{{- define "cms-lib.sentry" -}}
- name: RQ_SENTRY_DSN # https://python-rq.org/patterns/sentry/
  value: {{ .Values.sentry.dsn | quote }}
- name: SENTRY_DSN
  value: {{ .Values.sentry.dsn | quote }}
- name: SENTRY_RELEASE
  value: {{ .Values.release  | quote }}
- name: SENTRY_ENVIRONMENT
  value: {{ .Values.envName  | quote }}
- name: SENTRY_DEBUG
  value: {{ .Values.sentry.debug | quote }}
{{- end }}
