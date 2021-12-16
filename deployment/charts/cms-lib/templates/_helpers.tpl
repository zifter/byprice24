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
- name: RQ_REDIS_URL
  value: {{ required "Redis url is required"  .Values.redis.url | quote }}
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
{{- end }}