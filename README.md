# About Pyclash
A simple Python wrapper for Clash Of Clans.

## ⚙️Installation

```bash
pip install https://github.com/1Doomdie1/PyClash.git
```

## 🔄 Usage
### Get Player Data
```python
from pyclash import PlayersAPI

playersApi = PlayersAPI("[YOUR-API-KEY]")
playerInfo = playersApi.info(playerTag = "#[PLAYER-TAG]")

```

### Disabling SSL verification
There are cases when SSL verification can pose a problem in making a request to Tines REST API, fortunately
there is an easy way of disabling SSL verification in Tapi. Here is how:

```python
from pyclash.utils.http import disable_ssl_verification

disable_ssl_verification()
```

## Classes