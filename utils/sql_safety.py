import re

FORBIDDEN = re.compile(
     r"(||\b(ALTER|CREATE|DELETE|DROP|TRUNCATE|INSERT|UPDATE)\b)",
    re.IGNORECASE,
)
def is_sql_safe(sql: str) -> bool:
    return not FORBIDDEN.search(sql)
