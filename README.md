# whatsonthemenu

Python interface to [NYPL's What's on The Menu API](https://github.com/NYPL/menus-api).

## Installation

### From PyPI

```bash
pip install whatsonthemenu
```

### From source

```bash
git clone https://github.com/hugovk/whatsonthemenu.git
python setup.py install
```

## Example use

First, you need to ask NYPL for a token: https://github.com/NYPL/menus-api#tokens

Return values are the JSON responses documented in the API: https://github.com/NYPL/menus-api#menus

```python
from whatsonthemenu import WhatsOnTheMenu
from pprint import pprint

# Initialise the API with your token
api = WhatsOnTheMenu(token)

# # Get all menus
menus = api.get_menus(min_year=1950, max_year=1951)
# # Pick the first menu
print(menus)
menu = menus['menus'][0]
pprint(menu)

# Get a certain menu
menu = api.get_menus_id(30924)
pprint(menu)

# Get pages from a certain menu
pages = api.get_menus_id_pages(30924)
pprint(pages)

# Get dishes from a certain menu
dishes = api.get_menus_id_dishes(30924)
pprint(dishes)

# Search for meatballs
dishes = api.get_dishes_search("meatballs", per_page=20, page=2)
pprint(dishes)

# Show rate limit
print("Rate limit remaining: ", api.rate_limit_remaining())
```

## See also

The [open-source Menu Bot](https://github.com/hugovk/menubot) uses this API. See it in action on [Twitter](https://twitter.com/menubot) and [Tumblr](http://menubot.tumblr.com/).
