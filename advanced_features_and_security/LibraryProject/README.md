## This is going to be used for the library project

# Django Security Measures

1. **Settings Hardened**

   - DEBUG = False
   - Secure cookies (`CSRF_COOKIE_SECURE`, `SESSION_COOKIE_SECURE`)
   - XSS, clickjacking, and MIME protections

2. **CSRF Protection**

   - `{% csrf_token %}` added to all forms

3. **SQL Injection Prevention**

   - ORM queries instead of raw SQL
   - Input validation with Django Forms

4. **Content Security Policy (CSP)**

   - Restricts scripts, styles, and fonts to trusted domains

5. **Testing**
   - Verified form submissions reject CSRF attacks
   - Search functionality tested against SQL injection attempts
   - CSP tested by attempting to load external scripts (blocked)

Security Hardening — LibraryProject

1) HTTPS Enforcement
- SECURE_SSL_REDIRECT = True
- nginx configured to redirect port 80 -> 443

2) HSTS
- SECURE_HSTS_SECONDS = 31536000
- SECURE_HSTS_INCLUDE_SUBDOMAINS = True
- SECURE_HSTS_PRELOAD = True

3) Secure Cookies
- SESSION_COOKIE_SECURE = True
- CSRF_COOKIE_SECURE = True
- SESSION_COOKIE_SAMESITE = "Lax"

4) Secure Headers
- X_FRAME_OPTIONS = "DENY"
- SECURE_CONTENT_TYPE_NOSNIFF = True
- SECURE_BROWSER_XSS_FILTER = True

5) CSP
- django-csp middleware configured with a conservative CSP (only trusted CDNs)

6) Deployment Notes
- Use Let's Encrypt / Certbot for free SSL certs
- Ensure proxy sets X-Forwarded-Proto; configure SECURE_PROXY_SSL_HEADER accordingly
- Test using curl, browser devtools, and security scanners.

7) Next Steps
- Periodic dependency updates.
- Use automated scans (e.g., OWASP ZAP) before releases.
