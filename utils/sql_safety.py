import re

FORBIDDEN = re.compile(
     r"(|--|\b(ALTER|CREATE|DELETE|DROP|TRUNCATE|INSERT|UPDATE)\b)",
    re.IGNORECASE,
)
def is_sql_safe(sql: str) -> bool:
     sql = sql.strip().rstrip(";")
    return not FORBIDDEN.search(sql)
