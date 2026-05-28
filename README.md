# VulnScout Test Repository

Intentionally vulnerable project for testing VulnScout CLI scanning,
GitHub issue creation, and auto-fix PR generation.

## Vulnerabilities included

| File | Vulnerability | Severity |
|------|--------------|----------|
| `src/app.py` | Hardcoded credentials | high |
| `src/app.py` | SQL Injection | critical |
| `src/app.py` | eval() code injection | critical |
| `src/app.py` | OS Command Injection | high |
| `src/auth.py` | Hardcoded JWT secret | high |
| `src/auth.py` | Pickle deserialization | high |
| `api/server.js` | Hardcoded API key | high |
| `api/server.js` | eval() injection | critical |
| `api/server.js` | XSS | high |
| `utils/helper.java` | Hardcoded password | high |
| `utils/helper.java` | Command injection | high |
| `utils/buffer.c` | strcpy overflow | critical |
| `utils/buffer.c` | sprintf overflow | high |
| `utils/buffer.c` | gets() overflow | critical |
