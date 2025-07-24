# About PyClash
A simple Python wrapper for Clash Of Clans.

## ⚙️Installation

```bash
pip install https://github.com/1Doomdie1/PyClash.git
```

## 🔄 Usage

### Using main Clash class
```python
from pyclash import Clash

clash = Clash("[YOUR-API-KEY]")
clan = clash.clan.get(clanTag = "#[CLAN-TAG]")

print(clan.model_dump_json(indent = 4))
```

### Disabling SSL verification
There are cases when SSL verification can pose a problem in making a request to Tines REST API, fortunately
there is an easy way of disabling SSL verification in Tapi. Here is how:

```python
from pyclash.utils.http import disable_ssl_verification

disable_ssl_verification()
```

## Classes

<details>
<summary>Clash</summary>
This class acts as the main wrapper for the API through which all endpoints can be accessed.

### Attributes
| **Attribute** | **Description**                     |
|---------------|-------------------------------------|
| `clans`       | Access clan specific information.   |
| `labels`      | N/A                                 |
| `players`     | Access player specific information. |
| `leagues`     | Access league information.          |
| `goldpass`    | Access information about gold pass. |
| `locations`   | Access global and local rankings.   |

### Usage:
```python
from pyclash import Clash

def main():
    clash = Clash("[YOUR-API-KEY]")
    playerInfo = clash.players.get_payer_info(playerTag = "#[PLAYER-TAG]")

if __name__ == "__main__":
    main()
```

</details>

<details>
<summary>PlayersAPI</summary>
Access player specific information.

### Methods

| **Method**          | **Description**                                                 |
|---------------------|---------------------------------------------------------------- |
| `get_payer_info`    | Get player information.                                         |
| `verify_payer_token`| Verify player API token that can be found in the game settings. |

### Usage:
```python
from pyclash import PlayersAPI

def main():
    api = PlayersAPI("[YOUR-API-KEY]")
    playerInfo = api.get_player_info(playerTag = "#[PLAYER-TAG]")

if __name__ == "__main__":
    main()
```

</details>

<details>
<summary>ClansAPI</summary>
Access clan specific information.

### Methods

| **Method**            | **Description**                                    |
|-----------------------|----------------------------------------------------|
| `list`                | Search clans.                                      |
| `get`                 | Get clan info.                                     |
| `members`             | List clan members.                                 |
| `capital_raid_seasons`| Retrive clan's capital raid seasons.               |
| `current_war`         | Retrive information about clan's current clan war. |
| `war_log`             | Retrieve clan's clan war log.                      |

### Usage:
```python
from pyclash import ClansAPI

def main():
    clanApi = ClansAPI("[YOUR-API-KEY]")
    clanInfo = clanApi.get(clanTag = "#[CLAN-TAG]")

if __name__ == "__main__":
    main()
```

</details>

<details>
<summary>LeaguesAPI</summary>
Access league information.

### Methods

| **Method**             | **Description**                                                                                      |
|------------------------|------------------------------------------------------------------------------------------------------|
| `leagues`              | List leagues.                                                                                        |
| `league`               | Get league information.                                                                              |
| `capital_leagues`      | List capital leagues.                                                                                |
| `capital_league`       | Get capital league information.                                                                      |
| `league_seasons`       | Get league seasons. Note that league season information is available only for Legend League.         |
| `league_season`        | Get league season rankings. Note that league season information is available only for Legend League. |
| `builder_base_leagues` | List Builder Base leagues.                                                                           |
| `builder_base_league`  | Get Builder Base league information.                                                                 |
| `war_leagues`          | List war leagues.                                                                                    |
| `war_league`           | Get war league information.                                                                          |

### Usage:
```python
from pyclash import LeaguesAPI

def main():
    leaguesApi = LeaguesAPI("[YOUR-API-KEY]")
    leagueInfo = leaguesApi.league(leagueId = "#[LEAGUE-ID]")

if __name__ == "__main__":
    main()
```

</details>

<details>
<summary>LocationAPI</summary>
Access global and local rankings.

### Methods

| **Method**                      | **Description**                                           |
|---------------------------------|-----------------------------------------------------------|
| `list`                          | List locations.                                           |
| `get`                           | Get information about specific location.                  |
| `capitals_rankings`             | Get capital rankings for a specific location.             |
| `clans_rankings`                | Get clan rankings for a specific location.                |
| `players_rankings`              | Get player rankings for a specific location.              |
| `players_builder_base_rankings` | Get player Builder Base rankings for a specific location. |
| `clans_builder_base_rankings`   | Get clan Builder Base rankings for a specific location.   |

### Usage:
```python
from pyclash import LocationAPI

def main():
    locationApi = LocationAPI("[YOUR-API-KEY]")
    locationInfo = locationApi.get(leagueId = "#[LOCATION-ID]")

if __name__ == "__main__":
    main()
```

</details>

<details>
<summary>GoldPassAPI</summary>
Access information about gold pass.

### Methods

| **Method** | **Description**                                     |
|------------|-----------------------------------------------------|
| `info`     | Get information about the current gold pass season. |

### Usage:
```python
from pyclash import GoldPassAPI

def main():
    goldpassApi = GoldPassAPI("[YOUR-API-KEY]")
    goldpassInfo = goldpassApi.info()

if __name__ == "__main__":
    main()
```

</details>

</details>

<details>
<summary>LabelsAPI</summary>
N/A

### Methods

| **Method** | **Description**     |
|------------|---------------------|
| `players`  | List player labels. |
| `clans`    | List clan labels.   |

### Usage:
```python
from pyclash import LabelsAPI

def main():
    labelsApi = LabelsAPI("[YOUR-API-KEY]")
    playerLabelsInfo = labelsApi.players()

if __name__ == "__main__":
    main()
```

</details>