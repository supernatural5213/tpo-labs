# ZAP Scanning Report

ZAP by [Checkmarx](https://checkmarx.com/).


## Summary of Alerts

| Risk Level | Number of Alerts |
| --- | --- |
| High | 1 |
| Medium | 2 |
| Low | 8 |
| Informational | 4 |




## Insights

| Level | Reason | Site | Description | Statistic |
| --- | --- | --- | --- | --- |
| Low | Warning |  | ZAP errors logged - see the zap.log file for details | 2    |
| Low | Warning |  | ZAP warnings logged - see the zap.log file for details | 2    |
| Info | Informational | http://localhost:5000 | Percentage of responses with status code 2xx | 87 % |
| Info | Informational | http://localhost:5000 | Percentage of responses with status code 4xx | 9 % |
| Info | Informational | http://localhost:5000 | Percentage of responses with status code 5xx | 3 % |
| Info | Informational | http://localhost:5000 | Percentage of endpoints with content type application/json | 16 % |
| Info | Informational | http://localhost:5000 | Percentage of endpoints with content type text/html | 83 % |
| Info | Informational | http://localhost:5000 | Percentage of endpoints with method DELETE | 37 % |
| Info | Informational | http://localhost:5000 | Percentage of endpoints with method GET | 54 % |
| Info | Informational | http://localhost:5000 | Percentage of endpoints with method POST | 8 % |
| Info | Informational | http://localhost:5000 | Count of total endpoints | 24    |







## Alerts

| Name | Risk Level | Number of Instances |
| --- | --- | --- |
| SQL Injection | High | 1 |
| Content Security Policy (CSP) Header Not Set | Medium | 1 |
| Missing Anti-clickjacking Header | Medium | 1 |
| A Server Error response code was returned by the server | Low | 1 |
| Cross-Origin-Embedder-Policy Header Missing or Invalid | Low | 1 |
| Cross-Origin-Opener-Policy Header Missing or Invalid | Low | 1 |
| Cross-Origin-Resource-Policy Header Missing or Invalid | Low | 5 |
| Permissions Policy Header Not Set | Low | 1 |
| Server Leaks Version Information via "Server" HTTP Response Header Field | Low | 5 |
| Unexpected Content-Type was returned | Low | 22 |
| X-Content-Type-Options Header Missing | Low | 5 |
| A Client Error response code was returned by the server | Informational | 20 |
| Non-Storable Content | Informational | 2 |
| Storable and Cacheable Content | Informational | 2 |
| Storable but Non-Cacheable Content | Informational | 1 |




## Alert Detail



### [ SQL Injection ](https://www.zaproxy.org/docs/alerts/40018/)



##### High (Low)

### Description

SQL injection may be possible.

* URL: http://localhost:5000/api/users%3Fname=%2527&limit=10&offset=0
  * Node Name: `http://localhost:5000/api/users (limit,name,offset)`
  * Method: `GET`
  * Parameter: `name`
  * Attack: `'`
  * Evidence: `HTTP/1.1 500 INTERNAL SERVER ERROR`
  * Other Info: ``


Instances: 1

### Solution

Do not trust client side input, even if there is client side validation in place.
In general, type check all data on the server side.
If the application uses JDBC, use PreparedStatement or CallableStatement, with parameters passed by '?'
If the application uses ASP, use ADO Command Objects with strong type checking and parameterized queries.
If database Stored Procedures can be used, use them.
Do *not* concatenate strings into queries in the stored procedure, or use 'exec', 'exec immediate', or equivalent functionality!
Do not create dynamic SQL queries using simple string concatenation.
Escape all data received from the client.
Apply an 'allow list' of allowed characters, or a 'deny list' of disallowed characters in user input.
Apply the principle of least privilege by using the least privileged database user possible.
In particular, avoid using the 'sa' or 'db-owner' database users. This does not eliminate SQL injection, but minimizes its impact.
Grant the minimum database access that is necessary for the application.

### Reference


* [ https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html ](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)


#### CWE Id: [ 89 ](https://cwe.mitre.org/data/definitions/89.html)


#### WASC Id: 19

#### Source ID: 1

### [ Content Security Policy (CSP) Header Not Set ](https://www.zaproxy.org/docs/alerts/10038/)



##### Medium (High)

### Description

Content Security Policy (CSP) is an added layer of security that helps to detect and mitigate certain types of attacks, including Cross Site Scripting (XSS) and data injection attacks. These attacks are used for everything from data theft to site defacement or distribution of malware. CSP provides a set of standard HTTP headers that allow website owners to declare approved sources of content that browsers should be allowed to load on that page — covered types are JavaScript, CSS, HTML frames, fonts, images and embeddable objects such as Java applets, ActiveX, audio and video files.

* URL: http://localhost:5000/users
  * Node Name: `http://localhost:5000/users`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``


Instances: 1

### Solution

Ensure that your web server, application server, load balancer, etc. is configured to set the Content-Security-Policy header.

### Reference


* [ https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP ](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP)
* [ https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html ](https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html)
* [ https://www.w3.org/TR/CSP/ ](https://www.w3.org/TR/CSP/)
* [ https://w3c.github.io/webappsec-csp/ ](https://w3c.github.io/webappsec-csp/)
* [ https://web.dev/articles/csp ](https://web.dev/articles/csp)
* [ https://caniuse.com/#feat=contentsecuritypolicy ](https://caniuse.com/#feat=contentsecuritypolicy)
* [ https://content-security-policy.com/ ](https://content-security-policy.com/)


#### CWE Id: [ 693 ](https://cwe.mitre.org/data/definitions/693.html)


#### WASC Id: 15

#### Source ID: 3

### [ Missing Anti-clickjacking Header ](https://www.zaproxy.org/docs/alerts/10020/)



##### Medium (Medium)

### Description

The response does not protect against 'ClickJacking' attacks. It should include either Content-Security-Policy with 'frame-ancestors' directive or X-Frame-Options.

* URL: http://localhost:5000/users
  * Node Name: `http://localhost:5000/users`
  * Method: `GET`
  * Parameter: `x-frame-options`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``


Instances: 1

### Solution

Modern Web browsers support the Content-Security-Policy and X-Frame-Options HTTP headers. Ensure one of them is set on all web pages returned by your site/app.
If you expect the page to be framed only by pages on your server (e.g. it's part of a FRAMESET) then you'll want to use SAMEORIGIN, otherwise if you never expect the page to be framed, you should use DENY. Alternatively consider implementing Content Security Policy's "frame-ancestors" directive.

### Reference


* [ https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Frame-Options ](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Frame-Options)


#### CWE Id: [ 1021 ](https://cwe.mitre.org/data/definitions/1021.html)


#### WASC Id: 15

#### Source ID: 3

### [ A Server Error response code was returned by the server ](https://www.zaproxy.org/docs/alerts/100000/)



##### Low (High)

### Description

A response code of 500 was returned by the server.
This may indicate that the application is failing to handle unexpected input correctly.
Raised by the 'Alert on HTTP Response Code Error' script

* URL: http://localhost:5000/api/users%3Fname=5%253BURL%253D%2527https%253A%252F%252F6543469631144477992.owasp.org%2527&limit=10&offset=0
  * Node Name: `http://localhost:5000/api/users (limit,name,offset)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `500`
  * Other Info: ``


Instances: 1

### Solution



### Reference



#### CWE Id: [ 388 ](https://cwe.mitre.org/data/definitions/388.html)


#### WASC Id: 20

#### Source ID: 4

### [ Cross-Origin-Embedder-Policy Header Missing or Invalid ](https://www.zaproxy.org/docs/alerts/90004/)



##### Low (Medium)

### Description

Cross-Origin-Embedder-Policy header is a response header that prevents a document from loading any cross-origin resources that don't explicitly grant the document permission (using CORP or CORS).

* URL: http://localhost:5000/users
  * Node Name: `http://localhost:5000/users`
  * Method: `GET`
  * Parameter: `Cross-Origin-Embedder-Policy`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``


Instances: 1

### Solution

Ensure that the application/web server sets the Cross-Origin-Embedder-Policy header appropriately, and that it sets the Cross-Origin-Embedder-Policy header to 'require-corp' for documents.
If possible, ensure that the end user uses a standards-compliant and modern web browser that supports the Cross-Origin-Embedder-Policy header (https://caniuse.com/mdn-http_headers_cross-origin-embedder-policy).

### Reference


* [ https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cross-Origin-Embedder-Policy ](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cross-Origin-Embedder-Policy)


#### CWE Id: [ 693 ](https://cwe.mitre.org/data/definitions/693.html)


#### WASC Id: 14

#### Source ID: 3

### [ Cross-Origin-Opener-Policy Header Missing or Invalid ](https://www.zaproxy.org/docs/alerts/90004/)



##### Low (Medium)

### Description

Cross-Origin-Opener-Policy header is a response header that allows a site to control if others included documents share the same browsing context. Sharing the same browsing context with untrusted documents might lead to data leak.

* URL: http://localhost:5000/users
  * Node Name: `http://localhost:5000/users`
  * Method: `GET`
  * Parameter: `Cross-Origin-Opener-Policy`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``


Instances: 1

### Solution

Ensure that the application/web server sets the Cross-Origin-Opener-Policy header appropriately, and that it sets the Cross-Origin-Opener-Policy header to 'same-origin' for documents.
'same-origin-allow-popups' is considered as less secured and should be avoided.
If possible, ensure that the end user uses a standards-compliant and modern web browser that supports the Cross-Origin-Opener-Policy header (https://caniuse.com/mdn-http_headers_cross-origin-opener-policy).

### Reference


* [ https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cross-Origin-Opener-Policy ](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cross-Origin-Opener-Policy)


#### CWE Id: [ 693 ](https://cwe.mitre.org/data/definitions/693.html)


#### WASC Id: 14

#### Source ID: 3

### [ Cross-Origin-Resource-Policy Header Missing or Invalid ](https://www.zaproxy.org/docs/alerts/90004/)



##### Low (Medium)

### Description

Cross-Origin-Resource-Policy header is an opt-in header designed to counter side-channels attacks like Spectre. Resource should be specifically set as shareable amongst different origins.

* URL: http://localhost:5000/api/users/1
  * Node Name: `http://localhost:5000/api/users/1`
  * Method: `DELETE`
  * Parameter: `Cross-Origin-Resource-Policy`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://localhost:5000/api/users%3Fname=user_abc&limit=10&offset=0
  * Node Name: `http://localhost:5000/api/users (limit,name,offset)`
  * Method: `GET`
  * Parameter: `Cross-Origin-Resource-Policy`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://localhost:5000/openapi.json
  * Node Name: `http://localhost:5000/openapi.json`
  * Method: `GET`
  * Parameter: `Cross-Origin-Resource-Policy`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://localhost:5000/users
  * Node Name: `http://localhost:5000/users`
  * Method: `GET`
  * Parameter: `Cross-Origin-Resource-Policy`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: http://localhost:5000/api/users
  * Node Name: `http://localhost:5000/api/users ()({name,email})`
  * Method: `POST`
  * Parameter: `Cross-Origin-Resource-Policy`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``


Instances: 5

### Solution

Ensure that the application/web server sets the Cross-Origin-Resource-Policy header appropriately, and that it sets the Cross-Origin-Resource-Policy header to 'same-origin' for all web pages.
'same-site' is considered as less secured and should be avoided.
If resources must be shared, set the header to 'cross-origin'.
If possible, ensure that the end user uses a standards-compliant and modern web browser that supports the Cross-Origin-Resource-Policy header (https://caniuse.com/mdn-http_headers_cross-origin-resource-policy).

### Reference


* [ https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cross-Origin-Embedder-Policy ](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cross-Origin-Embedder-Policy)


#### CWE Id: [ 693 ](https://cwe.mitre.org/data/definitions/693.html)


#### WASC Id: 14

#### Source ID: 3

### [ Permissions Policy Header Not Set ](https://www.zaproxy.org/docs/alerts/10063/)



##### Low (Medium)

### Description

Permissions Policy Header is an added layer of security that helps to restrict from unauthorized access or usage of browser/client features by web resources. This policy ensures the user privacy by limiting or specifying the features of the browsers can be used by the web resources. Permissions Policy provides a set of standard HTTP headers that allow website owners to limit which features of browsers can be used by the page such as camera, microphone, location, full screen etc.

* URL: http://localhost:5000/users
  * Node Name: `http://localhost:5000/users`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``


Instances: 1

### Solution

Ensure that your web server, application server, load balancer, etc. is configured to set the Permissions-Policy header.

### Reference


* [ https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy ](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Permissions-Policy)
* [ https://developer.chrome.com/blog/feature-policy/ ](https://developer.chrome.com/blog/feature-policy/)
* [ https://scotthelme.co.uk/a-new-security-header-feature-policy/ ](https://scotthelme.co.uk/a-new-security-header-feature-policy/)
* [ https://w3c.github.io/webappsec-feature-policy/ ](https://w3c.github.io/webappsec-feature-policy/)
* [ https://www.smashingmagazine.com/2018/12/feature-policy/ ](https://www.smashingmagazine.com/2018/12/feature-policy/)


#### CWE Id: [ 693 ](https://cwe.mitre.org/data/definitions/693.html)


#### WASC Id: 15

#### Source ID: 3

### [ Server Leaks Version Information via "Server" HTTP Response Header Field ](https://www.zaproxy.org/docs/alerts/10036/)



##### Low (High)

### Description

The web/application server is leaking version information via the "Server" HTTP response header. Access to such information may facilitate attackers identifying other vulnerabilities your web/application server is subject to.

* URL: http://localhost:5000/api/users/1
  * Node Name: `http://localhost:5000/api/users/1`
  * Method: `DELETE`
  * Parameter: ``
  * Attack: ``
  * Evidence: `Werkzeug/3.1.9 Python/3.11.17`
  * Other Info: ``
* URL: http://localhost:5000/api/users%3Fname=user_abc&limit=10&offset=0
  * Node Name: `http://localhost:5000/api/users (limit,name,offset)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `Werkzeug/3.1.9 Python/3.11.17`
  * Other Info: ``
* URL: http://localhost:5000/openapi.json
  * Node Name: `http://localhost:5000/openapi.json`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `Werkzeug/3.1.9 Python/3.11.17`
  * Other Info: ``
* URL: http://localhost:5000/users
  * Node Name: `http://localhost:5000/users`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `Werkzeug/3.1.9 Python/3.11.17`
  * Other Info: ``
* URL: http://localhost:5000/api/users
  * Node Name: `http://localhost:5000/api/users ()({name,email})`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `Werkzeug/3.1.9 Python/3.11.17`
  * Other Info: ``


Instances: 5

### Solution

Ensure that your web server, application server, load balancer, etc. is configured to suppress the "Server" header or provide generic details.

### Reference


* [ https://httpd.apache.org/docs/current/mod/core.html#servertokens ](https://httpd.apache.org/docs/current/mod/core.html#servertokens)
* [ https://learn.microsoft.com/en-us/previous-versions/msp-n-p/ff648552(v=pandp.10) ](https://learn.microsoft.com/en-us/previous-versions/msp-n-p/ff648552(v=pandp.10))
* [ https://www.troyhunt.com/shhh-dont-let-your-response-headers/ ](https://www.troyhunt.com/shhh-dont-let-your-response-headers/)


#### CWE Id: [ 497 ](https://cwe.mitre.org/data/definitions/497.html)


#### WASC Id: 13

#### Source ID: 3

### [ Unexpected Content-Type was returned ](https://www.zaproxy.org/docs/alerts/100001/)



##### Low (High)

### Description

A Content-Type of text/html was returned by the server.
This is not one of the types expected to be returned by an API.
Raised by the 'Alert on Unexpected Content Types' script

* URL: http://localhost:5000/api/users/1/
  * Node Name: `http://localhost:5000/api/users/1/`
  * Method: `DELETE`
  * Parameter: ``
  * Attack: ``
  * Evidence: `text/html`
  * Other Info: ``
* URL: http://localhost:5000/computeMetadata/v1/
  * Node Name: `http://localhost:5000/computeMetadata/v1/`
  * Method: `DELETE`
  * Parameter: ``
  * Attack: ``
  * Evidence: `text/html`
  * Other Info: ``
* URL: http://localhost:5000/latest/meta-data/
  * Node Name: `http://localhost:5000/latest/meta-data/`
  * Method: `DELETE`
  * Parameter: ``
  * Attack: ``
  * Evidence: `text/html`
  * Other Info: ``
* URL: http://localhost:5000/metadata/instance
  * Node Name: `http://localhost:5000/metadata/instance`
  * Method: `DELETE`
  * Parameter: ``
  * Attack: ``
  * Evidence: `text/html`
  * Other Info: ``
* URL: http://localhost:5000/metadata/v1
  * Node Name: `http://localhost:5000/metadata/v1`
  * Method: `DELETE`
  * Parameter: ``
  * Attack: ``
  * Evidence: `text/html`
  * Other Info: ``
* URL: http://localhost:5000/opc/v1/instance/
  * Node Name: `http://localhost:5000/opc/v1/instance/`
  * Method: `DELETE`
  * Parameter: ``
  * Attack: ``
  * Evidence: `text/html`
  * Other Info: ``
* URL: http://localhost:5000/opc/v2/instance/
  * Node Name: `http://localhost:5000/opc/v2/instance/`
  * Method: `DELETE`
  * Parameter: ``
  * Attack: ``
  * Evidence: `text/html`
  * Other Info: ``
* URL: http://localhost:5000/openstack/latest/meta_data.json
  * Node Name: `http://localhost:5000/openstack/latest/meta_data.json`
  * Method: `DELETE`
  * Parameter: ``
  * Attack: ``
  * Evidence: `text/html`
  * Other Info: ``
* URL: http://localhost:5000
  * Node Name: `http://localhost:5000`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `text/html`
  * Other Info: ``
* URL: http://localhost:5000/
  * Node Name: `http://localhost:5000/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `text/html`
  * Other Info: ``
* URL: http://localhost:5000/3302048830088419775
  * Node Name: `http://localhost:5000/3302048830088419775`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `text/html`
  * Other Info: ``
* URL: http://localhost:5000/api
  * Node Name: `http://localhost:5000/api`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `text/html`
  * Other Info: ``
* URL: http://localhost:5000/api/
  * Node Name: `http://localhost:5000/api/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `text/html`
  * Other Info: ``
* URL: http://localhost:5000/api/1182079131424234075
  * Node Name: `http://localhost:5000/api/1182079131424234075`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `text/html`
  * Other Info: ``
* URL: http://localhost:5000/api/users%3Fname=5%253BURL%253D%2527https%253A%252F%252F6543469631144477992.owasp.org%2527&limit=10&offset=0
  * Node Name: `http://localhost:5000/api/users (limit,name,offset)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `text/html`
  * Other Info: ``
* URL: http://localhost:5000/api/users/
  * Node Name: `http://localhost:5000/api/users/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `text/html`
  * Other Info: ``
* URL: http://localhost:5000/api/users/956828164042614943
  * Node Name: `http://localhost:5000/api/users/956828164042614943`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `text/html`
  * Other Info: ``
* URL: http://localhost:5000/api/users/actuator/health
  * Node Name: `http://localhost:5000/api/users/actuator/health`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `text/html`
  * Other Info: ``
* URL: http://localhost:5000/openapi.json/
  * Node Name: `http://localhost:5000/openapi.json/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `text/html`
  * Other Info: ``
* URL: http://localhost:5000/users
  * Node Name: `http://localhost:5000/users`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `text/html`
  * Other Info: ``
* URL: http://localhost:5000/users/
  * Node Name: `http://localhost:5000/users/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `text/html`
  * Other Info: ``
* URL: http://localhost:5000/api/users/
  * Node Name: `http://localhost:5000/api/users/ ()({name,email})`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `text/html`
  * Other Info: ``


Instances: 22

### Solution



### Reference




#### Source ID: 4

### [ X-Content-Type-Options Header Missing ](https://www.zaproxy.org/docs/alerts/10021/)



##### Low (Medium)

### Description

The Anti-MIME-Sniffing header X-Content-Type-Options was not set to 'nosniff'. This allows older versions of Internet Explorer and Chrome to perform MIME-sniffing on the response body, potentially causing the response body to be interpreted and displayed as a content type other than the declared content type. Current (early 2014) and legacy versions of Firefox will use the declared content type (if one is set), rather than performing MIME-sniffing.

* URL: http://localhost:5000/api/users/1
  * Node Name: `http://localhost:5000/api/users/1`
  * Method: `DELETE`
  * Parameter: `x-content-type-options`
  * Attack: ``
  * Evidence: ``
  * Other Info: `This issue still applies to error type pages (401, 403, 500, etc.) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.
At "High" threshold this scan rule will not alert on client or server error responses.`
* URL: http://localhost:5000/api/users%3Fname=user_abc&limit=10&offset=0
  * Node Name: `http://localhost:5000/api/users (limit,name,offset)`
  * Method: `GET`
  * Parameter: `x-content-type-options`
  * Attack: ``
  * Evidence: ``
  * Other Info: `This issue still applies to error type pages (401, 403, 500, etc.) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.
At "High" threshold this scan rule will not alert on client or server error responses.`
* URL: http://localhost:5000/openapi.json
  * Node Name: `http://localhost:5000/openapi.json`
  * Method: `GET`
  * Parameter: `x-content-type-options`
  * Attack: ``
  * Evidence: ``
  * Other Info: `This issue still applies to error type pages (401, 403, 500, etc.) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.
At "High" threshold this scan rule will not alert on client or server error responses.`
* URL: http://localhost:5000/users
  * Node Name: `http://localhost:5000/users`
  * Method: `GET`
  * Parameter: `x-content-type-options`
  * Attack: ``
  * Evidence: ``
  * Other Info: `This issue still applies to error type pages (401, 403, 500, etc.) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.
At "High" threshold this scan rule will not alert on client or server error responses.`
* URL: http://localhost:5000/api/users
  * Node Name: `http://localhost:5000/api/users ()({name,email})`
  * Method: `POST`
  * Parameter: `x-content-type-options`
  * Attack: ``
  * Evidence: ``
  * Other Info: `This issue still applies to error type pages (401, 403, 500, etc.) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.
At "High" threshold this scan rule will not alert on client or server error responses.`


Instances: 5

### Solution

Ensure that the application/web server sets the Content-Type header appropriately, and that it sets the X-Content-Type-Options header to 'nosniff' for all web pages.
If possible, ensure that the end user uses a standards-compliant and modern web browser that does not perform MIME-sniffing at all, or that can be directed by the web application/web server to not perform MIME-sniffing.

### Reference


* [ https://learn.microsoft.com/en-us/previous-versions/windows/internet-explorer/ie-developer/compatibility/gg622941(v=vs.85) ](https://learn.microsoft.com/en-us/previous-versions/windows/internet-explorer/ie-developer/compatibility/gg622941(v=vs.85))
* [ https://owasp.org/www-community/Security_Headers ](https://owasp.org/www-community/Security_Headers)


#### CWE Id: [ 693 ](https://cwe.mitre.org/data/definitions/693.html)


#### WASC Id: 15

#### Source ID: 3

### [ A Client Error response code was returned by the server ](https://www.zaproxy.org/docs/alerts/100000/)



##### Informational (High)

### Description

A response code of 404 was returned by the server.
This may indicate that the application is failing to handle unexpected input correctly.
Raised by the 'Alert on HTTP Response Code Error' script

* URL: http://localhost:5000/api/users/1/
  * Node Name: `http://localhost:5000/api/users/1/`
  * Method: `DELETE`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: http://localhost:5000/computeMetadata/v1/
  * Node Name: `http://localhost:5000/computeMetadata/v1/`
  * Method: `DELETE`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: http://localhost:5000/latest/meta-data/
  * Node Name: `http://localhost:5000/latest/meta-data/`
  * Method: `DELETE`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: http://localhost:5000/metadata/instance
  * Node Name: `http://localhost:5000/metadata/instance`
  * Method: `DELETE`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: http://localhost:5000/metadata/v1
  * Node Name: `http://localhost:5000/metadata/v1`
  * Method: `DELETE`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: http://localhost:5000/opc/v1/instance/
  * Node Name: `http://localhost:5000/opc/v1/instance/`
  * Method: `DELETE`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: http://localhost:5000/opc/v2/instance/
  * Node Name: `http://localhost:5000/opc/v2/instance/`
  * Method: `DELETE`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: http://localhost:5000/openstack/latest/meta_data.json
  * Node Name: `http://localhost:5000/openstack/latest/meta_data.json`
  * Method: `DELETE`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: http://localhost:5000
  * Node Name: `http://localhost:5000`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: http://localhost:5000/
  * Node Name: `http://localhost:5000/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: http://localhost:5000/3302048830088419775
  * Node Name: `http://localhost:5000/3302048830088419775`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: http://localhost:5000/api
  * Node Name: `http://localhost:5000/api`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: http://localhost:5000/api/
  * Node Name: `http://localhost:5000/api/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: http://localhost:5000/api/1182079131424234075
  * Node Name: `http://localhost:5000/api/1182079131424234075`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: http://localhost:5000/api/users/
  * Node Name: `http://localhost:5000/api/users/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: http://localhost:5000/api/users/956828164042614943
  * Node Name: `http://localhost:5000/api/users/956828164042614943`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `405`
  * Other Info: ``
* URL: http://localhost:5000/api/users/actuator/health
  * Node Name: `http://localhost:5000/api/users/actuator/health`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: http://localhost:5000/openapi.json/
  * Node Name: `http://localhost:5000/openapi.json/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: http://localhost:5000/users/
  * Node Name: `http://localhost:5000/users/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: http://localhost:5000/api/users/
  * Node Name: `http://localhost:5000/api/users/ ()({name,email})`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``


Instances: 20

### Solution



### Reference



#### CWE Id: [ 388 ](https://cwe.mitre.org/data/definitions/388.html)


#### WASC Id: 20

#### Source ID: 4

### [ Non-Storable Content ](https://www.zaproxy.org/docs/alerts/10049/)



##### Informational (Medium)

### Description

The response contents are not storable by caching components such as proxy servers. If the response does not contain sensitive, personal or user-specific information, it may benefit from being stored and cached, to improve performance.

* URL: http://localhost:5000/api/users/1
  * Node Name: `http://localhost:5000/api/users/1`
  * Method: `DELETE`
  * Parameter: ``
  * Attack: ``
  * Evidence: `DELETE `
  * Other Info: ``
* URL: http://localhost:5000/api/users
  * Node Name: `http://localhost:5000/api/users ()({name,email})`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `201`
  * Other Info: ``


Instances: 2

### Solution

The content may be marked as storable by ensuring that the following conditions are satisfied:
The request method must be understood by the cache and defined as being cacheable ("GET", "HEAD", and "POST" are currently defined as cacheable)
The response status code must be understood by the cache (one of the 1XX, 2XX, 3XX, 4XX, or 5XX response classes are generally understood)
The "no-store" cache directive must not appear in the request or response header fields
For caching by "shared" caches such as "proxy" caches, the "private" response directive must not appear in the response
For caching by "shared" caches such as "proxy" caches, the "Authorization" header field must not appear in the request, unless the response explicitly allows it (using one of the "must-revalidate", "public", or "s-maxage" Cache-Control response directives)
In addition to the conditions above, at least one of the following conditions must also be satisfied by the response:
It must contain an "Expires" header field
It must contain a "max-age" response directive
For "shared" caches such as "proxy" caches, it must contain a "s-maxage" response directive
It must contain a "Cache Control Extension" that allows it to be cached
It must have a status code that is defined as cacheable by default (200, 203, 204, 206, 300, 301, 404, 405, 410, 414, 501).

### Reference


* [ https://datatracker.ietf.org/doc/html/rfc7234 ](https://datatracker.ietf.org/doc/html/rfc7234)
* [ https://datatracker.ietf.org/doc/html/rfc7231 ](https://datatracker.ietf.org/doc/html/rfc7231)
* [ https://www.w3.org/Protocols/rfc2616/rfc2616-sec13.html ](https://www.w3.org/Protocols/rfc2616/rfc2616-sec13.html)


#### CWE Id: [ 524 ](https://cwe.mitre.org/data/definitions/524.html)


#### WASC Id: 13

#### Source ID: 3

### [ Storable and Cacheable Content ](https://www.zaproxy.org/docs/alerts/10049/)



##### Informational (Medium)

### Description

The response contents are storable by caching components such as proxy servers, and may be retrieved directly from the cache, rather than from the origin server by the caching servers, in response to similar requests from other users. If the response data is sensitive, personal or user-specific, this may result in sensitive information being leaked. In some cases, this may even result in a user gaining complete control of the session of another user, depending on the configuration of the caching components in use in their environment. This is primarily an issue where "shared" caching servers such as "proxy" caches are configured on the local network. This configuration is typically found in corporate or educational environments, for instance.

* URL: http://localhost:5000/api/users%3Fname=user_abc&limit=10&offset=0
  * Node Name: `http://localhost:5000/api/users (limit,name,offset)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: `In the absence of an explicitly specified caching lifetime directive in the response, a liberal lifetime heuristic of 1 year was assumed. This is permitted by rfc7234.`
* URL: http://localhost:5000/users
  * Node Name: `http://localhost:5000/users`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: `In the absence of an explicitly specified caching lifetime directive in the response, a liberal lifetime heuristic of 1 year was assumed. This is permitted by rfc7234.`


Instances: 2

### Solution

Validate that the response does not contain sensitive, personal or user-specific information. If it does, consider the use of the following HTTP response headers, to limit, or prevent the content being stored and retrieved from the cache by another user:
Cache-Control: no-cache, no-store, must-revalidate, private
Pragma: no-cache
Expires: 0
This configuration directs both HTTP 1.0 and HTTP 1.1 compliant caching servers to not store the response, and to not retrieve the response (without validation) from the cache, in response to a similar request.

### Reference


* [ https://datatracker.ietf.org/doc/html/rfc7234 ](https://datatracker.ietf.org/doc/html/rfc7234)
* [ https://datatracker.ietf.org/doc/html/rfc7231 ](https://datatracker.ietf.org/doc/html/rfc7231)
* [ https://www.w3.org/Protocols/rfc2616/rfc2616-sec13.html ](https://www.w3.org/Protocols/rfc2616/rfc2616-sec13.html)


#### CWE Id: [ 524 ](https://cwe.mitre.org/data/definitions/524.html)


#### WASC Id: 13

#### Source ID: 3

### [ Storable but Non-Cacheable Content ](https://www.zaproxy.org/docs/alerts/10049/)



##### Informational (Medium)

### Description

The response contents are storable by caching components such as proxy servers, but will not be retrieved directly from the cache, without validating the request upstream, in response to similar requests from other users.

* URL: http://localhost:5000/openapi.json
  * Node Name: `http://localhost:5000/openapi.json`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `no-cache`
  * Other Info: ``


Instances: 1

### Solution



### Reference


* [ https://datatracker.ietf.org/doc/html/rfc7234 ](https://datatracker.ietf.org/doc/html/rfc7234)
* [ https://datatracker.ietf.org/doc/html/rfc7231 ](https://datatracker.ietf.org/doc/html/rfc7231)
* [ https://www.w3.org/Protocols/rfc2616/rfc2616-sec13.html ](https://www.w3.org/Protocols/rfc2616/rfc2616-sec13.html)


#### CWE Id: [ 524 ](https://cwe.mitre.org/data/definitions/524.html)


#### WASC Id: 13

#### Source ID: 3


