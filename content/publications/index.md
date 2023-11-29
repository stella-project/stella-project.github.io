---
title: STELLA Publications
---

{{< test.inline >}}

{{ $file := "/static/stella_pubs/stella.html" | readFile }}
{{ (print $file) | markdownify }}

{{< /test.inline >}}



{{< test.inline >}}

{{ $file := "/static/stella_pubs/scripts.html" | readFile }}
{{ (print $file) | markdownify }}

{{< /test.inline >}}
