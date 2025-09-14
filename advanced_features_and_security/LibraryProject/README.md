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
