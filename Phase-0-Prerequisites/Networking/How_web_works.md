### How the Web Actually Works (HTTP Deep Dive)

The Client-Server Model

Every time when we visit a website:


Our Browser (Client)                    Web Server
      │                                       │
      │──── HTTP Request ────────────────────▶│
      │     "GET /index.html HTTP/1.1"        │
      │     "Host: example.com"               │
      │                                       │
      │◀─── HTTP Response ────────────────────│
      │     "HTTP/1.1 200 OK"                 │
      │     "<html>Hello World</html>"        │

HTTP Request Structure

GET /login HTTP/1.1              ← Request Line (Method, Path, Version)
Host: example.com                ← Headers (metadata about the request)
User-Agent: Mozilla/5.0
Content-Type: application/x-www-form-urlencoded
Content-Length: 27
Cookie: session_id=abc123

username=admin&password=secret   ← Body (data sent to server)
HTTP Response Structure

HTTP/1.1 200 OK                  ← Status Line (Version, Code, Message)
Content-Type: text/html          ← Headers
Content-Length: 1234
Set-Cookie: session=xyz789

<html>                           ← Body (actual content)
  <h1>Welcome</h1>
</html>


HTTP Methods (CRITICAL for Web Security)

Method   | Purpose                    | Has Body? | Security Relevance
---------|----------------------------|-----------|---------------------------
GET      | Retrieve data              | No        | Data in URL (logged!)
POST     | Submit data                | Yes       | Login forms, file uploads
PUT      | Replace/update resource    | Yes       | Can overwrite files
DELETE   | Remove resource            | No        | Can delete data
PATCH    | Partial update             | Yes       | Modify specific fields
HEAD     | Like GET but no body       | No        | Reconnaissance
OPTIONS  | Ask what methods allowed   | No        | CORS preflight
TRACE    | Echo request back          | No        | XST attacks (rare)


HTTP Status Codes 

1xx - Informational
├── 100 Continue

2xx - Success ✅
├── 200 OK (request succeeded)
├── 201 Created (resource created)
└── 204 No Content

3xx - Redirection 🔄
├── 301 Moved Permanently
├── 302 Found (temporary redirect)
└── 304 Not Modified (cached)

4xx - Client Error ❌
├── 400 Bad Request (malformed)
├── 401 Unauthorized (not authenticated)
├── 403 Forbidden (authenticated but no permission)
├── 404 Not Found
├── 405 Method Not Allowed
└── 429 Too Many Requests (rate limited)

5xx - Server Error 💥
├── 500 Internal Server Error
├── 502 Bad Gateway
├── 503 Service Unavailable
└── 504 Gateway Timeout

Security Relevance:
├── 401 vs 403: Know the difference!
│   401 = "Who are you?" (need to login)
│   403 = "I know who you are, but you can't access this"
├── 404: Useful for directory brute forcing
│   (if /admin returns 404, it doesn't exist)
├── 500: May indicate SQL injection worked!
│   (server crashed trying to process malicious input)
└── 200 on /admin: The admin panel exists!

HTTP vs HTTPS

HTTP (Port 80):
├── Plaintext — anyone on the network can read it
├── No encryption, no integrity check
├── Attacker can see passwords, cookies, data
└── NEVER acceptable for login pages

HTTPS (Port 443):
├── Encrypted with TLS/SSL
├── Confidentiality (can't read data)
├── Integrity (can't modify data)
├── Authentication (server identity verified)
├── TLS Handshake:
│   1. Client Hello (supported ciphers)
│   2. Server Hello (chosen cipher + certificate)
│   3. Certificate verification (PKI chain)
│   4. Key exchange (Diffie-Hellman/RSA)
│   5. Encrypted session begins
└── Always look for the padlock 🔒


### HTTP Headers, Cookies, Sessions & Authentication

Important HTTP Headers (Security Focus)

Request Headers:
├── Host: target.com           (which website we want)
├── User-Agent: Mozilla/5.0    (our browser identity)
├── Referer: https://...       (where we came from)
├── Cookie: session=abc        (our session token)
├── Authorization: Bearer xyz  (API authentication)
├── Content-Type: ...          (what data format we're sending)
└── X-Forwarded-For: 1.2.3.4  (original client IP - spoofable!)

Response Headers (Security Headers to Check):
├── Set-Cookie: session=xyz    (server sets our cookie)
├── X-Frame-Options: DENY      (prevents clickjacking)
├── X-Content-Type-Options: nosniff (prevents MIME sniffing)
├── Content-Security-Policy: ... (prevents XSS)
├── Strict-Transport-Security: ... (forces HTTPS)
├── X-XSS-Protection: 1; mode=block (legacy XSS filter)
└── Server: Apache/2.4.41      (information disclosure!)

Security Testing:
├── Missing security headers = misconfiguration
├── Server header reveals version = info disclosure
├── No HSTS = downgrade attack possible
└── No CSP = XSS more likely to succeed


Cookies & Sessions

How Sessions Work:
1. User logs in with username + password
2. Server verifies credentials
3. Server creates a SESSION (stored server-side)
4. Server sends a SESSION ID cookie to browser
   Set-Cookie: PHPSESSID=a1b2c3d4e5f6; HttpOnly; Secure
5. Browser sends this cookie with EVERY request
6. Server looks up session ID → knows who we are
7. When we logout → session destroyed

Cookie Security Flags:
├── HttpOnly: JavaScript cannot read this cookie
│   (prevents XSS from stealing session)
├── Secure: Cookie only sent over HTTPS
│   (prevents interception on HTTP)
├── SameSite=Strict/Lax: Prevents CSRF attacks
│   (cookie not sent on cross-site requests)
└── Path=/ : Cookie valid for entire site

Session Attacks:
├── Session Hijacking: Steal the session cookie
│   (via XSS, MITM, or packet sniffing)
├── Session Fixation: Force victim to use YOUR session ID
│   (then when they login, you have their session)
├── Session Prediction: Guess the session ID pattern
│   (weak random number generation)
└── Cookie Theft: document.cookie in XSS


Authentication Mechanisms

1. Basic Authentication:
   Authorization: Basic dXNlcjpwYXNz (Base64 encoded!)
   ⚠️ NOT encrypted — easily decoded
   echo "dXNlcjpwYXNz" | base64 -d  →  user:pass

2. Bearer Token (JWT):
   Authorization: Bearer eyJhbGciOi...
   JWT = Header.Payload.Signature (Base64)
   Attacks: none algorithm, weak secret, token theft

3. API Keys:
   X-API-Key: abc123def456
   ⚠️ Often leaked in GitHub repos!

4. OAuth 2.0:
   "Login with Google/Facebook"
   Complex flow with authorization codes

5. Multi-Factor (MFA):
   Something we know + something we have
   TOTP codes, SMS, hardware keys
