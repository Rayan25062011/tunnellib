# tunnellib
Library that will make secure connection to your website to stops hackers to steal your passwords and your IP 


# Install
```
git clone https://github.com/Rayan25062011/tunnellib
```
# Examples
Secured connection:
```python
from tunnellib import tunnellib

secure_redirect = tunnellib(web='http://example.com')
print("Establishing secure connection...")
secure_redirect.secure_connection()
```

Default connection(Not secured):
```python
from tunnellib import tunnellib

unsecure_redirect = tunnellib(web='http://example.com')
print("Establishing default connection...")
unsecure_redirect.unsecure_connection()
```
Check if website is dangerous:
```python
from tunnellib import tunnellib

is_dangerous = tunnellib(web='http://example.com')
print("Checking...")
is_dangerous.is_dangerous()
```
# Accepting contributors
If you would like to join the team, just ask! I will only be accepting the minimum of 60 contributors! I would be very happy, thank you.
